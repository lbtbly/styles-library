# Cinema Glass

**Pairing:** Film still × frosted pane
**Concept:** Full-bleed imagery seen through dark blurred glass, with chrome reduced to floating pills.

Cinema Glass is for products where the **image is the product**: video and media tools,
travel and hospitality, premium consumer apps, brand campaign pages, creative tools with a
visual output. The whole interface is a sheet of dark glass laid over a photograph — the
picture runs edge to edge, and every panel, control and label floats translucent above it
so you never lose sight of what is underneath.

It is a demanding style. It needs a real imagery budget and it trades legibility for
atmosphere. Do not use it for data-dense dashboards, enterprise administration,
accessibility-critical services, or any product that cannot afford good pictures — with a
weak image behind it, the glass has nothing to be glass *over* and the whole thing collapses
into grey mush.

---

## Palette

Only four fixed hex values exist. Everything else is white or near-black at a stated alpha,
because translucency — not colour — is what carries this style.

| Token | Value | Role | Where it may appear |
|---|---|---|---|
| `bg` | `#000000` | True black ground | Behind the image, letterbox bars, page background, the safety colour under any failed image load. |
| `surface` | `rgba(24, 24, 24, 0.55)` | Dark glass panel | Glass cards, control panels, drawers, nav bars, modals. Always paired with `backdrop-filter`. |
| `raised` | `rgba(255, 255, 255, 0.10)` | Light glass | Pills, icon buttons, chips, secondary buttons, input fields, hover states, scrub-track fill. |
| `ink` | `#FFFFFF` | Primary text & icons | Headlines, control labels, active icons, the one white circular play button. |
| `muted` | `rgba(255, 255, 255, 0.66)` | Secondary text | Body copy, inactive nav, captions, helper text, inactive icons. Body copy sits here, not at full white. |
| `line` | `rgba(255, 255, 255, 0.14)` | Inner stroke | The 1px hairline on every glass surface, divider rules, chip outlines. |
| `accent` | `#D9E82A` | The single hot note | Exactly one thing per screen: the active pill, the progress fill, the current timeline marker, the primary CTA. |
| `accent_ink` | `#171A00` | Text on accent | Label colour on top of a `#D9E82A` fill. Nowhere else. |

The accent is acid yellow-green and it is loud. **One accent element per viewport.** If the
primary button is accent, the progress bar is white. If the timeline playhead is accent, the
buttons are glass.

```css
:root {
  --bg:         #000000;
  --surface:    rgba(24, 24, 24, 0.55);
  --raised:     rgba(255, 255, 255, 0.10);
  --ink:        #FFFFFF;
  --muted:      rgba(255, 255, 255, 0.66);
  --line:       rgba(255, 255, 255, 0.14);
  --accent:     #D9E82A;
  --accent-ink: #171A00;
}
```

---

## Typography

```css
--font-sans:  "Inter", "Neue Haas Grotesk", -apple-system, BlinkMacSystemFont,
              "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
--font-serif: "Playfair Display", "Didot", "Bodoni MT", "Times New Roman", Georgia, serif;
--font-mono:  "IBM Plex Mono", ui-monospace, SFMono-Regular, "SF Mono",
              Menlo, Consolas, "Liberation Mono", monospace;
```

| Role | Size / line-height | Weight | Family | Colour |
|---|---|---|---|---|
| Hero headline | 52px / 58px (clamp to 30px mobile) | 400 | sans, `letter-spacing:-.02em` | `--ink` |
| Hero italic clause | same size, +2% | 400 | **serif italic** | `--ink` |
| Section headline | 32px / 38px | 400 | sans | `--ink` |
| Card title | 17px / 23px | 500 | sans | `--ink` |
| Body | 15px / 23px | 400 | sans | `--muted` |
| Control label | 12px / 16px | 500 | sans | `--ink` |
| Metadata, timecode | 11px / 14px | 400 | mono, `letter-spacing:.06em` | `--muted` |
| Eyebrow / chip | 11px / 14px | 500 | sans, `letter-spacing:.10em`, uppercase | `--muted` |

