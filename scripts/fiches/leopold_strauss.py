"""Leopold Strauss, reference fiche (v3, Oct 2026, medium tier).

Same pipeline as John, Arthur, Dutch, Sadie, Micah, Hosea, Charles, Bill, Javier, Abigail and Jack. His page came from
the v2 entry in _enrich.py, so the base (meta, facts, intro, Development, Reception)
is rebuilt in scripts/fiches/parts/leopold_D.py; the body comes from leopold_A..C.
"""
import copy


def two(en, fr): return {"en": en, "fr": fr}


def build(cl, CH):
    import importlib
    P = {k: importlib.import_module(f"fiches.parts.leopold_{k}") for k in "ABCD"}
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
    _g(1, "Close-up of Leopold Strauss in round glasses and a hat", "Gros plan de Leopold Strauss, lunettes rondes et chapeau",
       "Strauss in 1899.", "Strauss en 1899."),
    _g(2, "Strauss, Hosea and Arthur in the snow", "Strauss, Hosea et Arthur dans la neige",
       "With Hosea and Arthur at Colter, \"Enter, Pursued by a Memory\".", "Avec Hosea et Arthur à Colter, \"Enter, Pursued by a Memory\"."),
    _g(3, "Strauss in a white nightshirt in camp at night", "Strauss en chemise de nuit blanche au camp, la nuit",
       "In his pajamas at Horseshoe Overlook.", "En pyjama à Horseshoe Overlook."),
    _g(4, "Dutch and Strauss drinking at a saloon table", "Dutch et Strauss buvant à une table de saloon",
       "With Dutch at Keane's Saloon, \"The Sheep and the Goats\".", "Avec Dutch au Keane's Saloon, \"The Sheep and the Goats\"."),
    _g(5, "Strauss talking to Arthur in camp", "Strauss parlant à Arthur au camp",
       "\"Sodom? Back to Gomorrah\": Strauss tells Arthur of Thomas Downes' death.", "\"Sodom? Back to Gomorrah\" : Strauss apprend à Arthur la mort de Thomas Downes."),
    _g(6, "Strauss and Javier leaning on a wooden railing", "Strauss et Javier appuyés à une balustrade de bois",
       "With Javier in \"A Fine Night of Debauchery\".", "Avec Javier dans \"A Fine Night of Debauchery\"."),
    _g(7, "Strauss on the deck of a riverboat at night", "Strauss sur le pont d'un bateau à aubes, la nuit",
       "Aboard the Grand Korrigan.", "À bord du Grand Korrigan."),
    _g(8, "Strauss speaking to Dutch in a dark room", "Strauss parlant à Dutch dans une pièce sombre",
       "\"Fleeting Joy\": at Lakay, Strauss greets Dutch on his return.", "\"Fleeting Joy\" : à Lakay, Strauss accueille Dutch à son retour."),
    _g(9, "Strauss handing Arthur a list in camp", "Strauss tendant une liste à Arthur au camp",
       "\"Money Lending and Other Sins VI\": Strauss gives Arthur his last debtors.", "\"Money Lending and Other Sins VI\" : Strauss confie à Arthur ses derniers débiteurs."),
    _g(10, "Arthur ordering Strauss out of camp", "Arthur chassant Strauss du camp",
       "\"Money Lending and Other Sins VII\": Arthur banishes Strauss.", "\"Money Lending and Other Sins VII\" : Arthur chasse Strauss."),
]
