"""Irish, reference fiche (v3, Oct 2026, medium tier).

Same pipeline as the other v3 fiches (scripts/v3/PROCEDURE.md). The base (meta, facts, intro, Development,
Reception) is rebuilt in scripts/fiches/parts/irish_D.py; the body comes from irish_A..C.
"""
import copy


def two(en, fr): return {"en": en, "fr": fr}


def build(cl, CH):
    import importlib
    P = {k: importlib.import_module(f"fiches.parts.irish_{k}") for k in "ABCD"}
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
        sec("Contraband, weapons and horses", "Contrebande, armes et chevaux", P["B"].BLOCKS_SKILLS),
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
    _g(1, "Close-up of Irish, bearded, in a dim room", "Gros plan d'Irish, barbu, dans une pièce sombre",
       "Irish in Red Dead Redemption.", "Irish dans Red Dead Redemption."),
    _g(2, "Irish slumped outside a wooden shack", "Irish affalé devant une cabane en bois",
       "Irish in \"A Frenchman, a Welshman and an Irishman\".", "Irish dans \"A Frenchman, a Welshman and an Irishman\"."),
    _g(3, "Irish drinking from a bottle beside John Marston", "Irish buvant à la bouteille à côté de John Marston",
       "Irish drinking beside John.", "Irish boit à côté de John."),
    _g(4, "Irish on a pale horse beside a wagon", "Irish sur un cheval clair près d'un chariot",
       "Irish with a wagon.", "Irish près d'un chariot."),
    _g(5, "Two nuns facing Irish in a narrow street", "Deux religieuses face à Irish dans une ruelle",
       "Irish and the two nuns.", "Irish et les deux religieuses."),
    _g(6, "Irish gesturing outdoors, John behind him", "Irish faisant un geste en extérieur, John derrière lui",
       "Irish and John in \"We Shall Be Together in Paradise\".", "Irish et John dans \"We Shall Be Together in Paradise\"."),
    _g(7, "Irish on a wooden jetty by the water", "Irish sur un ponton au bord de l'eau",
       "Irish at the river in \"We Shall Be Together in Paradise\".", "Irish au bord du fleuve dans \"We Shall Be Together in Paradise\"."),
]
