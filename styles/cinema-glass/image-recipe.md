# Cinema Glass — image recipe

Copy the block below, replace the `[SUBJECT: …]` line with one clause describing your
subject, and send it as-is. Everything under `STYLE`, `NEGATIVE SPACE` and
`DO NOT INCLUDE` is load-bearing — keep it verbatim. The negative-space rule in particular
is not stylistic: the lower third is where the glass panels and headline go.

```text
[SUBJECT: describe the subject in one clause — e.g. "a stack of shipping containers", "a single ceramic cup", "an abstract network of nodes"]

Rendered as an anamorphic cinematic film still, shallow depth of field, visible 35mm film grain.

STYLE — apply all of the following, they are not optional:
- full-bleed photographic image, dark overall exposure, nothing brighter than mid-grey except the key light
- a single strong light source raking from one side, with deep shadows that still retain detail
- desaturated throughout except one hot accent note near #D9E82A
- visible fine film grain and a gentle natural vignette
- wide cinematic framing with the subject off-centre, sitting in the upper two thirds
- cool neutral shadows, no colour grading beyond the single accent note

NEGATIVE SPACE: The lower third must fall dark and uncluttered — no subject detail, no texture, no highlights — so glass panels and type can be composited over it.

DO NOT INCLUDE: flat vector, bright even lighting, white backgrounds, stock-photo smiles, HDR over-processing, text or UI in the image, lens flare stars, multiple coloured light sources.
```

**Target:** provider, model and resolution are all **configurable** — set them to whatever
image stack you are using. Suggested resolution `1536×1024` (3:2 landscape); use
`1024×1536` for portrait hero panels and `1024×1024` for square cards. The composition
notes assume landscape; for portrait, move the negative space to the bottom 40%.

## Hard constraints

These must survive any edit you make to the prompt:

- full-bleed photographic image, dark overall exposure
- single strong light source with deep shadows retaining detail
- desaturated except one hot accent note near `#D9E82A`
- visible fine film grain
- wide cinematic framing with the subject off-centre
- negative space — the lower third falls dark and uncluttered for glass panels and type
- never include legible text, logos or UI chrome in the generated image

## Negative prompt

```text
flat vector, bright even lighting, white backgrounds, stock-photo smiles, HDR over-processing, text or UI in the image, watermark, logo, oversaturated colour, teal-and-orange grade, multiple light sources, hard flash, cluttered foreground, busy lower third
```

## Worked examples

Three deliberately unrelated subjects. The subject changes completely; the light, the
exposure and the empty lower third do not.

**1 — Architectural**

```text
[SUBJECT: a concrete stairwell spiralling down a service shaft]

Rendered as an anamorphic cinematic film still, shallow depth of field, visible 35mm film grain.
… (STYLE / NEGATIVE SPACE / DO NOT INCLUDE blocks unchanged)
```

Expect: the shaft falling away into black, one hard shaft of light crossing the upper third,
concrete reading as grey-green, a single acid-yellow reflection on a handrail, the bottom of
the frame pure shadow.

**2 — Culinary**

```text
[SUBJECT: a whole grilled fish resting on a scorched steel tray]

Rendered as an anamorphic cinematic film still, shallow depth of field, visible 35mm film grain.
… (STYLE / NEGATIVE SPACE / DO NOT INCLUDE blocks unchanged)
```

Expect: a single low side-light catching the skin, the tray going black at the near edge,
everything desaturated to steel and ash except one hot yellow-green note in a lemon wedge,
the table foreground empty.

**3 — Meteorological**

```text
[SUBJECT: a wall of rain crossing an empty reservoir]

Rendered as an anamorphic cinematic film still, shallow depth of field, visible 35mm film grain.
… (STYLE / NEGATIVE SPACE / DO NOT INCLUDE blocks unchanged)
```

Expect: the squall line off-centre in the upper two thirds, one break of hot light behind it,
water reading as flat dark grey, heavy grain, the near water surface falling to near-black.

## Notes on use

- If the model lifts the shadows, add `underexposed by one stop, protect the blacks` to the
  STYLE block rather than fighting it in the negative prompt.
- If the accent goes green-neon, restate it as `one small hot chartreuse highlight, less
  than 3% of the frame`.
- If the lower third comes back busy, add `empty foreground, nothing in the bottom third`
  as its own line — it is the constraint models drop first, and the one the layout depends on.
- The generated image must carry **no text**. All copy is composited in HTML/CSS over the
  dark lower third, which is exactly what the negative-space rule reserves.
- When no generated image is available, build the still in CSS instead — see the seven-layer
  gradient recipe under *Texture & effects* in `brief.md`. The previews in `previews/` are
  built entirely that way and are a working reference.
