# Hairline Ledger

**Pairing:** Trading terminal × Swiss timetable
**Concept:** Rules, not boxes — density earns trust when every divider is 1px and every figure is tabular.

Hairline Ledger is for screens whose primary job is *scanning many rows*: analytics and BI tools, admin consoles, developer and API dashboards, financial and trading interfaces. It buys trust with precision rather than personality — one flat surface colour, 1px rules where other styles would put a card, tabular numerals so decimal points stack, and colour used only where it carries meaning. Reach for it when the user's question is "which row is wrong?" and not "how does this make me feel".

Do **not** use it for consumer onboarding, marketing landing pages, brand-led storytelling, or low-information mobile-first products — it has no display tier and no warmth to offer them.

---

## Palette

Every value is sampled from the source shots. Treat them as fixed; do not nudge them toward your own preference.

| Token | Hex | Role | Where it is allowed to appear |
|---|---|---|---|
| `--bg` | `#F4F5F6` | Page ground | The `<body>` behind everything; row hover tint; input wells; sidebar ground. Never as a card fill on top of `--surface`. |
| `--surface` | `#FFFFFF` | Working surface | Table body, top bar, sidebar panel, drawers, popovers, buttons (secondary). The only "raised" colour. |
| `--ink` | `#0F1419` | Primary text | Headings, body copy, figures, table cells, active nav item. Also the fill of a checked checkbox. |
| `--muted` | `#697079` | Secondary text | Column labels, meta, captions, help text, inactive nav, placeholder, units and suffixes. Never for a figure. |
| `--line` | `#E3E5E8` | Hairline rules | Every 1px divider: row borders, column separators, input borders, sidebar edge, table header underline, chip borders. Never thicker than 1px. |
| `--accent` | `#0B5FD0` | Single interactive hue | Primary button fill, links, focus rings, active-sort indicator, selected-row left rule, active tab underline. One accent, nothing else. |
| `--positive` | `#0A7C4A` | Good delta / healthy state | Up-deltas, "Active"/"Healthy" chips, success dots. Text and dots only, never a full-width fill. |
| `--negative` | `#B42318` | Bad delta / failure state | Down-deltas, "Revoked"/"Failed" chips, destructive button label, error text. |
| `--warning` | `#B54708` | Attention state | "Review"/"Rate-limited"/"Paused" chips, threshold markers, quota bars over 80%. |

**Derived values** — do not invent new hues; derive them:

- Semantic chip fill = the semantic hue at **8% over `--surface`** → `rgb(10 124 74 / .08)`, `rgb(180 35 24 / .08)`, `rgb(181 71 8 / .08)`, `rgb(11 95 208 / .08)`.
- Focus ring = `rgb(11 95 208 / .18)`.
- Row hover = `--bg` on `--surface`. Selected row = `rgb(11 95 208 / .06)` plus a 2px `--accent` left rule.

```css
:root {
  /* palette — verbatim from style.json */
  --bg:        #F4F5F6;
  --surface:   #FFFFFF;
  --ink:       #0F1419;
  --muted:     #697079;
  --line:      #E3E5E8;
  --accent:    #0B5FD0;
  --positive:  #0A7C4A;
  --negative:  #B42318;
  --warning:   #B54708;

  /* derived — all traceable to the nine above */
  --accent-wash:   rgb(11 95 208 / .08);
  --accent-select: rgb(11 95 208 / .06);
  --focus:         rgb(11 95 208 / .18);
  --positive-wash: rgb(10 124 74 / .08);
  --negative-wash: rgb(180 35 24 / .08);
  --warning-wash:  rgb(181 71 8 / .08);

  /* the one shadow in the entire system */
  --shadow-float: 0 1px 2px rgb(15 20 25 / .06);

  /* geometry */
  --r-control: 6px;
  --r-float:   8px;
  --r-cell:    0;
  --sidebar:   216px;
  --cell-pad:  8px 12px;
}
```

---

## Typography

One family. Weight and size carry every distinction — there is no second face, no serif, no mono for prose.

```css
--font: "Inter", "Söhne", -apple-system, BlinkMacSystemFont, "Segoe UI",
        Roboto, "Helvetica Neue", Arial, sans-serif;
--font-num: "Inter", ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
```

`--font-num` is only for *opaque identifiers* — API keys, hashes, IPs, request IDs. Ordinary figures stay in `--font` with `font-variant-numeric: tabular-nums`.

