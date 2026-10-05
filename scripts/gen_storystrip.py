#!/usr/bin/env python3
"""Regenerate the "In the story" chapter strip on every character fiche.

Rule: a chapter appears on a fiche when that chapter's story guide links to the
fiche (EN guide -> /characters/<slug>/). No hand-picking: the strip mirrors the
guides. Fiches no guide links to get an empty zone (nothing rendered).

The zone sits right after the facts grid (</dl>), delimited by
<!-- @storystrip:start --> / <!-- @storystrip:end -->. On first run the markers
are inserted. Idempotent. Run: python scripts/gen_storystrip.py
Re-run whenever a story guide gains or loses a character link.
"""
import glob, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
START, END = "<!-- @storystrip:start -->", "<!-- @storystrip:end -->"

# (game, en_slug, fr_slug, chip_en, chip_fr, label_en, label_fr), story order per game
CHAPTERS = [
 ("rdr2", "rdr2-chapter-1-colter", "rdr2-chapitre-1-colter", "1", "1", "Chapter 1: Colter", "Chapitre 1 : Colter"),
 ("rdr2", "rdr2-chapter-2-horseshoe-overlook", "rdr2-chapitre-2-horseshoe-overlook", "2", "2", "Chapter 2: Horseshoe Overlook", "Chapitre 2 : Horseshoe Overlook"),
 ("rdr2", "rdr2-chapter-3-clemens-point", "rdr2-chapitre-3-clemens-point", "3", "3", "Chapter 3: Clemens Point", "Chapitre 3 : Clemens Point"),
 ("rdr2", "rdr2-chapter-4-saint-denis", "rdr2-chapitre-4-saint-denis", "4", "4", "Chapter 4: Saint Denis", "Chapitre 4 : Saint-Denis"),
 ("rdr2", "rdr2-chapter-5-guarma", "rdr2-chapitre-5-guarma", "5", "5", "Chapter 5: Guarma", "Chapitre 5 : Guarma"),
 ("rdr2", "rdr2-chapter-6-beaver-hollow", "rdr2-chapitre-6-beaver-hollow", "6", "6", "Chapter 6: Beaver Hollow", "Chapitre 6 : Beaver Hollow"),
 ("rdr2", "rdr2-epilogue-part-1-pronghorn-ranch", "rdr2-epilogue-partie-1-pronghorn-ranch", "E1", "É1", "Epilogue I: Pronghorn Ranch", "Épilogue I : Pronghorn Ranch"),
 ("rdr2", "rdr2-epilogue-part-2-beechers-hope", "rdr2-epilogue-partie-2-beechers-hope", "E2", "É2", "Epilogue II: Beecher's Hope", "Épilogue II : Beecher's Hope"),
 ("rdr1", "rdr1-act-1-new-austin", "rdr1-acte-1-new-austin", "I", "I", "Act I: New Austin", "Acte I : New Austin"),
 ("rdr1", "rdr1-act-2-nuevo-paraiso", "rdr1-acte-2-nuevo-paraiso", "II", "II", "Act II: Nuevo Paraíso", "Acte II : Nuevo Paraíso"),
 ("rdr1", "rdr1-act-3-west-elizabeth", "rdr1-acte-3-west-elizabeth", "III", "III", "Act III: West Elizabeth", "Acte III : West Elizabeth"),
]
GAMES = [("rdr2", "Red Dead Redemption 2"), ("rdr1", "Red Dead Redemption")]


def _mapping():
    m = {}
    for ch in CHAPTERS:
        s = open(os.path.join(ROOT, "story", ch[1], "index.html"), encoding="utf-8").read()
        for slug in set(re.findall(r'href="/characters/([a-z0-9-]+)/"', s)):
            m.setdefault(slug, []).append(ch)
    return m


def _strip(chs, lang):
    if not chs:
        return f"                {START}\n                {END}"
    title = "In the story" if lang == "en" else "Dans l'histoire"
    out = [f"                {START}",
           f'                <nav class="storystrip" aria-label="{title}">',
           f'                    <p class="storystrip__title">{title}</p>']
    for game, gname in GAMES:
        row = [c for c in chs if c[0] == game]
        if not row:
            continue
        out.append('                    <div class="storystrip__row">')
        out.append(f'                        <span class="storystrip__game">{gname}</span>')
        out.append('                        <ul class="storystrip__chips">')
        for _g, en, fr, chip_en, chip_fr, lab_en, lab_fr in row:
            href = f"/story/{en}/" if lang == "en" else f"/fr/histoire/{fr}/"
            chip, lab = (chip_en, lab_en) if lang == "en" else (chip_fr, lab_fr)
            out.append(f'                            <li><a href="{href}" title="{lab}" aria-label="{lab}">{chip}</a></li>')
        out.append("                        </ul>")
        out.append("                    </div>")
    out += ["                </nav>", f"                {END}"]
    return "\n".join(out)


def _apply(path, block):
    s = open(path, encoding="utf-8").read()
    if START in s and END in s:
        new = re.sub(re.escape(START) + r".*?" + re.escape(END), lambda _m: block.strip(), s, count=1, flags=re.S)
    else:
        if s.count("</dl>") != 1:
            raise SystemExit(f"ERROR: expected exactly one </dl> in {path}")
        new = s.replace("</dl>\n", "</dl>\n\n" + block + "\n", 1)
    if new != s:
        open(path, "w", encoding="utf-8").write(new)
        return True
    return False


def regenerate():
    m = _mapping()
    changed = 0
    for d in sorted(glob.glob(os.path.join(ROOT, "characters", "*", ""))):
        slug = os.path.basename(os.path.dirname(d))
        chs = m.get(slug, [])
        for path, lang in ((os.path.join(d, "index.html"), "en"),
                           (os.path.join(ROOT, "fr", "personnages", slug, "index.html"), "fr")):
            if os.path.isfile(path) and _apply(path, _strip(chs, lang)):
                changed += 1
    return changed


if __name__ == "__main__":
    print("updated", regenerate(), "pages")
