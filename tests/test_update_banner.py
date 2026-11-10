"""Integration checks for the actual command used by GitHub Actions."""

from pathlib import Path
from datetime import datetime, timedelta
from html.parser import HTMLParser
import re
import runpy
import subprocess
import sys
import tempfile
import unittest
from urllib.parse import parse_qs, urlsplit


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "update_banner.py"
START = "<!-- time-banner:start -->"
END = "<!-- time-banner:end -->"
PREFIX = "# A personal profile\n\n"
SUFFIX = "\n\n## License\nOriginal art © Iori Oikawa.\n"
ORIGINAL = PREFIX + START + "\nOld banner\n" + END + SUFFIX


class TypingSources(HTMLParser):
    def __init__(self, content):
        super().__init__()
        self.sources = []
        self.feed(content)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        url = attrs.get("srcset") if tag == "source" else attrs.get("src")
        if url and urlsplit(url).netloc == "readme-typing-svg.demolab.com":
            self.sources.append((attrs.get("media", "fallback"), parse_qs(urlsplit(url).query)))


class BannerCommandTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.readme = Path(self.temp.name) / "README.md"
        self.readme.write_text(ORIGINAL, encoding="utf-8")

    def run_banner(self, timestamp):
        return subprocess.run(
            [sys.executable, str(SCRIPT), "--readme", str(self.readme),
             "--at", timestamp],
            capture_output=True, text=True, cwd=self.temp.name,
        )

    def assert_scene(self, timestamp, asset):
        result = self.run_banner(timestamp)
        self.assertEqual(result.returncode, 0, result.stderr)
        content = self.readme.read_text(encoding="utf-8")
        self.assertIn(f"(asset_input/{asset}.gif)", content)
        self.assertTrue(content.startswith(PREFIX + START))
        self.assertTrue(content.endswith(END + SUFFIX))
        self.assertEqual(content.count(".gif)"), 1)

    def test_exact_boundaries_in_winter(self):
        for timestamp, asset in [
            ("2026-01-15T09:59:59Z", "los_angeles_midnight"),
            ("2026-01-15T10:00:00Z", "goldsmiths_morning"),
            ("2026-01-15T13:59:59Z", "goldsmiths_morning"),
            ("2026-01-15T14:00:00Z", "new_york_daytime"),
            ("2026-01-15T21:59:59Z", "new_york_daytime"),
            ("2026-01-15T22:00:00Z", "cambridge_sunset"),
            ("2026-01-16T01:59:59Z", "cambridge_sunset"),
            ("2026-01-16T02:00:00Z", "los_angeles_midnight"),
            ("2026-01-16T05:00:00Z", "los_angeles_midnight"),
        ]:
            with self.subTest(timestamp=timestamp):
                self.assert_scene(timestamp, asset)

    def test_summer_uses_daylight_saving_offset(self):
        for timestamp, asset in [
            ("2026-07-15T08:59:59Z", "los_angeles_midnight"),
            ("2026-07-15T09:00:00Z", "goldsmiths_morning"),
            ("2026-07-15T12:59:59Z", "goldsmiths_morning"),
            ("2026-07-15T13:00:00Z", "new_york_daytime"),
            ("2026-07-15T21:00:00Z", "cambridge_sunset"),
            ("2026-07-16T01:00:00Z", "los_angeles_midnight"),
        ]:
            with self.subTest(timestamp=timestamp):
                self.assert_scene(timestamp, asset)

    def test_daylight_saving_transition_days(self):
        for timestamp, asset in [
            ("2026-03-08T06:59:59Z", "los_angeles_midnight"),
            ("2026-03-08T07:00:00Z", "los_angeles_midnight"),
            ("2026-03-08T08:59:59Z", "los_angeles_midnight"),
            ("2026-03-08T09:00:00Z", "goldsmiths_morning"),
            ("2026-11-01T05:30:00Z", "los_angeles_midnight"),
            ("2026-11-01T06:30:00Z", "los_angeles_midnight"),
            ("2026-11-01T09:59:59Z", "los_angeles_midnight"),
            ("2026-11-01T10:00:00Z", "goldsmiths_morning"),
        ]:
            with self.subTest(timestamp=timestamp):
                self.assert_scene(timestamp, asset)

    def test_accepts_explicit_non_utc_offset(self):
        self.assert_scene("2026-07-15T09:00:00-04:00", "new_york_daytime")

    def test_greeting_matches_the_banner_at_each_time_boundary(self):
        for timestamp, asset, welcome in [
            ("2026-07-15T04:59:59-04:00", "los_angeles_midnight", "Hello, night owl!"),
            ("2026-07-15T05:00:00-04:00", "goldsmiths_morning", "Good morning, welcome!"),
            ("2026-07-15T08:59:59-04:00", "goldsmiths_morning", "Good morning, welcome!"),
            ("2026-07-15T09:00:00-04:00", "new_york_daytime", "Good afternoon, welcome!"),
            ("2026-07-15T16:59:59-04:00", "new_york_daytime", "Good afternoon, welcome!"),
            ("2026-07-15T17:00:00-04:00", "cambridge_sunset", "Good evening, welcome!"),
            ("2026-07-15T20:59:59-04:00", "cambridge_sunset", "Good evening, welcome!"),
            ("2026-07-15T21:00:00-04:00", "los_angeles_midnight", "Hello, night owl!"),
        ]:
            with self.subTest(timestamp=timestamp):
                self.assert_scene(timestamp, asset)
                sources = TypingSources(self.readme.read_text(encoding="utf-8")).sources
                self.assertEqual(len(sources), 4)
                for _, query in sources:
                    self.assertEqual(query["lines"][0].split(";")[0], welcome)

    def test_workflow_checks_soon_after_each_actual_scene_change(self):
        workflow = (ROOT / ".github/workflows/update-banner.yml").read_text()
        schedules = re.findall(
            r"^\s*- cron: ['\"]([^'\"]+)['\"]\s*\n"
            r"\s+timezone: ['\"]([^'\"]+)['\"]",
            workflow, re.MULTILINE,
        )
        self.assertTrue(schedules, "Expected timezone-aware banner schedules")
        module = runpy.run_path(str(SCRIPT))
        new_york, banner_at = module["NEW_YORK"], module["banner_at"]
        for cron, zone in schedules:
            self.assertEqual(zone, new_york.key)
            self.assertEqual(len(cron.split()), 5)

        def matches(cron, instant):
            # The workflow uses comma-separated values and wildcards only.
            values = (instant.minute, instant.hour, instant.day, instant.month,
                      (instant.weekday() + 1) % 7)
            return all(field == "*" or value in map(int, field.split(","))
                       for value, field in zip(values, cron.split()))

        for month, day in [(1, 15), (7, 15), (3, 8), (11, 1)]:
            for hour in range(24):
                boundary = datetime(2026, month, day, hour, tzinfo=new_york)
                before = boundary - timedelta(seconds=1)
                if banner_at(before) == banner_at(boundary):
                    continue
                with self.subTest(boundary=boundary.isoformat()):
                    self.assertTrue(
                        any(matches(cron, boundary + timedelta(minutes=delay))
                            for cron, _ in schedules for delay in range(1, 6)),
                        "No scheduled check within five minutes after this scene changes",
                    )

    def test_typing_preserves_the_exact_sentences_and_groups_them_together(self):
        self.assert_scene("2026-07-15T12:00:00-04:00", "new_york_daytime")
        content = self.readme.read_text(encoding="utf-8")
        sources = TypingSources(content).sources
        self.assertEqual(len(sources), 4)
        second = "As a hacker, a professor, a musician, a kigu..."
        third = "Is there anything I can do to make you code better?"
        for media, query in sources:
            with self.subTest(media=media):
                lines = query["lines"][0].split(";")
                if "max-width" in media:
                    self.assertEqual(" ".join(lines[1:3]), second)
                    self.assertEqual(" ".join(lines[3:5]), third)
                else:
                    self.assertEqual(lines[1:], [second, third])
                self.assertEqual(query["groups"], [str(len(lines))])
                self.assertEqual(query["multiline"], ["true"])
                self.assertEqual(query["repeat"], ["true"])
        self.assertLess(content.index(".gif)"), content.index("<picture>"))
        self.assertIn(second, content)
        self.assertIn(third, content)

    def test_typing_has_mobile_and_dark_theme_sources(self):
        self.assert_scene("2026-07-15T12:00:00-04:00", "new_york_daytime")
        sources = TypingSources(self.readme.read_text(encoding="utf-8")).sources
        self.assertEqual([media for media, _ in sources], [
            "(max-width: 600px) and (prefers-color-scheme: dark)",
            "(max-width: 600px)",
            "(prefers-color-scheme: dark)",
            "fallback",
        ])
        self.assertNotEqual(sources[0][1]["color"], sources[1][1]["color"])

    def test_unchanged_scene_does_not_rewrite_file(self):
        self.assert_scene("2026-07-15T12:00:00-04:00", "new_york_daytime")
        before = self.readme.stat().st_mtime_ns
        result = self.run_banner("2026-07-15T13:00:00-04:00")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(self.readme.stat().st_mtime_ns, before)

    def test_invalid_markers_fail_without_changing_content(self):
        for content in [
            PREFIX + SUFFIX,
            START + "\n" + SUFFIX,
            END + "\n" + START,
            ORIGINAL + START,
            ORIGINAL + END,
        ]:
            with self.subTest(content=content):
                self.readme.write_text(content, encoding="utf-8")
                result = self.run_banner("2026-07-15T16:00:00Z")
                self.assertNotEqual(result.returncode, 0)
                self.assertIn("marker", result.stderr.lower())
                self.assertEqual(self.readme.read_text(encoding="utf-8"), content)

    def test_invalid_or_naive_timestamp_fails_without_writing(self):
        for timestamp in ["", "tomorrow", "2026-07-15T12:00:00"]:
            with self.subTest(timestamp=timestamp):
                self.readme.write_text(ORIGINAL, encoding="utf-8")
                result = self.run_banner(timestamp)
                self.assertNotEqual(result.returncode, 0)
                self.assertIn("timestamp", result.stderr.lower())
                self.assertEqual(self.readme.read_text(encoding="utf-8"), ORIGINAL)

    def test_preserves_crlf_and_surrounding_unicode_bytes(self):
        original = ORIGINAL.replace("\n", "\r\n").encode("utf-8")
        self.readme.write_bytes(original)
        result = self.run_banner("2026-07-15T16:00:00Z")
        self.assertEqual(result.returncode, 0, result.stderr)
        updated = self.readme.read_bytes()
        self.assertTrue(updated.startswith((PREFIX + START).replace("\n", "\r\n").encode()))
        self.assertTrue(updated.endswith((END + SUFFIX).replace("\n", "\r\n").encode()))
        self.assertNotIn(b"\n", updated.replace(b"\r\n", b""))

    def test_missing_asset_fails_without_writing(self):
        script = Path(self.temp.name) / "scripts" / "update_banner.py"
        script.parent.mkdir()
        script.write_bytes(SCRIPT.read_bytes())
        result = subprocess.run(
            [sys.executable, str(script), "--readme", str(self.readme),
             "--at", "2026-07-15T16:00:00Z"],
            capture_output=True, text=True,
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("asset is missing", result.stderr)
        self.assertEqual(self.readme.read_text(encoding="utf-8"), ORIGINAL)


if __name__ == "__main__":
    unittest.main()
