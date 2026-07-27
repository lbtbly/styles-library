# Didone Signal

**Pairing:** Fashion masthead × pill button
**Concept:** High-contrast serif display against tangerine and black pills — masthead grammar on a product page.

Didone Signal borrows the grammar of a fashion or architecture magazine — a big
centred high-contrast serif, a tight measure, acres of paper-white — and drops
two modern controls into it: a black pill button with a tangerine arrow chip
welded onto its end, and flat black or tangerine blocks used as section breaks.
The result reads expensive without reading old. Use it for premium and luxury
brands, property and hospitality, editorial and publishing products,
professional services and brand-led launch pages. Avoid it for technical
developer products, dense dashboards, playful consumer apps and anything with a
high data density: the style's whole argument is that there is very little on the
page and every piece of it was chosen.

---

## Palette

Nine tokens. Two neutrals, one warm accent, one near-black block. Nothing else.

| Token | Value | Role | Allowed to appear |
|---|---|---|---|
| `--bg` | `#FBFBFA` | Paper ground | The page. Every light section. The colour the hero photograph dissolves into |
| `--surface` | `#FFFFFF` | Card / sheet | White cards, modals, dropdowns, input fills, the sticky nav |
| `--ink` | `#080808` | Display & body text | Serif headlines, sans body, table figures, the wordmark, icon strokes |
| `--muted` | `#6A6A68` | Secondary text | Standfirst and body paragraphs, captions, ALL-CAPS labels, table headers, placeholder text, footer links |
| `--line` | `#E6E5E1` | Hairline | 1px rules between sections, card borders, table rules, input borders, the editorial column rules. **This warm grey line is a signature — never substitute a cool grey** |
| `--accent` | `#E85A00` | Tangerine | The arrow chip, a full-bleed tangerine section field, one word of an eyebrow, the active tab underline, a price figure, small icon glyphs. **Never a headline colour** |
| `--accent_ink` | `#FFFFFF` | Text on tangerine | Text and arrows sitting on a `--accent` fill |
| `--block` | `#0A0A0A` | Black block | The pill button fill, black cards, the footer, the dark half of a split section |
| `--block_ink` | `#FAFAF8` | Text on black | All text on `--block`. Slightly warm off-white — never pure `#FFFFFF`, that is the tell |

```css
:root {
  --bg:         #FBFBFA;
  --surface:    #FFFFFF;
  --ink:        #080808;
  --muted:      #6A6A68;
  --line:       #E6E5E1;
  --accent:     #E85A00;
  --accent-ink: #FFFFFF;
  --block:      #0A0A0A;
  --block-ink:  #FAFAF8;

  /* derived — allowed, do not invent others */
  --accent-wash: rgba(232, 90, 0, .08);   /* tangerine chip fill on paper */
  --grid-rule:   rgba(255, 255, 255, .14); /* the architectural grid on tangerine */
  --block-line:  rgba(250, 250, 248, .16); /* hairline inside a black block */
}
```

Tangerine is a **signal**, not a theme. On a typical page it should account for
well under 10% of the pixels: a few arrow chips, one price, and at most one
full-bleed band. Photographic colour (sky, stone, timber) is exempt from this
palette but must stay muted and high-key.

---

## Typography

**The serif/sans pairing IS the style.** Two families, and they never swap jobs.

```css
/* display serif — headlines only */
--font-display: "Instrument Serif", "Playfair Display", "Bodoni Moda", "Prata",
                Didot, "Didot LT STD", "Bodoni 72", "Hoefler Text",
                "Times New Roman", Times, serif;

/* neo-grotesque — everything else */
--font-sans: "Inter", "Söhne", "Helvetica Now", -apple-system,
             BlinkMacSystemFont, "Segoe UI", "Helvetica Neue", Helvetica,
             Arial, sans-serif;
```

The fallback chain matters: Didot and Bodoni 72 ship with macOS, Times New Roman
is everywhere, and all three keep the thick–thin contrast that makes the style
work. If only the last fallback resolves, the page still reads as a masthead.