| Role | Size / line-height | Weight | Tracking | Notes |
|---|---|---|---|---|
| Page title | 20 / 28 | 600 | -0.01em | The largest type on the screen. Never exceed 24px. |
| Section header | 13 / 18 | 600 | 0 | Sits on a 1px rule, not inside a card header. |
| Body / table cell | 13 / 18 | 400 | 0 | The workhorse size. |
| Figure (cell, KPI) | 13–15 / 18–20 | 600 | 0 | Always `tabular-nums`, always right-aligned in a column. |
| KPI headline figure | 18 / 24 | 600 | -0.01em | Only in the stat strip; still tabular. |
| Column label | 10 / 12 | 600 | 0.08em | ALL-CAPS. Table headers and micro-labels only. |
| Meta / help | 12 / 16 | 400 | 0 | `--muted`. Timestamps, counts, hints. |
| Chip / badge label | 11 / 14 | 500 | 0 | Sentence case, never uppercase. |
| Mono identifier | 12 / 16 | 400 | 0 | `--font-num`, for keys and IDs only. |

**Usage rules**

- Sentence case for all content. ALL-CAPS is reserved for column headers and micro-labels, and always carries `letter-spacing: 0.08em`.
- Never letterspace body copy.
- Right-align every numeric column, left-align text columns, and keep decimal points lined up — use `font-variant-numeric: tabular-nums` globally on `body` so no figure can escape it.
- Units and suffixes (`%`, `ms`, `USD`, `mo`) go in `--muted` at the same size, so the digits stay the loudest thing in the cell.
- Deltas read `+6.4%` / `−0.9%` with a real minus sign (U+2212) and the semantic colour, never an arrow glyph larger than the text.

---

## Texture & effects

There is effectively no texture, and that is the point. The style's entire material vocabulary is: one flat surface, 1px rules, one shadow.

**1. The only shadow.** Reserved for elements that genuinely float — dropdown menus, popovers, drawers, dialogs. Resting elements get a border instead.

```css
.floating {                       /* menu, popover, drawer, dialog */
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: var(--r-float);
  box-shadow: 0 1px 2px rgb(15 20 25 / .06);
}
```

**2. Rules instead of boxes.** A region is delimited by a rule and a label, never by a rounded container.

```css
.section { border-top: 1px solid var(--line); padding-top: 12px; }
.row     { border-bottom: 1px solid var(--line); }        /* never margin-bottom */
.split   { border-left: 1px solid var(--line); }          /* vertical separators in a stat strip */
```

Use `border-collapse: separate; border-spacing: 0` on tables and put the rule on `td`/`th` `border-bottom` so sticky headers keep their line.

**3. Focus.** Visible, square-ish, accent-tinted — no glow.

```css
:where(button, a, input, select, [tabindex]):focus-visible {
  outline: none;
  box-shadow: 0 0 0 3px var(--focus);
  border-color: var(--accent);
}
```

**4. Micro data-graphics.** Inline SVG only, 1px strokes, no fills heavier than 8%. A cell bar is a 1px-ruled track with a flat fill:

```css
.bar   { height: 4px; background: var(--bg); border-radius: 2px; overflow: hidden; }
.bar > i { display: block; height: 100%; background: var(--accent); }
.bar.is-over > i { background: var(--warning); }
```

Sparklines: `<svg viewBox="0 0 80 20"><polyline fill="none" stroke="#0B5FD0" stroke-width="1" points="…"/></svg>` — 1px, no smoothing flourish, no area gradient.

**5. Explicitly forbidden.** No gradients (`linear-gradient` appears nowhere except a 1px rule substitute), no `backdrop-filter`, no blur, no glow, no bevel, no noise overlay, no border thicker than 1px except the 2px selected-row rule and the 2px active-tab underline.

---

## Layout & spacing

- **Base scale 4px.** Legal steps: 4, 8, 12, 16, 20, 24, 32, 40. Nothing else.
- **Cell padding `8px 12px`** — deliberately starved. Comfortable density adds 4px vertically, never more.
- **Radii:** `6px` on controls (buttons, inputs, chips), `8px` on floating panels, `0` on table cells and rule-bounded sections.
- **Sidebar 216px fixed.** It does not resize; it collapses to a 52px icon rail below 900px and disappears below 720px.
- **Top bar 48px**, page header 20px vertical padding, content gutter 20–24px.
- **Tables run full-bleed** to the container edge with no outer card and no outer border — the header rule and the row rules are the container.
- **Grid attitude:** everything snaps to a baseline. Columns are declared widths, not `auto`; the numeric columns are the ones allowed to be narrow.
- **Density is the aesthetic.** When in doubt, fit two more rows rather than add whitespace. A 40px row is the target; 44px is the maximum.

```css
body { background: var(--bg); color: var(--ink); font: 400 13px/18px var(--font);
       font-variant-numeric: tabular-nums; -webkit-font-smoothing: antialiased; }
.app { display: grid; grid-template-columns: var(--sidebar) 1fr; min-height: 100vh; }
.main { background: var(--surface); border-left: 1px solid var(--line); min-width: 0; }
```

