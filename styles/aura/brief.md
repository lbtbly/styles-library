# Aura

**Pairing:** Sunrise haze × product shot
**Concept:** Crisp white cards lifted off a soft coloured bloom — atmosphere with no texture at all.

Aura is a marketing style. It exists to make a young software product look calm,
optimistic and already-finished — the visual equivalent of a well-lit product
photograph. The whole effect is one contrast: a hazy, weatherless coloured ground
versus razor-sharp white surfaces sitting on top of it, with an enormous tightly
tracked headline doing all the talking. Reach for it on landing pages, launch
pages, pricing, waitlists and any page whose job is to convert a stranger in one
scroll. Do **not** reach for it for dense dashboards, data tables, internal admin
tooling, or any product whose primary mode is dark — the style has no dark mode
and its generosity with space is fatal to density.

---

## Palette

Nine tokens. That is the entire palette — there is no secondary accent, no
success green, no warning amber. Status is communicated with `--ink` and
`--muted`, never with new hues.

| Token | Value | Role | Allowed to appear |
|---|---|---|---|
| `--bg` | `#F2F2F3` | Page ground | Body background, section bands, the field the blooms are painted onto, input fills, inactive tab tracks |
| `--surface` | `#FFFFFF` | Card / sheet | Cards, nav bar, modals, dropdowns, the product screenshot frame, footer top band |
| `--ink` | `#0C0C0C` | Primary text & dark fill | Headlines, card titles, table figures, logo wordmark, the *dark* pill CTA fill and its border, footer background |
| `--muted` | `#6C6F76` | Secondary text | Body paragraphs, sub-labels, nav links at rest, footer links, form helper text, placeholder text, chart axis labels |
| `--line` | `#E7E8EA` | Hairline | 1px card borders, dividers, input borders, table rules, logo-row separators. Never thicker than 1px |
| `--accent` | `#2450E8` | Single accent | Eyebrow labels, inline links, active nav underline, focus rings, small icon glyphs, one KPI figure per card, the accent pill CTA |
| `--accent_ink` | `#FFFFFF` | Text on accent | Label text sitting on a `--accent` fill. Nothing else |
| `--bloom_a` | `rgba(88, 132, 255, 0.28)` | Cool bloom | Radial-gradient stop only. Never a fill, border or text colour |
| `--bloom_b` | `rgba(255, 176, 140, 0.24)` | Warm bloom | Radial-gradient stop only. Never a fill, border or text colour |

The blooms are the only warm colour in the system, and they are *never* opaque.
If you find yourself using `#FFB08C` as a solid, you have left the style.

```css
:root {
  --bg:          #F2F2F3;
  --surface:     #FFFFFF;
  --ink:         #0C0C0C;
  --muted:       #6C6F76;
  --line:        #E7E8EA;
  --accent:      #2450E8;
  --accent-ink:  #FFFFFF;
  --bloom-a:     rgba(88, 132, 255, 0.28);
  --bloom-b:     rgba(255, 176, 140, 0.24);

  /* derived — allowed, do not invent others */
  --accent-wash: rgba(36, 80, 232, 0.08);  /* accent chip fill */
  --shadow-card: 0 8px 32px -12px rgb(12 12 12 / .12);
  --shadow-lift: 0 24px 64px -24px rgb(12 12 12 / .18);
}
```

---

## Typography

One family. A neo-grotesque or geometric sans — the reference cut is Inter
Display; General Sans and Aeonik are equally correct. **The headline is the
whole design**, so the family must have a real semibold and must tolerate very
tight tracking.

```css
--font-sans: "Inter Display", "Inter", "General Sans", "Aeonik",
             -apple-system, BlinkMacSystemFont, "Segoe UI",
             "Helvetica Neue", Helvetica, Arial, sans-serif;
```

Numerals: enable `font-feature-settings: "tnum" 1;` on any figure that will
change (counters, prices, metrics) so it does not jitter.

| Role | Size / line-height | Weight | Tracking | Colour |
|---|---|---|---|---|
| Hero | 68px / 68px | 600 | `-0.035em` | `--ink` |
| Hero (≤700px) | clamp to 40px / 42px | 600 | `-0.03em` | `--ink` |
| Section heading | 36px / 42px | 600 | `-0.025em` | `--ink` |
| Card / feature title | 20px / 28px | 600 | `-0.015em` | `--ink` |
| Lead paragraph | 18px / 30px | 400 | `-0.005em` | `--muted` |
| Body | 16px / 26px | 400 | `0` | `--muted` |
| Small / caption | 14px / 22px | 400 | `0` | `--muted` |
| Label / eyebrow | 12px / 16px | 500 | `0.02em` | `--accent` or `--muted` |
| Metric figure | 44px / 48px | 600 | `-0.03em` | `--ink` |

