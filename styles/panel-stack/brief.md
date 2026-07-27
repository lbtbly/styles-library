# Panel Stack

**Pairing:** Split-pane IDE × filing drawer
**Concept:** Work happens in panels — master list, detail drawer, kanban column — layered over a scrim instead of navigated away from.

Panel Stack is for operational software with a list-plus-detail spine: project and task management, CRM and support desks, content and asset managers, internal tooling with multi-step workflows. Its governing idea is that you never lose your place — opening an item slides a panel *over* the board rather than replacing the page, and the dimmed context behind it stays legible so you can see what you came from. It reads calm and workmanlike: flat white panels, hairline borders, one violet accent, and exactly two levels of elevation.

Avoid it for marketing sites, single-purpose landing pages, data-viz-first analytics, and products whose main object is a canvas rather than a list — it has nothing to say when there is no list to sit beside.

---

## Palette

Sampled from the source shots. Fixed values — do not adjust them toward a house palette.

| Token | Hex | Role | Where it is allowed to appear |
|---|---|---|---|
| `--bg` | `#F7F8F9` | App ground | The page behind all panels; the gap between panels; toolbar grounds. |
| `--surface` | `#FFFFFF` | Panel fill | Every panel: master list, detail pane, drawer, dialog, card, popover, top bar. |
| `--well` | `#EFF1F3` | Recessed fill | Kanban column wells, composer input wells, code/quote blocks, disabled controls, avatar placeholders. Recessed — it never takes a border. |
| `--ink` | `#0B1220` | Primary text | Titles, card titles, body copy, active nav, the scrim's base hue. |
| `--muted` | `#667085` | Secondary text | Meta lines, timestamps, counts, placeholders, inactive nav, icon strokes. |
| `--line` | `#E4E7EC` | Hairline border | Panel edges, card borders, dividers, input borders, table rules. Always exactly 1px. |
| `--accent` | `#5B2FD6` | Primary violet | Primary button, active nav rail item, focus ring, selected list item rule, links, active tab underline, progress fill. The only saturated colour. |
| `--positive` | `#0A7C4A` | Done / healthy | "Done", "Resolved", "On track" capsules; success dots; completed checklist ticks. |
| `--negative` | `#B42318` | Blocked / overdue | "Blocked", "Overdue", "High priority" capsules; destructive action label; SLA breach. |
| `--scrim` | `rgba(11, 18, 32, 0.42)` | Overlay dim | Behind drawers and dialogs only. Dim it — never blur it. |

**Derived values** — everything else comes from these, nothing new is invented:

- Capsule fill = the semantic hue at **10% over `--surface`** → `rgb(91 47 214 / .10)`, `rgb(10 124 74 / .10)`, `rgb(180 35 24 / .10)`. Neutral capsule = `--well`.
- Focus ring = `rgb(91 47 214 / .18)`.
- Selected list row = `rgb(91 47 214 / .06)` plus a 2px `--accent` left rule.
- Hover on a white panel = `--bg`. A card inside a `--well` column does **not** change fill or lift on hover — hover shows as a 2px `--accent` left rule appearing on the card.

```css
:root {
  /* palette — verbatim from style.json */
  --bg:       #F7F8F9;
  --surface:  #FFFFFF;
  --well:     #EFF1F3;
  --ink:      #0B1220;
  --muted:    #667085;
  --line:     #E4E7EC;
  --accent:   #5B2FD6;
  --positive: #0A7C4A;
  --negative: #B42318;
  --scrim:    rgba(11, 18, 32, 0.42);

  /* derived */
  --accent-wash:   rgb(91 47 214 / .10);
  --accent-select: rgb(91 47 214 / .06);
  --focus:         rgb(91 47 214 / .18);
  --positive-wash: rgb(10 124 74 / .10);
  --negative-wash: rgb(180 35 24 / .10);

  /* the two elevations — there is no third */
  --e0: none;                                   /* resting: 1px solid var(--line) instead */
  --e1: 0 12px 32px -8px rgb(11 18 32 / .18);   /* floating: drawer, dialog, popover */

  /* geometry */
  --r-card: 10px;
  --r-ctl:  8px;
  --r-cap:  6px;
  --gap:    12px;
  --pad:    16px;
  --col:    300px;   /* kanban column */
  --master: 320px;   /* master list minimum */
  --drawer: 520px;   /* detail drawer */
}
```

---

## Typography

One neo-grotesque at every level. No second face, no display tier.

```css
--font: "Inter", "Söhne", -apple-system, BlinkMacSystemFont, "Segoe UI",
        Roboto, "Helvetica Neue", Arial, sans-serif;
--font-mono: ui-monospace, SFMono-Regular, Menlo, Consolas, "Liberation Mono", monospace;
```

