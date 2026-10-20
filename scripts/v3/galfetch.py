#!/usr/bin/env python3
"""galfetch.py <key> "<Wiki page>" -> work/<key>/gal/: candidates.json, dl/NNN.img, contact.jpg (numbered contact sheet).

Lists every image >= 480 px wide on the wiki page and its /Gallery subpage, downloads them (CDN needs Referer +
Accept + Sec-Fetch headers since Sept 2026; it answers WebP whatever the extension) and builds a contact sheet.
Idempotent: files already in dl/ are not downloaded again. Read contact.jpg BEFORE choosing (reject cards,
promo art with text/logos, unreadable interiors, wrong person).
"""
import json, subprocess, urllib.parse, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _paths import UA, api, kdir, rel
from PIL import Image, ImageDraw
if len(sys.argv) < 3:
    raise SystemExit(__doc__)
key, page = sys.argv[1], sys.argv[2]
D = kdir(key) + "gal/"; os.makedirs(D + "dl", exist_ok=True)
c = {}
for p in [page, page + "/Gallery"]:
    r = api("action=query&generator=images&gimlimit=500&prop=imageinfo|fileusage&iiprop=url|size&fulimit=5&format=json&titles=" + urllib.parse.quote(p))
    for x in r.get("query", {}).get("pages", {}).values():
        ii = x.get("imageinfo", [{}])[0]
        if ii.get("width", 0) >= 480 and not x["title"].lower().endswith(".svg"):
            c[x["title"]] = ii
json.dump(c, open(D + "candidates.json", "w"), indent=1)
items = sorted(c.items())
for i, (t, ii) in enumerate(items):
    f = f"{D}dl/{i:03d}.img"
    if not os.path.exists(f):
        subprocess.run(["curl", "-s", "-A", UA, "-e", "https://reddead.fandom.com/", "-H", "Accept: image/avif,image/webp,image/png,image/*;q=0.8",
                        "-H", "Sec-Fetch-Dest: image", "-H", "Sec-Fetch-Mode: no-cors", "-H", "Sec-Fetch-Site: cross-site", "-o", f, ii["url"]])
    print(i, t, ii["width"], ii["height"])
W, H = 300, 200; cols = 6; rows = max(1, (len(items) + cols - 1) // cols)
sh = Image.new("RGB", (cols * W, rows * (H + 20)), "white"); d = ImageDraw.Draw(sh)
for k in range(len(items)):
    try:
        im = Image.open(f"{D}dl/{k:03d}.img").convert("RGB"); im.thumbnail((W, H))
    except Exception:
        continue
    x, y = (k % cols) * W, (k // cols) * (H + 20); sh.paste(im, (x, y)); d.text((x + 3, y + H + 3), f"{k:03d}", fill="black")
sh.save(D + "contact.jpg", quality=80)
print(len(items), "candidates; contact sheet:", rel(D + "contact.jpg"))
