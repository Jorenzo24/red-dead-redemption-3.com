"""Kieran Duffy, reference fiche (v3, Oct 2026, medium tier).

Same pipeline as John, Arthur, Dutch, Sadie, Micah, Hosea, Charles, Bill, Javier, Abigail and Jack. His page came from
the v2 entry in _enrich.py, so the base (meta, facts, intro, Development, Reception)
is rebuilt in scripts/fiches/parts/kieran_D.py; the body comes from kieran_A..C.
"""
import copy


def two(en, fr): return {"en": en, "fr": fr}


def build(cl, CH):
    import importlib
    P = {k: importlib.import_module(f"fiches.parts.kieran_{k}") for k in "ABCD"}
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
    _g(1, "Kieran Duffy in a wide hat and open shirt", "Kieran Duffy en chapeau large et chemise ouverte",
       "Kieran in 1899.", "Kieran en 1899."),
    _g(2, "A rider leaving a snowy camp", "Un cavalier quittant un camp enneigé",
       "Kieran leaving the O'Driscoll camp.", "Kieran quitte le camp des O'Driscoll."),
    _g(3, "A rider fleeing through the snow", "Un cavalier fuyant dans la neige",
       "\"Old Friends\": Kieran chased by Arthur.", "\"Old Friends\" : Kieran poursuivi par Arthur."),
    _g(4, "Kieran standing in a dark stable", "Kieran debout dans une écurie sombre",
       "Held in the stable at Colter.", "Retenu dans l'écurie de Colter."),
    _g(5, "Kieran lifting a saddle in camp", "Kieran soulevant une selle au camp",
       "Picking up a saddle at Horseshoe Overlook.", "Il soulève une selle à Horseshoe Overlook."),
    _g(6, "Kieran and Mary-Beth sitting by wagons", "Kieran et Mary-Beth assis près des chariots",
       "With Mary-Beth in camp.", "Avec Mary-Beth au camp."),
    _g(7, "Kieran at a table with Abigail and Karen nearby", "Kieran à une table, près d'Abigail et de Karen",
       "Kieran talking to Abigail.", "Kieran parle à Abigail."),
    _g(8, "Kieran wiping a table at night", "Kieran essuyant une table, la nuit",
       "Cleaning the tables at Clemens Point.", "Il nettoie les tables à Clemens Point."),
    _g(9, "A wooden grave marker on a mound of earth", "Une stèle de bois sur un monticule de terre",
       "Kieran's grave.", "La tombe de Kieran."),
    _g(10, "Kieran's Cattleman revolver with an ivory grip", "Le revolver Cattleman de Kieran à crosse d'ivoire",
       "His unique Cattleman Revolver.", "Son revolver Cattleman unique."),
    _g(11, "Kieran's horse, a roan Tennessee Walker", "Le cheval de Kieran, un Tennessee Walker rouan",
       "His horse, Branwen.", "Son cheval, Branwen."),
]
