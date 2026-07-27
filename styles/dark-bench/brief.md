# Dark Bench

**Pairing:** Node graph × macro lens
**Concept:** Matte graphite tools on an infinite dotted canvas — one node in focus, the rest racked away.

Dark Bench is the workbench look for products whose central object is a **graph**: workflow
and automation builders, agent and pipeline tooling, ETL and data engineering consoles,
developer infrastructure. It is the dark style with **no glow** — nothing bloom, nothing
neon, nothing glassy. Everything is matte graphite on near-black, and the single saturated
green exists to say *this wire carries data* and almost nothing else.

Use it when the user's mental model is "boxes I wire together" or "machines I watch". Avoid
it for marketing pages, editorial content, consumer mobile, or form-heavy admin software —
the canvas metaphor has nothing to hold onto there and the palette reads as gloom.

---

## Palette

| Token | Hex / value | Role | Where it may appear |
|---|---|---|---|
| `bg` | `#0B0B0B` | Canvas ground | The infinite canvas, page background, minimap ground. Never on a card. |
| `surface` | `#1C1C1C` | Node & panel fill | Node cards, side panels, toolbars, table rows, modal bodies. The default box. |
| `raised` | `#262626` | One step up | Hover states, input fields, secondary buttons, chips, node headers, sticky table headers. |
| `ink` | `#FAFAFA` | Primary text | Node titles, headings, values, active nav. Never a fill. |
| `muted` | `#8C8C8C` | Secondary text + idle wires | Labels, body copy inside nodes, port names, timestamps, **and the default connector colour**. |
| `line` | `#333333` | Hairlines | 1px borders on every card and input, table rules, dividers, minimap frame. Never text. |
| `accent` | `#3FBF52` | Live signal | Active connectors, running-state dots, primary button fill, sparkline for healthy series, focus ring. Strictly rationed. |
| `accent_ink` | `#052A0C` | Text on accent | Label colour *on top of* an `#3FBF52` fill. Nowhere else. |
| `dot` | `rgba(255, 255, 255, 0.10)` | Canvas grid | The 24px dot lattice only. |
| `warn` | `#E0A32E` | Degraded | Warning chips, "queued"/"degraded" status dots, threshold lines. |
| `negative` | `#E0503F` | Failed | Error chips, failed node borders, error wires, delete affordances. |

Accent discipline is the whole style. On a full-screen canvas expect roughly **one accent
element per 8 neutral ones**. If two nodes are both "running", that is already the accent
budget spent.

```css
:root {
  --bg:         #0B0B0B;
  --surface:    #1C1C1C;
  --raised:     #262626;
  --ink:        #FAFAFA;
  --muted:      #8C8C8C;
  --line:       #333333;
  --accent:     #3FBF52;
  --accent-ink: #052A0C;
  --dot:        rgba(255, 255, 255, 0.10);
  --warn:       #E0A32E;
  --negative:   #E0503F;
}
```

---

## Typography

Everything is **small**. The canvas is the subject; type is instrumentation. A node title at
13px is correct — resist scaling it up.

```css
--font-sans: "Inter", "General Sans", -apple-system, BlinkMacSystemFont,
             "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
--font-mono: "JetBrains Mono", ui-monospace, SFMono-Regular, "SF Mono",
             Menlo, Consolas, "Liberation Mono", monospace;
```

| Role | Size / line-height | Weight | Family | Colour |
|---|---|---|---|---|
| Canvas / page heading | 20px / 26px | 500 | sans | `--ink` |
| Section heading | 15px / 20px | 500 | sans | `--ink` |
| Node title | 13px / 18px | 500 | sans | `--ink` |
| Body, node body | 12px / 16px | 400 | sans | `--muted` |
| Control & button label | 12px / 16px | 500 | sans | `--ink` |
| Port label, metadata | 10px / 13px | 400 | mono | `--muted` |
| Metric figure | 26px / 30px | 500 | sans, `font-variant-numeric: tabular-nums` | `--ink` |
| Chip / badge | 10px / 12px | 500 | sans, `letter-spacing: .04em` | contextual |

**Usage rules**

- Sentence case everywhere. No ALL-CAPS headlines; small caps only inside 10px chips, and
  even then prefer sentence case with letter-spacing.
