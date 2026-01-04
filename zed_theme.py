"""Generate a Zed editor theme based on the FT palette."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, Iterable

from ft_palette import INVERSE_THEME, STANDARD_THEME, ThemeDefinition, get_color

SCHEMA_URL = "https://zed.dev/schema/themes/v0.2.0.json"


def hex_rgba(color: str, alpha: float = 1.0) -> str:
    """Convert hex color to RGBA with alpha channel."""
    color = color.lstrip("#")
    if len(color) == 8:
        return f"#{color}" if color[6:8].lower() != "ff" else f"#{color[:6]}"
    if alpha >= 1.0:
        return f"#{color}ff"
    a = max(0, min(255, round(alpha * 255)))
    return f"#{color}{a:02x}"


def mix(color_a: str, color_b: str, amount: float) -> str:
    """Mix two colors together."""
    amount = max(0.0, min(1.0, amount))
    color_a = color_a.lstrip("#")
    color_b = color_b.lstrip("#")
    ar, ag, ab = (int(color_a[i : i + 2], 16) for i in (0, 2, 4))
    br, bg, bb = (int(color_b[i : i + 2], 16) for i in (0, 2, 4))
    rr = round(ar + (br - ar) * amount)
    rg = round(ag + (bg - ag) * amount)
    rb = round(ab + (bb - ab) * amount)
    return f"#{rr:02x}{rg:02x}{rb:02x}"


def build_style(theme: ThemeDefinition) -> Dict[str, object]:
    """Build the style dictionary for a theme."""
    bg = theme.background.hex_value
    fg = theme.body_text.hex_value
    muted = theme.comment_text.hex_value
    selection = theme.selection.hex_value

    is_dark = theme.slug == "inverse"
    blend_target = "#ffffff" if is_dark else "#000000"

    # Derive colors
    surface = mix(bg, blend_target, 0.04)
    border = mix(bg, blend_target, 0.15)
    border_variant = mix(bg, blend_target, 0.10)
    element_bg = mix(bg, blend_target, 0.05)
    element_hover = mix(bg, blend_target, 0.10)
    element_active = mix(bg, blend_target, 0.20)

    # Accent color (using teal for info/links)
    accent = get_color("teal-100").hex_value if is_dark else get_color("teal").hex_value

    # Status colors
    error_color = get_color("crimson").hex_value
    warning_color = get_color("mandarin").hex_value
    success_color = get_color("jade").hex_value

    style = {
        # Borders
        "border": hex_rgba(border),
        "border.variant": hex_rgba(border_variant),
        "border.focused": hex_rgba(accent),
        "border.selected": hex_rgba(selection),
        "border.transparent": "#00000000",
        "border.disabled": hex_rgba(border),
        # Surfaces
        "elevated_surface.background": hex_rgba(surface),
        "surface.background": hex_rgba(surface),
        "background": hex_rgba(bg),
        # Elements
        "element.background": hex_rgba(element_bg),
        "element.hover": hex_rgba(element_hover),
        "element.active": hex_rgba(element_active),
        "element.selected": hex_rgba(element_active),
        "element.disabled": hex_rgba(element_bg),
        # Ghost elements
        "ghost_element.background": "#00000000",
        "ghost_element.hover": hex_rgba(element_hover),
        "ghost_element.active": hex_rgba(element_active),
        "ghost_element.selected": hex_rgba(element_active),
        "ghost_element.disabled": hex_rgba(element_bg),
        # Text
        "text": hex_rgba(fg),
        "text.muted": hex_rgba(muted),
        "text.placeholder": hex_rgba(muted),
        "text.disabled": hex_rgba(muted),
        "text.accent": hex_rgba(accent),
        # Icons
        "icon": hex_rgba(fg),
        "icon.muted": hex_rgba(muted),
        "icon.disabled": hex_rgba(muted),
        "icon.placeholder": hex_rgba(muted),
        "icon.accent": hex_rgba(accent),
        # UI chrome
        "status_bar.background": hex_rgba(bg),
        "title_bar.background": hex_rgba(bg),
        "title_bar.inactive_background": hex_rgba(element_bg),
        "toolbar.background": hex_rgba(surface),
        "tab_bar.background": hex_rgba(surface),
        "tab.inactive_background": hex_rgba(surface),
        "tab.active_background": hex_rgba(bg),
        # Search
        "search.match_background": hex_rgba(selection, 0.4),
        "search.active_match_background": hex_rgba(warning_color, 0.4),
        # Panel
        "panel.background": hex_rgba(surface),
        "panel.focused_border": None,
        "pane.focused_border": None,
        # Scrollbar
        "scrollbar.thumb.background": hex_rgba(mix(bg, blend_target, 0.3), 0.3),
        "scrollbar.thumb.hover_background": hex_rgba(element_hover),
        "scrollbar.thumb.border": hex_rgba(element_hover),
        "scrollbar.track.background": "#00000000",
        "scrollbar.track.border": hex_rgba(border_variant),
        # Editor
        "editor.foreground": hex_rgba(fg),
        "editor.background": hex_rgba(bg),
        "editor.gutter.background": hex_rgba(bg),
        "editor.subheader.background": hex_rgba(surface),
        "editor.active_line.background": hex_rgba(surface, 0.75),
        "editor.highlighted_line.background": hex_rgba(surface),
        "editor.line_number": hex_rgba(muted),
        "editor.active_line_number": hex_rgba(fg),
        "editor.invisible": hex_rgba(muted),
        "editor.wrap_guide": hex_rgba(border, 0.05),
        "editor.active_wrap_guide": hex_rgba(border, 0.1),
        # Document highlights (selections)
        "editor.document_highlight.read_background": hex_rgba(
            selection, 0.4 if is_dark else 0.75
        ),
        "editor.document_highlight.write_background": hex_rgba(selection, 0.4),
        # Terminal
        "terminal.background": hex_rgba(bg),
        "terminal.foreground": hex_rgba(fg),
        "terminal.bright_foreground": hex_rgba(fg),
        "terminal.dim_foreground": hex_rgba(muted),
        # Terminal ANSI colors
        "terminal.ansi.black": hex_rgba(get_color("slate").hex_value),
        "terminal.ansi.red": hex_rgba(get_color("claret").hex_value),
        "terminal.ansi.green": hex_rgba(get_color("jade").hex_value),
        "terminal.ansi.yellow": hex_rgba(get_color("mandarin").hex_value),
        "terminal.ansi.blue": hex_rgba(get_color("oxford").hex_value),
        "terminal.ansi.magenta": hex_rgba(get_color("velvet").hex_value),
        "terminal.ansi.cyan": hex_rgba(get_color("teal").hex_value),
        "terminal.ansi.white": hex_rgba(get_color("paper").hex_value),
        "terminal.ansi.bright_black": hex_rgba(get_color("black-70").hex_value),
        "terminal.ansi.bright_red": hex_rgba(get_color("crimson").hex_value),
        "terminal.ansi.bright_green": hex_rgba(get_color("wasabi").hex_value),
        "terminal.ansi.bright_yellow": hex_rgba(get_color("lemon").hex_value),
        "terminal.ansi.bright_blue": hex_rgba(get_color("light-blue").hex_value),
        "terminal.ansi.bright_magenta": hex_rgba(get_color("candy").hex_value),
        "terminal.ansi.bright_cyan": hex_rgba(get_color("teal-80").hex_value),
        "terminal.ansi.bright_white": hex_rgba(get_color("white").hex_value),
        "terminal.ansi.dim_black": hex_rgba(get_color("black-40").hex_value),
        "terminal.ansi.dim_red": hex_rgba(mix(get_color("claret").hex_value, bg, 0.3)),
        "terminal.ansi.dim_green": hex_rgba(mix(get_color("jade").hex_value, bg, 0.3)),
        "terminal.ansi.dim_yellow": hex_rgba(
            mix(get_color("mandarin").hex_value, bg, 0.3)
        ),
        "terminal.ansi.dim_blue": hex_rgba(mix(get_color("oxford").hex_value, bg, 0.3)),
        "terminal.ansi.dim_magenta": hex_rgba(
            mix(get_color("velvet").hex_value, bg, 0.3)
        ),
        "terminal.ansi.dim_cyan": hex_rgba(mix(get_color("teal").hex_value, bg, 0.3)),
        "terminal.ansi.dim_white": hex_rgba(muted),
        # Links
        "link_text.hover": hex_rgba(accent),
        # Version control
        "version_control.added": hex_rgba(success_color),
        "version_control.modified": hex_rgba(warning_color),
        "version_control.deleted": hex_rgba(error_color),
        "version_control.word_added": hex_rgba(success_color, 0.35),
        "version_control.word_deleted": hex_rgba(error_color, 0.35),
        "version_control.conflict_marker.ours": hex_rgba(success_color, 0.1),
        "version_control.conflict_marker.theirs": hex_rgba(accent, 0.1),
        # Status colors
        "conflict": hex_rgba(warning_color),
        "conflict.background": hex_rgba(warning_color, 0.1),
        "conflict.border": hex_rgba(warning_color, 0.3),
        "created": hex_rgba(success_color),
        "created.background": hex_rgba(success_color, 0.1),
        "created.border": hex_rgba(success_color, 0.3),
        "deleted": hex_rgba(error_color),
        "deleted.background": hex_rgba(error_color, 0.1),
        "deleted.border": hex_rgba(error_color, 0.3),
        "error": hex_rgba(error_color),
        "error.background": hex_rgba(error_color, 0.1),
        "error.border": hex_rgba(error_color, 0.3),
        "hidden": hex_rgba(muted),
        "hidden.background": hex_rgba(bg),
        "hidden.border": hex_rgba(border),
        "hint": hex_rgba(accent),
        "hint.background": hex_rgba(accent, 0.05),
        "hint.border": hex_rgba(accent, 0.3),
        "ignored": hex_rgba(muted),
        "ignored.background": hex_rgba(bg),
        "ignored.border": hex_rgba(border),
        "info": hex_rgba(accent),
        "info.background": hex_rgba(accent, 0.1),
        "info.border": hex_rgba(accent, 0.3),
        "modified": hex_rgba(warning_color),
        "modified.background": hex_rgba(warning_color, 0.1),
        "modified.border": hex_rgba(warning_color, 0.3),
        "predictive": hex_rgba(muted),
        "predictive.background": hex_rgba(muted, 0.1),
        "predictive.border": hex_rgba(muted, 0.3),
        "renamed": hex_rgba(accent),
        "renamed.background": hex_rgba(accent, 0.1),
        "renamed.border": hex_rgba(accent, 0.3),
        "success": hex_rgba(success_color),
        "success.background": hex_rgba(success_color, 0.1),
        "success.border": hex_rgba(success_color, 0.3),
        "unreachable": hex_rgba(muted),
        "unreachable.background": hex_rgba(bg),
        "unreachable.border": hex_rgba(border),
        "warning": hex_rgba(warning_color),
        "warning.background": hex_rgba(warning_color, 0.1),
        "warning.border": hex_rgba(warning_color, 0.3),
        # Players (for collaborative editing)
        "players": [
            {
                "cursor": hex_rgba(fg),
                "background": hex_rgba(selection),
                "selection": hex_rgba(selection, 0.75 if is_dark else 1.0),
            },
            {
                "cursor": hex_rgba(get_color("claret").hex_value),
                "background": hex_rgba(get_color("claret").hex_value),
                "selection": hex_rgba(get_color("claret").hex_value, 0.24),
            },
            {
                "cursor": hex_rgba(get_color("mandarin").hex_value),
                "background": hex_rgba(get_color("mandarin").hex_value),
                "selection": hex_rgba(get_color("mandarin").hex_value, 0.24),
            },
            {
                "cursor": hex_rgba(get_color("velvet").hex_value),
                "background": hex_rgba(get_color("velvet").hex_value),
                "selection": hex_rgba(get_color("velvet").hex_value, 0.24),
            },
            {
                "cursor": hex_rgba(get_color("teal").hex_value),
                "background": hex_rgba(get_color("teal").hex_value),
                "selection": hex_rgba(get_color("teal").hex_value, 0.24),
            },
            {
                "cursor": hex_rgba(get_color("crimson").hex_value),
                "background": hex_rgba(get_color("crimson").hex_value),
                "selection": hex_rgba(get_color("crimson").hex_value, 0.24),
            },
            {
                "cursor": hex_rgba(get_color("lemon").hex_value),
                "background": hex_rgba(get_color("lemon").hex_value),
                "selection": hex_rgba(get_color("lemon").hex_value, 0.24),
            },
            {
                "cursor": hex_rgba(get_color("jade").hex_value),
                "background": hex_rgba(get_color("jade").hex_value),
                "selection": hex_rgba(get_color("jade").hex_value, 0.24),
            },
        ],
    }

    return style


def build_syntax(theme: ThemeDefinition) -> Dict[str, Dict[str, object]]:
    """Build syntax highlighting rules - minimal highlighting with only comments muted."""
    fg = theme.body_text.hex_value
    comment = theme.comment_text.hex_value

    # Default style for most tokens - use foreground color
    default_style = {
        "color": hex_rgba(fg),
        "font_style": None,
        "font_weight": None,
    }

    return {
        # Comments are muted
        "comment": {
            "color": hex_rgba(comment),
            "font_style": None,
            "font_weight": None,
        },
        "comment.doc": {
            "color": hex_rgba(comment),
            "font_style": None,
            "font_weight": None,
        },
        # Everything else uses default foreground color
        "attribute": default_style,
        "boolean": default_style,
        "constant": default_style,
        "constructor": default_style,
        "embedded": default_style,
        "emphasis": default_style,
        "emphasis.strong": {**default_style, "font_weight": 700},
        "enum": default_style,
        "function": default_style,
        "hint": default_style,
        "keyword": default_style,
        "label": default_style,
        "link_text": default_style,
        "link_uri": default_style,
        "namespace": default_style,
        "number": default_style,
        "operator": default_style,
        "predictive": {**default_style, "font_style": "italic"},
        "preproc": default_style,
        "primary": default_style,
        "property": default_style,
        "punctuation": default_style,
        "punctuation.bracket": default_style,
        "punctuation.delimiter": default_style,
        "punctuation.list_marker": default_style,
        "punctuation.markup": default_style,
        "punctuation.special": default_style,
        "selector": default_style,
        "selector.pseudo": default_style,
        "string": default_style,
        "string.escape": default_style,
        "string.regex": default_style,
        "string.special": default_style,
        "string.special.symbol": default_style,
        "tag": default_style,
        "text.literal": default_style,
        "title": {**default_style, "font_weight": 400},
        "type": default_style,
        "variable": default_style,
        "variable.special": default_style,
        "variant": default_style,
    }


def build_theme(theme: ThemeDefinition) -> Dict[str, object]:
    """Build a complete theme definition."""
    appearance = "dark" if theme.slug == "inverse" else "light"
    style = build_style(theme)

    # Extract players and syntax from style dict
    players = style.pop("players")
    syntax = build_syntax(theme)

    return {
        "name": f"Financial Times {theme.slug.title()}",
        "appearance": appearance,
        "style": {**style, "syntax": syntax, "players": players},
    }


def main(themes: Iterable[ThemeDefinition] | None = None) -> None:
    """Generate Zed themes."""
    if themes is None:
        themes = (STANDARD_THEME, INVERSE_THEME)

    payload = {
        "$schema": SCHEMA_URL,
        "name": "Financial Times",
        "author": "meriksen",
        "themes": [build_theme(theme) for theme in themes],
    }

    out_dir = Path("build/zed")
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / "financial-times.json"
    path.write_text(json.dumps(payload, indent=2) + "\n")
    print(f"wrote {path}")


if __name__ == "__main__":
    main()
