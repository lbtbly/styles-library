# Grey Room

**Pairing —** Gallery wall × system font
**Concept —** Drain every hue, then let luminance, letter-tracking and one black pill carry the entire hierarchy.

Grey Room is for surfaces that must not compete with what the user puts inside them: design and creative tools, studio and portfolio sites, premium positioning, collaboration products where the only colour on screen is an avatar or an uploaded thumbnail. Every value in the palette is achromatic — if a colour has saturation, it does not belong here. Hierarchy is built from three things and only three: a 3% luminance step between planes, tracked-out ALL-CAPS micro-labels, and one solid black pill button per screen.

Do not reach for it when you need semantic colour (status dashboards, alerting, safety-critical work), a playful consumer voice, or strong brand-colour recall.

---

## Palette

Nine achromatic values, sampled from the source shots. They are fixed — do not re-tint, warm them up, or introduce a hue "just for the accent".

| Token | Hex | Role | Allowed to appear |
|---|---|---|---|
| `--bg` | `#EFEFEF` | Room ground | The page body, canvas behind panels, sidebar ground, gutters |
| `--surface` | `#F8F8F8` | Panel plane | Cards, panels, list rows, inputs, table body, section blocks |
| `--raised` | `#FFFFFF` | Lifted plane | Modals, dropdowns, popovers, the active card in a list, hovered rows, sticky headers |
| `--ink` | `#171717` | Primary text | Display and section headings, body copy, table values, icon strokes, the black pill fill |
| `--muted` | `#767676` | Secondary text | Micro-caps labels, meta, placeholder, inactive nav, the second clause of a two-tone headline, axis ticks |
| `--line` | `#E0E0E0` | Hairline | 1px borders where a luminance step alone would be ambiguous; dividers; input borders; chart gridlines |
| `--accent` | `#000000` | The pill | Primary button fill, active tab underline, selected state, focus ring. Pure black, at most twice per screen. |
| `--accent_ink` | `#FFFFFF` | On-accent text | Text and icons sitting on `--accent` |
| `--tint` | `rgba(23, 23, 23, 0.06)` | Whisper wash | Chip and badge fills, avatar placeholder, progress track, hover on a `--surface` row, code inline |

```css
:root {
  --bg:         #EFEFEF;
  --surface:    #F8F8F8;
  --raised:     #FFFFFF;
  --ink:        #171717;
  --muted:      #767676;
  --line:       #E0E0E0;
  --accent:     #000000;
  --accent-ink: #FFFFFF;
  --tint:       rgba(23, 23, 23, 0.06);
}
```

**The three-plane rule.** `--bg` `#EFEFEF` → `--surface` `#F8F8F8` → `--raised` `#FFFFFF` is a ~3% luminance step at each stage, and **that step is the border**. Reach for `--line` only when two planes of the same value meet, or when a step would be ambiguous at a glance (table rules, input outlines). Never stack more than three planes.

**Zero saturation, no exceptions.** Status is expressed with a word ("Overdue"), a shape (a filled vs hollow dot), or ink weight — never with green, amber or red. If the product genuinely requires semantic colour, this is the wrong style.

---

## Typography

Typography does the work colour normally would, so the family must hold up at 10px as well as 40px. One neo-grotesque, tightly set.

```css
font-family: Inter, "Helvetica Now Display", "Söhne", -apple-system, BlinkMacSystemFont,
             "Segoe UI", "Helvetica Neue", Helvetica, Arial, sans-serif;
```

| Role | Size / line-height | Weight | Tracking | Colour |
|---|---|---|---|---|
| Display | 40 / 44 | 600 | **-0.03em** | `--ink` (+ `--muted` second clause) |
| Display, large hero | 56 / 58 | 600 | -0.035em | `--ink` / `--muted` |
| Section | 22 / 28 | 500 | -0.015em | `--ink` |
| Card title | 15 / 22 | 500 | -0.005em | `--ink` |
| Body | 14 / 21 | 400 | 0 | `--ink` |
| Small / meta | 12 / 18 | 400 | 0 | `--muted` |
| **Micro-caps** | 10 / 12 | 600 | **0.14em** ALL-CAPS | `--muted` |
| Numeral (data) | 28 / 32 | 500, tabular | -0.02em | `--ink` |

