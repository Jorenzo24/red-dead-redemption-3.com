"""Archer Fordham, reference fiche (v3, Oct 2026, medium tier).

Same pipeline as the other v3 fiches (scripts/v3/PROCEDURE.md). The base (meta, facts, intro, Development,
Reception) is rebuilt in scripts/fiches/parts/fordham_D.py; the body comes from fordham_A..C.
"""
import copy


def two(en, fr): return {"en": en, "fr": fr}


def build(cl, CH):
    import importlib
    P = {k: importlib.import_module(f"fiches.parts.fordham_{k}") for k in "ABCD"}
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
    d["updated"] = "2026-10-22"
    return d


# Gallery: official art and in-game captures sourced from the Red Dead Wiki
# (rights checked by Joseph before publication), chronological.
def _g(n, alt_en, alt_fr, cap_en, cap_fr):
    return {"img": f"gallery-{n}.jpeg", "alt": two(alt_en, alt_fr), "cap": two(cap_en, cap_fr)}

GALLERY = [
    _g(1, "Close-up of Archer Fordham in a bowler hat", "Gros plan d'Archer Fordham en chapeau melon",
       "Archer Fordham in Red Dead Redemption 2 (1907).", "Archer Fordham dans Red Dead Redemption 2 (1907)."),
    _g(2, "Two men walking towards a body in the snow", "Deux hommes marchant vers un corps dans la neige",
       "Fordham and Edgar Ross find Micah's body in the end credits (1907).", "Fordham et Edgar Ross trouvent le corps de Micah dans le générique de fin (1907)."),
    _g(3, "Two agents seen from behind, looking at a farm", "Deux agents vus de dos, observant une ferme",
       "Ross and Fordham watching a ranch.", "Ross et Fordham observent un ranch."),
    _g(4, "Close-up of Fordham in Red Dead Redemption", "Gros plan de Fordham dans Red Dead Redemption",
       "Fordham in Red Dead Redemption (1911).", "Fordham dans Red Dead Redemption (1911)."),
    _g(5, "Ross, John Marston and Fordham walking in a town street", "Ross, John Marston et Fordham marchant dans une rue",
       "Ross, John and Fordham in Blackwater.", "Ross, John et Fordham à Blackwater."),
    _g(6, "John Marston between two agents in an office", "John Marston entre deux agents dans un bureau",
       "John with Ross and Fordham at the Bureau.", "John avec Ross et Fordham au Bureau."),
    _g(7, "Agents questioning people in a saloon", "Des agents interrogeant des gens dans un saloon",
       "The agents questioning people in a saloon.", "Les agents interrogent des gens dans un saloon."),
]
