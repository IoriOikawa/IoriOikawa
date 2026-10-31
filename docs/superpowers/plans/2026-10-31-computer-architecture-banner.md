# ComputerArchitecture-L0 responsive banner

**Goal:** Create the next local project banner in the established image-pair format.

**Design:** Keep 1200 × 400 desktop and 750 × 450 mobile canvases with the
600-pixel switch. Preserve the supplied portrait as an original input and use
a rounded portrait window. Use warm rose, cocoa and charcoal from the artwork.
The title is `ComputerArchitecture-L0`, with an intentional wrap opportunity
for narrow layouts. English description: “A self-study library for computer
architecture.” Display `TEACHING MATERIAL` above the desktop title, the exact
status `Developing♡`, a separate `CSCI260` bubble and a `View project` entrance.
Render the ASCII digit 0 in `-L0` using a distinguishable monospaced zero glyph.
The whole card links to `https://github.com/IoriOikawa/ComputerArchitecture-L0`;
the trailing Chinese comma in the supplied link is punctuation, not part of it.

## Tasks

- [x] Verify project purpose and copy the supplied image without changing it.
- [x] Create `assets/projects/computer-architecture-l0/banner-source.html`.
- [x] Export the desktop/mobile PNG pair and add an independent responsive
  preview under `preview/project-banners/computer-architecture-l0/`.
- [x] Check source dimensions, title and status visibility, image/link selection,
  text bounds and horizontal overflow at 320, 390, 600, 601 and 1050 pixels.
- [x] Visually inspect both versions and leave the work local for review.

## Local verification before publishing

- Read the current repository README to confirm the self-study course-library
  description. The supplied portrait was copied byte-for-byte unchanged.
- Exported PNG headers match the expected dimensions. Native title, description
  and exact `Developing♡` / `CSCI260` labels fit both canvases.
- Visually checked both native artwork images and the 390-pixel preview.
- Viewports 320, 390 and 600 load the mobile PNG; 601 and 1050 load desktop.
  All images load and the page has no horizontal overflow. Both variants link
  to the verified project URL without the supplied trailing comma.
- The main profile README hash and repository HEAD remain unchanged.
- No commit or push was performed.

## Publication

After reviewing the revised title, heading and both bubble tags, the user
approved publishing. Add this responsive card after TLDrRacket in the profile
Projects section and publish only this project's artwork and supporting files.
Keep the Tenpai Prism sample local.
