# Field Notes

**Pairing —** Landscape photograph × monospace caption
**Concept —** Analytics dressed as a magazine: full-bleed landscape, serif headline, monospace figures inline in prose.

Field Notes is for products that have something real to show and time to say it properly — sustainability and climate reporting, agriculture and land data, travel and outdoor brands, research desks, annual reviews and data journalism. It treats the browser window as a **printed page**: a soft landscape photograph bleeds to all four edges, and a translucent white sheet of type floats on top of it. Reach for it when the brand owns real photography and the content rewards reading; avoid it for high-frequency operational tools, developer consoles, or any product with no photographic assets — without the photograph the style collapses into plain white.

---

## Palette

Eight tokens. The hex values are sampled from the source shots and are **fixed** — do not brighten, saturate or "modernise" them.

| Token | Value | Role | Where it may appear |
|---|---|---|---|
| `bg` | `#FAFAF8` | Warm paper white | Page fallback behind the photograph; body background of any screen with no photo; sheet colour when `backdrop-filter` is unsupported |
| `surface` | `#FFFFFF` | Opaque white | Inputs, modal panels, table zebra rows, image plate mounts — anywhere the sheet's translucency would hurt legibility |
| `sheet` | `rgba(255, 255, 255, 0.86)` | The floating page sheet | The one and only container that sits on the photograph. Never nest a second sheet inside a sheet |
| `ink` | `#1C221E` | Near-black, green-shifted | Headlines, body copy, table figures, icon strokes. This is the **only** text colour for primary content |
| `muted` | `#6B7169` | Secondary text | Decks, captions, table headers, labels, placeholder text, footer copy. Never for body paragraphs |
| `line` | `#E4E5E0` | Hairline rule | 1px section rules, table rules, input borders, divider between sheet regions. Always 1px, always square |
| `accent` | `#4E6030` | Field green | Primary button fill, active nav underline, link underline, chart series, positive delta, chip fills at low opacity |
| `accent_ink` | `#FFFFFF` | Text on accent | Label of a filled `accent` button or badge. Nothing else |

Contrast: `ink` on `bg` is 13.6:1 (AAA). `accent` on `bg` is 6.1:1 — safe for body-sized links as well as fills.

```css
:root {
  --bg:         #FAFAF8;
  --surface:    #FFFFFF;
  --sheet:      rgba(255, 255, 255, 0.86);
  --ink:        #1C221E;
  --muted:      #6B7169;
  --line:       #E4E5E0;
  --accent:     #4E6030;
  --accent-ink: #FFFFFF;
}
```

Derived values you are allowed to compute (nothing else):

```css
:root {
  --accent-wash:  rgba(78, 96, 48, 0.10);   /* accent at 10% — chip and row fills */
  --accent-hover: #3E4D26;                  /* accent darkened ~12% for :hover  */
  --ink-wash:     rgba(28, 34, 30, 0.06);   /* ghost-button hover               */
  --sheet-edge:   rgba(255, 255, 255, 0.60);/* 1px inner edge on the sheet      */
}
```

---

## Typography

**Three voices, deliberately.** Every piece of text belongs to exactly one of them. Getting this three-way split right *is* the style — a Field Notes page with a single font family is not in style, however good the photograph is.

```css
:root {
  /* 1 — serif: headlines only */
  --font-serif: "Instrument Serif", "Fraunces", "Source Serif 4",
                "Iowan Old Style", "Palatino Linotype", Palatino,
                "Book Antiqua", Georgia, "Times New Roman", serif;

  /* 2 — neo-grotesque: UI, body, navigation, buttons */
  --font-sans:  "Inter", "Söhne", "Neue Haas Grotesk", -apple-system,
                BlinkMacSystemFont, "Segoe UI", "Helvetica Neue",
                Helvetica, Arial, sans-serif;

  /* 3 — monospace: every figure, date, code, ID and label */
  --font-mono:  "JetBrains Mono", "IBM Plex Mono", ui-monospace,
                "SF Mono", SFMono-Regular, Menlo, Consolas,
                "Liberation Mono", monospace;
}
```

If the artifact must be fully self-contained (no webfont requests), drop the first entries and ship the system tail — `Georgia` / `-apple-system` / `ui-monospace` carry the style perfectly well.

