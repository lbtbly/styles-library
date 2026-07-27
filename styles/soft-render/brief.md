# Soft Render

**Pairing:** Product photography × pale lime
**Concept:** Borderless pale fills and oversized light numerals, presented as a soft-focus 3D render in a grey studio.

Soft Render is for products that want a **calm physical presence** — hardware and IoT companion apps, wellness and sustainability brands, premium consumer SaaS, and the launch pages that sell them. It treats the interface as an *object*: a matte screen sitting in a grey photographic studio, slightly out of focus at the frame edges, lit from one soft source. Inside that object, everything is borderless — cards are separated by a whisper of fill difference and a lot of air, never by a stroke.

Reach for it when the brand adjective list contains *calm, tactile, premium, soft, modern*. Do **not** reach for it for dense data tools, developer consoles, high-urgency operational software, or budget/utilitarian positioning — the airiness that makes it feel expensive makes it feel slow when there are 400 rows to scan.

---

## Palette

| Token | Value | Role | Where it is allowed to appear |
|---|---|---|---|
| `--bg` | `#E2E2E2` | The grey studio ground. The colour of the room. | Page background, the stage behind the device, gaps between cards. Never on a card. |
| `--surface` | `#D9DED2` | Card fill — a barely-there warm-grey-green. | Cards, panels, list rows, sidebar rail, chart wells. This is the only "card colour". |
| `--raised` | `rgba(255, 255, 255, 0.72)` | Frosted translucent control layer. | Buttons, segmented controls, floating toolbars, tooltips, avatar chips, anything that sits *on top of* a card or image. Always pair with `backdrop-filter`. |
| `--ink` | `#101010` | Primary text and icons. | Headings, numerals, body copy, icon strokes. |
| `--muted` | `#6E7168` | Secondary text. | Labels, captions, units, axis ticks, inactive nav, helper text. Never for anything below 11px. |
| `--line` | `transparent` | **Deliberately transparent.** This style has no borders. | Nowhere. It exists so that a component library that expects a `--line` token renders nothing. |
| `--accent` | `#DCEE92` | Pale lime. Signals "live / active / positive". | Small fills only: chips, pills, toggle-on states, one primary button, chart bar highlights, progress fills, a single active nav pip. Never a page-wide background. |
| `--accent-ink` | `#20260A` | Text and icons on `--accent`. | Only on top of `--accent`. |
| `--deep` | `#1E7C5A` | The one saturated colour. Deep green. | Status dots, a single emphasized numeral, sparkline strokes, a "verified/secure" badge. Use at most twice per screen. |

Contrast notes: `--ink` on `--bg` is ~16:1 — safe everywhere. `--accent` on `--bg` is **not** a text pairing; lime only ever carries `--accent-ink`. `--muted` on `--surface` passes AA for 14px and up; do not shrink it below 11px, and never set `--muted` on `--accent`.

```css
:root {
  --bg:         #E2E2E2;
  --surface:    #D9DED2;
  --raised:     rgba(255, 255, 255, 0.72);
  --ink:        #101010;
  --muted:      #6E7168;
  --line:       transparent;
  --accent:     #DCEE92;
  --accent-ink: #20260A;
  --deep:       #1E7C5A;
}
```

---

## Typography

One geometric sans, **light to regular weight only**. This style never uses bold — not for headings, not for emphasis, not for numbers. Weight contrast is deliberately near-zero; size and colour do all the separating.

```css
--font: "Aeonik", "General Sans", "Inter", -apple-system, BlinkMacSystemFont,
        "Segoe UI", "Helvetica Neue", Arial, sans-serif;
```

If you can load webfonts, use Aeonik or General Sans; the Google fallback is **Inter at 300/400** (or Poppins Light, or Work Sans Light). Offline, the system chain above lands on SF Pro / Segoe UI / Helvetica, all of which have usable Light cuts.

| Role | Size / line-height | Weight | Tracking | Colour |
|---|---|---|---|---|
| Hero numeral | 56 / 56 | 300 | -0.02em | `--ink` |
| Display / page hero | 44 / 48 | 300 | -0.02em | `--ink` |
| Secondary numeral | 32 / 34 | 300 | -0.01em | `--ink` |
| Page title | 28 / 34 | 300 | -0.01em | `--ink` |
| Card title | 20 / 26 | 400 | 0 | `--ink` |
| Sub-title | 16 / 24 | 400 | 0 | `--ink` |
| Body | 14 / 21 | 400 | 0 | `--ink` |
| Body secondary | 14 / 21 | 400 | 0 | `--muted` |
| Label / caption | 11 / 14 | 400 | 0.01em | `--muted` |
| Button text | 13 / 13 | 400 | 0 | `--ink` or `--accent-ink` |

