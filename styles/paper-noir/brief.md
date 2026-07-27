# Paper Noir

**Pairing:** Studio still-life × risograph
**Concept:** Grained off-white pill geometry and solid black circular controls, photographed on a black set.

Paper Noir is for work that wants to look **made, not shipped** — design and creative studios, portfolio and case-study presentation, premium mobile apps, brand-led product launches, boutique and agency positioning. The interface behaves like a printed object: a warm off-white sheet with a real paper tooth, cut into pills and circles, lit by a single soft key and set down on a pure black studio floor.

The force in this style comes from **geometry and contrast, not from type or colour**. The type stays small and quiet; the solid black circular buttons and the fluorescent chartreuse dot do the shouting. Avoid it for dense enterprise dashboards, data-heavy reporting, accessibility-critical services, and high-volume transactional interfaces — the grain, the small type and the black-on-black staging all cost legibility that those products cannot spare.

---

## Palette

Two grounds, and this is the thing to get right: **`--stage` is the black void the artifact floats in; `--bg` is the artifact's own ground.** Every surface inside the UI is warm off-white. Black exists outside the sheet, and inside it only as circular controls and ink.

| Token | Value | Role | Where it is allowed to appear |
|---|---|---|---|
| `--bg` | `#F3F1EA` | The paper. Warm off-white ground of the interface itself. | Page/app background, the sheet, the gaps between cards. Always carries the grain. |
| `--surface` | `#FFFFFF` | Raised card, one step brighter than the paper. | Cards, sheets, list panels, input fills, phone screens. |
| `--stage` | `#080808` | The black set the whole artifact is photographed on. | The area *outside* the sheet — page margins, device-render backdrop, full-bleed section between chapters. Never a card fill. |
| `--ink` | `#141414` | Text and icons. Warm-black, not pure black. | All copy, headings, numerals, icon strokes on light surfaces. |
| `--muted` | `#71706A` | Secondary text. | Labels, captions, metadata, table headers, inactive nav, timestamps. |
| `--line` | `#E2DFD5` | Hairline. The *only* stroke in the style. | 1px dividers inside cards, table row rules, input outlines at rest. Never around a card. |
| `--accent` | `#C9F500` | Fluorescent chartreuse. Signals *now / live / selected*. | Status dots, a 2px underline, one small chip, a progress fill, a single selected pill. **Never larger than a chip.** |
| `--accent-ink` | `#1A2000` | Text on `--accent`. | Only on top of `--accent`. |
| `--control` | `#0D0D0D` | The solid black circular button. The style's signature. | Circular icon buttons (40–48px), the primary CTA pill, the active tab in a bottom bar, the FAB. |
| `--control-ink` | `#FFFFFF` | Text/icons on `--control`. | Only on top of `--control` or `--stage`. |

Contrast notes: `--ink` on `--bg` is ~14:1. `--muted` on `--bg` is ~4.8:1 — fine at 13px and up, do not go below 11px. `--accent` `#C9F500` on `--bg` is roughly 1.4:1 and is **never** a text colour on paper; it only ever appears as a fill carrying `--accent-ink`, or as a shape (dot, bar, underline).

```css
:root {
  --bg:          #F3F1EA;
  --surface:     #FFFFFF;
  --stage:       #080808;
  --ink:         #141414;
  --muted:       #71706A;
  --line:        #E2DFD5;
  --accent:      #C9F500;
  --accent-ink:  #1A2000;
  --control:     #0D0D0D;
  --control-ink: #FFFFFF;
}
```

---

## Typography

One geometric sans in **light and regular only**. Small sizes, generous spacing, sentence case throughout.

```css
--font: "Aeonik", "General Sans", "Poppins", "Inter", -apple-system,
        BlinkMacSystemFont, "Segoe UI", "Helvetica Neue", Arial, sans-serif;
```

Webfont-capable: Aeonik or General Sans. Google fallback: **Poppins 300/400** (closest geometric match) or Inter 300/400. Offline, the system chain lands on SF Pro / Segoe UI / Helvetica.

