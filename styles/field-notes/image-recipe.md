# Field Notes — image recipe

The hero asset for this style is a **defocused natural landscape** that a translucent white page sheet will sit on top of. Copy the block below whole, replace only the `[SUBJECT: …]` line, and keep every constraint verbatim.

```text
[SUBJECT: describe the subject in one clause — e.g. "a hedgerow dividing two harvested fields", "a slow river bend under low cloud", "a stand of pine on a ridge"]

Rendered as a landscape photograph. Natural light, shallow depth of field, slightly
defocused throughout so the frame reads as a backdrop rather than a subject.
Shot on a 50mm lens at f/2.0, ISO 200, handheld, very fine natural film grain.

STYLE — apply all of the following, they are not optional:
- full-bleed natural landscape — hills, field, forest, coastline or sky
- soft overcast or golden-hour light; no harsh sun, no visible sunstar, no hard shadows
- muted natural greens and earth tones, low saturation, gentle contrast
- slight defocus so the image reads as a backdrop, not a subject
- horizon placed low (bottom third) or high (top third), never centred
- a single quiet tonal field across the middle of the frame — no busy detail there
- optional out-of-focus foreground grass or branch along one edge for depth

COLOUR: sage and moss greens, oat, stone grey, warm bone. Nothing saturated.
The brightest value in the frame should be a soft sky, not a highlight.

NEGATIVE SPACE: The centre must be quiet and low-contrast so a white sheet of type
can sit on it. Keep the middle third free of horizon lines, strong edges, hard
tonal breaks and any subject that would compete with overlaid text.

DO NOT INCLUDE: people looking at camera, urban or industrial scenes, buildings,
vehicles, high saturation, HDR processing, heavy vignette, lens flare, vector or
3D rendering, illustration, text or watermarks in the image.
```

**Target —** provider, model and resolution are all **configurable**; set them to whatever image stack the project uses. Recommended defaults: `1536×1024` (3:2 landscape) for a full-bleed hero, `1024×1536` for a portrait sheet, `1024×1024` for a square plate. Ask for 2–3 variations and pick the one with the quietest middle third.

## Hard constraints

These travel with the prompt on every generation — do not drop them to fit a subject.

- full-bleed natural landscape — hills, field, forest, sky
- soft overcast or golden-hour light, no harsh sun
- muted natural greens and earth tones, low saturation
- slight defocus so the image reads as a backdrop, not a subject
- horizon placed low or high, never centred
- negative space — the centre must be quiet and low-contrast so a white sheet of type can sit on it
- never include legible text, logos or UI chrome in the generated image

## Negative prompt

```text
people looking at camera, portraits, crowds, urban or industrial scenes, buildings,
machinery, vehicles, high saturation, oversaturated greens, HDR processing, heavy
contrast, lens flare, sunstar, bokeh balls, vector art, 3D rendering, illustration,
painterly texture, text, lettering, watermark, logo, UI chrome, borders, frames
```

## Post-generation checks

1. Cover the middle third with a white rectangle at 86% opacity — 15px text must still be legible on it. If not, regenerate.
2. The horizon must not sit between 40% and 60% of the frame height.
3. No element in the frame should draw the eye more than the sky does.
4. Convert to greyscale mentally: the image should read as three or four soft tonal bands, not as a scene with a subject.

## Worked examples

Three unrelated subjects, same recipe — the style holds because the constraints, not the subject, carry it.

**A — carbon-removal reporting**

```text
[SUBJECT: a wide harvested barley field with a single hedgerow running across the far edge]
```
Expect: oat-and-sage horizontal bands, horizon high at ~28%, stubble texture entirely defocused, sky pale and even. The quietest area is the mid-field — ideal for the sheet.

**B — a coastal shipping and freight analytics product**

```text
[SUBJECT: a tidal estuary at low water, sandbanks and shallow channels under flat cloud]
```
Expect: near-monochrome stone and moss, horizon low at ~72%, cloud doing all the work in the top two-thirds. Reads industrial-adjacent without a single industrial object in frame.

**C — a clinical-research journal**

```text
[SUBJECT: an alpine meadow sloping away toward a treeline lost in haze]
```
Expect: layered green-to-grey recession, no hard edges anywhere, horizon dissolved rather than drawn. Grave and quiet — appropriate for a subject that has nothing to do with meadows.
