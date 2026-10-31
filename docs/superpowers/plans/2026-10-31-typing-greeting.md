# Time-aware typing greeting

**Goal:** Add DenverCoder1/readme-typing-svg immediately below the time banner,
with a time-aware welcome followed by the user's two exact sentences.

**Design:** Keep the GIF and greeting in the same generated README block so one
New York time decision updates both together. Use a three-line desktop SVG and
a mobile SVG that breaks long sentences at word boundaries. Lines type in order,
remain visible, then repeat together. Preserve the existing character/title row.
Implemented locally first; publishing was approved after the preview.

**Content:**

1. Morning: `Good morning, welcome!`; afternoon: `Good afternoon, welcome!`;
   evening: `Good evening, welcome!`; late night: `Hello, night owl!`.
2. `As a hacker, a professor, a musician, a kigu...`
3. `Is there anything I can do to make you code better?`

## Tasks

- [x] Confirm upstream multiline/grouping behavior and live SVG response.
- [x] Add integration checks proving GIF/greeting alignment at all time
  boundaries, exact user text, responsive source selection and no unrelated
  README changes. Run the added checks before implementation.
- [x] Extend `scripts/update_banner.py` to select scene and welcome together
  and build escaped typing-SVG URLs with Python's standard library.
- [x] Run the updater locally to place the component under the banner.
- [x] Add an animated local preview and document the service dependency,
  time mapping, line wrapping and local preview instructions.
- [x] Run the full checks; inspect desktop/mobile and light/dark rendering,
  text bounds, sequential typing and repeat behavior. Keep the draft local until
  publishing is approved.

## Verification results

- All 12 unittest cases pass, including synchronization at every time boundary,
  exact text preservation, source variants, idempotency and CRLF preservation.
- The live service returns the requested grouped SVGs with embedded Fira Code.
- Browser checks confirm earlier rows remain visible while subsequent rows
  type, all rows are fully visible before the reset, and the cycle restarts.
- All text bounds fit the 900 × 110 desktop and 420 × 140 mobile SVG canvases.
- At 1050 and 390 pixels, both light and dark previews load the intended SVG
  and original artwork without horizontal overflow.
- Workflow syntax validation passes; existing character/title and license
  content after the generated block remains byte-for-byte unchanged.
- Independent code review found no actionable issues.
- Publication is verified separately after user approval.
