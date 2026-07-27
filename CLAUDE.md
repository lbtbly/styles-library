# Styles Library — agent contract

A catalog of reusable visual styles ("design DNA") synthesized from a personal
Dribbble collection. **Primary consumer: a coding agent.** The gallery is a view;
the filesystem is the source of truth.

Use this library whenever you are about to design or build a user-facing
artifact — landing page, dashboard, auth screen, pricing page, mobile app,
marketing site — and the visual direction is not already fixed by an existing
codebase or brand.

## Resolving paths — read this first

Every path in this document is **relative to the library root**, which is not
usually your working directory. Resolve it before reading anything:

- **Installed as a plugin** — the root is `${CLAUDE_PLUGIN_ROOT}`. Read
  `${CLAUDE_PLUGIN_ROOT}/styles/index.json`, not `styles/index.json`.
- **Cloned as a repo** — the root is the clone directory.

If a read fails, you almost certainly resolved the root wrong; do not conclude
the library is missing a file.

---

## The flow

### 1. Read the index — always start here

```
<library-root>/styles/index.json
```

One file. It carries every style's `id`, `name`, `collection`, `pairing`,
`concept`, `keywords`, `fit` block, and `thumbnail`. Never hardcode the number of
styles or collections — count them from this file. It is the only entry point you
need; do not crawl `styles/*/` to discover what exists.

### 2. Shortlist by `fit`

Each entry carries:

| field | meaning |
|---|---|
| `fit.best_for` | product/artifact kinds this style flatters |
| `fit.avoid_for` | where it actively misfires — treat as a hard filter |
| `fit.mood` | brand adjectives it projects |
| `fit.artifact_types_proven` | artifact kinds evidenced by this style's own source shots |
| `surfaces.devices` | `desktop` / `mobile` / `tablet` — what the style is proven on |
| `surfaces.artifacts` | artifact vocabulary, most-evidenced first |
| `surfaces.artifact_counts` | how many source shots back each claim — use it to weigh confidence |
| `keywords` | visual DNA tags for matching |
| `swatch` | the style's leading hex values, for a quick visual read |

`index.json` also publishes `artifact_vocabulary` and `device_vocabulary` — the
complete controlled vocabularies in use, so you can filter without guessing at
string values. Both facet sets are **derived** from each style's source shots by
`scripts/facets.py`; they describe what a style is *proven* on, not the limit of
where it can be applied.

Filter out anything matching `avoid_for` first, then rank the remainder on
`best_for` + `mood` overlap with the brief. If you want the selection heuristics
spelled out — including how to map project type, industry, audience, brand
adjectives, and content density onto these fields — invoke the
**`style-picker`** skill (`<library-root>/skills/style-picker/SKILL.md`; when
installed as a plugin it is auto-loaded — invoke it by name).

### 3. Open the shortlisted styles

```
<library-root>/styles/<style-id>/style.json    # full tokens, fit, sources, image_recipe
<library-root>/styles/<style-id>/brief.md      # the copyable design brief
```

`style.json` is the machine-readable definition. `brief.md` is the human/agent
prose brief and is **self-contained** — an agent given only that file can
reproduce the style on any artifact with no other context.

### 4. Apply

- **Inject `brief.md` into working context.** It is written to be pasted whole.
- **Use `tokens.palette` for CSS custom properties.** The hex values are exact
  and sampled from the source shots; do not "improve" them.
- **Use `tokens.type` for the font stack and hierarchy rules**, `tokens.texture`
  for effect implementation, `tokens.layout` for spacing and composition.
- **Use `image_recipe` for hero/illustration assets** — fill the `[SUBJECT: …]`
  slot, keep every hard constraint verbatim. See `image-recipe.md` for the
  copyable version.
- **Read a preview before writing code.** `<library-root>/styles/<id>/previews/*.html` are real,
  self-contained artifacts in the style; they show the intended component
  treatments better than prose can.

### 5. Cite your choice

When you finish, say which style you applied and why in one line, e.g.
*"Applied **<name>** — its `best_for` covers developer tooling and its mood
(precise, technical) matches the brand adjectives you gave."*

---

## Layout

```
styles-library/
├── CLAUDE.md                     # this contract
├── sources/
│   ├── manifest.json             # every harvested shot + attribution
│   ├── shots/                    # full-resolution source images
│   └── analysis/                 # per-shot visual analysis (synthesis input)
├── styles/
│   ├── index.json                # master index — the only required entry point
│   └── <style-id>/
│       ├── style.json            # full schema
│       ├── brief.md              # COPY BRIEF target
│       ├── image-recipe.md       # COPY IMAGE PROMPT target
│       └── previews/*.html       # self-contained proof artifacts
├── gallery/index.html            # static human explorer (reads index.json)
├── skills/style-picker/SKILL.md  # selection heuristics
└── scripts/                      # validator, manifest builder, re-ingestion diff
```

## `style.json` schema

```jsonc
{
  "id": "<slug, matches directory name>",
  "name": "<style name>",
  "collection": "<collection name>",
  "pairing": "<'X × Y' descriptor>",
  "concept": "<one-line concept statement>",
  "keywords": ["<5-8 visual DNA tags>"],
  "tokens": {
    "palette": { "bg": "#…", "surface": "#…", "ink": "#…", "accent": "#…", … },
    "type":    { "families": …, "hierarchy": …, "usage": … },
    "texture": "<effects / materials, with implementation notes>",
    "layout":  "<spacing & composition attitude>"
  },
  "fit": {
    "best_for": [], "avoid_for": [], "mood": [], "artifact_types_proven": []
  },
  "image_recipe": {
    "template": "<… [SUBJECT: …] …>", "provider": "<configurable>",
    "model": "<configurable>", "resolution": "", "hard_constraints": []
  },
  "sources": [{ "shot_url": "", "designer": "", "local_image": "" }],
  "index": 0
}
```

`palette` keys `bg` / `ink` / `accent` are load-bearing: the QA suite contrast-checks
`ink` against `bg` (WCAG AA) and warns when `accent` on `bg` is too low for body copy.

## Rules

- **Never edit `sources/`** — it is the harvest record and the attribution trail.
- **Style ids are permanent.** Re-ingestion may add shots or styles; it must not
  renumber or rename existing ones, or every reference breaks.
- **Keep attribution.** Every style carries the `shot_url` + `designer` of the
  shots it was derived from. This is a personal reference tool built on other
  designers' work — the credit travels with the style.
- **Previews are original work in the style**, never reproductions of a source shot.
- **Previews must render offline** — inline CSS/JS, no external asset URLs. The
  validator fails the build on any `http(s)` asset reference.
- **Bump the plugin version before every commit.** The `version` in
  `.claude-plugin/plugin.json` is the plugin autoUpdate cache key — installed
  copies only refresh when it changes, and installs ship the whole repo. Before
  committing anything, bump the version in the same commit, or the change
  silently never reaches installs. `validate.py` fails when content has drifted
  without a bump.

## Maintenance

```bash
python3 scripts/validate.py    # full QA suite — schema, index, contrast, render, drift
python3 scripts/sync.py        # what changed since the last harvest
```

To re-sync with the Dribbble collection, see **Re-ingestion** in
`scripts/README.md`: re-harvest in the browser, rebuild the manifest, then run
`sync.py` to see which new shots belong to existing styles and which want a new one.
