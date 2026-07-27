# Ember Console — image recipe

Copy the block below, replace the `[SUBJECT: …]` line with your subject clause, and send it as-is. Everything under `STYLE`, `NEGATIVE SPACE` and `DO NOT INCLUDE` is load-bearing — keep it verbatim.

```text
[SUBJECT: describe the subject in one clause — e.g. "a stack of shipping containers", "a single ceramic cup", "an abstract network of nodes"]

Rendered as a flat vector UI illustration with analytics subject matter, as if it were an
oversized diagram lifted out of a business dashboard.

STYLE — apply all of the following, they are not optional:
- white ground #FCFCFC, with white #FFFFFF card planes separated by crisp 1px #E6E8EB rules
- exactly one saturated hue — burnt orange #D64B00 — carrying every data series, highlight
  and call-to-action shape; it must occupy no more than 15% of the frame
- a secondary pass of the same orange at roughly 35% opacity for any comparison or
  background series; never introduce a second hue for it
- all other elements in near-black #15171F and neutral greys (#6B7280 for secondary marks)
- flat even lighting, no cast shadows, no ambient occlusion, no gradients — the single
  permitted exception is one optional soft lilac-to-pink band (#8B5CF6 toward pink) if the
  subject needs a machine-intelligence cue
- charts and diagram lines rendered as clean 2px strokes with rounded caps, no fills,
  no textures, no dimensionality
- geometry sits on a strict grid with 10px-equivalent rounded corners on any panel shapes

NEGATIVE SPACE: Leave the top 25% as clean white ground for a headline; keep the chart and
diagram mass in the lower two-thirds.

DO NOT INCLUDE: multiple competing accent colours, categorical chart palettes, 3D or
isometric charts, neon, glassmorphism, drop shadows, photographic elements, dark
backgrounds, legible text, numerals, logos or UI chrome.
```

**Target —** provider, model and resolution are all configurable; set them to whatever image stack you are using.
Recommended resolution: **1536×1024** (3:2 landscape). Use **1024×1536** for portrait slots and **1024×1024** for square cards.

## Hard constraints

These must survive any edit to the prompt. If the returned image breaks one, regenerate rather than retouch.

- White ground `#FCFCFC` with white cards separated by 1px `#E6E8EB` rules.
- Exactly one saturated hue — burnt orange `#D64B00` — carrying every data series and call to action.
- Comparison / secondary data drawn in that same orange at ~35% opacity, never a second hue.
- All other elements in near-black `#15171F` and greys (`#6B7280`).
- Flat lighting, no gradients, except one optional lilac-pink band for AI/intelligence cues.
- Charts rendered as clean 2px strokes — no fills, no textures, no 3D.
- Negative space — leave the top 25% as clean white for a headline; keep charts in the lower two-thirds.
- Never include legible text, numerals, logos or UI chrome in the generated image.

## Negative prompt

```text
multiple competing accent colours, categorical colour palette, rainbow data series,
3D charts, isometric illustration, neon, glow, glassmorphism, frosted glass, drop shadows,
photographic elements, photorealism, dark backgrounds, dark mode, gradient meshes,
hand-drawn or sketchy strokes, text, numerals, watermarks, logos, UI chrome, cluttered
composition
```

## Worked examples

Three unrelated subjects, to show the treatment holds regardless of what is depicted.

**1 — Logistics**

```text
[SUBJECT: a row of stacked shipping containers seen straight on, one container pulled forward from the line]
```
Reads as: flat grey container blocks on white, the pulled-forward one solid `#D64B00`, a 2px orange route line arcing across the lower third, thin grey gridlines behind.

**2 — Agriculture**

```text
[SUBJECT: a single stalk of wheat rising from a flat horizon line]
```
Reads as: near-black stalk on white ground, grain heads reduced to flat geometric strokes, one 2px orange yield curve running left-to-right beneath the horizon and an orange marker dot at its peak.

**3 — Music**

```text
[SUBJECT: an abstract cluster of concentric sound rings radiating from a small point]
```
Reads as: concentric 2px rings in `#15171F` and grey with a single orange ring carrying the active frequency, a faint 35%-opacity orange ring behind it as the comparison state, all on flat white with the top quarter empty.