**Usage rules (from the style definition, non-negotiable):**

- Set headlines **as large and as tight as legibility allows**. When in doubt, go
  one step larger and one notch tighter, not smaller.
- **Body copy stays grey and small.** Never promote a paragraph to `--ink`; the
  contrast between black headline and grey body is the hierarchy.
- **Sentence case everywhere** — headlines, buttons, nav, labels. No Title Case,
  no ALL CAPS except a single 12px eyebrow, and even that is optional.
- **Never letterspace the hero.** Positive tracking on a display size instantly
  reads as a different (older) style.
- Headline measure: 12–18 words max, wrapped by hand with `<br>` or
  `max-width: 16ch` so the ragged edge is deliberate.
- Bold inside a paragraph is allowed once, in `--ink`, to promote a single
  phrase. That is the only in-paragraph emphasis.

---

## Texture & effects

**Atmosphere with no material.** There is no grain, no glass, no bevel, no inner
shadow, no gloss. Two techniques carry the whole style.

### 1. The bloom (the ground)

One or two very large, heavily feathered radial gradients painted on a
`--bg` field. They must be *large* — 800–1400px across — and stopped to
`transparent` well before the edge. Put them behind everything, on the section,
not on the card.

```css
.bloom-field {
  position: relative;
  background: var(--bg);
  isolation: isolate;
}
.bloom-field::before {
  content: "";
  position: absolute;
  inset: 0;
  z-index: -1;
  background:
    radial-gradient(60% 46% at 22% 2%,  var(--bloom-a), transparent 70%),
    radial-gradient(52% 40% at 84% 12%, var(--bloom-b), transparent 72%);
  pointer-events: none;
}
```

Variants that stay in style: a single centred bloom
(`radial-gradient(50% 40% at 50% 0%, var(--bloom-a), transparent 70%)`) for a
symmetric hero; a bottom-anchored bloom under a signup card. Two blooms maximum
per viewport. If you can see a hard edge on a bloom, the stop percentage is too
low.

### 2. The card (the figure)

Flat white, hairline border, one soft wide shadow. No gradient on the card. No
border-image. No highlight line.

```css
.card {
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: 16px;
  padding: 24px;
  box-shadow: 0 8px 32px -12px rgb(12 12 12 / .12);
}
.card--hero {           /* the product-shot frame bleeding out of the hero */
  border-radius: 20px 20px 0 0;
  box-shadow: 0 24px 64px -24px rgb(12 12 12 / .18);
}
```

### Other effects, in full

```css
/* focus ring — the only glow in the system */
:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }

/* accent chip / eyebrow pill */
.eyebrow { background: rgba(36,80,232,.08); color: var(--accent); }

/* hairline separator between marketing sections */
.rule { height: 1px; background: var(--line); border: 0; }

/* fade a long list or screenshot into the ground */
.fade-out { -webkit-mask-image: linear-gradient(180deg, #000 60%, transparent);
                    mask-image: linear-gradient(180deg, #000 60%, transparent); }

/* transitions: short, no bounce */
* { transition: background-color .16s ease, border-color .16s ease,
                box-shadow .16s ease, transform .16s ease; }
```

**Forbidden textures:** SVG noise/grain overlays, `backdrop-filter` /
frosted glass, `background-blend-mode`, inset highlight strokes, drop shadows
with visible offset and no blur, any gradient on a button, any gradient on text.
A gradient in Aura is *always* a bloom on a ground, never a fill on an object.

---

## Layout & spacing

- **Scale:** 8px. Use 4px only inside a chip. Real steps: 8 / 16 / 24 / 32 / 48 / 64 / 96 / 140.
- **Container:** 1160px max-width, 24px gutters (16px below 720px). The nav is a
  full-width bar with the same inner container.
- **Section rhythm:** 96px vertical padding minimum, 140px between major
  marketing beats. This is the single most style-defining number after the
  headline size — a cramped Aura page is not an Aura page.
