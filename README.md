# Styles Library

A catalog of reusable visual styles — "design DNA" — synthesised from a personal
Dribbble collection. The primary consumer is **Claude Code**: an agent reads the
index, shortlists by fit, and applies a style to whatever it is building. The
gallery is a view for humans; the filesystem is the source of truth.

**18 styles · 5 collections · derived from 117 bookmarked shots by 40 designers.**

## Install as a Claude Code plugin

The repo is also a Claude Code plugin marketplace — installing it makes the
`style-picker` skill available in every session, so Claude reaches for the
library on its own whenever it is about to design something.

In Claude Code:

```
/plugin marketplace add lbtbly/styles-library
/plugin install styles-library@styles-library
```

Or point at a local clone instead of GitHub:

```
/plugin marketplace add ~/Claude/styles-library
/plugin install styles-library@styles-library
```

Then just ask for UI work — *"design a landing page for a fintech app"* — and
the skill triggers itself. `/style-picker` invokes it explicitly.

Once installed, the library root is `${CLAUDE_PLUGIN_ROOT}`, not your working
directory: the index lives at `${CLAUDE_PLUGIN_ROOT}/styles/index.json`. Every
path in `CLAUDE.md` and the skill is relative to that root.

To update after re-syncing the collection, or to remove it:

```
/plugin marketplace update styles-library
/plugin uninstall styles-library@styles-library
```

The plugin ships the styles, briefs, image recipes, previews and the
`style-picker` skill. The gallery and the `scripts/` maintenance tooling come
along with it but are meant to be used from a clone.

## Run the gallery

```bash
python3 -m http.server 8000
```

Then open <http://localhost:8000/gallery/>. It needs to be served over HTTP
rather than opened from `file://`, because the copy actions and the detail sheet
fetch `styles/index.json` and each `style.json`.

## For an agent

Start at `CLAUDE.md`. The short version:

1. Read `styles/index.json` — the only entry point.
2. Shortlist on `fit.avoid_for` (a veto), then rank on `fit.best_for`,
   `fit.mood` and `surfaces`.
3. Open `styles/<id>/brief.md` and apply it.
4. Cite which style you used and why.

`skills/style-picker/SKILL.md` encodes the selection heuristics — at most three
intake questions, always a primary plus one alternate.

## Layout

```
CLAUDE.md                     agent contract
.claude-plugin/               plugin + marketplace manifests
sources/                      harvested shots, manifest, per-shot analysis
styles/index.json             master index — counts computed, never hardcoded
styles/<id>/style.json        full definition: tokens, fit, surfaces, sources
styles/<id>/brief.md          self-contained design brief (COPY BRIEF)
styles/<id>/image-recipe.md   parameterised image prompt (COPY IMAGE PROMPT)
styles/<id>/previews/*.html   self-contained proof artifacts
gallery/index.html            static explorer
skills/style-picker/          selection heuristics
scripts/                      builders, validator, re-ingestion diff
```

## Maintenance

```bash
python3 scripts/validate.py    # QA suite — schema, index, contrast, render, drift
python3 scripts/sync.py        # what changed since the last harvest
```

`scripts/README.md` documents each script and the full "sync with my Dribbble
collection" procedure.

## Provenance

Every style records the `shot_url` and `designer` of the shots it was derived
from, and the validator fails if any style loses that trail or if any harvested
shot goes unassigned. Styles are transferable DNA — palette, type, texture,
layout attitude — not reproductions; the previews are original artifacts built
in each style, never copies of a source shot.

This is a personal reference tool. All credit for the source work belongs to the
designers listed in `sources/manifest.json` and in each style's `sources` array.