- **Monospace for any machine-facing string** — node ids, port names, cron expressions,
  payload keys, durations, versions, hashes, HTTP status codes.
- Truncate aggressively inside nodes (`text-overflow: ellipsis`). A node is a summary, not
  a document. Two lines maximum in a node body.
- Numbers use tabular figures so columns of latency and throughput stay aligned.
- Letter-spacing stays at 0 for sans; only chips and mono labels get `.02–.04em`.

---

## Texture & effects

Matte and flat. **There is no glow in this style.** If you find yourself typing
`box-shadow: 0 0 20px var(--accent)` you have left Dark Bench.

**The dotted canvas** — the ground for every canvas-type surface:

```css
.canvas {
  background-color: var(--bg);
  background-image: radial-gradient(var(--dot) 1px, transparent 1px);
  background-size: 24px 24px;
  background-position: -1px -1px;
}
```

**Cards** — solid fill, 1px line, one tight shadow. Nothing softer, nothing wider:

```css
.card {
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: 10px;
  box-shadow: 0 2px 8px rgb(0 0 0 / .5);
}
```

**Selected node** — accent border plus a 1px ring; still no blur:

```css
.node.is-selected {
  border-color: var(--accent);
  box-shadow: 0 0 0 1px var(--accent), 0 2px 8px rgb(0 0 0 / .5);
}
```

**Bezier wires** — 2px curves in `--muted`, promoted to `--accent` when the edge is live.
Draw them in an inline SVG layer sitting under the nodes:

```html
<svg class="wires" viewBox="0 0 1200 600" preserveAspectRatio="none">
  <defs>
    <marker id="head" markerWidth="7" markerHeight="7" refX="6" refY="3.5" orient="auto">
      <path d="M0,0 L7,3.5 L0,7 Z" fill="currentColor"/>
    </marker>
  </defs>
  <path d="M 300 180 C 380 180, 400 300, 480 300"
        stroke="var(--muted)" stroke-width="2" fill="none" marker-end="url(#head)"/>
  <path d="M 300 180 C 380 180, 400 300, 480 300"
        stroke="var(--accent)" stroke-width="2" fill="none" marker-end="url(#head)"
        class="wire--live"/>
</svg>
```

Control points sit on the **horizontal** axis out of each port (`C x1+Δ,y1 x2−Δ,y2`) so
wires leave and enter flat — that is what makes it read as a node editor rather than a
mind map. Terminate with the solid triangular arrowhead above, or an 8px port dot.

**Port dots** — the small solid circles where wires attach:

```css
.port { width: 8px; height: 8px; border-radius: 50%;
        background: var(--raised); border: 1px solid var(--line); }
.port.is-connected { background: var(--accent); border-color: var(--accent); }
```

**Racked focus (the signature presentation trick).** In a hero or gallery shot, keep one
node crisp and push everything else out of focus. In CSS this is a blur plus a slight
opacity drop on a wrapper, optionally with a whole-canvas tilt:

```css
.stage      { transform: perspective(1400px) rotateX(4deg) rotateZ(-1.5deg); }
.rack       { filter: blur(3px); opacity: .55; }
.rack--far  { filter: blur(7px); opacity: .35; }
.in-focus   { filter: none; opacity: 1; }
```

Use it for one hero region only — never blur working UI the user must read.

**Optional grain** — 3% at most, to kill banding on the near-black ground:

```css
.grain::after {
  content: ""; position: absolute; inset: 0; pointer-events: none; opacity: .03;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='120' height='120'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='3'/%3E%3C/filter%3E%3Crect width='120' height='120' filter='url(%23n)'/%3E%3C/svg%3E");
}
```

Forbidden textures: gradients on fills (a flat `--surface` only), glassmorphism,
`backdrop-filter`, coloured shadows, glow, bloom, inner light, bevels, iridescence.

---

## Layout & spacing

- **Base scale 4px** inside nodes and controls; **8px** between canvas furniture.
- **Node padding 12px**; card/panel padding 16px; page gutters 20–24px.
- **Radii:** 10px on nodes and cards, 8px on inputs and small buttons, 6px on chips,
  999px on floating toolbar pills and status dots.
