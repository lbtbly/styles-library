# Ember Console

**Pairing —** Control room × safety orange
**Concept —** A single hot orange carries every chart series, CTA and alert across an otherwise white hairline shell.

Ember Console is for commercial operating surfaces: e-commerce and marketplace analytics, order and shipment tracking, performance detail views, operations dashboards — anywhere one metric family (revenue, volume, throughput) dominates and the operator needs to act on it fast. The whole shell is white-on-white separated by hairlines, so the burnt orange is the only saturated thing on screen and reads instantly as "this is the data / this is the action". Its signature composition is the **detail sheet over context**: a modal or side sheet floating over a visibly dimmed but still legible parent screen, so the user never loses their place.

Do not reach for it when you need colour flexibility (white-label), a dark-first tool, an editorial voice, or a calm clinical context where orange reads as alarm.

---

## Palette

Every value below is sampled from the source shots. They are fixed — do not substitute, re-tint or "improve" them.

| Token | Hex | Role | Allowed to appear |
|---|---|---|---|
| `--bg` | `#FCFCFC` | App ground | The page/body behind everything; the dimmed parent screen; sheet ground behind cards |
| `--surface` | `#FFFFFF` | Card & sheet fill | Cards, modals, side sheets, popovers, table header, input fills, top bar |
| `--subtle` | `#F4F5F6` | Recessed fill | Segmented-control track, table zebra, sidebar hover, avatar/thumbnail placeholder, disabled fields |
| `--ink` | `#15171F` | Primary text | Headings, metrics, table values, icon strokes, primary-button fill on secondary layouts |
| `--muted` | `#6B7280` | Secondary text | Labels, axis ticks, meta rows, breadcrumb non-current, placeholder text, inactive nav |
| `--line` | `#E6E8EB` | Hairline | 1px card/sheet borders, table row rules, dividers, input borders, chart gridlines |
| `--accent` | `#D64B00` | The one hot hue | Primary button fill, current chart series, active bars, progress fills, active nav rail item, focus ring, brand mark |
| `--accent_soft` | `#FDEDE3` | Accent wash | Accent chip/badge background, selected row tint, sparkline area fill, chart hover band |
| `--ai` | `#8B5CF6` | AI marker | AI badge text/icon + the lilac→pink gradient strip. Nothing else. |
| `--positive` | `#0A7C4A` | Upward delta | Delta text + arrow only. Never a fill, never a chart series. |
| `--negative` | `#B42318` | Downward delta / destructive | Delta text + arrow, destructive button label, error text. Never a chart series. |
| `--scrim` | `rgba(21, 23, 31, 0.38)` | Dimmer | The overlay between a sheet and its parent screen. One use only. |

```css
:root {
  --bg:          #FCFCFC;
  --surface:     #FFFFFF;
  --subtle:      #F4F5F6;
  --ink:         #15171F;
  --muted:       #6B7280;
  --line:        #E6E8EB;
  --accent:      #D64B00;
  --accent-soft: #FDEDE3;
  --ai:          #8B5CF6;
  --positive:    #0A7C4A;
  --negative:    #B42318;
  --scrim:       rgba(21, 23, 31, 0.38);
}
```

**Colour budget.** Orange is the only saturated hue with a general licence. `--positive` and `--negative` are permitted *only* on delta text and its arrow glyph — they are the sole colours allowed to compete with the orange, and they never fill a shape. `--ai` is permitted only on AI-attributed content. If you find yourself wanting a fifth hue, use weight or `--muted` instead.

---

## Typography

One neo-grotesque family, nothing else. Numerals are **tabular in every metric, table cell and axis tick** — figures must not jitter when they update.

```css
font-family: Inter, "Söhne", -apple-system, BlinkMacSystemFont, "Segoe UI",
             "Helvetica Neue", Arial, sans-serif;
font-feature-settings: "tnum" 1, "cv05" 1;   /* tabular numerals */
font-variant-numeric: tabular-nums;
```

If loading webfonts, Inter is the target; the system stack above is the fallback chain and is close enough to ship with.