`--font-mono` appears only in ticket IDs, code blocks and API references.

| Role | Size / line-height | Weight | Tracking | Notes |
|---|---|---|---|---|
| Drawer / page title | 18 / 24 | 600 | -0.01em | Largest type in the system. Nothing exceeds 20px. |
| Panel header | 14 / 20 | 600 | 0 | Column headers, panel titles, section titles inside the drawer. |
| Card title | 14 / 20 | 500 | 0 | Kanban card, list row subject. Two lines maximum, then ellipsis. |
| Body | 13 / 18 | 400 | 0 | Descriptions, message bodies, form values. |
| Meta | 12 / 16 | 400 | 0 | `--muted`. Timestamps, counts, assignee names, breadcrumb. |
| Group header | 11 / 14 | 600 | 0.06em | ALL-CAPS. Nav group labels and drawer field labels only. |
| Capsule label | 11 / 14 | 500 | 0 | Sentence case. Never uppercase. |
| Mono ID | 12 / 16 | 500 | 0 | `--font-mono`, `--muted`, e.g. `PLT-4192`. |

**Usage rules**

- Sentence case everywhere except group headers.
- Capsule labels are 11px medium and never uppercase — that is what separates a capsule from a group header.
- Keep line length in the detail pane under **68 characters** (`max-width: 62ch` on prose blocks).
- Timestamps are relative under 24h ("14m ago", "3h ago") and absolute above ("12 Mar, 09:41").
- Numerals do not need to be tabular in prose, but counts in a column header and any figure in a table do: `font-variant-numeric: tabular-nums`.

---

## Texture & effects

Flat fills, hairline borders, **exactly two elevations**. Getting these two right is most of the style.

**Elevation 0 — resting.** Cards, list rows, panels at rest have no shadow at all. They are separated by a 1px `--line` border or by sitting on a different fill.

```css
.card { background: var(--surface); border: 1px solid var(--line);
        border-radius: var(--r-card); padding: var(--pad); box-shadow: none; }
```

**Elevation 1 — floating.** Drawer, dialog, popover, dropdown, toast. One shadow value, always paired with a scrim if it is modal.

```css
.floating { background: var(--surface); border-radius: 12px;
            box-shadow: 0 12px 32px -8px rgb(11 18 32 / .18); }
```

**The scrim.** Dim, never blur. This is the style's signature and the single easiest thing to get wrong.

```css
.scrim { position: fixed; inset: 0; background: rgba(11, 18, 32, 0.42);
         /* NO backdrop-filter. The board behind must stay readable. */ }
.drawer { position: fixed; inset: 0 0 0 auto; width: min(520px, 88vw);
          background: var(--surface); border-left: 1px solid var(--line);
          box-shadow: 0 12px 32px -8px rgb(11 18 32 / .18);
          display: flex; flex-direction: column; }
```

The drawer **overlays**; it never pushes the board sideways. The board keeps its scroll position and stays visible at the left edge.

**Wells.** A column or an input well is a recessed fill, not a bordered box:

```css
.well { background: var(--well); border-radius: var(--r-card); border: none; }
```

**Focus.**

```css
:where(button, a, input, textarea, select, [tabindex]):focus-visible {
  outline: none; border-color: var(--accent); box-shadow: 0 0 0 3px var(--focus);
}
```

**Motion.** Drawer enters with `transform: translateX(100%) → 0` over 180ms `cubic-bezier(.32,.72,0,1)`; the scrim fades over 140ms. Nothing else animates.

**Forbidden:** `backdrop-filter` of any kind, gradients (a capsule wash is a flat alpha fill, not a gradient), glow, inner shadows, borders above 1px except the 2px accent selection rule, and any third elevation between "flat" and "floating".

---

## Layout & spacing

- **Base scale 8px** (4px permitted for icon gaps and capsule padding). Legal steps: 4, 8, 12, 16, 24, 32, 48.
- **The screen is panels, not pages.** Typical spine: icon rail (56px) → master list (min 320px) → detail pane (fills) → optional context panel (280px).
- **Kanban columns** are `--well` wells `300px` wide, `12px` internal padding, holding `--surface` cards with `12px` gaps. The column header sits *outside* the well or in its top padding, with a count capsule.
- **Detail drawer** 480–560px (`520px` default), right-docked, full height.
- **Card padding 16px**, gap between cards 12px, radius 10px on cards, 8px on controls, 6px on capsules.
- **Panel gaps:** 1px `--line` between fixed panels; 12–16px of `--bg` when panels genuinely float apart.
- **Density:** comfortable, not starved. A kanban card is 96–140px tall; a list row is 72–84px with three lines (subject, snippet, meta).