**Usage rules** (from `tokens.type.usage`):

- **Set everything a weight lighter than feels safe.** If 400 looks right, try 300. Never exceed 400 anywhere in the artifact.
- **Numerals are large and thin.** A metric card is a 56px/300 number with an 11px `--muted` label underneath — that size gap *is* the hierarchy. Units (`°C`, `%`, `min`) sit at 14px `--muted`, baseline-aligned with the numeral, never superscripted.
- **No uppercase except tiny labels** (11px and below), and even then use it sparingly — sentence case is the default for every heading, button and nav item.
- **Tracking stays neutral.** Only the 56px+ numerals get negative tracking; nothing gets positive tracking above 0.01em.
- Use `font-variant-numeric: tabular-nums` on anything that ticks or updates so the layout does not jitter.

---

## Texture & effects

Four effects carry the whole style. Implement all four.

### 1. The studio ground

The page is a photographic sweep, not a flat colour: `--bg` with a soft light pool up and to the left, falling off at the corners.

```css
body {
  background:
    radial-gradient(120% 90% at 28% 0%, #EFEFEF 0%, #E2E2E2 46%, #D6D6D6 100%);
  background-attachment: fixed;
}
```

### 2. Borderless fills

Cards have **no stroke at all**. The only thing separating a card from the ground is the fill difference between `--surface` and `--bg`, plus generous space.

```css
.card {
  background: var(--surface);
  border: none;               /* say it out loud — do not inherit a border */
  border-radius: 20px;
  padding: 24px;
}
```

If a card must sit on top of another card, do not add a stroke — switch it to `--raised` and blur it (see below).

### 3. Frosted controls

Anything that floats — buttons, segmented controls, tooltips, toolbars over imagery — uses the translucent white layer with a real backdrop blur.

```css
.frosted {
  background: var(--raised);                /* rgba(255, 255, 255, 0.72) */
  backdrop-filter: blur(20px) saturate(115%);
  -webkit-backdrop-filter: blur(20px) saturate(115%);
  border-radius: 999px;
  box-shadow: 0 1px 2px rgb(0 0 0 / .04);   /* the ONLY hairline allowed, and it is a shadow */
}
```

### 4. Big soft shadows

Shadows are large, low-opacity and offset far down. There are no tight `0 1px 3px` UI shadows in this style except the one inside `.frosted` above.

```css
--shadow-object: 0 40px 80px -40px rgb(0 0 0 / .35);   /* the device / hero object */
--shadow-lift:   0 24px 48px -32px rgb(0 0 0 / .28);   /* a card that is being dragged or hovered */
--shadow-pop:    0 18px 40px -24px rgb(0 0 0 / .22);   /* modals, dropdowns, drawers */
```

### 5. The soft-focus render presentation (optional but signature)

The strongest expression of this style frames the entire artifact as a matte object photographed in the studio: a rounded screen floating with `--shadow-object`, with the frame edges falling gently out of focus.

```css
.stage   { padding: clamp(16px, 5vw, 72px); }
.device  {
  background: var(--bg);
  border-radius: clamp(18px, 2.4vw, 34px);
  box-shadow: 0 40px 80px -40px rgb(0 0 0 / .35),
              0 2px 4px rgb(0 0 0 / .05);
  overflow: hidden;
}
/* depth-of-field falloff painted over the stage, not the content */
.stage::after {
  content: ""; position: fixed; inset: 0; pointer-events: none;
  background: radial-gradient(88% 72% at 50% 42%,
              rgb(226 226 226 / 0) 55%, rgb(214 214 214 / .55) 100%);
}
```

Keep the falloff on a `::after` overlay — never `filter: blur()` on the content itself, which would make text unreadable.

### 6. Grain (very light)

A trace of sensor grain keeps the large flat greys from banding. Keep it under 4%.

```css
.grain::before {
  content: ""; position: absolute; inset: 0; pointer-events: none;
  opacity: .035; mix-blend-mode: multiply;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='160' height='160'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.8' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='160' height='160' filter='url(%23n)'/%3E%3C/svg%3E");
}
```

---

## Layout & spacing

