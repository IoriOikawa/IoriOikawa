#!/usr/bin/env python3
"""Update the profile banner and typing greeting using the time in New York."""

import argparse
from datetime import datetime, timezone
from html import escape
from pathlib import Path
from textwrap import wrap
from urllib.parse import urlencode
from zoneinfo import ZoneInfo


ROOT = Path(__file__).resolve().parents[1]
NEW_YORK = ZoneInfo("America/New_York")
START = "<!-- time-banner:start -->"
END = "<!-- time-banner:end -->"
ROLE_TEXT = "As a hacker, a professor, a musician, a kigu..."
HELP_TEXT = "Is there anything I can do to make you code better?"


def typing_svg_url(greeting: str, *, mobile: bool, dark: bool) -> str:
    """Use one animation group so every typed line remains until the reset."""
    lines = [greeting, ROLE_TEXT, HELP_TEXT]
    if mobile:
        lines = [greeting] + wrap(ROLE_TEXT, 26) + wrap(HELP_TEXT, 26)
    parameters = {
        "font": "Fira Code",
        "size": 18 if mobile else 22,
        "duration": 1800 if mobile else 2800,
        "pause": 4000,
        "color": "A9D5E2" if dark else "476D82",
        "background": "00000000",
        "center": "true",
        "vCenter": "true",
        "multiline": "true",
        "repeat": "true",
        "groups": len(lines),
        "width": 420 if mobile else 900,
        "height": 140 if mobile else 110,
        "lines": ";".join(lines),
    }
    return "https://readme-typing-svg.demolab.com/?" + urlencode(parameters)


def typing_greeting(greeting: str) -> str:
    """Offer readable mobile artwork and light/dark color variants."""
    sources = [
        ('(max-width: 600px) and (prefers-color-scheme: dark)', True, True),
        ('(max-width: 600px)', True, False),
        ('(prefers-color-scheme: dark)', False, True),
    ]
    markup = ['<p align="center">', '  <picture>']
    for media, mobile, dark in sources:
        url = escape(typing_svg_url(greeting, mobile=mobile, dark=dark), quote=True)
        markup.append(f'    <source media="{media}" srcset="{url}">')
    url = escape(typing_svg_url(greeting, mobile=False, dark=False), quote=True)
    alt = escape(f"{greeting} {ROLE_TEXT} {HELP_TEXT}", quote=True)
    markup.extend([
        f'    <img src="{url}" alt="{alt}" width="900">',
        '  </picture>',
        '</p>',
    ])
    return "\n".join(markup)


def banner_at(instant: datetime) -> str:
    """Select the GIF and welcome together for an offset-aware instant."""
    if instant.utcoffset() is None:
        raise ValueError("timestamp must include a timezone offset or Z")
    hour = instant.astimezone(NEW_YORK).hour
    if 5 <= hour < 9:
        scene, description = "goldsmiths_morning", "Morning at Goldsmiths, London"
        greeting = "Good morning, welcome!"
    elif 9 <= hour < 17:
        scene, description = "new_york_daytime", "Daytime in New York"
        greeting = "Good afternoon, welcome!"
    elif 17 <= hour < 21:
        scene, description = "cambridge_sunset", "Sunset in Cambridge, Massachusetts"
        greeting = "Good evening, welcome!"
    else:
        scene, description = "los_angeles_midnight", "Midnight in Los Angeles"
        greeting = "Hello, night owl!"

    asset = Path("asset_input") / f"{scene}.gif"
    if not (ROOT / asset).is_file():
        raise ValueError(f"banner asset is missing: {asset}")
    image = f"![{description}; scenes follow New York time]({asset.as_posix()})"
    return image + "\n\n" + typing_greeting(greeting)


def update_readme(path: Path, instant: datetime) -> bool:
    """Replace the marked block, preserving all bytes outside it."""
    original = path.read_bytes().decode("utf-8")
    if original.count(START) != 1 or original.count(END) != 1:
        raise ValueError("README must contain exactly one pair of banner markers")
    start = original.index(START) + len(START)
    end = original.index(END)
    if end < start:
        raise ValueError("banner start marker must precede the end marker")

    newline = "\r\n" if "\r\n" in original else "\n"
    block = banner_at(instant).replace("\n", newline)
    updated = original[:start] + newline + block + newline + original[end:]
    if updated == original:
        return False
    path.write_bytes(updated.encode("utf-8"))
    return True


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--readme", type=Path, default=ROOT / "README.md")
    parser.add_argument("--at", help="preview an ISO 8601 timestamp with offset or Z")
    args = parser.parse_args()
    try:
        if args.at is not None:
            try:
                instant = datetime.fromisoformat(args.at)
            except ValueError as error:
                raise ValueError("timestamp must be ISO 8601 with a timezone offset or Z") from error
        else:
            instant = datetime.now(timezone.utc)
        changed = update_readme(args.readme, instant)
    except (ValueError, OSError) as error:
        parser.error(str(error))
    print("Banner and greeting updated." if changed else "Banner and greeting unchanged.")


if __name__ == "__main__":
    main()