### Scale

| Role | Voice | Size / leading | Weight | Tracking | Notes |
|---|---|---|---|---|---|
| Display headline | serif | `clamp(34px, 5vw, 48px)` / 54px | 400 | `-0.01em` | Ends with a full stop |
| Section head | serif | 30px / 36px | 400 | `-0.005em` | Ends with a full stop |
| Deck / standfirst | sans | 18px / 28px | 400 | `0` | Colour `--muted` |
| Body | sans | 15px / 24px | 400 | `0` | Max 68ch measure |
| Figure inline | mono | 14px / 20px | 500 | `0` | Sits *inside* body prose |
| Big figure | mono | 34px / 38px | 500 | `-0.01em` | Stat blocks, table totals |
| Table cell | mono | 13px / 20px | 400 | `0` | Right-aligned, tabular nums |
| Table header | mono | 10px / 12px | 500 | `0.14em` | ALL-CAPS, `--muted` |
| Issue / section label | mono | 10px / 12px | 500 | `0.14em` | ALL-CAPS, `--muted` |
| Caption | mono | 11px / 16px | 400 | `0.02em` | Under plates and charts |
| Button label | sans | 14px / 1 | 500 | `0.01em` | |

### Usage rules

1. **Headlines end with a period.** "Ninety hectares, measured." Not a title — a sentence. This is magazine grammar and it is non-negotiable.
2. **Monospace figures appear inline in running prose**, not only in tables: *"We retired `1,284` credits across `17` sites this season."* Wrap them in `<span class="fig">` and let them sit slightly heavier than the surrounding sans.
3. **Letterspaced ALL-CAPS monospace** carries every label: issue number, section eyebrow, table header, chart axis, footer meta.
4. **Never bold a serif headline.** Emphasis comes from size and the full stop, never from weight.
5. **One serif headline per view section.** If two serif blocks are competing, one of them should be a deck.
6. Tabular figures everywhere: `font-variant-numeric: tabular-nums;` on every mono element.

```css
.fig { font-family: var(--font-mono); font-weight: 500; font-size: .95em;
       font-variant-numeric: tabular-nums; letter-spacing: 0; }
.label { font-family: var(--font-mono); font-size: 10px; line-height: 12px;
         font-weight: 500; letter-spacing: .14em; text-transform: uppercase;
         color: var(--muted); }
h1, h2 { font-family: var(--font-serif); font-weight: 400; }
```

---

## Texture & effects

Four things, in this order of importance: **the photograph**, **the sheet**, **hairlines**, **grain**. There are no other effects. No drop shadows on internal elements, no card elevation, no gradients on buttons.

### 1. The full-bleed photograph

A soft, defocused natural landscape covers the whole viewport, fixed behind the scroll. Muted greens and earth tones, overcast or golden-hour light, horizon high or low but never centred, and a **quiet low-contrast middle** so type can sit on it.

```css
.backdrop { position: fixed; inset: 0; z-index: 0; overflow: hidden; background: var(--bg); }
.backdrop > svg { width: 100%; height: 100%; display: block; }
.page { position: relative; z-index: 1; }
```

When you have no photograph to ship (offline artifact, no asset budget), **build one** from an inline SVG — layered gradients for sky and field, turbulence for foliage, Gaussian blur for the defocus. The skeleton:

