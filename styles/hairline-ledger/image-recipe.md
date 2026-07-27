# Hairline Ledger — image recipe

Copy the block below, replace the `[SUBJECT: …]` line with one clause describing what the picture is of, and send it as-is. Everything under `STYLE`, `NEGATIVE SPACE` and `DO NOT INCLUDE` is load-bearing — keep it verbatim.

```text
[SUBJECT: describe the subject in one clause — e.g. "a stack of shipping containers", "a single ceramic cup", "an abstract network of nodes"]

Rendered as a flat vector-style technical illustration with the sensibility of an
engineering drawing or a Swiss railway timetable — measured, orthogonal, unemotional.

STYLE — apply all of the following, they are not optional:
- near-white background #F4F5F6, with any surfaces or planes in pure white #FFFFFF
- all linework exactly 1px and the same weight everywhere, colour #E3E5E8 — no heavy
  strokes, no tapering, no outline hierarchy
- colour restricted to one blue #0B5FD0 used sparingly as the single accent, plus at
  most a few small semantic marks in green #0A7C4A, red #B42318 or amber #B54708
- flat even lighting; absolutely no gradients, glows, bevels, drop shadows or ambient
  occlusion — every shape is a flat fill bounded by a 1px rule
- strictly orthogonal composition on a visible modular grid; every element aligned to a
  shared baseline and to vertical column edges
- generous white space between elements; density comes from repetition of small equal
  units, not from clutter
- dark near-black #0F1419 used only for the few smallest marks that need to read first

NEGATIVE SPACE: Reserve the upper-left third of the frame as flat #F4F5F6 with no
linework at all, so a headline and subhead can sit there.

DO NOT INCLUDE: 3D rendering, isometric extrusion, glassmorphism, neon or glow,
photographic texture, hand-drawn or organic shapes, gradient backgrounds, vignetting,
lens blur, legible text, logos, or UI chrome.
```

**Target** — provider, model and resolution are configurable; set them to whatever image stack you are using.

- Provider: configurable — set to your image provider
- Model: configurable — set to your image model
- Resolution: `1536×1024` (3:2 landscape). Use `1024×1536` for portrait, `1024×1024` for square.

## Hard constraints

These must survive any edit to the prompt. If a generation breaks one, regenerate rather than accept it.

- Near-white background `#F4F5F6`, white surfaces `#FFFFFF`.
- All linework 1px, colour `#E3E5E8` — no heavy strokes anywhere.
- Colour restricted to one blue `#0B5FD0` plus small semantic marks in green `#0A7C4A` / red `#B42318` / amber `#B54708`.
- Flat lighting; absolutely no gradients, glows, bevels or drop shadows.
- Orthogonal composition on a strict grid; everything aligned to a baseline.
- Negative space: the upper-left third stays flat `#F4F5F6` with no linework, for headline and subhead.
- Never include legible text, logos or UI chrome in the generated image.

## Negative prompt

```text
3D rendering, isometric extrusion, glassmorphism, neon, glow, photographic texture,
hand-drawn or organic shapes, gradient background, vignetting, lens blur, bokeh,
drop shadow, bevel, emboss, watercolour, sketch lines, brush texture, legible text,
logos, watermark, UI chrome, screenshot, cluttered composition, warm colour cast
```

## Worked examples

Three deliberately unrelated subjects, to show the style holds regardless of what is depicted.

**1 — Logistics**

```text
[SUBJECT: a stack of shipping containers seen straight on, arranged four wide and three high]
```
Reads as a modular grid of flat white rectangles on near-white, every edge a 1px `#E3E5E8` rule, with three containers picked out in `#0B5FD0` and one small `#B42318` mark denoting an exception. The upper-left third stays empty.

**2 — Botany**

```text
[SUBJECT: a single fern frond laid flat, leaflets fanning symmetrically from a central stem]
```
Reads as a specimen plate: leaflets become equal repeated shapes on a strict vertical axis, all outlines 1px `#E3E5E8`, the central stem in `#0F1419`, one leaflet filled `#0B5FD0` as the only colour. No organic wobble — the frond is redrawn as geometry.

**3 — Astronomy**

```text
[SUBJECT: the orbits of four planets around a small central star, viewed from directly above]
```
Reads as an orrery diagram: four concentric 1px `#E3E5E8` circles on `#F4F5F6`, planets as small flat discs, the star as a plain `#0F1419` dot, one orbit and one planet in `#0B5FD0`, tick marks at regular angular intervals. Flat, no glow around the star — the constraint that most wants breaking here, so check it first.
