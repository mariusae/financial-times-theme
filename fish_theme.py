"""Generate fish shell color themes based on the FT palette."""

from __future__ import annotations

from pathlib import Path
from typing import Iterable, List, Sequence

from ft_palette import INVERSE_THEME, STANDARD_THEME, ThemeDefinition, get_color

FISH_SELECTION_COLORS = {
    "standard": "oxford-40",
    "inverse": "jade",
}


def color_hex(name: str) -> str:
    """Lookup a palette entry and return its hex value."""

    return get_color(name).hex_value
INLINE_KEYS = (
    "fish_color_normal",
    "fish_color_command",
    "fish_color_keyword",
    "fish_color_quote",
    "fish_color_redirection",
    "fish_color_end",
    "fish_color_error",
    "fish_color_param",
    "fish_color_comment",
    "fish_color_selection",
    "fish_color_operator",
    "fish_color_escape",
    "fish_color_autosuggestion",
)

PAGER_KEYS = (
    "fish_pager_color_progress",
    "fish_pager_color_background",
    "fish_pager_color_prefix",
    "fish_pager_color_completion",
    "fish_pager_color_description",
    "fish_pager_color_selected_background",
    "fish_pager_color_selected_prefix",
    "fish_pager_color_selected_completion",
    "fish_pager_color_selected_description",
    "fish_pager_color_secondary_background",
    "fish_pager_color_secondary_prefix",
    "fish_pager_color_secondary_completion",
    "fish_pager_color_secondary_description",
)


def build_assignment_lines(theme: ThemeDefinition) -> List[str]:
    """Compose fish color assignments for the theme."""

    fg = theme.body_text.hex_value
    comment = theme.comment_text.hex_value
    selection_bg = color_hex(FISH_SELECTION_COLORS.get(theme.slug, "sky"))

    mapping = {
        "fish_color_normal": fg,
        "fish_color_command": color_hex("teal"),
        "fish_color_keyword": color_hex("oxford"),
        "fish_color_quote": color_hex("mandarin"),
        "fish_color_redirection": color_hex("oxford"),
        "fish_color_end": color_hex("jade"),
        "fish_color_error": color_hex("claret"),
        "fish_color_param": fg,
        "fish_color_comment": comment,
        "fish_color_selection": f"--background={selection_bg}",
        "fish_color_operator": fg,
        "fish_color_escape": color_hex("jade"),
        "fish_color_autosuggestion": color_hex("support-text"),
        "fish_pager_color_progress": color_hex("mandarin"),
        "fish_pager_color_background": "",
        "fish_pager_color_prefix": fg,
        "fish_pager_color_completion": color_hex("support-text"),
        "fish_pager_color_description": comment,
        "fish_pager_color_selected_background": f"--background={selection_bg}",
        "fish_pager_color_selected_prefix": fg,
        "fish_pager_color_selected_completion": fg,
        "fish_pager_color_selected_description": fg,
        "fish_pager_color_secondary_background": "",
        "fish_pager_color_secondary_prefix": fg,
        "fish_pager_color_secondary_completion": fg,
        "fish_pager_color_secondary_description": comment,
    }

    lines: List[str] = []
    for key in INLINE_KEYS:
        value = mapping.get(key, "")
        lines.append(f"{key} {value}".rstrip())
    lines.append("\n# Completion Pager Colors")
    for key in PAGER_KEYS:
        value = mapping.get(key, "")
        lines.append(f"{key} {value}".rstrip())
    return lines


def build_theme_lines(theme: ThemeDefinition) -> List[str]:
    """Return the header and assignment lines for the fish theme."""

    lines = [
        f"# Financial Times {theme.slug.title()} fish theme",
        "# Source this file to apply the colors globally (universal vars).",
    ]
    lines.extend(build_assignment_lines(theme))
    return lines


def write_theme(theme: ThemeDefinition, out_dir: Path) -> Path:
    """Write the fish theme file to the build directory."""

    out_dir.mkdir(parents=True, exist_ok=True)
    lines = build_theme_lines(theme)
    path = out_dir / f"financial-times-{theme.slug}.theme"
    path.write_text("\n".join(lines) + "\n")
    return path


def main(themes: Iterable[ThemeDefinition] | None = None) -> None:
    """Generate fish theme files for all configured FT variants."""

    if themes is None:
        themes = (STANDARD_THEME, INVERSE_THEME)

    out_dir = Path("build/fish")
    for theme in themes:
        path = write_theme(theme, out_dir)
        print(f"wrote {path}")


if __name__ == "__main__":
    main()
