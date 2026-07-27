# Aura — image recipe

Copy the block below, replace the `[SUBJECT: …]` line with your subject, and send
it as the prompt. Everything under `STYLE` is what makes the output read as Aura;
keep it verbatim.

```text
[SUBJECT: describe the subject in one clause — e.g. "a stack of shipping containers", "a single ceramic cup", "an abstract network of nodes"]

Rendered as a soft gradient abstraction or a clean product render on a light ground.

STYLE — apply all of the following, they are not optional:
- near-white #F2F2F3 ground filling the whole frame
- one or two very large soft colour blooms, heavily feathered, in cool blue (#5884FF) and warm peach (#FFB08C), each spanning at least a third of the frame and fading fully to the ground with no visible edge
- any product surface rendered crisp and sharp against the soft ground — the contrast between hazy background and sharp object is the entire look
- even soft lighting, no visible light source, no specular hotspots
- shadows are wide, soft and low-contrast; contact shadow only
- no texture, grain or noise anywhere — surfaces are perfectly clean matte or clean gloss
- restrained palette: the ground, the two blooms, and the subject's own material. No third accent colour
- calm, centred, generous composition with a lot of empty ground

NEGATIVE SPACE: Keep the centre-top clear for a large headline — at least 35% of the frame must be empty near-white or bloom, with no subject detail in it.

DO NOT INCLUDE: grain or noise, dark backgrounds, hard shadows, glassmorphism, 3D bevels, busy detail, legible text, logos, UI chrome, watermarks, borders or frames.
```

**Target** — provider, model and resolution are configurable; set them to
whatever image stack you are using.

- **Provider:** configurable — set to your image provider
- **Model:** configurable — set to your image model
- **Resolution:** `1536x1024` (3:2 landscape) · `1024x1536` portrait · `1024x1024` square

## Hard constraints

Every one of these must survive into the final prompt. If a constraint is
dropped, the image stops being Aura.

- near-white `#F2F2F3` ground
- one or two very large soft colour blooms in cool blue and warm peach, heavily feathered
- any product surface rendered crisp and sharp against the soft ground
- even soft lighting, no visible light source
- no texture, grain or noise anywhere
- negative space — keep the centre-top clear for a large headline, at least 35% of the frame
- never include legible text, logos or UI chrome in the generated image

## Negative prompt

```text
grain, noise, film grain, dark background, black background, moody lighting, hard shadows, harsh contrast, glassmorphism, frosted glass, 3D bevel, chrome bezel, busy detail, clutter, text, lettering, typography, watermark, logo, UI chrome, buttons, vignette, border, frame
```

## Worked examples

Three deliberately unrelated subjects — the style holds because the ground,
blooms and lighting are doing the work, not the subject.

**1 · Infrastructure**

> `[SUBJECT: a loose cluster of stacked shipping containers seen from a low three-quarter angle]`
> Rendered as a soft gradient abstraction or a clean product render on a light ground.
> …containers are matte, edges razor-sharp, sitting on the near-white ground while a cool blue bloom rises behind the left stack and a peach bloom warms the right horizon. Upper 40% of the frame is empty haze.

**2 · Botany**

> `[SUBJECT: a single monstera leaf held upright, stem cropped by the bottom edge]`
> Rendered as a soft gradient abstraction or a clean product render on a light ground.
> …the leaf is crisply lit and perfectly in focus with a wide soft contact shadow; the blooms sit behind it, peach low-left and blue high-right, so the silhouette reads clean against empty ground above.

**3 · Abstract data**

> `[SUBJECT: an abstract network of small connected nodes drifting in space]`
> Rendered as a soft gradient abstraction or a clean product render on a light ground.
> …nodes are small, crisp, matte-white spheres with hairline connectors, clustered in the lower third; the entire top of the frame is one large feathered blue bloom dissolving into `#F2F2F3`.
