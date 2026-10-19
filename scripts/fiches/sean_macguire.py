"""Sean MacGuire, reference fiche (v3, Oct 2026, medium tier).

Same pipeline as John, Arthur, Dutch, Sadie, Micah, Hosea, Charles, Bill, Javier, Abigail and Jack. His page came from
the v2 entry in _enrich.py, so the base (meta, facts, intro, Development, Reception)
is rebuilt in scripts/fiches/parts/sean_D.py; the body comes from sean_A..C.
"""
import copy


def two(en, fr): return {"en": en, "fr": fr}


def build(cl, CH):
    import importlib
    P = {k: importlib.import_module(f"fiches.parts.sean_{k}") for k in "ABCD"}
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
    _g(1, "Sean MacGuire in a green bowler hat, outdoors", "Sean MacGuire en chapeau melon vert, en plein air",
       "Sean in 1899.", "Sean en 1899."),
    _g(2, "Sean and Karen by a campfire at night", "Sean et Karen près d'un feu de camp, la nuit",
       "With Karen at his welcome-home party.", "Avec Karen lors de la fête donnée pour son retour."),
    _g(3, "Sean standing by a tree with mountains behind", "Sean debout près d'un arbre, des montagnes au fond",
       "Sean whittling wood at Horseshoe Overlook.", "Sean taille un morceau de bois à Horseshoe Overlook."),
    _g(4, "Sean standing next to Molly, who is reading", "Sean debout à côté de Molly, qui lit",
       "With Molly at Horseshoe Overlook.", "Avec Molly à Horseshoe Overlook."),
    _g(5, "Sean and Arthur on horseback, masked", "Sean et Arthur à cheval, masqués",
       "Sean and Arthur during the train robbery.", "Sean et Arthur pendant l'attaque du train."),
    _g(6, "Arthur and Sean inside a train car", "Arthur et Sean dans un wagon",
       "Arthur and Sean inside the train.", "Arthur et Sean à l'intérieur du train."),
    _g(7, "Sean leaning over a table in camp", "Sean penché sur une table au camp",
       "Sean planning a coach robbery.", "Sean prépare l'attaque d'une diligence."),
    _g(8, "Sean talking with Arthur in camp", "Sean discutant avec Arthur au camp",
       "Sean and Arthur discussing the coach robbery.", "Sean et Arthur parlent de l'attaque de la diligence."),
    _g(9, "Masked Sean in a dark barn", "Sean masqué dans une grange sombre",
       "Sean dousing the Grays' barn.", "Sean arrose la grange des Gray."),
    _g(10, "Sean holding a lit fire bottle at night", "Sean tenant une bouteille incendiaire allumée, la nuit",
       "Sean holding a fire bottle.", "Sean, une bouteille incendiaire à la main."),
    _g(11, "Sean leaning against a post in Rhodes", "Sean appuyé contre un poteau à Rhodes",
       "His last cigarette, in Rhodes.", "Sa dernière cigarette, à Rhodes."),
    _g(12, "A pencil drawing of a fallen man in a journal", "Un dessin au crayon d'un homme à terre dans un journal",
       "Arthur's journal drawing after Sean's death.", "Le dessin du journal d'Arthur après la mort de Sean."),
    _g(13, "A stone grave with a wooden cross under trees", "Une tombe de pierres surmontée d'une croix de bois, sous des arbres",
       "Sean's grave.", "La tombe de Sean."),
    _g(14, "Sean's Cattleman revolver", "Le revolver Cattleman de Sean",
       "His Cattleman Revolver.", "Son revolver Cattleman."),
    _g(15, "Close-up of Sean in Red Dead Online", "Gros plan de Sean dans Red Dead Online",
       "Sean in Red Dead Online.", "Sean dans Red Dead Online."),
    _g(16, "Sean sitting by a tent at a camp", "Sean assis près d'une tente, dans un camp",
       "His camp near Quaker's Cove in Red Dead Online.", "Son camp près de Quaker's Cove dans Red Dead Online."),
]
