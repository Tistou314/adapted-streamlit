"""
Visual content detection and rendering for AdaptEd.

Detects ```tikz, ```svg, and ```mermaid blocks in Claude's response,
and renders them into inline HTML.
"""

import base64
import io
import re
from html import escape as _escape_html

from PIL import Image

MAX_IMAGE_WIDTH = 1500

SUPPORTED_MEDIA_TYPES = {"image/jpeg", "image/png", "image/gif", "image/webp"}


# ---------------------------------------------------------------------------
# HTML helpers
# ---------------------------------------------------------------------------

def escape_html(text: str) -> str:
    return _escape_html(text, quote=True)


def unescape_html(text: str) -> str:
    return (
        text.replace("&amp;", "&")
        .replace("&lt;", "<")
        .replace("&gt;", ">")
        .replace("&quot;", '"')
        .replace("&#39;", "'")
        .replace("&#x27;", "'")
    )


# ---------------------------------------------------------------------------
# Markdown pre-processing (BEFORE markdown conversion)
# ---------------------------------------------------------------------------

def preprocess_visual_blocks(markdown: str) -> str:
    """Replace visual code blocks with rendered HTML before markdown conversion."""
    result = markdown

    # ```svg blocks → inline SVG
    # Anchor on <svg>...</svg> tags instead of relying on closing ```.
    result = re.sub(
        r"```svg\s*\n\s*(<svg[\s\S]*?</svg>)\s*(?:```)?",
        _replace_svg,
        result,
        flags=re.IGNORECASE,
    )

    # ```mermaid blocks → <pre class="mermaid"> for client-side rendering
    result = re.sub(
        r"```mermaid\s*\n([\s\S]*?)```",
        _replace_mermaid,
        result,
    )

    # ```tikz blocks → styled placeholder
    result = re.sub(
        r"```tikz\s*\n([\s\S]*?)```",
        _replace_tikz,
        result,
    )

    return result


def _replace_svg(match: re.Match) -> str:
    svg_code = match.group(1).strip()
    svg_code = re.sub(r"\n\s*\n", "\n", svg_code)
    return f'\n\n<div class="adapted-figure" data-type="svg">{svg_code}</div>\n\n'


def _replace_mermaid(match: re.Match) -> str:
    code = escape_html(match.group(1).strip())
    return f'\n\n<div class="adapted-figure" data-type="mermaid"><pre class="mermaid">{code}</pre></div>\n\n'


def _replace_tikz(match: re.Match) -> str:
    code = escape_html(match.group(1).strip())
    return (
        f'\n\n<div class="adapted-figure" data-type="tikz">'
        f'<div class="tikz-placeholder">'
        f'<p style="margin:0 0 8px;font-weight:600;color:#334155;">Figure TikZ</p>'
        f'<pre style="margin:0;white-space:pre-wrap;font-size:0.85em;">{code}</pre>'
        f"</div></div>\n\n"
    )


# ---------------------------------------------------------------------------
# HTML post-processing (fallback, AFTER markdown conversion)
# ---------------------------------------------------------------------------

def process_visual_content(html: str) -> str:
    """Fallback post-processor for visual code blocks that survived markdown conversion."""
    result = html

    renderers = {
        "svg": lambda code: code.strip(),
        "mermaid": lambda code: f'<pre class="mermaid">{escape_html(code.strip())}</pre>',
        "tikz": lambda code: (
            f'<div class="tikz-placeholder">'
            f'<p style="margin:0 0 8px;font-weight:600;color:#334155;">Figure TikZ</p>'
            f'<pre style="margin:0;white-space:pre-wrap;font-size:0.85em;">{escape_html(code.strip())}</pre>'
            f"</div>"
        ),
    }

    for vtype, renderer in renderers.items():
        pattern = re.compile(
            rf'<pre>\s*<code\s+class="(?:language-|lang-)?{vtype}"[^>]*>([\s\S]*?)</code>\s*</pre>',
            re.IGNORECASE,
        )
        result = pattern.sub(
            lambda m, r=renderer, t=vtype: f'<div class="adapted-figure" data-type="{t}">{r(unescape_html(m.group(1)))}</div>',
            result,
        )

    return result


# ---------------------------------------------------------------------------
# Image preparation for the Anthropic multimodal API
# ---------------------------------------------------------------------------

def prepare_image_for_api(
    file_bytes: bytes, mime_type: str
) -> dict[str, str]:
    """
    Resize image to max MAX_IMAGE_WIDTH px wide and return base64 + media_type
    suitable for the Anthropic API.
    """
    img = Image.open(io.BytesIO(file_bytes))

    # Resize if too wide
    if img.width > MAX_IMAGE_WIDTH:
        ratio = MAX_IMAGE_WIDTH / img.width
        new_size = (MAX_IMAGE_WIDTH, int(img.height * ratio))
        img = img.resize(new_size, Image.LANCZOS)

    # Determine output format
    if mime_type in SUPPORTED_MEDIA_TYPES:
        media_type = mime_type
    else:
        media_type = "image/png"

    fmt_map = {
        "image/jpeg": "JPEG",
        "image/png": "PNG",
        "image/gif": "GIF",
        "image/webp": "WEBP",
    }
    fmt = fmt_map.get(media_type, "PNG")

    # Convert RGBA to RGB for JPEG
    if fmt == "JPEG" and img.mode in ("RGBA", "P"):
        img = img.convert("RGB")

    buf = io.BytesIO()
    img.save(buf, format=fmt)
    b64 = base64.b64encode(buf.getvalue()).decode("ascii")

    return {"base64": b64, "media_type": media_type}
