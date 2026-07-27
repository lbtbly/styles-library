#!/usr/bin/env python3
"""Render brief.md and image-recipe.md from style.json + sources/brief-extras.json.

Generated briefs stay in lockstep with the tokens, which is what the validator's
style-drift check is looking for. Hand-written briefs are never overwritten
unless --force is passed.

  python3 scripts/build_brief.py                 # fill in anything missing
  python3 scripts/build_brief.py <id> [<id>...]  # specific styles
  python3 scripts/build_brief.py --force <id>    # overwrite an existing brief
"""
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load(*p):
    return json.load(open(os.path.join(ROOT, *p), encoding="utf-8"))


def hexes(pal):
    return {k: v for k, v in pal.items() if isinstance(v, str) and v.startswith("#")}


def brief_md(s, x):
    pal = s["tokens"]["palette"]
    t = s["tokens"]["type"]

    rows = "\n".join(
        f"| `--{k}` | {'`' + v + '`' if len(v) < 44 else '`' + v[:41] + '…`'} | {role(k)} |"
        for k, v in pal.items()
    )
    css = "\n".join(f"  --{k}: {v};" for k, v in pal.items())

    comp = "\n\n".join(f"### {k}\n\n{v}" for k, v in x["components"].items())
    do = "\n".join(f"- {d}" for d in x["do"])
    dont = "\n".join(f"- {d}" for d in x["dont"])

    return f"""# {s['name']}

**{s['pairing']}**

{s['concept']}

{x['for']}

---

## Palette

Every value below is sampled from the source shots listed at the foot of this
brief. Treat them as fixed — this style's coherence depends on the exact values,
not on approximations of them.

| Token | Value | Role |
|---|---|---|
{rows}

```css
:root {{
{css}
}}
```

## Typography

**Stack**

```css
font-family: {x['font_stack']};
```

**Families —** {t['families']}

**Hierarchy —** {t['hierarchy']}

**Usage —** {t['usage']}

## Texture & effects

{s['tokens']['texture']}

## Layout & spacing

{s['tokens']['layout']}

## Components

{comp}

## Imagery

{imagery(s)}

Generate hero and illustration assets with `image-recipe.md` in this directory —
it decouples the subject from the style, so any subject comes back on-style.

## Do

{do}

## Don't

{dont}

---

## Fit

**Best for —** {', '.join(s['fit']['best_for'])}.

**Avoid for —** {', '.join(s['fit']['avoid_for'])}.

**Mood —** {', '.join(s['fit']['mood'])}.

**Proven on —** {', '.join(s['surfaces']['artifacts'])} · {', '.join(s['surfaces']['devices'])}.

## Sources

Synthesised from {len(s['sources'])} shots. All credit to the original designers:

{chr(10).join('- [' + src['title'] + '](' + src['shot_url'] + ') — ' + src['designer'] for src in s['sources'])}
"""


ROLE = {
    "bg": "page ground — the base everything sits on",
    "bg_solid": "flat fallback for the gradient ground",
    "surface": "card and panel fill",
    "subtle": "recessed or secondary fill",
    "well": "recessed column/well fill",
    "raised": "elevated or floating surface",
    "stage": "presentation environment behind the UI, not a UI surface",
    "ink": "primary text — must hold 4.5:1 against `--bg`",
    "muted": "secondary text, labels, meta",
    "line": "hairline borders and dividers",
    "accent": "the single interactive/brand hue — ration it",
    "accent_ink": "text colour on top of `--accent` fills",
    "accent_soft": "tinted wash of the accent",
    "positive": "success, growth, upward delta",
    "negative": "error, loss, downward delta",
    "warning": "caution state",
    "warn": "caution state",
    "scrim": "dim layer behind modals and drawers",
    "block": "solid counterweight mass",
    "block_ink": "text on top of `--block`",
    "control": "solid control fill (buttons, circular actions)",
    "control_ink": "text/icon on top of `--control`",
    "ai": "reserved for AI-generated affordances only",
    "dot": "canvas dot-grid colour",
    "glow_a": "primary radial glow",
    "glow_b": "secondary radial glow",
    "bloom_a": "primary atmospheric bloom",
    "bloom_b": "secondary atmospheric bloom",
    "mint": "secondary hue, charts and highlights",
    "deep": "deep accent for emphasis",
    "warm": "single warm status note",
    "band_a": "flat band colour",
    "band_b": "flat band colour",
    "band_c": "flat band colour",
    "chip_tints": "tint recipe for status chips",
    "pastels": "pastel chip set",
}