- **Node width 240–320px.** Narrower and the truncation gets silly; wider and it stops
  reading as a node.
- **Composition is a canvas, not a page.** Nodes are placed freely (absolute positioning
  on a dotted plane), wired together, and chrome *docks over* the canvas: a floating
  toolbar pill top-centre or bottom-centre, a minimap bottom-right, an inspector panel
  flush to the right edge, a thin icon rail on the left.
- **Dashboards** (the non-canvas archetype) keep the dotted ground but use a 12-column
  grid with 16px gutters and dense 8–12px cell padding. Density is high: this style
  expects a lot of small facts per screen, not generous whitespace.
- Max container width 1440px; the canvas itself is unbounded and may bleed.
- Narrow viewports: collapse to a single column, keep the dot grid, shrink the toolbar pill
  to icons only, and let the minimap drop out entirely.

---

## Components

### Buttons

```css
.btn { font: 500 12px/16px var(--font-sans); padding: 8px 14px; border-radius: 8px;
       border: 1px solid transparent; cursor: pointer; }

.btn--primary   { background: var(--accent); color: var(--accent-ink); }
.btn--primary:hover { filter: brightness(1.08); }

.btn--secondary { background: var(--raised); color: var(--ink); border-color: var(--line); }
.btn--secondary:hover { background: #2E2E2E; }

.btn--ghost     { background: transparent; color: var(--muted); }
.btn--ghost:hover { color: var(--ink); background: var(--raised); }

.btn--danger    { background: transparent; color: var(--negative); border-color: var(--negative); }

.btn:focus-visible { outline: none; box-shadow: 0 0 0 2px var(--bg), 0 0 0 3px var(--accent); }
```

There is at most **one** primary button per screen. Everything else is secondary or ghost.

### Inputs & selects

```css
.input, .select {
  background: var(--raised); color: var(--ink); border: 1px solid var(--line);
  border-radius: 8px; padding: 8px 10px; font: 400 12px/16px var(--font-sans); width: 100%;
}
.input::placeholder { color: var(--muted); }
.input:focus, .select:focus { outline: none; border-color: var(--accent); }
.input--mono { font-family: var(--font-mono); }
```

Labels sit **above** the field at 10px mono in `--muted`. Selects use a chevron drawn as a
CSS border-triangle or inline SVG — never a system dropdown arrow on a coloured plate.

### Nav / sidebar / toolbar

- **Left rail:** 56px wide, `--surface`, 1px `--line` on the right edge, 20px icon glyphs
  in `--muted`. Active item: `--ink` icon on a `--raised` 8px square, plus a 2px `--accent`
  bar flush to the left edge.
- **Top bar:** 52px, `--bg` with a bottom `--line`, breadcrumb in 12px `--muted` with the
  current crumb in `--ink`, actions right-aligned.
- **Floating toolbar:** a pill docked over the canvas —
  `position:absolute; background: var(--surface); border:1px solid var(--line); border-radius:999px; padding:6px; box-shadow: 0 2px 8px rgb(0 0 0 / .5);`
  containing 32px icon buttons separated by 1px `--line` dividers.

### Cards & nodes

A node is a card with a header strip, a body, and ports:

```html
<article class="node">
  <header class="node__head">
    <span class="node__dot"></span>
    <h3 class="node__title">Enrich contact</h3>
    <span class="node__kind">http</span>
  </header>
  <div class="node__body">
    <p class="node__line">POST /v2/contacts/enrich</p>
    <p class="node__meta">retry 3 · timeout 30s</p>
  </div>
  <span class="port port--in"></span><span class="port port--out is-connected"></span>
</article>
```

`.node__head` is `--raised` with a bottom `--line`; `.node__kind` is a 10px mono chip;
`.node__dot` is an 8px status dot (`--accent` running, `--warn` queued, `--negative` failed,
`--muted` idle).

### Tables

```css
.table { width: 100%; border-collapse: collapse; font: 400 12px/16px var(--font-sans); }
.table th { text-align: left; font: 500 10px/13px var(--font-mono); color: var(--muted);
            padding: 8px 12px; border-bottom: 1px solid var(--line); }
.table td { padding: 10px 12px; border-bottom: 1px solid var(--line); color: var(--ink); }
.table tr:hover td { background: var(--raised); }
.table td.num { font-family: var(--font-mono); font-variant-numeric: tabular-nums;
                text-align: right; }
```

