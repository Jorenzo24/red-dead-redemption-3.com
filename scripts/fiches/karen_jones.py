"""Karen Jones, reference fiche (v3, Oct 2026, medium tier).

Same pipeline as John, Arthur, Dutch, Sadie, Micah, Hosea, Charles, Bill, Javier, Abigail and Jack. His page came from
the v2 entry in _enrich.py, so the base (meta, facts, intro, Development, Reception)
is rebuilt in scripts/fiches/parts/karen_D.py; the body comes from karen_A..C.
"""
import copy


def two(en, fr): return {"en": en, "fr": fr}


def build(cl, CH):
    import importlib
    P = {k: importlib.import_module(f"fiches.parts.karen_{k}") for k in "ABCD"}
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
    _g(1, "Karen Jones in a winter coat in the snow", "Karen Jones en manteau d'hiver dans la neige",
       "Karen at Colter, 1899.", "Karen à Colter, 1899."),
    _g(2, "Karen, Mary-Beth and Tilly sitting in the grass", "Karen, Mary-Beth et Tilly assises dans l'herbe",
       "Karen, Mary-Beth and Tilly at Horseshoe Overlook.", "Karen, Mary-Beth et Tilly à Horseshoe Overlook."),
    _g(3, "Karen standing by a campfire at night", "Karen debout près d'un feu de camp, la nuit",
       "Singing at the campfire at Horseshoe Overlook.", "Elle chante au coin du feu à Horseshoe Overlook."),
    _g(4, "Karen and Sean sitting close together at night", "Karen et Sean assis l'un contre l'autre, la nuit",
       "With Sean at his welcome-home party.", "Avec Sean lors de la fête donnée pour son retour."),
    _g(5, "Karen holding a rifle in camp", "Karen tenant un fusil au camp",
       "On guard duty at Shady Belle.", "De garde à Shady Belle."),
    _g(6, "Karen asleep on a cot", "Karen endormie sur un lit de camp",
       "Karen asleep in camp.", "Karen endormie au camp."),
    _g(7, "Karen, disheveled, standing among trees", "Karen, débraillée, debout parmi les arbres",
       "Karen at Beaver Hollow.", "Karen à Beaver Hollow."),
    _g(8, "Karen's horse, a dark grey Nokota", "Le cheval de Karen, un Nokota gris foncé",
       "Her horse, Old Belle.", "Son cheval, Old Belle."),
]