---

## Components

### Buttons

32px tall (28px in a toolbar), 13px/500–600, `6px` radius, 1px borders everywhere.

```css
.btn        { height: 32px; padding: 0 12px; border-radius: var(--r-control);
              font: 600 13px/1 var(--font); display: inline-flex; align-items: center;
              gap: 6px; border: 1px solid transparent; cursor: pointer; }
.btn-primary{ background: var(--accent); color: #FFFFFF; border-color: var(--accent); }
.btn-primary:hover { background: #0A55BB; }              /* accent darkened, not a new hue */
.btn-secondary { background: var(--surface); color: var(--ink); border-color: var(--line); }
.btn-secondary:hover { background: var(--bg); }
.btn-ghost  { background: transparent; color: var(--muted); border-color: transparent; }
.btn-ghost:hover { background: var(--bg); color: var(--ink); }
.btn-danger { background: var(--surface); color: var(--negative); border-color: var(--line); }
```

One primary button per screen region. Toolbars are ghost buttons separated by a 1px vertical rule.

### Inputs & selects

```css
.field { height: 32px; padding: 0 10px; border: 1px solid var(--line);
         border-radius: var(--r-control); background: var(--surface);
         color: var(--ink); font: 400 13px/1 var(--font); }
.field::placeholder { color: var(--muted); }
.field:focus { border-color: var(--accent); box-shadow: 0 0 0 3px var(--focus); outline: none; }
.select { appearance: none; padding-right: 26px; }   /* chevron = inline 8×5 SVG, stroke --muted */
.field-search { padding-left: 28px; background: var(--bg); border-color: transparent; }
```

Labels sit *above* at 10px ALL-CAPS `--muted`, or inline-left in a settings row. Never float a label inside the input. Checkboxes are 14px squares, `1px --line`, checked = `--accent` fill with a white 1px tick.

### Nav / sidebar

```css
.side { width: 216px; background: var(--bg); border-right: 1px solid var(--line);
        padding: 12px 8px; }
.side-group { font: 600 10px/12px var(--font); letter-spacing: .08em;
              text-transform: uppercase; color: var(--muted); padding: 12px 8px 6px; }
.side-item { height: 28px; padding: 0 8px; border-radius: var(--r-control);
             color: var(--muted); display: flex; align-items: center; gap: 8px; }
.side-item:hover { background: var(--surface); color: var(--ink); }
.side-item[aria-current] { background: var(--surface); color: var(--ink); font-weight: 600;
                           box-shadow: inset 2px 0 0 var(--accent); }
```

Counts sit right-aligned in `--muted` tabular figures. No icons larger than 14px; icons are 1.25px-stroke line glyphs.

### Cards → rule-bounded blocks

This style has **no cards**. A "card" is a labelled block bounded by rules:

```html
<section class="block">
  <div class="block-head"><h2>Rate limits</h2><button class="btn btn-ghost">Configure</button></div>
  <!-- rows separated by border-bottom -->
</section>
```
```css
.block      { border-top: 1px solid var(--line); }
.block-head { display: flex; justify-content: space-between; align-items: center;
              padding: 16px 20px 8px; }
.block-head h2 { font: 600 13px/18px var(--font); }
```

A KPI strip is a flex row of stats separated by `border-left: 1px solid var(--line)`, not five boxes.

### Tables

The centrepiece. Full-bleed, sticky header, 1px rules, tabular figures.

```css
table { width: 100%; border-collapse: separate; border-spacing: 0; }
thead th { position: sticky; top: 0; z-index: 2; background: var(--surface);
           font: 600 10px/12px var(--font); letter-spacing: .08em; text-transform: uppercase;
           color: var(--muted); text-align: left; padding: 8px 12px; white-space: nowrap;
           border-bottom: 1px solid var(--line); cursor: pointer; user-select: none; }
thead th.num, tbody td.num { text-align: right; font-variant-numeric: tabular-nums; }
thead th[aria-sort] { color: var(--ink); }              /* caret in --accent, 8×5 SVG */
tbody td { padding: 8px 12px; border-bottom: 1px solid var(--line); vertical-align: middle; }
tbody tr:hover td { background: var(--bg); }
tbody tr[aria-selected="true"] td { background: var(--accent-select); }
tbody tr[aria-selected="true"] td:first-child { box-shadow: inset 2px 0 0 var(--accent); }
```

Rules: header row is 10px ALL-CAPS; every numeric column right-aligned; no zebra striping (rules do that job); no vertical grid lines except where a column group genuinely changes meaning; row height 36–40px; the first column may carry a 20px monogram tile (`1px --line`, 4px radius, 10px `--muted` initials) instead of a logo.

### Chips / badges

