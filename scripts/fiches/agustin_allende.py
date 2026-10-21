"""Agustin Allende, reference fiche (v3, Oct 2026, medium tier).

Same pipeline as the other v3 fiches (scripts/v3/PROCEDURE.md). The base (meta, facts, intro, Development,
Reception) is rebuilt in scripts/fiches/parts/allende_D.py; the body comes from allende_A..C.
"""
import copy


def two(en, fr): return {"en": en, "fr": fr}


def build(cl, CH):
    import importlib
    P = {k: importlib.import_module(f"fiches.parts.allende_{k}") for k in "ABCD"}
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
        sec("Weapons and stagecoach", "Armes et diligence", P["B"].BLOCKS_SKILLS),
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
    _g(1, "Close-up of Colonel Agustin Allende in uniform", "Gros plan du colonel Agustin Allende en uniforme",
       "Colonel Agustin Allende in Red Dead Redemption.", "Le colonel Agustin Allende dans Red Dead Redemption."),
    _g(2, "Allende with two young women beside John Marston", "Allende avec deux jeunes femmes à côté de John Marston",
       "Allende with the two young women De Santa brings to the manor in \"Mexican Caesar\".", "Allende avec les deux jeunes femmes que De Santa amène au manoir dans \"Mexican Caesar\"."),
    _g(3, "Allende speaking on a sunny terrace", "Allende parlant sur une terrasse ensoleillée",
       "Allende on a terrace in \"The Demon Drink\".", "Allende sur une terrasse dans \"The Demon Drink\"."),
    _g(4, "Allende raising his arms on a terrace, De Santa behind him", "Allende levant les bras sur une terrasse, De Santa derrière lui",
       "Allende with De Santa standing behind him in \"The Demon Drink\".", "Allende, De Santa debout derrière lui, dans \"The Demon Drink\"."),
    _g(5, "Two men in a large room with arched windows", "Deux hommes dans une grande salle aux fenêtres en arc",
       "Allende and Bill Williamson in the mansion before their escape in \"An Appointed Time\".", "Allende et Bill Williamson dans le manoir avant leur fuite dans \"An Appointed Time\"."),
    _g(6, "Rebel poster showing General Sanchez holding a small Allende on his lap above a pile of skulls", "Affiche rebelle montrant le général Sanchez tenant un petit Allende sur ses genoux, au-dessus d'un tas de crânes",
       "A rebel poster: \"Allende es el perrito faldero del General Ignacio Sanchez\" (Allende is General Ignacio Sanchez's lapdog).", "Une affiche rebelle : « Allende es el perrito faldero del General Ignacio Sanchez » (Allende est le toutou du général Ignacio Sanchez)."),
]
