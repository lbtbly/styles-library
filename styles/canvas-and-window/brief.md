# Canvas & Window

**Pairing:** App window × photographer's seamless
**Concept:** Float the product in a rounded window on a flat neutral stage so the interface is the only subject in frame.

Canvas & Window is a *staging* style. You compose the shot, not just the screen: a rounded app window sits centred on an unbroken grey field with real breathing room on all four sides, lifted by one soft wide shadow, and everything inside the window is flat. Use it for SaaS product marketing where the app is the hero, for dashboards and CRM, for feature announcements and changelogs, documentation screenshots, and investor or sales decks. It projects composure — the product looks finished and photographed rather than sketched.

Avoid it for editorial or content-led sites, brand identity work, products with no screen to show, and dark-mode-first tools. Without a screen to frame, the stage is just an empty grey page.

---

## Palette

Sampled from the source shots. Fixed values.

| Token | Hex | Role | Where it is allowed to appear |
|---|---|---|---|
| `--bg` | `#ECECEC` | The stage | The flat field the window floats on. Also the page ground on marketing surfaces. Never used *inside* the window. |
| `--surface` | `#FFFFFF` | Window & card fill | The app window, every card, the top bar, panels, popovers, pricing cards. |
| `--subtle` | `#F6F7F8` | Inside-window ground | The window's content area behind cards, sidebar fill, table header rows, input wells, code blocks. This is the only grey allowed inside the window. |
| `--ink` | `#0E1113` | Primary text | Headings, card titles, figures, body copy, the browser-chrome URL text. |
| `--muted` | `#6A7178` | Secondary text | Labels, captions, meta, placeholders, inactive nav, axis labels, footnotes. |
| `--line` | `#E5E7EA` | Hairline border | Card borders, dividers, table rules, input borders, window-chrome separator. Always 1px. |
| `--accent` | `#00849E` | Teal-cyan accent | Primary button, active nav, links, focus ring, chart series 1, selected state, "Recommended" plan marker. The only saturated hue. |
| `--positive` | `#12805C` | Positive state | Up-deltas, "Active"/"Paid"/"Healthy" chips, success ticks, upward chart segments. |
| `--negative` | `#C0392B` | Negative state | Down-deltas, "Failed"/"Past due" chips, destructive labels, error text. |

**Chip tints** — 10% tints of a semantic hue on white, given as literal hexes so they stay stable:

| Tint | Hex | Pairs with text colour | Typical use |
|---|---|---|---|
| Mint | `#E7F5EF` | `#12805C` | Active, Paid, Delivered, On track |
| Lilac | `#EEEBFB` | `#5B4BC4` | Beta, Trial, Scheduled, Draft |
| Butter | `#FBF3E0` | `#8A6100` | Pending, Review, Low stock |
| Blush | `#FBECEA` | `#C0392B` | Failed, Past due, Churn risk |

**Contrast note:** `#00849E` on white measures ≈4.4:1. It is safe for fills, borders, icons, and text at **14px semibold or larger**. For 13px links, keep the text `#0E1113` and use `#00849E` for the underline and hover state.

```css
:root {
  /* palette — verbatim from style.json */
  --bg:       #ECECEC;
  --surface:  #FFFFFF;
  --subtle:   #F6F7F8;
  --ink:      #0E1113;
  --muted:    #6A7178;
  --line:     #E5E7EA;
  --accent:   #00849E;
  --positive: #12805C;
  --negative: #C0392B;

  /* chip tints */
  --tint-mint:   #E7F5EF;
  --tint-lilac:  #EEEBFB;
  --tint-butter: #FBF3E0;
  --tint-blush:  #FBECEA;
  --ink-lilac:   #5B4BC4;
  --ink-butter:  #8A6100;

  /* derived */
  --accent-wash: rgb(0 132 158 / .10);
  --focus:       rgb(0 132 158 / .20);

  /* the one elevation in the system */
  --lift: 0 24px 60px -20px rgb(14 17 19 / .22);

  /* geometry */
  --r-window: 16px;
  --r-card:   12px;
  --r-ctl:    8px;
  --r-chip:   6px;
  --stage:    64px;   /* breathing room around the window: 48–80px */
  --side:     232px;  /* in-window sidebar */
}
```

---

## Typography

One family. A second face is permitted **only** in the browser-chrome URL field, where a system UI face is more convincing.

```css
--font: "Inter", "General Sans", "Plus Jakarta Sans", -apple-system, BlinkMacSystemFont,
        "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
--font-chrome: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
```

