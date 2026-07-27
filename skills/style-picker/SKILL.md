---
name: style-picker
description: Pick and apply a visual style from the styles library for any app, website, or product artifact. Use when starting UI work with no fixed visual direction — "design a landing page for X", "make this look good", "pick a style for my dashboard", "what style suits a fintech app" — or when the user explicitly asks for a style recommendation. Selects a primary plus one alternate with rationale, then applies the chosen brief.
---

# Style picker

Choose a visual style from the library and apply it faithfully. The library is
filesystem-first: `styles/index.json` is the only file you must read to start.

## Resolving paths — do this before your first read

Every path below is relative to the **library root**, which is not your working
directory. When this skill is installed as a plugin, the root is
`${CLAUDE_PLUGIN_ROOT}` — so the index is at
`${CLAUDE_PLUGIN_ROOT}/styles/index.json`. When the library is a plain clone, the
root is the clone directory. A failed read means you resolved the root wrong, not
that the file is missing.

## 1. Establish the brief — at most 3 questions

You need five things. **Infer whatever you can from the request, the repo, and
any existing design tokens — only ask about what genuinely changes the answer,
and never ask more than three questions.**

| Input | How to infer it before asking |
|---|---|
| **Artifact** | The request usually says it: landing page, dashboard, pricing, auth, mobile app, data table. |
| **Device** | "app"/"mobile"/React Native → mobile. Otherwise desktop. |
| **Domain** | Product name, repo contents, existing copy. |
| **Audience** | Developers, operators, consumers, executives — usually implied by the domain. |
| **Brand adjectives** | Existing brand, README tone, or the user's own words. Absent any signal, this is the one worth asking. |
| **Content density** | Dashboards and tables are dense; marketing and onboarding are sparse. |

If the user gave a brand adjective and an artifact type, ask nothing. Just pick.

## 2. Filter, then rank

Read `<library-root>/styles/index.json`. Every entry carries `fit`, `surfaces`,
`keywords` and `swatch`.

**Filter — hard exclusions first:**

1. Drop any style whose `fit.avoid_for` matches the project. This is a veto, not
   a penalty.
2. If the target is mobile, prefer styles with `"mobile"` in `surfaces.devices`.
   Others can still work, but you must say you are extending beyond what is proven.

**Rank the survivors:**

| Signal | Weight |
|---|---|
| `fit.best_for` names the project type | highest |
| `fit.mood` overlaps the brand adjectives | high |
| `surfaces.artifacts` already includes this artifact type | medium — this is *proven*, not merely plausible |
| `keywords` match stated visual preferences | medium |
| Density fit: dense styles for dense screens | medium |

`surfaces.artifact_counts` tells you how much evidence backs each claim — a
style proven on eight dashboards is a safer dashboard bet than one proven on one.

## 3. Propose primary + alternate

Always offer exactly two, each with a one-line rationale naming the *specific*
field that drove it. Never present a bare list.

> **Primary — Hairline Ledger.** Its `best_for` covers analytics and BI tools, and
> the dense/precise mood matches the "serious, no-nonsense" brand you described.
>
> **Alternate — Panel Stack.** Same restraint but organised around a list-plus-detail
> spine; pick this instead if users spend more time on one record than scanning many.

Then proceed with the primary unless the user says otherwise. Do not wait for
permission to start when the request was "build me X".

## 4. Apply

1. **Read `<library-root>/styles/<id>/brief.md` in full and keep it in context.** It is written
   to be self-sufficient — palette table, type scale, texture implementation,
   component treatments, do/don't.
2. **Emit `tokens.palette` as CSS custom properties** at `:root`, using the exact
   hex values. They were sampled from real source shots; changing them breaks the
   style. Keep the token names so the artifact stays traceable to the style.
3. **Follow `tokens.type`** for family, scale and usage rules. The font stacks in
   `brief.md` include fallback chains that work without network access.
4. **Implement `tokens.texture` from the brief's code**, not from memory. Shadow
   values, gradients, blur radii and grain data-URIs are given literally.
5. **Read a preview before writing your own.** `<library-root>/styles/<id>/previews/*.html` are
   real artifacts in the style; they resolve ambiguity faster than prose. Pick the
   one closest to your artifact type.
6. **For hero or illustration assets**, use `<library-root>/styles/<id>/image-recipe.md`: fill the
   `[SUBJECT: …]` slot, keep every hard constraint verbatim, and keep the reserved
   negative space so real typography has somewhere to sit.
7. **Cite the choice** in your closing message: which style, and the one reason.

## 5. When nothing fits

Say so rather than forcing it. Two honest options:

- **Nearest style plus named deviations** — "Aura, but with the accent swapped to
  your brand green." Name every deviation explicitly so the artifact does not
  quietly drift from the library.
- **A new style** — if the project genuinely needs something the catalog lacks,
  note it. New styles come from the ingestion pipeline (`<library-root>/scripts/README.md`), not
  from improvisation.

## Traps

- **Do not blend two styles.** Their internal logic conflicts — Hairline Ledger's
  starved padding fights Soft Body's 24px gaps, and the result reads as neither.
  Pick one and deviate from it deliberately.
- **`avoid_for` is a veto.** A style whose `avoid_for` names your project will look
  wrong no matter how well its mood scores.
- **Density is not a preference, it is a constraint.** A style built for eight cards
  breaks when you put forty rows in it.
- **Accent colours are rationed on purpose.** Most of these styles work because one
  colour is scarce. Using the accent on every element destroys the style faster
  than getting the hex wrong.
- **Previews are proof, not templates.** Build an original artifact in the style;
  do not copy a preview's content.
