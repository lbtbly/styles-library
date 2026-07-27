# Panel Stack — image recipe

Copy the block below, replace the `[SUBJECT: …]` line with one clause describing what the picture is of, and send it as-is. Everything under `STYLE`, `NEGATIVE SPACE` and `DO NOT INCLUDE` is load-bearing — keep it verbatim.

```text
[SUBJECT: describe the subject in one clause — e.g. "a stack of shipping containers", "a single ceramic cup", "an abstract network of nodes"]

Rendered as a flat vector illustration built from overlapping rectangular panels, as if
the subject had been filed into drawers — layered, orderly, softly lit.

STYLE — apply all of the following, they are not optional:
- off-white ground #F7F8F9 with panels and planes in white #FFFFFF
- recessed areas and negative shapes in light grey #EFF1F3, used as flat fill with no border
- one violet #5B2FD6 as the only saturated colour, on no more than 15% of the frame
- the subject is composed from overlapping rounded rectangles: 10px corner radius,
  1px #E4E7EC borders, clearly stacked front-to-back with visible overlap
- exactly one soft wide drop shadow, under the frontmost panel only; every other panel
  is perfectly flat and separated by its 1px border alone
- flat even lighting, no gradients inside panels, no ambient occlusion
- near-black #0B1220 reserved for the smallest details that must read first
- straight-on orthographic view, panels parallel to the frame edges

NEGATIVE SPACE: Keep the lower third of the frame an unbroken #F7F8F9 field with no
panels or marks, for supporting copy.

DO NOT INCLUDE: neon, 3D extrusion, isometric perspective, glass blur, frosted or
translucent panels, photographic backgrounds, heavy outlines, skeuomorphic texture,
multiple drop shadows, legible text, logos, or UI chrome.
```

**Target** — provider, model and resolution are configurable; set them to whatever image stack you are using.

- Provider: configurable — set to your image provider
- Model: configurable — set to your image model
- Resolution: `1536×1024` (3:2 landscape). Use `1024×1536` for portrait, `1024×1024` for square.

## Hard constraints

If a generation breaks one of these, regenerate rather than accept it.

- Off-white ground `#F7F8F9` with white panels `#FFFFFF`.
- One violet `#5B2FD6` as the only saturated colour.
- Overlapping rectangular panels with 10px rounded corners and 1px `#E4E7EC` borders.
- A single soft drop shadow under the frontmost panel only.
- Flat even lighting, no gradients inside panels.
- Recessed shapes use flat `#EFF1F3` with no border.
- Negative space: the lower third stays an unbroken `#F7F8F9` field for supporting copy.
- Never include legible text, logos or UI chrome in the generated image.

## Negative prompt

```text
neon, 3D extrusion, isometric perspective, glass blur, frosted glass, translucency,
backdrop blur, photographic background, heavy outlines, skeuomorphic texture, bevel,
emboss, multiple drop shadows, glow, gradient fill, drop cap, legible text, logos,
watermark, UI chrome, screenshot, cluttered edges, warm colour cast
```

## Worked examples

Three deliberately unrelated subjects, to show the style holds regardless of what is depicted.

**1 — Architecture**

```text
[SUBJECT: a terraced hillside town, houses stepping down the slope in rows]
```
Reads as five or six white rounded panels overlapping in a descending stagger on `#F7F8F9`, each with a 1px `#E4E7EC` edge, the recesses between terraces filled flat `#EFF1F3`, and one house-panel picked out in `#5B2FD6`. Only the frontmost, lowest terrace carries the shadow. The lower third of the frame stays empty.

**2 — Cooking**

```text
[SUBJECT: a club sandwich cut in half, layers of filling stacked between slices]
```
Reads as a literal panel stack: each layer is a white rounded rectangle with a 1px border, slightly offset from the one below, fillings rendered as flat `#EFF1F3` slabs, one layer violet `#5B2FD6`. Straight-on, no perspective, no crumbs or texture — the sandwich becomes a filing system.

**3 — Music**

```text
[SUBJECT: a four-track mixing session, parallel waveform lanes running left to right]
```
Reads as four stacked white lanes on `#F7F8F9`, each a rounded rectangle with a 1px `#E4E7EC` border; waveforms are flat `#EFF1F3` blocks of varying height inside the lanes, with the active lane's blocks in `#5B2FD6`. The frontmost lane sits slightly forward with the single shadow beneath it. Resist the urge to add glow to the active lane — that is the constraint this subject most wants to break.
