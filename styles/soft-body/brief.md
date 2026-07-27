# Soft Body

**Pairing:** Moulded plastic × pastel stationery
**Concept:** Large radii, soft shadows and barely-saturated pastels make dense data feel handled, not audited.

Soft Body is an application style, not a marketing style. It exists so that a
person who does not enjoy numbers can open a screen full of numbers and not
flinch. Everything is moulded: nothing has a hard edge, nothing is separated by a
heavy rule, and depth comes from soft shadow rather than from borders. Use it for
consumer and prosumer dashboards, freelancer and small-business tools, HR,
scheduling and booking, habit and health tracking — anywhere the user is not a
professional analyst. Avoid it for high-density trading or analytics screens,
developer tooling, enterprise admin with hundreds of rows, or any brand that
needs to sound severe: the whole style trades density for calm, and where a
hairline table fits 24 rows this fits 8. **That is the trade and the point.**

---

## Palette

| Token | Value | Role | Allowed to appear |
|---|---|---|---|
| `--bg` | `#E7E8F0` | Tinted field | The page behind the app shell, the gutter around the shell, the sidebar rail, empty-state grounds. Never a card fill |
| `--surface` | `#FFFFFF` | Card / sheet | Every card, modal, dropdown, popover, table body, the top bar |
| `--subtle` | `#F4F5F9` | Recessed fill | Input fills, table header rows, chart tracks, hover states, avatar placeholders, segmented-control troughs |
| `--ink` | `#131C33` | Primary text & dark fill | Headings, figures, table values, the one dark chip/pill, the selected day in a picker, chart focus bars |
| `--muted` | `#6A7288` | Secondary text | Labels, captions, table headers, axis labels, placeholder text, inactive nav items, helper copy |
| `--line` | `#E6E8EF` | Hairline | Optional 1px card border, row dividers, input borders. Always 1px, always optional — the shadow already separates |
| `--accent` | `#4A46D8` | Single indigo accent | Primary button fill, active nav pill, links, focus rings, the primary chart series, toggle-on state |
| `--accent_ink` | `#FFFFFF` | Text on accent | Text and icons on a `--accent` fill. Nothing else |
| `--pastel-mint` | `#DFF3E9` | Pastel chip / block | Chip fills, category blocks, chart series 2, illustration blocks |
| `--pastel-lilac` | `#E9E6FA` | Pastel chip / block | as above |
| `--pastel-peach` | `#FCEBE4` | Pastel chip / block | as above |
| `--pastel-butter` | `#FBF4DC` | Pastel chip / block | as above |
| `--pastel-sky` | `#E2EEFB` | Pastel chip / block | as above |

**Pastel ink rule (load-bearing):** a pastel chip carries dark ink **of its own
hue family**, never white and never `--ink`. The five matching inks below are
derived from the pastels and are the only permitted text colours on them.

```css
:root {
  /* ---- Soft Body tokens ---- */
  --bg:            #E7E8F0;
  --surface:       #FFFFFF;
  --subtle:        #F4F5F9;
  --ink:           #131C33;
  --muted:         #6A7288;
  --line:          #E6E8EF;
  --accent:        #4A46D8;
  --accent-ink:    #FFFFFF;

  /* pastels */
  --pastel-mint:   #DFF3E9;
  --pastel-lilac:  #E9E6FA;
  --pastel-peach:  #FCEBE4;
  --pastel-butter: #FBF4DC;
  --pastel-sky:    #E2EEFB;

  /* derived — matching ink for each pastel, and nothing else */
  --on-mint:       #1F6B4C;
  --on-lilac:      #4A3FA8;
  --on-peach:      #A2542F;
  --on-butter:     #7A6320;
  --on-sky:        #2A5E96;

  --accent-wash:   rgba(74, 70, 216, .10);
  --shadow-card:   0 2px 8px rgb(19 28 51 / .06);
  --shadow-raise:  0 8px 24px -8px rgb(19 28 51 / .14);
  --shadow-shell:  0 24px 60px -24px rgb(19 28 51 / .22);
}
```