- **Scale:** 8px. Legal steps: 4, 8, 12, 16, 20, 24, 32, 40, 56, 72.
- **Because there are no borders, spacing is the only separator.** Gaps between cards are **20–24px, never 8px**. Inside a card, 12–16px between stacked elements. If two things are 8px apart they read as one thing — that is the only correct use of 8px.
- **Card padding:** 24px desktop, 20px on narrow. Compact list rows may drop to 16px vertical.
- **Radii:** 20px on cards and panels, 16px on nested cards and media wells, 12px on inputs and small tiles, `999px` on every button, chip, toggle and avatar. Nothing is square.
- **Container:** 1200px max for dashboards, 1080px for marketing pages, 32px side gutters shrinking to 16px under 640px.
- **Grid attitude:** wide and low, not tall and dense. A 12-column grid where most cards span 4–8 columns and are wider than they are tall. Let one card be visibly bigger than the rest — the hero metric — and let it breathe.
- **Density:** low. A dashboard screen carries 6–9 cards, not 20. If you need 20, this is the wrong style.
- **Rhythm:** marketing sections are 96–120px apart vertically; dashboard rows are 24px apart.

---

## Components

### Buttons

Fully rounded, no borders, no bold. Primary is the one lime moment on the screen.

```css
.btn        { font: 400 13px/1 var(--font); padding: 12px 20px; border: 0;
              border-radius: 999px; cursor: pointer; display: inline-flex;
              align-items: center; gap: 8px; transition: transform .18s, box-shadow .18s; }
.btn-primary{ background: var(--accent); color: var(--accent-ink); }
.btn-primary:hover { transform: translateY(-1px); box-shadow: 0 10px 20px -12px rgb(0 0 0 / .35); }
.btn-secondary{ background: var(--raised); color: var(--ink);
              backdrop-filter: blur(20px); box-shadow: 0 1px 2px rgb(0 0 0 / .05); }
.btn-ghost  { background: transparent; color: var(--muted); padding-inline: 12px; }
.btn-ghost:hover { color: var(--ink); background: rgb(255 255 255 / .45); }
```

One `.btn-primary` per view. A second lime button anywhere on the same screen kills the effect.

### Inputs & selects

```css
.field { background: rgb(255 255 255 / .55); border: 0; border-radius: 12px;
         padding: 13px 16px; font: 400 14px/1.4 var(--font); color: var(--ink);
         width: 100%; }
.field::placeholder { color: var(--muted); }
.field:focus { outline: 0; background: rgb(255 255 255 / .85);
               box-shadow: 0 0 0 3px rgb(220 238 146 / .55); }   /* lime focus halo */
.select { appearance: none; padding-right: 38px;
          background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='8'%3E%3Cpath d='M1 1l5 5 5-5' fill='none' stroke='%236E7168' stroke-width='1.4'/%3E%3C/svg%3E");
          background-repeat: no-repeat; background-position: right 16px center; }
```

Labels sit *above* the field at 11px `--muted`. Error state is `--deep`-free: use a 1px inset shadow in `rgb(150 60 60 / .5)` and red-free copy where possible; this style has no error red token, so keep validation textual.

### Nav / sidebar

A narrow icon rail on `--surface`, fully rounded, floating away from the edge — not a full-height wall. The active item is a lime pill.

```css
.rail       { background: var(--surface); border-radius: 999px; padding: 12px 8px;
              display: flex; flex-direction: column; gap: 6px; align-self: start; }
.rail a     { width: 40px; height: 40px; border-radius: 999px; display: grid;
              place-items: center; color: var(--muted); }
.rail a[aria-current] { background: var(--accent); color: var(--accent-ink); }
```

Top nav on marketing pages is a floating frosted pill centred in the header, with the wordmark left and one primary button right.

### Cards

```css
.card       { background: var(--surface); border-radius: 20px; padding: 24px; }
.card-head  { display: flex; align-items: center; justify-content: space-between;
              margin-bottom: 20px; }
.card-title { font: 400 20px/26px var(--font); }
.metric     { font: 300 56px/56px var(--font); letter-spacing: -.02em; }
.metric-unit{ font: 400 14px/21px var(--font); color: var(--muted); }
.metric-label{ font: 400 11px/14px var(--font); color: var(--muted); }
```

Media inside a card sits in a 16px-radius well, inset 0 from the padding box.

### Tables

Tables are borderless list-cards, not grids. No rules, no zebra striping — row separation is 4px of `--bg` showing through between `--raised` rows.