**Usage rules**

- **The signature move**: a grotesque headline that breaks mid-line into an italic display
  serif for exactly one clause. `Nights you will <em>never quite</em> describe.` One break
  per page, in the hero only. Never two.
- All chrome type stays small and quiet — 12px labels, 11px mono metadata. The image carries
  the frame; type is a caption on it.
- Body copy runs at `--muted` (66% white), not full white. Full white is reserved for
  headlines, control labels and active state.
- Uppercase only for eyebrows and chips, always with `letter-spacing: .10em`.
- Monospace for timecodes, durations, coordinates, ISO codes, resolutions, prices per night.
- Never set type directly on a bright part of the image — either move it to the dark third
  or put it on glass.

---

## Texture & effects

**The glass panel** — the one component everything else is built from:

```css
.glass {
  background: rgba(24, 24, 24, 0.55);
  backdrop-filter: blur(28px) saturate(120%);
  -webkit-backdrop-filter: blur(28px) saturate(120%);
  border: 1px solid rgba(255, 255, 255, 0.14);
  border-radius: 22px;
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.10),
              0 18px 50px rgba(0, 0, 0, 0.45);
}
```

The `inset 0 1px 0` top highlight is what sells it as a physical pane. Light glass (pills,
chips, inputs) swaps the fill for `rgba(255,255,255,.10)` and drops the blur to `16px`.

**Never place a solid opaque panel over the image.** If a surface needs to be more readable,
raise the scrim under it — do not raise its own opacity past `0.72`.

**The scrim** — how you make type legible without killing the picture:

```css
.scrim-bottom {
  position: absolute; inset: 0; pointer-events: none;
  background: linear-gradient(to top,
    rgba(0,0,0,.88) 0%, rgba(0,0,0,.62) 22%, rgba(0,0,0,.20) 48%, rgba(0,0,0,0) 72%);
}
```

**Grain** — 4–6%, applied once over the whole composite so image and chrome share a surface:

```css
.grain::after {
  content: ""; position: fixed; inset: 0; pointer-events: none; z-index: 90;
  opacity: .05; mix-blend-mode: overlay;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='160' height='160'%3E%3Cfilter id='g'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.85' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='160' height='160' filter='url(%23g)'/%3E%3C/svg%3E");
  background-size: 160px 160px;
}
```

**Vignette** — always, it is what makes a screen read as a frame:

```css
.vignette { position:absolute; inset:0; pointer-events:none;
  background: radial-gradient(ellipse 120% 90% at 50% 45%,
              rgba(0,0,0,0) 38%, rgba(0,0,0,.55) 78%, rgba(0,0,0,.85) 100%); }
```

**Building a "photograph" from CSS when you have no image file.** This is a required skill
for this style — an offline artifact still has to look like a film still. Layer, back to
front:

1. **Base** `background: #000000`.
2. **Sky / field gradient** — one `linear-gradient` establishing the exposure, kept dark
   (nothing above ~35% lightness).
3. **Key light** — a single large off-centre radial:
   `radial-gradient(circle 46vw at 72% 34%, rgba(217,232,42,.30), rgba(150,120,40,.10) 40%, transparent 70%)`.
   One source only. Cinema Glass images are single-key.
4. **Atmosphere** — two or three very wide, very soft elliptical radials at 6–14% white to
   make haze bands.
5. **Silhouettes** — inline SVG paths in `#000` / `#050607` for ridges, foliage, a figure,
   architecture. Give distant layers `opacity:.55` and `filter: blur(1.5px)`, near layers
   full black and sharp. Three depth planes is enough to read as real.
6. **Light shafts** (optional) — skewed `linear-gradient` strips at 4–8% white,
   `mix-blend-mode: screen`.
7. **Vignette**, then **grain**.

Desaturate everything except the key light. The image should read as one colour plus black.

