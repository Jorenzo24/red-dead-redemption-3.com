"""Bonnie MacFarlane, reference fiche (v3, Oct 2026, medium tier).

Same pipeline as the other v3 fiches (scripts/v3/PROCEDURE.md). The base (meta, facts, intro, Development,
Reception) is rebuilt in scripts/fiches/parts/bonnie_D.py; the body comes from bonnie_A..C.
"""
import copy


def two(en, fr): return {"en": en, "fr": fr}


def build(cl, CH):
    import importlib
    P = {k: importlib.import_module(f"fiches.parts.bonnie_{k}") for k in "ABCD"}
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
    _g(1, "Close-up of Bonnie MacFarlane in a striped blouse", "Gros plan de Bonnie MacFarlane en chemisier rayé",
       "Bonnie in Red Dead Online (1898).", "Bonnie dans Red Dead Online (1898)."),
    _g(2, "Bonnie leaning on a porch rail", "Bonnie accoudée à une rambarde de perron",
       "Bonnie in Red Dead Online.", "Bonnie dans Red Dead Online."),
    _g(3, "Bonnie seated on a porch chair", "Bonnie assise sur une chaise de perron",
       "Bonnie on the porch of the ranch house in Red Dead Online.", "Bonnie sous le porche du ranch dans Red Dead Online."),
    _g(4, "Close-up of Bonnie with her hair tied back", "Gros plan de Bonnie, cheveux attachés",
       "Bonnie in Red Dead Redemption (1911).", "Bonnie dans Red Dead Redemption (1911)."),
    _g(5, "Bonnie talking indoors", "Bonnie parlant dans une pièce",
       "Bonnie at MacFarlane's Ranch.", "Bonnie au ranch MacFarlane."),
    _g(6, "Bonnie and John Marston leaning on a porch rail", "Bonnie et John Marston accoudés à une rambarde",
       "Bonnie and John Marston at MacFarlane's Ranch.", "Bonnie et John Marston au ranch MacFarlane."),
]
