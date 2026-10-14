"""Dutch van der Linde, full reference fiche (v3, Oct 2026).

Same pipeline as John Marston and Arthur Morgan: the body comes from drafted
parts (scripts/fiches/parts/dutch_A..D.py) written against the Red Dead Wiki
page under scripts/coverage.py's spec, then fact-checked. The base entry
(meta, intro, facts, Development and Reception) is the v2 entry kept in
scripts/_enrich.py, passed in as `base`.
"""
import copy


def two(en, fr): return {"en": en, "fr": fr}


def build(cl, CH, base):
    import importlib
    P = {k: importlib.import_module(f"fiches.parts.dutch_{k}") for k in "ABCD"}
    d = copy.deepcopy(base)
    keep = {sec["summary"]["en"]: sec for sec in d["sections"]}

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
        # drop a leading h3 that only repeats the section title
        if blocks and "h3" in blocks[0] and blocks[0]["h3"]["en"].strip().lower().startswith(en.lower()[:10]):
            blocks = blocks[1:]
        x = {"summary": {"en": en, "fr": fr}, "blocks": blocks}
        if open_:
            x["open"] = True
        return x

    sections = [
        sec("Biography", "Biographie", P["A"].BLOCKS + P["B"].BLOCKS, open_=True),
        sec("Personality", "Personnalité", P["C"].BLOCKS_PERSONALITY),
        sec("Skills, weapons and horses", "Compétences, armes et chevaux", P["C"].BLOCKS_SKILLS),
        sec("Missions", "Missions", P["D"].BLOCKS_MISSIONS),
        sec("Quotes", "Citations", P["D"].BLOCKS_QUOTES),
    ]
    for k in ("Development and performance", "Reception"):
        if k in keep:
            sections.append(keep[k])
    sections += [
        sec("Other media and legacy", "Autres médias et postérité", P["D"].BLOCKS_MEDIA),
        sec("Trivia", "Anecdotes", P["D"].BLOCKS_TRIVIA),
    ]
    d["sections"] = sections
    for fct in d["facts"]:      # Dutch is not in Red Dead Online
        if fct["label"]["en"] == "Games":
            fct["value"] = two("Red Dead Redemption, Red Dead Redemption 2", "Red Dead Redemption, Red Dead Redemption 2")
    d["relationships"] = P["C"].RELATIONSHIPS
    d["rel_after"] = 1          # right after Personality
    d["gallery"] = GALLERY
    d["updated"] = "2026-10-14"
    return d


# Gallery: official renders and in-game captures sourced from the Red Dead Wiki
# (rights checked by Joseph before publication), chronological.
def _g(n, alt_en, alt_fr, cap_en, cap_fr):
    return {"img": f"gallery-{n}.jpeg", "alt": two(alt_en, alt_fr), "cap": two(cap_en, cap_fr)}

GALLERY = [
    _g(1, "Dutch van der Linde in Red Dead Redemption 2", "Dutch van der Linde dans Red Dead Redemption 2",
       "Dutch in 1899.", "Dutch en 1899."),
    _g(3, "Red Dead Redemption 2 key art of Dutch van der Linde holding a knife", "Artwork de Red Dead Redemption 2 : Dutch van der Linde, un couteau à la main",
       "Official Red Dead Redemption 2 key art.", "Artwork officiel de Red Dead Redemption 2."),
    _g(5, "The gang riding through deep snow, Dutch on a white horse", "Le gang dans la neige, Dutch sur un cheval blanc",
       "Chapter 1: the gang in the snow, Dutch at the front.", "Chapitre 1 : le gang dans la neige, Dutch en tête."),
    _g(6, "The Van der Linde gang riding across a meadow", "Le gang Van der Linde à cheval dans une prairie",
       "The gang on the move, Dutch on his white horse.", "Le gang en déplacement, Dutch sur son cheval blanc."),
    _g(7, "Dutch standing at the centre of the gang", "Dutch au centre du gang",
       "Dutch at the centre of the gang.", "Dutch au centre du gang."),
    _g(8, "Dutch and Molly O'Shea in his tent at camp", "Dutch et Molly O'Shea sous sa tente, au camp",
       "Dutch and Molly O'Shea at camp.", "Dutch et Molly O'Shea au camp."),
    _g(9, "Dutch and Micah standing in a field", "Dutch et Micah debout dans un champ",
       "Dutch and Micah at the meeting with Colm O'Driscoll.", "Dutch et Micah lors de la rencontre avec Colm O'Driscoll."),
    _g(10, "Dutch drawing his revolver on an opponent", "Dutch braquant son revolver sur un adversaire",
       "Dutch draws on an opponent.", "Dutch dégaine face à un adversaire."),
    _g(11, "Old photograph of a young Arthur with Dutch and Hosea", "Photographie ancienne d'un jeune Arthur avec Dutch et Hosea",
       "The photograph of Dutch and Hosea with a young Arthur.", "La photographie de Dutch et Hosea avec le jeune Arthur."),
    _g(12, "Dutch holding Angelo Bronte's head down", "Dutch maintenant la tête d'Angelo Bronte",
       "Chapter 4, \"Revenge is a Dish Best Eaten\": Dutch drowns Angelo Bronte.", "Chapitre 4, \"Revenge is a Dish Best Eaten\" : Dutch noie Angelo Bronte."),
    _g(13, "Dutch reloading a revolver behind cover", "Dutch rechargeant un revolver à couvert",
       "Dutch reloading in \"Just a Social Call\".", "Dutch recharge dans \"Just a Social Call\"."),
    _g(14, "Dutch aiming a revolver from the doorway of a cabin in the snow", "Dutch braquant un revolver depuis la porte d'une cabane enneigée",
       "1907, \"American Venom\": Dutch on Mount Hagen.", "1907, \"American Venom\" : Dutch au mont Hagen."),
    _g(15, "Dutch in 1911, older, in an orange shirt", "Dutch en 1911, vieilli, en chemise orange",
       "Dutch in 1911.", "Dutch en 1911."),
    _g(16, "A gunfight inside the Blackwater bank", "Une fusillade dans la banque de Blackwater",
       "1911: John and lawmen confront Dutch and his men at the Blackwater bank.", "1911 : John et les forces de l'ordre affrontent Dutch et ses hommes à la banque de Blackwater."),
    _g(17, "Dutch firing a mounted machine gun in his snowy hideout", "Dutch tirant à la mitrailleuse montée dans son repaire enneigé",
       "1911: Dutch at the mounted machine gun of his hideout.", "1911 : Dutch à la mitrailleuse montée de son repaire."),
    _g(18, "John Marston holding Dutch at gunpoint in the snow", "John Marston tenant Dutch en joue dans la neige",
       "1911: John holds Dutch at gunpoint at Cochinay.", "1911 : John tient Dutch en joue à Cochinay."),
    _g(19, "Dutch falling backwards from the cliff edge", "Dutch basculant en arrière du haut de la falaise",
       "1911: Dutch lets himself fall from the cliff.", "1911 : Dutch se laisse tomber de la falaise."),
    _g(20, "John Marston looking down at Dutch's body in the snow", "John Marston devant le corps de Dutch dans la neige",
       "John looks down at Dutch's body.", "John devant le corps de Dutch."),
]
