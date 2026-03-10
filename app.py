"""
AdaptEd — Streamlit version
Adaptation de contenu pédagogique pour les élèves à besoins éducatifs particuliers.
"""

import os
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

import anthropic
import markdown as md
import streamlit as st

from prompts.builder import build_system_prompt, build_user_prompt
from visuals import prepare_image_for_api, preprocess_visual_blocks, process_visual_content
from document import (
    extract_docx_content,
    extract_pdf_content,
    build_marked_text,
    rebuild_docx,
    rebuild_html_with_images,
)

# ---------------------------------------------------------------------------
# Constants (ported from constants.ts)
# ---------------------------------------------------------------------------

PROFILE_LABELS: dict[str, dict] = {
    "DYSLEXIA": {"label": "Dyslexie", "emoji": "📖", "description": "Trouble de la lecture et du décodage"},
    "DYSORTHOGRAPHIA": {"label": "Dysorthographie", "emoji": "✏️", "description": "Trouble de l'orthographe et de l'écriture"},
    "DYSPRAXIA": {"label": "Dyspraxie", "emoji": "🤲", "description": "Trouble de la coordination motrice"},
    "ADHD": {"label": "TDAH", "emoji": "⚡", "description": "Trouble de l'attention avec ou sans hyperactivité"},
    "DYSCALCULIA": {"label": "Dyscalculie", "emoji": "🔢", "description": "Trouble du calcul et du raisonnement logico-mathématique"},
    "ALLOPHONE": {"label": "Allophone", "emoji": "🌍", "description": "Français langue seconde"},
    "GIFTED": {"label": "Haut Potentiel", "emoji": "🚀", "description": "Enrichissement et approfondissement"},
    "CUSTOM": {"label": "Personnalisé", "emoji": "🎯", "description": "Profil sur mesure"},
}

CONTENT_TYPE_LABELS: dict[str, str] = {
    "EXERCISE": "Exercice",
    "EVALUATION": "Évaluation",
    "LESSON": "Leçon / Cours",
    "INSTRUCTION": "Consigne",
    "TEXT": "Texte documentaire",
    "WORKSHEET": "Fiche de travail",
    "OTHER": "Autre",
}

SCHOOL_LEVEL_LABELS: dict[str, str] = {
    "CP": "CP",
    "CE1": "CE1",
    "CE2": "CE2",
    "CM1": "CM1",
    "CM2": "CM2",
    "SIXIEME": "6ème",
    "CINQUIEME": "5ème",
    "QUATRIEME": "4ème",
    "TROISIEME": "3ème",
    "SECONDE": "2nde",
    "PREMIERE": "1ère",
    "TERMINALE": "Terminale",
    "POST_BAC": "Post-bac",
    "OTHER": "Autre",
}

# CSS for rendered HTML
ADAPTED_CSS = """
<style>
    .adapted-content {
        font-family: Arial, Helvetica, sans-serif;
        line-height: 1.7;
        color: #1e293b;
        max-width: 100%;
        overflow-x: auto;
    }
    .adapted-content h1, .adapted-content h2, .adapted-content h3 {
        color: #1e40af;
        margin-top: 1.2em;
        margin-bottom: 0.5em;
    }
    .adapted-content h2 { border-bottom: 2px solid #bfdbfe; padding-bottom: 0.3em; }
    .adapted-content blockquote {
        border-left: 4px solid #3b82f6;
        background: #eff6ff;
        padding: 0.8em 1em;
        margin: 1em 0;
        border-radius: 0 8px 8px 0;
    }
    .adapted-content table {
        border-collapse: collapse;
        width: 100%;
        margin: 1em 0;
    }
    .adapted-content th, .adapted-content td {
        border: 1px solid #cbd5e1;
        padding: 8px 12px;
        text-align: left;
    }
    .adapted-content th { background: #f1f5f9; font-weight: 600; }
    .adapted-content tr:nth-child(even) { background: #f8fafc; }
    .adapted-content .adapted-figure {
        text-align: center;
        margin: 1.5em auto;
        max-width: 100%;
    }
    .adapted-content .adapted-figure svg {
        max-width: 100%;
        height: auto;
    }
    .adapted-content .original-figure img {
        max-width: 100%;
        height: auto;
        border: 1px solid #e2e8f0;
        border-radius: 8px;
    }
    .adapted-content hr { border: none; border-top: 2px solid #e2e8f0; margin: 1.5em 0; }
    .adapted-content ul, .adapted-content ol { padding-left: 1.5em; }
    .adapted-content li { margin-bottom: 0.3em; }
    .adapted-content code {
        background: #f1f5f9;
        padding: 2px 6px;
        border-radius: 4px;
        font-size: 0.9em;
    }
    .adapted-content pre {
        background: #f8fafc;
        padding: 1em;
        border-radius: 8px;
        overflow-x: auto;
    }
</style>
"""