```css
.table      { width: 100%; border-collapse: separate; border-spacing: 0 4px; }
.table th   { font: 400 11px/14px var(--font); color: var(--muted);
              text-align: left; padding: 0 16px 8px; }
.table td   { background: rgb(255 255 255 / .45); padding: 16px; }
.table tr td:first-child { border-radius: 14px 0 0 14px; }
.table tr td:last-child  { border-radius: 0 14px 14px 0; }
.table tr:hover td { background: rgb(255 255 255 / .72); }
```

### Chips & badges

```css
.chip       { font: 400 11px/1 var(--font); padding: 7px 12px; border-radius: 999px;
              background: rgb(255 255 255 / .55); color: var(--muted); }
.chip-on    { background: var(--accent); color: var(--accent-ink); }
.dot        { width: 7px; height: 7px; border-radius: 999px; background: var(--deep); }
```

### Modals & drawers

A drawer is a `--raised` frosted sheet with a 24px radius and `--shadow-pop`, sliding in from the right with 24px of `--bg` still visible behind it. The scrim is `rgb(226 226 226 / .55)` **plus** `backdrop-filter: blur(8px)` — grey and soft, never black.

```css
.scrim { position: fixed; inset: 0; background: rgb(226 226 226 / .55);
         backdrop-filter: blur(8px); }
.sheet { background: var(--raised); backdrop-filter: blur(20px);
         border-radius: 24px; padding: 24px; box-shadow: 0 18px 40px -24px rgb(0 0 0 / .22); }
```

### Footer

Low and quiet: a `--surface` card with a 20px radius sitting in the same rhythm as everything above it, 40px of internal padding, links at 14px `--muted`, wordmark at 20px/300, and one line of 11px legal type. No dark footer band — this style has no dark mode surface.

---

## Imagery

Soft Render **does** use imagery, and it is always the same thing: a soft-focus 3D product render, matte, in the grey studio.

- **Treatment:** rounded 16px well, no border, image bleeds to the well edge. Add a `linear-gradient(to top, rgb(0 0 0 / .18), transparent 55%)` only if a frosted control sits on top of it.
- **Subject:** the product itself, or an abstract matte form. Shallow depth of field — the subject sharp, the background dissolving.
- **Never:** stock photos of people at desks, flat vector illustration, line-art icon spots, or saturated photography. One lime element may appear in the render; nothing else is coloured.
- **Icons:** 1.4px stroke, rounded caps and joins, 20px box, `--muted` at rest and `--ink` when active. Inline SVG, never a filled glyph.
- **Charts:** bars and areas in `--accent` with `--surface`-toned rests, 999px-rounded bar caps, no gridlines, no axis lines, ticks at 11px `--muted`.
- If you have no render available, generate one with `image-recipe.md`, or build the object out of layered radial gradients — a blurred ellipse stack reads as a matte form and stays offline.

---

## Do

1. Set type one weight lighter than you think — 300 for anything 28px and up.
2. Let one 56px numeral dominate each screen and give it a whole card.
3. Separate cards with 20–24px of `--bg`, never with a stroke.
4. Round *everything*: 20px cards, 999px controls.
5. Use `--accent` exactly once as a fill per view, plus small chips and chart highlights.
6. Put `backdrop-filter: blur(20px)` on any control that overlaps a card or image.
7. Use one big soft shadow (`0 40px 80px -40px`) on the object, and almost none elsewhere.
8. Keep cards wide and low — landscape proportions, six to nine per dashboard.

## Don't

1. Don't add borders. `--line` is `transparent` on purpose; a 1px stroke anywhere breaks the style instantly.
2. Don't use bold, semibold, or `font-weight: 600` — this style tops out at 400.
3. Don't use tight 8px gaps between cards; without borders they merge into a blob.
4. Don't make lime a background — `#DCEE92` at page scale reads as a highlighter accident.
5. Don't put `--muted` text on `--accent`; lime only ever carries `--accent-ink` `#20260A`.
6. Don't use black scrims or dark overlays — the scrim is grey and blurred.
7. Don't introduce a second saturated colour beyond `--deep`; no red/amber/blue status system.
8. Don't pack the screen. If the design needs a dense table with 20 rows visible, pick a different style.
9. Don't use `filter: blur()` on real content to fake depth of field — overlay a gradient instead.
10. Don't square off corners for "data" areas; charts and tables get the same radii as everything else.

---

*Derived from shots by RonDesignLab ⭐️ — Convox SaaS Call Center Dashboard, Farm Management SaaS Dashboard, UPS Platform Airfreight Dashboard. Previews in `previews/` are original work in the style, not reproductions.*