Forbidden: bright even lighting, white or light backgrounds, flat vector illustration,
multiple saturated hues, drop shadows with colour, hard borders on panels, opaque cards
over the image.

---

## Layout & spacing

- **The image is the layout.** Start from a full-bleed picture and subtract: chrome is what
  is left after you protect the subject.
- **8px base scale.** Glass card padding 16px (20px on large cards); page gutters 24px
  desktop, 16px mobile.
- **Radii:** 999px on every control, pill and chip; 18–24px on glass cards; 28–32px on a
  full-width bottom dock or a phone frame.
- **Content sits in the lower third or along one edge — never centred over the subject.**
  Hero copy bottom-left; controls bottom dock; metadata top-right; nav a floating pill at
  top-centre.
- Max content width 1180px, but the image always bleeds to 100vw.
- **Density is low.** A screen holds one headline, one paragraph, two actions, and a strip
  of metadata. If you are stacking six cards, you have picked the wrong style.
- Gaps between floating elements are 12–16px; they must not touch. Floating means floating.
- Safe area: keep 24px minimum between any glass edge and the viewport edge, so the picture
  is visible around everything.

---

## Components

### Buttons

```css
.btn { font:500 12px/16px var(--font-sans); border-radius:999px; padding:11px 20px;
       border:1px solid transparent; cursor:pointer; display:inline-flex; align-items:center; gap:8px; }

.btn--primary { background: var(--accent); color: var(--accent-ink); }

.btn--secondary { background: var(--raised); color: var(--ink);
  border-color: var(--line); backdrop-filter: blur(16px); -webkit-backdrop-filter: blur(16px); }

.btn--ghost { background: transparent; color: var(--muted); }
.btn--ghost:hover { color: var(--ink); }

/* the media-control exception: one solid white circle, always */
.btn--play { width:56px; height:56px; padding:0; border-radius:999px;
  background: var(--ink); color: #000000; justify-content:center; }
```

### Inputs & selects

```css
.input, .select {
  background: var(--raised); color: var(--ink); border: 1px solid var(--line);
  border-radius: 999px; padding: 12px 18px; font: 400 14px/20px var(--font-sans);
  backdrop-filter: blur(16px); -webkit-backdrop-filter: blur(16px); width: 100%;
}
.input::placeholder { color: var(--muted); }
.input:focus { outline: none; border-color: rgba(255,255,255,.38); }
```

Search fields are pills with a 16px monoline icon inset left. A composite search bar
(destination · dates · guests) is one glass pill split by 1px `--line` dividers, with the
submit control as an accent circle at its right end.

### Nav / sidebar

- **Top nav** is a floating pill, not a bar: centred, `--surface` glass, 999px radius, 8px
  padding, 12px links in `--muted` with the active link in `--ink` on a `--raised` pill.
- **Icon rail** (media apps) is a vertical stack of 44px glass circles docked to the left
  edge, 12px apart; the active one is solid `--ink` with a black glyph.
- Logo is a 15px wordmark in `--ink`, letter-spaced `-.01em`. No logo lockup boxes.

### Cards

```html
<article class="glass card">
  <span class="eyebrow">CHAPTER 04</span>
  <h3 class="card__title">The long crossing</h3>
  <p class="card__body">Shot over eleven nights in the Hebrides with a single lamp.</p>
  <footer class="card__meta"><span class="mono">12:41</span><span class="mono">4K · HDR</span></footer>
</article>
```

Cards are glass, 22px radius, 16px padding, and they **overlap the image edge** rather than
sitting in a tidy grid. Where a card needs its own picture, use it as the card's background
with an inset scrim and put the type over the bottom.

### Tables

Tables are rare here and should be as light as possible: no fills, no zebra, rows separated
by 1px `--line`, header row in 11px uppercase `--muted` with `letter-spacing:.10em`, numbers
in mono, right-aligned. Wrap in a glass panel so it still floats.