Semantic colour: positive uses `--on-mint` on `--pastel-mint`; caution uses
`--on-butter` on `--pastel-butter`; attention uses `--on-peach` on
`--pastel-peach`. **There is no red and no pure green in this style** — a bad
number is reported in peach, not in alarm.

---

## Typography

A neo-grotesque or rounded humanist. Slight roundness in the letterforms helps —
Plus Jakarta Sans and Nunito Sans both have it; Inter is the safe default.

```css
--font-sans: "Plus Jakarta Sans", "Nunito Sans", "Inter",
             -apple-system, BlinkMacSystemFont, "Segoe UI",
             "Helvetica Neue", Helvetica, Arial, sans-serif;
```

Every figure gets `font-variant-numeric: tabular-nums;` — columns of money that
jitter are the fastest way to make this style look cheap.

| Role | Size / line-height | Weight | Tracking | Colour |
|---|---|---|---|---|
| Page title | 26px / 32px | 600 | `-0.02em` | `--ink` |
| Section heading | 20px / 28px | 600 | `-0.015em` | `--ink` |
| Card title | 16px / 22px | 600 | `-0.01em` | `--ink` |
| Big figure | 30px / 36px | 600 | `-0.02em` | `--ink` |
| Hero figure (one per screen) | 40px / 46px | 600 | `-0.025em` | `--ink` |
| Body | 14px / 21px | 400 | `0` | `--ink` or `--muted` |
| Label / caption | 12px / 18px | 500 | `0` | `--muted` |
| Chip | 11px / 15px | 500 | `0.01em` | pastel's own `--on-*` |
| Table header | 12px / 18px | 500 | `0.01em` | `--muted` |

**Usage rules:**

- **Sentence case throughout.** Nav items, buttons, table headers, chips,
  everything. No ALL CAPS anywhere, not even in a 12px label.
- **Pastel chips carry dark ink of their own hue family, never white.**
- **Numbers get room to breathe** — 14–16px of vertical padding per table row,
  never less. This style never crams a table.
- Comfortable, never cramped: if a card's content touches its padding, the card
  is too small, not the text.
- Weight does the hierarchy work, not size. There are only two weights in
  practice: 400 and 600. Skip 500 except on labels and chips, and never use 700.
- One hero figure per screen. If three numbers are all 40px, none of them is.

---

## Texture & effects

**Depth comes from shadow, not borders.** There is no gradient on a card, no
glass, no grain, no bevel. Four techniques.

### 1. The card

```css
.card {
  background: var(--surface);
  border-radius: 22px;                    /* 20–24px */
  padding: 24px;
  box-shadow: 0 2px 8px rgb(19 28 51 / .06);
  /* border: 1px solid var(--line);  ← optional, and usually omitted */
}
.card--raised { box-shadow: 0 8px 24px -8px rgb(19 28 51 / .14); }
```

That shadow is deliberately tiny. It is a *seat*, not a lift. Only floating
things (dropdowns, modals, dragged cards) get `--shadow-raise`.

### 2. The rounded shell

The signature move. The whole app sits inside one big rounded panel, inset in the
tinted `--bg` field with 24–40px of margin all round, so the product reads as an
object resting on a surface.

```css
body  { background: var(--bg); padding: 28px; }
.shell{
  background: var(--subtle);
  border-radius: 28px;
  overflow: hidden;
  box-shadow: 0 24px 60px -24px rgb(19 28 51 / .22);
  min-height: calc(100vh - 56px);
}
```

On narrow screens drop the margin to 0 and the shell radius to 0 — a 16px-wide
gutter looks like a mistake, not a decision.

### 3. Friendly charts

Charts are drawn, not plotted. Three approved forms:

```html
<!-- lollipop: a thin capsule stem with a circular cap -->
<svg viewBox="0 0 40 120" width="40" height="120">
  <rect x="18" y="34" width="4" height="70" rx="2" fill="#E6E8EF"/>
  <circle cx="20" cy="34" r="7" fill="#4A46D8"/>
</svg>
```

