"""Generate Ghostty terminal themes based on the FT palette."""

from __future__ import annotations

import math
from pathlib import Path
from typing import Iterable, List

from ft_palette import INVERSE_THEME, STANDARD_THEME, ThemeDefinition, get_color

ANSI_PALETTE_NAMES: List[str] = [
    "slate",
    "claret",
    "jade",
    "mandarin",
    "oxford",
    "velvet",
    "teal",
    "paper",
    "support-text",
    "crimson",
    "wasabi",
    "lemon",
    "light-blue",
    "candy",
    "teal-80",
    "white",
]

MIN_CONTRAST_RATIO = 4.5

# Minimum luminance ratio between red/green pairs for colorblind accessibility.
# A ratio of 2.0:1 provides strong differentiation for deuteranopia/protanopia.
MIN_COLORBLIND_LUMINANCE_RATIO = 2.0

# Indices in ANSI_PALETTE_NAMES that are green-ish (should be lighter than reds)
GREEN_INDICES = {2, 10}  # jade, wasabi
# Indices that are red-ish (reference for luminance comparison)
RED_INDICES = {1, 9}  # claret, crimson


def hex_to_rgb(color: str) -> tuple[float, float, float]:
    """Convert #rrggbb to linearized RGB components."""

    color = color.lstrip("#")
    r = int(color[0:2], 16) / 255.0
    g = int(color[2:4], 16) / 255.0
    b = int(color[4:6], 16) / 255.0

    def to_linear(channel: float) -> float:
        return (
            math.pow((channel + 0.055) / 1.055, 2.4)
            if channel > 0.04045
            else channel / 12.92
        )

    return (to_linear(r), to_linear(g), to_linear(b))


def relative_luminance(color: str) -> float:
    """Return the perceived luminance from a hex string."""

    r, g, b = hex_to_rgb(color)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast_ratio(color_a: str, color_b: str) -> float:
    """Compute the WCAG contrast ratio between two colors."""

    lum_a = relative_luminance(color_a)
    lum_b = relative_luminance(color_b)
    lighter = max(lum_a, lum_b)
    darker = min(lum_a, lum_b)
    return (lighter + 0.05) / (darker + 0.05)


def mix_colors(color: str, fallback: str, amount: float) -> str:
    """Blend two hex colours."""

    color = color.lstrip("#")
    fallback = fallback.lstrip("#")
    cr, cg, cb = (int(color[i : i + 2], 16) for i in (0, 2, 4))
    fr, fg, fb = (int(fallback[i : i + 2], 16) for i in (0, 2, 4))
    nr = round(cr + (fr - cr) * amount)
    ng = round(cg + (fg - cg) * amount)
    nb = round(cb + (fb - cb) * amount)
    return f"#{nr:02x}{ng:02x}{nb:02x}"


def ensure_contrast(
    color: str, background: str, fallback: str, min_ratio: float = MIN_CONTRAST_RATIO
) -> str:
    """Return a color with acceptable contrast to the background."""

    if contrast_ratio(color, background) >= min_ratio:
        return color
    for amount in [0.05 * i for i in range(1, 21)]:
        candidate = mix_colors(color, fallback, amount)
        if contrast_ratio(candidate, background) >= min_ratio:
            return candidate
    return fallback


def trim_hash(value: str) -> str:
    """Return the hex colour without a leading hash."""

    return value.lstrip("#")


def luminance_ratio(color_a: str, color_b: str) -> float:
    """Compute the luminance ratio between two colors (lighter/darker)."""

    lum_a = relative_luminance(color_a)
    lum_b = relative_luminance(color_b)
    lighter = max(lum_a, lum_b)
    darker = min(lum_a, lum_b)
    if darker == 0:
        return float("inf")
    return lighter / darker


def build_palette_values(theme: ThemeDefinition) -> List[str]:
    """Map the configured palette names to hex values with contrast fixes."""

    background = theme.background.hex_value
    fallback = theme.body_text.hex_value
    is_dark_theme = relative_luminance(background) < 0.2

    # First pass: ensure contrast with background
    values: List[str] = []
    for name in ANSI_PALETTE_NAMES:
        color = get_color(name).hex_value
        color = ensure_contrast(color, background, fallback)
        values.append(color)

    # Second pass: ensure colorblind accessibility on dark themes
    # Boost green luminance if too close to corresponding red
    if is_dark_theme:
        for green_idx in GREEN_INDICES:
            # Find corresponding red (0-7 normal, 8-15 bright)
            red_idx = green_idx - 1  # jade(2)->claret(1), wasabi(10)->crimson(9)
            if red_idx not in RED_INDICES:
                continue

            green_color = values[green_idx]
            red_color = values[red_idx]
            green_lum = relative_luminance(green_color)
            red_lum = relative_luminance(red_color)

            # Green should be noticeably lighter than red
            current_ratio = green_lum / red_lum if red_lum > 0 else float("inf")

            if current_ratio < MIN_COLORBLIND_LUMINANCE_RATIO:
                # Boost green luminance by mixing more toward white
                target_lum = red_lum * MIN_COLORBLIND_LUMINANCE_RATIO
                for amount in [0.05 * i for i in range(1, 21)]:
                    candidate = mix_colors(green_color, fallback, amount)
                    if relative_luminance(candidate) >= target_lum:
                        # Verify we still have good background contrast
                        if contrast_ratio(candidate, background) >= MIN_CONTRAST_RATIO:
                            values[green_idx] = candidate
                        break

    return [trim_hash(c) for c in values]


def build_theme_lines(theme: ThemeDefinition, palette_values: List[str]) -> List[str]:
    """Compose the Ghostty config lines for a given theme."""

    lines = [f"# Financial Times {theme.slug.title()} (Ghostty)"]
    for index, hex_value in enumerate(palette_values):
        lines.append(f"palette = {index}=#{hex_value}")

    background = trim_hash(theme.background.hex_value)
    foreground = trim_hash(theme.body_text.hex_value)
    selection_bg = trim_hash(theme.selection.hex_value)
    comment = trim_hash(theme.comment_text.hex_value)

    lines.extend(
        [
            f"background = {background}",
            f"foreground = {foreground}",
            f"cursor-color = {foreground}",
            f"cursor-text = {background}",
            f"selection-background = {selection_bg}",
            f"selection-foreground = {foreground}",
            f"split-divider-color = {comment}",
        ]
    )
    return lines


def write_theme(
    theme: ThemeDefinition, palette_values: List[str], out_dir: Path
) -> Path:
    """Write a Ghostty theme file for the given theme object."""

    out_dir.mkdir(parents=True, exist_ok=True)
    lines = build_theme_lines(theme, palette_values)
    path = out_dir / f"financial-times-{theme.slug}"
    path.write_text("\n".join(lines) + "\n")
    return path


def main(themes: Iterable[ThemeDefinition] | None = None) -> None:
    """Generate Ghostty themes for all configured FT variants."""

    if themes is None:
        themes = (STANDARD_THEME, INVERSE_THEME)

    out_dir = Path("build/ghostty")
    for theme in themes:
        palette_values = build_palette_values(theme)
        path = write_theme(theme, palette_values, out_dir)
        print(f"wrote {path}")


if __name__ == "__main__":
    main()
