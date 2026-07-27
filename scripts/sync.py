#!/usr/bin/env python3
"""Re-ingestion diff (F9).

Run after a fresh harvest has refreshed sources/manifest.json. Reports what
changed relative to the styles already in the catalog, so new bookmarks can be
assigned to existing styles (or drafted as new ones) without disturbing ids.

  python3 scripts/sync.py            # human-readable report
  python3 scripts/sync.py --json     # machine-readable, for an agent to act on

Style ids are never rewritten here: assignment is a deliberate act. This script
only tells you what is unassigned, what is missing, and where new shots most
plausibly belong (by tag overlap with each style's existing sources).
"""
import json
import os
import sys
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MANIFEST = os.path.join(ROOT, "sources", "manifest.json")
STYLES = os.path.join(ROOT, "styles")


def load_styles():
    out = []
    if not os.path.isdir(STYLES):
        return out
    for d in sorted(os.listdir(STYLES)):
        p = os.path.join(STYLES, d, "style.json")
        if os.path.exists(p):
            out.append(json.load(open(p)))
    return out


def main():
    as_json = "--json" in sys.argv
    manifest = json.load(open(MANIFEST))
    shots = {s["shot_url"]: s for s in manifest["shots"]}
    styles = load_styles()

    assigned = {}
    for st in styles:
        for src in st.get("sources", []):
            assigned.setdefault(src["shot_url"], []).append(st["id"])

    new_shots = [u for u in shots if u not in assigned]
    missing = [u for u in assigned if u not in shots]
    dupes = {u: ids for u, ids in assigned.items() if len(ids) > 1}

    # suggest a home for each new shot: highest tag overlap with a style's sources
    style_tags = {}
    for st in styles:
        c = Counter()
        for src in st.get("sources", []):
            sh = shots.get(src["shot_url"])
            if sh:
                c.update(sh.get("tag_tokens", []))
        style_tags[st["id"]] = c

    suggestions = {}
    for u in new_shots:
        tags = set(shots[u].get("tag_tokens", []))
        scored = []
        for sid, c in style_tags.items():
            if not c:
                continue
            overlap = sum(c[t] for t in tags if t in c)
            denom = sum(c.values()) ** 0.5 or 1
            scored.append((overlap / denom, sid))
        scored.sort(reverse=True)
        suggestions[u] = [
            {"style": sid, "score": round(sc, 3)} for sc, sid in scored[:3] if sc > 0
        ]

    result = {
        "manifest_shots": len(shots),
        "styles": len(styles),
        "assigned": len([u for u in shots if u in assigned]),
        "new_unassigned": [
            {
                "shot_url": u,
                "title": shots[u]["title"],
                "designer": shots[u]["designer"],
                "local_image": shots[u]["local_image"],
                "suggested_styles": suggestions[u],
            }
            for u in new_shots
        ],
        "missing_from_manifest": missing,
        "assigned_to_multiple_styles": dupes,
    }

    if as_json:
        print(json.dumps(result, indent=2))
        return 0

    print(f"manifest: {len(shots)} shots · catalog: {len(styles)} styles · "
          f"assigned: {result['assigned']}/{len(shots)}")
    if not new_shots and not missing:
        print("\nIn sync — every bookmarked shot is assigned to a style.")
    if new_shots:
        print(f"\n{len(new_shots)} NEW shot(s) awaiting assignment:")
        for e in result["new_unassigned"]:
            best = e["suggested_styles"][0]["style"] if e["suggested_styles"] else "— no close match, may need a new style"
            print(f"  + {e['title'][:52]:52s} ({e['designer'][:18]})  → likely: {best}")
    if missing:
        print(f"\n{len(missing)} shot(s) referenced by a style but no longer in the collection:")
        for u in missing:
            print(f"  - {u}")
    if dupes:
        print(f"\n{len(dupes)} shot(s) claimed by more than one style:")
        for u, ids in dupes.items():
            print(f"  ! {u.rsplit('/', 1)[-1][:44]} → {', '.join(ids)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
