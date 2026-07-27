# Studio Object — image recipe

Fill the `[SUBJECT]` slot and leave everything below it alone. The constraints
are what make three unrelated subjects come back looking like one family.

```text
[SUBJECT: describe the subject in one clause — e.g. "a stack of shipping containers", "a single ceramic cup", "an abstract network of nodes"]

Rendered as matte 3D product render, grey seamless studio.

STYLE — apply all of the following, they are not optional:
- flat mid-grey #D6D6D6 seamless background with soft falloff
- one object centred, matte finish, no gloss or chrome
- soft large key light from above-left, gentle contact shadow
- near-monochrome with at most one small colour note
- orthographic or mild isometric projection

NEGATIVE SPACE: At least 30% flat grey ground on one side for docked UI and type.

DO NOT INCLUDE: glossy or reflective materials, coloured lighting, busy scenes, photographic backgrounds, neon, dramatic contrast.
```

**Target —** provider, model and resolution are all configurable; set them to
whatever image stack you are using.

- provider: `configurable — set to your image provider`
- model: `configurable — set to your image model`
- resolution: `1536x1024 (3:2 landscape); use 1024x1536 for portrait, 1024x1024 for square`

## Hard constraints

- flat mid-grey #D6D6D6 seamless background with soft falloff
- one object centred, matte finish, no gloss or chrome
- soft large key light from above-left, gentle contact shadow
- near-monochrome with at most one small colour note
- orthographic or mild isometric projection
- negative space — At least 30% flat grey ground on one side for docked UI and type.
- never include legible text, logos or UI chrome in the generated image

## Negative prompt

```text
glossy or reflective materials, coloured lighting, busy scenes, photographic backgrounds, neon, dramatic contrast
```

## Worked examples

Three unrelated subjects, same style:

**1 — Warehouse**

> an isometric stack of pallets and racking

**2 — Hardware**

> a matte sensor module on a neutral plinth

**3 — Construction**

> a matte concrete column section
