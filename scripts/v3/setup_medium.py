#!/usr/bin/env python3
"""Set up (or refresh) a medium-tier v3 fiche work folder: wiki text, mission pages/transcripts, brief, prompts, assembler.

First run:
  python3 scripts/v3/setup_medium.py <key> <slug> "<Wiki page title>" ["<blurb>"] [--name "Display Name"] [--model uncle]
Refresh on another device / after git pull (arguments are re-read from work/<key>/setup.json):
  python3 scripts/v3/setup_medium.py <key>

<key>  = the parts prefix (scripts/fiches/parts/<key>_A.py ...). Pass it explicitly: "mary" is Mary-Beth, Mary Linton is "linton".
<blurb> = 2-5 lines of fiche-specific guidance for the drafters (games, key missions, death, actor to verify).
Idempotent: pages already in the shared cache work/_m/ are not fetched again; generated files are rewritten
(BRIEF.md, prompts/, assemble.py, live_slugs.txt, missions.txt); FIX_RULES.md is created once and never overwritten.
"""
import json, os, re, subprocess, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _paths import R, W, M, TEMPLATES, RULES, SOURCES, kdir, rel, fill, fetch_cached, live_slugs, v3_done, today

args = sys.argv[1:]
opts = {}
for o in ("--name", "--model"):
    if o in args:
        i = args.index(o); opts[o[2:]] = args[i + 1]; del args[i:i + 2]
if not args:
    raise SystemExit(__doc__)
key = args[0]; D = kdir(key)
cfgf = D + "setup.json"
if len(args) == 1:
    if not os.path.exists(cfgf):
        raise SystemExit(f"no {rel(cfgf)}: give <slug> and <Wiki title> on the first run")
    cfg = json.load(open(cfgf, encoding="utf-8"))
else:
    cfg = {"key": key, "slug": args[1], "title": args[2], "blurb": args[3] if len(args) > 3 else "",
           "name": args[2], "model": "uncle"}
    if os.path.exists(cfgf):
        old = json.load(open(cfgf, encoding="utf-8"))
        cfg["blurb"] = cfg["blurb"] or old.get("blurb", "")
        cfg["name"] = old.get("name", cfg["name"]); cfg["model"] = old.get("model", "uncle")
cfg.update({k: v for k, v in opts.items()})
slug, title, name = cfg["slug"], cfg["title"], cfg["name"]
os.makedirs(D + "fc", exist_ok=True); os.makedirs(D + "prompts", exist_ok=True); os.makedirs(M, exist_ok=True)
json.dump(cfg, open(cfgf, "w", encoding="utf-8"), indent=1, ensure_ascii=False)

# 1. Wiki page (EN + FR) via the repo's coverage tool
if not os.path.exists(D + "en.txt"):
    subprocess.run(["python3", "scripts/coverage.py", slug, title, "--save", D], cwd=R, capture_output=True)
if not os.path.exists(D + "en.txt"):
    raise SystemExit(f"could not fetch the wiki page {title!r} (network? wrong title?)")

# 2. Mission pages + transcripts listed in "Mission appearances", into the shared cache
w = open(D + "en.txt", encoding="utf-8").read()
a = re.search(r"==\s*Mission [Aa]ppearances\s*==", w)
ms = []
if a:
    sec = w[a.end():]; b = re.search(r"\n==[^=]", sec); sec = sec[:b.start()] if b else sec
    ms = list(dict.fromkeys(re.findall(r"\[\[([^|\]#]+)", sec)))
lines = []
for t in ms:
    for suf in ("", "/dialogues"):
        f = fetch_cached(t + suf)
        lines.append(f"{t + suf}\t{rel(f) if f else 'MISSING (no such wiki page)'}")
open(D + "missions.txt", "w", encoding="utf-8").write("\n".join(lines) + "\n")
open(D + "live_slugs.txt", "w").write("\n".join(live_slugs()) + "\n")

# 3. Generated briefs / prompts / assembler
auth = sorted({p for _, _, p, s in v3_done() if p and p != key})
model = cfg["model"]
P = dict(R=R, KEY=key, SLUG=slug, TITLE=title, NAME=name, FIRST=name.split()[0], BLURB=cfg["blurb"],
         KD=rel(D), M=rel(M), RULES=rel(RULES), SOURCES=rel(SOURCES), MODEL=model, TODAY=today(),
         AUTH="{" + ",".join(auth) + "}")
open(D + "BRIEF.md", "w", encoding="utf-8").write(fill(open(TEMPLATES + "BRIEF.md", encoding="utf-8").read(), **P))
open(D + "FC_PROMPT.md", "w", encoding="utf-8").write(fill(open(TEMPLATES + "FC_PROMPT.md", encoding="utf-8").read(), **P))
for f in sorted(os.listdir(TEMPLATES + "prompts")):
    open(D + "prompts/" + f, "w", encoding="utf-8").write(fill(open(TEMPLATES + "prompts/" + f, encoding="utf-8").read(), **P))
if not os.path.exists(D + "FIX_RULES.md"):
    open(D + "FIX_RULES.md", "w", encoding="utf-8").write(fill(open(TEMPLATES + "FIX_RULES.md", encoding="utf-8").read(), **P))
# assemble.py: values injected as JSON literals, so names with apostrophes (O'Driscoll, O'Shea) cannot break it
asm = open(TEMPLATES + "assemble.py", encoding="utf-8").read()
for k, v in (("__SLUG__", slug), ("__TITLE__", title), ("__KEY__", key)):
    asm = asm.replace(k, json.dumps(v, ensure_ascii=False))
open(D + "assemble.py", "w", encoding="utf-8").write(asm)
print(key, slug, f"{len(ms)} missions,", sum(1 for l in lines if "MISSING" not in l), "cache files;", "work dir:", rel(D))
