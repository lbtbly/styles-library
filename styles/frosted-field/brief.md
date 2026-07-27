# Frosted Field

**Sea glass × gradient wash**

Carve every surface out of one pale gradient using translucency instead of borders or fills.

Frosted Field suits products people check rather than operate — finance, wellness, smart home, an AI assistant. Everything is carved out of one gradient, so the interface feels like a single continuous material. It is the wrong choice anywhere legibility is safety-critical, because translucency always costs contrast.

---

## Palette

Every value below is sampled from the source shots listed at the foot of this
brief. Treat them as fixed — this style's coherence depends on the exact values,
not on approximations of them.

| Token | Value | Role |
|---|---|---|
| `--bg` | `linear-gradient(155deg, #E8EAF8 0%, #DCE8…` | page ground — the base everything sits on |
| `--bg_solid` | `#E4E7EF` | flat fallback for the gradient ground |
| `--surface` | `rgba(255, 255, 255, 0.55)` | card and panel fill |
| `--raised` | `rgba(255, 255, 255, 0.78)` | elevated or floating surface |
| `--ink` | `#141620` | primary text — must hold 4.5:1 against `--bg` |
| `--muted` | `#5D6273` | secondary text, labels, meta |
| `--line` | `rgba(255, 255, 255, 0.60)` | hairline borders and dividers |
| `--accent` | `#5D51C8` | the single interactive/brand hue — ration it |
| `--accent_ink` | `#FFFFFF` | text colour on top of `--accent` fills |
| `--mint` | `#69C6AE` | secondary hue, charts and highlights |

```css
:root {
  --bg: linear-gradient(155deg, #E8EAF8 0%, #DCE8EC 48%, #E9E4F2 100%);
  --bg_solid: #E4E7EF;
  --surface: rgba(255, 255, 255, 0.55);
  --raised: rgba(255, 255, 255, 0.78);
  --ink: #141620;
  --muted: #5D6273;
  --line: rgba(255, 255, 255, 0.60);
  --accent: #5D51C8;
  --accent_ink: #FFFFFF;
  --mint: #69C6AE;
}
```

## Typography

**Stack**

```css
font-family: "Aeonik", "General Sans", "Outfit", ui-sans-serif, -apple-system, "Segoe UI", Inter, sans-serif;
```

**Families —** Geometric sans, light to regular (Aeonik, General Sans, Outfit). Low weight contrast.

**Hierarchy —** Title 22/28 regular · figure 34/38 light · body 14/21 regular · label 11/14 regular in `--muted`. Thin, wide-set type suits the soft ground.

**Usage —** Keep weights light — bold type fights the translucency. Sentence case. Labels sit above values, not beside them.

## Texture & effects

Every surface is carved out of the gradient rather than drawn on top of it: `background: rgba(255,255,255,.55); backdrop-filter: blur(24px);` with a 1px inner highlight `rgba(255,255,255,.6)` and no outer border. One blurred colour metaball (a 320px circle of `--accent` at 30% opacity, `filter: blur(80px)`) drifts behind the content to give the field variation. Shadows are wide and faint.

## Layout & spacing

Soft and generous. 8px scale, 24px padding, 20-24px radius on cards, 999px on every control. Because nothing has a border, rely on 20px+ gaps for separation. Charts render as translucent gradient-filled bars or dot matrices, never as hard strokes.

## Components

### Buttons

Primary is a solid `--accent` pill, 999px radius, 11px 22px, white label. Secondary is a frosted pill: `rgba(255,255,255,.5)` with `backdrop-filter: blur(16px)` and a 1px `rgba(255,255,255,.6)` inner highlight — no outer border. Ghost is label-only in `--muted`.

### Inputs & selects

Frosted capsule — `rgba(255,255,255,.45)`, `backdrop-filter: blur(16px)`, 999px radius, no border, 11px 18px padding. Focus lifts opacity to .72 and adds a 2px `--accent` ring.

### Nav / sidebar

