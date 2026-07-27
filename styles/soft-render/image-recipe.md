# Soft Render — image recipe

Copy the block below, replace the `[SUBJECT: …]` line with one clause describing your subject, and send it as-is. Everything under `STYLE` is load-bearing — deleting a line changes the style.

```
[SUBJECT: describe the subject in one clause — e.g. "a stack of shipping containers", "a single ceramic cup", "an abstract network of nodes"]

Rendered as a soft-focus 3D product render, studio lighting, shot on a long lens.

STYLE — apply all of the following, they are not optional:
- matte grey studio environment #E2E2E2, seamless sweep, soft gradient falloff toward the corners
- shallow depth of field — the subject sharp, the background falling gently out of focus
- one pale lime accent #DCEE92 on a single small element only, no larger than a tenth of the frame
- soft diffused key light from upper left, large source, no hard shadows
- one long soft contact shadow pooling beneath the subject
- rounded matte geometry, generous fillets, no sharp edges
- surfaces are matte and slightly powdery — no gloss, no chrome, no reflections
- muted, near-monochrome palette apart from the single lime accent

COMPOSITION: subject centred or slightly off-centre, sitting low in the frame, plenty of headroom.

NEGATIVE SPACE: the defocused background should occupy at least a third of the frame, clean enough to place text over.

DO NOT INCLUDE: hard specular highlights, saturated colour, busy environments, sharp corners, flat vector look, text in the image, logos, UI chrome, people.
```

**Target** — provider, model and resolution are all configurable; set them to whatever you have.
Suggested default resolution **1536×1024 (3:2 landscape)**; use **1024×1536** for portrait hero slots and **1024×1024** for square card art. Ask for the highest quality tier your provider offers — the soft gradient falloff bands badly at low bitrates.

## Hard constraints

These must survive any edit you make to the prompt:

- matte grey studio environment `#E2E2E2` with soft gradient falloff
- shallow depth of field — subject sharp, background falling gently out of focus
- one pale lime accent `#DCEE92` on a small element only
- soft diffused key light from upper left, no hard shadows
- rounded matte geometry, no sharp edges
- negative space — the defocused background occupies at least a third of the frame
- never include legible text, logos or UI chrome in the generated image

## Negative prompt

```
hard specular highlights, saturated colour, busy environments, sharp corners,
flat vector look, text in the image, glossy plastic, chrome, neon, rim lighting,
dark background, high contrast, dramatic shadows, lens flare, HDR, cluttered props,
watermark, signature
```

## Worked examples

**1 — A logistics product**

```
[SUBJECT: a single shipping container standing upright on a bare floor]

Rendered as a soft-focus 3D product render, studio lighting, shot on a long lens.
… (STYLE block unchanged) …
```

*Expected:* a corrugated grey box with softened corners, one lime latch handle catching the light, the far edge dissolving into the sweep.

**2 — A wellness product**

```
[SUBJECT: a single unglazed ceramic cup with a rolled rim]

Rendered as a soft-focus 3D product render, studio lighting, shot on a long lens.
… (STYLE block unchanged) …
```

*Expected:* a chalky, powdery cup with a long soft shadow, a lime thread of glaze at the rim, background grey falling off to nothing.

**3 — An abstract data concept**

```
[SUBJECT: an abstract cluster of connected nodes floating in loose formation]

Rendered as a soft-focus 3D product render, studio lighting, shot on a long lens.
… (STYLE block unchanged) …
```

*Expected:* matte grey spheres joined by soft tubes, the nearest node lime, the back half of the cluster blurred into the studio grey.

The style holds across a shipping container, a cup and an abstract graph because the grey sweep, the single lime note and the shallow focus do the work — not the subject.
