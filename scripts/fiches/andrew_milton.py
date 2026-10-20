"""Andrew Milton, reference fiche (v3, Oct 2026, medium tier).

Same pipeline as John, Arthur, Dutch, Sadie, Micah, Hosea, Charles, Bill, Javier, Abigail and Jack. His page came from
the v2 entry in _enrich.py, so the base (meta, facts, intro, Development, Reception)
is rebuilt in scripts/fiches/parts/andrew_D.py; the body comes from andrew_A..C.
"""
import copy


def two(en, fr): return {"en": en, "fr": fr}


def build(cl, CH):
    import importlib
    P = {k: importlib.import_module(f"fiches.parts.andrew_{k}") for k in "ABCD"}
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
        sec("Pinkerton agent", "Agent de la Pinkerton", P["B"].BLOCKS_SKILLS),
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
# (rights checked by Joseph before publication), chronological; the trailer still comes last.
def _g(n, alt_en, alt_fr, cap_en, cap_fr):
    return {"img": f"gallery-{n}.jpeg", "alt": two(alt_en, alt_fr), "cap": two(cap_en, cap_fr)}

GALLERY = [
    _g(1, "Close-up of Andrew Milton in a bowler hat", "Gros plan d'Andrew Milton en chapeau melon",
       "Andrew Milton in 1899.", "Andrew Milton en 1899."),
    _g(2, "Milton facing the camera with gang members behind him", "Milton face à l'objectif, des membres du gang derrière lui",
       "Milton at the gang's camp.", "Milton au camp du gang."),
    _g(3, "Two agents standing on a forest trail", "Deux agents debout sur un sentier forestier",
       "Milton with Edgar Ross on a forest trail.", "Milton avec Edgar Ross sur un sentier forestier."),
    _g(4, "Two agents facing armed men", "Deux agents face à des hommes armés",
       "Milton and Ross face the gang in 1899.", "Milton et Ross face au gang en 1899."),
    _g(5, "Milton aiming a pistol", "Milton braquant un pistolet",
       "Milton during the attack on Lakay in \"Fleeting Joy\".", "Milton pendant l'attaque de Lakay dans \"Fleeting Joy\"."),
    _g(6, "Milton gesturing in a town street", "Milton faisant un geste dans une rue",
       "Milton in a trailer for the game.", "Milton dans une bande-annonce du jeu."),
]