```css
/* capsule-tracked bar */
.track { height: 10px; border-radius: 999px; background: var(--subtle); overflow: hidden; }
.track > i { display:block; height:100%; border-radius:999px; background: var(--accent); }

/* soft area fill under a line — the ONE place a gradient is allowed */
<linearGradient id="fill" x1="0" y1="0" x2="0" y2="1">
  <stop offset="0%"   stop-color="#4A46D8" stop-opacity=".18"/>
  <stop offset="100%" stop-color="#4A46D8" stop-opacity="0"/>
</linearGradient>
```

Bars are capsules (`rx` = half the width). Donuts have round line caps
(`stroke-linecap: round`) and a generous 14–18px stroke. Grid lines, if any, are
`--line` at 1px and dashed. No axis boxes, no tick marks, no legend borders.

### 4. Motion

```css
* { transition: background-color .18s ease, color .18s ease,
                box-shadow .18s ease, transform .18s ease; }
.card--i:hover { transform: translateY(-2px); box-shadow: var(--shadow-raise); }
:focus-visible { outline: 2px solid var(--accent); outline-offset: 3px; border-radius: 12px; }
```

Everything eases, nothing bounces. No spring, no overshoot — moulded plastic is
soft, not bouncy.

**Forbidden:** hard 1px borders used as the primary separator, square corners,
drop shadows with a visible dark edge, glass/`backdrop-filter`, grain, neon,
saturated fills other than `--accent`, red.

---

## Layout & spacing

- **Scale:** 8px. Steps: 8 / 12 / 16 / 20 / 24 / 32 / 40. 4px only inside a chip.
- **Card padding:** 24px standard, 20px on a compact stat card, 16px on a list row.
- **Gaps:** 20px between cards, both axes. Nothing touches anything.
- **Radii:** 28px shell · 22px cards · 16px inner blocks, inputs and buttons ·
  12px chart bars and small tiles · 999px pills, chips, avatars, toggles and
  segmented controls. **Nothing is square, and nothing is less than 12px.**
- **Shell margin:** 24–40px of `--bg` visible around the shell on desktop.
- **App frame:** 236px sidebar (rail, `--bg` or `--subtle`, no border — the
  colour change is the separation) · 68px top bar · content area padded 24px.
- **Grid attitude:** a roomy 12-column feel, but expressed as CSS grid with
  explicit fractions — `2fr 1fr` hero row, then `1fr 1fr 1fr` stat row. Cards are
  large; there are rarely more than six on a screen.
- **Density:** low by design. A dashboard shows 3–4 KPI tiles, one chart, one
  8-row list. If you need a 24th row, this is the wrong style.
- **Content max-width:** 1280px inside the shell; the shell itself can be full-bleed.

---

## Components

### Buttons

```css
.btn { display:inline-flex; align-items:center; justify-content:center; gap:8px;
       font:600 14px/1 var(--font-sans); letter-spacing:-.01em;
       padding:12px 20px; border-radius:999px; border:1px solid transparent; cursor:pointer; }

/* primary — indigo pill */
.btn--primary { background:var(--accent); color:var(--accent-ink); }
.btn--primary:hover { background:#3F3BC4; transform:translateY(-1px);
                      box-shadow:0 8px 20px -8px rgb(74 70 216 / .5); }

/* secondary — white pill seated on the tinted field */
.btn--secondary { background:var(--surface); color:var(--ink);
                  box-shadow:0 2px 8px rgb(19 28 51 / .06); }
.btn--secondary:hover { background:#fff; transform:translateY(-1px); box-shadow:var(--shadow-raise); }

/* ghost — no fill until hover */
.btn--ghost { background:transparent; color:var(--muted); }
.btn--ghost:hover { background:var(--subtle); color:var(--ink); }

/* icon button — always a perfect circle */
.btn--icon { width:40px; height:40px; padding:0; border-radius:50%; background:var(--surface);
             box-shadow:0 2px 8px rgb(19 28 51 / .06); }
```

A `--ink` pill is legitimate as a second solid button (e.g. "Export"), but only
one solid dark button per screen.

