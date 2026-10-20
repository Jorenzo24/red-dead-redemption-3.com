#!/usr/bin/env python3
"""mkmodule.py <key> <module_name> "<Display Name>" [--model uncle] [--captions PATH] [--force]
-> scripts/fiches/<module_name>.py, built from an existing v3 fiche module + the gallery captions.

--model    existing module in scripts/fiches/ to copy build() from (default: uncle). Its docstring is replaced,
           its parts prefix becomes <key>, and d["updated"] is set to TODAY's date.
--captions JSON list of [alt_en, alt_fr, cap_en, cap_fr], one per gallery image, in gallery order
           (default: work/<key>/gal/captions.json).
Refuses to overwrite an existing module unless --force. Section titles are the model's: rename them in the new
module if the fiche needs another one (e.g. Cornwall's "Business empire" instead of "Skills, weapons and horses").
"""
import sys, os, re, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _paths import R, kdir, today, rel
from datetime import date
a = sys.argv[1:]
def opt(name, default=None):
    if name in a:
        i = a.index(name); v = a[i + 1]; del a[i:i + 2]; return v
    return default
force = "--force" in a
if force: a.remove("--force")
model = opt("--model", "uncle"); cap = opt("--captions")
if len(a) < 3:
    raise SystemExit(__doc__)
key, mod, name = a[:3]
cap = cap or kdir(key) + "gal/captions.json"
F = R + "scripts/fiches/"
out = F + mod + ".py"
if os.path.exists(out) and not force:
    raise SystemExit(f"{rel(out)} exists: pass --force to overwrite")
s = open(F + model + ".py", encoding="utf-8").read().split("# Gallery:")[0]
if not re.search(r"def build\(cl, CH\)", s):
    print("WARNING: model build() signature is not (cl, CH); pick a model like uncle or leviticus_cornwall")
pm = re.search(r"fiches\.parts\.(\w+?)_\{k\}", s)
if not pm:
    raise SystemExit("model module does not import fiches.parts.<prefix>_{k}")
s = s.replace(f"fiches.parts.{pm.group(1)}_", f"fiches.parts.{key}_")
doc = (f'"""{name}, reference fiche (v3, {date.today().strftime("%b %Y")}, medium tier).\n\n'
       f'Same pipeline as the other v3 fiches (scripts/v3/PROCEDURE.md). The base (meta, facts, intro, Development,\n'
       f'Reception) is rebuilt in scripts/fiches/parts/{key}_D.py; the body comes from {key}_A..C.\n"""')
s = re.sub(r'^""".*?"""', lambda m: doc, s, count=1, flags=re.S)
s, n = re.subn(r'd\["updated"\] = "[0-9-]+"', f'd["updated"] = "{today()}"', s)
if not n:
    print('WARNING: no d["updated"] line found in the model')
G = json.load(open(cap, encoding="utf-8"))
def esc(x): return x.replace('\\', '\\\\').replace('"', '\\"')
L = ['# Gallery: official art and in-game captures sourced from the Red Dead Wiki',
     '# (rights checked by Joseph before publication), chronological.',
     'def _g(n, alt_en, alt_fr, cap_en, cap_fr):',
     '    return {"img": f"gallery-{n}.jpeg", "alt": two(alt_en, alt_fr), "cap": two(cap_en, cap_fr)}', '', 'GALLERY = [']
for i, g in enumerate(G, 1):
    L.append(f'    _g({i}, "{esc(g[0])}", "{esc(g[1])}",\n       "{esc(g[2])}", "{esc(g[3])}"),')
L.append(']\n')
open(out, "w", encoding="utf-8").write(s + "\n".join(L))
print("wrote", rel(out), f"({len(G)} gallery entries, updated {today()})")
