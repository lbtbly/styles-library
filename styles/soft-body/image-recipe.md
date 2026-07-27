# Soft Body — image recipe

Copy the block below, replace the `[SUBJECT: …]` line with your subject, and send
it as the prompt. Everything under `STYLE` is what makes the output read as Soft
Body; keep it verbatim.

```text
[SUBJECT: describe the subject in one clause — e.g. "a stack of shipping containers", "a single ceramic cup", "an abstract network of nodes"]

Rendered as a soft 3D render or a rounded flat illustration.

STYLE — apply all of the following, they are not optional:
- pale lavender-grey ground #E7E8F0 filling the whole frame, flat and even
- every form is rounded and moulded — large corner radii, filleted edges, no sharp corners or points anywhere, as if injection-moulded in matte plastic
- matte surfaces with no gloss, no reflection, no specular highlight
- pastel accent palette — mint #DFF3E9, lilac #E9E6FA, peach #FCEBE4, butter #FBF4DC, sky #E2EEFB — plus exactly one saturated indigo #4A46D8 used as the single focal accent
- soft diffused lighting from above, gentle low-contrast contact shadows directly under each form
- friendly geometric shapes, generous spacing between elements, nothing touching or overlapping
- calm, centred, uncluttered composition; a small number of large objects rather than many small ones

NEGATIVE SPACE: Keep at least a third of the frame as empty tinted ground.

DO NOT INCLUDE: sharp corners, high contrast, dark backgrounds, neon, technical or industrial imagery, dense detail, legible text, logos, UI chrome, hard shadows, outlines.
```

**Target** — provider, model and resolution are configurable; set them to
whatever image stack you are using.

- **Provider:** configurable — set to your image provider
- **Model:** configurable — set to your image model
- **Resolution:** `1536x1024` (3:2 landscape) · `1024x1536` portrait · `1024x1024` square

## Hard constraints

Every one of these must survive into the final prompt. If a constraint is
dropped, the image stops being Soft Body.

- pale lavender-grey ground `#E7E8F0`
- rounded matte forms with large corner radii and no sharp edges
- pastel accent palette — mint, lilac, peach — plus one indigo `#4A46D8`
- soft diffused lighting with gentle contact shadows
- friendly geometric shapes, generous spacing between elements
- negative space — keep at least a third of the frame as empty tinted ground
- never include legible text, logos or UI chrome in the generated image

## Negative prompt

```text
sharp corners, hard edges, bevels, chamfers, high contrast, dark background, black background, dramatic lighting, hard shadows, neon, saturated colours, technical illustration, industrial, mechanical, wireframe, dense detail, clutter, text, lettering, watermark, logo, UI chrome, outlines, grain, noise, glossy reflections
```

## Worked examples

Three deliberately unrelated subjects — the style holds because the ground, the
fillets and the lighting are doing the work, not the subject.

**1 · Logistics**

> `[SUBJECT: three shipping containers stacked loosely, seen three-quarter from above]`
> Rendered as a soft 3D render or a rounded flat illustration.
> …the containers are moulded matte blocks with heavily filleted corners and no ridges, one mint, one peach, one indigo, spaced apart on the lavender-grey ground with soft contact shadows beneath each.

**2 · Domestic object**

> `[SUBJECT: a single wide ceramic cup with a rounded handle, sitting alone]`
> Rendered as a soft 3D render or a rounded flat illustration.
> …the cup is matte butter-yellow with a fat rounded rim and a fully filleted handle; a soft lilac saucer sits beneath it, and the upper half of the frame is empty tinted ground.

**3 · Abstract systems**

> `[SUBJECT: an abstract network of connected nodes]`
> Rendered as a soft 3D render or a rounded flat illustration.
> …five or six large matte spheres in mint, sky and lilac joined by thick capsule-shaped connectors with rounded ends; one sphere is indigo and slightly forward; everything is generously spaced with a lot of empty ground around the cluster.
