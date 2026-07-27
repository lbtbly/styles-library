#!/usr/bin/env python3
"""QA suite for the styles library (F9).

Checks:
  1. schema      — every style.json has all required fields, correct types
  2. index       — styles/index.json matches the style dirs; counts computed, not stale
  3. traceability— every style source maps to a manifest shot; every shot is assigned
  4. files       — brief.md, image-recipe.md, >=1 preview exist and are non-trivial
  5. contrast    — WCAG AA check on each style's ink/bg and accent/bg pairs
  6. render      — previews are self-contained (no external http(s) asset refs)
  7. version     — plugin version bumped whenever published content changed
                   (the version is the plugin autoUpdate cache key: without a
                   bump, installed copies never refresh)

Usage: python3 scripts/validate.py [--quiet]
Exit code 0 = all pass, 1 = failures.
"""
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STYLES = os.path.join(ROOT, "styles")
INDEX = os.path.join(STYLES, "index.json")
MANIFEST = os.path.join(ROOT, "sources", "manifest.json")

REQUIRED = {
    "id": str, "name": str, "collection": str, "pairing": str, "concept": str,
    "keywords": list, "tokens": dict, "fit": dict, "image_recipe": dict,
    "sources": list, "index": int,
}
TOKEN_KEYS = {"palette", "type", "texture", "layout"}
FIT_KEYS = {"best_for", "avoid_for", "mood", "artifact_types_proven"}
RECIPE_KEYS = {"template", "provider", "model", "resolution", "hard_constraints"}

fails, warns = [], []


def fail(m):
    fails.append(m)


def warn(m):
    warns.append(m)


# ---------- contrast ----------
def _srgb(c):
    c /= 255
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4


def luminance(hexstr):
    h = hexstr.lstrip("#")
    if len(h) == 3:
        h = "".join(ch * 2 for ch in h)
    r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
    return 0.2126 * _srgb(r) + 0.7152 * _srgb(g) + 0.0722 * _srgb(b)


def contrast(a, b):
    la, lb = luminance(a), luminance(b)
    hi, lo = max(la, lb), min(la, lb)
    return (hi + 0.05) / (lo + 0.05)


HEX = re.compile(r"^#(?:[0-9a-fA-F]{3}|[0-9a-fA-F]{6})$")

# ---------- plugin version discipline ----------
PLUGIN_JSON = os.path.join(ROOT, ".claude-plugin", "plugin.json")


def _git(*args):
    r = subprocess.run(["git", "-C", ROOT, *args],
                       capture_output=True, text=True)
    if r.returncode != 0:
        raise RuntimeError(r.stderr.strip())
    return r.stdout


def check_version_discipline():
    """The plugin version is autoUpdate's cache key: installed copies only
    refresh when it changes. Fail if published content drifted since the
    commit that introduced the current version string."""
    if not os.path.exists(PLUGIN_JSON):
        return  # not packaged as a plugin
    try:
        current = json.load(open(PLUGIN_JSON)).get("version")
    except Exception as e:
        fail(f"plugin.json unparseable — {e}")
        return
    if not current:
        fail("plugin.json has no 'version' — autoUpdate cannot track releases")
        return
    try:
        commits = _git("rev-list", "HEAD", "--",
                       ".claude-plugin/plugin.json").split()
    except (RuntimeError, FileNotFoundError):
        return  # not a git checkout (e.g. an installed plugin copy) — skip
    # walk newest→oldest to the commit that introduced the current version
    bump_commit = None
    for c in commits:
        try:
            v = json.loads(_git("show", f"{c}:.claude-plugin/plugin.json")).get("version")
        except (RuntimeError, ValueError):
            break
        if v != current:
            break
        bump_commit = c
    if bump_commit is None:
        return  # version bumped in the working tree, not yet committed — fine
    # plugin installs ship the whole repo, so any tracked change requires a bump
    drifted = _git("diff", "--name-only", bump_commit, "--", ".").split("\n")
    drifted = [f for f in drifted if f and f != ".claude-plugin/plugin.json"]
    if drifted:
        fail(f"plugin version {current} unchanged but {len(drifted)} published "
             f"file(s) drifted since it was set (e.g. {drifted[0]}) — bump "
             f"'version' in .claude-plugin/plugin.json or installed copies "
             f"never receive the change")


