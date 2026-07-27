#!/usr/bin/env python3
"""Render sources/catalog-draft.json as a visual review sheet (F2 approval gate)."""
import base64
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from facets import shot_facets, style_facets  # noqa: E402

facets = shot_facets()


def datauri(shot_id):
    """Inline the thumbnail so the review sheet is portable/self-contained."""
    p = os.path.join(ROOT, "sources", "thumbs", f"{shot_id}.jpg")
    with open(p, "rb") as f:
        return "data:image/jpeg;base64," + base64.b64encode(f.read()).decode()
cat = json.load(open(os.path.join(ROOT, "sources", "catalog-draft.json")))
an = {s["index"]: s for s in json.load(open(os.path.join(ROOT, "sources", "analysis", "all.json")))}
man = {s["index"]: s for s in json.load(open(os.path.join(ROOT, "sources", "manifest.json")))["shots"]}

by_coll = {}
for st in cat["styles"]:
    by_coll.setdefault(st["collection"], []).append(st)

parts = ["""<!doctype html><meta charset="utf-8">
<title>Styles Moodboard — catalog for approval</title>
<style>
:root{--bg:#F7F7F5;--ink:#141414;--mut:#6E6E6A;--line:#E2E2DE;--card:#FFF}
@media(prefers-color-scheme:dark){:root{--bg:#121211;--ink:#EDEDEA;--mut:#9A9A94;--line:#2A2A28;--card:#1A1A19}}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);
 font:15px/1.55 ui-sans-serif,-apple-system,"Segoe UI",Inter,system-ui,sans-serif;
 -webkit-font-smoothing:antialiased}
.wrap{max-width:1180px;margin:0 auto;padding:56px 28px 90px}
h1{font-size:30px;letter-spacing:-.022em;margin:0 0 6px;font-weight:640}
.sub{color:var(--mut);margin:0 0 40px;font-size:14px}
h2{font-size:11px;text-transform:uppercase;letter-spacing:.14em;color:var(--mut);
 margin:46px 0 14px;padding-bottom:9px;border-bottom:1px solid var(--line);font-weight:620}
.style{background:var(--card);border:1px solid var(--line);border-radius:13px;
 padding:19px 20px 20px;margin-bottom:15px}
.hd{display:flex;align-items:baseline;gap:11px;flex-wrap:wrap;margin-bottom:3px}
.nm{font-size:19px;font-weight:640;letter-spacing:-.014em}
.pr{color:var(--mut);font-size:13px}
.ct{margin-left:auto;color:var(--mut);font-size:12px;font-variant-numeric:tabular-nums}
.cc{font-size:14px;color:var(--ink);opacity:.85;margin:0 0 13px;max-width:74ch}
.tg{display:flex;flex-wrap:wrap;gap:5px;margin:0 0 12px}
.tg b{font:500 11px/1 ui-sans-serif,system-ui;letter-spacing:.01em;color:var(--mut);
 border:1px solid var(--line);border-radius:999px;padding:5px 9px;display:inline-flex;gap:5px;align-items:center}
.tg b.dev{color:var(--ink);border-color:currentColor;opacity:.75}
.tg em{font-style:normal;opacity:.55;font-variant-numeric:tabular-nums}
.sw{display:flex;gap:5px;margin:0 0 13px}
.sw i{width:26px;height:26px;border-radius:6px;border:1px solid rgba(128,128,128,.28);display:block}
.gr{display:grid;grid-template-columns:repeat(auto-fill,minmax(132px,1fr));gap:8px}
.gr a{display:block;border-radius:7px;overflow:hidden;border:1px solid var(--line);
 background:#0000000d;text-decoration:none}
.gr img{width:100%;height:92px;object-fit:cover;display:block}
.gr span{display:block;font-size:10px;color:var(--mut);padding:5px 6px;line-height:1.3;
 white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
</style>
<div class="wrap">
<h1>Styles Moodboard — proposed catalog</h1>
<p class="sub">Derived from 117 bookmarked shots · 40 designers · every shot assigned, none duplicated.
Swatches are sampled from the source images, not chosen. Click any thumbnail to open its Dribbble shot.</p>
"""]

for coll in cat["collections"]:
    styles = by_coll.get(coll["name"], [])
    total = sum(len(s["shots"]) for s in styles)
    parts.append(f'<h2>{coll["name"]} — {coll["note"]} · {len(styles)} styles, {total} shots</h2>')
    for st in styles:
        # representative palette: most common accent + bg across member shots
        accents, bgs, inks = [], [], []
        for i in st["shots"]:
            p = an[i]["palette"]
            accents.append(p.get("accent"))
            bgs.append(p.get("bg"))
            inks.append(p.get("ink"))
        sw = "".join(
            f'<i style="background:{c}"></i>'
            for c in ([max(set(bgs), key=bgs.count), max(set(inks), key=inks.count)]
                      + [a for a in dict.fromkeys(accents) if a][:6])
        )
        cells = "".join(
            f'<a href="{man[i]["shot_url"]}" target="_blank" rel="noopener">'
            f'<img loading="lazy" src="{datauri(man[i]["shot_id"])}" alt="">'
            f'<span>{man[i]["designer"]}</span></a>'
            for i in st["shots"]
        )
        f = style_facets(st["shots"], facets)
        tags = "".join(f'<b class="dev">{d}</b>' for d in f["devices"]) + "".join(
            f'<b>{a}<em>{f["artifact_counts"][a]}</em></b>' for a in f["artifacts"]
        )
        parts.append(
            f'<div class="style"><div class="hd"><span class="nm">{st["name"]}</span>'
            f'<span class="pr">{st["pairing"]}</span>'
            f'<span class="ct">{len(st["shots"])} shots</span></div>'
            f'<p class="cc">{st["concept"]}</p>'
            f'<div class="tg">{tags}</div>'
            f'<div class="sw">{sw}</div><div class="gr">{cells}</div></div>'
        )

parts.append("</div>")
out = os.path.join(ROOT, "sources", "catalog-review.html")
open(out, "w", encoding="utf-8").write("\n".join(parts))
print("wrote", out)