```html
<svg viewBox="0 0 1600 1000" preserveAspectRatio="xMidYMid slice" aria-hidden="true">
  <defs>
    <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0"    stop-color="#9FB2B4"/>
      <stop offset=".44"  stop-color="#CBD5CC"/>
      <stop offset=".78"  stop-color="#E7E8DA"/>
      <stop offset="1"    stop-color="#F2EEDF"/>
    </linearGradient>
    <linearGradient id="field" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0"   stop-color="#8B9E6F"/>  <!-- far, hazy -->
      <stop offset=".45" stop-color="#63793F"/>
      <stop offset="1"   stop-color="#3F5326"/>  <!-- near, dark -->
    </linearGradient>
    <!-- organic foliage patches -->
    <filter id="mottle">
      <feTurbulence type="fractalNoise" baseFrequency=".010" numOctaves="5" seed="5"/>
      <feColorMatrix type="matrix"
        values="0 0 0 0 .22  0 0 0 0 .30  0 0 0 0 .13  .55 .35 0 0 -.30"/>
      <feGaussianBlur stdDeviation="2"/>
    </filter>
    <!-- grass, displaced then defocused -->
    <filter id="grass" x="-10%" y="-10%" width="120%" height="120%">
      <feTurbulence type="fractalNoise" baseFrequency=".004 .03" numOctaves="4" seed="11" result="n"/>
      <feDisplacementMap in="SourceGraphic" in2="n" scale="90"
                         xChannelSelector="R" yChannelSelector="G"/>
      <feGaussianBlur stdDeviation="3.5"/>
    </filter>
    <filter id="soft12" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="12"/>
    </filter>
  </defs>

  <rect width="1600" height="1000" fill="url(#sky)"/>
  <!-- ridge lines, blurred, progressively darker and greener toward the viewer -->
  <path d="M0 300 C 240 250, 430 292, 660 268 S 1180 236, 1600 288 L1600 400 0 400Z"
        fill="#B3BFB4" filter="url(#soft12)" opacity=".9"/>
  <rect y="300" width="1600" height="700" fill="url(#field)"/>
  <rect y="300" width="1600" height="700" filter="url(#mottle)" style="mix-blend-mode:multiply"/>
  <!-- out-of-focus foreground blades sell the depth of field -->
  <g filter="url(#soft12)" opacity=".75" fill="#31421F">
    <path d="M60 1000 C 40 900, 96 860, 120 810 L150 1000Z"/>
    <path d="M1480 1000 C 1450 880, 1520 850, 1560 790 L1600 1000Z"/>
  </g>
</svg>
```

Rules that hold whether the photograph is real or synthetic: **slight defocus always**, horizon at ~30% or ~70% of the height, no legible detail in the middle third, no people looking at camera, no urban or industrial subject.

### 2. The sheet

```css
.sheet {
  background: var(--sheet);
  -webkit-backdrop-filter: blur(8px) saturate(1.02);
          backdrop-filter: blur(8px) saturate(1.02);
  border: 1px solid var(--sheet-edge);
  border-radius: 20px;                      /* 16–20px, never more */
  box-shadow:
    0 1px 2px   rgba(28, 34, 30, .04),
    0 24px 60px -30px rgba(28, 34, 30, .28);
  padding: 40px;
}
@supports not (backdrop-filter: blur(8px)) { .sheet { background: rgba(255,255,255,.95); } }
```

That is the **only** shadow in the entire style, and it exists to lift the sheet off the photograph — nothing inside the sheet ever casts one.

### 3. Hairlines instead of cards

Sections inside the sheet are separated by 1px rules, not by boxes:

```css
.rule      { border: 0; border-top: 1px solid var(--line); margin: 32px 0; }
.section   { border-top: 1px solid var(--line); padding-top: 24px; }
.plate     { background: var(--surface); border: 1px solid var(--line);
             border-radius: 4px; padding: 8px; }  /* photo mount — square-ish */
```

### 4. Grain (photograph only)

A single fixed grain layer, clipped to the backdrop, at 5–7% — never over the sheet.

```css
.backdrop::after {
  content: ""; position: absolute; inset: 0; pointer-events: none; opacity: .07;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='160' height='160'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.85' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='160' height='160' filter='url(%23n)'/%3E%3C/svg%3E");
  background-size: 160px 160px;
  mix-blend-mode: multiply;
}
```

---

## Layout & spacing

