"""Molly O'Shea, reference fiche (v3, Oct 2026, medium tier).

Same pipeline as John, Arthur, Dutch, Sadie, Micah, Hosea, Charles, Bill, Javier, Abigail and Jack. His page came from
the v2 entry in _enrich.py, so the base (meta, facts, intro, Development, Reception)
is rebuilt in scripts/fiches/parts/molly_D.py; the body comes from molly_A..C.
"""
import copy


def two(en, fr): return {"en": en, "fr": fr}


def build(cl, CH):
    import importlib
    P = {k: importlib.import_module(f"fiches.parts.molly_{k}") for k in "ABCD"}
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
        sec("Skills, weapons and horses", "Compétences, armes et chevaux", P["B"].BLOCKS_SKILLS),
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
    d["updated"] = "2026-10-20"
    return d


# Gallery: official art and in-game captures sourced from the Red Dead Wiki
# (rights checked by Joseph before publication), chronological.
def _g(n, alt_en, alt_fr, cap_en, cap_fr):
    return {"img": f"gallery-{n}.jpeg", "alt": two(alt_en, alt_fr), "cap": two(cap_en, cap_fr)}

GALLERY = [
    _g(1, "Close-up of Molly O'Shea with a fan", "Gros plan de Molly O'Shea avec un éventail",
       "Molly in 1899.", "Molly en 1899."),
    _g(2, "Molly in a dark coat by a cabin", "Molly en manteau sombre près d'une cabane",
       "Molly at Colter.", "Molly à Colter."),
    _g(3, "Close-up of Molly in a green dress", "Gros plan de Molly en robe verte",
       "Molly at Horseshoe Overlook.", "Molly à Horseshoe Overlook."),
    _g(4, "Molly sitting on a cot with a fan", "Molly assise sur un lit de camp, un éventail à la main",
       "In Dutch's tent at Horseshoe Overlook.", "Dans la tente de Dutch à Horseshoe Overlook."),
    _g(5, "Molly reading a book on a rock", "Molly lisant un livre sur un rocher",
       "Reading at Horseshoe Overlook.", "En pleine lecture à Horseshoe Overlook."),
    _g(6, "Molly resting on a rock with a cigarette", "Molly allongée sur un rocher, une cigarette à la main",
       "Molly with a cigarette.", "Molly, une cigarette à la main."),
    _g(7, "Molly standing against a tree", "Molly debout contre un arbre",
       "Molly at Clemens Point.", "Molly à Clemens Point."),
    _g(8, "Molly standing with her arms folded", "Molly debout, les bras croisés",
       "Molly by Flat Iron Lake.", "Molly au bord du lac Flat Iron."),
    _g(9, "Molly sitting by a lake shore", "Molly assise au bord d'un lac",
       "Resting at Clemens Point.", "Au repos à Clemens Point."),
    _g(10, "Close-up of Molly by a tree", "Gros plan de Molly près d'un arbre",
       "During \"An Honest Mistake\".", "Pendant \"An Honest Mistake\"."),
    _g(11, "Character model of Molly in a green gown", "Modèle du personnage de Molly en robe verte",
       "Her cut outfit for \"The Gilded Cage\".", "Sa tenue coupée pour \"The Gilded Cage\"."),
]
