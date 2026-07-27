#!/usr/bin/env python3
"""Extract a grounded palette from shot images.

Usage: palette.py <image> [<image> ...]
Prints, per image: dominant colours with coverage %, plus a light/dark read.
Used during style synthesis so palettes are sampled, never guessed.
"""
import sys
from collections import Counter

from PIL import Image


def hexof(rgb):
    return "#%02X%02X%02X" % rgb


def luma(rgb):
    r, g, b = [c / 255 for c in rgb]
    f = lambda c: c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4
    return 0.2126 * f(r) + 0.7152 * f(g) + 0.0722 * f(b)


def analyse(path, k=10):
    im = Image.open(path).convert("RGB")
    im.thumbnail((420, 420))
    data = im.tobytes()
    px = [tuple(data[i:i + 3]) for i in range(0, len(data), 3)]
    total = len(px)

    # quantise to reduce near-identical shades, keep counts
    q = Counter((r // 12 * 12, g // 12 * 12, b // 12 * 12) for r, g, b in px)
    top = q.most_common(k)

    # saturation-weighted accents: colourful pixels that are not the dominant neutral
    def sat(c):
        mx, mn = max(c), min(c)
        return 0 if mx == 0 else (mx - mn) / mx

    accents = Counter(
        (r // 16 * 16, g // 16 * 16, b // 16 * 16)
        for r, g, b in px
        if sat((r, g, b)) > 0.35 and 25 < max(r, g, b) < 250
    )

    bg = top[0][0]
    print(f"\n== {path.split('/')[-1]}")
    print(f"   base: {'DARK' if luma(bg) < 0.2 else 'LIGHT' if luma(bg) > 0.7 else 'MID'} "
          f"({hexof(bg)}, L={luma(bg):.2f})")
    print("   dominant:")
    for c, n in top:
        print(f"     {hexof(c)}  {100*n/total:5.1f}%  L={luma(c):.2f}")
    if accents:
        print("   accents (saturated):")
        for c, n in accents.most_common(6):
            print(f"     {hexof(c)}  {100*n/total:5.1f}%  sat-weighted")
    else:
        print("   accents: none — near-monochrome / desaturated")


if __name__ == "__main__":
    for p in sys.argv[1:]:
        try:
            analyse(p)
        except Exception as e:
            print(f"\n== {p}\n   ERROR: {e}")
