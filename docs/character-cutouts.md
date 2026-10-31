# Transparent character illustrations

The profile uses sibling transparent PNGs so the original artwork remains
available unchanged:

| Original | README asset |
| --- | --- |
| `asset_input/omote_halloween.png` | `asset_input/omote_halloween-transparent.png` |
| `asset_input/ura_halloween.png` | `asset_input/ura_halloween-transparent.png` |

Both final assets were made with the built-in imagegen editing tool with
`transparent_background: true`, using the respective original as the edit target.
They are 1024 × 1536 RGBA PNGs. These are AI-assisted extractions; the original
files are retained for exact source fidelity. The first iteration added ink-like
outlines, so the selected second iteration emphasized the original soft rendering.

## Final prompts

The following prompt was used once for each original. Substitute `SUBJECT` with
`blue-haired Omote and the floating jack-o-lantern` for Omote and
`pink-haired Ura, the book, and the trident` for Ura:

> BACKGROUND EXTRACTION ONLY. This attached image is the EDIT TARGET, not a style reference. Make a transparent PNG cutout of the exact existing SUBJECT from this original image. Preserve the original character pixels, rendering, texture and soft sculpted three-dimensional shading as faithfully as possible. This is NOT an illustration redraw: DO NOT convert to flat anime/cel shading, DO NOT introduce black ink contour lines, DO NOT smooth away original material texture, DO NOT redesign or repaint. Retain the exact original pose, facial expression, proportions, framing and every original costume detail and accessory. The only change requested is to erase the dark charcoal background to alpha transparency, including visible background holes within the character silhouette. Keep dark clothing, boots, shadows and all foreground props. Output real transparent alpha, no glow, no colored halo, no replacement backdrop, no checkerboard texture, no drop shadow. Full body, original 2:3 portrait composition. Faithful original soft 3D-rendered appearance is essential.
