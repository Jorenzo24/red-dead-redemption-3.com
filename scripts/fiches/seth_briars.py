"""Seth Briars, reference fiche (v3, Oct 2026, medium tier).

Same pipeline as the other v3 fiches (scripts/v3/PROCEDURE.md). The base (meta, facts, intro, Development,
Reception) is rebuilt in scripts/fiches/parts/seth_D.py; the body comes from seth_A..C.
"""
import copy


def two(en, fr): return {"en": en, "fr": fr}


def build(cl, CH):
    import importlib
    P = {k: importlib.import_module(f"fiches.parts.seth_{k}") for k in "ABCD"}
    d = copy.deepcopy(P["D"].BASE)
    keep = {sec["summary"]["en"]: sec for sec in d.get("sections", [])}

    def fix(blocks):
        out = []
        for b in blocks:
            b = dict(b)
            if "chapter" in b and not isinstance(b["chapter"], tuple):
                b["chapter"] = CH[b["chapter"]]
            out.append(b)
        return out

    def sec(en, fr, blocks, open_=False):
        blocks = fix(blocks)
        if blocks and "h3" in blocks[0] and blocks[0]["h3"]["en"].strip().lower().startswith(en.lower()[:10]):
            blocks = blocks[1:]
        x = {"summary": {"en": en, "fr": fr}, "blocks": blocks}
        if open_:
            x["open"] = True
        return x

    sections = [
        sec("Biography", "Biographie", P["A"].BLOCKS, open_=True),
        sec("Personality", "Personnalité", P["B"].BLOCKS_PERSONALITY),
        sec("Grave robbing, weapons and horse", "Pillage de tombes, armes et cheval", P["B"].BLOCKS_SKILLS),
        sec("Missions", "Missions", P["C"].BLOCKS_MISSIONS),
        sec("Quotes", "Citations", P["C"].BLOCKS_QUOTES),
    ]
    for k in ("Development and performance", "Reception"):
        if k in keep:
            sections.append(keep[k])
    sections += [
        sec("Other media and legacy", "Autres médias et postérité", P["C"].BLOCKS_MEDIA),
        sec("Trivia", "Anecdotes", P["C"].BLOCKS_TRIVIA),
    ]
    d["sections"] = sections
    d["relationships"] = P["B"].RELATIONSHIPS
    d["rel_after"] = 1
    d["gallery"] = GALLERY
    d["updated"] = "2026-10-21"
    return d


# Gallery: official art and in-game captures sourced from the Red Dead Wiki
# (rights checked by Joseph before publication), chronological.
def _g(n, alt_en, alt_fr, cap_en, cap_fr):
    return {"img": f"gallery-{n}.jpeg", "alt": two(alt_en, alt_fr), "cap": two(cap_en, cap_fr)}

GALLERY = [
    _g(1, "Close-up of Seth Briars in a battered hat", "Gros plan de Seth Briars, chapeau cabossé",
       "Seth Briars in Red Dead Redemption.", "Seth Briars dans Red Dead Redemption."),
    _g(2, "Seth walking among graves in daylight", "Seth marchant entre des tombes en plein jour",
       "Seth in a cemetery in \"Exhuming and Other Fine Hobbies\".", "Seth dans un cimetière dans \"Exhuming and Other Fine Hobbies\"."),
    _g(3, "Seth and John Marston at night", "Seth et John Marston de nuit",
       "Seth and John at night in \"A Gentle Drive with Friends\".", "Seth et John de nuit dans \"A Gentle Drive with Friends\"."),
    _g(4, "Seth on the wall of a fort", "Seth sur le rempart d'un fort",
       "Seth on the wall of Fort Mercer during the assault.", "Seth sur le rempart de Fort Mercer pendant l'assaut."),
    _g(5, "Seth holding a light inside a dark building", "Seth tenant une lumière dans un bâtiment sombre",
       "Seth searching a building in \"Let the Dead Bury Their Dead\".", "Seth fouille un bâtiment dans \"Let the Dead Bury Their Dead\"."),
]
