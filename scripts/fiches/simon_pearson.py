"""Simon Pearson, reference fiche (v3, Oct 2026, medium tier).

Same pipeline as John, Arthur, Dutch, Sadie, Micah, Hosea, Charles, Bill, Javier, Abigail and Jack. His page came from
the v2 entry in _enrich.py, so the base (meta, facts, intro, Development, Reception)
is rebuilt in scripts/fiches/parts/simon_D.py; the body comes from simon_A..C.
"""
import copy


def two(en, fr): return {"en": en, "fr": fr}


def build(cl, CH):
    import importlib
    P = {k: importlib.import_module(f"fiches.parts.simon_{k}") for k in "ABCD"}
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
    _g(1, "Simon Pearson in a black top hat and knitted sweater, arms crossed", "Simon Pearson en haut-de-forme noir et pull tricoté, bras croisés",
       "Pearson in 1899.", "Pearson en 1899."),
    _g(2, "Close-up of Pearson in a fur coat in the snow", "Gros plan de Pearson en manteau de fourrure dans la neige",
       "Pearson at Colter.", "Pearson à Colter."),
    _g(3, "Pearson, Arthur and Charles in a dark cabin", "Pearson, Arthur et Charles dans une cabane sombre",
       "Pearson, Arthur and Charles at Colter.", "Pearson, Arthur et Charles à Colter."),
    _g(4, "Pearson speaking to the gang in camp", "Pearson s'adressant au gang au camp",
       "\"We need food.\"", "\"We need food.\""),
    _g(5, "Pearson talking to Arthur in the cold", "Pearson parlant à Arthur dans le froid",
       "Pearson telling Arthur a navy story.", "Pearson raconte à Arthur une histoire de marine."),
    _g(6, "Pearson holding a knife, Micah and Arthur behind him", "Pearson tenant un couteau, Micah et Arthur derrière lui",
       "\"Like a cornered tiger.\"", "\"Like a cornered tiger.\""),
    _g(7, "Pearson with Arthur, Dutch and Micah under a tent by the lake", "Pearson avec Arthur, Dutch et Micah sous une tente au bord du lac",
       "Pearson tells Dutch about the O'Driscolls' offer.", "Pearson rapporte à Dutch l'offre des O'Driscoll."),
    _g(8, "Pearson facing Arthur, a woman in the foreground", "Pearson face à Arthur, une femme au premier plan",
       "Pearson and Sadie in a row over the kitchen work.", "Pearson et Sadie se disputent à propos des corvées de cuisine."),
    _g(9, "Pearson holding out a letter to Arthur", "Pearson tendant une lettre à Arthur",
       "Pearson giving Arthur the letter for his aunt.", "Pearson confie à Arthur la lettre pour sa tante."),
    _g(10, "Pearson and Hosea at a camp table", "Pearson et Hosea à une table du camp",
       "Pearson sharing a table with Hosea, Clemens Point.", "Pearson attablé avec Hosea, à Clemens Point."),
    _g(11, "Pearson playing an accordion by a tent at night", "Pearson jouant de l'accordéon près d'une tente, la nuit",
       "Pearson playing the accordion in camp at night.", "Pearson joue de l'accordéon au camp, la nuit."),
    _g(12, "Pearson in an apron behind a store counter", "Pearson en tablier derrière le comptoir d'un magasin",
       "Pearson in 1907.", "Pearson en 1907."),
    _g(13, "Pearson in a winter coat behind a store counter", "Pearson en manteau d'hiver derrière le comptoir d'un magasin",
       "Pearson behind his counter in a winter coat, 1907.", "Pearson derrière son comptoir en manteau d'hiver, 1907."),
    _g(14, "An anchor tattoo on the back of Pearson's hand", "Une ancre tatouée sur le dos de la main de Pearson",
       "The anchor tattoo on the back of his hand.", "L'ancre tatouée sur le dos de sa main."),
]