```css
.app  { display: grid; grid-template-columns: 56px var(--master) 1fr; height: 100vh;
        background: var(--bg); }
.panel{ background: var(--surface); border-right: 1px solid var(--line);
        display: flex; flex-direction: column; min-width: 0; overflow: hidden; }
.board{ display: flex; gap: 16px; padding: 16px; overflow-x: auto; align-items: flex-start; }
.column { flex: 0 0 var(--col); background: var(--well); border-radius: var(--r-card); padding: 12px; }
```

---

## Components

### Buttons

36px tall (32px in a toolbar), 8px radius, 13px/500.

```css
.btn         { height: 36px; padding: 0 14px; border-radius: var(--r-ctl); border: 1px solid transparent;
               font: 500 13px/1 var(--font); display: inline-flex; align-items: center; gap: 6px; cursor: pointer; }
.btn-primary { background: var(--accent); color: #FFFFFF; }
.btn-primary:hover { background: #4E27B8; }             /* accent darkened, not a new hue */
.btn-secondary { background: var(--surface); color: var(--ink); border-color: var(--line); }
.btn-secondary:hover { background: var(--bg); }
.btn-ghost   { background: transparent; color: var(--muted); }
.btn-ghost:hover { background: var(--well); color: var(--ink); }
.btn-danger  { background: var(--surface); color: var(--negative); border-color: var(--line); }
.btn-icon    { width: 32px; height: 32px; padding: 0; justify-content: center; border-radius: var(--r-ctl); }
```

One primary per panel. The drawer footer is the only place two buttons of equal weight sit side by side (Cancel = secondary, Save = primary, right-aligned).

### Inputs & selects

```css
.field { height: 36px; padding: 0 12px; background: var(--surface); border: 1px solid var(--line);
         border-radius: var(--r-ctl); font: 400 13px/1 var(--font); color: var(--ink); width: 100%; }
.field::placeholder { color: var(--muted); }
.field:focus { border-color: var(--accent); box-shadow: 0 0 0 3px var(--focus); outline: none; }
.search { background: var(--well); border-color: transparent; padding-left: 34px; }
.textarea, .composer { min-height: 88px; padding: 12px; background: var(--well);
                       border: 1px solid transparent; border-radius: var(--r-ctl); resize: vertical; }
.select { appearance: none; padding-right: 30px; }   /* chevron = inline 10×6 SVG, stroke --muted */
```

Field labels sit above at 11px ALL-CAPS `--muted` 0.06em in the drawer, or as a left column in a two-column meta grid (`grid-template-columns: 108px 1fr; row-gap: 12px`).

### Nav / rail / sidebar

Two nav idioms, both valid:

```css
/* 56px icon rail — for apps with a wide master list */
.rail       { width: 56px; background: var(--surface); border-right: 1px solid var(--line);
              display: flex; flex-direction: column; align-items: center; gap: 4px; padding: 12px 0; }
.rail-item  { width: 36px; height: 36px; border-radius: var(--r-ctl); display: grid; place-items: center;
              color: var(--muted); }
.rail-item[aria-current] { background: var(--accent-wash); color: var(--accent); }

/* 232px labelled sidebar — for apps without one */
.side-item  { height: 34px; padding: 0 10px; border-radius: var(--r-ctl); color: var(--muted);
              display: flex; align-items: center; gap: 10px; font-weight: 500; }
.side-item[aria-current] { background: var(--accent-wash); color: var(--accent); }
```

Nav group labels are 11px ALL-CAPS 0.06em `--muted` with 16px of space above.

### Cards

The kanban card is the style's most recognisable object:

```html
<article class="card">
  <span class="cap cap-warn">In review</span>
  <h3>Migrate billing webhooks to v2</h3>
  <p class="meta">Retry queue must drain before cutover.</p>
  <div class="card-foot"><span class="mono">PLT-4192</span><span class="meta">3 Jul</span></div>
</article>
```

Order inside a card: capsule → title (14/20 medium) → one line of body → footer row with ID, avatars, due date, and small count icons. Cards never carry a shadow, never a coloured fill, and the only colour on them is the capsule and, when selected, a 2px `--accent` left rule.

### Master list rows

```css
.row { padding: 12px 16px; border-bottom: 1px solid var(--line); display: grid;
       grid-template-columns: 32px 1fr auto; gap: 12px; cursor: pointer; }
.row:hover { background: var(--bg); }
.row[aria-selected="true"] { background: var(--accent-select); box-shadow: inset 2px 0 0 var(--accent); }
.row .subject { font: 500 14px/20px var(--font); }
.row .snippet { font: 400 13px/18px var(--font); color: var(--muted);
                overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
.unread::before { content:""; width:7px; height:7px; border-radius:50%; background: var(--accent); }
```

Avatars are 32px `--well` circles with 12px `--muted` semibold initials.

### Tables

Panel Stack tables are quieter than its cards — they live inside a panel, not full-bleed:

```css
table th { font: 600 11px/14px var(--font); letter-spacing: .06em; text-transform: uppercase;
           color: var(--muted); text-align: left; padding: 10px 12px; border-bottom: 1px solid var(--line); }
table td { padding: 12px; border-bottom: 1px solid var(--line); font-size: 13px; }
table tr:last-child td { border-bottom: none; }
```

### Capsules (status)

```css
.cap { display: inline-flex; align-items: center; gap: 5px; height: 22px; padding: 0 8px;
       border-radius: var(--r-cap); font: 500 11px/1 var(--font);
       background: var(--well); color: var(--muted); }
.cap::before { content:""; width: 6px; height: 6px; border-radius: 50%; background: currentColor; }
.cap-done  { background: var(--positive-wash); color: var(--positive); }
.cap-block { background: var(--negative-wash); color: var(--negative); }
.cap-live  { background: var(--accent-wash);   color: var(--accent); }
```

A capsule states a *status*, not a category. If it is a category, use the neutral `--well` capsule with no dot.

### Drawers & dialogs

```html
<div class="scrim" data-close></div>
<aside class="drawer" role="dialog" aria-modal="true" aria-label="Task detail">
  <header class="drawer-head">…title, capsule, close button…</header>
  <div class="drawer-body">…meta grid, description, checklist, activity…</div>
  <footer class="drawer-foot">…secondary + primary…</footer>
</aside>
```
```css
.drawer-head { height: 60px; padding: 0 20px; display: flex; align-items: center;
               justify-content: space-between; border-bottom: 1px solid var(--line); flex: 0 0 auto; }
.drawer-body { padding: 20px; overflow: auto; flex: 1 1 auto; }
.drawer-foot { padding: 12px 20px; border-top: 1px solid var(--line);
               display: flex; justify-content: flex-end; gap: 8px; flex: 0 0 auto; }
```

A dialog is the same object centred: `max-width: 520px`, `border-radius: 12px`, same shadow, same scrim. Both close on scrim click and on Escape.

### Footer

Operational apps rarely need a marketing footer. Use a 40px panel footer instead: 1px top rule, 12px `--muted` on the left (count, sync state, "Updated 2m ago"), pagination or a "New item" ghost button on the right. On a settings or admin surface, a single 48px bar with product name, version and three text links is enough.

---

## Imagery

**No photography, no illustration.** The panels are the picture.

- Avatars are 24/32px circles filled `--well` with `--muted` semibold initials. A team stack overlaps them with a 2px `--surface` ring and a `+2` counter capsule.
- File and integration marks are 32px `--well` rounded squares with a 14px line icon in `--muted`.
- Icons are 16px, 1.5px stroke, `currentColor`, rounded caps. Never filled, never two-tone, never coloured except when they inherit a capsule's colour.
- Progress is a 6px `--well` track with an `--accent` fill and a 12px tabular label to its right.
- Empty states: a 40px `--well` rounded square holding one line icon, a 14/20 semibold line, a 13/18 `--muted` line, and one secondary button. No illustration.
- If a marketing surface needs a hero, use `image-recipe.md`: flat vector panels, violet `#5B2FD6`, one soft shadow.

---

## Do

1. Open detail as a right-docked drawer over a `rgba(11, 18, 32, 0.42)` scrim — never navigate the board away.
2. Keep exactly two elevations: flat with a 1px `#E4E7EC` border at rest, `0 12px 32px -8px rgb(11 18 32 / .18)` when floating.
3. Make kanban columns `#EFF1F3` wells holding white cards; the well is the column, the card is the work.
4. Let `#5B2FD6` be the only saturated colour on the screen, and use it only for interaction and selection.
5. Mark selection with a 2px accent left rule plus a 6% accent tint, so it survives a screenshot in greyscale.
6. Give every card a status capsule first, title second — state before subject.
7. Keep prose in the detail pane under 68 characters per line.
8. Let the board stay visible and scrolled where the user left it while the drawer is open.

## Don't

1. Don't blur the backdrop. `backdrop-filter` is not part of this style — dim it instead.
2. Don't push content sideways to make room for the drawer; it overlays.
3. Don't put a shadow on a resting card, a list row, or a column well.
4. Don't add a third elevation, a "hover lift", or a `translateY(-2px)` on cards.
5. Don't give the well a border — it is recessed fill, and a border on a well flattens the whole idea.
6. Don't introduce a second accent hue or tint capsules beyond the 10% wash.
7. Don't uppercase capsule labels or card titles; ALL-CAPS belongs to nav group headers and field labels only.
8. Don't use coloured avatar circles, emoji reactions, or brand logos — `#EFF1F3` initials only.
9. Don't stack more than two panels of chrome before the content; rail + list + detail is the ceiling.