- **Radii:** 16px cards · 12px inputs, small controls and logo tiles · 20px hero
  screenshot frame · 999px pill CTAs, chips and avatars. Nothing is square.
- **Padding:** 24px card padding standard, 32px on a hero/feature card, 14px 22px
  on a pill button, 12px 14px on an input.
- **Grid attitude:** marketing rhythm, not a dashboard grid. Full-width bands
  alternating `--bg` and `--surface`. Hero centred. Feature grid is 3 columns
  desktop → 2 at 900px → 1 at 620px, 20px gap. Logo row is a single flex row that
  wraps, opacity `.55`, greyscale, evenly spaced.
- **Density:** low, deliberately. One idea per band. A feature card carries an
  icon, a 20px title and two lines of grey body — nothing more.
- **The bleed:** the hero product screenshot is anchored to the *bottom edge* of
  the hero section and clipped by it, so the top of the frame is visible and the
  bottom runs off. Never put a screenshot in a floating centred frame with air
  underneath.

---

## Components

### Buttons

Three variants only. All pills. No gradient, no icon-only primary.

```css
.btn { display:inline-flex; align-items:center; gap:8px;
       font: 500 15px/1 var(--font-sans); letter-spacing:-.01em;
       padding:14px 22px; border-radius:999px; cursor:pointer;
       border:1px solid transparent; }

/* primary — solid ink pill. The default CTA. */
.btn--primary  { background:var(--ink); color:#fff; }
.btn--primary:hover { background:#000; transform:translateY(-1px);
                      box-shadow:0 8px 24px -10px rgb(12 12 12 / .45); }

/* accent — same pill in blue. Use for ONE action per page (signup, join). */
.btn--accent   { background:var(--accent); color:var(--accent-ink); }
.btn--accent:hover { background:#1B41C8; }

/* secondary — white pill on the bloom */
.btn--secondary{ background:var(--surface); color:var(--ink);
                 border-color:var(--line); box-shadow:0 2px 8px -4px rgb(12 12 12 / .12); }

/* ghost — text only, for tertiary nav actions */
.btn--ghost    { background:transparent; color:var(--muted); padding-inline:8px; }
.btn--ghost:hover { color:var(--ink); }
```

Never place `--primary` and `--accent` side by side; pick one as the CTA and pair
it with `--secondary`.

### Inputs & selects

```css
.field { width:100%; font:400 15px/1.4 var(--font-sans); color:var(--ink);
         background:var(--surface); border:1px solid var(--line);
         border-radius:12px; padding:13px 14px; }
.field::placeholder { color:var(--muted); }
.field:focus { outline:none; border-color:var(--accent);
               box-shadow:0 0 0 3px rgba(36,80,232,.14); }
.field[aria-invalid="true"] { border-color:var(--ink);
               box-shadow:0 0 0 3px rgb(12 12 12 / .08); }
select.field { appearance:none; padding-right:36px;
  background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='8'%3E%3Cpath d='M1 1.5 6 6.5l5-5' fill='none' stroke='%236C6F76' stroke-width='1.5' stroke-linecap='round'/%3E%3C/svg%3E");
  background-repeat:no-repeat; background-position:right 14px center; }
```

Error state uses `--ink`, not red. There is no red in this palette.

**Inline capture pill** (the waitlist signature): an input and a pill button
welded inside one white rounded container so it reads as a single object.

```css
.capture { display:flex; gap:8px; padding:8px; background:var(--surface);
           border:1px solid var(--line); border-radius:999px;
           box-shadow:0 8px 32px -12px rgb(12 12 12 / .12); }
.capture .field { border:0; box-shadow:none; background:transparent; padding-left:16px; }
.capture .btn { flex:none; }
```

### Nav

Full-width, `--surface` at 88% with no blur, hairline bottom border, sticky.
Wordmark left, links centred, one pill CTA right. Links are `--muted` 15px; the
active link is `--ink` with a 2px `--accent` underline sitting 6px below the
baseline. On mobile, collapse the centre links and keep wordmark + CTA.

```css
.nav { position:sticky; top:0; z-index:20;
       background:rgb(255 255 255 / .88);
       border-bottom:1px solid var(--line); }
```

(That is a translucent fill, *not* a `backdrop-filter` — glass is out of style here.)

### Cards

