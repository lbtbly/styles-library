# Highlighter — image recipe

Fill the `[SUBJECT]` slot and leave everything below it alone. The constraints
are what make three unrelated subjects come back looking like one family.

```text
[SUBJECT: describe the subject in one clause — e.g. "a stack of shipping containers", "a single ceramic cup", "an abstract network of nodes"]

Rendered as flat vector illustration or matte 3D render with a single fluorescent accent.

STYLE — apply all of the following, they are not optional:
- desaturated warm-grey ground #EDEFEA
- exactly one fluorescent chartreuse #C3EC2E used on no more than 10% of the frame
- solid near-black #1C1E18 masses as counterweight
- matte surfaces, flat or very soft lighting
- geometric shapes with generous rounding

NEGATIVE SPACE: Keep the right 30% as empty desaturated ground for type.

DO NOT INCLUDE: multiple bright colours, pastel palettes, glossy or metallic surfaces, photographic realism, gradients, neon glow.
```

**Target —** provider, model and resolution are all configurable; set them to
whatever image stack you are using.

- provider: `configurable — set to your image provider`
- model: `configurable — set to your image model`
- resolution: `1536x1024 (3:2 landscape); use 1024x1536 for portrait, 1024x1024 for square`

## Hard constraints

- desaturated warm-grey ground #EDEFEA
- exactly one fluorescent chartreuse #C3EC2E used on no more than 10% of the frame
- solid near-black #1C1E18 masses as counterweight
- matte surfaces, flat or very soft lighting
- geometric shapes with generous rounding
- negative space — Keep the right 30% as empty desaturated ground for type.
- never include legible text, logos or UI chrome in the generated image

## Negative prompt

```text
multiple bright colours, pastel palettes, glossy or metallic surfaces, photographic realism, gradients, neon glow
```

## Worked examples

Three unrelated subjects, same style:

**1 — Automation**

> a matte mechanical arm holding a single marker

**2 — Agriculture**

> a stack of desaturated hay bales

**3 — Music**

> a matte black studio monitor at three-quarter view
