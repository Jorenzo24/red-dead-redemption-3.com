"""Lenny Summers, reference fiche (v3, Oct 2026, medium tier).

Same pipeline as John, Arthur, Dutch, Sadie, Micah, Hosea, Charles, Bill, Javier, Abigail and Jack. His page came from
the v2 entry in _enrich.py, so the base (meta, facts, intro, Development, Reception)
is rebuilt in scripts/fiches/parts/lenny_D.py; the body comes from lenny_A..C.
"""
import copy


def two(en, fr): return {"en": en, "fr": fr}


def build(cl, CH):
    import importlib
    P = {k: importlib.import_module(f"fiches.parts.lenny_{k}") for k in "ABCD"}
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
    _g(1, "Close-up of Lenny Summers in a wide-brimmed hat", "Gros plan de Lenny Summers coiffé d'un chapeau à larges bords",
       "Lenny in 1899.", "Lenny en 1899."),
    _g(2, "Lenny standing guard in the snow with a rifle", "Lenny montant la garde dans la neige, fusil en main",
       "Standing guard at Colter.", "De garde à Colter."),
    _g(3, "Lenny on horseback, aiming a rifle", "Lenny à cheval, fusil pointé",
       "Lenny in the first Red Dead Redemption 2 trailer.", "Lenny dans la première bande-annonce de Red Dead Redemption 2."),
    _g(4, "Arthur and Lenny at a saloon bar", "Arthur et Lenny au comptoir d'un saloon",
       "At Smithfield's Saloon with Arthur, in \"A Quiet Time\".", "Au Smithfield's Saloon avec Arthur, dans \"A Quiet Time\"."),
    _g(5, "Arthur and Lenny lying drunk on a floor", "Arthur et Lenny ivres, allongés par terre",
       "Drunk on the floor with Arthur.", "Ivre par terre, avec Arthur."),
    _g(6, "Arthur and Lenny dancing in a crowded saloon", "Arthur et Lenny dansant dans un saloon bondé",
       "On the saloon dance floor with Arthur.", "Sur la piste du saloon avec Arthur."),
    _g(7, "Lenny aiming a revolver in camp", "Lenny visant au revolver dans le camp",
       "Revolver drawn in camp.", "Revolver au poing, au camp."),
    _g(8, "Lenny asleep in a red union suit", "Lenny endormi en sous-vêtement long rouge",
       "Asleep in his union suit.", "Endormi en sous-vêtement long."),
    _g(9, "Lenny sitting by a tree stump in camp", "Lenny assis près d'une souche au camp",
       "In the Clemens Point camp.", "Au camp de Clemens Point."),
    _g(10, "Lenny pointing toward a group of men", "Lenny montrant du doigt un groupe d'hommes",
       "\"Preaching Forgiveness as He Went\": Lenny addresses the Lemoyne Raiders.", "\"Preaching Forgiveness as He Went\" : Lenny s'adresse aux Lemoyne Raiders."),
    _g(11, "Lenny at a table with a rifle", "Lenny à une table, un fusil devant lui",
       "Laying out the stagecoach job.", "Le plan de l'attaque de la diligence."),
    _g(12, "A grave marker in a grassy field", "Une pierre tombale dans un champ d'herbe",
       "His grave in Bluewater Marsh.", "Sa tombe à Bluewater Marsh."),
    _g(13, "Lenny's Cattleman revolver", "Le revolver Cattleman de Lenny",
       "His Cattleman Revolver.", "Son revolver Cattleman."),
    _g(14, "Lenny's Rolling Block rifle", "Le fusil Rolling Block de Lenny",
       "His Rolling Block Rifle.", "Son fusil Rolling Block."),
]