def role(k):
    return ROLE.get(k, "supporting colour")


def imagery(s):
    kws = " ".join(s["keywords"]).lower()
    if "3d" in kws or "render" in kws:
        return ("This style is image-led: a matte 3D render or staged object carries the "
                "composition and the UI is arranged around it. Keep renders matte and neutrally "
                "lit; the interface supplies structure, the render supplies presence.")
    if "photo" in kws or "imagery" in kws or "film" in kws:
        return ("Photography is structural here, not decorative — it fills the frame and the "
                "interface floats over it. Choose images with a quiet, low-contrast region where "
                "type and controls can sit, and never place opaque panels over the subject.")
    if "glow" in kws or "bloom" in kws or "gradient" in kws:
        return ("Imagery is atmospheric rather than literal: gradients, glows and abstract forms. "
                "Any photographic or rendered element should be the single saturated mass on the "
                "page, with everything else reduced to stroke and light.")
    return ("Imagery is secondary to structure. Prefer product screenshots, diagrams and icons over "
            "decorative photography, and let the interface itself be the visual interest. Where an "
            "illustration is needed, keep it flat and schematic.")


def recipe_md(s, name):
    r = s["image_recipe"]
    cons = "\n".join(f"- {c}" for c in r["hard_constraints"])
    neg = ", ".join(r["negative_prompt"])
    subs = SUBJECTS.get(s["id"], ["a coffee cup", "a city bridge", "a pair of running shoes"])
    ex = "\n\n".join(
        f"**{i} — {sub[0]}**\n\n> {sub[1]}"
        for i, sub in enumerate(subs, 1)
    )
    return f"""# {name} — image recipe

Fill the `[SUBJECT]` slot and leave everything below it alone. The constraints
are what make three unrelated subjects come back looking like one family.

```text
{r['template']}
```

**Target —** provider, model and resolution are all configurable; set them to
whatever image stack you are using.

- provider: `{r['provider']}`
- model: `{r['model']}`
- resolution: `{r['resolution']}`

## Hard constraints

{cons}

## Negative prompt

```text
{neg}
```

## Worked examples

Three unrelated subjects, same style:

{ex}
"""


SUBJECTS = {
    "bloom": [("Data", "a faceted crystalline shard suspended and slowly rotating"),
              ("Logistics", "a chrome shipping container floating in void"),
              ("Biology", "an iridescent coral-like organic form")],
    "didone-signal": [("Property", "a sunlit stone villa terrace at golden hour"),
                      ("Food", "a single ceramic bowl on white linen"),
                      ("Travel", "a cloud bank seen from above at dawn")],
    "frosted-field": [("Finance", "a soft translucent stack of rounded cards"),
                      ("Weather", "a frosted glass sphere holding pale mist"),
                      ("Wellness", "smooth overlapping pebbles in pale water")],
    "highlighter": [("Automation", "a matte mechanical arm holding a single marker"),
                    ("Agriculture", "a stack of desaturated hay bales"),
                    ("Music", "a matte black studio monitor at three-quarter view")],
    "poster-block": [("Festival", "a crowd silhouette cut out against flat colour"),
                     ("Coffee", "a hard-masked cut-out of a filter cone"),
                     ("Cycling", "a cut-out cyclist mid-turn at mismatched scale")],
    "studio-object": [("Warehouse", "an isometric stack of pallets and racking"),
                      ("Hardware", "a matte sensor module on a neutral plinth"),
                      ("Construction", "a matte concrete column section")],
}


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    force = "--force" in sys.argv
    ids = args or sorted(os.listdir(os.path.join(ROOT, "styles")))
    extras = load("sources", "brief-extras.json")
    n_b = n_r = 0

    for sid in ids:
        sdir = os.path.join(ROOT, "styles", sid)
        if not os.path.isdir(sdir):
            continue
        s = load("styles", sid, "style.json")

        bp = os.path.join(sdir, "brief.md")
        if sid in extras and (force or not os.path.exists(bp)):
            open(bp, "w", encoding="utf-8").write(brief_md(s, extras[sid]))
            n_b += 1
            print(f"brief   {sid}")

        rp = os.path.join(sdir, "image-recipe.md")
        if force or not os.path.exists(rp):
            open(rp, "w", encoding="utf-8").write(recipe_md(s, s["name"]))
            n_r += 1
            print(f"recipe  {sid}")

    print(f"\n{n_b} brief(s), {n_r} recipe(s) written")


if __name__ == "__main__":
    main()