| Role | Size / line-height | Weight | Tracking | Colour |
|---|---|---|---|---|
| Page title | 24 / 32 | 600 | -0.01em | `--ink` |
| Sheet / modal title | 20 / 28 | 600 | -0.01em | `--ink` |
| Metric (hero number) | 28 / 34 | 600, tabular | -0.01em | `--ink` |
| Metric (secondary/compare) | 20 / 26 | 500, tabular | 0 | `--muted` |
| Section heading | 16 / 22 | 600 | 0 | `--ink` |
| Card title | 14 / 20 | 600 | 0 | `--ink` |
| Body / table cell | 13 / 18 | 400 | 0 | `--ink` |
| Delta | 12 / 16 | 500, tabular | 0 | `--positive` / `--negative` |
| Label / axis / meta | 11 / 14 | 500 | 0.01em | `--muted` |

**Usage rules**

- **Sentence case everywhere.** "Total revenue", not "Total Revenue" and not "TOTAL REVENUE".
- **Metrics carry the largest optical weight on the screen** — bigger and heavier than any heading near them. A card's title is deliberately smaller than its number.
- **Deltas are 12px medium with a directional arrow glyph** (`↑` / `↓`), coloured `--positive` / `--negative`, followed by an uncoloured comparison phrase: `↑ 1.34%` then `vs last month` in `--muted`.
- Labels above metrics; never a colon. Units ride with the number (`$1,150`, `5m 24s`), never in the label.
- No italics. No letter-spaced caps. No display faces.

---

## Texture & effects

Flat white on flat white, separated by hairlines. There is essentially no depth in this style except where a surface must float above another.

**Hairline separation — the default.** Cards are `--surface` on `--bg`, distinguished by a 1px `--line` border, not a shadow.

```css
.card {
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: 10px;
  padding: 16px;
}
```

**The floating sheet.** Only modals, side sheets and popovers get a shadow, and it is always this one:

```css
.sheet {
  box-shadow: 0 20px 48px -12px rgb(21 23 31 / .24);
  border-radius: 14px;
  background: var(--surface);
}
```

**The scrim — dimmed, never blurred.** The parent screen stays sharp and readable underneath. No `backdrop-filter` anywhere in this style.

```css
.scrim {
  position: fixed; inset: 0;
  background: var(--scrim);          /* rgba(21, 23, 31, 0.38) */
  /* NO backdrop-filter: blur(). The parent must stay legible. */
}
```

**Charts — one hue, two states.** The current series is a solid 2px `--accent` stroke; the comparison series is *the same hue at 35% opacity*. Never a second colour.

```css
.series-current    { stroke: var(--accent); stroke-width: 2; fill: none; }
.series-compare    { stroke: var(--accent); stroke-width: 2; fill: none; opacity: .35; }
.grid              { stroke: var(--line); stroke-width: 1; stroke-dasharray: 3 4; }
.axis-label        { fill: var(--muted); font-size: 11px; }
```

Bars follow the same logic — `--accent` for the highlighted bar, `--accent` at 35% for the rest, or `--accent-soft` for the track behind a progress bar. Area fills, when used at all, are `--accent-soft` under a solid accent stroke.

For a share breakdown (donut, stacked bar) where you genuinely need three or more slices, step the **opacity of the same orange**: `1` / `.55` / `.28`, on an `--accent-soft` ring. Still one hue. Never a categorical palette.

**Sparkline / area fill:**

```css
.spark-area { fill: var(--accent-soft); }   /* #FDEDE3 */
.spark-line { stroke: var(--accent); stroke-width: 2; fill: none; }
```

**The one licensed gradient — AI attribution.** A lilac→pink strip marks AI-generated content. Nothing else in the system may use a gradient, ever.

```css
.ai-strip {
  background-image: linear-gradient(90deg,
    rgb(139 92 246 / .16) 0%,     /* --ai #8B5CF6 */
    rgb(236 72 153 / .14) 55%,
    rgb(255 255 255 / 0) 100%);
  border: 1px solid rgb(139 92 246 / .22);
  border-radius: 10px;
  padding: 12px 14px;
}
.ai-badge {
  color: var(--ai);
  background: var(--surface);
  border: 1px solid rgb(139 92 246 / .28);
  border-radius: 8px;
  font-size: 11px; font-weight: 600;
  padding: 5px 8px;
}
```

