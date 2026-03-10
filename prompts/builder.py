from .base import BASE_SYSTEM_PROMPT
from .profiles import PROFILE_PROMPTS
from .levels import LEVEL_CONTEXTS
from .content_types import CONTENT_TYPE_CONTEXTS

CONTENT_TYPE_LABELS: dict[str, str] = {
    "EXERCISE": "Exercice",
    "EVALUATION": "Évaluation",
    "LESSON": "Leçon / Cours",
    "INSTRUCTION": "Consigne",
    "TEXT": "Texte documentaire",
    "WORKSHEET": "Fiche de travail",
    "OTHER": "Autre",
}


FIGURE_PRESERVE_INSTRUCTION = """## Figures et images originales

Le document original contient des figures/images identifiées par des marqueurs {{FIGURE_ORIGINALE_N}}.
Tu DOIS :
1. **Conserver ces marqueurs EXACTEMENT tels quels** dans ta sortie (ex: {{FIGURE_ORIGINALE_1}}, {{FIGURE_ORIGINALE_2}}, etc.)
2. **NE PAS les supprimer**, les renommer, les renuméroter ou les déplacer
3. **NE PAS générer de figures SVG, Mermaid ou TikZ** pour remplacer ces images — les images originales seront automatiquement réinsérées
4. Placer chaque marqueur à l'endroit logique dans le texte adapté (même position relative que dans l'original)
5. Tu peux ajouter une brève description textuelle AVANT le marqueur si le profil de l'élève le nécessite (ex: "La figure ci-dessous montre...")

Les images originales seront automatiquement réinsérées à la place de ces marqueurs dans le document final."""


def build_system_prompt(
    profile_type: str,
    content_type: str,
    level: str | None = None,
    custom_description: str | None = None,
    figure_mode: str = "generate",
) -> str:
    parts: list[str] = [BASE_SYSTEM_PROMPT]

    if profile_type == "CUSTOM" and custom_description:
        parts.append(PROFILE_PROMPTS["CUSTOM"])
        parts.append(
            f"\n**Description du profil personnalisé par l'enseignant** :\n{custom_description}"
        )
    else:
        profile_prompt = PROFILE_PROMPTS.get(profile_type)
        if profile_prompt:
            parts.append(profile_prompt)

    if level and level in LEVEL_CONTEXTS:
        parts.append(f"## Contexte du niveau scolaire\n{LEVEL_CONTEXTS[level]}")

    if content_type and content_type in CONTENT_TYPE_CONTEXTS:
        parts.append(
            f"## Contexte du type de contenu\n{CONTENT_TYPE_CONTEXTS[content_type]}"
        )

    if figure_mode == "preserve":
        parts.append(FIGURE_PRESERVE_INSTRUCTION)

    return "\n\n---\n\n".join(parts)


def build_user_prompt(
    original_content: str,
    content_type: str,
    level: str | None = None,
    subject: str | None = None,
) -> str:
    level_label = level or "Non précisé"
    subject_label = subject or "Non précisée"
    type_label = CONTENT_TYPE_LABELS.get(content_type, content_type)

    return f"""## Contenu pédagogique à adapter

**Type** : {type_label}
**Niveau** : {level_label}
**Matière** : {subject_label}

---

{original_content}"""
