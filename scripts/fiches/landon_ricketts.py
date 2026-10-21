"""Landon Ricketts, reference fiche (v3, Oct 2026, medium tier).

Same pipeline as the other v3 fiches (scripts/v3/PROCEDURE.md). The base (meta, facts, intro, Development,
Reception) is rebuilt in scripts/fiches/parts/landon_D.py; the body comes from landon_A..C.
"""
import copy


def two(en, fr): return {"en": en, "fr": fr}


def build(cl, CH):
    import importlib
    P = {k: importlib.import_module(f"fiches.parts.landon_{k}") for k in "ABCD"}
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
        sec("Gunfighting and weapons", "Tir et armes", P["B"].BLOCKS_SKILLS),
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
    _g(1, "Close-up of Landon Ricketts in a dark hat", "Gros plan de Landon Ricketts en chapeau sombre",
       "Landon Ricketts, as rendered in the 2023 port of Red Dead Redemption.", "Landon Ricketts dans le portage de Red Dead Redemption sorti en 2023."),
    _g(2, "Landon in front of a church in a Mexican town", "Landon devant une église dans une ville mexicaine",
       "Landon in the square of Chuparosa in \"The Gunslinger's Tragedy\".", "Landon sur la place de Chuparosa dans \"The Gunslinger's Tragedy\"."),
    _g(3, "Landon seated against a wall", "Landon assis contre un mur",
       "Landon in Chuparosa.", "Landon à Chuparosa."),
    _g(4, "Landon and John standing in open country", "Landon et John debout en rase campagne",
       "Shooting practice outside town in \"The Gunslinger's Tragedy\".", "Entraînement au tir hors de la ville dans \"The Gunslinger's Tragedy\"."),
    _g(5, "Landon at a card table", "Landon à une table de jeu",
       "Landon at the card table in \"Lucky in Love\".", "Landon à la table de jeu dans \"Lucky in Love\"."),
    _g(6, "Landon and John Marston at a barrel table", "Landon et John Marston autour d'un tonneau",
       "Undead Nightmare (non-canon): Landon in Casa Madrugada in \"Biographies and Lies\".", "Undead Nightmare (hors canon) : Landon à Casa Madrugada dans \"Biographies and Lies\"."),
    _g(7, "Landon firing a revolver at the ground", "Landon tirant au revolver vers le sol",
       "Undead Nightmare (non-canon): Landon sets off Boom Bait in \"Biographies and Lies\".", "Undead Nightmare (hors canon) : Landon fait exploser un appât dans \"Biographies and Lies\"."),
]