**Focus ring** — accent, always visible, never removed:

```css
:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}
```

No noise, no glass, no glow, no inner bevel, no coloured shadow.

---

## Layout & spacing

- **Base scale: 4px.** Use 4 / 8 / 12 / 16 / 20 / 24 / 32 / 40. Nothing off-grid.
- **Sheet padding 20px. Card padding 16px.** Section gap 20-24px inside a sheet, 16px between cards in a grid.
- **Radii:** 10px cards and inputs · 14px sheets and modals · 8px chips, small buttons and badges · 999px avatars and dots only.
- **Container widths:** dashboard content max 1240px; **detail sheet 720-880px** (use 820px as the default); side sheet 480-560px.
- **Grid attitude:** two-column metric grids inside a sheet (`grid-template-columns: 1fr 1fr; gap: 16px`); a chart gets a full-width row of its own and is never squeezed beside a metric list. Dashboards run a 12-column grid with 16px gutters, most cards spanning 3, 4 or 6.
- **Density:** moderate-to-dense. Table rows 44px, nav items 36px, buttons 36px (32px for compact toolbars). Whitespace comes from the 20px sheet padding and the hairline rhythm, not from oversized gaps.
- **Composition:** left icon rail (56-64px, icons only) + optional secondary nav column (220px) + content. Content gets a sticky top bar with breadcrumb on the left and actions on the right.

```css
.shell   { display: grid; grid-template-columns: 60px 220px 1fr; min-height: 100vh; }
.metrics { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; }
.chart-row { grid-column: 1 / -1; }
```

---

## Components

### Buttons

```css
.btn        { height: 36px; padding: 0 14px; border-radius: 8px; font: 500 13px/1 inherit;
              display: inline-flex; align-items: center; gap: 8px; cursor: pointer; }

.btn-primary   { background: var(--accent); color: #FFFFFF; border: 1px solid var(--accent); }
.btn-primary:hover { background: #C24400; }              /* accent, 6% darker */

.btn-secondary { background: var(--surface); color: var(--ink); border: 1px solid var(--line); }
.btn-secondary:hover { background: var(--subtle); }

.btn-ghost     { background: transparent; color: var(--muted); border: 1px solid transparent; }
.btn-ghost:hover { background: var(--subtle); color: var(--ink); }

.btn-danger    { background: var(--surface); color: var(--negative); border: 1px solid var(--line); }
```

One primary (orange) button per view — two at most, and never two side by side. Secondary is white with a hairline. Ghost is for toolbar and icon actions.

### Inputs & selects

```css
.field {
  height: 36px; padding: 0 12px;
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: 10px;
  font: 400 13px/1 inherit; color: var(--ink);
}
.field::placeholder { color: var(--muted); }
.field:focus { border-color: var(--accent); box-shadow: 0 0 0 3px var(--accent-soft); outline: none; }
.field[disabled] { background: var(--subtle); color: var(--muted); }
```

Selects are the same box with a 10px chevron in `--muted` at the right. Search fields carry a leading magnifier icon and may sit on `--subtle` in the top bar. Labels sit above at 11/14 in `--muted`.

### Nav / sidebar

Left icon rail on `--surface` with a 1px `--line` right border. The active item is a 36px rounded square filled `--accent` with a white glyph — this is the only place the rail is coloured. Everything else is `--muted`, going `--ink` on `--subtle` hover. A secondary nav column lists sections as 32px rows; the active row is `--subtle` with `--ink` text and a 2px `--accent` left marker.

```css
.rail-item        { width: 36px; height: 36px; border-radius: 9px; color: var(--muted); }
.rail-item:hover  { background: var(--subtle); color: var(--ink); }
.rail-item.active { background: var(--accent); color: #FFFFFF; }
```

### Cards

`--surface`, 1px `--line`, 10px radius, 16px padding, no shadow. Header row: 14/20 semibold title on the left (optional 14px `--muted` icon), a ghost expand/menu control on the right. Then the metric block, then the chart. Cards do not nest inside cards — use a 1px `--line` divider instead.

### Tables