| Role | Size / line-height | Weight | Tracking | Notes |
|---|---|---|---|---|
| Marketing headline (stage) | 40 / 46 | 600 | -0.02em | Only outside the window, on a marketing surface. Drops to 30/36 under 700px. |
| Marketing subhead | 16 / 26 | 400 | 0 | `--muted`, `max-width: 60ch`, centred under the headline. |
| Window title / page title | 16 / 22 | 600 | -0.01em | The largest type *inside* the window. |
| Card title | 14 / 20 | 600 | 0 | Sentence case, never uppercase. |
| Body | 13 / 18 | 400 | 0 | The workhorse. |
| Figure | 22 / 28 | 600 | -0.01em | KPI numbers. May reach 32/38 for one hero figure per card. |
| Chip | 11 / 14 | 500 | 0 | Sentence case on a 10% tint, full-strength hue as text colour. |
| Label / meta | 12 / 16 | 400 | 0 | `--muted`. |
| Micro label | 11 / 14 | 600 | 0.06em | ALL-CAPS. Table headers and sidebar group labels only. |

**Usage rules**

- Sentence case throughout. Never uppercase a card title or a chip.
- Status chips carry an 11px medium label on a 10% tint with the full-strength hue as the text colour — the tint and the text always come from the same table row above.
- Figures use `font-variant-numeric: tabular-nums`; prose does not need it.
- Inside the window, nothing exceeds 22px except a single hero figure per card. Big type lives on the stage, not in the app.
- Currency and units sit at 13px `--muted` beside a 22px figure, baseline-aligned.

---

## Texture & effects

**The window is the only elevated object in the entire design.** Everything else is flat with a 1px border. If two things have shadows, the composition has already failed.

```css
.stage  { background: var(--bg); padding: var(--stage); min-height: 100vh; }
.window { max-width: 1180px; margin: 0 auto; background: var(--surface);
          border-radius: var(--r-window); overflow: hidden;
          box-shadow: 0 24px 60px -20px rgb(14 17 19 / .22); }
```

**Browser chrome** (optional but characteristic). Real, restrained, and never a screenshot of a real browser:

```html
<div class="chrome">
  <span class="dot"></span><span class="dot"></span><span class="dot"></span>
  <div class="tab">Cadence — Insights</div>
  <div class="url">app.cadence.io/insights</div>
</div>
```
```css
.chrome { height: 44px; display: flex; align-items: center; gap: 8px; padding: 0 14px;
          background: var(--subtle); border-bottom: 1px solid var(--line); }
.dot    { width: 10px; height: 10px; border-radius: 50%; background: #D6D9DC; }   /* neutral, not red/amber/green */
.tab    { height: 28px; padding: 0 12px; display: flex; align-items: center;
          background: var(--surface); border: 1px solid var(--line); border-radius: 8px 8px 0 0;
          font: 500 12px/1 var(--font-chrome); color: var(--ink); }
.url    { flex: 1; height: 28px; padding: 0 12px; display: flex; align-items: center;
          background: var(--surface); border: 1px solid var(--line); border-radius: 999px;
          font: 400 12px/1 var(--font-chrome); color: var(--muted); }
```

Traffic-light dots stay neutral grey — coloured dots pull the eye off the product. The URL field is a rounded pill, and the domain is plausible, never `example.com`.

**Status colour on cards.** State reads from the grid alone, via a 3px top strip or a 3px left rule:

```css
.card       { background: var(--surface); border: 1px solid var(--line);
              border-radius: var(--r-card); padding: 16px; box-shadow: none; }
.card-strip { border-top: 3px solid var(--accent); border-radius: var(--r-card) var(--r-card) 0 0; }
.card-rule  { box-shadow: inset 3px 0 0 var(--positive); }
```

**Focus.**

```css
:where(button, a, input, select, [tabindex]):focus-visible {
  outline: none; border-color: var(--accent); box-shadow: 0 0 0 3px var(--focus);
}
```

**Charts.** Flat, hairline-gridded, one accent series. Area fills are a flat 10% alpha, never a gradient:

```css
.spark-area { fill: rgb(0 132 158 / .10); }
.spark-line { fill: none; stroke: var(--accent); stroke-width: 2; stroke-linejoin: round; }
.grid-line  { stroke: var(--line); stroke-width: 1; }
```

**Forbidden:** gradients of any kind inside the UI, a second shadow, `backdrop-filter`, glow, perspective transforms or tilt on the window, a coloured or textured stage, and rounded corners above 16px on the window.

---

## Layout & spacing

- **Compose the shot.** Stage padding 48–80px on every side (`64px` default; `32px` under 900px; `12px` under 480px so the window never touches the edge).
- **Window** max-width 1180px, radius 14–16px, `overflow: hidden` so the chrome and the content share the corner.
- **Inside the window:** sidebar 232px, content padded 24px, cards 16px padding with 12px radius, 16px gutters between cards.
- **Base scale 4px**; common steps 8, 12, 16, 24, 32, 48, 64.
- **Grid:** 12-column thinking inside the window; KPI rows are 4-up on desktop, 2-up at 900px, 1-up at 520px. Marketing sections outside the window are centred with `max-width: 1180px`.
- **Density:** comfortable. Table rows 44–48px, list rows 56px. This style has room; it is a product shot, not a terminal.
- **Caption the shot.** A 12px `--muted` centred line under the window ("Cadence — revenue and retention in one view") is idiomatic and makes the staging deliberate.