- **A page, not a screen.** One centred column, `max-width: 720px` for prose sheets, up to `1080px` for a data sheet. The photograph bleeds past it on all four sides — always leave at least 24px of visible photograph around the sheet on desktop, 12px on mobile.
- **8px scale.** Allowed gaps: `4 8 12 16 24 32 40 56 72 96`. Nothing else.
- **Sheet padding** 40px desktop / 32px tablet / 20px mobile. Sheet top margin 56–96px so the photograph reads before the type starts.
- **Radii:** 20px on the sheet, 999px on pills and nav, 4px on photo plates and inputs, 0 on rules, tables and table cells. Square is the default inside the sheet; round is reserved for the sheet itself and for pills.
- **Density is low.** Prose measure 62–68ch, generous 32–40px between sections, one idea per band. If a screen feels crowded, remove a module rather than shrinking the type.
- **Grid attitude:** magazine columns, not dashboard cards. A 12-column grid used asymmetrically — 8/4 for article-plus-margin, 6/6 for a paired comparison, 4/4/4 only for a stat row. Marginal notes (mono, `--muted`) live in the narrow column.
- **Data is a magazine table**, never a card grid: ruled rows, mono, figures right-aligned, header in tracked caps.

---

## Components

### Buttons

```css
.btn { font-family: var(--font-sans); font-size: 14px; font-weight: 500;
       letter-spacing: .01em; padding: 11px 20px; border-radius: 999px;
       border: 1px solid transparent; cursor: pointer; transition: .15s ease; }

.btn--primary { background: var(--accent); color: var(--accent-ink); }
.btn--primary:hover { background: var(--accent-hover); }

.btn--secondary { background: var(--surface); color: var(--ink);
                  border-color: var(--line); }
.btn--secondary:hover { border-color: var(--muted); }

.btn--ghost { background: transparent; color: var(--ink); padding-inline: 12px; }
.btn--ghost:hover { background: var(--ink-wash); }

.btn:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
```

No gradients, no shadows on buttons, no uppercase button labels (caps belong to mono labels only).

### Inputs & selects

Square, hairline, no fill until focus.

```css
.field { font-family: var(--font-sans); font-size: 15px; color: var(--ink);
         background: var(--surface); border: 1px solid var(--line);
         border-radius: 4px; padding: 10px 12px; width: 100%; }
.field::placeholder { color: var(--muted); }
.field:focus { outline: none; border-color: var(--accent);
               box-shadow: 0 0 0 3px var(--accent-wash); }
.field-label { /* .label — mono, tracked caps, 8px above the input */ }
select.field { appearance: none;
  background-image: linear-gradient(45deg, transparent 50%, var(--muted) 50%),
                    linear-gradient(135deg, var(--muted) 50%, transparent 50%);
  background-position: right 16px center, right 11px center;
  background-size: 5px 5px, 5px 5px; background-repeat: no-repeat; }
```

### Nav & sidebar

Top nav is a **floating pill** on the photograph, above the sheet — small, mono-labelled, translucent white.

```css
.nav { display: flex; gap: 4px; align-items: center; padding: 6px;
       background: rgba(255,255,255,.86); backdrop-filter: blur(8px);
       border: 1px solid var(--sheet-edge); border-radius: 999px; }
.nav a { font-size: 13px; color: var(--muted); padding: 8px 14px;
         border-radius: 999px; text-decoration: none; }
.nav a:hover { color: var(--ink); background: var(--ink-wash); }
.nav a[aria-current] { color: var(--ink); background: #FFFFFF; }
```

A sidebar, when a web app needs one, is a **table of contents**: no fill, no icons-in-boxes, mono tracked-caps group headers, items separated by 1px `--line` rules, the active item marked with a 2px `--accent` left border.

### Cards

There are effectively no cards. A "card" is a hairline-topped block inside the sheet:

```css
.block { border-top: 1px solid var(--line); padding: 20px 0 24px; }
.block h3 { font-family: var(--font-serif); font-size: 20px; font-weight: 400; margin: 6px 0 8px; }
.block .label { margin-bottom: 4px; }
```

If a genuinely detached card is unavoidable (a stat tile on the photograph), it uses `--surface`, a 1px `--line` border, 4px radius, and **no shadow**.

### Tables

```css
.table { width: 100%; border-collapse: collapse; font-family: var(--font-mono);
         font-size: 13px; font-variant-numeric: tabular-nums; }
.table th { font-size: 10px; letter-spacing: .14em; text-transform: uppercase;
            color: var(--muted); font-weight: 500; text-align: left;
            padding: 0 0 8px; border-bottom: 1px solid var(--ink); }
.table td { padding: 10px 0; border-bottom: 1px solid var(--line); }
.table td:not(:first-child), .table th:not(:first-child) { text-align: right; }
.table tfoot td { border-bottom: 0; border-top: 1px solid var(--ink); font-weight: 500; }
.table tr:hover td { background: var(--accent-wash); }
```