**Usage rules**

- **Tracked-out ALL-CAPS micro-labels are the primary wayfinding device.** Every section, column, group, sidebar heading and card kicker gets one: 10px, 600, `0.14em`, `--muted`. They replace the coloured section headers other styles use.
- **Two-tone headlines are the signature move.** The first clause in `--ink`, the second fading to `--muted`, inside one sentence. `<h1>Studio for the <em>quiet end</em> of the brief</h1>` where `em` is `color: var(--muted); font-style: normal`.
- **The gap between display and body is deliberately extreme** — 40px next to 14px, nothing in between except the 22px section size. Do not fill the ladder in.
- Never introduce a coloured word, a highlight, or an underline in a heading.
- Numerals tabular in any table, metric or ledger. Set metrics at 28/32 medium with -0.02em, not bold.
- Sentence case for everything except micro-caps.

---

## Texture & effects

There is almost no texture. The material is *paper planes at slightly different luminance*.

**Plane stepping — the default separation:**

```css
.page   { background: var(--bg); }        /* #EFEFEF */
.panel  { background: var(--surface); border-radius: 12px; }  /* #F8F8F8 — no border needed */
.raised { background: var(--raised); border: 1px solid var(--line); border-radius: 12px; }
```

**Shadow — sparingly, and only this one.** Used on `--raised` planes that genuinely float (modals, dropdowns, dragged cards, a card lifted on hover). Never on a static panel.

```css
.lift      { box-shadow: 0 1px 2px rgb(0 0 0 / .05); }
.floating  { box-shadow: 0 1px 2px rgb(0 0 0 / .05), 0 12px 32px -12px rgb(0 0 0 / .14); }
```

**Hover** is a plane promotion, not a colour change: `--surface` → `--raised`, plus the `.lift` shadow. Rows on `--raised` hover to `--tint`.

**Whisper tint** for chips, tracks and placeholders:

```css
.tint { background: var(--tint); }   /* rgba(23, 23, 23, 0.06) */
```

**Charts and meters** are drawn in ink and greys only. A progress track is `--tint`; its fill is `--ink`. A comparison series is `--muted` (or `--ink` at 30% opacity). Sparklines are 1.5px `--ink` strokes on nothing.

```css
.track { height: 6px; border-radius: 999px; background: var(--tint); }
.track > i { display: block; height: 100%; border-radius: 999px; background: var(--ink); }
.series      { fill: none; stroke: var(--ink);   stroke-width: 1.5; }
.series-prev { fill: none; stroke: var(--muted); stroke-width: 1.5; }
.gridline    { stroke: var(--line); stroke-width: 1; stroke-dasharray: 2 4; }
```

**A greyscale gradient is permitted only as a soft vignette on a large empty field** (a hero ground, an image placeholder). It must stay within the palette and must not read as a colour:

```css
.vignette { background-image: radial-gradient(120% 80% at 50% 0%, #FFFFFF 0%, #EFEFEF 68%); }
```

**Focus ring:**

```css
:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
```

No glow, no glass, no blur, no noise, no coloured shadow, no bevel. If you are reaching for an effect, reach for a luminance step instead.

---

## Layout & spacing

- **Base scale: 8px.** Use 8 / 12 / 16 / 24 / 32 / 48 / 64 / 96.
- **Section padding 24-32px** inside panels; **64-96px** vertical rhythm between marketing sections.
- **Radii:** 12px on panels and cards · 10px on inputs and small buttons · **999px on pills, chips and avatars** · 0 on full-bleed dividers.
- **Container widths:** marketing content 1120px max, with a 640px measure for prose. App content fills, with a 240-280px sidebar.
- **Grid attitude:** either generous and quiet, or dense and quiet — never loud. Marketing pages use a 12-column grid with big empty gutters and asymmetric splits (7/5, 8/4). App screens use a fixed sidebar + fluid content, panels stacked at 16px gaps.
- **Density:** list rows 44-48px, nav rows 36px, buttons 40px (36px compact). Whitespace is the luxury signal — when in doubt add 8px, not a border.
- **The single black pill** is the only high-contrast object on the page. **At most twice per screen**, and never twice in the same visual block.

