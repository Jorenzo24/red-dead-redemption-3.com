"""Josiah Trelawny, reference fiche (v3, Oct 2026, medium tier).

Same pipeline as John, Arthur, Dutch, Sadie, Micah, Hosea, Charles, Bill, Javier, Abigail and Jack. His page came from
the v2 entry in _enrich.py, so the base (meta, facts, intro, Development, Reception)
is rebuilt in scripts/fiches/parts/josiah_D.py; the body comes from josiah_A..C.
"""
import copy


def two(en, fr): return {"en": en, "fr": fr}


def build(cl, CH):
    import importlib
    P = {k: importlib.import_module(f"fiches.parts.josiah_{k}") for k in "ABCD"}
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
    _g(1, "Josiah Trelawny in a top hat", "Josiah Trelawny en haut-de-forme",
       "Trelawny in 1899.", "Trelawny en 1899."),
    _g(2, "Three men carrying Trelawny", "Trois hommes portant Trelawny",
       "Trelawny carried off by Cole Stoudemire's bounty hunters.", "Trelawny emmené par les chasseurs de primes de Cole Stoudemire."),
    _g(3, "Trelawny lying on the ground in front of two men", "Trelawny allongé par terre devant deux hommes",
       "Faking a fit to distract Ike Skelding's men.", "Il simule une crise pour détourner l'attention des hommes d'Ike Skelding."),
    _g(4, "Arthur, Hosea, Trelawny and Dutch walking together", "Arthur, Hosea, Trelawny et Dutch marchant ensemble",
       "Arthur, Hosea, Trelawny and Dutch in Rhodes.", "Arthur, Hosea, Trelawny et Dutch à Rhodes."),
    _g(5, "Trelawny and Arthur on horseback", "Trelawny et Arthur à cheval",
       "Waiting for Chester Damsen's stagecoach with Arthur.", "Avec Arthur, en attendant la diligence de Chester Damsen."),
    _g(6, "Arthur, Trelawny, Javier and Strauss on a dock", "Arthur, Trelawny, Javier et Strauss sur un quai",
       "With Arthur, Javier and Strauss in \"A Fine Night of Debauchery\".", "Avec Arthur, Javier et Strauss dans \"A Fine Night of Debauchery\"."),
    _g(7, "Trelawny and Arthur in a riverboat corridor", "Trelawny et Arthur dans une coursive de bateau à aubes",
       "With Arthur aboard the Grand Korrigan.", "Avec Arthur à bord du Grand Korrigan."),
    _g(8, "Trelawny and Arthur walking in a city street", "Trelawny et Arthur marchant dans une rue de la ville",
       "With Arthur in Saint Denis.", "Avec Arthur à Saint-Denis."),
    _g(9, "Trelawny talking to Arthur by a tree", "Trelawny parlant à Arthur près d'un arbre",
       "The start of \"Friends in Very Low Places\".", "Le début de \"Friends in Very Low Places\"."),
    _g(10, "Trelawny with the Anderson Boys in a prison wagon", "Trelawny avec les frères Anderson dans un fourgon cellulaire",
       "In a prison wagon with the Anderson Boys.", "Dans un fourgon cellulaire avec les frères Anderson."),
    _g(11, "Trelawny crouching near Arthur and another man", "Trelawny accroupi près d'Arthur et d'un autre homme",
       "Approaching Javier, Arthur and Charles.", "Il rejoint Javier, Arthur et Charles."),
    _g(12, "Close-up of Trelawny", "Gros plan de Trelawny",
       "\"The Fine Art of Conversation\".", "\"The Fine Art of Conversation\"."),
    _g(13, "Trelawny and Arthur sitting in camp", "Trelawny et Arthur assis au camp",
       "Saying goodbye to Arthur at Beaver Hollow.", "Il dit adieu à Arthur à Beaver Hollow."),
    _g(14, "Trelawny walking away with a suitcase", "Trelawny s'éloignant, une valise à la main",
       "Leaving the gang.", "Il quitte le gang."),
    _g(15, "Trelawny reading on the porch of a caravan", "Trelawny lisant sur le porche d'une roulotte",
       "Red Dead Online: on the porch of his caravan.", "Red Dead Online : sur le porche de sa roulotte."),
    _g(16, "Trelawny holding a revolver to his head", "Trelawny pointant un revolver sur sa tempe",
       "Red Dead Online: the revolver he turns into a bird.", "Red Dead Online : le revolver qu'il transforme en oiseau."),
]
