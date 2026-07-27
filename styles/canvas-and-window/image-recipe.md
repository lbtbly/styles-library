# Canvas & Window — image recipe

Copy the block below, replace the `[SUBJECT: …]` line with one clause describing what the picture is of, and send it as-is. Everything under `STYLE`, `NEGATIVE SPACE` and `DO NOT INCLUDE` is load-bearing — keep it verbatim.

```text
[SUBJECT: describe the subject in one clause — e.g. "a stack of shipping containers", "a single ceramic cup", "an abstract network of nodes"]

Rendered as a flat vector illustration staged like a studio product shot: the subject is
framed inside a single rounded rectangular window floating on a seamless flat backdrop.

STYLE — apply all of the following, they are not optional:
- a single rounded rectangular window, 16px corner radius, floating centred on a flat
  #ECECEC field; the subject is rendered inside that window and nowhere else
- generous empty margin on all four sides of the window — the window never touches the
  frame edge and never bleeds off it
- window interior in white #FFFFFF with recessed areas in light grey #F6F7F8 and all
  internal linework 1px #E5E7EA
- one teal-cyan accent #00849E as the only saturated colour; everything else is white,
  grey and near-black #0E1113
- one soft wide drop shadow beneath the window and no other shadows anywhere in the frame
- flat even lighting, no gradients, no ambient occlusion, no reflections
- straight-on orthographic view — the window is parallel to the frame, no perspective tilt,
  no rotation, no mockup angle

NEGATIVE SPACE: The flat grey margin around the window is the negative space — keep at
least 15% of the frame empty on the left.

DO NOT INCLUDE: perspective distortion, 3D bevels, gradient backgrounds, neon glow,
photographic desks, hands or people, cluttered edges, multiple shadows, reflections,
textured or coloured backdrop, legible text, logos, or UI chrome.
```

**Target** — provider, model and resolution are configurable; set them to whatever image stack you are using.

- Provider: configurable — set to your image provider
- Model: configurable — set to your image model
- Resolution: `1536×1024` (3:2 landscape). Use `1024×1536` for portrait, `1024×1024` for square.

## Hard constraints

If a generation breaks one of these, regenerate rather than accept it.

- A single rounded rectangular window floating centred on a flat `#ECECEC` field.
- Generous empty margin on all four sides of the window.
- One teal-cyan accent `#00849E`; everything else white, grey and near-black `#0E1113`.
- One soft wide drop shadow beneath the window, no other shadows.
- Straight-on orthographic view — no perspective tilt.
- Window interior white `#FFFFFF`, recesses `#F6F7F8`, linework 1px `#E5E7EA`.
- Negative space: at least 15% of the frame empty on the left.
- Never include legible text, logos or UI chrome in the generated image.

## Negative prompt

```text
perspective distortion, isometric view, tilted mockup, 3D bevel, extrusion, gradient
background, radial gradient, neon glow, bloom, photographic desk, hands, people, laptop
photo, cluttered edges, multiple shadows, reflection, mirror floor, textured backdrop,
coloured background, vignette, legible text, logos, watermark, UI chrome, screenshot
```

## Worked examples

Three deliberately unrelated subjects, to show the style holds regardless of what is depicted.

**1 — Marine biology**

```text
[SUBJECT: a jellyfish drifting with its tentacles trailing below the bell]
```
Reads as a specimen framed in a white window on a flat `#ECECEC` field: the bell is a flat white shape with a 1px `#E5E7EA` outline, the tentacles are `#00849E` hairlines, the water behind them a flat `#F6F7F8` panel. One shadow under the window, nothing glowing — bioluminescence is the constraint this subject will try to break.

**2 — Transport**

```text
[SUBJECT: a cable car suspended from a single overhead line between two pylons]
```
Reads as a flat side elevation inside the window: pylons and cabin as white shapes with 1px `#E5E7EA` outlines, the cable a single `#00849E` line running the width of the window, the sky a flat `#F6F7F8` block. Straight-on, no drama, no perspective — the mountain becomes a grey silhouette.

**3 — Domestic**

```text
[SUBJECT: a single ceramic cup on a saucer, seen straight on]
```
Reads as a catalogue photograph redrawn flat: the cup a white shape outlined 1px `#E5E7EA`, its interior `#F6F7F8`, one teal `#00849E` band around the rim, and the surface it stands on a plain flat plane with no reflection or cast shadow — the only shadow in the frame is the one beneath the window itself.
