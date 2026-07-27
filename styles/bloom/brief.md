# Bloom

**Planetarium × keynote stage**

Colour arrives as light: feathered radial glow behind 1px-stroked cards on near-black.

Reach for Bloom when the product is technically ambitious and the page has to feel like a keynote. It suits AI platforms, infrastructure and anything where you want the visitor to feel they are looking at something engineered rather than assembled. It is a marketing register first — it will exhaust people who have to work in it all day.

---

## Palette

Every value below is sampled from the source shots listed at the foot of this
brief. Treat them as fixed — this style's coherence depends on the exact values,
not on approximations of them.

| Token | Value | Role |
|---|---|---|
| `--bg` | `#08080D` | page ground — the base everything sits on |
| `--surface` | `rgba(255, 255, 255, 0.03)` | card and panel fill |
| `--raised` | `#12121B` | elevated or floating surface |
| `--ink` | `#F4F4F7` | primary text — must hold 4.5:1 against `--bg` |
| `--muted` | `#9A9AAA` | secondary text, labels, meta |
| `--line` | `rgba(255, 255, 255, 0.10)` | hairline borders and dividers |
| `--accent` | `#5B57F0` | the single interactive/brand hue — ration it |
| `--accent_ink` | `#FFFFFF` | text colour on top of `--accent` fills |
| `--glow_a` | `#4A3FD8` | primary radial glow |
| `--glow_b` | `#B838C8` | secondary radial glow |

```css
:root {
  --bg: #08080D;
  --surface: rgba(255, 255, 255, 0.03);
  --raised: #12121B;
  --ink: #F4F4F7;
  --muted: #9A9AAA;
  --line: rgba(255, 255, 255, 0.10);
  --accent: #5B57F0;
  --accent_ink: #FFFFFF;
  --glow_a: #4A3FD8;
  --glow_b: #B838C8;
}
```

## Typography

**Stack**

```css
font-family: "Aeonik", "General Sans", "Satoshi", ui-sans-serif, -apple-system, "Segoe UI", Inter, sans-serif;
```

**Families —** Geometric sans (Aeonik, General Sans, Satoshi). Headlines set tight at -0.025em; italic is permitted for emphasis inside a headline.

**Hierarchy —** Hero 56/60 medium · section 32/38 medium · body 15/24 regular in `--muted` · micro-caps 10/12 medium ALL-CAPS 0.12em with a small bullet dot. Body text is deliberately grey, not white — only headlines get full `--ink`.

**Usage —** Sentence case headlines, tracked micro-caps as section eyebrows. Never set long body copy in pure white on black — it vibrates. Cap paragraph width at 62 characters.

## Texture & effects

Colour arrives as light, never as fill. Cards are defined by a 1px `rgba(255,255,255,.10)` stroke over an almost invisible 3% white fill — no solid card colours. Behind them, one or two large feathered radial gradients (`radial-gradient(60% 50% at 30% 0%, var(--glow-a) 0%, transparent 70%)`) bleed from an edge or from behind a 3D hero object. Add 2-4% noise over the whole page to stop the gradients banding.

## Layout & spacing

Modules butted edge to edge with hairline dividers and zero gutters, so the page reads as one continuous dark surface subdivided by light. 8px scale, 28-32px module padding, 14px radius. The hero object (a faceted, iridescent or chrome 3D form) is the only saturated mass; everything else is stroke and glow.

## Components

### Buttons

Primary is a solid `--accent` pill, 999px radius, 11px 22px padding, white label, with a soft `0 8px 24px -8px rgb(91 87 240 / .55)` bloom underneath. Secondary is transparent with a 1px `--line` stroke and `--ink` label — it must never gain a fill. Ghost is label-only in `--muted` with an arrow glyph.

### Inputs & selects

Transparent field with a 1px `--line` border, 10px radius, 10px 14px padding, `--ink` text and `--muted` placeholder. On focus the border becomes `--accent` and gains `box-shadow: 0 0 0 3px rgb(91 87 240 / .18)`. Never fill an input with a solid colour.

