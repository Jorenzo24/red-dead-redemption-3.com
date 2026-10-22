"""Eagle Flies, reference fiche (v3, Oct 2026, medium tier).

Same pipeline as the other v3 fiches (scripts/v3/PROCEDURE.md). The base (meta, facts, intro, Development,
Reception) is rebuilt in scripts/fiches/parts/eagle_D.py; the body comes from eagle_A..C.
"""
import copy


def two(en, fr): return {"en": en, "fr": fr}


def build(cl, CH):
    import importlib
    P = {k: importlib.import_module(f"fiches.parts.eagle_{k}") for k in "ABCD"}
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
        sec("Raids, weapons and horses", "Raids, armes et chevaux", P["B"].BLOCKS_SKILLS),
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
    _g(1, "Official render of Eagle Flies in Red Dead Redemption 2", "Rendu officiel d'Eagle Flies dans Red Dead Redemption 2",
       "Eagle Flies, son of the Wapiti chief Rains Fall.", "Eagle Flies, fils du chef wapiti Rains Fall."),
    _g(2, "Eagle Flies looking through binoculars over the Heartland Oil Fields", "Eagle Flies observe les Heartland Oil Fields à la jumelle",
       "Scouting the Heartland Oil Fields before \"American Fathers II\".", "En repérage au-dessus des Heartland Oil Fields avant \"American Fathers II\"."),
    _g(3, "Eagle Flies at night at the end of a mission in Red Dead Redemption 2", "Eagle Flies de nuit à la fin d'une mission dans Red Dead Redemption 2",
       "At the end of \"American Fathers II\".", "À la fin de \"American Fathers II\"."),
    _g(4, "Eagle Flies wearing red and white war paint", "Eagle Flies avec des peintures de guerre rouges et blanches",
       "Eagle Flies in war paint.", "Eagle Flies avec ses peintures de guerre."),
    _g(5, "John Marston at the grave of Eagle Flies in 1907", "John Marston devant la tombe d'Eagle Flies en 1907",
       "Visiting the grave of Eagle Flies as John Marston, 1907.", "John Marston se recueille sur la tombe d'Eagle Flies, en 1907."),
]
