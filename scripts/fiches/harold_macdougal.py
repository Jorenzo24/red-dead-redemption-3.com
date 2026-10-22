"""Harold MacDougal, reference fiche (v3, Oct 2026, medium tier).

Same pipeline as the other v3 fiches (scripts/v3/PROCEDURE.md). The base (meta, facts, intro, Development,
Reception) is rebuilt in scripts/fiches/parts/macdougal_D.py; the body comes from macdougal_A..C.
"""
import copy


def two(en, fr): return {"en": en, "fr": fr}


def build(cl, CH):
    import importlib
    P = {k: importlib.import_module(f"fiches.parts.macdougal_{k}") for k in "ABCD"}
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
        sec("Research, weapons and horses", "Recherches, armes et chevaux", P["B"].BLOCKS_SKILLS),
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
    _g(1, "Harold MacDougal at a desk with a microscope, bookshelves behind", "Harold MacDougal à un bureau avec un microscope, des étagères derrière",
       "Harold MacDougal in his office in Red Dead Redemption.", "Harold MacDougal dans son bureau, dans Red Dead Redemption."),
    _g(2, "MacDougal and Nastas leaning over the camera", "MacDougal et Nastas penchés vers l'objectif",
       "MacDougal and Nastas watch John wake up in Blackwater at the end of \"At Home with Dutch\".", "MacDougal et Nastas regardent John se réveiller à Blackwater, à la fin de \"At Home with Dutch\"."),
    _g(3, "MacDougal facing the camera in his office, John Marston behind him", "MacDougal face à l'objectif dans son bureau, John Marston derrière lui",
       "MacDougal with John Marston.", "MacDougal avec John Marston."),
    _g(4, "MacDougal in a deserted street at night with fires", "MacDougal dans une rue déserte, de nuit, au milieu des incendies",
       "Undead Nightmare (non-canon): MacDougal in Blackwater in \"Curious Tales from Blackwater\".", "Undead Nightmare (hors canon) : MacDougal à Blackwater dans \"Curious Tales from Blackwater\"."),
    _g(5, "MacDougal beside an undead Nastas in a street", "MacDougal à côté de Nastas mort-vivant dans une rue",
       "Undead Nightmare (non-canon): MacDougal and the undead Nastas.", "Undead Nightmare (hors canon) : MacDougal et Nastas mort-vivant."),
]
