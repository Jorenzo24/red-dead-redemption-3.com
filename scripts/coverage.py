#!/usr/bin/env python3
"""Coverage check: compare one of our fiches with its Red Dead Wiki page.

Usage: python scripts/coverage.py <slug> "<Wiki_Page_Title>" [--save DIR]

Prints the wiki's sections (EN and FR) with their word counts, and our fiche's
sections with theirs, so the gap is visible section by section. With --save,
also writes the raw wikitext (en.txt, fr.txt) to DIR for drafting agents.
Not deployed (scripts/ is excluded from .cpanel.yml).
"""
import json, os, re, subprocess, sys, urllib.parse

UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/128.0 Safari/537.36")
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def wikitext(host, title):
    url = (f"https://{host}/api.php?action=parse&page={urllib.parse.quote(title)}"
           "&prop=wikitext&format=json&redirects=1")
    out = subprocess.run(["curl", "-s", "-A", UA, url], capture_output=True, text=True).stdout
    return json.loads(out)["parse"]["wikitext"]["*"]


def plain_words(w):
    w = re.sub(r"<ref[^>]*>.*?</ref>|<ref[^>]*/>", " ", w, flags=re.S)
    w = re.sub(r"\{\{[^{}]*\}\}", " ", w)
    w = re.sub(r"\[\[(?:File|Image|Fichier):[^\]]*\]\]", " ", w)
    w = re.sub(r"\[\[(?:[^|\]]*\|)?([^\]]*)\]\]", r"\1", w)
    w = re.sub(r"<[^>]+>|'''?|==+", " ", w)
    return len(w.split())


def wiki_sections(w):
    parts = re.split(r"^(=+)\s*(.*?)\s*=+\s*$", w, flags=re.M)
    rows = [("(intro)", 1, plain_words(parts[0]))]
    for i in range(1, len(parts), 3):
        rows.append((re.sub(r"<[^>]+>|''", "", parts[i + 1]), len(parts[i]) - 1, plain_words(parts[i + 2])))
    return rows


def our_sections(path):
    s = open(path, encoding="utf-8").read()
    body = s[s.find('<div class="profile__intro">'):s.find('<aside class="related"')]
    chunks = re.split(r"<summary>(.*?)</summary>", body)
    rows = [("(intro + key facts + facts)", len(re.sub(r"<[^>]+>", " ", chunks[0]).split()))]
    for i in range(1, len(chunks), 2):
        rows.append((chunks[i], len(re.sub(r"<[^>]+>", " ", chunks[i + 1]).split())))
    return rows


def main():
    slug, title = sys.argv[1], sys.argv[2]
    save = sys.argv[sys.argv.index("--save") + 1] if "--save" in sys.argv else None
    total = {}
    for lang, host in (("en", "reddead.fandom.com"), ("fr", "reddead.fandom.com/fr")):
        try:
            w = wikitext(host, title)
        except Exception as e:
            print(f"[{lang}] wiki page not found ({e})"); continue
        if save:
            os.makedirs(save, exist_ok=True)
            open(os.path.join(save, f"{lang}.txt"), "w", encoding="utf-8").write(w)
        rows = wiki_sections(w)
        total[lang] = sum(r[2] for r in rows)
        print(f"\n=== Red Dead Wiki {lang.upper()}: {total[lang]} words")
        for name, lvl, n in rows:
            print(f"{'  ' * (lvl - 1)}{name}: {n}")
    for lang, rel in (("en", f"characters/{slug}/index.html"), ("fr", f"fr/personnages/{slug}/index.html")):
        rows = our_sections(os.path.join(ROOT, rel))
        n = sum(r[1] for r in rows)
        ref = total.get(lang)
        print(f"\n=== Our fiche {lang.upper()}: {n} words" + (f" ({n * 100 // ref}% of the wiki)" if ref else ""))
        for name, k in rows:
            print(f"  {name}: {k}")


if __name__ == "__main__":
    main()
