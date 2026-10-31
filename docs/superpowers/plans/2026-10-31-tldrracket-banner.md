# TLDrRacket responsive banner

**Goal:** Extend the approved Tenpai Prism banner format to TLDrRacket.
Build and review locally first, then publish following explicit approval.

**Design:** Reuse the 1200 × 400 desktop and 750 × 450 mobile canvases and
600-pixel image switch. Preserve the supplied `sicp.png` character unmodified.
Use indigo, slate and warm cream from the character artwork. The left side
shows the character, including her laptop and SICP book; the right side gives
the project name and a short description of the programming-languages course
reading companion, grounded in its current README. Link the whole image to
`https://github.com/IoriOikawa/TLDrRacket`.

The final requested English copy is exactly “An RAG reading companion for Racket
learners.”, with no second sentence. Both artwork sizes retain “View project”.
The copy wraps naturally while preserving the same font size.

## Tasks

- [x] Verify project scope from its repository and preserve the original image.
- [x] Add editable artwork in `assets/projects/tldrracket/banner-source.html`.
- [x] Render `banner-desktop.png` and `banner-mobile.png` in the same directory.
- [x] Add a TLDrRacket responsive preview and copyable README snippet under
  `preview/project-banners/tldrracket/`.
- [x] Check exact PNG dimensions, text bounds, preserved artwork and image/link
  selection at 320, 390, 600, 601 and 1050 pixels. Inspect both versions.
- [x] Leave the main profile README and existing Tenpai Prism sample unchanged;
  do not commit or push.

## Local verification before publishing

- Read the current repository README and HTTP entry point. Banner content
  reflects its course-reading and grounded-question-answering purpose.
- Supplied PNG copy is byte-for-byte identical to the attachment.
- Output headers match 1200 × 400 and 750 × 450. Native text fits both canvases.
- Both artwork versions and the 390-pixel mobile preview were visually checked.
- At 320, 390 and 600 pixels, the mobile source is selected; at 601 and 1050
  pixels, the desktop source is selected. No horizontal overflow; all images
  load and the entire card links to the specified project repository.
- Main README digest and repository HEAD remain unchanged; no commit or push.

## Publication

After reviewing the local banner and its English copy, the user approved
publishing and linking it. Add the responsive image pair to the profile's
Projects section, with the entire banner linking to the specified repository.
Publish only TLDrRacket materials; the Tenpai Prism sample remains local.