### Inputs & selects

Inputs are **filled, not outlined**. The fill is `--subtle`; the border is
optional and only appears on focus.

```css
.field { width:100%; font:400 14px/1.5 var(--font-sans); color:var(--ink);
         background:var(--subtle); border:1px solid transparent;
         border-radius:16px; padding:12px 16px; }
.field::placeholder { color:var(--muted); }
.field:focus { outline:none; background:var(--surface);
               border-color:var(--accent); box-shadow:0 0 0 3px rgba(74,70,216,.14); }
select.field { appearance:none; padding-right:40px;
  background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='8'%3E%3Cpath d='M1 1.5 6 6.5l5-5' fill='none' stroke='%236A7288' stroke-width='1.6' stroke-linecap='round'/%3E%3C/svg%3E");
  background-repeat:no-repeat; background-position:right 16px center; }

/* search field is a full pill */
.field--search { border-radius:999px; padding-left:42px;
  background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' height='16'%3E%3Ccircle cx='7' cy='7' r='5.2' fill='none' stroke='%236A7288' stroke-width='1.6'/%3E%3Cpath d='M11 11l4 4' stroke='%236A7288' stroke-width='1.6' stroke-linecap='round'/%3E%3C/svg%3E");
  background-repeat:no-repeat; background-position:16px center; }

/* toggle */
.toggle { width:44px; height:26px; border-radius:999px; background:var(--line); position:relative; }
.toggle[aria-checked="true"] { background:var(--accent); }
.toggle::after { content:""; position:absolute; top:3px; left:3px; width:20px; height:20px;
  border-radius:50%; background:#fff; box-shadow:0 1px 3px rgb(19 28 51 / .2); transition:left .18s ease; }
.toggle[aria-checked="true"]::after { left:21px; }
```

### Sidebar & nav

The sidebar has **no border**. It is `--bg` (or `--subtle`) against a `--surface`
content area; the tone change is the whole separation. Items are 44px tall with
16px radius, 12px gap between icon and label. The active item is a solid
`--accent` pill with white text and a soft indigo shadow; hover is a `--subtle`
pill.

```css
.nav-item { display:flex; align-items:center; gap:12px; height:44px; padding:0 14px;
            border-radius:16px; font:500 14px/1 var(--font-sans); color:var(--muted); }
.nav-item:hover { background:var(--subtle); color:var(--ink); }
.nav-item[aria-current="page"] { background:var(--accent); color:#fff;
            box-shadow:0 8px 20px -10px rgb(74 70 216 / .7); }
```

The top bar is `--surface`, 68px tall, no bottom border — a page title on the
left, a pill search in the middle, and circular icon buttons plus a 36px round
avatar on the right.

### Cards

Base `.card` above. Variants:
- **Stat tile** — 12px `--muted` label, 30px figure, then a pastel delta chip. 20px padding.
- **Chart card** — title row with a pill segmented control ("Week / Month / Year") on the right, chart below, 24px padding.
- **List card** — 24px header, then rows separated by 1px `--line` that stops short of the padding, or by nothing at all.
- **Pastel block** — a whole card filled with one pastel and set in its `--on-*` ink. Use for one promo/next-action card per screen, never two.

### Tables

Soft Body tables are lists that happen to have columns.

```css
table { width:100%; border-collapse:separate; border-spacing:0; }
th { font:500 12px/18px var(--font-sans); color:var(--muted); text-align:left;
     padding:12px 16px; background:var(--subtle); }
th:first-child { border-radius:12px 0 0 12px; }
th:last-child  { border-radius:0 12px 12px 0; }
td { padding:16px; font-size:14px; border-bottom:1px solid var(--line); }
tr:last-child td { border-bottom:0; }
tbody tr:hover td { background:var(--subtle); }
td:first-child { border-radius:12px 0 0 12px; }   /* so the hover fill is rounded too */
td:last-child  { border-radius:0 12px 12px 0; text-align:right; }
```

No vertical rules. No zebra striping. No borders around the table. Money and
dates are right-aligned and tabular. Eight rows is a full table; past twelve,
paginate.

