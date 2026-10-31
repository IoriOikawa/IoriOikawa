# Transparent character illustrations

The profile uses sibling transparent PNGs so the original artwork remains
available unchanged:

| Original | README asset |
| --- | --- |
| `asset_input/omote_halloween.png` | `asset_input/omote_halloween-transparent.png` |
| `asset_input/ura_halloween.png` | `asset_input/ura_halloween-transparent.png` |
| `asset_input/title.PNG` | `asset_input/title-transparent.png` |

The final assets were made with the built-in imagegen editing tool with
`transparent_background: true`, using the respective original as the edit target.
The character PNGs are 1024 × 1536; the title keeps its 1448 × 1086 canvas.
These are RGBA PNGs and AI-assisted extractions; the original
files are retained for exact source fidelity. The first iteration added ink-like
outlines, so the selected second iteration emphasized the original soft rendering.

## Character extraction prompts

The following prompt was used once for each original. Substitute `SUBJECT` with
`blue-haired Omote and the floating jack-o-lantern` for Omote and
`pink-haired Ura, the book, and the trident` for Ura:

> BACKGROUND EXTRACTION ONLY. This attached image is the EDIT TARGET, not a style reference. Make a transparent PNG cutout of the exact existing SUBJECT from this original image. Preserve the original character pixels, rendering, texture and soft sculpted three-dimensional shading as faithfully as possible. This is NOT an illustration redraw: DO NOT convert to flat anime/cel shading, DO NOT introduce black ink contour lines, DO NOT smooth away original material texture, DO NOT redesign or repaint. Retain the exact original pose, facial expression, proportions, framing and every original costume detail and accessory. The only change requested is to erase the dark charcoal background to alpha transparency, including visible background holes within the character silhouette. Keep dark clothing, boots, shadows and all foreground props. Output real transparent alpha, no glow, no colored halo, no replacement backdrop, no checkerboard texture, no drop shadow. Full body, original 2:3 portrait composition. Faithful original soft 3D-rendered appearance is essential.

## Title extraction prompt

> Use case: background-extraction. Edit target: the attached original Iori / PaperNeko / Oikawa illustrated title logo. Remove ONLY the plain white/off-white background outside the designed logo, making it truly transparent with an alpha channel. Preserve the exact original illustration, character, colors, painterly rendering, composition, lettering, typography, cat-shaped letter glyphs, blue-white sticker outlines, orange accents, paw prints, books, geometric decorations, tiny hanging cat charm and all other intentional design elements. Preserve the three text elements exactly as shown: 'Iori', 'PaperNeko', 'Oikawa'. Do not retype, correct, simplify, redesign or rearrange the lettering. The white lettering interiors, white fur highlights, white papers and white sticker border belong to the logo and must remain opaque; only the surrounding blank canvas and genuinely empty gaps should become transparent. Keep delicate pale-blue decorative lines and clean soft antialiased edges. No replacement background, no rectangular white plate, no glow, no drop shadow added. Keep original full-logo framing and 4:3 landscape canvas; no clipping any decorative element. Intended use: this transparent logo will sit between two character cutouts in a GitHub README on both light and dark themes. Output one transparent PNG.

## README composition

The transparent title replaces the welcome text between Omote and Ura. The
three columns use 28% / 44% / 28% widths. Character images have a requested
width of 220 pixels; the title uses 300 pixels. GitHub constrains images to
their column widths on narrow screens. The separate title above the row was
removed so the logo appears once.