```css
.table td { padding:14px 12px; border-bottom:1px solid var(--line); color:var(--ink); font-size:14px; }
.table th { padding:10px 12px; border-bottom:1px solid var(--line);
            font:500 11px/14px var(--font-sans); letter-spacing:.10em;
            text-transform:uppercase; color:var(--muted); text-align:left; }
```

### Chips & badges

```css
.chip { display:inline-flex; align-items:center; gap:6px; padding:6px 12px; border-radius:999px;
        font:500 11px/14px var(--font-sans); letter-spacing:.06em;
        background:var(--raised); border:1px solid var(--line); color:var(--muted);
        backdrop-filter:blur(16px); -webkit-backdrop-filter:blur(16px); }
.chip--on { background: var(--accent); border-color: var(--accent); color: var(--accent-ink); }
```

A live indicator is a 6px `--accent` dot inside a glass chip — never a red dot.

### Modals & drawers

Prefer a **bottom dock** or a **bottom sheet** over a centred modal: a full-width glass slab
with a 28px top radius, docked to the bottom edge, 20px padding. If a centred modal is
required: 640px max width, 24px radius, `--surface` glass, and a scrim of
`rgba(0,0,0,.55)` **with** `backdrop-filter: blur(6px)` — here the blur on the scrim is
correct, because the whole style is about looking through things.

### Footer

Marketing surfaces end with the image still running behind: a 1px `--line` top rule, three
columns of 13px `--muted` links, a 15px wordmark, and an 11px mono legal line. No solid
footer slab, no colour change — the picture continues to the bottom of the document.

---

## Imagery

**Imagery is not decoration here; it is the substrate.** Every screen starts with a
full-bleed picture and the UI is composited onto it.

- **Treatment:** dark overall exposure, single strong light source, deep shadows that retain
  detail, desaturated except one hot note near `#D9E82A`, visible fine grain, wide framing
  with the subject off-centre.
- **Crop:** the subject sits in the upper two-thirds and off the centre line. The lower third
  is deliberately dark and empty so glass and type have somewhere to live.
- **Always** apply the bottom scrim, the vignette and the global grain — an untreated
  photograph will not sit with the chrome.
- Generate hero imagery with `image-recipe.md`; keep every hard constraint verbatim.
- **Never** use bright, evenly-lit, smiling stock photography. Never place an image inside a
  bordered frame — images bleed.
- Icons are 16–20px monoline strokes at `stroke-width: 1.5`, `--muted` idle, `--ink` active.
- **No photography available?** Build the still in CSS with the seven-layer recipe in
  *Texture & effects*. An offline artifact in this style must still read as atmospheric
  imagery — a flat dark rectangle is a failed implementation.

---

## Do

- Bleed the image to all four edges and keep it visible around every floating element.
- Make every panel translucent with `backdrop-filter` and a 1px `rgba(255,255,255,.14)` stroke.
- Break the hero headline into italic display serif for exactly one clause.
- Keep chrome type at 11–12px so the picture stays the loudest thing on screen.
- Ration `#D9E82A` to one element per viewport.
- Push content into the lower third or one edge; leave the subject uncovered.
- Apply the scrim, the vignette and 4–6% grain to every composition.
- Use 999px radii on controls and 18–24px on glass cards, consistently.
- Set body copy at 66% white, reserving `#FFFFFF` for headlines and active state.

## Don't

- Don't put an opaque panel over the image — if it needs contrast, deepen the scrim instead.
- Don't centre a headline over the subject of the photograph.
- Don't use more than one accent element, and never use `#D9E82A` for body text.
- Don't introduce a second hue; this palette is black, white-at-alpha, and one acid yellow.
- Don't use light or white backgrounds anywhere, including modals and empty states.
- Don't square off controls — every button, chip and input is a pill.
- Don't stack dense data; if the screen needs a table of twenty rows, change style.
- Don't use bright evenly-lit stock photography, or frame images in borders.
- Don't skip the grain — it is what fuses image and chrome into one surface.
- Don't use more than one serif italic break per page.
