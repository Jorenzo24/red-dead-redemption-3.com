"""Nastas, reference fiche (v3, Oct 2026, medium tier).

Same pipeline as the other v3 fiches (scripts/v3/PROCEDURE.md). The base (meta, facts, intro, Development,
Reception) is rebuilt in scripts/fiches/parts/nastas_D.py; the body comes from nastas_A..C.
"""
import copy


def two(en, fr): return {"en": en, "fr": fr}


def build(cl, CH):
    import importlib
    P = {k: importlib.import_module(f"fiches.parts.nastas_{k}") for k in "ABCD"}
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
        sec("Guide, weapons and horses", "Guide, armes et chevaux", P["B"].BLOCKS_SKILLS),
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
    _g(1, "Close-up of Nastas wearing a red headband", "Gros plan de Nastas portant un bandeau rouge",
       "Nastas in Red Dead Redemption.", "Nastas dans Red Dead Redemption."),
    _g(2, "Nastas, John Marston and Harold MacDougal held at gunpoint, hands raised", "Nastas, John Marston et Harold MacDougal tenus en joue, mains levées",
       "Nastas, John and MacDougal held at gunpoint at the Bear Claw cabin in \"For Purely Scientific Purposes\".", "Nastas, John et MacDougal tenus en joue à la cabane de Bear Claw dans \"For Purely Scientific Purposes\"."),
    _g(3, "Nastas and Harold MacDougal looking down", "Nastas et Harold MacDougal regardant vers le bas",
       "Nastas and MacDougal watch John wake up in MacDougal's room at the end of \"At Home with Dutch\".", "Nastas et MacDougal regardent John se réveiller dans la chambre de MacDougal, à la fin de \"At Home with Dutch\"."),
    _g(4, "An undead Nastas in a street", "Nastas mort-vivant dans une rue",
       "Undead Nightmare (non-canon): Nastas among the undead.", "Undead Nightmare (hors canon) : Nastas parmi les morts-vivants."),
]