| Role | Family | Size / line-height | Weight | Tracking | Case |
|---|---|---|---|---|---|
| Hero headline | display serif | 72px / 74px | 400 | `-0.01em` | Sentence |
| Hero (≤700px) | display serif | 40px / 44px | 400 | `-0.01em` | Sentence |
| Section headline | display serif | 44px / 50px | 400 | `-0.005em` | Sentence |
| Card headline | display serif | 28px / 34px | 400 | `0` | Sentence |
| Display figure (price, stat) | display serif | 56px / 60px | 400 | `-0.01em` | — |
| Standfirst | sans | 18px / 30px | 400 | `0` | Sentence |
| Body | sans | 16px / 26px | 400 | `0` | Sentence |
| Small / caption | sans | 14px / 22px | 400 | `0` | Sentence |
| Label / eyebrow | sans | 12px / 16px | 500 | `0.08em` | **ALL CAPS** |
| Button | sans | 15px / 1 | 500 | `0` | Sentence |
| Nav link | sans | 15px / 1 | 400 | `0` | Sentence |

**Usage rules:**

- **The serif appears only at display sizes. Below 24px it is always the sans.**
  No serif body copy, no serif buttons, no serif nav, no serif table cells, no
  serif captions. This is the single rule that separates the style from a
  generic "elegant" template.
- **Never set a headline in the sans.** If a heading is too small for the serif,
  it is a label, and labels are 12px ALL-CAPS sans.
- **Centre the hero** and keep the measure tight: **maximum ~20 characters per
  headline line**. Wrap by hand with `<br>` or `max-width: 20ch`.
- Let the serif's thick–thin contrast do the decorating: **no italic, no
  underline, no colour, no weight change on the headline.** One exception is
  permitted per page — a single italic word inside a headline — and most pages
  should not use it.
- Body copy is quiet grey sans (`--muted`) at 16/26. Only promote a paragraph to
  `--ink` when it is a pull quote.
- ALL CAPS + `0.08em` exists in exactly one place: the 12px eyebrow / label.
  Nothing else in the design is capitalised or letterspaced.
- Numerals: `font-variant-numeric: tabular-nums` on tables and stat rows; leave
  the display serif's default figures alone in a price.

---

## Texture & effects

**Print-flat.** No gradients on surfaces, no glass, no glow, no grain, no bevel,
no shadow on a card. A card is separated by a 1px `--line` or by being black.
Three real effects exist.

### 1. The signature button — black pill, welded tangerine arrow chip

The one component people will recognise. The chip is a perfect circle inset
inside the pill so that it is tangent to the pill's trailing edge — the pill's
right padding equals its vertical padding.

```html
<a class="pill" href="#">Enquire about a stay
  <span class="pill__chip" aria-hidden="true">
    <svg viewBox="0 0 16 16"><path d="M4 12 12 4M6 4h6v6"/></svg>
  </span>
</a>
```

```css
.pill{
  display:inline-flex; align-items:center; gap:16px;
  background:var(--block); color:var(--block-ink);
  font:500 15px/1 var(--font-sans);
  padding:7px 7px 7px 26px;      /* 7px right == 7px vertical: welds the chip */
  border-radius:999px; border:1px solid var(--block);
  transition:background-color .18s ease, color .18s ease;
}
.pill__chip{
  width:38px; height:38px; flex:none;
  border-radius:50%; background:var(--accent);
  display:grid; place-items:center;
  transition:transform .18s ease;
}
.pill__chip svg{ width:15px; height:15px; fill:none; stroke:var(--accent-ink);
                 stroke-width:1.6; stroke-linecap:round; stroke-linejoin:round; }
.pill:hover .pill__chip{ transform:rotate(45deg); }   /* the only flourish */

/* inverted: white pill, same tangerine chip — for use on a black block */
.pill--light{ background:var(--surface); color:var(--ink); border-color:var(--surface); }
/* outline: paper pill, hairline border, tangerine chip */
.pill--outline{ background:transparent; color:var(--ink); border-color:var(--line); }
```

