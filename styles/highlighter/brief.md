# Highlighter

**Lab notebook × neon marker**

Keep the page desaturated so a single chartreuse stroke reads as emphasis rather than decoration.

Highlighter is for products with an opinion — AI tooling, developer platforms, growth analytics, challenger fintech. The whole page is deliberately desaturated so that one fluorescent chartreuse reads as emphasis rather than decoration. Ration it: the moment the acid appears on more than a tenth of the screen, the effect dies.

---

## Palette

Every value below is sampled from the source shots listed at the foot of this
brief. Treat them as fixed — this style's coherence depends on the exact values,
not on approximations of them.

| Token | Value | Role |
|---|---|---|
| `--bg` | `#EDEFEA` | page ground — the base everything sits on |
| `--surface` | `#FFFFFF` | card and panel fill |
| `--ink` | `#0B0C08` | primary text — must hold 4.5:1 against `--bg` |
| `--muted` | `#70736A` | secondary text, labels, meta |
| `--line` | `#DFE2DA` | hairline borders and dividers |
| `--accent` | `#C3EC2E` | the single interactive/brand hue — ration it |
| `--accent_ink` | `#141600` | text colour on top of `--accent` fills |
| `--block` | `#1C1E18` | solid counterweight mass |
| `--block_ink` | `#F2F4EC` | text on top of `--block` |

```css
:root {
  --bg: #EDEFEA;
  --surface: #FFFFFF;
  --ink: #0B0C08;
  --muted: #70736A;
  --line: #DFE2DA;
  --accent: #C3EC2E;
  --accent_ink: #141600;
  --block: #1C1E18;
  --block_ink: #F2F4EC;
}
```

## Typography

**Stack**

```css
font-family: "Space Grotesk", "General Sans", "Aeonik", ui-sans-serif, -apple-system, "Segoe UI", Inter, sans-serif;
```

**Families —** Geometric sans with tight tracking (Space Grotesk, General Sans, Aeonik). Headlines set negative at -0.03em.

**Hierarchy —** Hero numeral 64/64 light or 72/72 · section 24/30 medium · body 14/21 regular · micro-caps 10/12 medium ALL-CAPS 0.1em. Oversized light-weight numerals are the signature — a metric should be able to fill a third of a card.

**Usage —** Let one huge numeral carry the hierarchy per card. Chartreuse never sets type — it sits *behind* type as a highlighter swipe, or fills a pill whose label is `--accent_ink`.

## Texture & effects

Flat, with one behaviour that defines the style: chartreuse is applied like a marker, not a fill. Use it as a short swipe behind a word (a skewed rectangle at 0 opacity change), as an underline 6px thick sitting behind the baseline, or as a solid pill. Solid charcoal `--block` cards provide the counterweight. No gradients, no glow — the acid does all the shouting.

## Layout & spacing

Moderate density with strong blocking. 8px scale, 20-24px card padding, 12-16px radius, occasional pill (999px). Cards alternate between white and solid `--block`. Folder-tab navigation — tabs that visually attach to the panel below — is the characteristic nav pattern. Charts render as open thin-arc gauges rather than filled donuts.

## Components

### Buttons

Primary is a solid `--accent` pill with `--accent_ink` label — never white text, which disappears on chartreuse. Secondary is a solid `--block` charcoal pill with `--block_ink` label. Ghost is a 1px `--line` outline with `--ink` label.

### Inputs & selects

White field, 1px `--line` border, 10px radius, 11px 14px padding. Focus swaps the border to `--ink` and adds a 3px `rgba(195,236,46,.45)` ring — the acid appears as a glow, not a fill.

### Nav / sidebar

Folder-tab navigation is the signature: tabs sit on the panel below and visually attach to it, with the active tab sharing the panel's fill and losing its bottom border. Collapse to a solid `--block` pill on mobile.

### Cards

Alternate white cards (1px `--line`) with solid `--block` charcoal cards carrying `--block_ink` text. The charcoal cards are the counterweight that lets the acid read.

### Tables

White rows, 1px `--line` rules, `--muted` tracked-caps headers. Highlight the active row with a 4px left rule in `--accent`, never a full-row fill.

### Chips & badges

Solid `--accent` pill with `--accent_ink` text for the emphatic case; otherwise a 1px `--line` outline chip with `--muted` text.

### Modals & drawers

White panel, 16px radius, `0 24px 60px -20px rgb(11 12 8 / .3)`, over a `rgba(11,12,8,.4)` dim. Header rule in `--line`.

### Footer

A solid `--block` charcoal band with `--block_ink` links and one `--accent` underline on the primary call to action.

## Imagery

Imagery is secondary to structure. Prefer product screenshots, diagrams and icons over decorative photography, and let the interface itself be the visual interest. Where an illustration is needed, keep it flat and schematic.

Generate hero and illustration assets with `image-recipe.md` in this directory —
it decouples the subject from the style, so any subject comes back on-style.

## Do

- Keep the ground desaturated so the chartreuse has something to work against
- Apply the acid like a marker — a swipe behind a word, a thick underline, a pill
- Let one oversized light-weight numeral carry each card's hierarchy
- Use solid charcoal blocks as the counterweight to the acid
- Render gauges as open thin arcs rather than filled donuts
- Set `--accent_ink` (near-black) on chartreuse fills, never white

## Don't

- Do not set type in chartreuse — it fails contrast at every body size
- Do not let the accent cover more than about a tenth of the screen
- Do not add a second bright hue; the acid must stay singular
- Do not use this for clinical, regulated or safety-critical products
- Do not rely on the accent alone to carry meaning — pair it with a label
- Do not soften the palette with pastels; the ground is grey, not tinted

---

## Fit

**Best for —** AI and automation products, developer tools with personality, growth and marketing analytics, fintech challengers, products targeting a younger technical audience.

**Avoid for —** healthcare and clinical software, government or regulated finance, luxury or heritage brands, accessibility-critical products where the accent would be relied on for meaning.

**Mood —** electric, current, confident, irreverent, technical.

**Proven on —** landing page, dashboard, mobile app, crm · desktop, mobile.

## Sources

Synthesised from 6 shots. All credit to the original designers:

- [AI SaaS Landing Page Design](https://dribbble.com/shots/27584703-AI-SaaS-Landing-Page-Design) — Mahid
- [Case Study for Squadhub - Saas Team Management Website](https://dribbble.com/shots/27578441-Case-Study-for-Squadhub-Saas-Team-Management-Website) — Plainthing Studio
- [AI SaaS Landing Page](https://dribbble.com/shots/26440808-AI-SaaS-Landing-Page) — Awsmd
- [CreditTB - Credit SaaS Dashboard](https://dribbble.com/shots/24070360-CreditTB-Credit-SaaS-Dashboard) — RonDesignLab ⭐️
- [SavingPro Mobile App - Savings SaaS Dashboard](https://dribbble.com/shots/24028927-SavingPro-Mobile-App-Savings-SaaS-Dashboard) — RonDesignLab ⭐️
- [Synetica SaaS CRM - AI Finance Dashboard](https://dribbble.com/shots/26460868-Synetica-SaaS-CRM-AI-Finance-Dashboard) — RonDesignLab ⭐️
