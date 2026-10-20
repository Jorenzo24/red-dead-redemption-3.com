"""Shared paths and helpers for the v3 fiche pipeline (portable: everything is derived from the repo).

R  = repo root (two levels above this file)
V3 = scripts/v3/
W  = scripts/v3/work/            one folder per fiche: W/<key>/
M  = scripts/v3/work/_m/         ONE shared cache of mission pages and transcripts (gitignored, re-fetchable)
"""
import json, os, re, subprocess, time, urllib.parse
from datetime import date

V3 = os.path.dirname(os.path.abspath(__file__)) + "/"
R = os.path.dirname(os.path.dirname(V3.rstrip("/"))) + "/"
W = V3 + "work/"
M = W + "_m/"
TEMPLATES = V3 + "templates/"
RULES = V3 + "rules/"
SOURCES = V3 + "sources/"

UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/128.0 Safari/537.36")
API = "https://reddead.fandom.com/api.php?"


def rel(p):
    """Repo-relative path (what goes into briefs and prompts, so they work on any device)."""
    return os.path.relpath(p, R)


def kdir(key):
    if not re.fullmatch(r"[a-z][a-z0-9]*", key):
        raise SystemExit(f"bad key {key!r}: use the parts prefix, lowercase letters/digits only (e.g. linton, mary)")
    return W + key + "/"


def today():
    return date.today().isoformat()


def api(query):
    out = subprocess.run(["curl", "-s", "-A", UA, API + query], capture_output=True, text=True).stdout
    return json.loads(out)


def wikitext(title, tries=3):
    for _ in range(tries):
        try:
            r = api("action=parse&prop=wikitext&format=json&redirects=1&page=" + urllib.parse.quote(title))
            return r["parse"]["wikitext"]["*"] if "parse" in r else None
        except Exception:
            time.sleep(3)
    return None


def mfile(title):
    """Cache file name for a wiki page title (same naming as the old scratchpad m/ folders)."""
    return M + re.sub(r"[^A-Za-z0-9]+", "_", title).strip("_") + ".txt"


def fetch_cached(title):
    """Fetch a wiki page into the shared cache unless it is already there. Returns the path or None."""
    os.makedirs(M, exist_ok=True)
    f = mfile(title)
    if os.path.exists(f) and os.path.getsize(f) > 0:
        return f
    s = wikitext(title)
    time.sleep(0.3)
    if s:
        open(f, "w", encoding="utf-8").write(s)
        return f
    return None


def live_slugs():
    """Published fiches = folders under characters/ (the drip creates them on publish)."""
    return sorted(d for d in os.listdir(R + "characters") if os.path.isfile(R + f"characters/{d}/index.html"))


def queue_slugs():
    q = R + "_queue/"
    return sorted(re.sub(r"^\d+-", "", d) for d in os.listdir(q) if os.path.isdir(q + d)) if os.path.isdir(q) else []


def v3_done():
    """[(alias, module, parts_prefix, slug)] for every build( entry in _FULL of scripts/_enrich.py."""
    s = open(R + "scripts/_enrich.py", encoding="utf-8").read()
    imp = re.search(r"^from fiches import (.+)$", s, re.M).group(1)
    alias2mod = {a.strip(): m.strip() for m, a in (x.split(" as ") for x in imp.split(","))}
    full = re.search(r"^_FULL = \[(.+)\]$", s, re.M).group(1)
    out = []
    for a in re.findall(r"(\w+)\.build\(", full):
        mod = alias2mod[a]
        src = open(R + f"scripts/fiches/{mod}.py", encoding="utf-8").read()
        m = re.search(r"fiches\.parts\.(\w+?)_\{k\}", src)
        out.append((a, mod, m.group(1) if m else None, mod.replace("_", "-")))
    return out


def fill(text, **kw):
    """Replace {{NAME}} placeholders. Unknown placeholders are left visible on purpose."""
    for k, v in kw.items():
        text = text.replace("{{" + k + "}}", str(v))
    return text