# ---------------------------------------------------------------------------
# Page config
# ---------------------------------------------------------------------------

st.set_page_config(
    page_title="AdaptEd — Adaptation de contenu",
    page_icon="🎓",
    layout="wide",
)

# ---------------------------------------------------------------------------
# Session state init
# ---------------------------------------------------------------------------

if "results" not in st.session_state:
    st.session_state.results = {}
if "generating" not in st.session_state:
    st.session_state.generating = False
if "document_blocks" not in st.session_state:
    st.session_state.document_blocks = None
if "input_mode" not in st.session_state:
    st.session_state.input_mode = "text_input"

# ---------------------------------------------------------------------------
# Sidebar
# ---------------------------------------------------------------------------

with st.sidebar:
    st.title("🎓 AdaptEd")
    st.caption("Adaptation de contenu pédagogique")
    st.divider()

    # API Key: secrets > env var > manual input
    _default_key = ""
    try:
        _default_key = st.secrets["ANTHROPIC_API_KEY"]
    except (KeyError, FileNotFoundError):
        _default_key = os.environ.get("ANTHROPIC_API_KEY", "")

    if _default_key:
        api_key = _default_key
        st.success("Clé API configurée ✓")
    else:
        api_key = st.text_input(
            "Clé API Anthropic",
            type="password",
            help="Votre clé API Anthropic (sk-ant-...).",
        )

    st.divider()

    # Content type
    content_type_options = list(CONTENT_TYPE_LABELS.keys())
    content_type_display = list(CONTENT_TYPE_LABELS.values())
    content_type_idx = st.selectbox(
        "Type de contenu",
        range(len(content_type_options)),
        format_func=lambda i: content_type_display[i],
        index=0,
    )
    content_type = content_type_options[content_type_idx]

    # School level
    level_options = [""] + list(SCHOOL_LEVEL_LABELS.keys())
    level_display = ["— Non précisé —"] + list(SCHOOL_LEVEL_LABELS.values())
    level_idx = st.selectbox(
        "Niveau scolaire",
        range(len(level_options)),
        format_func=lambda i: level_display[i],
        index=0,
    )
    level = level_options[level_idx] or None

    # Subject
    subject = st.text_input("Matière", placeholder="ex : Mathématiques, Français, SVT...")

    st.divider()

    # Profiles
    st.subheader("Profils d'adaptation")
    profile_options = list(PROFILE_LABELS.keys())
    selected_profiles: list[str] = []
    for key in profile_options:
        info = PROFILE_LABELS[key]
        if st.checkbox(
            f"{info['emoji']} {info['label']}",
            key=f"profile_{key}",
            help=info["description"],
        ):
            selected_profiles.append(key)

    # Custom profile description
    custom_description = None
    if "CUSTOM" in selected_profiles:
        custom_description = st.text_area(
            "Description du profil personnalisé",
            placeholder="Décrivez les besoins spécifiques de l'élève...",
            height=100,
        )

    st.divider()

    # Model selection
    model_choice = st.selectbox(
        "Modèle Claude",
        ["claude-sonnet-4-5-20250929", "claude-haiku-4-5-20251001"],
        format_func=lambda m: "Sonnet 4.5 (recommandé)" if "sonnet" in m else "Haiku 4.5 (rapide)",
        index=0,
    )

# ---------------------------------------------------------------------------
# Main area — Input mode selection
# ---------------------------------------------------------------------------

st.header("Contenu à adapter")

input_mode = st.radio(
    "Mode de saisie",
    ["text_input", "file_upload"],
    format_func=lambda m: {
        "text_input": "📝 Texte (coller + photos optionnelles)",
        "file_upload": "📄 Fichier Word ou PDF",
    }[m],
    horizontal=True,
)

original_content = ""
uploaded_images = None
document_blocks = None
figure_mode = "generate"

if input_mode == "text_input":
    # --- Text + photos mode (original flow) ---
    original_content = st.text_area(
        "Collez ici le contenu pédagogique original",
        height=250,
        placeholder="Collez ici un exercice, une évaluation, une leçon, un texte...\n\nMinimum 10 caractères.",
    )

    uploaded_images = st.file_uploader(
        "Images (optionnel) — photos d'exercices, pages scannées...",
        accept_multiple_files=True,
        type=["png", "jpg", "jpeg", "gif", "webp"],
    )
    figure_mode = "generate"