```css
.win-body { display: grid; grid-template-columns: var(--side) 1fr; min-height: 560px; }
.win-side { background: var(--subtle); border-right: 1px solid var(--line); padding: 16px 12px; }
.win-main { background: var(--subtle); padding: 24px; min-width: 0; }
.grid-4   { display: grid; grid-template-columns: repeat(4, minmax(0,1fr)); gap: 16px; }
```

---

## Components

### Buttons

40px on marketing surfaces, 34px inside the window. 8px radius.

```css
.btn         { height: 40px; padding: 0 18px; border-radius: var(--r-ctl); border: 1px solid transparent;
               font: 600 14px/1 var(--font); display: inline-flex; align-items: center; gap: 8px; cursor: pointer; }
.btn-sm      { height: 34px; padding: 0 12px; font-size: 13px; }
.btn-primary { background: var(--accent); color: #FFFFFF; }
.btn-primary:hover { background: #026F86; }              /* accent darkened, not a new hue */
.btn-secondary { background: var(--surface); color: var(--ink); border-color: var(--line); }
.btn-secondary:hover { background: var(--subtle); }
.btn-ghost   { background: transparent; color: var(--muted); }
.btn-ghost:hover { background: var(--subtle); color: var(--ink); }
```

Buttons never carry a shadow — that elevation belongs to the window.

### Inputs & selects

```css
.field { height: 38px; padding: 0 12px; background: var(--surface); border: 1px solid var(--line);
         border-radius: var(--r-ctl); font: 400 13px/1 var(--font); color: var(--ink); }
.field::placeholder { color: var(--muted); }
.field:focus { border-color: var(--accent); box-shadow: 0 0 0 3px var(--focus); outline: none; }
.field-well  { background: var(--subtle); border-color: transparent; }   /* search inside the window */
.select { appearance: none; padding-right: 30px; }   /* chevron = inline 10×6 SVG, stroke --muted */
.toggle { width: 40px; height: 22px; border-radius: 999px; background: var(--line); position: relative; }
.toggle[aria-checked="true"] { background: var(--accent); }
.toggle i { position: absolute; top: 2px; left: 2px; width: 18px; height: 18px; border-radius: 50%;
            background: var(--surface); transition: transform .16s ease; }
.toggle[aria-checked="true"] i { transform: translateX(18px); }
```

### Nav / sidebar

```css
.win-side .group { font: 600 11px/14px var(--font); letter-spacing: .06em; text-transform: uppercase;
                   color: var(--muted); padding: 14px 10px 6px; }
.nav-item { height: 34px; padding: 0 10px; border-radius: var(--r-ctl); color: var(--muted);
            display: flex; align-items: center; gap: 10px; font: 500 13px/1 var(--font); }
.nav-item:hover { background: var(--surface); color: var(--ink); }
.nav-item[aria-current] { background: var(--surface); color: var(--accent); font-weight: 600;
                          border: 1px solid var(--line); }
```

The in-window top bar is 56px, `--surface`, with a 1px bottom rule: workspace name, breadcrumb, a `--subtle` search field, then icon buttons and a 28px avatar.

On a **marketing** surface the nav is a 64px transparent bar over the stage: wordmark left, 13px `--muted` links centre, one secondary and one primary button right. No sticky shadow — if it sticks, give it a 1px `--line` bottom rule instead.

### Cards

```html
<article class="card card-strip">
  <p class="label">Net revenue retention</p>
  <p class="figure">112.4<span class="unit">%</span></p>
  <p class="delta up">▲ 3.1 pts vs last quarter</p>
</article>
```

Rules: 1px `--line` border, 12px radius, 16px padding, no shadow. Status is a 3px top strip or left rule in a semantic hue. Label above figure, delta below, always in that order. Cards sit on `--subtle` inside the window and on `--bg` on the stage.

### Tables

```css
thead th { background: var(--subtle); font: 600 11px/14px var(--font); letter-spacing: .06em;
           text-transform: uppercase; color: var(--muted); text-align: left;
           padding: 10px 14px; border-bottom: 1px solid var(--line); }
tbody td { padding: 13px 14px; border-bottom: 1px solid var(--line); font-size: 13px; }
tbody tr:hover td { background: var(--subtle); }
tbody tr:last-child td { border-bottom: none; }
td.num, th.num { text-align: right; font-variant-numeric: tabular-nums; }
```

