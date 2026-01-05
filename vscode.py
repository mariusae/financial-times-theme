"""VSCode theme generator built from the FT palette."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Iterable, List, Tuple
import subprocess

from ft_palette import INVERSE_THEME, STANDARD_THEME, ThemeDefinition, get_color

PACKAGE_METADATA = {
    "name": "financial-times-theme",
    "displayName": "Financial Times Theme",
    "description": "FT paper-inspired light and inverse VSCode themes derived from the Origami palette.",
    "version": "0.1.0",
    "publisher": "meriksen",
    "engines": {"vscode": ">=1.85.0"},
    "license": "SEE LICENSE IN LICENSE",
    "categories": ["Themes"],
}


def build_theme_payload(theme: ThemeDefinition) -> dict:
    """Return the VSCode theme JSON payload for a given FT theme."""

    background = theme.background.hex_value
    foreground = theme.body_text.hex_value
    selection = theme.selection.hex_value
    comment = theme.comment_text.hex_value

    # Use a subtler, muted color for the status bar to reduce visual prominence
    if theme.slug == "standard":
        status_bar_bg = get_color("black-10").hex_value  # #e6d9ce - muted with good contrast
    else:
        status_bar_bg = background

    colors = {
        "editor.background": background,
        "editor.foreground": foreground,
        "editor.selectionBackground": selection,
        "editor.selectionHighlightBackground": selection,
        "editor.inactiveSelectionBackground": selection,
        "editor.selectionForeground": foreground,
        "editorGutter.commentRangeForeground": comment,
        "sideBar.background": background,
        "sideBar.foreground": foreground,
        "statusBar.background": status_bar_bg,
        "statusBar.foreground": foreground,
        "statusBar.noFolderBackground": status_bar_bg,
        "statusBar.noFolderForeground": foreground,
        "activityBar.background": background,
        "activityBar.foreground": foreground,
        "editorLineNumber.foreground": comment,
        "editorLineNumber.activeForeground": foreground,
    }

    token_colors = [
        {
            "name": "Comments",
            "scope": ["comment", "punctuation.definition.comment"],
            "settings": {"foreground": comment},
        },
        {
            "name": "Keywords",
            "scope": ["keyword"],
            "settings": {"foreground": foreground},
        },
    ]

    return {
        "$schema": "vscode://schemas/color-theme",
        "name": f"Financial Times {theme.slug.title()}",
        "type": "dark" if theme.slug == "inverse" else "light",
        "colors": colors,
        "tokenColors": token_colors,
    }


def write_theme(theme: ThemeDefinition, out_dir: Path) -> Path:
    """Write a VSCode theme JSON file and return its path."""

    payload = build_theme_payload(theme)
    out_dir.mkdir(parents=True, exist_ok=True)
    file_path = out_dir / f"ft-{theme.slug}.json"
    file_path.write_text(json.dumps(payload, indent=2) + "\n")
    return file_path


def write_package_json(theme_entries: List[Tuple[ThemeDefinition, Path]], out_dir: Path) -> Path:
    """Emit the VSCode extension manifest pointing at our theme files."""

    themes = []
    for theme, path in theme_entries:
        ui_theme = "vs-dark" if theme.slug == "inverse" else "vs"
        themes.append(
            {
                "label": f"Financial Times {theme.slug.title()}",
                "uiTheme": ui_theme,
                "path": f"./{path.name}",
            }
        )

    manifest = dict(PACKAGE_METADATA)
    manifest["scripts"] = {
        "build": "python3 ../../vscode.py",
        "package": "vsce package",
    }
    manifest["contributes"] = {"themes": themes}
    manifest_path = out_dir / "package.json"
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n")
    return manifest_path


def run_vsce_package(out_dir: Path) -> None:
    """Invoke vsce package within the generated theme directory."""

    result = subprocess.run(
        ["vsce", "package"],
        cwd=str(out_dir),
        capture_output=True,
        text=True,
        check=False,
    )
    print(result.stdout.strip())
    if result.stderr:
        print(result.stderr.strip())
    if result.returncode != 0:
        raise SystemExit(result.returncode)


def main(themes: Iterable[ThemeDefinition] | None = None) -> None:
    """Generate VSCode themes for the provided FT theme set."""

    if themes is None:
        themes = (STANDARD_THEME, INVERSE_THEME)

    out_dir = Path("build/vscode")
    written: List[Tuple[ThemeDefinition, Path]] = []
    for theme in themes:
        path = write_theme(theme, out_dir)
        written.append((theme, path))
        print(f"wrote {path}")

    manifest = write_package_json(written, out_dir)
    print(f"wrote {manifest}")

    run_vsce_package(out_dir)


if __name__ == "__main__":
    main()
