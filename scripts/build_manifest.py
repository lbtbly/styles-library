#!/usr/bin/env python3
"""Expand the raw browser harvest into sources/manifest.json (F1 / F9 re-ingestion)."""
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW = os.path.join(ROOT, "sources", "manifest_raw.json")
OUT = os.path.join(ROOT, "sources", "manifest.json")
CDN = "https://cdn.dribbble.com/userupload/"
SITE = "https://dribbble.com/shots/"

COLLECTION = {
    "name": "Styles Moodboard",
    "url": "https://dribbble.com/lbtbouley/collections/7904481-Styles-Moodboard",
    "owner": "lbtbouley",
}


def slug(text, maxlen=60):
    s = re.sub(r"[^a-z0-9]+", "-", (text or "").lower()).strip("-")
    return s[:maxlen].strip("-")


def main():
    raw = json.load(open(RAW))
    rows = raw["rows"]

    # Preserve ids across re-ingestion: local filenames are keyed on the Dribbble shot id.
    entries = []
    for r in rows:
        ext = os.path.splitext(r["g"])[1].lower() or ".png"
        local = f"shots/{r['id']}-{slug(r['t'], 48)}{ext}"
        tags = [t for t in (r.get("k") or "").split() if t]
        entries.append(
            {
                "shot_id": r["id"],
                "index": r["i"],
                "title": r["t"],
                "designer": r["d"],
                "shot_url": SITE + r["u"],
                "image_url": CDN + r["g"],
                "local_image": local,
                "tags_raw": r.get("k", ""),
                "tag_tokens": tags,
            }
        )

    manifest = {
        "collection": COLLECTION,
        "shot_count": len(entries),
        "designer_count": len({e["designer"] for e in entries}),
        "shots": entries,
    }
    json.dump(manifest, open(OUT, "w"), indent=2, ensure_ascii=False)
    print(f"wrote {OUT}: {len(entries)} shots, {manifest['designer_count']} designers")

    # emit a download list for the fetch step
    with open(os.path.join(ROOT, "sources", ".fetchlist"), "w") as f:
        for e in entries:
            f.write(f"{e['image_url']}\t{e['local_image']}\n")


if __name__ == "__main__":
    main()