```css
.chip { display: inline-flex; align-items: center; gap: 5px; height: 20px; padding: 0 8px;
        border-radius: var(--r-control); font: 500 11px/1 var(--font);
        border: 1px solid var(--line); background: var(--surface); color: var(--muted); }
.chip::before { content: ""; width: 5px; height: 5px; border-radius: 50%; background: currentColor; }
.chip.is-positive { color: var(--positive); background: var(--positive-wash); border-color: transparent; }
.chip.is-negative { color: var(--negative); background: var(--negative-wash); border-color: transparent; }
.chip.is-warning  { color: var(--warning);  background: var(--warning-wash);  border-color: transparent; }
.chip.is-info     { color: var(--accent);   background: var(--accent-wash);   border-color: transparent; }
```

Chips are 20px tall and never uppercase. A neutral chip keeps the hairline border; a semantic chip drops the border and takes the 8% wash.

### Drawers / dialogs / menus

The only floating things, and the only users of the shadow.

```css
.drawer { position: fixed; inset: 0 0 0 auto; width: 480px; background: var(--surface);
          border-left: 1px solid var(--line); box-shadow: var(--shadow-float); }
.menu   { min-width: 180px; padding: 4px; background: var(--surface);
          border: 1px solid var(--line); border-radius: var(--r-float);
          box-shadow: var(--shadow-float); }
.menu-item { height: 28px; padding: 0 8px; border-radius: 4px; display: flex; align-items: center; }
.menu-item:hover { background: var(--bg); }
.menu-sep  { height: 1px; background: var(--line); margin: 4px 0; }
```

A dialog scrim is `rgb(15 20 25 / .28)` — dimmed, never blurred. Drawer header is a 48px row with a title and a 1px bottom rule; drawer footer is a 56px row with a 1px top rule and the action buttons right-aligned.

### Footer / status bar

A 40px status bar pinned under the table, 1px top rule, 12px `--muted` text on the left (row count, refresh time), pagination on the right as ghost buttons with a tabular page indicator.

```css
.statusbar { height: 40px; display: flex; justify-content: space-between; align-items: center;
             padding: 0 20px; border-top: 1px solid var(--line);
             font: 400 12px/16px var(--font); color: var(--muted); }
```

---

## Imagery

**This style uses no photography and no illustration inside the product UI.** The data *is* the imagery.

- Logos and avatars are 20–24px monogram tiles: `1px --line` border, 4px radius, `--muted` 10px semibold initials on `--surface`. Never a coloured avatar circle.
- Charts are 1px-stroke inline SVG: line charts with a 1px `--line` baseline grid, bars as flat `--accent` rectangles, no axis chrome beyond hairlines and 10px `--muted` labels. Fills never exceed 8% opacity.
- Flags, country marks and status glyphs are 1.25px-stroke line icons at 14px, `currentColor`.
- Empty states are a centred 13px line of copy plus one secondary button — no illustration.
- If a marketing surface genuinely needs a hero image, use `image-recipe.md`: flat vector, 1px `#E3E5E8` linework, one blue `#0B5FD0`.

---

## Do

1. Separate every row with a 1px `#E3E5E8` border-bottom, never with a gap, a card, or a shadow.
2. Put `font-variant-numeric: tabular-nums` on `body` so no figure can escape it, and right-align every numeric column.
3. Keep the largest type on the page at 20px — a page title, not a headline.
4. Use ALL-CAPS at 10px/0.08em for column headers and micro-labels, and nowhere else.
5. Let the table run full-bleed to the container edge; the rules are the container.
6. Spend colour only where it means something: `#0B5FD0` for interaction, `#0A7C4A`/`#B42318`/`#B54708` for state.
7. Reserve `0 1px 2px rgb(15 20 25 / .06)` for things that genuinely float — menus, popovers, drawers.
8. Prefer one more visible row over one more pixel of padding.

## Don't

1. Don't wrap the table in a rounded white card on a grey page — that is the exact move this style rejects.
2. Don't use gradients, glass, blur, glow or noise anywhere; there is no `backdrop-filter` in this system.
3. Don't zebra-stripe rows — the hairlines already do the separating, and stripes fight them.
4. Don't introduce a second typeface, a display size, or a serif; monospace is only for keys and IDs.
5. Don't draw a border thicker than 1px, except the 2px accent rule on a selected row or active tab.
6. Don't use coloured avatar circles, emoji, or brand logos — monogram tiles only.
7. Don't add a second accent hue, and don't tint a semantic colour beyond the 8% wash.
8. Don't centre-align numbers, don't letterspace body copy, and don't let a figure sit in `#697079`.
9. Don't animate rows in, bounce a drawer, or ease anything longer than 120ms — motion reads as imprecision here.
