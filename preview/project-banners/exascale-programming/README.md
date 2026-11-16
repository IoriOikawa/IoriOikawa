# Exascale Programming responsive project banner

This profile card links to <https://github.com/IoriOikawa/tutorial-multi-gpu>.
It presents the user's SC26 multi-GPU experiments and study notes.

- Title: **Exascale Programming**.
- Eyebrow: **SC26 · HANDS-ON STUDY** (desktop only).
- Description: **Hands-on experiments and study notes from JUPITER.**
- Tags: **Nsight**, **MPI**, **NCCL/NVSHMEM**.
- Action: **View project →**.

Desktop uses a 1200 × 400 canvas with the existing character, laptop and two
miniature JUPITER-style cabinets. Mobile uses a 750 × 450 canvas, a two-line
title, larger relative text and one cabinet. Both PNGs have transparent outer
corners with a 26px radius. The preview selects mobile at widths up to 600px.

## Files

- `assets/projects/exascale-programming/banner-source.html`: editable layout;
  append `?layout=desktop` or `?layout=mobile` when exporting one canvas.
- `assets/projects/exascale-programming/banner-desktop.png`: desktop image.
- `assets/projects/exascale-programming/banner-mobile.png`: compact image.
- `asset_input/exascale-programming-original.png`: byte-identical copy of the
  supplied repository banner, retained as the character and cabinet reference.
- `asset_input/exascale-programming-desktop-illustration.png`: isolated desktop
  illustration, generated with the built-in imagegen tool in edit mode.
- `asset_input/exascale-programming-mobile-illustration.png`: its compact
  one-cabinet edit, also generated with built-in imagegen.

The root README includes this responsive card after nekoinfo in the Projects
section, following the user's approval of both banner variants.

## Illustration prompts

Both image edits use a genuinely transparent background. Desktop reference:
`tutorial-multi-gpu/docs/assets/sc26-multi-gpu-banner.png`.

### Desktop

> Use case: compositing / identity-preserve. Reference image: the provided SC26 banner. Create an isolated compact illustration for a GitHub profile project card. Preserve the SAME cheerful brown-haired anime girl from the reference: brown eyes, long twin ponytails tied with dark purple ribbons, a small ahoge, navy-and-white sailor outfit, warm friendly excited expression, and the same polished soft detailed anime illustration style. Show her at a compact open dark laptop in the foreground, facing the viewer, with one hand poised near the keyboard and a small excited raised fist. Add TWO miniature JUPITER-style supercomputer rack cabinets just behind her on the right: graphite cabinets with the reference's distinctive curved vent patterns and restrained ice-blue LED lines. A couple of subtle glowing blue connection lines between laptop and cabinets suggest cooperating GPUs. The character should remain the visual focus, large and clearly recognizable when the whole illustration is reduced to about 350 pixels wide; racks are supporting objects, not a giant background hall. Keep the group compact and roughly square, with the girl's head and upper body, laptop and both rack cabinets fully inside the canvas; avoid excessive transparent padding. Preserve warm orange hair highlights, purple bows, blue/graphite rack colors. Background must be genuinely transparent PNG, with a very soft minimal contact shadow. Remove all banner titles, subtitle, SC26 text, notebook, coffee cup, room architecture and floor. No typography except a tiny optional JUPITER mark on the foremost rack; no brand logos, no project title, no watermark, no checkerboard or solid backdrop. The result is a character-and-mini-supercomputer illustration only; all project text will be typeset separately.

### Mobile

Reference: the generated desktop illustration above.

> Use case: precise-object-edit / identity-preserve. Edit the supplied transparent character-and-JUPITER illustration for the mobile version of the same project banner. Keep the girl's identity, brown eyes and hair, twin ponytails, purple bows, sailor outfit, cheerful expression, hand pose, the laptop and its stickers, detailed soft anime rendering, warm highlights and color palette exactly consistent. Change only the supporting hardware: remove the smaller rear cabinet so there is exactly ONE miniature graphite JUPITER cabinet behind her on the right, retaining its curved vent motif, ice-blue LED line and subtle blue connection to the laptop. Tuck that single cabinet slightly closer behind the girl's shoulder to make the grouping compact and portrait-friendly without covering her face or hands. The character and laptop remain dominant and fully visible; the complete top hair strand, ponytails and laptop must fit within the frame. Keep the image tightly framed with safe margin, genuine transparent background and minimal soft contact shadow; no floor rectangle, no added text, no banner title, no watermark, no checkerboard. Preserve everything else.

## Verification

Both source layouts were rendered in Chrome at native PNG dimensions. The title,
three exact tags and vertical/horizontal text bounds pass. The preview was
checked at 320, 390, 600, 601 and 1050px for image selection, aspect ratio,
loading, whole-card link and horizontal overflow. Light and dark previews were
inspected. All four outer corner pixels are transparent in both exported PNGs.

## README integration snippet

```html
<a href="https://github.com/IoriOikawa/tutorial-multi-gpu">
  <picture>
    <source media="(max-width: 600px)" srcset="assets/projects/exascale-programming/banner-mobile.png">
    <img src="assets/projects/exascale-programming/banner-desktop.png"
         alt="Exascale Programming: Hands-on experiments and study notes from JUPITER. Nsight, MPI, NCCL/NVSHMEM. View project."
         width="1200">
  </picture>
</a>
```
