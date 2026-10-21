"""Vincente de Santa, reference fiche (v3, Oct 2026, medium tier).

Same pipeline as the other v3 fiches (scripts/v3/PROCEDURE.md). The base (meta, facts, intro, Development,
Reception) is rebuilt in scripts/fiches/parts/desanta_D.py; the body comes from desanta_A..C.
"""
import copy


def two(en, fr): return {"en": en, "fr": fr}


def build(cl, CH):
    import importlib
    P = {k: importlib.import_module(f"fiches.parts.desanta_{k}") for k in "ABCD"}
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
        sec("Weapons, horse and gameplay", "Armes, monture et mécaniques de jeu", P["B"].BLOCKS_SKILLS),
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
    d["updated"] = "2026-10-21"
    return d


# Gallery: official art and in-game captures sourced from the Red Dead Wiki
# (rights checked by Joseph before publication), chronological.
def _g(n, alt_en, alt_fr, cap_en, cap_fr):
    return {"img": f"gallery-{n}.jpeg", "alt": two(alt_en, alt_fr), "cap": two(cap_en, cap_fr)}

GALLERY = [
    _g(1, "Close-up of Captain Vincente de Santa", "Gros plan du capitaine Vincente de Santa",
       "Captain Vincente de Santa in Red Dead Redemption.", "Le capitaine Vincente de Santa dans Red Dead Redemption."),
    _g(2, "De Santa with a soldier at a manor gate at dusk", "De Santa avec un soldat devant le portail d'un manoir au crépuscule",
       "De Santa at the manor gate in \"Civilization, at Any Price\".", "De Santa devant le portail du manoir dans \"Civilization, at Any Price\"."),
    _g(3, "De Santa and John Marston at a table", "De Santa et John Marston à une table",
       "De Santa and John share tequila in Escalera in \"Civilization, at Any Price\".", "De Santa et John partagent une tequila à Escalera dans \"Civilization, at Any Price\"."),
    _g(4, "Allende and De Santa on a terrace", "Allende et De Santa sur une terrasse",
       "De Santa with Colonel Allende on the terrace in \"The Demon Drink\".", "De Santa avec le colonel Allende sur la terrasse dans \"The Demon Drink\"."),
    _g(5, "De Santa with John Marston and Quique Montemayor", "De Santa avec John Marston et Quique Montemayor",
       "De Santa, John and Quique Montemayor in \"Mexican Caesar\".", "De Santa, John et Quique Montemayor dans \"Mexican Caesar\"."),
    _g(6, "John Marston striking De Santa", "John Marston frappant De Santa",
       "John beats De Santa at Sepulcro in \"Captain De Santa's Downfall\".", "John roue De Santa de coups à Sepulcro dans \"Captain De Santa's Downfall\"."),
    _g(7, "An undead De Santa in front of a gravestone", "De Santa mort-vivant devant une pierre tombale",
       "Undead Nightmare (non-canon): De Santa risen from his grave.", "Undead Nightmare (hors canon) : De Santa sorti de sa tombe."),
]