The arrow is a 45° north-east arrow, not a chevron and not a right-pointing
arrow. The chip is **always** tangerine, on every variant, including inside a
tangerine section (where the pill becomes white and the chip becomes black —
that is the only permitted chip inversion).

### 2. The photograph that dissolves

The one material moment: a soft sky/cloud/landscape image behind the hero type
that fades into `--bg` with no hard edge. With a real photograph, mask it. In an
offline artifact, build the sky from layered radial gradients and mask it the
same way.

```css
.sky{
  position:absolute; inset:0; z-index:-1; pointer-events:none;
  background:
    radial-gradient(46% 38% at 20% 30%, rgba(255,255,255,.96), rgba(255,255,255,0) 62%),
    radial-gradient(40% 32% at 74% 20%, rgba(255,255,255,.92), rgba(255,255,255,0) 64%),
    radial-gradient(34% 28% at 50% 46%, rgba(255,255,255,.90), rgba(255,255,255,0) 66%),
    linear-gradient(180deg, #C6D6E2 0%, #E2EAEF 44%, var(--bg) 86%);
  -webkit-mask-image: linear-gradient(180deg, #000 0%, #000 40%, transparent 88%);
          mask-image: linear-gradient(180deg, #000 0%, #000 40%, transparent 88%);
}
```

With a real image, the equivalent is
`mask-image: linear-gradient(180deg,#000 40%,transparent 88%)` plus
`filter: saturate(.82) brightness(1.04)` to keep it high-key. **Never darken a
photograph to make text legible** — move the text or lighten the image.

### 3. The tangerine field with an architectural grid

The house section break: a flat tangerine band ruled with a faint white grid,
like a drawing sheet.

```css
.field-accent{
  background-color: var(--accent);
  color: var(--accent-ink);
  background-image:
    linear-gradient(to right,  var(--grid-rule) 1px, transparent 1px),
    linear-gradient(to bottom, var(--grid-rule) 1px, transparent 1px);
  background-size: 96px 96px;
}
/* the same grid on paper, at half strength, for a quiet section */
.field-grid{ background-color: var(--bg);
  background-image:
    linear-gradient(to right,  var(--line) 1px, transparent 1px),
    linear-gradient(to bottom, var(--line) 1px, transparent 1px);
  background-size: 96px 96px; }
```

### Everything else

```css
hr, .rule { height:1px; background:var(--line); border:0; }
:focus-visible { outline:2px solid var(--accent); outline-offset:3px; }
* { transition: background-color .18s ease, color .18s ease, border-color .18s ease; }
```

**Forbidden:** box-shadows of any kind on cards (the hairline is the separation),
gradients on buttons or surfaces, backdrop-filter, noise, rounded-everything —
and any translucency other than the two derived rgba rules above.

---

## Layout & spacing

- **Scale:** 8px. Steps: 8 / 16 / 24 / 40 / 64 / 96 / 120 / 160.
- **Section rhythm:** 120px vertical padding minimum, 160px on a hero or a
  closing CTA. Sections are separated by a 1px `--line`, a colour change, or
  both — never by a shadow.
- **Container:** 1180px max-width, 32px gutters (20px below 720px).
- **Editorial symmetry:** the hero is centred; the standfirst is centred under it
  at `max-width: 46ch`; the CTA row is centred. Body sections may go asymmetric
  (a 5/7 split with the serif heading left and two grey columns right), but the
  hero never does.
- **Measure:** headlines ≤20 characters per line; body ≤72 characters per line.
- **Radii:** 16–20px on cards and images · 999px on pills, chips and the arrow
  chip · 0px on full-bleed bands and table cells. Nothing in between; a 6px
  radius reads as a different style entirely.
- **Density:** low. Three feature cards, not six. Four rows in a stat strip, not
  eight. If a section has more than one idea in it, split it.