| Role | Size / line-height | Weight | Tracking | Colour |
|---|---|---|---|---|
| Display (case-study hero only) | 40 / 44 | 300 | -0.02em | `--ink` |
| Numeral / statistic | 32 / 36 | 300 | -0.01em | `--ink` |
| Title | 22 / 28 | 400 | -0.005em | `--ink` |
| Subtitle | 16 / 24 | 400 | 0 | `--ink` |
| Body | 13 / 20 | 400 | 0 | `--ink` |
| Body secondary | 13 / 20 | 400 | 0 | `--muted` |
| Label | 11 / 15 | 400 | 0.02em | `--muted` |
| Micro-caps (sparingly) | 10 / 14 | 400 | 0.08em, uppercase | `--muted` |
| Button / pill | 12 / 12 | 400 | 0.01em | `--ink`, `--control-ink` or `--accent-ink` |

**Usage rules** (from `tokens.type.usage`):

- **Sentence case everywhere.** Uppercase is reserved for 10px micro-caps used as section eyebrows, and even then no more than two per screen.
- **Generous letter-spacing on small labels** — `letter-spacing: .02em` at 11px, `.08em` at 10px caps. Nothing above 16px gets positive tracking.
- **The type never shouts.** A 22px title is the normal maximum inside an app; only a case-study hero earns 40px, and it is set at 300.
- Weight tops out at **400**. If something needs emphasis, make it a pill, a dot, or a black circle — not bold.
- Numerals go light (300) and get `font-variant-numeric: tabular-nums`.
- Body measure caps at ~68 characters.

---

## Texture & effects

### 1. Paper grain — the defining material

Every off-white surface carries a fine tooth. Without it this style is just a white UI. Keep it at **3–5% opacity**, `multiply` blend, and always on a `::before` overlay with `pointer-events: none`.

```css
.grain::before {
  content: ""; position: absolute; inset: 0; pointer-events: none; z-index: 2;
  opacity: .05; mix-blend-mode: multiply; border-radius: inherit;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='180' height='180'%3E%3Cfilter id='p'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='180' height='180' filter='url(%23p)'/%3E%3C/svg%3E");
}
```

Put it on the sheet (the `--bg` container) once, not on every card — one layer of tooth reads as paper, twenty layers read as noise.

### 2. Solid black circular controls

40–48px, perfectly circular, `--control` fill, white icon at 1.5px stroke. These are the punctuation of the layout. Use 1–3 per screen, and place them where the eye should land.

```css
.circ {
  width: 44px; height: 44px; border-radius: 999px; border: 0;
  background: var(--control); color: var(--control-ink);
  display: grid; place-items: center; cursor: pointer;
  transition: transform .18s;
}
.circ:hover { transform: scale(1.06); }
.circ--sm { width: 36px; height: 36px; }
.circ--lg { width: 56px; height: 56px; }
```

### 3. The black set

The whole artifact is presented as an object photographed on a black seamless — a laptop screen, a phone, or a printed sheet lying on the floor.

```css
body { background: var(--stage); }
.set  { padding: clamp(14px, 5vw, 72px);
        background:
          radial-gradient(120% 80% at 50% -10%, #1A1A1A 0%, #0C0C0C 45%, #050505 100%); }
.sheet{ background: var(--bg); border-radius: clamp(16px, 2.2vw, 28px);
        box-shadow: 0 60px 90px -50px rgb(0 0 0 / .9), 0 2px 6px rgb(0 0 0 / .5);
        position: relative; overflow: hidden; }
```

A soft top-light falloff across the set sells the photograph. Never light the set evenly.

### 4. Pill geometry

`border-radius: 999px` is the default, not the exception. Inputs, chips, buttons, tabs, avatars, search fields, segmented controls, progress tracks — all fully rounded. Cards get 20–24px. Nothing in this style has a 4px or 8px corner.

### 5. Colour restraint

`--accent` appears at chip scale or smaller. The legal uses are: a 7px status dot, a chip, a 2–3px progress or underline bar, a single selected pill, one small highlight square in a chart. A chartreuse hero section is not Paper Noir — it is a different style wearing its clothes.

### 6. Shadows

Cards fan and overlap rather than sitting in a strict grid, so they need a shadow to separate. Keep them soft and short-throw on light surfaces, deep and long under the whole object.

```css
--shadow-card:   0 12px 28px -18px rgb(20 20 20 / .28);
--shadow-fan:    0 20px 40px -24px rgb(20 20 20 / .34);   /* the overlapping card */
--shadow-object: 0 60px 90px -50px rgb(0 0 0 / .9);       /* the sheet on the black set */
```

---

## Layout & spacing

