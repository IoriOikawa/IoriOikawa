#!/usr/bin/env python3
"""Update only the profile banner, using the current time in New York."""

import argparse
from datetime import datetime, timezone
from pathlib import Path
from zoneinfo import ZoneInfo


ROOT = Path(__file__).resolve().parents[1]
NEW_YORK = ZoneInfo("America/New_York")
START = "<!-- time-banner:start -->"
END = "<!-- time-banner:end -->"


def banner_at(instant: datetime) -> str:
    """Return a Markdown image for an offset-aware instant."""
    if instant.utcoffset() is None:
        raise ValueError("timestamp must include a timezone offset or Z")
    hour = instant.astimezone(NEW_YORK).hour
    if 6 <= hour < 12:
        scene, description = "goldsmiths_morning", "Morning at Goldsmiths, London"
    elif 12 <= hour < 17:
        scene, description = "new_york_daytime", "Daytime in New York"
    elif 17 <= hour < 21:
        scene, description = "cambridge_sunset", "Sunset in Cambridge, Massachusetts"
    else:
        scene, description = "los_angeles_midnight", "Midnight in Los Angeles"

    asset = Path("asset_input") / f"{scene}.gif"
    if not (ROOT / asset).is_file():
        raise ValueError(f"banner asset is missing: {asset}")
    return f"![{description}; scenes follow New York time]({asset.as_posix()})"


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
    updated = original[:start] + newline + banner_at(instant) + newline + original[end:]
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
    print("Banner updated." if changed else "Banner unchanged.")


if __name__ == "__main__":
    main()
