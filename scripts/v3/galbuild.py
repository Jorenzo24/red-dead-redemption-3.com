#!/usr/bin/env python3
"""galbuild.py <key> <slug> 'idx:fill|obj,...' -> 1400x787 crops in work/<key>/gal/out/, review.jpg, copy to assets.

idx = number on the contact sheet; fill = photo (cover crop, or sharp image centred on a blurred copy when the
ratio is far from 16:9); obj = object/cut-out on a dark background. Order of the spec = gallery order
(chronological). The spec is saved to gal/spec.txt so another session can rebuild the same gallery
(re-run galfetch first if gal/dl/ is missing: downloads are not committed).
Writes assets/characters/<slug>/gallery-N.jpeg + .webp (existing gallery-N files are overwritten).
"""
import sys, os, shutil
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _paths import R, kdir, rel
from PIL import Image, ImageFilter
if len(sys.argv) < 4:
    raise SystemExit(__doc__)
key, slug, spec = sys.argv[1], sys.argv[2], sys.argv[3]
D = kdir(key) + "gal/"; os.makedirs(D + "out", exist_ok=True)
for f in os.listdir(D + "out"):
    os.remove(D + "out/" + f)
W, H = 1400, 787
def fill(src):
    im = Image.open(src).convert("RGB"); r = im.width / im.height
    if r >= W / H * 0.88 and r < 2.6:
        s = max(W / im.width, H / im.height); t = im.resize((round(im.width * s), round(im.height * s)), Image.LANCZOS)
        x = (t.width - W) // 2; y = (t.height - H) // 2; return t.crop((x, y, x + W, y + H))
    s = max(W / im.width, H / im.height); bg = im.resize((round(im.width * s), round(im.height * s))); x = (bg.width - W) // 2; y = (bg.height - H) // 2
    bg = bg.crop((x, y, x + W, y + H)).filter(ImageFilter.GaussianBlur(28)).point(lambda v: int(v * 0.7))
    s = min(W / im.width, H / im.height); fg = im.resize((round(im.width * s), round(im.height * s)), Image.LANCZOS)
    bg.paste(fg, ((W - fg.width) // 2, (H - fg.height) // 2)); return bg
def obj(src):
    im = Image.open(src).convert("RGBA"); bg = Image.new("RGB", (W, H), "#18130f")
    s = min(W * 0.8 / im.width, H * 0.8 / im.height); fg = im.resize((round(im.width * s), round(im.height * s)), Image.LANCZOS)
    bg.paste(fg, ((W - fg.width) // 2, (H - fg.height) // 2), fg); return bg
items = [x.split(':') for x in spec.split(',')]
for n, (k, m) in enumerate(items, 1):
    im = (obj if m == "obj" else fill)(f"{D}dl/{int(k):03d}.img")
    im.save(f"{D}out/gallery-{n}.jpeg", quality=84, optimize=True, progressive=True); im.save(f"{D}out/gallery-{n}.webp", quality=80)
sh = Image.new("RGB", (5 * 280, ((len(items) + 4) // 5) * 158), "white")
for i in range(len(items)):
    t = Image.open(f"{D}out/gallery-{i + 1}.jpeg").resize((280, 158)); sh.paste(t, ((i % 5) * 280, (i // 5) * 158))
sh.save(D + "review.jpg")
open(D + "spec.txt", "w").write(spec + "\n")
A = R + f"assets/characters/{slug}/"; os.makedirs(A, exist_ok=True)
for f in os.listdir(D + "out"):
    shutil.copy(D + "out/" + f, A + f)
print(len(items), "images ->", rel(A), "; check", rel(D + "review.jpg"))