Base `.card` above. Three flavours:
- **Feature card** — 24px pad, 40px accent-wash rounded-12 icon tile, 20px title, 15px grey body.
- **Stat card** — 44px `--ink` figure with `tnum`, 14px grey label under it.
- **Quote card** — 18/30 `--ink` body (the one place body goes dark), 14px grey attribution row with a 32px circular avatar.

Cards do not lift on hover on a marketing page; only interactive cards do
(`transform:translateY(-2px)` + `--shadow-lift`).

### Tables

Aura is not a table style, but a small pricing/comparison table is legitimate:
transparent background, no vertical rules, 1px `--line` horizontal rules,
`th` 12px `--muted` medium sentence case, `td` 15px `--ink`, 14px 0 cell padding,
no zebra striping, no hover fill. Keep it under 8 rows.

### Chips & badges

```css
.chip { display:inline-flex; align-items:center; gap:6px;
        font:500 12px/1 var(--font-sans); padding:7px 12px; border-radius:999px; }
.chip--accent  { background:rgba(36,80,232,.08); color:var(--accent); }
.chip--neutral { background:var(--bg); color:var(--muted); border:1px solid var(--line); }
.chip--ink     { background:var(--ink); color:#fff; }
```

A 6px `--accent` dot before the label is the house detail.

### Modals & drawers

Centred sheet, `--surface`, 20px radius, 32px padding, `--shadow-lift`, max-width
440px. Scrim is `rgb(12 12 12 / .28)` — flat, **not** blurred. A drawer is the
same sheet pinned right with `border-radius:20px 0 0 20px`. Close control is a
32px circular ghost button top-right.

### Footer

Dark. `--ink` background, `--surface` text at 90%, `rgb(255 255 255 / .55)` for
links, `rgb(255 255 255 / .12)` hairlines. Four columns (wordmark + blurb, then
three link stacks), 64px top padding, a hairline, then a 14px legal row. The dark
footer is what stops the page dissolving at the bottom — always include it on a
landing page.

---

## Imagery

Aura uses **product imagery, not decoration**. Three legitimate sources:

1. **Product UI screenshot** — the hero anchor. Rendered inside a `--surface`
   frame with 20px top radii and `--shadow-lift`, bleeding off the bottom edge of
   the hero. In an offline artifact, *build the screenshot in HTML/CSS* — a
   miniature of the real app in the same tokens.
2. **Soft gradient abstraction** — a bloom-on-white render for section headers or
   an OG image. See `image-recipe.md`.
3. **Photography** — light, airy, high-key, people at work, cool-neutral grade,
   always inside a 16px-radius frame. Never full-bleed, never darkened, never
   with text on top.

Logos in the trust row are monochrome `--ink` at `opacity:.55`, sized by optical
weight not by bounding box. Icons are 20px, 1.5px stroke, round caps,
`--accent` or `--ink`, never filled and never multicolour. There is no
illustration style here — if you need a picture and have none, use a bloom.

---

## Do

1. Make the headline enormous and tightly tracked — it *is* the design.
2. Keep body copy grey (`#6C6F76`) and 16px. Resist promoting it.
3. Paint the atmosphere on the ground with one or two huge feathered blooms; keep every card razor-sharp on top.
4. Give sections 96–140px of vertical breathing room.
5. Bleed the hero product shot off the bottom edge of the hero section.
6. Use exactly one accent (`#2450E8`) and use it sparingly — an eyebrow, a link, a focus ring, one CTA.
7. Pill everything interactive: buttons, chips, avatars, the capture field.
8. Close the page with the dark `#0C0C0C` footer.

## Don't

1. Don't put a gradient on a button, a card, a chip or text. Gradients live only on the ground.
2. Don't add grain, noise, glass, `backdrop-filter`, bevels or inner highlights — the style is explicitly texture-free.
3. Don't introduce a second accent or a status palette. No red errors, no green success ticks.
4. Don't letterspace, italicise, underline or colour the hero headline.
5. Don't use Title Case or ALL CAPS outside a single 12px eyebrow.
6. Don't build a dense grid — no dashboards, no 24-row tables, no sidebars. Aura has no dark mode and no data mode.
7. Don't make the blooms opaque, small, or hard-edged; if you can see where one stops, it's wrong.
8. Don't float the product screenshot in the middle of the hero with air below it — anchor it to the bottom edge.
9. Don't stack a primary ink pill next to an accent blue pill; one CTA per decision.
10. Don't use square corners anywhere.
