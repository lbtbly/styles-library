# Dark Bench — image recipe

Copy the block below, replace the `[SUBJECT: …]` line with one clause describing your
subject, and send it as-is. Everything under `STYLE`, `NEGATIVE SPACE` and
`DO NOT INCLUDE` is load-bearing — keep it verbatim.

```text
[SUBJECT: describe the subject in one clause — e.g. "a stack of shipping containers", "a single ceramic cup", "an abstract network of nodes"]

Rendered as a macro photograph of a dark matte screen at a slight tilt, shot on a fast prime at f/1.8, shallow depth of field.

STYLE — apply all of the following, they are not optional:
- near-black #0B0B0B ground carrying a faint regular dot grid that recedes with the tilt
- matte graphite panels in the #1C1C1C–#262626 range, absolutely no glow, bloom or specular sheen
- one green #3FBF52 as the only saturated colour, confined to connector lines and a single status point
- shallow depth of field — exactly one element sharp, everything else falling progressively out of focus
- slight perspective tilt, cool neutral colour temperature, fine sensor grain
- soft off-frame key light raking from one side; deep shadows that still hold detail

NEGATIVE SPACE: The out-of-focus region should occupy the outer half of the frame, leaving the sharp element off-centre with clean dark space around it.

DO NOT INCLUDE: neon glow, iridescence, warm colour casts, flat orthographic vector, light backgrounds, lens flare, legible text, logos, UI chrome.
```

**Target:** provider, model and resolution are all **configurable** — set them to whatever
image stack you are using. Suggested resolution `1536×1024` (3:2 landscape); use
`1024×1536` for portrait and `1024×1024` for square. Composition assumes landscape.

## Hard constraints

These must survive any edit you make to the prompt:

- near-black `#0B0B0B` ground with a faint regular dot grid
- matte graphite panels, absolutely no glow or bloom
- one green `#3FBF52` as the only saturated colour, on connector lines only
- shallow depth of field — one element sharp, the rest falling off
- slight perspective tilt, cool neutral colour temperature
- negative space — the out-of-focus region occupies the outer half of the frame
- never include legible text, logos or UI chrome in the generated image

## Negative prompt

```text
neon glow, iridescence, warm colour casts, flat orthographic vector, light backgrounds, lens flare, text, logos, UI chrome, HDR over-processing, bokeh balls, purple fringing, glossy reflections
```

## Worked examples

Three deliberately unrelated subjects, to show the treatment — not the content — is what
carries the style.

**1 — Industrial**

```text
[SUBJECT: a stack of weathered shipping containers seen end-on]

Rendered as a macro photograph of a dark matte screen at a slight tilt, shot on a fast prime at f/1.8, shallow depth of field.
… (STYLE / NEGATIVE SPACE / DO NOT INCLUDE blocks unchanged)
```

Expect: containers reduced to matte graphite slabs, their gaps reading as the dot grid's
rhythm, one green lashing rod as the single saturated note, the near stack sharp and the
rest dissolving.

**2 — Botanical**

```text
[SUBJECT: a single fern frond uncurling]

Rendered as a macro photograph of a dark matte screen at a slight tilt, shot on a fast prime at f/1.8, shallow depth of field.
… (STYLE / NEGATIVE SPACE / DO NOT INCLUDE blocks unchanged)
```

Expect: the frond desaturated almost to graphite, one green node at the crozier tip, the
dot grid faintly behind it, everything past the first curl racked out.

**3 — Musical**

```text
[SUBJECT: the bridge and strings of an upright double bass]

Rendered as a macro photograph of a dark matte screen at a slight tilt, shot on a fast prime at f/1.8, shallow depth of field.
… (STYLE / NEGATIVE SPACE / DO NOT INCLUDE blocks unchanged)
```

Expect: the strings read as connector wires, one of them green; the bridge sharp and
matte; the body and f-hole falling into unlit near-black.

## Notes on use

- If the model keeps adding glow, add `matte finish, no emissive surfaces` to the STYLE
  block rather than strengthening the negative prompt.
- If the dot grid disappears, describe it explicitly as `a printed dot lattice on the
  surface behind the subject, 1px dots on a 24px pitch`.
- Never let the generated image carry text — all copy is composited in HTML/CSS on top,
  and the recipe's negative space exists exactly so there is somewhere to put it.