```css
.shell { display: grid; grid-template-columns: 260px 1fr; min-height: 100vh; background: var(--bg); }
.stack { display: flex; flex-direction: column; gap: 16px; }
.section { padding: 96px 24px; }
```

---

## Components

### Buttons

```css
.btn { height: 40px; padding: 0 20px; border-radius: 999px; font: 500 14px/1 inherit;
       display: inline-flex; align-items: center; gap: 8px; cursor: pointer; }

/* the black pill — max two per screen */
.btn-primary   { background: var(--accent); color: var(--accent-ink); border: 1px solid var(--accent); }
.btn-primary:hover { background: #262626; }

.btn-secondary { background: var(--raised); color: var(--ink); border: 1px solid var(--line); }
.btn-secondary:hover { background: var(--surface); }

.btn-ghost     { background: transparent; color: var(--muted); border: 1px solid transparent; }
.btn-ghost:hover { background: var(--tint); color: var(--ink); }
```

Pills for marketing and primary app actions; 10px-radius rectangles are acceptable for dense toolbars. Destructive actions are a `--secondary` pill whose label reads "Delete permanently" — the weight of the words carries the warning, not a red fill.

### Inputs & selects

```css
.field { height: 40px; padding: 0 14px; background: var(--raised); border: 1px solid var(--line);
         border-radius: 10px; font: 400 14px/1 inherit; color: var(--ink); }
.field::placeholder { color: var(--muted); }
.field:focus { border-color: var(--ink); box-shadow: 0 0 0 3px var(--tint); outline: none; }
.field[disabled] { background: var(--surface); color: var(--muted); }
```

Labels are micro-caps above the field. Selects are the same box with a 12px `--muted` chevron. Search fields sit on `--surface` with no border, gaining `--line` on focus. Checkboxes and radios are 16px, `--line` border, filling solid `--ink` when checked with a white glyph.

### Nav / sidebar

App sidebar on `--surface` with a 1px `--line` right edge. Group headings are micro-caps in `--muted`. Rows are 36px, 10px radius, `--muted` text; hover goes `--tint` + `--ink`; the active row is `--raised` with `--ink` text, 500 weight and the `.lift` shadow — a plane promotion, not a colour.

Marketing nav is a single 64px bar: wordmark left, 14px `--muted` links centre, one black pill right. On scroll it gains a 1px `--line` bottom, never a shadow.

```css
.navrow        { height: 36px; border-radius: 10px; padding: 0 12px; color: var(--muted); }
.navrow:hover  { background: var(--tint); color: var(--ink); }
.navrow.active { background: var(--raised); color: var(--ink); font-weight: 500;
                 box-shadow: 0 1px 2px rgb(0 0 0 / .05); }
```

### Cards

`--surface` on `--bg`, 12px radius, 24px padding, no border and no shadow — the luminance step does it. A card that is selected, hovered or dragged promotes to `--raised` + `.lift`. Card structure: micro-caps kicker, then a 15/22 title, then 14/21 body in `--muted`, then a ghost link. Do not nest cards; use a `--line` divider.

### Tables

```css
.table th { font: 600 10px/12px inherit; letter-spacing: .14em; text-transform: uppercase;
            color: var(--muted); text-align: left; padding: 12px 16px;
            border-bottom: 1px solid var(--line); }
.table td { padding: 14px 16px; border-bottom: 1px solid var(--line); font-size: 14px; }
.table td.num { text-align: right; font-variant-numeric: tabular-nums; }
.table tr:hover td { background: var(--tint); }
```

Header row in micro-caps, hairline rules, 48px rows, numerics right-aligned and tabular. No zebra striping — it introduces a fourth plane.

