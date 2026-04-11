"""Generate Zellij themes based on the FT palette."""

from __future__ import annotations

from pathlib import Path
from typing import Iterable, List

from ft_palette import INVERSE_THEME, STANDARD_THEME, ThemeDefinition, get_color
from ghostty import ANSI_PALETTE_NAMES, build_palette_values, ensure_contrast


def hex_to_rgb_tokens(value: str) -> str:
    """Convert a hex colour into space-separated RGB tokens."""

    value = value.lstrip("#")
    red = int(value[0:2], 16)
    green = int(value[2:4], 16)
    blue = int(value[4:6], 16)
    return f"{red} {green} {blue}"


def render_kdl_color(value: str | int) -> str:
    """Render a colour value in the format Zellij expects."""

    if isinstance(value, int):
        return str(value)
    return hex_to_rgb_tokens(value)


def build_theme_lines(theme: ThemeDefinition) -> List[str]:
    """Compose the KDL theme lines for a given FT theme."""

    ansi_palette = {
        name: f"#{value}"
        for name, value in zip(ANSI_PALETTE_NAMES, build_palette_values(theme))
    }

    if theme.slug == "standard":
        panel_bg = get_color("paper-dim").hex_value
        ribbon_bg = get_color("black-20").hex_value
    else:
        panel_bg = get_color("slate-dim").hex_value
        ribbon_bg = get_color("black-90").hex_value

    foreground = theme.body_text.hex_value
    background = theme.background.hex_value
    selection_bg = theme.selection.hex_value
    accent_bg = ansi_palette["teal"]
    accent_text = ensure_contrast(background, accent_bg, foreground)
    ribbon_text = ensure_contrast(foreground, ribbon_bg, background)
    selected_text = ensure_contrast(foreground, selection_bg, background)

    emphasis_0 = ansi_palette["mandarin"]
    emphasis_1 = ansi_palette["light-blue"]
    emphasis_2 = ansi_palette["wasabi"]
    emphasis_3 = ansi_palette["candy"]
    success = ansi_palette["wasabi"]
    error = ansi_palette["crimson"]
    frame = ensure_contrast(ansi_palette["teal"], background, foreground)
    highlight = ensure_contrast(ansi_palette["mandarin"], background, foreground)

    sections = {
        "text_unselected": {
            "base": foreground,
            "background": panel_bg,
            "emphasis_0": emphasis_0,
            "emphasis_1": emphasis_1,
            "emphasis_2": emphasis_2,
            "emphasis_3": emphasis_3,
        },
        "text_selected": {
            "base": selected_text,
            "background": selection_bg,
            "emphasis_0": emphasis_0,
            "emphasis_1": emphasis_1,
            "emphasis_2": emphasis_2,
            "emphasis_3": emphasis_3,
        },
        "ribbon_selected": {
            "base": accent_text,
            "background": accent_bg,
            "emphasis_0": error,
            "emphasis_1": emphasis_0,
            "emphasis_2": emphasis_3,
            "emphasis_3": ansi_palette["oxford"],
        },
        "ribbon_unselected": {
            "base": ribbon_text,
            "background": ribbon_bg,
            "emphasis_0": error,
            "emphasis_1": foreground,
            "emphasis_2": ansi_palette["oxford"],
            "emphasis_3": emphasis_3,
        },
        "table_title": {
            "base": frame,
            "background": 0,
            "emphasis_0": emphasis_0,
            "emphasis_1": emphasis_1,
            "emphasis_2": emphasis_2,
            "emphasis_3": emphasis_3,
        },
        "table_cell_selected": {
            "base": selected_text,
            "background": selection_bg,
            "emphasis_0": emphasis_0,
            "emphasis_1": emphasis_1,
            "emphasis_2": emphasis_2,
            "emphasis_3": emphasis_3,
        },
        "table_cell_unselected": {
            "base": foreground,
            "background": panel_bg,
            "emphasis_0": emphasis_0,
            "emphasis_1": emphasis_1,
            "emphasis_2": emphasis_2,
            "emphasis_3": emphasis_3,
        },
        "list_selected": {
            "base": selected_text,
            "background": selection_bg,
            "emphasis_0": emphasis_0,
            "emphasis_1": emphasis_1,
            "emphasis_2": emphasis_2,
            "emphasis_3": emphasis_3,
        },
        "list_unselected": {
            "base": foreground,
            "background": panel_bg,
            "emphasis_0": emphasis_0,
            "emphasis_1": emphasis_1,
            "emphasis_2": emphasis_2,
            "emphasis_3": emphasis_3,
        },
        "frame_selected": {
            "base": frame,
            "background": 0,
            "emphasis_0": error,
            "emphasis_1": emphasis_1,
            "emphasis_2": emphasis_3,
            "emphasis_3": 0,
        },
        "frame_highlight": {
            "base": highlight,
            "background": 0,
            "emphasis_0": emphasis_3,
            "emphasis_1": highlight,
            "emphasis_2": highlight,
            "emphasis_3": highlight,
        },
        "exit_code_success": {
            "base": success,
            "background": 0,
            "emphasis_0": emphasis_1,
            "emphasis_1": background,
            "emphasis_2": emphasis_3,
            "emphasis_3": ansi_palette["oxford"],
        },
        "exit_code_error": {
            "base": error,
            "background": 0,
            "emphasis_0": ansi_palette["lemon"],
            "emphasis_1": 0,
            "emphasis_2": 0,
            "emphasis_3": 0,
        },
        "multiplayer_user_colors": {
            "player_1": emphasis_3,
            "player_2": ansi_palette["oxford"],
            "player_3": 0,
            "player_4": ansi_palette["lemon"],
            "player_5": emphasis_1,
            "player_6": 0,
            "player_7": error,
            "player_8": 0,
            "player_9": 0,
            "player_10": 0,
        },
    }

    lines = ["themes {", f"    financial-times-{theme.slug} {{"]
    for section_name, values in sections.items():
        lines.append(f"        {section_name} {{")
        for key, value in values.items():
            lines.append(f"            {key} {render_kdl_color(value)}")
        lines.append("        }")
    lines.extend(["    }", "}"])
    return lines


def write_theme(theme: ThemeDefinition, out_dir: Path) -> Path:
    """Write a Zellij theme file for the given theme object."""

    out_dir.mkdir(parents=True, exist_ok=True)
    lines = build_theme_lines(theme)
    path = out_dir / f"financial-times-{theme.slug}.kdl"
    path.write_text("\n".join(lines) + "\n")
    return path


def main(themes: Iterable[ThemeDefinition] | None = None) -> None:
    """Generate Zellij themes for all configured FT variants."""

    if themes is None:
        themes = (STANDARD_THEME, INVERSE_THEME)

    out_dir = Path("build/zellij")
    for theme in themes:
        path = write_theme(theme, out_dir)
        print(f"wrote {path}")


if __name__ == "__main__":
    main()
