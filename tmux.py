"""Generate tmux themes based on the FT palette."""

from __future__ import annotations

from pathlib import Path
from typing import Iterable, List

from ft_palette import INVERSE_THEME, STANDARD_THEME, ThemeDefinition, get_color


def trim_hash(value: str) -> str:
    """Return the hex colour without a leading hash."""

    return value.lstrip("#")


def build_theme_lines(theme: ThemeDefinition) -> List[str]:
    """Compose the tmux config lines for a given theme."""

    background = theme.background.hex_value
    foreground = theme.body_text.hex_value
    selection = theme.selection.hex_value
    comment = theme.comment_text.hex_value

    # Use a subtler, muted color for the status bar
    if theme.slug == "standard":
        status_bg = get_color("black-10").hex_value  # #e6d9ce
    else:
        status_bg = get_color("black-90").hex_value  # #1a1817

    # Accent color for active elements
    accent = get_color("teal").hex_value  # #0d7680

    lines = [
        f"# Financial Times {theme.slug.title()} (tmux)",
        "#",
        "# Usage: Add to your ~/.tmux.conf or source this file:",
        f"#   source-file ~/.config/tmux/financial-times-{theme.slug}.conf",
        "",
        "# Status bar",
        f"set -g status-style 'bg={status_bg},fg={foreground}'",
        f"set -g status-left-style 'bg={status_bg},fg={foreground}'",
        f"set -g status-right-style 'bg={status_bg},fg={foreground}'",
        "",
        "# Window status",
        f"set -g window-status-style 'bg={status_bg},fg={comment}'",
        f"set -g window-status-current-style 'bg={status_bg},fg={foreground},bold'",
        f"set -g window-status-activity-style 'bg={status_bg},fg={accent}'",
        f"set -g window-status-bell-style 'bg={status_bg},fg={accent}'",
        "",
        "# Pane borders",
        f"set -g pane-border-style 'fg={comment}'",
        f"set -g pane-active-border-style 'fg={accent}'",
        "",
        "# Message styling",
        f"set -g message-style 'bg={selection},fg={foreground}'",
        f"set -g message-command-style 'bg={selection},fg={foreground}'",
        "",
        "# Mode styling (copy mode, etc.)",
        f"set -g mode-style 'bg={selection},fg={foreground}'",
        "",
        "# Clock mode",
        f"set -g clock-mode-colour '{accent}'",
        "",
        "# Copy mode match highlighting",
        f"set -g copy-mode-match-style 'bg={selection},fg={foreground}'",
        f"set -g copy-mode-current-match-style 'bg={accent},fg={background}'",
    ]

    return lines


def write_theme(theme: ThemeDefinition, out_dir: Path) -> Path:
    """Write a tmux theme file for the given theme object."""

    out_dir.mkdir(parents=True, exist_ok=True)
    lines = build_theme_lines(theme)
    path = out_dir / f"financial-times-{theme.slug}.conf"
    path.write_text("\n".join(lines) + "\n")
    return path


def main(themes: Iterable[ThemeDefinition] | None = None) -> None:
    """Generate tmux themes for all configured FT variants."""

    if themes is None:
        themes = (STANDARD_THEME, INVERSE_THEME)

    out_dir = Path("build/tmux")
    for theme in themes:
        path = write_theme(theme, out_dir)
        print(f"wrote {path}")


if __name__ == "__main__":
    main()
