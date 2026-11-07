# SoundCanvas responsive project banner

- Desktop: `assets/projects/soundcanvas/banner-desktop.png`, 1200 × 400.
- Mobile: `assets/projects/soundcanvas/banner-mobile.png`, 750 × 450.
- The README selects the mobile image at viewport widths up to 600px.
- Both images have 26px rounded corners with transparent outer pixels, so the
  shape also works in GitHub dark mode without relying on inline CSS.
- The entire image links to <https://github.com/IoriOikawa/SoundCanvas>.

Open `index.html` to preview the responsive card. Editable artwork is in
`assets/projects/soundcanvas/banner-source.html`; use `?layout=desktop` or
`?layout=mobile` to show a single canvas when exporting.

The supplied original is retained in
`asset_input/soundcanvas-project-banner-original.png`. Desktop preserves its
composition. Mobile uses the isolated illustration with freshly typeset copy
and all three original tags.

## Illustration cutout

Prepared with the built-in imagegen tool in edit mode, with a transparent
background. The source file is the supplied original banner; the generated
cutout is `asset_input/soundcanvas-illustration-transparent.png`.

Exact prompt:

> Use case: background-extraction / identity-preserve. Edit target: the supplied SoundCanvas project banner. Extract ONLY the existing illustration on the left: the brown-haired green-eyed anime woman wearing black over-ear headphones and a dark sailor outfit, both hands carefully holding and touching a luminous teal globe, golden sound-wave lines, water droplets, and the small glowing cream rabbit inside the globe. Output that isolated illustration as a genuinely transparent PNG cutout on a portrait canvas, tightly framed with the entire visible hair, headphones, face, hands and globe included; preserve the same bottom crop of the torso. Precisely preserve the reference character identity, facial expression, pose, colors, original soft detailed painterly anime rendering, the globe and rabbit. Do not redesign or add anything. Remove ALL typography, chips, card borders, decorative bottom-right triangle, and the cream background. Keep the teal/gold glow near the illustration with soft alpha edges, but leave the surrounding canvas fully transparent. No text, no watermark, no background rectangle or checkerboard.