Tables live inside a bordered card (12px radius, `overflow: hidden`) — unlike the flat-out full-bleed tables of denser styles, here the table is an object in the composition.

### Chips / badges

```css
.chip { display: inline-flex; align-items: center; gap: 6px; height: 22px; padding: 0 8px;
        border-radius: var(--r-chip); font: 500 11px/1 var(--font); }
.chip-mint   { background: var(--tint-mint);   color: var(--positive); }
.chip-lilac  { background: var(--tint-lilac);  color: var(--ink-lilac); }
.chip-butter { background: var(--tint-butter); color: var(--ink-butter); }
.chip-blush  { background: var(--tint-blush);  color: var(--negative); }
.chip-plain  { background: var(--subtle);      color: var(--muted); }
```

A leading 6px dot in `currentColor` is optional and should be used consistently or not at all.

### Modals & popovers

There is only one shadow, and the window owns it. A modal *inside* the window is therefore drawn with a 1px `--line` border and a `rgb(14 17 19 / .32)` scrim, plus at most a softened reuse of the window lift:

```css
.scrim  { position: absolute; inset: 0; background: rgb(14 17 19 / .32); }
.modal  { background: var(--surface); border: 1px solid var(--line); border-radius: var(--r-card);
          box-shadow: 0 24px 60px -20px rgb(14 17 19 / .22); max-width: 520px; }
.popover{ background: var(--surface); border: 1px solid var(--line); border-radius: var(--r-ctl); }
```

Popovers and dropdowns take the border only — no shadow.

### Footer

Marketing surfaces get a real footer on the stage: 4 columns of 13px `--muted` links under 11px ALL-CAPS group labels, a 1px `--line` rule above, and a bottom row with the wordmark, a copyright line, and a status chip ("All systems operational", mint). Inside the window, a 40px bar with 12px `--muted` text and a version number is enough.

---

## Imagery

**The product screenshot is the imagery.** The window *is* the hero shot; do not put a photograph behind it or inside it.

- **No photography.** No stock desks, hands, offices, or people. If a human presence is needed, use a 28px `--subtle` initial avatar.
- **Logos** are wordmarks set in `--ink` at 15/20 semibold with -0.02em tracking, or a 28px `--surface` rounded square with a 1px `--line` border and a simple `--accent` geometric mark inside. Customer logo strips are `--muted` wordmarks at 60% opacity, evenly spaced, never colour.
- **Icons** are 16–18px, 1.5px stroke, `currentColor`, rounded caps.
- **Charts** are the main decorative element: flat inline SVG, 1px `--line` grid, one `--accent` series, 10% flat area fill, 11px `--muted` axis labels. Donut charts use `--accent` plus two neutral greys, never a rainbow.
- **Second window.** A small secondary window (a popover, a mobile frame) may overlap the main one at the corner — but it shares the *same* shadow value and must overlap, never float separately.
- If a generated hero is genuinely needed, use `image-recipe.md`: a single rounded window on a flat `#ECECEC` field, teal `#00849E`, one shadow.

---

## Do

1. Float the window centred on an unbroken `#ECECEC` stage with 48–80px of clear margin on every side.
2. Give the window exactly one shadow — `0 24px 60px -20px rgb(14 17 19 / .22)` — and nothing else any shadow at all.
3. Keep the interior flat: 1px `#E5E7EA` borders, `#F6F7F8` grounds, `#FFFFFF` cards.
4. Show state with a 3px semantic strip or left rule on a card, so the grid reads at a glance.
5. Use the four chip tints (`#E7F5EF`, `#EEEBFB`, `#FBF3E0`, `#FBECEA`) with their paired full-strength text colour.
6. Include restrained browser chrome — neutral grey dots, a rounded URL pill with a plausible domain.
7. Caption the shot with a 12px `--muted` line beneath the window.
8. Keep in-window type under 22px; save big type for the stage.

## Don't

1. Don't tilt, rotate, or apply perspective to the window — the view is straight-on and orthographic.
2. Don't put a gradient anywhere: not on the stage, not in a card, not behind a chart.
3. Don't give buttons, cards, chips, or popovers a shadow; the window owns the only elevation.
4. Don't colour the traffic-light dots red/amber/green — they stay neutral grey.
5. Don't put a photograph on the stage or behind the window; there is no imagery but the product.
6. Don't let the window bleed to the frame edge or lose its margin at small widths — shrink the padding, never remove it.
7. Don't introduce a second accent hue; `#00849E` is the only saturated colour outside the four chip tints.
8. Don't use `#00849E` for 13px body links — keep the text `#0E1113` and let teal carry the underline.
9. Don't fill a chart area with a gradient or a second series colour; flat 10% alpha, one series.
