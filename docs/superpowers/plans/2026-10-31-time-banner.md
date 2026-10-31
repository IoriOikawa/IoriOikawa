# Time-aware profile banner implementation plan

> Execute inline in this session, following the selected New York timezone design.

**Goal:** Show the appropriate animated scene directly in the GitHub profile README.

**Architecture:** A Python script replaces a marked README block. GitHub Actions
checks the time and commits only scene changes. Original GIFs stay in `asset_input`.

**Tech stack:** Python 3.11+ standard library, unittest, GitHub Actions, Markdown.

## Tasks

- [x] Add `tests/test_update_banner.py`: invoke the script against temporary
  READMEs with explicit ISO timestamps. Cover every transition, winter/summer
  UTC conversion, DST transitions, unchanged runs, text preservation, malformed
  markers and invalid timestamps. Run `python3 -m unittest discover -s tests -v`
  and confirm failure because the updater is absent.
- [x] Add `scripts/update_banner.py`: use `ZoneInfo('America/New_York')`, select
  morning from 6, daytime from 12, sunset from 17 and midnight from 21. Replace
  only text between `<!-- time-banner:start -->` and `<!-- time-banner:end -->`.
  Expose `--at` and `--readme`; reject naive timestamps, invalid markers and
  missing assets before writing. Skip writing when content is unchanged.
  Re-run the test command and require all tests to pass.
- [x] Add the marked banner above the existing README content, preserving the
  introduction and license. Run `python3 scripts/update_banner.py` to select the
  current scene. Add `.gitignore` for `.DS_Store` and Python caches.
- [x] Add `.github/workflows/update-banner.yml`: schedule `7,22,37,52 * * * *`,
  relevant push paths and manual dispatch. Restrict writes to the default
  branch, serialize jobs, check out the latest default-branch tip, run tests,
  update, and conditionally commit/push only README without force.
- [x] Add `docs/banner.md` with the time table, activation instructions,
  local preview commands, workflow limits and test command.
- [x] Validate the workflow, run the tests, preview each GIF, review the final
  diff and report local completion separately from GitHub activation.

## Verification results

- Nine unittest cases pass, with subtests covering all scene boundaries and DST.
- `actionlint` v1.7.12 reports no workflow errors.
- All four GIFs and timestamp-driven previews have been checked.
- Existing README content is preserved byte-for-byte after the new banner.
- Independent code review found no remaining actionable issues.
- GitHub activation is verified separately after publishing to the default branch.
