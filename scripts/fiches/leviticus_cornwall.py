"""Leviticus Cornwall, reference fiche (v3, Oct 2026, medium tier).

Same pipeline as John, Arthur, Dutch, Sadie, Micah, Hosea, Charles, Bill, Javier, Abigail and Jack. His page came from
the v2 entry in _enrich.py, so the base (meta, facts, intro, Development, Reception)
is rebuilt in scripts/fiches/parts/leviticus_D.py; the body comes from leviticus_A..C.
"""
import copy


def two(en, fr): return {"en": en, "fr": fr}


def build(cl, CH):
    import importlib
    P = {k: importlib.import_module(f"fiches.parts.leviticus_{k}") for k in "ABCD"}
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
        sec("Business empire", "Un empire industriel", P["B"].BLOCKS_SKILLS),
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
    _g(1, "Close-up of Leviticus Cornwall", "Gros plan de Leviticus Cornwall",
       "Leviticus Cornwall in 1899.", "Leviticus Cornwall en 1899."),
    _g(2, "Cornwall seated on a porch", "Cornwall assis sur un perron",
       "Cornwall in Valentine.", "Cornwall à Valentine."),
    _g(3, "Cornwall standing with an armed man", "Cornwall debout près d'un homme armé",
       "Cornwall with one of his men.", "Cornwall avec l'un de ses hommes."),
    _g(4, "Painted portrait of a seated Cornwall", "Portrait peint de Cornwall assis",
       "A painted portrait of Cornwall in his private car.", "Un portrait peint de Cornwall dans sa voiture privée."),
    _g(5, "Painted portrait of Cornwall with a cane and top hat", "Portrait peint de Cornwall avec canne et haut-de-forme",
       "A painted portrait of Cornwall in \"Who the Hell is Leviticus Cornwall?\".", "Un portrait peint de Cornwall dans \"Who the Hell is Leviticus Cornwall?\"."),
    _g(6, "Cigarette card of Leviticus Cornwall", "Carte de cigarettes de Leviticus Cornwall",
       "His Jolly Jack's cigarette card, \"Oil Tycoon\".", "Sa carte de cigarettes Jolly Jack's, \"Oil Tycoon\"."),
    _g(7, "Seal with the motto Pecuniae Obediunt Omnia", "Sceau portant la devise Pecuniae Obediunt Omnia",
       "The Cornwall seal, emblem on his trains: \"Pecuniae obediunt omnia\".", "Le sceau de Cornwall, emblème de ses trains : \"Pecuniae obediunt omnia\"."),
]
