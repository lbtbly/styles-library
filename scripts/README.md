# Scripts

Plain Python 3, no dependencies except Pillow (for palette sampling only, and
only during synthesis). Create the venv once:

```bash
python3 -m venv .venv && .venv/bin/pip install Pillow
```

| script | what it does |
|---|---|
| `build_manifest.py` | Expands a raw browser harvest (`sources/manifest_raw.json`) into `sources/manifest.json` + a download list. Local filenames are keyed on the Dribbble **shot id**, so re-running never renames an existing image. |
| `palette.py` | Samples dominant + saturated-accent colours from a shot image. Used during style synthesis so palettes are measured, never guessed. `palette.py <image> [...]` |
| `sync.py` | Re-ingestion diff: which bookmarked shots are new/unassigned, which are gone, which are double-claimed, and which existing style each new shot most plausibly joins. `--json` for agent consumption. |
| `validate.py` | The QA suite. Exit 0 = green. |

## QA suite

```bash
python3 scripts/validate.py
```

Checks, in order:

1. **schema** — every `style.json` has all required fields at the right types;
   `id` matches its directory; 5–8 keywords; `tokens`/`fit`/`image_recipe` complete;
   `image_recipe.template` contains a `[SUBJECT]` slot; palette values are valid hex.
2. **index** — `styles/index.json` ids match the style directories, `style_count`
   matches the array length, and **every collection count is recomputed from the
   data** (a hardcoded or stale count fails the build). Index entries carry
   everything the gallery needs, and each `thumbnail` resolves on disk.
3. **traceability** — every style source resolves to a shot in `sources/manifest.json`
   and to an image on disk; every manifest shot is assigned to some style.
4. **files** — `brief.md`, `image-recipe.md`, and ≥1 preview exist and are
   substantial (not stubs).
5. **contrast** — WCAG: `ink` on `bg` must reach AA 4.5:1 (fails below); `accent`
   on `bg` below 3:1 warns that it is fill/large-text only.
6. **render / self-containment** — previews contain no `http(s)` or
   protocol-relative asset references, so they open offline from `file://`.

Plus a **style-drift** warning when a `brief.md` no longer cites its own palette
values — the cheapest signal that a style and its brief have diverged.

## Re-ingestion — "sync with my Dribbble collection"

Style ids are permanent; this flow only ever **adds**.

1. **Re-harvest** (needs the browser tools and a logged-in Dribbble session).
   Open the collection, then in the page context page through
   `?page=N` until a page yields no `li.shot-thumbnail`, collecting for each card:
   `data-thumbnail-id`, the `noscript > img` src (the original, un-resized asset),
   the shot href, `.shot-title`, the designer display name, and the `img alt`
   (title + tags). Export the array as `sources/manifest_raw.json` in the shape
   `{"count": N, "rows": [{i, id, t, d, u, g, k}, …]}`.

   Two gotchas, both already worked around above: shot **detail** pages answer
   scripted fetches with a bot-challenge status, so take tags from the listing's
   `alt` text rather than per-shot pages; and the page cannot POST to
   `http://localhost` (Chrome blocks private-network requests from an HTTPS
   origin), so move the harvest out as a file rather than an HTTP call.

2. **Rebuild the manifest and fetch new images.**

   ```bash
   python3 scripts/build_manifest.py
   cat sources/.fetchlist | while IFS=$'\t' read -r url path; do
     [ -s "sources/$path" ] || curl -sSL --max-time 60 -o "sources/$path" "$url"
   done
   ```

   Existing images are skipped, so this is cheap to re-run.

3. **Diff.**

   ```bash
   python3 scripts/sync.py
   ```

   For each new shot it suggests the existing styles with the strongest tag
   overlap. Assign it to one by appending to that style's `sources` array, or —
   if it matches nothing — draft a new style directory for it. Then update
   `styles/index.json`.

4. **Validate.**

   ```bash
   python3 scripts/validate.py
   ```

   `validate.py` fails while any manifest shot is unassigned, so an incomplete
   sync cannot pass silently.
