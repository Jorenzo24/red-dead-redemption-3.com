"""Leigh Johnson, reference fiche (v3, Oct 2026, medium tier).

Same pipeline as the other v3 fiches (scripts/v3/PROCEDURE.md). The base (meta, facts, intro, Development,
Reception) is rebuilt in scripts/fiches/parts/leigh_D.py; the body comes from leigh_A..C.
"""
import copy


def two(en, fr): return {"en": en, "fr": fr}


def build(cl, CH):
    import importlib
    P = {k: importlib.import_module(f"fiches.parts.leigh_{k}") for k in "ABCD"}
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
        sec("Law enforcement, weapons and horses", "Maintien de l'ordre, armes et chevaux", P["B"].BLOCKS_SKILLS),
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
    _g(1, "Close-up of Leigh Johnson in a wide-brimmed hat", "Gros plan de Leigh Johnson en chapeau à large bord",
       "Marshal Leigh Johnson in Red Dead Redemption.", "Le marshal Leigh Johnson dans Red Dead Redemption."),
    _g(2, "Johnson standing by a barred window", "Johnson debout près d'une fenêtre à barreaux",
       "Johnson in his office in Armadillo.", "Johnson dans son bureau d'Armadillo."),
    _g(3, "Johnson standing in a dusty street", "Johnson debout dans une rue poussiéreuse",
       "Johnson in the main street of Armadillo.", "Johnson dans la rue principale d'Armadillo."),
    _g(4, "Johnson, John Marston and a white-mustached man", "Johnson, John Marston et un homme à moustache blanche",
       "Johnson with John Marston.", "Johnson avec John Marston."),
    _g(5, "Johnson and John Marston in rocky country", "Johnson et John Marston dans un paysage rocheux",
       "Johnson and John in the open country.", "Johnson et John en rase campagne."),
    _g(6, "John looking through a spyglass beside Johnson", "John regardant à la longue-vue à côté de Johnson",
       "John scouts with a spyglass beside Johnson.", "John observe à la longue-vue aux côtés de Johnson."),
]
