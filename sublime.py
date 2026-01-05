"""Sublime Text theme generator built from the FT palette."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Iterable, List

from ft_palette import (
    INVERSE_THEME,
    STANDARD_THEME,
    ThemeDefinition,
    get_color,
)


def build_color_scheme(theme: ThemeDefinition) -> dict:
    """Return the Sublime Text color scheme payload for a given FT theme."""

    background = theme.background.hex_value
    foreground = theme.body_text.hex_value
    selection = theme.selection.hex_value
    comment = theme.comment_text.hex_value

    # Colors for git diff indicators
    jade = get_color("jade").hex_value
    oxford = get_color("oxford").hex_value
    claret = get_color("claret").hex_value
    teal = get_color("teal").hex_value

    if theme.slug == "inverse":
        line_highlight = get_color("black-80").hex_value
        gutter_fg = get_color("muted-inverse-text").hex_value
        find_highlight = get_color("oxford-40").hex_value
        guide_color = get_color("black-70").hex_value
    else:
        line_highlight = get_color("wheat").hex_value
        gutter_fg = comment
        find_highlight = get_color("sky").hex_value
        guide_color = get_color("black-20").hex_value

    return {
        "name": f"Financial Times {theme.slug.title()}",
        "author": "FT Theme Generator",
        "variables": {
            "background": background,
            "foreground": foreground,
            "selection": selection,
            "comment": comment,
        },
        "globals": {
            "background": "var(background)",
            "foreground": "var(foreground)",
            "caret": "var(foreground)",
            "block_caret": "var(foreground)",
            "line_highlight": line_highlight,
            "selection": "var(selection)",
            "selection_border": "var(selection)",
            "inactive_selection": "var(selection)",
            "misspelling": claret,
            "shadow": background,
            "active_guide": teal,
            "stack_guide": guide_color,
            "guide": guide_color,
            "find_highlight": find_highlight,
            "find_highlight_foreground": foreground,
            "brackets_foreground": "var(foreground)",
            "brackets_options": "underline",
            "bracket_contents_foreground": "var(foreground)",
            "bracket_contents_options": "underline",
            "tags_foreground": "var(foreground)",
            "tags_options": "stippled_underline",
            "gutter": "var(background)",
            "gutter_foreground": gutter_fg,
            "gutter_foreground_highlight": "var(foreground)",
            "line_diff_added": jade,
            "line_diff_modified": oxford,
            "line_diff_deleted": claret,
            "accent": teal,
            "popup_css": f"html {{ background-color: {background}; color: {foreground}; }}",
        },
        "rules": [
            {
                "name": "Comment",
                "scope": "comment, punctuation.definition.comment",
                "foreground": "var(comment)",
            },
        ],
    }


def write_color_scheme(theme: ThemeDefinition, out_dir: Path) -> Path:
    """Write a Sublime Text color scheme file and return its path."""

    payload = build_color_scheme(theme)
    out_dir.mkdir(parents=True, exist_ok=True)
    file_path = out_dir / f"Financial Times {theme.slug.title()}.sublime-color-scheme"
    file_path.write_text(json.dumps(payload, indent=2) + "\n")
    return file_path


def main(themes: Iterable[ThemeDefinition] | None = None) -> None:
    """Generate Sublime Text themes for the provided FT theme set."""

    if themes is None:
        themes = (STANDARD_THEME, INVERSE_THEME)

    out_dir = Path("build/sublime")
    written: List[Path] = []
    for theme in themes:
        path = write_color_scheme(theme, out_dir)
        written.append(path)
        print(f"wrote {path}")


if __name__ == "__main__":
    main()
