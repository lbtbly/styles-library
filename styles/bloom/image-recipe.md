# Bloom — image recipe

Fill the `[SUBJECT]` slot and leave everything below it alone. The constraints
are what make three unrelated subjects come back looking like one family.

```text
[SUBJECT: describe the subject in one clause — e.g. "a stack of shipping containers", "a single ceramic cup", "an abstract network of nodes"]

Rendered as 3D render, iridescent or chrome material, dark studio.

STYLE — apply all of the following, they are not optional:
- near-black background #08080D with deep falloff
- one faceted or organic 3D form as the sole subject, iridescent indigo-to-magenta refraction
- light appears as a soft feathered bloom around the object, not as a lamp
- subtle film grain across the whole frame
- no ground plane — the object floats in void

NEGATIVE SPACE: The lower 40% falls to near-black for text overlay.

DO NOT INCLUDE: flat vector, white or light backgrounds, hard rim lighting, text or UI in the image, busy multi-object scenes, warm orange casts.
```

**Target —** provider, model and resolution are all configurable; set them to
whatever image stack you are using.

- provider: `configurable — set to your image provider`
- model: `configurable — set to your image model`
- resolution: `1536x1024 (3:2 landscape); use 1024x1536 for portrait, 1024x1024 for square`

## Hard constraints

- near-black background #08080D with deep falloff
- one faceted or organic 3D form as the sole subject, iridescent indigo-to-magenta refraction
- light appears as a soft feathered bloom around the object, not as a lamp
- subtle film grain across the whole frame
- no ground plane — the object floats in void
- negative space — The lower 40% falls to near-black for text overlay.
- never include legible text, logos or UI chrome in the generated image

## Negative prompt

```text
flat vector, white or light backgrounds, hard rim lighting, text or UI in the image, busy multi-object scenes, warm orange casts
```

## Worked examples

Three unrelated subjects, same style:

**1 — Data**

> a faceted crystalline shard suspended and slowly rotating

**2 — Logistics**

> a chrome shipping container floating in void

**3 — Biology**

> an iridescent coral-like organic form
