"""Colm O'Driscoll, reference fiche (v3, Oct 2026, medium tier).

Same pipeline as John, Arthur, Dutch, Sadie, Micah, Hosea, Charles, Bill, Javier, Abigail and Jack. His page came from
the v2 entry in _enrich.py, so the base (meta, facts, intro, Development, Reception)
is rebuilt in scripts/fiches/parts/colm_D.py; the body comes from colm_A..C.
"""
import copy


def two(en, fr): return {"en": en, "fr": fr}


def build(cl, CH):
    import importlib
    P = {k: importlib.import_module(f"fiches.parts.colm_{k}") for k in "ABCD"}
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
    _g(1, "Close-up of Colm O'Driscoll in a black hat", "Gros plan de Colm O'Driscoll en chapeau noir",
       "Colm O'Driscoll in 1899.", "Colm O'Driscoll en 1899."),
    _g(2, "Colm in a striped shirt and black vest", "Colm en chemise rayée et gilet noir",
       "Colm in Red Dead Redemption 2.", "Colm dans Red Dead Redemption 2."),
    _g(3, "Full-length view of Colm", "Colm en pied",
       "Leader of the O'Driscoll Boys.", "Le chef des O'Driscoll Boys."),
    _g(4, "Colm standing in a field with two of his men", "Colm debout dans un champ avec deux de ses hommes",
       "Colm and his men in the open country.", "Colm et ses hommes en rase campagne."),
    _g(5, "Colm holding a lantern in a dark room", "Colm tenant une lanterne dans une pièce sombre",
       "Colm during Arthur's captivity.", "Colm pendant la captivité d'Arthur."),
    _g(6, "Colm aiming a revolver in a dark room", "Colm braquant un revolver dans une pièce sombre",
       "Colm with his revolver during Arthur's captivity.", "Colm, revolver au poing, pendant la captivité d'Arthur."),
    _g(7, "Colm gagged", "Colm bâillonné",
       "Colm before his execution in Saint Denis.", "Colm avant son exécution à Saint-Denis."),
]
