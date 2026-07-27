# Poster Block

**Silkscreen poster × brand board**

Edge-to-edge colour bands and display caps — the page behaves like a printed poster, not a screen.

Poster Block is for work that should feel printed — campaign sites, studios, events, community marketplaces. The page is a stack of flat colour bands with an enormous display headline, and the ink is a chosen brand colour rather than black. It has no business anywhere near a dashboard.

---

## Palette

Every value below is sampled from the source shots listed at the foot of this
brief. Treat them as fixed — this style's coherence depends on the exact values,
not on approximations of them.

| Token | Value | Role |
|---|---|---|
| `--bg` | `#FBFBEF` | page ground — the base everything sits on |
| `--surface` | `#FFFFFF` | card and panel fill |
| `--ink` | `#2E2440` | primary text — must hold 4.5:1 against `--bg` |
| `--muted` | `#6E667E` | secondary text, labels, meta |
| `--line` | `#DEDACF` | hairline borders and dividers |
| `--accent` | `#F5CE3E` | the single interactive/brand hue — ration it |
| `--accent_ink` | `#3A2E10` | text colour on top of `--accent` fills |
| `--band_a` | `#0F6B4C` | flat band colour |
| `--band_b` | `#D96A5E` | flat band colour |
| `--band_c` | `#C9D8B0` | flat band colour |

```css
:root {
  --bg: #FBFBEF;
  --surface: #FFFFFF;
  --ink: #2E2440;
  --muted: #6E667E;
  --line: #DEDACF;
  --accent: #F5CE3E;
  --accent_ink: #3A2E10;
  --band_a: #0F6B4C;
  --band_b: #D96A5E;
  --band_c: #C9D8B0;
}
```

## Typography

**Stack**

```css
font-family: "Anton", "Archivo Black", "Bricolage Grotesque", "Haettenschweiler", "Arial Narrow Bold", ui-sans-serif, sans-serif;
```

**Families —** A condensed or expressive display face for headlines (Anton, Archivo Expanded, Bricolage Grotesque, PP Right Grotesk) with a plain geometric sans for body. The display face should be strange enough to be memorable.

**Hierarchy —** Poster headline 96/88 display, justified to the full column width · section 32/36 display · body 16/25 sans · label 12/15 sans medium ALL-CAPS 0.06em.

**Usage —** Set the headline enormous and justify it edge to edge — the type is a graphic element, not a label. Ink is a chosen brand colour (deep aubergine, chocolate, forest), never plain black.

## Texture & effects

Print, not screen. Flat colour bands with hard edges, zero shadows, zero gradients. Optional paper grain at 4%. Shapes are cut with jagged, zigzag or arc section dividers rather than straight rules. Cut-out photography and mascot illustration overlap and interrupt the type.

## Layout & spacing

Edge-to-edge horizontal bands, each a different flat colour, stacked down the page. No card floats above another — everything is inline in its band. 8px scale, 0-8px radius (sharp is the default), 64-96px band padding. Elements deliberately break their band's boundary to create energy.

## Components

### Buttons

Sharp or barely-rounded rectangles (0-6px), solid `--accent` with `--accent_ink` label, no shadow. Secondary is a 2px `--ink` outline with a transparent fill. Buttons are chunky — 14px 26px padding minimum.

### Inputs & selects

2px `--ink` border, 0-4px radius, transparent fill, `--ink` text. Focus thickens the border to 3px. Nothing is soft here.

### Nav / sidebar

A simple horizontal row of links in the band's own ink colour, tracked slightly, with the active item underlined 3px. The nav sits inside the top band — it never floats over it.

### Cards

Flat colour rectangles inline in their band. No shadow, no border, no radius beyond 8px. Cards may deliberately overhang their band's edge to break the grid.

### Tables

Set as a print table: 2px rules above and below the header, 1px between rows, `--ink` text, no fills.

### Chips & badges

Flat rectangles or hard-edged pills in a band colour with contrasting ink. No tints, no transparency.

### Modals & drawers

A solid flat panel in a band colour filling most of the viewport, hard-edged, with a large close glyph. No scrim blur.

### Footer

A final full-bleed band in the darkest palette colour, carrying the wordmark set enormous and cropped by the viewport edge.

## Imagery

Imagery is secondary to structure. Prefer product screenshots, diagrams and icons over decorative photography, and let the interface itself be the visual interest. Where an illustration is needed, keep it flat and schematic.

Generate hero and illustration assets with `image-recipe.md` in this directory —
it decouples the subject from the style, so any subject comes back on-style.

## Do

- Stack edge-to-edge flat colour bands down the page
- Set the headline enormous and justify it to the full column width
- Use a brand ink (aubergine, forest, chocolate) instead of plain black
- Let cut-out photography and illustration overlap and interrupt the type
- Cut bands apart with zigzag, arc or angled dividers rather than straight rules
- Add a 4% paper grain so the flat colour reads as printed

## Don't

- Do not use drop shadows — nothing floats in this style
- Do not use gradients; every colour is a flat spot colour
- Do not use this for dashboards, tables or any dense working UI
- Do not round corners heavily — sharp is the default
- Do not use pure black for text; the ink is always a chosen hue
- Do not centre everything — asymmetry and overhang give the page its energy

---

## Fit

**Best for —** brand identity and campaign sites, creative agencies and studios, events and conferences, community and marketplace products, anything wanting personality over polish.

**Avoid for —** enterprise software, dashboards and data tools, regulated finance or healthcare, products needing a neutral canvas for user content.

**Mood —** bold, playful, graphic, characterful, confident.

**Proven on —** landing page, dashboard, branding board · desktop.

## Sources

Synthesised from 5 shots. All credit to the original designers:

- [SaaS Marketplace Platform Website | Branding](https://dribbble.com/shots/23694117-SaaS-Marketplace-Platform-Website-Branding) — Voila
- [Team Management Saas UIUX](https://dribbble.com/shots/27239425-Team-Management-Saas-UIUX) — Fahema Yesmin
- [SaaS Platform Landing Page for Startups](https://dribbble.com/shots/26661002-SaaS-Platform-Landing-Page-for-Startups) — Ronas IT | UI/UX Team
- [CyberGuard - Cybersecurity SaaS  Dashboard](https://dribbble.com/shots/25341116-CyberGuard-Cybersecurity-SaaS-Dashboard) — RonDesignLab ⭐️
- [Saas Website Design / Branding](https://dribbble.com/shots/27329813-Saas-Website-Design-Branding) — Julien Renvoye