else:
    # --- File upload mode (new flow) ---
    uploaded_file = st.file_uploader(
        "Fichier Word (.docx) ou PDF (.pdf)",
        accept_multiple_files=False,
        type=["docx", "pdf"],
    )

    if uploaded_file:
        file_bytes = uploaded_file.read()
        try:
            if uploaded_file.name.lower().endswith(".docx"):
                document_blocks = extract_docx_content(file_bytes)
            elif uploaded_file.name.lower().endswith(".pdf"):
                document_blocks = extract_pdf_content(file_bytes)

            if document_blocks:
                st.session_state.document_blocks = document_blocks

                text_count = sum(1 for b in document_blocks if b.type == "text")
                image_count = sum(1 for b in document_blocks if b.type == "image")
                st.success(f"Extraction réussie : {text_count} bloc(s) de texte, {image_count} image(s) détectée(s)")

                with st.expander("Aperçu du contenu extrait"):
                    for block in document_blocks:
                        if block.type == "text":
                            preview = block.text[:300] + ("..." if len(block.text) > 300 else "")
                            st.text(preview)
                        else:
                            st.image(block.image_bytes, caption=f"Image {block.image_index + 1}", width=300)

                original_content = build_marked_text(document_blocks)
                figure_mode = "preserve"
            else:
                st.warning("Aucun contenu extrait du fichier.")
        except Exception as e:
            st.error(f"Erreur lors de l'extraction : {e}")

# ---------------------------------------------------------------------------
# Generation
# ---------------------------------------------------------------------------


def generate_one(
    client: anthropic.Anthropic,
    profile_type: str,
    original_content: str,
    content_type: str,
    level: str | None,
    subject: str | None,
    images: list[dict],
    model: str,
    custom_description: str | None,
    figure_mode: str = "generate",
) -> dict:
    """Generate adaptation for a single profile. Runs in a thread."""
    system_prompt = build_system_prompt(
        profile_type, content_type, level, custom_description,
        figure_mode=figure_mode,
    )
    user_prompt = build_user_prompt(original_content, content_type, level, subject)

    # Build message content
    if images:
        content_blocks = []
        for img in images:
            content_blocks.append({
                "type": "image",
                "source": {
                    "type": "base64",
                    "media_type": img["media_type"],
                    "data": img["base64"],
                },
            })
        content_blocks.append({
            "type": "text",
            "text": f"Les images ci-dessus montrent le contenu pédagogique original à adapter. Analyse-les en détail et intègre fidèlement leur contenu.\n\n{user_prompt}",
        })
        message_content = content_blocks
    else:
        message_content = user_prompt

    start = time.time()
    response = client.messages.create(
        model=model,
        max_tokens=12000,
        system=system_prompt,
        messages=[{"role": "user", "content": message_content}],
    )
    duration = time.time() - start

    raw_md = response.content[0].text if response.content[0].type == "text" else ""

    # Process visual blocks then convert to HTML
    preprocessed = preprocess_visual_blocks(raw_md)
    raw_html = md.markdown(
        preprocessed,
        extensions=["tables", "fenced_code", "nl2br"],
    )
    final_html = process_visual_content(raw_html)

    return {
        "profile": profile_type,
        "markdown": raw_md,
        "html": final_html,
        "tokens": response.usage.output_tokens,
        "duration": round(duration, 1),
        "model": model,
    }


# Generate button
col1, col2 = st.columns([1, 3])
with col1:
    generate_clicked = st.button(
        "🚀 Adapter",
        type="primary",
        use_container_width=True,
        disabled=st.session_state.generating,
    )

