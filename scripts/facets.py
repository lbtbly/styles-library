#!/usr/bin/env python3
"""Derive device + artifact-type facets for each shot, and roll them up per style.

The raw `artifact_type` strings in sources/analysis/*.json are free text written
per shot. This maps them onto a small controlled vocabulary so the gallery and
the style-picker can filter on them, and so `fit.artifact_types_proven` is
computed from real source material rather than asserted.

Import `shot_facets` / `style_facets`, or run directly for a report.
"""
import json
import os
import re
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ordered: first match wins, so put specific before generic
ARTIFACT_RULES = [
    ("mobile app",      r"mobile app|ios app|android app|phone ui|mobile ui"),
    ("data table",      r"data ?grid|data table|datagrid|spreadsheet|table view"),
    ("design tool",     r"design tool|node-canvas|node canvas|workflow builder|canvas ui|editor"),
    ("auth & onboarding", r"auth|onboarding|sign[- ]?up|login"),
    ("pricing page",    r"pricing"),
    ("branding board",  r"branding board|brand board|identity"),
    ("component study", r"component study|ui component"),
    ("landing page",    r"landing page|marketing site|marketing page|marketing-|hero|website|web page"),
    ("crm",             r"\bcrm\b|support desk|inbox|helpdesk"),
    ("dashboard",       r"dashboard|analytics|monitoring|admin|console|overview"),
    ("web app",         r"web app|kanban|task management|project management|scheduling|workspace|app\b"),
]

DEVICE_RULES = [
    ("mobile", r"mobile|ios|android|phone"),
    ("tablet", r"tablet|ipad"),
]


def classify(artifact_type):
    t = (artifact_type or "").lower()
    artifact = next((name for name, pat in ARTIFACT_RULES if re.search(pat, t)), "dashboard")
    device = next((name for name, pat in DEVICE_RULES if re.search(pat, t)), "desktop")
    return artifact, device


def shot_facets():
    an = json.load(open(os.path.join(ROOT, "sources", "analysis", "all.json")))
    out = {}
    for s in an:
        a, d = classify(s["artifact_type"])
        out[s["index"]] = {"artifact": a, "device": d, "raw": s["artifact_type"]}
    return out


def style_facets(shots, facets):
    """Roll shot-level facets up to a style, most-common first."""
    arts = Counter(facets[i]["artifact"] for i in shots)
    devs = Counter(facets[i]["device"] for i in shots)
    return {
        "artifacts": [a for a, _ in arts.most_common()],
        "devices": [d for d, _ in devs.most_common()],
        "artifact_counts": dict(arts),
        "device_counts": dict(devs),
    }


if __name__ == "__main__":
    facets = shot_facets()
    cat = json.load(open(os.path.join(ROOT, "sources", "catalog-draft.json")))
    print(f"{len(cat['styles'])} styles · {sum(len(s['shots']) for s in cat['styles'])} shots\n")
    all_a, all_d = Counter(), Counter()
    for st in cat["styles"]:
        f = style_facets(st["shots"], facets)
        all_a.update(f["artifact_counts"])
        all_d.update(f["device_counts"])
        print(f"{st['name']:18s} {len(st['shots']):2d}  "
              f"devices={'/'.join(f['devices']):16s} artifacts={', '.join(f['artifacts'])}")
    print(f"\nvocabulary in use — artifacts: {dict(all_a)}")
    print(f"                    devices:   {dict(all_d)}")
