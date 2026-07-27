# Grey Room — image recipe

Copy the block below, replace the `[SUBJECT: …]` line with your subject clause, and send it as-is. Everything under `STYLE`, `NEGATIVE SPACE` and `DO NOT INCLUDE` is load-bearing — keep it verbatim.

```text
[SUBJECT: describe the subject in one clause — e.g. "a stack of shipping containers", "a single ceramic cup", "an abstract network of nodes"]

Rendered as monochrome studio photography, or as a greyscale 3D render with the same
lighting discipline. Gallery-object treatment, not product-catalogue treatment.

STYLE — apply all of the following, they are not optional:
- strictly greyscale — zero saturation anywhere in the frame, no warm or cool cast,
  no colour temperature drift in the shadows
- soft even studio lighting from a large source with gentle falloff; light grey seamless
  background around #EFEFEF, subject values sitting between #767676 and #171717
- matte surfaces throughout — no gloss, no specular hotspots, no reflections
- one subject, centred or on a clean thirds placement, with generous empty space
- separation between subject and ground comes from subtle luminance difference, not from
  a hard edge, a rim light or a cast contact shadow
- shallow, quiet depth: a single soft floor shadow at most, no dramatic falloff

NEGATIVE SPACE: At least 40% of the frame must be empty light-grey ground, with the
largest clear run along one edge so a headline can sit over it.

DO NOT INCLUDE: any colour or colour cast, neon, harsh shadows, high-contrast blacks,
busy backgrounds, props or set dressing, text, numerals or logos in the image, visible
studio equipment, film grain, vignette borders.
```

**Target —** provider, model and resolution are all configurable; set them to whatever image stack you are using.
Recommended resolution: **1536×1024** (3:2 landscape). Use **1024×1536** for portrait slots and **1024×1024** for square cards.

## Hard constraints

These must survive any edit to the prompt. If the returned image breaks one, regenerate rather than retouch — and if you must retouch, `filter: grayscale(1)` in CSS is the backstop.

- Strictly greyscale — zero saturation anywhere in the frame.
- Soft even studio lighting with gentle falloff, light grey seamless background (~`#EFEFEF`).
- Matte surfaces, no gloss or specular hotspots.
- One subject, centred, with generous empty space.
- Subtle luminance separation between subject and ground rather than hard edges.
- Negative space — at least 40% of the frame must be empty light-grey ground.
- Never include legible text, numerals, logos or UI chrome in the generated image.

## Negative prompt

```text
colour, colour cast, warm tone, cool tone, sepia, duotone, neon, saturated, vibrant,
harsh shadows, hard rim light, high contrast blacks, crushed shadows, busy background,
clutter, props, set dressing, text, numerals, watermarks, logos, UI chrome, lens flare,
film grain, heavy vignette, glossy, chrome, metallic reflections, HDR
```

## Worked examples

Three unrelated subjects, to show the treatment holds regardless of what is depicted.

**1 — Architecture**

```text
[SUBJECT: a single concrete stairwell curving up out of frame]
```
Reads as: matte concrete in mid-greys against a near-identical light-grey ground, the curve legible only through a slow luminance gradient, the upper-left third completely empty.

**2 — Textile**

```text
[SUBJECT: a folded length of heavy linen resting on a flat surface]
```
Reads as: soft even light raking just enough to describe the fold, fibre texture present but never sharp, no shadow darker than `#767676`, the right 40% clean ground.

**3 — Instrumentation**

```text
[SUBJECT: an abstract cluster of thin rods suspended at different heights]
```
Reads as: matte grey rods on a seamless light-grey field, separation between rods carried purely by luminance steps, one soft floor shadow, generous air above the cluster for a headline.