### Nav / sidebar

A transparent bar over the page with only a hairline bottom rule. Links are 14px `--muted`, going `--ink` on hover. The nav floats — it never gets a solid background, even on scroll; increase the backdrop blur instead.

### Cards

1px `--line` stroke over `--surface` (3% white). No solid fills. Butt cards edge to edge sharing borders so the page reads as one subdivided surface. 14px radius only on the outermost container.

### Tables

Rare in this style. If needed: no zebra striping, 1px `--line` row rules, `--muted` headers in tracked caps, figures in `--ink`.

### Chips & badges

Tracked ALL-CAPS 10px labels in `--muted` preceded by a 4px `--accent` bullet dot. No pill background — the dot plus the tracking is the badge.

### Modals & drawers

Centred panel at `--raised` with a 1px `--line` stroke, backed by `rgba(8,8,13,.7)` plus `backdrop-filter: blur(8px)`. Keep the page's glow visible through the scrim.

### Footer

Separated by a hairline, generous 80px+ padding, link columns in `--muted` with tracked caps headers, and the wordmark scaled large enough to crop at the viewport edge.

## Imagery

This style is image-led: a matte 3D render or staged object carries the composition and the UI is arranged around it. Keep renders matte and neutrally lit; the interface supplies structure, the render supplies presence.

Generate hero and illustration assets with `image-recipe.md` in this directory —
it decouples the subject from the style, so any subject comes back on-style.

## Do

- Let one or two big radial glows do all the colour work
- Define every card with a 1px white-alpha stroke, never a fill
- Keep body copy `--muted` grey — reserve pure `--ink` for headlines
- Add 2-4% noise over the page so gradients do not band
- Butt modules edge to edge with shared hairlines and no gutters
- Give the 3D hero object room — it is the only saturated mass allowed

## Don't

- Do not set long body copy in pure white on black — it vibrates
- Do not fill cards with a solid lighter grey; the stroke is the card
- Do not add a second accent hue — the glow already carries the colour
- Do not use this for a dense working dashboard people stare at for hours
- Do not let the glow touch the text it sits behind; keep contrast above 4.5:1
- Do not use hard rim lighting or lens flares — the light is soft and feathered

---

## Fit

**Best for —** AI and ML platforms, developer infrastructure, crypto and fintech, product launches and keynotes, premium technical positioning.

**Avoid for —** dense working dashboards used all day, healthcare and accessibility-first services, children's or education products, print-first or document-heavy tools.

**Mood —** cinematic, advanced, premium, atmospheric, engineered.

**Proven on —** landing page, dashboard, auth & onboarding · desktop.

## Sources

Synthesised from 7 shots. All credit to the original designers:

- [Constellation - AI SaaS Startup Platform Landing Page Website](https://dribbble.com/shots/26435909-Constellation-AI-SaaS-Startup-Platform-Landing-Page-Website) — LAIN
- [Saas Landing  page design](https://dribbble.com/shots/27540722-Saas-Landing-page-design) — theosm™
- [Dashboard for a Management SaaS ✦ Mytasky](https://dribbble.com/shots/25686392-Dashboard-for-a-Management-SaaS-Mytasky) — HALO LAB
- [SkyFort - Corporate Cyber Security SaaS Website Web Design](https://dribbble.com/shots/15711117-SkyFort-Corporate-Cyber-Security-SaaS-Website-Web-Design) — Phenomenon Studio
- [Constellation - AI SaaS Startup Product Platform About Website](https://dribbble.com/shots/26475403-Constellation-AI-SaaS-Startup-Product-Platform-About-Website) — LAIN
- [IdeaPilot AI - Onboarding design for AI-powered SaaS platform](https://dribbble.com/shots/24677624-IdeaPilot-AI-Onboarding-design-for-AI-powered-SaaS-platform) — Outcrowd
- [Landing Page (Saas Digital Marketing)](https://dribbble.com/shots/25679017-Landing-Page-Saas-Digital-Marketing) — Yoga V Wijaya
