"""Angelo Bronte, reference fiche (v3, Oct 2026, medium tier).

Same pipeline as John, Arthur, Dutch, Sadie, Micah, Hosea, Charles, Bill, Javier, Abigail and Jack. His page came from
the v2 entry in _enrich.py, so the base (meta, facts, intro, Development, Reception)
is rebuilt in scripts/fiches/parts/angelo_D.py; the body comes from angelo_A..C.
"""
import copy


def two(en, fr): return {"en": en, "fr": fr}


def build(cl, CH):
    import importlib
    P = {k: importlib.import_module(f"fiches.parts.angelo_{k}") for k in "ABCD"}
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
    _g(1, "Close-up of Angelo Bronte in an embroidered cap", "Gros plan d'Angelo Bronte coiffé d'un calot brodé",
       "Angelo Bronte in 1899.", "Angelo Bronte en 1899."),
    _g(2, "Painted portrait of Bronte above a fireplace", "Portrait peint de Bronte au-dessus d'une cheminée",
       "A painted portrait of Bronte in his mansion.", "Un portrait peint de Bronte dans sa demeure."),
    _g(3, "Framed photograph of Bronte with another man", "Photographie encadrée de Bronte avec un autre homme",
       "A framed photograph of Bronte dated 1898.", "Une photographie encadrée de Bronte datée de 1898."),
    _g(4, "Arthur, Dutch and John in Bronte's study", "Arthur, Dutch et John dans le bureau de Bronte",
       "The gang confronts Bronte in his mansion.", "Le gang face à Bronte dans sa demeure."),
    _g(5, "Bronte arguing in a green room", "Bronte en pleine dispute dans une pièce verte",
       "Bronte in his mansion.", "Bronte dans sa demeure."),
    _g(6, "Bronte aiming a pistol", "Bronte braquant un pistolet",
       "Bronte with his pistol drawn.", "Bronte, pistolet au poing."),
    _g(7, "Bronte seated in a rowing boat with the gang", "Bronte assis dans une barque avec le gang",
       "Bronte taken out on the water.", "Bronte emmené sur l'eau."),
    _g(8, "Dutch holding Bronte over the side of a boat", "Dutch maintenant Bronte au-dessus du bord d'une barque",
       "Dutch kills Bronte.", "Dutch tue Bronte."),
]
