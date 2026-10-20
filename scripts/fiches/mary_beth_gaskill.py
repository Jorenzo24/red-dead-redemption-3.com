"""Mary-Beth Gaskill, reference fiche (v3, Oct 2026, medium tier).

Same pipeline as John, Arthur, Dutch, Sadie, Micah, Hosea, Charles, Bill, Javier, Abigail and Jack. His page came from
the v2 entry in _enrich.py, so the base (meta, facts, intro, Development, Reception)
is rebuilt in scripts/fiches/parts/mary_D.py; the body comes from mary_A..C.
"""
import copy


def two(en, fr): return {"en": en, "fr": fr}


def build(cl, CH):
    import importlib
    P = {k: importlib.import_module(f"fiches.parts.mary_{k}") for k in "ABCD"}
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
        sec("Talents and camp life", "Talents et vie au camp", P["B"].BLOCKS_SKILLS),
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
    d["updated"] = "2026-10-19"
    return d


# Gallery: official art and in-game captures sourced from the Red Dead Wiki
# (rights checked by Joseph before publication), chronological.
def _g(n, alt_en, alt_fr, cap_en, cap_fr):
    return {"img": f"gallery-{n}.jpeg", "alt": two(alt_en, alt_fr), "cap": two(cap_en, cap_fr)}

GALLERY = [
    _g(1, "Close-up of Mary-Beth Gaskill", "Gros plan de Mary-Beth Gaskill",
       "Mary-Beth in 1899.", "Mary-Beth en 1899."),
    _g(2, "Mary-Beth in a winter coat in the snow", "Mary-Beth en manteau d'hiver dans la neige",
       "Mary-Beth at Colter.", "Mary-Beth à Colter."),
    _g(3, "Mary-Beth standing among trees in camp", "Mary-Beth debout parmi les arbres au camp",
       "Mary-Beth at Horseshoe Overlook.", "Mary-Beth à Horseshoe Overlook."),
    _g(4, "Mary-Beth lying in the grass, reading", "Mary-Beth allongée dans l'herbe, en train de lire",
       "Mary-Beth reading.", "Mary-Beth en pleine lecture."),
    _g(5, "Mary-Beth sitting on the ground in camp", "Mary-Beth assise par terre au camp",
       "Resting in camp.", "Au repos au camp."),
    _g(6, "Mary-Beth standing with a cup, horses behind her", "Mary-Beth debout une tasse à la main, des chevaux derrière elle",
       "Mary-Beth at Beaver Hollow.", "Mary-Beth à Beaver Hollow."),
    _g(7, "Mary-Beth sitting on a bench at a station, writing", "Mary-Beth assise sur un banc de gare, en train d'écrire",
       "The 1907 encounter with John.", "La rencontre de 1907 avec John."),
    _g(8, "Mary-Beth writing by lamplight", "Mary-Beth écrivant à la lumière d'une lampe",
       "Mary-Beth in the end credits.", "Mary-Beth dans le générique de fin."),
]
