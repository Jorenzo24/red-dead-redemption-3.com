#!/usr/bin/env python3
"""Regenerate the grouped card region of the Characters listing pages from the
registry (scripts/characters_registry.py). Renders only characters whose fiche
is actually published (live dir exists), grouped by faction, alphabetical within
each group.

Idempotent. Run standalone (`python scripts/gen_listing.py`) or import and call
regenerate(). The daily drip calls this after moving a fiche live, so new fiches
land in the right group automatically.

The region is delimited by <!-- @charlist:start --> / <!-- @charlist:end -->.
On first run (markers absent) it replaces the old flat grid (…<!-- @ccards --></div>).
"""
import os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from characters_registry import CHARACTERS, GROUPS

# listing file -> (img_prefix, link_prefix, lang)
FILES = [
    ("characters/index.html",     "../",   "/characters/",     "en"),
    ("fr/personnages/index.html", "../../","/fr/personnages/", "fr"),
]

START = "<!-- @charlist:start -->"
END = "<!-- @charlist:end -->"


def _published():
    d = os.path.join(ROOT, "characters")
    return {n for n in os.listdir(d) if os.path.isdir(os.path.join(d, n))}


def _ccard(slug, name, role, img_prefix, link_prefix, lang):
    if lang == "en":
        tag, cta, aria = "Character", "View profile &rarr;", f"{name} character profile"
    else:
        tag, cta, aria = "Personnage", "Voir le profil &rarr;", f"Fiche du personnage {name}"
    return (
        f'                        <a class="ccard" href="{link_prefix}{slug}/" aria-label="{aria}">\n'
        f'                            <img src="{img_prefix}assets/characters/{slug}/portrait.jpeg" alt="{name}" loading="lazy" width="1000" height="562">\n'
        f'                            <span class="ccard__overlay">\n'
        f'                                <span class="ccard__tag">{tag}</span>\n'
        f'                                <span class="ccard__name">{name}</span>\n'
        f'                                <span class="ccard__role">{role}</span>\n'
        f'                                <span class="ccard__cta">{cta}</span>\n'
        f'                            </span>\n'
        f'                        </a>\n'
    )


def _region(img_prefix, link_prefix, lang):
    pub = _published()
    out = [START]
    for key, title_en, title_fr, note_en, note_fr in GROUPS:
        members = [c for c in CHARACTERS if c[4] == key and c[0] in pub]
        members.sort(key=lambda c: c[1].lower())
        if not members:
            continue
        title = title_en if lang == "en" else title_fr
        note = note_en if lang == "en" else note_fr
        out.append('                <div class="char-group">')
        out.append(f'                    <h2 class="char-group__title">{title}</h2>')
        out.append(f'                    <p class="char-group__note">{note}</p>')
        out.append('                    <div class="card-grid card-grid--portraits">')
        for slug, name, role_en, role_fr, _g in members:
            role = role_en if lang == "en" else role_fr
            out.append(_ccard(slug, name, role, img_prefix, link_prefix, lang).rstrip("\n"))
        out.append('                    </div>')
        out.append('                </div>')
    out.append("                " + END)
    return "\n".join(out)


def regenerate():
    changed = []
    for relpath, img_prefix, link_prefix, lang in FILES:
        p = os.path.join(ROOT, relpath)
        s = open(p, encoding="utf-8").read()
        region = _region(img_prefix, link_prefix, lang)
        if START in s and END in s:
            new = re.sub(re.escape(START) + r".*?" + re.escape(END), region, s, count=1, flags=re.S)
        else:
            # first run: replace the old flat grid (…<!-- @ccards --></div>)
            new = re.sub(
                r'<div class="card-grid card-grid--portraits">.*?<!-- @ccards -->\s*</div>',
                region, s, count=1, flags=re.S)
        if new != s:
            open(p, "w", encoding="utf-8").write(new)
            changed.append(relpath)
    return changed


if __name__ == "__main__":
    ch = regenerate()
    print("regenerated:", ", ".join(ch) if ch else "no changes")
