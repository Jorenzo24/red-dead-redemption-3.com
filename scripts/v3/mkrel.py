#!/usr/bin/env python3
"""mkrel.py <key> <slug> <module> <alias>
-> relationship portraits (600 px wide, JPEG + WebP) for every RELATIONSHIPS entry of parts/<key>_B.py that has
   both "img" and "slug" (copied from that character's live portrait.jpeg), then wires the module into
   scripts/_enrich.py (import "<module> as <alias>" + "<alias>.build(cl, CH)" appended to _FULL).
<alias> must be unique in _enrich.py (look at the existing ones: _un, _co, _lc, ...).
"""
import sys, os, re, importlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _paths import R
if len(sys.argv) < 5:
    raise SystemExit(__doc__)
key, slug, mod, alias = sys.argv[1:5]
sys.path.insert(0, R + 'scripts')
B = importlib.import_module(f'fiches.parts.{key}_B')
from PIL import Image
os.makedirs(R + f'assets/characters/{slug}/rel', exist_ok=True); n = 0
for r in B.RELATIONSHIPS:
    if r.get('img') and r.get('slug'):
        im = Image.open(R + f"assets/characters/{r['slug']}/portrait.jpeg").convert("RGB")
        im = im.resize((600, round(600 * im.height / im.width)), Image.LANCZOS)
        base = R + f"assets/characters/{slug}/rel/{r['img'].rsplit('.', 1)[0]}"
        im.save(base + ".jpeg", quality=82, optimize=True, progressive=True); im.save(base + ".webp", quality=78); n += 1
p = R + 'scripts/_enrich.py'; s = open(p, encoding='utf-8').read()
if f' as {alias}' not in s:
    s = re.sub(r'(from fiches import [^\n]*)\n', lambda m: m.group(1) + f', {mod} as {alias}\n', s, count=1)
    s = re.sub(r'(_FULL = \[[^\n]*)\]\n', lambda m: m.group(1) + f', {alias}.build(cl, CH)]\n', s, count=1)
    open(p, 'w', encoding='utf-8').write(s)
print(slug, n, 'portraits; wired' if f'{alias}.build' in open(p, encoding='utf-8').read() else 'NOT wired')
