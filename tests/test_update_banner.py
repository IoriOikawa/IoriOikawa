"""Integration checks for the actual command used by GitHub Actions."""

from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "update_banner.py"
START = "<!-- time-banner:start -->"
END = "<!-- time-banner:end -->"
PREFIX = "# A personal profile\n\n"
SUFFIX = "\n\n## License\nOriginal art © Iori Oikawa.\n"
ORIGINAL = PREFIX + START + "\nOld banner\n" + END + SUFFIX


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
            ("2026-01-15T10:59:59Z", "los_angeles_midnight"),
            ("2026-01-15T11:00:00Z", "goldsmiths_morning"),
            ("2026-01-15T16:59:59Z", "goldsmiths_morning"),
            ("2026-01-15T17:00:00Z", "new_york_daytime"),
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
            ("2026-07-15T10:00:00Z", "goldsmiths_morning"),
            ("2026-07-15T16:00:00Z", "new_york_daytime"),
            ("2026-07-15T21:00:00Z", "cambridge_sunset"),
            ("2026-07-16T01:00:00Z", "los_angeles_midnight"),
        ]:
            with self.subTest(timestamp=timestamp):
                self.assert_scene(timestamp, asset)

    def test_daylight_saving_transition_days(self):
        for timestamp, asset in [
            ("2026-03-08T06:59:59Z", "los_angeles_midnight"),
            ("2026-03-08T07:00:00Z", "los_angeles_midnight"),
            ("2026-03-08T10:00:00Z", "goldsmiths_morning"),
            ("2026-11-01T05:30:00Z", "los_angeles_midnight"),
            ("2026-11-01T06:30:00Z", "los_angeles_midnight"),
            ("2026-11-01T11:00:00Z", "goldsmiths_morning"),
        ]:
            with self.subTest(timestamp=timestamp):
                self.assert_scene(timestamp, asset)

    def test_accepts_explicit_non_utc_offset(self):
        self.assert_scene("2026-07-15T12:00:00-04:00", "new_york_daytime")

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