First column is the label (sans is acceptable there); every numeric column is mono and right-aligned. Rules, never zebra stripes, never vertical borders.

### Chips & badges

```css
.chip { font-family: var(--font-mono); font-size: 10px; letter-spacing: .14em;
        text-transform: uppercase; padding: 5px 10px; border-radius: 999px;
        border: 1px solid var(--line); color: var(--muted); background: transparent; }
.chip--on { background: var(--accent-wash); border-color: transparent; color: var(--accent); }
.chip--solid { background: var(--accent); border-color: transparent; color: var(--accent-ink); }
```

### Modals & drawers

A modal is a **second sheet** on a dimmed photograph — same radius, same border, slightly stronger opacity so nested content stays readable.

```css
.scrim { position: fixed; inset: 0; background: rgba(28,34,30,.32);
         backdrop-filter: blur(2px); }
.modal { max-width: 520px; background: rgba(255,255,255,.96);
         border: 1px solid var(--sheet-edge); border-radius: 20px; padding: 32px;
         box-shadow: 0 30px 80px -40px rgba(28,34,30,.45); }
.modal__head { display: flex; justify-content: space-between; align-items: baseline;
               border-bottom: 1px solid var(--line); padding-bottom: 16px; }
```

Drawers slide from the right, full height, 20px radius on the left corners only.

### Footer

Inside the bottom of the sheet or as a separate low sheet: a 1px `--line` top rule, then mono tracked-caps column headers with sans links beneath, and a final line of mono meta — issue number, date, licence.

```html
<footer class="section">
  <p class="label">Issue 04 · Spring 2026 · Compiled 12 March</p>
</footer>
```

---

## Imagery

**Photography is mandatory and it is the interface.** One landscape image per page, full-bleed, fixed, defocused; the sheet does the rest. Rules:

- Subject: natural land — fields, hills, forest edge, coastline, sky. No cities, no offices, no product shots, no people looking at camera.
- Treatment: muted greens and earth tones, low saturation, overcast or golden hour, slight defocus, faint grain. Never HDR, never high-contrast, never a colour-graded duotone.
- Secondary imagery — supporting photos inside the sheet — is mounted as a **plate**: white `--surface` mount, 1px `--line` border, 4px radius, and a mono caption underneath in `--muted`.
- Charts are drawn like plates, not like widgets: 1px `--line` axes, a single `--accent` series, mono axis labels, no fills unless the fill is `--accent-wash`.
- Icons, if any, are 1.25px stroke, `--ink` or `--muted`, never filled, never in a coloured circle.

---

## Do

1. Let the photograph bleed to all four edges and stay fixed while the sheet scrolls over it.
2. End every headline with a full stop.
3. Set every number, date, ID and code in monospace — including numbers inside running sentences.
4. Use letterspaced ALL-CAPS monospace for labels, eyebrows, table headers and captions.
5. Separate content with 1px `--line` rules; let the sheet be the only container.
6. Keep the middle of the photograph quiet — that is where the type lands.
7. Right-align numeric columns and turn on `tabular-nums`.
8. Keep one accent (`#4E6030`) and spend it sparingly: one primary button, one chart series, one active state.

## Don't

1. Don't stack a card inside the sheet with its own shadow — the sheet's shadow is the only one on the page.
2. Don't use a busy, high-contrast or urban photograph, and never a stock image of people at a desk.
3. Don't set body copy in the serif, and don't bold the serif headline.
4. Don't set figures in the sans — that breaks the three-voice system that defines the style.
5. Don't introduce a second accent colour, a status palette of five hues, or a coloured chart legend.
6. Don't round table corners, add vertical table borders, or zebra-stripe rows.
7. Don't apply grain, blur or gradient to the sheet or to any UI surface — those belong to the photograph alone.
8. Don't let the sheet reach the viewport edges; if it does, the page stops being a page.
9. Don't tighten the measure past 60ch or expand it past 72ch to fit more content in.
10. Don't use uppercase in buttons, headlines or body — capitals belong to mono labels only.