- **Grid attitude:** hard 12-column feel expressed as 2, 3 or 4 equal cards with
  24px gaps and full-bleed bands between them. Black cards and white cards may
  alternate inside one row — that contrast is a compositional device, not a state.

---

## Components

### Buttons

Four, and only four.

| Variant | Use | Recipe |
|---|---|---|
| **Signature pill** | The one primary CTA per section | black pill + welded tangerine arrow chip (code above) |
| **Light pill** | Primary CTA on a black or tangerine block | `.pill--light` — white pill, tangerine chip (black chip on tangerine) |
| **Outline pill** | Secondary action beside the primary | `.pill--outline` — transparent, 1px `--line`, `--ink` text, tangerine chip |
| **Text link** | Tertiary | 15px sans `--ink`, 1px `--line` underline offset 6px; underline becomes `--accent` on hover |

There is no ghost icon-only button and no small/large size ramp — a pill is
either the standard 52px tall version or the 44px compact version used in the nav.

### Inputs & selects

Squared-off rectangles with a hairline, not pills. This is the deliberate
contrast against all the round CTAs.

```css
.field{ width:100%; font:400 16px/1.5 var(--font-sans); color:var(--ink);
        background:var(--surface); border:1px solid var(--line);
        border-radius:14px; padding:15px 16px; }
.field::placeholder{ color:var(--muted); }
.field:focus{ outline:none; border-color:var(--ink); }
.field[aria-invalid="true"]{ border-color:var(--accent); }
select.field{ appearance:none; padding-right:44px;
  background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='8'%3E%3Cpath d='M1 1.5 6 6.5l5-5' fill='none' stroke='%23080808' stroke-width='1.4' stroke-linecap='round'/%3E%3C/svg%3E");
  background-repeat:no-repeat; background-position:right 16px center; }
label{ display:block; font:500 12px/16px var(--font-sans);
       letter-spacing:.08em; text-transform:uppercase; color:var(--muted);
       margin-bottom:8px; }
```

### Nav

Sticky, `--bg` at rest with a 1px `--line` underneath. Wordmark left in the
**display serif** at 22px (the wordmark is the only sub-24px serif permitted, and
only because it is a logotype). Links centre or right in 15px sans `--muted`;
the active link is `--ink` with a 2px `--accent` underline. One compact signature
pill on the right. Below 900px, drop the link list and keep wordmark + pill.

### Cards

Two kinds, used against each other.

```css
.card{ background:var(--surface); border:1px solid var(--line);
       border-radius:18px; padding:32px; }
.card--black{ background:var(--block); color:var(--block-ink); border-color:var(--block); }
.card--black .muted{ color:rgb(250 250 248 / .62); }
.card--black .rule{ background:var(--block-line); }
.card--accent{ background:var(--accent); color:var(--accent-ink); border-color:var(--accent); }
```

A card carries: a 12px ALL-CAPS label, a serif headline at 28/34, two lines of
grey sans, and optionally a pill or a `→` text link. Never a shadow. Never a
hover lift — at most, the border darkens to `--ink`.

### Tables

Editorial, not spreadsheet. Used mainly for a pricing comparison.

```css
table{ width:100%; border-collapse:collapse; }
th{ font:500 12px/16px var(--font-sans); letter-spacing:.08em;
    text-transform:uppercase; color:var(--muted); text-align:left;
    padding:16px 20px; border-bottom:1px solid var(--line); }
td{ font:400 15px/24px var(--font-sans); color:var(--ink);
    padding:18px 20px; border-bottom:1px solid var(--line);
    font-variant-numeric:tabular-nums; }
tr:last-child td{ border-bottom:0; }
td:not(:first-child), th:not(:first-child){ text-align:center; }
```

No zebra, no vertical rules, no borders around the table, no hover fill. A tick
is a 16px tangerine SVG check; an omission is a 16px `--line` dash. Keep to 10
rows.

### Chips & badges

