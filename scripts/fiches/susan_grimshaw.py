"""Susan Grimshaw, reference fiche (v3, Oct 2026, medium tier).

Same pipeline as John, Arthur, Dutch, Sadie, Micah, Hosea, Charles, Bill, Javier, Abigail and Jack. His page came from
the v2 entry in _enrich.py, so the base (meta, facts, intro, Development, Reception)
is rebuilt in scripts/fiches/parts/susan_D.py; the body comes from susan_A..C.
"""
import copy


def two(en, fr): return {"en": en, "fr": fr}


def build(cl, CH):
    import importlib
    P = {k: importlib.import_module(f"fiches.parts.susan_{k}") for k in "ABCD"}
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
    d["updated"] = "2026-10-19"
    return d


# Gallery: official art and in-game captures sourced from the Red Dead Wiki
# (rights checked by Joseph before publication), chronological.
def _g(n, alt_en, alt_fr, cap_en, cap_fr):
    return {"img": f"gallery-{n}.jpeg", "alt": two(alt_en, alt_fr), "cap": two(cap_en, cap_fr)}

GALLERY = [
    _g(1, "Close-up of Susan Grimshaw in a dark dress", "Gros plan de Susan Grimshaw en robe sombre",
       "Susan in 1899.", "Susan en 1899."),
    _g(2, "Close-up of Susan in camp", "Gros plan de Susan au camp",
       "Susan at Horseshoe Overlook.", "Susan à Horseshoe Overlook."),
    _g(3, "Susan, Tilly and Karen standing in camp", "Susan, Tilly et Karen debout au camp",
       "Susan, Tilly and Karen.", "Susan, Tilly et Karen."),
    _g(4, "Susan speaking sternly to Mary-Beth", "Susan parlant sèchement à Mary-Beth",
       "Susan berating Mary-Beth in camp.", "Susan sermonne Mary-Beth au camp."),
    _g(5, "Susan sitting beside Tilly on a porch", "Susan assise à côté de Tilly sur un perron",
       "Susan comforting Tilly.", "Susan réconforte Tilly."),
    _g(6, "Susan holding a pump-action shotgun at Beaver Hollow", "Susan, un fusil à pompe à la main, à Beaver Hollow",
       "Susan after shooting Molly.", "Susan après avoir abattu Molly."),
    _g(7, "Susan smoking at night", "Susan fumant, la nuit",
       "Susan at Beaver Hollow.", "Susan à Beaver Hollow."),
    _g(8, "A wooden cross on a grassy mound under a tree", "Une croix de bois sur un tertre herbeux, sous un arbre",
       "Susan's grave.", "La tombe de Susan."),
]
