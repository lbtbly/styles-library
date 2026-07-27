#!/usr/bin/env python3
"""Emit styles/<id>/style.json and styles/index.json (F3).

Sources of truth:
  sources/catalog-draft.json  — clustering, names, pairings, concepts
  sources/spec-a.json + b     — hand-authored tokens / fit / recipe per style
  sources/analysis/all.json   — per-shot visual analysis (drives artifact facets)
  sources/manifest.json       — attribution

Everything derivable is derived: facets, artifact_types_proven, source lists,
collection counts. Nothing is hardcoded twice.
"""
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from facets import shot_facets, style_facets  # noqa: E402

IMG_PROVIDER = "configurable — set to your image provider"
IMG_MODEL = "configurable — set to your image model"
IMG_RES = "1536x1024 (3:2 landscape); use 1024x1536 for portrait, 1024x1024 for square"


def load(*parts):
    return json.load(open(os.path.join(ROOT, *parts), encoding="utf-8"))


def main():
    cat = load("sources", "catalog-draft.json")
    spec = {**load("sources", "spec-a.json"), **load("sources", "spec-b.json")}
    man = {s["index"]: s for s in load("sources", "manifest.json")["shots"]}
    facets = shot_facets()

    missing = [s["id"] for s in cat["styles"] if s["id"] not in spec]
    if missing:
        raise SystemExit(f"no spec for: {missing}")

    index_entries, written = [], 0
    for n, st in enumerate(cat["styles"]):
        sp = spec[st["id"]]
        f = style_facets(st["shots"], facets)
        sdir = os.path.join(ROOT, "styles", st["id"])
        os.makedirs(os.path.join(sdir, "previews"), exist_ok=True)

        recipe = sp["recipe"]
        template = (
            f"[SUBJECT: describe the subject in one clause — e.g. \"a stack of "
            f"shipping containers\", \"a single ceramic cup\", \"an abstract network of nodes\"]\n\n"
            f"Rendered as {recipe['medium']}.\n\n"
            "STYLE — apply all of the following, they are not optional:\n"
            + "\n".join(f"- {c}" for c in recipe["constraints"])
            + f"\n\nNEGATIVE SPACE: {recipe['negative_space']}\n\n"
            "DO NOT INCLUDE: " + ", ".join(recipe["negative"]) + "."
        )

        style = {
            "id": st["id"],
            "name": st["name"],
            "collection": st["collection"],
            "pairing": st["pairing"],
            "concept": st["concept"],
            "keywords": sp["keywords"],
            "tokens": sp["tokens"],
            "fit": {
                "best_for": sp["fit"]["best_for"],
                "avoid_for": sp["fit"]["avoid_for"],
                "mood": sp["fit"]["mood"],
                "artifact_types_proven": f["artifacts"],
            },
            "surfaces": {
                "devices": f["devices"],
                "artifacts": f["artifacts"],
                "artifact_counts": f["artifact_counts"],
                "device_counts": f["device_counts"],
            },
            "image_recipe": {
                "template": template,
                "provider": IMG_PROVIDER,
                "model": IMG_MODEL,
                "resolution": IMG_RES,
                "hard_constraints": recipe["constraints"] + [
                    f"negative space — {recipe['negative_space']}",
                    "never include legible text, logos or UI chrome in the generated image",
                ],
                "negative_prompt": recipe["negative"],
            },
            "sources": [
                {
                    "shot_url": man[i]["shot_url"],
                    "designer": man[i]["designer"],
                    "local_image": man[i]["local_image"],
                    "thumbnail": f"thumbs/{man[i]['shot_id']}.jpg",
                    "title": man[i]["title"],
                }
                for i in st["shots"]
            ],
            "index": n,
        }
        json.dump(style, open(os.path.join(sdir, "style.json"), "w", encoding="utf-8"),
                  indent=2, ensure_ascii=False)
        written += 1

        pal = sp["tokens"]["palette"]
        index_entries.append({
            "id": st["id"],
            "name": st["name"],
            "collection": st["collection"],
            "pairing": st["pairing"],
            "concept": st["concept"],
            "keywords": sp["keywords"],
            "swatch": [v for k, v in pal.items()
                       if isinstance(v, str) and v.startswith("#")][:6],
            "fit": style["fit"],
            "surfaces": style["surfaces"],
            "source_count": len(st["shots"]),
            "designers": sorted({man[i]["designer"] for i in st["shots"]}),
            "thumbnail": f"styles/{st['id']}/previews/{previews_for(st['id'])[0]}"
                         if previews_for(st["id"]) else f"sources/thumbs/{man[st['shots'][0]]['shot_id']}.jpg",
            "previews": previews_for(st["id"]),
            "index": n,
        })

    collections = []
    for c in cat["collections"]:
        count = sum(1 for e in index_entries if e["collection"] == c["name"])
        collections.append({"name": c["name"], "note": c["note"], "count": count})

    index = {
        "generated_from": "sources/catalog-draft.json + sources/spec-*.json",
        "source_collection": load("sources", "manifest.json")["collection"],
        "shot_count": len(man),
        "style_count": len(index_entries),
        "collections": collections,
        "artifact_vocabulary": sorted({a for e in index_entries for a in e["surfaces"]["artifacts"]}),
        "device_vocabulary": sorted({d for e in index_entries for d in e["surfaces"]["devices"]}),
        "styles": index_entries,
    }
    json.dump(index, open(os.path.join(ROOT, "styles", "index.json"), "w", encoding="utf-8"),
              indent=2, ensure_ascii=False)
    print(f"wrote {written} style.json + index.json "
          f"({len(collections)} collections, {sum(c['count'] for c in collections)} styles)")


def previews_for(sid):
    p = os.path.join(ROOT, "styles", sid, "previews")
    if not os.path.isdir(p):
        return []
    return sorted(f for f in os.listdir(p) if f.endswith(".html"))


if __name__ == "__main__":
    main()