```css
.chip{ display:inline-flex; align-items:center; gap:8px;
       font:500 12px/16px var(--font-sans); letter-spacing:.08em;
       text-transform:uppercase; padding:9px 16px; border-radius:999px; }
.chip--outline{ border:1px solid var(--line); color:var(--muted); }
.chip--accent { background:var(--accent-wash); color:var(--accent); }
.chip--solid  { background:var(--accent); color:var(--accent-ink); }
.chip--ink    { background:var(--block);  color:var(--block-ink); }
```

Chips are the only place ALL CAPS appears besides labels. A 5px tangerine dot
before the text is the house detail.

### Modals & drawers

Centred sheet, `--surface`, 20px radius, 40px padding, **1px `--line` border and
no shadow**, max-width 520px. Scrim `rgb(8 8 8 / .38)`, flat. The close control
is a 40px circular outline button with a hairline border. Content inside a modal
follows the same grammar: 12px ALL-CAPS label, serif headline, grey sans body,
one signature pill.

### Footer

Full-bleed `--block`. Four columns: a display-serif wordmark plus a one-line
statement, then three link stacks with 12px ALL-CAPS headers in
`rgb(250 250 248 / .5)` and 15px sans links in `rgb(250 250 248 / .62)`. 96px top
padding, a `--block-line` hairline, then a 14px legal row. A single tangerine
arrow chip beside the newsletter field is the only colour in the footer.

---

## Imagery

Photography, treated as print. One image per screen at most.

- **Subject:** sky, cloud, coast, stone, timber, an empty well-lit room, a
  building corner against light. Never people looking at the camera, never a
  laptop on a desk, never a stock handshake.
- **Grade:** high-key, gentle contrast, muted natural palette, one warm note.
  `filter: saturate(.85) brightness(1.04) contrast(.96)` is the house grade.
- **Treatment:** either (a) the hero image dissolving into `--bg` through a
  linear-gradient mask, or (b) a contained image in an 18px-radius rectangle with
  a 1px `--line` border and a 12px ALL-CAPS caption underneath. Nothing else.
- **Never** darken an image to place white text on it, never full-bleed a dark
  photograph, never apply duotone, and never crop a face to a circle.
- **Icons** are 16–20px, 1.6px stroke, round caps, `--ink` or `--accent`. The
  45° arrow is the house icon and should appear far more often than any other.
- **No illustration.** If there is no photograph, use type, a hairline rule and a
  tangerine field — that is a complete composition in this style.

---

## Do

1. Set every headline in the display serif and everything under 24px in the sans.
2. Centre the hero and hold the headline to about 20 characters a line.
3. Use the black pill with the welded circular tangerine arrow chip as the primary CTA — one per section.
4. Give sections 120–160px of vertical air and separate them with a 1px `#E6E5E1` rule or a colour change.
5. Let one soft high-key photograph dissolve into `#FBFBFA` behind the hero type.
6. Use a flat `#E85A00` field ruled with a faint white grid as a section break.
7. Alternate black `#0A0A0A` cards and white cards inside one row for contrast.
8. Reserve ALL CAPS and `0.08em` tracking for 12px labels and chips only.
9. Keep body copy quiet grey sans at 16/26.

## Don't

1. Don't set a headline in the sans, or body copy in the serif.
2. Don't colour, italicise, underline or embolden the hero headline — the thick–thin contrast is the decoration.
3. Don't put a box-shadow on anything. Separation is a hairline or a colour change.
4. Don't use a gradient on a surface, a button or a card; the only gradient in the style is inside the dissolving photograph.
5. Don't let tangerine become a theme colour — it is a signal, well under 10% of the page.
6. Don't use pure white text on black; use the warm `#FAFAF8`.
7. Don't swap the arrow chip for a chevron, a right-arrow, or a differently coloured circle.
8. Don't use mid-range radii — pills are 999px, cards are 16–20px, bands and tables are 0.
9. Don't build dense screens: no dashboards, no 24-row tables, no sidebars, no data grids.
10. Don't darken a photograph so text can sit on it, and don't use people-facing stock photography.