### Chips & badges

```css
.chip { display:inline-flex; align-items:center; gap:6px;
        font:500 11px/15px var(--font-sans); padding:6px 11px; border-radius:999px; }
.chip--mint   { background:var(--pastel-mint);   color:var(--on-mint); }
.chip--lilac  { background:var(--pastel-lilac);  color:var(--on-lilac); }
.chip--peach  { background:var(--pastel-peach);  color:var(--on-peach); }
.chip--butter { background:var(--pastel-butter); color:var(--on-butter); }
.chip--sky    { background:var(--pastel-sky);    color:var(--on-sky); }
.chip--ink    { background:var(--ink);           color:#fff; }
```

A pastel chip may carry a 6px dot in its own ink. Avatars are 36px circles;
groups overlap by -8px with a 2px `--surface` ring.

### Modals & drawers

Centred sheet, `--surface`, **28px radius** (one step rounder than a card), 28px
padding, max-width 480px, `--shadow-shell`. Scrim `rgb(19 28 51 / .28)`, flat.
Close is a 36px circular ghost button. A drawer is the same sheet pinned to the
right with `border-radius: 28px 0 0 28px` and full height inside the shell.
Modals often open with a pastel-filled header block — that is the house detail.

### Footer

An app footer is a single quiet 56px strip inside the shell: `--muted` 12px on
`--subtle`, left "Last synced 4 minutes ago", right a couple of ghost links. On a
marketing-adjacent screen (a booking confirmation page), use a `--surface` card
footer with 24px padding instead. Never a dark footer — this style has no dark
regions.

---

## Imagery

Soft Body barely uses photography. In order of preference:

1. **None.** Pastel blocks, generous whitespace and a friendly chart carry the screen.
2. **Rounded 3D or flat vector spot illustration** — matte, large radii, no sharp
   edges, pastel palette plus one indigo. Used at 120–200px inside an empty
   state, an upgrade card or a modal header. See `image-recipe.md`.
3. **Avatars** — real people, but always circular, always small (28–44px). In an
   offline artifact, render them as a pastel circle with the person's initials in
   the matching `--on-*` ink.
4. **Photography** — only for a venue or product thumbnail (a booking screen), in
   a 16px-radius rounded rectangle, never full-bleed, never with text over it.

Icons: 20px, 1.6px stroke, **round caps and round joins**, `--muted` at rest and
`--accent` or `--ink` when active. Never filled, never multicolour, never sharp-cornered.

---

## Do

1. Seat every card on `0 2px 8px rgb(19 28 51 / .06)` and let the shadow, not a border, do the separating.
2. Put the whole app inside a 28px rounded shell inset in the `#E7E8F0` field.
3. Keep radii large and consistent — 22px cards, 16px controls, 999px pills.
4. Give tables 16px of row padding and stop at eight rows.
5. Use pastels for state and category, always with their own dark hue-family ink.
6. Draw charts as lollipops, capsule bars and round-capped donuts.
7. Fill inputs with `#F4F5F9` instead of outlining them.
8. Keep exactly one hero figure and one solid accent button per screen.
9. Use tabular numerals on every figure.

## Don't

1. Don't use hard borders as the primary separator, and never a border heavier than 1px.
2. Don't square a corner — not on a card, a chart bar, an input, a table header or an icon tile.
3. Don't put white text on a pastel chip; use the matching `--on-*` ink.
4. Don't introduce red, neon, or any saturated colour beyond `#4A46D8`.
5. Don't cram — no 24-row tables, no 6-column stat strips, no 8px gaps between cards.
6. Don't add glass, grain, bevels or heavy drop shadows; the shadow is a seat, not a lift.
7. Don't build a dark mode or a dark footer. There are no dark regions in this style except one small `--ink` pill.
8. Don't use ALL CAPS or letterspaced labels — sentence case everywhere.
9. Don't put a gradient on a surface; the only gradient allowed is the soft area fill under a chart line.
10. Don't animate with bounce or spring easing.