# Validation & generation
if generate_clicked:
    # Validate inputs
    errors = []
    if not api_key:
        errors.append("Veuillez saisir votre clé API Anthropic dans la barre latérale.")
    if input_mode == "file_upload" and not document_blocks:
        errors.append("Veuillez uploader un fichier Word ou PDF valide.")
    elif not original_content or len(original_content.strip()) < 10:
        errors.append("Le contenu doit faire au moins 10 caractères.")
    if len(original_content or "") > 50000:
        errors.append("Le contenu ne doit pas dépasser 50 000 caractères.")
    if not selected_profiles:
        errors.append("Sélectionnez au moins un profil dans la barre latérale.")

    if errors:
        for err in errors:
            st.error(err)
    else:
        st.session_state.generating = True
        st.session_state.results = {}
        st.session_state.input_mode = input_mode

        # Prepare images (only for text+photo mode)
        prepared_images: list[dict] = []
        if input_mode == "text_input" and uploaded_images:
            for f in uploaded_images:
                prepared = prepare_image_for_api(f.read(), f.type)
                prepared_images.append(prepared)

        client = anthropic.Anthropic(api_key=api_key)

        progress_bar = st.progress(0, text="Génération en cours...")
        status_container = st.empty()

        results: dict[str, dict] = {}
        total = len(selected_profiles)
        completed_count = 0

        with ThreadPoolExecutor(max_workers=min(total, 4)) as executor:
            futures = {
                executor.submit(
                    generate_one,
                    client,
                    profile,
                    original_content,
                    content_type,
                    level,
                    subject or None,
                    prepared_images,
                    model_choice,
                    custom_description,
                    figure_mode,
                ): profile
                for profile in selected_profiles
            }

            for future in as_completed(futures):
                profile = futures[future]
                label = PROFILE_LABELS[profile]
                try:
                    result = future.result()
                    results[profile] = result
                    completed_count += 1
                    progress_bar.progress(
                        completed_count / total,
                        text=f"{label['emoji']} {label['label']} terminé ({completed_count}/{total})",
                    )
                except Exception as e:
                    results[profile] = {"error": str(e), "profile": profile}
                    completed_count += 1
                    progress_bar.progress(
                        completed_count / total,
                        text=f"Erreur pour {label['label']} ({completed_count}/{total})",
                    )

        progress_bar.empty()
        st.session_state.results = results
        st.session_state.generating = False
        st.rerun()

# ---------------------------------------------------------------------------
# Results display
# ---------------------------------------------------------------------------

if st.session_state.results:
    st.divider()
    st.header("Résultats")

    # Retrieve document blocks for post-processing
    doc_blocks = st.session_state.document_blocks
    is_file_mode = st.session_state.input_mode == "file_upload" and doc_blocks

    # Post-process results if in file mode (replace markers with images)
    if is_file_mode:
        image_blocks = [b for b in doc_blocks if b.type == "image"]
        for key, result in st.session_state.results.items():
            if "error" not in result and image_blocks:
                result["html"] = rebuild_html_with_images(result["html"], image_blocks)
                result["docx_bytes"] = rebuild_docx(doc_blocks, result["markdown"])

    # Build tabs
    results = st.session_state.results
    profile_keys = list(results.keys())
    tab_labels = [
        f"{PROFILE_LABELS[k]['emoji']} {PROFILE_LABELS[k]['label']}" for k in profile_keys
    ]

    tabs = st.tabs(tab_labels)

    for tab, profile_key in zip(tabs, profile_keys):
        with tab:
            result = results[profile_key]

            if "error" in result:
                st.error(f"Erreur : {result['error']}")
                continue

            info = PROFILE_LABELS[profile_key]

            # Stats
            col_a, col_b, col_c = st.columns(3)
            col_a.metric("Tokens", f"{result['tokens']:,}")
            col_b.metric("Durée", f"{result['duration']}s")
            col_c.metric("Modèle", result["model"].split("-")[1].capitalize())

            # Rendered HTML
            st.subheader("Aperçu rendu")
            full_html = f"{ADAPTED_CSS}<div class='adapted-content'>{result['html']}</div>"
            st.html(full_html)

            # Export buttons
            st.divider()
            has_docx = "docx_bytes" in result
            export_cols = st.columns(3 if has_docx else 2)

            # Download complete HTML
            export_html = f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>AdaptEd — {info['label']}</title>
{ADAPTED_CSS}
</head>
<body>
<div class="adapted-content">
{result['html']}
</div>
<script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
<script>mermaid.initialize({{startOnLoad: true}});</script>
</body>
</html>"""

            with export_cols[0]:
                st.download_button(
                    "📥 Exporter HTML",
                    data=export_html,
                    file_name=f"adapted_{profile_key.lower()}.html",
                    mime="text/html",
                    use_container_width=True,
                )

            with export_cols[1]:
                st.download_button(
                    "📝 Exporter Markdown",
                    data=result["markdown"],
                    file_name=f"adapted_{profile_key.lower()}.md",
                    mime="text/markdown",
                    use_container_width=True,
                )

            if has_docx:
                with export_cols[2]:
                    st.download_button(
                        "📄 Exporter Word",
                        data=result["docx_bytes"],
                        file_name=f"adapted_{profile_key.lower()}.docx",
                        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                        use_container_width=True,
                    )

            # Show raw markdown in expander
            with st.expander("Voir le Markdown brut"):
                st.code(result["markdown"], language="markdown")
