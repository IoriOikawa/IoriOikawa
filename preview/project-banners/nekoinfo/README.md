# nekoinfo responsive project banner

Approved direction: cartoon Dr. Ginger in front of a small computer displaying
one large cat kaomoji, a cream background, mint and graphite accents, and the
same rounded-card treatment as the existing profile project banners.

The artwork is an illustration, not a screenshot of the application.

Dr. Ginger is based on the user's photo (`IMG_2172.HEIC`): an orange-and-white
short-haired adult cat with a round face, orange tabby forehead, white nose
blaze/muzzle/chest/paws and muted olive-gray eyes. The photo is used as an
identity reference and is not included among the banner assets.

- Desktop: `assets/projects/nekoinfo/banner-desktop.png`, 1200 × 400.
- Mobile: `assets/projects/nekoinfo/banner-mobile.png`, 750 × 450.
- Transparent 26px rounded corners in both PNGs.
- `index.html` selects mobile at viewport widths up to 600px.
- Entire card links to <https://github.com/IoriOikawa/nekoinfo>.
- Editable layout: `assets/projects/nekoinfo/banner-source.html`.
- Current illustration: `asset_input/nekoinfo-dr-ginger-kaomoji-transparent.png`.

Copy: **nekoinfo** / **A native Linux monitor, with a little cat.**
Tags: **Linux**, **GTK4**, **System Monitor**. Action: **View project →**.

## Artwork revisions

1. Initial cat-and-monitor concept generated with the built-in imagegen tool.
2. Cat replaced with Dr. Ginger, using the user's photograph as an identity
   reference in built-in edit mode.
3. Cartoon styling: rounded shapes, clean outlines, restrained cel shading,
   simplified keyboard and screen.
4. Current edit: screen contents replaced with one large cat kaomoji. The
   current source is the previous cartoon illustration; genuine alpha is
   preserved. Built-in imagegen edit mode, transparent background enabled.

Exact prompt for the current edit:

> Use case: precise-object-edit. Edit ONLY the display contents inside the existing monitor in this transparent illustration. Remove the words CPU and Memory and both green chart lines. In their place, put ONE large friendly cat kaomoji, centered on the pale mint screen, reading exactly '(=^･ω･^=)'. This is typographic text made from characters, not a drawing of a cat and not an emoji icon. Use a simple dark sage/graphite rounded monospaced-looking typeface with thick clear strokes and ample breathing room so the cat face stays legible when reduced to a small banner. Keep the screen otherwise completely uncluttered: no graphs, no metric labels, no additional text, no decoration. Preserve EVERYTHING outside the screen exactly: the same cartoon Dr. Ginger orange-and-white short-haired cat, coat markings, round face, gray-olive eyes, expression, pose, white paws, curled tail, keyboard, monitor casing and stand, composition, sizes, outlines, colors, cel shading and contact shadow. Do not redraw or redesign the cat. Preserve genuine transparency around the illustration. No backdrop, no checkerboard, no watermark.

## Verification

Rendered both source canvases in Chrome at their native PNG dimensions. Checked
320, 390, 600, 601 and 1050px viewports: image selection, aspect ratio, image load,
whole-card link and horizontal overflow. Inspected light and dark previews, text
bounds and alpha values at all four corners of both exported images.

## README integration snippet

The root README includes this card after SoundCanvas, following user approval
of the Dr. Ginger illustration and the cat-kaomoji screen.

```html
<a href="https://github.com/IoriOikawa/nekoinfo">
  <picture>
    <source media="(max-width: 600px)" srcset="assets/projects/nekoinfo/banner-mobile.png">
    <img src="assets/projects/nekoinfo/banner-desktop.png"
         alt="nekoinfo: A native Linux monitor, with a little cat. Linux, GTK4, System Monitor. View project."
         width="1200">
  </picture>
</a>
```
