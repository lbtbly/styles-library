# Studio Object

**Industrial catalogue × single object**

A rendered object is the page; the interface shrinks to hairline pills docked around it.

Studio Object is for products with something physical at their centre — hardware, logistics, construction, manufacturing. A single matte render fills most of the frame and the interface shrinks to hairline pills docked around it. If there is nothing to render, this style has nothing to stand on.

---

## Palette

Every value below is sampled from the source shots listed at the foot of this
brief. Treat them as fixed — this style's coherence depends on the exact values,
not on approximations of them.

| Token | Value | Role |
|---|---|---|
| `--bg` | `#D6D6D6` | page ground — the base everything sits on |
| `--surface` | `#FFFFFF` | card and panel fill |
| `--ink` | `#050505` | primary text — must hold 4.5:1 against `--bg` |
| `--muted` | `#6E6E6E` | secondary text, labels, meta |
| `--line` | `#DCDCDC` | hairline borders and dividers |
| `--accent` | `#0079DE` | the single interactive/brand hue — ration it |
| `--accent_ink` | `#FFFFFF` | text colour on top of `--accent` fills |
| `--warm` | `#E09400` | single warm status note |

```css
:root {
  --bg: #D6D6D6;
  --surface: #FFFFFF;
  --ink: #050505;
  --muted: #6E6E6E;
  --line: #DCDCDC;
  --accent: #0079DE;
  --accent_ink: #FFFFFF;
  --warm: #E09400;
}
```

## Typography

**Stack**

```css
font-family: "Aeonik", "General Sans", ui-sans-serif, -apple-system, "Segoe UI", Inter, Helvetica, sans-serif;
```

**Families —** Neo-grotesque or geometric sans, weight-alternating within a single headline (one clause light, the next semibold).

**Hierarchy —** Headline 44/48 with mixed weights · body 15/23 regular · label 11/14 medium ALL-CAPS 0.1em · single display numeral up to 120px when the object is a metric.

**Usage —** Alternate weight inside one headline rather than using colour or size for emphasis. Keep all UI type small — the render should dominate.

## Texture & effects

The object is the page. A single matte 3D render — a sphere in liquid, an isometric building, a device — fills most of the frame, lit softly in a grey studio. UI reduces to hairline pill buttons and small floating micro-panels docked to the render, often with thin leader lines connecting a label to a point on the object. Surfaces are matte; no gloss, no neon.

## Layout & spacing

Composition over structure. The render occupies 60-75% of the viewport; content is docked to one edge or floats over a quiet area of the image. 8px scale, 999px radius on pills, 12px on micro-panels, 16px padding. Hairline leader lines (1px, `--line`) tie annotations to the object.

## Components

### Buttons

Hairline pills — 1px `--line` border, 999px radius, transparent fill, `--ink` label, 9px 18px padding. The primary version fills with `--ink` and takes `--surface` as its label colour. Buttons float over the render, so they stay small.

### Inputs & selects

1px `--line` border, 999px radius, `--surface` fill at 90% opacity, 10px 16px padding. Focus swaps the border to `--accent`.

### Nav / sidebar

A thin transparent bar with hairline-pill links, docked to the top edge over the render. Never a solid band — the render must run beneath it.

### Cards

Small floating micro-panels: `--surface`, 12px radius, 1px `--line`, `0 4px 16px -6px rgb(5 5 5 / .18)`, 16px padding. They annotate the object rather than containing the page.

### Tables

Compact specification tables — 1px `--line` rules, `--muted` tracked-caps labels in the left column, `--ink` values right-aligned. This style loves a spec sheet.

### Chips & badges

Hairline outline pills only, `--muted` text. The `--warm` amber version marks a single status and appears at most once per screen.

### Modals & drawers

A `--surface` panel with a 1px `--line` border and a soft shadow, over a lightly dimmed render. Keep the object visible behind it.

### Footer

A quiet hairline-separated row of links in `--muted` over flat `--bg`, with the render stopping short of it.

## Imagery

This style is image-led: a matte 3D render or staged object carries the composition and the UI is arranged around it. Keep renders matte and neutrally lit; the interface supplies structure, the render supplies presence.

Generate hero and illustration assets with `image-recipe.md` in this directory —
it decouples the subject from the style, so any subject comes back on-style.

## Do

- Give the render 60-75% of the viewport — it is the page
- Dock UI to one edge or into a quiet area of the image
- Alternate weight inside a single headline instead of using colour
- Use 1px leader lines to tie annotations to points on the object
- Keep every surface matte — no gloss, no chrome, no specular hits
- Hold at least 30% flat grey ground on one side for type

## Don't

- Do not use this when there is no object worth rendering
- Do not add coloured lighting — the studio is neutral
- Do not let UI cover the object's silhouette
- Do not use more than one small colour note in the whole composition
- Do not use dramatic contrast or hard shadows; the light is large and soft
- Do not fill the frame with text — this style is image-led by definition

---

## Fit

**Best for —** hardware and physical products, logistics, warehousing and supply chain, architecture and construction tech, manufacturing and industrial software, product launch and concept pages.

**Avoid for —** text-heavy applications, dense dashboards, products with no renderable object, fast-iterating marketing needing cheap assets.

**Mood —** industrial, precise, material, sober, engineered.

**Proven on —** landing page, mobile app, dashboard · desktop, mobile.

## Sources

Synthesised from 4 shots. All credit to the original designers:

- [Imagica clean SAAS design tool](https://dribbble.com/shots/21344417-Imagica-clean-SAAS-design-tool) — Gleb Kuznetsov ✈
- [Floware — Warehouse SaaS Platform Dashboard Website Landing Page](https://dribbble.com/shots/27246128-Floware-Warehouse-SaaS-Platform-Dashboard-Website-Landing-Page) — LAIN
- [Property Management Mobile SaaS](https://dribbble.com/shots/25614261-Property-Management-Mobile-SaaS) — RonDesignLab ⭐️
- [OptiSpace SaaS - Office Operating Dashboard](https://dribbble.com/shots/26530776-OptiSpace-SaaS-Office-Operating-Dashboard) — RonDesignLab ⭐️