```css
.table            { width: 100%; border-collapse: collapse; font-size: 13px; }
.table th         { font: 500 11px/14px inherit; letter-spacing: .01em; color: var(--muted);
                    text-align: left; padding: 10px 12px; background: var(--subtle); }
.table td         { padding: 12px; border-top: 1px solid var(--line); color: var(--ink); }
.table td.num     { text-align: right; font-variant-numeric: tabular-nums; }
.table tr:hover td{ background: var(--bg); }
.table tr.sel td  { background: var(--accent-soft); }
```

Header row on `--subtle`, hairline row rules, numeric columns right-aligned and tabular. Row height 44px. Inline mini-bars in a cell are `--accent` on an `--accent-soft` track.

### Chips & badges

```css
.chip        { height: 24px; padding: 0 8px; border-radius: 8px; font: 500 11px/1 inherit;
               border: 1px solid var(--line); background: var(--surface); color: var(--muted); }
.chip-accent { background: var(--accent-soft); border-color: transparent; color: var(--accent); }
.chip-pos    { background: var(--surface); border-color: var(--line); color: var(--positive); }
.chip-neg    { background: var(--surface); border-color: var(--line); color: var(--negative); }
```

Segmented controls (`2wk / 1mo / 3mo`) sit in a `--subtle` track with 6px radius; the selected segment is a white pill with a hairline and a soft `0 1px 2px rgb(21 23 31 / .06)`.

### Modals & drawers — the signature move

820px wide, `--surface`, 14px radius, `0 20px 48px -12px rgb(21 23 31 / .24)`, 20px padding, over a `--scrim`-dimmed parent that stays sharp. Header row: 20/28 semibold title left, ghost close (×) right, 1px `--line` underneath. Body scrolls; a footer with actions is optional and, if present, sits on `--surface` above a 1px `--line`. Side drawers are the same treatment at 480-560px, pinned right, full height.

### Footer

Dashboards get a thin utility footer, not a marketing one: 1px `--line` top rule, 11/14 `--muted` text, left side "Last synced 2 min ago", right side a few ghost links. Height 44px. Never a dark footer block.

---

## Imagery

**Near-zero photography.** The only bitmaps are small product thumbnails and avatars inside data rows — 40px, 8px radius, on a `--subtle` placeholder fill with a 1px `--line`. There are no hero images, no illustrations in the shell, no background art.

Where an illustration is genuinely required (empty states, marketing pages, onboarding), use the `image-recipe.md` prompt: flat vector analytics subject matter, white ground, orange as the only hue. Empty states are better served by a 32px `--muted` line icon, an 14/20 semibold line and a 13/18 `--muted` sentence — no illustration at all.

Icons: 16px or 20px line icons, 1.5px stroke, `--muted` by default, `--ink` when active, `--accent` only when the icon *is* the primary action.

---

## Do

- Keep the shell white-on-white and let 1px `#E6E8EB` hairlines do all the separating.
- Use `#D64B00` for exactly three jobs: the data, the primary action, the active state.
- Draw the comparison series in the *same* orange at 35% opacity — never a second colour.
- Make the metric the biggest, heaviest thing in its card; shrink the title to suit.
- Float detail sheets over a **dimmed but sharp** parent screen so context survives.
- Set every figure in tabular numerals so numbers don't jitter on refresh.
- Reserve `#0A7C4A` and `#B42318` for delta text and its arrow, nothing else.
- Give charts their own full-width row rather than cramming them next to metrics.

## Don't

- Don't add a second brand colour, a blue, a teal or a categorical chart palette — one hue carries everything.
- Don't blur the parent behind a modal; dim it with `rgba(21, 23, 31, 0.38)` and leave it legible.
- Don't use gradients anywhere except the one lilac `#8B5CF6`→pink AI attribution strip.
- Don't fill shapes with `#0A7C4A` or `#B42318` — green and red are text-and-arrow only.
- Don't put drop shadows on cards; they float only when they are a sheet, drawer or popover.
- Don't use ALL-CAPS headings, letter-spaced display type, or any italics.
- Don't stack two orange buttons in the same view — one primary action per screen.
- Don't go dark, glassy or neon; there is no dark mode in this style.
- Don't let `#FDEDE3` become a large background field — it is a chip, a track and an area fill, not a page.