- **Scale:** 8px. Legal steps: 4, 8, 12, 16, 20, 24, 32, 40, 56, 72.
- **Card padding:** 20px, 24px for a hero card, 16px for compact list rows.
- **Radii:** `999px` on inputs, chips, buttons, tabs, avatars; `20–24px` on cards; `28px` on the sheet; `16px` on media wells.
- **Overlap and fan.** Cards do not sit in a strict grid — one card overlaps the one behind it by 16–24px, or is rotated 1.5–3°, or breaks the column edge. Two or three fanned elements per screen; the rest align normally, or it reads as a mistake instead of a composition.
- **Container:** 1120px for case-study pages, 390×844 for phone frames, 32px page gutters shrinking to 16px under 640px.
- **Density:** moderate. Rows are 56–64px tall, not 36px.
- **Vertical rhythm:** case-study sections 80–120px apart; app sections 24–32px apart.
- **Dividers before boxes.** When separating list items, use a 1px `--line` rule, not a card border.

---

## Components

### Buttons

```css
.btn { font: 400 12px/1 var(--font); letter-spacing: .01em; padding: 14px 22px;
       border: 0; border-radius: 999px; cursor: pointer; display: inline-flex;
       align-items: center; gap: 8px; transition: transform .18s, background .18s; }
.btn-primary   { background: var(--control); color: var(--control-ink); }
.btn-primary:hover { transform: translateY(-1px); }
.btn-secondary { background: var(--surface); color: var(--ink);
                 box-shadow: inset 0 0 0 1px var(--line); }
.btn-ghost     { background: transparent; color: var(--muted); padding-inline: 12px; }
.btn-ghost:hover { color: var(--ink); }
.btn-accent    { background: var(--accent); color: var(--accent-ink); }  /* max once per screen */
```

The primary action is black. Chartreuse is for *state*, not for *action* — use `.btn-accent` only when the button itself is the live thing (e.g. "Recording").

### Inputs & selects

Pill fields with a hairline at rest, black hairline on focus.

```css
.field { background: var(--surface); border: 1px solid var(--line); border-radius: 999px;
         padding: 14px 20px; font: 400 13px/1.4 var(--font); color: var(--ink); width: 100%; }
.field::placeholder { color: var(--muted); }
.field:focus { outline: 0; border-color: var(--ink); }
.field-wrap { position: relative; }
.field-wrap .circ--sm { position: absolute; right: 5px; top: 50%; transform: translateY(-50%); }
.select { appearance: none; padding-right: 44px;
          background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='11' height='7'%3E%3Cpath d='M1 1l4.5 4.5L10 1' fill='none' stroke='%2371706A' stroke-width='1.3'/%3E%3C/svg%3E");
          background-repeat: no-repeat; background-position: right 20px center; }
```

A search field with a black circular submit button tucked inside its right edge is the house pattern.

### Nav / sidebar

Desktop: a row of **pill tabs** floating at the top of the sheet, the active one filled `--control`. No underline indicator, no full-width bar.

```css
.tabs { display: flex; gap: 6px; flex-wrap: wrap; }
.tabs a { font: 400 12px/1 var(--font); letter-spacing: .01em; padding: 11px 18px;
          border-radius: 999px; color: var(--ink); text-decoration: none;
          background: var(--surface); box-shadow: inset 0 0 0 1px var(--line); }
.tabs a[aria-current] { background: var(--control); color: var(--control-ink); box-shadow: none; }
```

Mobile: a floating pill bottom bar on `--surface` with 4–5 icons and one raised black circle in the centre.

### Cards

```css
.card { background: var(--surface); border-radius: 22px; padding: 20px;
        box-shadow: 0 12px 28px -18px rgb(20 20 20 / .28); }
.card--paper { background: var(--bg); }                 /* recedes into the sheet */
.card--fan   { transform: rotate(-1.8deg); margin-bottom: -18px; z-index: 2;
               box-shadow: 0 20px 40px -24px rgb(20 20 20 / .34); }
```

Cards carry no border. Separation comes from the fill step (`--bg` → `--surface`) plus the soft shadow.

### Tables

Hairline rules only, no fills, no zebra. Row height 56px.

```css
.table { width: 100%; border-collapse: collapse; font-size: 13px; }
.table th { font: 400 11px/15px var(--font); letter-spacing: .02em; color: var(--muted);
            text-align: left; padding: 0 0 12px; }
.table td { padding: 18px 0; border-top: 1px solid var(--line); line-height: 20px; }
.table tr:hover td { background: rgb(20 20 20 / .02); }
.table td:last-child { text-align: right; }
```

### Chips & badges