### Chips & badges

```css
.chip { height: 24px; padding: 0 10px; border-radius: 999px; background: var(--tint);
        color: var(--muted); font: 500 12px/24px inherit; }
.chip-solid { background: var(--accent); color: var(--accent-ink); }   /* counts as one of your two blacks */
.chip-outline { background: transparent; border: 1px solid var(--line); color: var(--muted); }
```

Role and status chips are whisper-tints of ink, never colour. A status dot is 6px: filled `--ink` = active, `--line` = idle, hollow with a 1px `--ink` ring = pending.

### Modals & drawers

`--raised`, 12px radius, 32px padding, `0 1px 2px rgb(0 0 0 / .05), 0 12px 32px -12px rgb(0 0 0 / .14)`, over a `rgba(23, 23, 23, 0.28)` scrim. Title 22/28 medium, body 14/21 in `--muted`, actions bottom-right: a ghost "Cancel" and one black pill. Drawers are the same at 400-480px, pinned right, full height, with a `--line` left edge.

### Footer

Marketing footer on `--surface` with a 1px `--line` top rule and 64px vertical padding. Four columns of links under micro-caps headings; the wordmark and a one-line positioning statement in the first column; a bottom bar with 12/18 `--muted` copyright and legal links. Never a black footer block — the black is spent on the pill.

---

## Imagery

Imagery is welcome but must be **desaturated to zero**. Studio photography, greyscale 3D renders, or plain tinted planes. Treat it as follows:

```css
.media { filter: grayscale(1) contrast(1.02); background: var(--tint); border-radius: 12px; }
```

- Apply `filter: grayscale(1)` to every photograph, without exception. A single colour cast in an image will break the whole page.
- Images sit on `--tint` placeholders at 12px radius, usually 4:3 or 3:2, with generous surrounding whitespace.
- **Avatars are the licensed exception** — in collaboration contexts, user avatars may keep their colour, because they are user content and are the only colour on the screen. Keep them ≤28px and circular.
- Where no photograph exists, use a `--tint` block with a thin `--ink` line-drawing (1.25px strokes) or the greyscale vignette. Never an illustration with a colour.
- Icons: 16-20px, 1.5px strokes, `--muted` default, `--ink` active. Never filled, never coloured.

See `image-recipe.md` for generating in-style photography or renders.

---

## Do

- Keep every value achromatic — `#EFEFEF`, `#F8F8F8`, `#FFFFFF`, `#171717`, `#767676`, `#E0E0E0`, `#000000`.
- Separate planes with the 3% luminance step first; add `#E0E0E0` hairlines only where the step is ambiguous.
- Put a tracked ALL-CAPS 10px micro-label on every section, column and group.
- Write two-tone headlines — first clause `#171717`, second clause `#767676`.
- Spend the black pill deliberately: at most twice per screen, and make it the real primary action.
- Express state with words, weight, or a filled-vs-hollow dot instead of semantic colour.
- Desaturate every photograph with `filter: grayscale(1)`.
- Let whitespace do the premium signalling — 64-96px between marketing sections.

## Don't

- Don't introduce any saturated hue, not even for success, warning or error states.
- Don't put three black pills on one screen, or two side by side — the black stops meaning "primary".
- Don't build hierarchy with size steps you invented; the ladder is 40 → 22 → 14 → 10 and it is meant to be gappy.
- Don't outline everything — a border where a luminance step already separates two planes is noise.
- Don't use drop shadows on static cards, or any shadow heavier than `0 1px 2px rgb(0 0 0 / .05)` outside a floating layer.
- Don't stack a fourth plane (no zebra rows, no `#FAFAFA` invented in-between value).
- Don't use `rgba(23, 23, 23, 0.06)` as a page background — it is a chip, a track and a hover, not a field.
- Don't set headlines in ALL-CAPS; caps belong to the 10px micro-labels only.
- Don't let a coloured logo, chart series, badge or emoji sneak in — avatars are the sole exception.