A floating frosted capsule bar inset 16px from the top, not a full-width band. Sidebar items are frosted pills when active and plain `--muted` labels when not.

### Cards

`rgba(255,255,255,.55)` + `backdrop-filter: blur(24px)`, 20-24px radius, a 1px `rgba(255,255,255,.6)` inset highlight along the top edge, no outer border. Separation comes from 20px+ gaps, never from strokes.

### Tables

Avoid true tables. Use spaced rows on a single frosted card with 1px `rgba(255,255,255,.45)` dividers and generous 14px row padding.

### Chips & badges

Fully rounded, `rgba(255,255,255,.6)` frosted, `--muted` label. The accent version fills with `--accent` at 14% and takes `--accent` as its text colour.

### Modals & drawers

A heavier frost — `rgba(255,255,255,.78)` with `blur(40px)` — over a lightly dimmed field. The gradient must stay perceptible through it.

### Footer

Minimal: a frosted capsule row of links centred at the bottom, or nothing at all. This style dislikes heavy footers.

## Imagery

Imagery is atmospheric rather than literal: gradients, glows and abstract forms. Any photographic or rendered element should be the single saturated mass on the page, with everything else reduced to stroke and light.

Generate hero and illustration assets with `image-recipe.md` in this directory —
it decouples the subject from the style, so any subject comes back on-style.

## Do

- Carve every surface out of the gradient with translucency, never with a border
- Keep one blurred colour metaball drifting behind the content for variation
- Set type light — bold weights fight the softness
- Use 20px+ gaps as the separator, since nothing has an edge
- Render charts as translucent gradient fills or dot matrices
- Check contrast on every frosted surface; raise opacity before you darken the ink

## Don't

- Do not put hard 1px outer borders on frosted cards — only inner highlights
- Do not stack more than two translucent layers; the third turns to mud
- Do not use this for dense tables or anything with forty rows
- Do not introduce a third hue beyond the violet and the seafoam
- Do not use pure white or pure black anywhere in the palette
- Do not let a blurred metaball sit directly behind body copy

---

## Fit

**Best for —** fintech and personal finance, wellness and health tracking, smart home and IoT, AI assistants and copilots, consumer dashboards.

**Avoid for —** high-density enterprise tables, developer tools, accessibility-critical services (translucency hurts legibility), print or export-heavy products.

**Mood —** serene, contemporary, soft, optimistic, light.

**Proven on —** dashboard, crm, mobile app, design tool · desktop, mobile.

## Sources

Synthesised from 7 shots. All credit to the original designers:

- [Sugar CRM - SaaS Dashboard & UX UI Design](https://dribbble.com/shots/26629031-Sugar-CRM-SaaS-Dashboard-UX-UI-Design) — RonDesignLab ⭐️
- [ShipLens SaaS – AI Shipment Management Platform](https://dribbble.com/shots/27136565-ShipLens-SaaS-AI-Shipment-Management-Platform) — RonDesignLab ⭐️
- [Orriso Dashboard – AI Workspace SaaS](https://dribbble.com/shots/26702934-Orriso-Dashboard-AI-Workspace-SaaS) — RonDesignLab ⭐️
- [WindFarm SaaS - Renewable Energy Dashboard](https://dribbble.com/shots/25432271-WindFarm-SaaS-Renewable-Energy-Dashboard) — RonDesignLab ⭐️
- [Synthex UI – Analytics SaaS Dashboard](https://dribbble.com/shots/27131881-Synthex-UI-Analytics-SaaS-Dashboard) — RonDesignLab ⭐️
- [LoopAI – CRM Dashboard for B2B SaaS](https://dribbble.com/shots/25961490-LoopAI-CRM-Dashboard-for-B2B-SaaS) — Phenomenon Studio
- [Dashboard for a Finance SaaS ✦ FundFlow](https://dribbble.com/shots/24828700-Dashboard-for-a-Finance-SaaS-FundFlow) — HALO LAB