```css
.chip     { font: 400 11px/1 var(--font); letter-spacing: .02em; padding: 9px 14px;
            border-radius: 999px; background: var(--surface); color: var(--muted);
            box-shadow: inset 0 0 0 1px var(--line); display: inline-flex;
            align-items: center; gap: 7px; }
.chip--on { background: var(--accent); color: var(--accent-ink); box-shadow: none; }
.chip--ink{ background: var(--control); color: var(--control-ink); box-shadow: none; }
.dot      { width: 7px; height: 7px; border-radius: 999px; background: var(--accent); flex: none; }
```

### Modals & sheets

A bottom sheet on mobile, a centred card on desktop: `--surface`, 28px radius, 24px padding, a 36px `--line` grab handle at the top, and a black circular close button in the top-right corner. Scrim is `rgb(8 8 8 / .55)` — the black set bleeding through — with no blur.

```css
.scrim { position: fixed; inset: 0; background: rgb(8 8 8 / .55); }
.sheet-modal { background: var(--surface); border-radius: 28px; padding: 24px;
               box-shadow: 0 40px 80px -40px rgb(0 0 0 / .8); }
.grab { width: 36px; height: 4px; border-radius: 999px; background: var(--line);
        margin: 0 auto 18px; }
```

### Footer

On a case-study page the footer is where the black set is allowed *inside* the composition: a full-bleed `--stage` block at the bottom of the sheet with `--control-ink` type, one chartreuse dot, and a large light wordmark. Keep the links at 13px and the legal line at 11px `--muted`-on-black (use `rgb(255 255 255 / .5)` there, since `--muted` is tuned for paper).

---

## Imagery

Paper Noir uses imagery, and it is always **studio still-life on a black set**: one object, one soft key light from above, deep falloff, warm off-white surfaces, a single chartreuse detail.

- **Treatment:** 16–20px radius well, no border, and the same grain overlay across the top so the photo and the paper share a texture. Optional `filter: grayscale(1) contrast(1.06)` if the source image has stray colour — this style tolerates monochrome photography but not competing hues.
- **Placement:** images fan and overlap like prints on a table. A portrait crop that overlaps a card edge is very much in style.
- **Illustration:** none. No spot illustration, no 3D characters, no gradient meshes.
- **Icons:** 1.5px stroke, rounded caps, 18–20px box. White on black circles; `--ink` on paper.
- **Charts:** thin bars with 999px caps, `--line` for the rest state and `--accent` for the one bar being talked about. No gridlines, no legend boxes — label directly.
- Generate hero imagery with `image-recipe.md`, or build the object out of layered radial gradients on a `--stage` block.

---

## Do

1. Put the grain on. 3–5%, multiply, on the sheet — it is the whole material story.
2. Set the artifact on the black `--stage` and give it a long soft shadow.
3. Use `border-radius: 999px` for every input, chip, tab, avatar and button.
4. Make the primary action a solid black circle or black pill.
5. Keep type small — 22px titles, 13px body — and never above weight 400.
6. Let one or two cards overlap or rotate 1.5–3° so the layout reads as objects on a table.
7. Use `--accent` `#C9F500` at chip scale only: dots, one pill, a 3px bar.
8. Separate list rows with a 1px `--line` rule instead of boxing them.

## Don't

1. Don't fill anything larger than a chip with `#C9F500`. No chartreuse hero, no chartreuse card.
2. Don't set `--accent` as text on paper — 1.4:1 contrast; it only ever carries `--accent-ink`.
3. Don't use bold. Emphasis is geometry (black circle, filled pill), never weight.
4. Don't put borders around cards — the fill step plus a soft shadow is the separation.
5. Don't make `--stage` a card colour. Black is the set and the controls, not a panel.
6. Don't use square or 8px corners anywhere — it reads as a different design system immediately.
7. Don't stack the grain overlay on every element; one layer per sheet.
8. Don't add a second accent hue. There is no red/green/amber status system here — status is a chartreuse dot or nothing.
9. Don't shout with type. If a headline needs to be 64px, this is not the style.
10. Don't grid everything perfectly. A page with zero overlap loses the still-life quality that makes it Paper Noir.

---

*Derived from shots by RonDesignLab ⭐️ — AI Car Inspection SaaS Dashboard, RecruitTrack, RentEase Mobile App, Aella Credit Dashboard, AirFreight SaaS. Previews in `previews/` are original work in the style, not reproductions.*
