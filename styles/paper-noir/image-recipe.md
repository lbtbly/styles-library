# Paper Noir — image recipe

Copy the block below, replace the `[SUBJECT: …]` line with one clause describing your subject, and send it as-is. Everything under `STYLE` is load-bearing — deleting a line changes the style.

```
[SUBJECT: describe the subject in one clause — e.g. "a stack of shipping containers", "a single ceramic cup", "an abstract network of nodes"]

Rendered as a studio product photograph on a black set, fine paper grain, medium-format still life.

STYLE — apply all of the following, they are not optional:
- pure black seamless background, unlit at the edges
- warm off-white #F3F1EA subject surfaces with visible fine paper grain, matte and slightly powdery
- single soft key light from directly above, gentle falloff into the black, no fill light
- rounded pill and circle geometry — softened corners, capsule forms, discs
- one small fluorescent chartreuse #C9F500 detail, no larger than a coin in frame
- monochrome apart from that single chartreuse note
- a shallow contact shadow where the subject meets the floor, everything else in shadow

COMPOSITION: subject placed slightly high in the frame, shot square-on or from a low three-quarter angle.

NEGATIVE SPACE: at least half the frame is unlit black, clean enough to hold text.

DO NOT INCLUDE: coloured backgrounds, glossy plastic, neon glow, multiple accent colours, cluttered props, flat vector rendering, text, logos, people.
```

**Target** — provider, model and resolution are all configurable; set them to whatever you have.
Suggested default resolution **1536×1024 (3:2 landscape)**; use **1024×1536** for portrait case-study slots and **1024×1024** for square card art. Ask for a high-quality tier — the black falloff posterises badly at low bitrates, and the paper grain is the first thing a cheap render throws away.

## Hard constraints

These must survive any edit you make to the prompt:

- pure black seamless background
- warm off-white `#F3F1EA` subject surfaces with visible fine paper grain
- single soft key light from above, gentle falloff into the black
- rounded pill and circle geometry
- one small fluorescent chartreuse `#C9F500` detail, no larger than a coin in frame
- negative space — at least half the frame is unlit black
- never include legible text, logos or UI chrome in the generated image

## Negative prompt

```
coloured backgrounds, glossy plastic, neon glow, multiple accent colours,
cluttered props, flat vector rendering, text in the image, watermark, logo,
white background, studio softbox reflections, rim light, HDR, high saturation,
sharp square corners, busy scene, people, hands
```

## Worked examples

**1 — A logistics product**

```
[SUBJECT: a stack of three shipping containers with softened corners]

Rendered as a studio product photograph on a black set, fine paper grain, medium-format still life.
… (STYLE block unchanged) …
```

*Expected:* chalky off-white capsule-cornered boxes stacked slightly off-axis, one chartreuse latch, the bottom edge dissolving into black.

**2 — A hospitality brand**

```
[SUBJECT: a single ceramic cup with a rolled rim on a low plinth]

Rendered as a studio product photograph on a black set, fine paper grain, medium-format still life.
… (STYLE block unchanged) …
```

*Expected:* a matte disc-and-cylinder form under one soft overhead light, a chartreuse ring of glaze inside the rim, three-quarters of the frame black.

**3 — An abstract technology concept**

```
[SUBJECT: an abstract network of connected nodes arranged as a loose constellation]

Rendered as a studio product photograph on a black set, fine paper grain, medium-format still life.
… (STYLE block unchanged) …
```

*Expected:* off-white spheres and capsule links floating in black, grain visible on every lit face, a single node glowing chartreuse.

The style holds across containers, a cup and an abstract graph because the black set, the paper tooth, the single overhead key and the coin-sized chartreuse note do the work — not the subject.
