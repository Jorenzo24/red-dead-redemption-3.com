"""Abraham Reyes, reference fiche (v3, Oct 2026, medium tier).

Same pipeline as the other v3 fiches (scripts/v3/PROCEDURE.md). The base (meta, facts, intro, Development,
Reception) is rebuilt in scripts/fiches/parts/reyes_D.py; the body comes from reyes_A..C.
"""
import copy


def two(en, fr): return {"en": en, "fr": fr}


def build(cl, CH):
    import importlib
    P = {k: importlib.import_module(f"fiches.parts.reyes_{k}") for k in "ABCD"}
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
    d["updated"] = "2026-10-21"
    return d


# Gallery: official art and in-game captures sourced from the Red Dead Wiki
# (rights checked by Joseph before publication), chronological.
def _g(n, alt_en, alt_fr, cap_en, cap_fr):
    return {"img": f"gallery-{n}.jpeg", "alt": two(alt_en, alt_fr), "cap": two(cap_en, cap_fr)}

GALLERY = [
    _g(1, "Close-up of Abraham Reyes with long dark hair", "Gros plan d'Abraham Reyes aux longs cheveux bruns",
       "Abraham Reyes, as rendered in the 2023 port of Red Dead Redemption.", "Abraham Reyes dans le portage de Red Dead Redemption sorti en 2023."),
    _g(2, "Reyes in a green scarf facing John Marston", "Reyes, écharpe verte, face à John Marston",
       "Reyes with John Marston in Nuevo Paraíso.", "Reyes avec John Marston au Nuevo Paraíso."),
    _g(3, "Reyes and John standing in a town square at night", "Reyes et John debout sur une place, de nuit",
       "Reyes and John at night.", "Reyes et John de nuit."),
    _g(4, "John and Reyes aiming their weapons outdoors", "John et Reyes braquant leurs armes en extérieur",
       "John and Reyes at Escalera.", "John et Reyes à Escalera."),
    _g(5, "A zombified Reyes in a dark room", "Reyes zombifié dans une pièce sombre",
       "Undead Nightmare (non-canon): Reyes as one of the undead.", "Undead Nightmare (hors canon) : Reyes changé en mort-vivant."),
]
