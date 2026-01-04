"""Financial Times colour palette definitions.

This module is generated from the public palette documented at
https://origami.ft.com/foundations/colours/ on the FT Origami design system.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple


@dataclass(frozen=True)
class FTColor:
    name: str
    css_variable: str
    description: str
    hex_value: str


FT_COLOR_PALETTE: Tuple[FTColor, ...] = (
    FTColor(
        name="ft-pink",
        css_variable="--o3-color-palette-ft-pink",
        description="FT Pink is used for the FT logo",
        hex_value="#fcd0b1",
    ),
    FTColor(
        name="ft-grey",
        css_variable="--o3-color-palette-ft-grey",
        description="...",
        hex_value="#333333",
    ),
    FTColor(
        name="white",
        css_variable="--o3-color-palette-white",
        description="...",
        hex_value="#ffffff",
    ),
    FTColor(
        name="black",
        css_variable="--o3-color-palette-black",
        description="...",
        hex_value="#000000",
    ),
    FTColor(
        name="claret",
        css_variable="--o3-color-palette-claret",
        description="Claret is the main branding colour for MyFT related products. It should be used sparingly and never be used as a background colour. Usage example: MyFT branding; MyFT CTAs",
        hex_value="#990f3d",
    ),
    FTColor(
        name="teal",
        css_variable="--o3-color-palette-teal",
        description="Teal is the most striking colour and main CTA colour on ft.com. It is reserved for important action items that need to stand out: buttons, text links and other critical functional use cases.",
        hex_value="#0d7680",
    ),
    FTColor(
        name="oxford",
        css_variable="--o3-color-palette-oxford",
        description="Oxford is used to denote opinion pieces (in combination with Sky). It is used on the homepage and in articles. Use for information and callouts in general. Usage example: opinion branding; opinion topic tags.",
        hex_value="#0f5499",
    ),
    FTColor(
        name="slate",
        css_variable="--o3-color-palette-slate",
        description="Slate is a warmer version of black. It is used as inverse backgrounds for editorial content and as a theme option(Mono) for buttons.",
        hex_value="#262a33",
    ),
    FTColor(
        name="paper",
        css_variable="--o3-color-palette-paper",
        description="Paper, as it's name implies, is the FT's main background colour. It is the main expression of the brand colour on product. It is a lighter, more legible shade of FT Pink and can be seen as a kind of replacement of white.",
        hex_value="#fff1e5",
    ),
    FTColor(
        name="mandarin",
        css_variable="--o3-color-palette-mandarin",
        description="...",
        hex_value="#ff8833",
    ),
    FTColor(
        name="light-blue",
        css_variable="--o3-color-palette-light-blue",
        description="...",
        hex_value="#00a0dd",
    ),
    FTColor(
        name="crimson",
        css_variable="--o3-color-palette-crimson",
        description="...",
        hex_value="#cc0000",
    ),
    FTColor(
        name="graphics-dark-blue",
        css_variable="--o3-color-palette-graphics-dark-blue",
        description="...",
        hex_value="#006f9b",
    ),
    FTColor(
        name="wheat",
        css_variable="--o3-color-palette-wheat",
        description="...",
        hex_value="#f2dfce",
    ),
    FTColor(
        name="candy",
        css_variable="--o3-color-palette-candy",
        description="...",
        hex_value="#ff7faa",
    ),
    FTColor(
        name="wasabi",
        css_variable="--o3-color-palette-wasabi",
        description="...",
        hex_value="#96cc28",
    ),
    FTColor(
        name="jade",
        css_variable="--o3-color-palette-jade",
        description="...",
        hex_value="#00994d",
    ),
    FTColor(
        name="velvet",
        css_variable="--o3-color-palette-velvet",
        description="...",
        hex_value="#593380",
    ),
    FTColor(
        name="lemon",
        css_variable="--o3-color-palette-lemon",
        description="...",
        hex_value="#ffec1a",
    ),
    FTColor(
        name="sky",
        css_variable="--o3-color-palette-sky",
        description="...",
        hex_value="#cce6ff",
    ),
    FTColor(
        name="matisse-blue",
        css_variable="--o3-color-palette-matisse-blue",
        description="...",
        hex_value="#355778",
    ),
    FTColor(
        name="link-text",
        css_variable="--o3-color-use-case-link-text",
        description="...",
        hex_value="#0d7680",
    ),
    FTColor(
        name="link-text-hover",
        css_variable="--o3-color-use-case-link-text-hover",
        description="...",
        hex_value="#08474d",
    ),
    FTColor(
        name="link-underline",
        css_variable="--o3-color-use-case-link-underline",
        description="...",
        hex_value="#cfd8d1",
    ),
    FTColor(
        name="link-underline-hover",
        css_variable="--o3-color-use-case-link-underline-hover",
        description="...",
        hex_value="#9ec0bd",
    ),
    FTColor(
        name="link-inverse-text",
        css_variable="--o3-color-use-case-link-inverse-text",
        description="...",
        hex_value="#ffffff",
    ),
    FTColor(
        name="link-inverse-text-hover",
        css_variable="--o3-color-use-case-link-inverse-text-hover",
        description="...",
        hex_value="#d4d4d6",
    ),
    FTColor(
        name="link-inverse-underline",
        css_variable="--o3-color-use-case-link-inverse-underline",
        description="...",
        hex_value="#ffffff",
    ),
    FTColor(
        name="link-inverse-underline-hover",
        css_variable="--o3-color-use-case-link-inverse-underline-hover",
        description="...",
        hex_value="#d4d4d6",
    ),
    FTColor(
        name="page-background",
        css_variable="--o3-color-use-case-page-background",
        description="...",
        hex_value="#fff1e5",
    ),
    FTColor(
        name="page-inverse-background",
        css_variable="--o3-color-use-case-page-inverse-background",
        description="...",
        hex_value="#262a33",
    ),
    FTColor(
        name="body-text",
        css_variable="--o3-color-use-case-body-text",
        description="...",
        hex_value="#33302e",
    ),
    FTColor(
        name="body-inverse-text",
        css_variable="--o3-color-use-case-body-inverse-text",
        description="...",
        hex_value="#ffffff",
    ),
    FTColor(
        name="support-text",
        css_variable="--o3-color-use-case-support-text",
        description="...",
        hex_value="#4d4845",
    ),
    FTColor(
        name="support-inverse-text",
        css_variable="--o3-color-use-case-support-inverse-text",
        description="...",
        hex_value="#e9eaeb",
    ),
    FTColor(
        name="muted-text",
        css_variable="--o3-color-use-case-muted-text",
        description='"Muted" text is less prominent, for example credits and captions.',
        hex_value="#807973",
    ),
    FTColor(
        name="muted-inverse-text",
        css_variable="--o3-color-use-case-muted-inverse-text",
        description='"Muted" text is less prominent, for example credits and captions.',
        hex_value="#a8aaad",
    ),
    FTColor(
        name="heading-text",
        css_variable="--o3-color-use-case-heading-text",
        description="...",
        hex_value="#33302e",
    ),
    FTColor(
        name="heading-inverse-text",
        css_variable="--o3-color-use-case-heading-inverse-text",
        description="...",
        hex_value="#ffffff",
    ),
    FTColor(
        name="footer-text",
        css_variable="--o3-color-use-case-footer-text",
        description="...",
        hex_value="#33302e",
    ),
    FTColor(
        name="caption-text",
        css_variable="--o3-color-use-case-caption-text",
        description="...",
        hex_value="#33302e",
    ),
    FTColor(
        name="button-foreground",
        css_variable="--o3-color-use-case-button-foreground",
        description="...",
        hex_value="#ffffff",
    ),
    FTColor(
        name="button-foreground-disabled",
        css_variable="--o3-color-use-case-button-foreground-disabled",
        description="...",
        hex_value="#fff7ef",
    ),
    FTColor(
        name="button-default",
        css_variable="--o3-color-use-case-button-default",
        description="...",
        hex_value="#0d7680",
    ),
    FTColor(
        name="button-hover",
        css_variable="--o3-color-use-case-button-hover",
        description="...",
        hex_value="#0a5e66",
    ),
    FTColor(
        name="button-pressed",
        css_variable="--o3-color-use-case-button-pressed",
        description="...",
        hex_value="#052f33",
    ),
    FTColor(
        name="button-disabled",
        css_variable="--o3-color-use-case-button-disabled",
        description="...",
        hex_value="#9ec0bd",
    ),
    FTColor(
        name="error-background",
        css_variable="--o3-color-use-case-error-background",
        description="...",
        hex_value="rgba(204, 0, 0, 0.06)",
    ),
    FTColor(
        name="error-text",
        css_variable="--o3-color-use-case-error-text",
        description="...",
        hex_value="#cc0000",
    ),
    FTColor(
        name="error",
        css_variable="--o3-color-use-case-error",
        description="[DEPRECATED] This token is going to be looked at in the upcoming audit.",
        hex_value="#cc0000",
    ),
    FTColor(
        name="success-background",
        css_variable="--o3-color-use-case-success-background",
        description="...",
        hex_value="#d7f0d1",
    ),
    FTColor(
        name="success-foreground",
        css_variable="--o3-color-use-case-success-foreground",
        description="...",
        hex_value="#00572c",
    ),
    FTColor(
        name="black-5",
        css_variable="--o3-color-palette-black-5",
        description="...",
        hex_value="#f2e5da",
    ),
    FTColor(
        name="black-10",
        css_variable="--o3-color-palette-black-10",
        description="...",
        hex_value="#e6d9ce",
    ),
    FTColor(
        name="black-20",
        css_variable="--o3-color-palette-black-20",
        description="...",
        hex_value="#ccc1b7",
    ),
    FTColor(
        name="black-30",
        css_variable="--o3-color-palette-black-30",
        description="...",
        hex_value="#b3a9a0",
    ),
    FTColor(
        name="black-40",
        css_variable="--o3-color-palette-black-40",
        description="...",
        hex_value="#999189",
    ),
    FTColor(
        name="black-50",
        css_variable="--o3-color-palette-black-50",
        description="...",
        hex_value="#807973",
    ),
    FTColor(
        name="black-60",
        css_variable="--o3-color-palette-black-60",
        description="...",
        hex_value="#66605c",
    ),
    FTColor(
        name="black-70",
        css_variable="--o3-color-palette-black-70",
        description="...",
        hex_value="#4d4845",
    ),
    FTColor(
        name="black-80",
        css_variable="--o3-color-palette-black-80",
        description="...",
        hex_value="#33302e",
    ),
    FTColor(
        name="black-90",
        css_variable="--o3-color-palette-black-90",
        description="...",
        hex_value="#1a1817",
    ),
    FTColor(
        name="white-10",
        css_variable="--o3-color-palette-white-10",
        description="...",
        hex_value="#fff2e8",
    ),
    FTColor(
        name="white-20",
        css_variable="--o3-color-palette-white-20",
        description="...",
        hex_value="#fff4ea",
    ),
    FTColor(
        name="white-40",
        css_variable="--o3-color-palette-white-40",
        description="...",
        hex_value="#fff7ef",
    ),
    FTColor(
        name="white-60",
        css_variable="--o3-color-palette-white-60",
        description="...",
        hex_value="#fff9f5",
    ),
    FTColor(
        name="white-80",
        css_variable="--o3-color-palette-white-80",
        description="...",
        hex_value="#fffcfa",
    ),
    FTColor(
        name="oxford-30",
        css_variable="--o3-color-palette-oxford-30",
        description="...",
        hex_value="#082a4d",
    ),
    FTColor(
        name="oxford-40",
        css_variable="--o3-color-palette-oxford-40",
        description="...",
        hex_value="#0a3866",
    ),
    FTColor(
        name="oxford-50",
        css_variable="--o3-color-palette-oxford-50",
        description="...",
        hex_value="#0d4680",
    ),
    FTColor(
        name="oxford-60",
        css_variable="--o3-color-palette-oxford-60",
        description="...",
        hex_value="#0f5499",
    ),
    FTColor(
        name="oxford-70",
        css_variable="--o3-color-palette-oxford-70",
        description="...",
        hex_value="#1262b3",
    ),
    FTColor(
        name="oxford-80",
        css_variable="--o3-color-palette-oxford-80",
        description="...",
        hex_value="#1470cc",
    ),
    FTColor(
        name="oxford-90",
        css_variable="--o3-color-palette-oxford-90",
        description="...",
        hex_value="#177ee6",
    ),
    FTColor(
        name="oxford-100",
        css_variable="--o3-color-palette-oxford-100",
        description="...",
        hex_value="#1a8cff",
    ),
    FTColor(
        name="teal-20",
        css_variable="--o3-color-palette-teal-20",
        description="...",
        hex_value="#052f33",
    ),
    FTColor(
        name="teal-30",
        css_variable="--o3-color-palette-teal-30",
        description="...",
        hex_value="#08474d",
    ),
    FTColor(
        name="teal-40",
        css_variable="--o3-color-palette-teal-40",
        description="...",
        hex_value="#0a5e66",
    ),
    FTColor(
        name="teal-50",
        css_variable="--o3-color-palette-teal-50",
        description="...",
        hex_value="#0d7680",
    ),
    FTColor(
        name="teal-60",
        css_variable="--o3-color-palette-teal-60",
        description="...",
        hex_value="#0f8e99",
    ),
    FTColor(
        name="teal-70",
        css_variable="--o3-color-palette-teal-70",
        description="...",
        hex_value="#12a5b3",
    ),
    FTColor(
        name="teal-80",
        css_variable="--o3-color-palette-teal-80",
        description="...",
        hex_value="#14bdcc",
    ),
    FTColor(
        name="teal-90",
        css_variable="--o3-color-palette-teal-90",
        description="...",
        hex_value="#17d4e6",
    ),
    FTColor(
        name="teal-100",
        css_variable="--o3-color-palette-teal-100",
        description="...",
        hex_value="#1aecff",
    ),
    FTColor(
        name="claret-30",
        css_variable="--o3-color-palette-claret-30",
        description="...",
        hex_value="#4d081f",
    ),
    FTColor(
        name="claret-40",
        css_variable="--o3-color-palette-claret-40",
        description="...",
        hex_value="#660a29",
    ),
    FTColor(
        name="claret-50",
        css_variable="--o3-color-palette-claret-50",
        description="...",
        hex_value="#800d33",
    ),
    FTColor(
        name="claret-60",
        css_variable="--o3-color-palette-claret-60",
        description="...",
        hex_value="#990f3d",
    ),
    FTColor(
        name="claret-70",
        css_variable="--o3-color-palette-claret-70",
        description="...",
        hex_value="#b31247",
    ),
    FTColor(
        name="claret-80",
        css_variable="--o3-color-palette-claret-80",
        description="...",
        hex_value="#cc1452",
    ),
    FTColor(
        name="claret-90",
        css_variable="--o3-color-palette-claret-90",
        description="...",
        hex_value="#e6175c",
    ),
    FTColor(
        name="claret-100",
        css_variable="--o3-color-palette-claret-100",
        description="...",
        hex_value="#ff1a66",
    ),
    FTColor(
        name="wheat-100",
        css_variable="--o3-color-palette-wheat-100",
        description="...",
        hex_value="#ffebd9",
    ),
)

FT_COLOR_BY_NAME = {color.name: color for color in FT_COLOR_PALETTE}


@dataclass(frozen=True)
class ThemeDefinition:
    """Minimal theme definition for FT surfaces."""

    slug: str
    background: FTColor
    body_text: FTColor
    comment_text: FTColor
    selection: FTColor


def get_color(name: str) -> FTColor:
    """Return a palette entry by name, raising ValueError when absent."""

    try:
        return FT_COLOR_BY_NAME[name]
    except KeyError as exc:  # pragma: no cover - defensive programming
        raise ValueError(f"Unknown FT color '{name}'") from exc


def create_standard_theme() -> ThemeDefinition:
    """Theme with paper background, standard text, and muted comments."""

    return ThemeDefinition(
        slug="standard",
        background=get_color("paper"),
        body_text=get_color("body-text"),
        comment_text=get_color("muted-text"),
        selection=get_color("sky"),
    )


def create_inverse_theme() -> ThemeDefinition:
    """Inverse variant using the matching FT inverse use cases."""

    return ThemeDefinition(
        slug="inverse",
        background=get_color("slate"),
        body_text=get_color("paper"),
        comment_text=get_color("muted-inverse-text"),
        selection=get_color("jade"),
    )


STANDARD_THEME = create_standard_theme()
INVERSE_THEME = create_inverse_theme()
