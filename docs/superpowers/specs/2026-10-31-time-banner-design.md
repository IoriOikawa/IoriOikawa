# Time-aware profile banner

## Decision

The profile README displays one of four existing animated GIFs according to
`America/New_York`, including daylight saving time. The user chose this shared
timezone after discussing GitHub README's inability to read a visitor's local
clock. No external hosting or image service is needed.

| New York local time | Asset |
| --- | --- |
| 06:00–11:59 | `asset_input/goldsmiths_morning.gif` |
| 12:00–16:59 | `asset_input/new_york_daytime.gif` |
| 17:00–20:59 | `asset_input/cambridge_sunset.gif` |
| 21:00–05:59 | `asset_input/los_angeles_midnight.gif` |

All four GIFs are 1200 × 400 and are displayed without cropping or re-encoding.
The locations are scenes representing times of day; their own local clocks do
not drive the selection. Boundaries are fixed rather than seasonal sunrise times.

## Alternatives considered

- Recommended and selected: GitHub Actions updates the README image reference.
  All visitors see the same scene; the four source GIFs remain unchanged.
- A GitHub Pages site can use each visitor's local clock, but the user prefers
  the banner directly inside the profile README.
- A static banner is simpler, but does not provide the requested daily cycle.

## Implementation

A Python standard-library script selects the scene with `zoneinfo` and rewrites
only a marked block at the top of README. It accepts an explicit offset-aware
timestamp for reproducible previews. Missing, repeated, or reversed markers
cause an error without writing. Missing source assets also cause an error.
An unchanged scene leaves the README file untouched.

A GitHub Actions workflow checks every 15 minutes at minutes 7, 22, 37 and 52,
on relevant default-branch pushes, and on manual dispatch. It runs tests before
updating and commits only README when its banner changes. The job uses the
built-in token with `contents: write`; it does not need a personal token.
Concurrent banner jobs are serialized; pushes never overwrite remote history.

## Operational limits

GitHub scheduling is best-effort, and images/pages can be cached. An already
open profile does not replace its scene until reloaded. A failed run leaves the
last working banner visible. The workflow must be on the default branch and
Actions must be enabled; branch protection can prevent the bot's commit.
GitHub can disable schedules in public repositories after 60 days of inactivity.

## Verification

Exercise all four scenes and exact transition boundaries with UTC input,
including winter and summer offsets and DST transition dates. Verify unrelated
README text is preserved, repeated runs do not rewrite the file, malformed
markers and naive timestamps fail safely, and all four referenced GIFs exist.
Validate workflow syntax and inspect the rendered banner at the original ratio.

## References

- [GitHub Markdown rendering and sanitization](https://github.com/github/markup#github-markup)
- [GitHub scheduled workflows](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#schedule)