No zebra striping — hairlines do the work. Numeric columns are mono and right-aligned.

### Chips & badges

```css
.chip { display:inline-flex; align-items:center; gap:5px; padding:3px 8px; border-radius:6px;
        font:500 10px/12px var(--font-sans); letter-spacing:.04em;
        background: var(--raised); color: var(--muted); border:1px solid var(--line); }
.chip--ok   { color: var(--accent);   border-color: color-mix(in srgb, var(--accent) 40%, var(--line)); }
.chip--warn { color: var(--warn);     border-color: color-mix(in srgb, var(--warn) 40%, var(--line)); }
.chip--bad  { color: var(--negative); border-color: color-mix(in srgb, var(--negative) 40%, var(--line)); }
```

Status chips are **outlined and tinted**, never a saturated filled pill — the filled accent
is reserved for the primary button and live wires.

### Modals & drawers

Prefer a **right-edge inspector drawer** (360–420px, `--surface`, 1px `--line` on the left,
no radius, full height) over a centred modal — it matches the canvas metaphor. When a true
modal is needed: 10px radius, `--surface`, 1px `--line`, `box-shadow: 0 8px 32px rgb(0 0 0 / .7)`,
scrim `rgb(0 0 0 / .6)` with **no** backdrop blur.

### Footer

Dashboards and canvases end in a 32px status strip rather than a marketing footer:
`--bg`, top 1px `--line`, 10px mono `--muted`, holding build version, region, last-sync
timestamp, and a single accent dot for connection health, spaced with `justify-content: space-between`.

---

## Imagery

**This style is essentially imageless.** There is no photography, no illustration, no
3D render inside the UI. The visual interest comes from the dot grid, the wires, and the
node arrangement itself.

What stands in for imagery:

- **The graph** — the wired node arrangement is the hero visual. Compose it deliberately.
- **Data marks** — 1px `--line` sparklines and 2px `--accent` series lines, drawn as inline
  SVG polylines with no fills or gradients; bar charts are flat `--raised` rectangles with
  the current bar in `--accent`.
- **Icons** — 16–20px monoline strokes, `stroke-width: 1.5`, `--muted` idle and `--ink`
  active. Never filled, never multicolour, never rounded-cartoon.
- **Avatars** — 24px circles, `--raised` fill with 10px mono initials in `--muted`.
- **Hero shots only:** if a marketing surface genuinely needs a picture, generate it with
  `image-recipe.md` — a macro photograph of a dark tilted screen with shallow depth of
  field — and never place UI text over the in-focus region.

---

## Do

- Keep the dot grid visible on every canvas surface at 24px — it is the style's signature.
- Ration the green: live wires, running status, one primary button. Count your accents.
- Draw connectors as 2px beziers with horizontal control points and solid triangular heads.
- Keep every type size small; a 13px node title is the intended maximum inside a node.
- Use monospace for every machine-facing string — ids, ports, cron, durations, payloads.
- Separate surfaces with 1px `#333333` hairlines instead of shadows or spacing.
- Dock chrome over the canvas as floating pills and edge panels, not as a page header.
- Let density be high — many small true facts beats a few large ones.
- Truncate inside nodes and move the detail to the inspector drawer.

## Don't

- Don't add glow, bloom, neon edges or coloured shadows — this is the matte dark style.
- Don't use `backdrop-filter` or translucent glass panels; surfaces are opaque `#1C1C1C`.
- Don't gradient-fill a node, a button, or a chart area. Flat fills only.
- Don't introduce a second saturated hue; `#E0A32E` and `#E0503F` are status semantics,
  not palette colours to decorate with.
- Don't set headlines above 20px or use bold weights above 500.
- Don't round corners past 10px on cards (999px is only for toolbar pills and dots).
- Don't blur working UI — racked focus is a presentation device for hero shots only.
- Don't use photography, illustration, or 3D renders inside the product UI.
- Don't centre content in generous whitespace; this style is a bench, not a gallery.