def main():
    quiet = "--quiet" in sys.argv

    if not os.path.isdir(STYLES):
        fail("styles/ directory missing")
        return report(quiet)

    style_dirs = sorted(
        d for d in os.listdir(STYLES)
        if os.path.isdir(os.path.join(STYLES, d)) and not d.startswith(".")
    )

    manifest = json.load(open(MANIFEST)) if os.path.exists(MANIFEST) else {"shots": []}
    shot_by_url = {s["shot_url"]: s for s in manifest["shots"]}
    assigned = set()

    styles = []
    for d in style_dirs:
        p = os.path.join(STYLES, d, "style.json")
        if not os.path.exists(p):
            fail(f"{d}: style.json missing")
            continue
        try:
            s = json.load(open(p))
        except Exception as e:
            fail(f"{d}: style.json unparseable — {e}")
            continue
        styles.append(s)

        # 1. schema
        for k, t in REQUIRED.items():
            if k not in s:
                fail(f"{d}: missing field '{k}'")
            elif not isinstance(s[k], t):
                fail(f"{d}: field '{k}' should be {t.__name__}, got {type(s[k]).__name__}")
        if s.get("id") != d:
            fail(f"{d}: id '{s.get('id')}' does not match directory name")
        kw = s.get("keywords", [])
        if not (5 <= len(kw) <= 8):
            fail(f"{d}: keywords must be 5-8, got {len(kw)}")
        missing_tokens = TOKEN_KEYS - set(s.get("tokens", {}))
        if missing_tokens:
            fail(f"{d}: tokens missing {sorted(missing_tokens)}")
        missing_fit = FIT_KEYS - set(s.get("fit", {}))
        if missing_fit:
            fail(f"{d}: fit missing {sorted(missing_fit)}")
        missing_recipe = RECIPE_KEYS - set(s.get("image_recipe", {}))
        if missing_recipe:
            fail(f"{d}: image_recipe missing {sorted(missing_recipe)}")
        if "[SUBJECT" not in s.get("image_recipe", {}).get("template", ""):
            fail(f"{d}: image_recipe.template has no [SUBJECT] slot")

        # palette hex sanity
        pal = s.get("tokens", {}).get("palette", {})
        if not isinstance(pal, dict) or not pal:
            fail(f"{d}: tokens.palette empty")
        for name, val in (pal.items() if isinstance(pal, dict) else []):
            if isinstance(val, str) and val.startswith("#") and not HEX.match(val):
                fail(f"{d}: palette.{name} '{val}' is not a valid hex")

        # 3. traceability
        if not s.get("sources"):
            fail(f"{d}: no sources — style is not traceable")
        for src in s.get("sources", []):
            u = src.get("shot_url", "")
            if u not in shot_by_url:
                fail(f"{d}: source {u} not in manifest")
            else:
                assigned.add(u)
            li = src.get("local_image", "")
            if li and not os.path.exists(os.path.join(ROOT, "sources", li)):
                fail(f"{d}: source image missing on disk: {li}")

        # 4. files
        for f in ("brief.md", "image-recipe.md"):
            fp = os.path.join(STYLES, d, f)
            if not os.path.exists(fp):
                fail(f"{d}: {f} missing")
            elif os.path.getsize(fp) < 400:
                fail(f"{d}: {f} is suspiciously short ({os.path.getsize(fp)} bytes)")
        pdir = os.path.join(STYLES, d, "previews")
        previews = sorted(f for f in os.listdir(pdir)) if os.path.isdir(pdir) else []
        previews = [f for f in previews if f.endswith(".html")]
        if not previews:
            fail(f"{d}: no previews")
        # 6. render / self-containment
        for pv in previews:
            html = open(os.path.join(pdir, pv), encoding="utf-8").read()
            if len(html) < 1000:
                fail(f"{d}/{pv}: preview too small to be a real artifact")
            for m in re.findall(r'(?:src|href)\s*=\s*["\'](https?://[^"\']+)', html):
                fail(f"{d}/{pv}: external asset breaks offline rendering — {m[:60]}")
            if re.search(r'<(?:script|link)[^>]+\ssrc\s*=\s*["\']//', html):
                fail(f"{d}/{pv}: protocol-relative external asset")
            if "<title" not in html.lower():
                warn(f"{d}/{pv}: no <title> — it names the artifact in the gallery")
            # preview-drift: a preview must actually use its style's core palette
            low = html.lower()
            core = [pal.get(k) for k in ("bg", "surface", "ink", "accent")]
            absent = [v for v in core
                      if isinstance(v, str) and HEX.match(v) and v.lower() not in low]
            if absent:
                fail(f"{d}/{pv}: preview does not use core palette value(s) "
                     f"{absent} — it has drifted from style.json")

        # 5. contrast
        def get(*names):
            for n in names:
                v = pal.get(n)
                if isinstance(v, str) and HEX.match(v):
                    return v
            return None

        bg, ink, accent = get("bg", "background", "base"), get("ink", "text", "fg"), get("accent", "primary")
        if bg and ink:
            c = contrast(bg, ink)
            if c < 4.5:
                fail(f"{d}: body contrast ink {ink} on bg {bg} = {c:.2f}:1 (WCAG AA needs 4.5)")
            elif c < 7:
                warn(f"{d}: ink/bg contrast {c:.2f}:1 passes AA but not AAA")
        if bg and accent:
            c = contrast(bg, accent)
            if c < 3.0:
                warn(f"{d}: accent {accent} on bg {bg} = {c:.2f}:1 — only safe for large text/fills, not body copy")

    # 2. index integrity
    if not os.path.exists(INDEX):
        fail("styles/index.json missing")
    else:
        idx = json.load(open(INDEX))
        idx_styles = idx.get("styles", [])
        idx_ids = [s.get("id") for s in idx_styles]
        if sorted(idx_ids) != sorted(style_dirs):
            fail(f"index.json ids != style dirs (index {len(idx_ids)}, dirs {len(style_dirs)})")
        if idx.get("style_count") != len(idx_styles):
            fail(f"index.json style_count {idx.get('style_count')} != {len(idx_styles)} styles")
        # collection counts must be computed from the data
        computed = {}
        for s in idx_styles:
            computed[s.get("collection")] = computed.get(s.get("collection"), 0) + 1
        for c in idx.get("collections", []):
            if computed.get(c.get("name")) != c.get("count"):
                fail(f"index.json collection '{c.get('name')}' count "
                     f"{c.get('count')} != computed {computed.get(c.get('name'))}")
        if {c.get("name") for c in idx.get("collections", [])} != set(computed):
            fail("index.json collections list does not match collections used by styles")
        # index entries must carry what the gallery needs
        for s in idx_styles:
            for k in ("id", "name", "collection", "pairing", "concept", "keywords", "thumbnail"):
                if k not in s:
                    fail(f"index.json entry '{s.get('id')}' missing '{k}'")
            th = s.get("thumbnail")
            if th and not os.path.exists(os.path.join(ROOT, th.lstrip("./"))):
                fail(f"index.json entry '{s.get('id')}' thumbnail not found: {th}")

    # 3b. every manifest shot assigned
    unassigned = [u for u in shot_by_url if u not in assigned]
    if unassigned:
        fail(f"{len(unassigned)} manifest shots not assigned to any style "
             f"(e.g. {unassigned[0].rsplit('/',1)[-1][:40]})")

    # style-drift checklist: keywords/palette echoed in brief
    for s in styles:
        d = s["id"]
        bp = os.path.join(STYLES, d, "brief.md")
        if os.path.exists(bp):
            brief = open(bp, encoding="utf-8").read().lower()
            pal = s.get("tokens", {}).get("palette", {})
            missing = [v for v in pal.values()
                       if isinstance(v, str) and HEX.match(v) and v.lower() not in brief]
            if missing:
                warn(f"{d}: brief.md does not cite palette value(s) {missing[:3]} — possible style drift")

    # 7. plugin version discipline
    check_version_discipline()

    return report(quiet, len(styles))


def report(quiet, n=0):
    if fails:
        print(f"FAIL — {len(fails)} error(s):")
        for f in fails:
            print(f"  ✗ {f}")
    if warns and not quiet:
        print(f"\n{len(warns)} warning(s):")
        for w in warns:
            print(f"  ! {w}")
    if not fails:
        print(f"PASS — {n} styles valid "
              f"({len(warns)} warning(s))" if warns else f"PASS — {n} styles valid")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
