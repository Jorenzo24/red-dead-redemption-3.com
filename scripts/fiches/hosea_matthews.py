"""Hosea Matthews, full reference fiche (v3, Oct 2026).

Same pipeline as John, Arthur, Dutch, Sadie and Micah. His phase-2 page was hand-written HTML
with no data source, so the base (meta, facts, intro, Development, Reception)
is rebuilt in scripts/fiches/parts/hosea_D.py; the body comes from hosea_A..C.
"""
import copy


def two(en, fr): return {"en": en, "fr": fr}


def build(cl, CH):
    import importlib
    P = {k: importlib.import_module(f"fiches.parts.hosea_{k}") for k in "ABCD"}
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
    d["updated"] = "2026-10-16"
    return d


# Gallery: official art and in-game captures sourced from the Red Dead Wiki
# (rights checked by Joseph before publication), chronological.
def _g(n, alt_en, alt_fr, cap_en, cap_fr):
    return {"img": f"gallery-{n}.jpeg", "alt": two(alt_en, alt_fr), "cap": two(cap_en, cap_fr)}

GALLERY = [
    _g(1, "Red Dead Redemption 2 character poster of Hosea Matthews holding a rifle", "Affiche du personnage de Hosea Matthews pour Red Dead Redemption 2, un fusil à la main",
       "Official character poster, Red Dead Redemption 2.", "Affiche officielle du personnage, Red Dead Redemption 2."),
    _g(2, "Old photograph of a young Hosea with Dutch and Arthur", "Photographie ancienne d'un jeune Hosea avec Dutch et Arthur",
       "The photograph of a young Hosea (left) with Dutch and Arthur.", "La photographie d'un jeune Hosea (à gauche) avec Dutch et Arthur."),
    _g(3, "Hosea in his fur-collared coat at Horseshoe Overlook", "Hosea dans son manteau à col de fourrure, à Horseshoe Overlook",
       "Hosea at Horseshoe Overlook.", "Hosea à Horseshoe Overlook."),
    _g(4, "Hosea sitting in the woods cleaning his rifle", "Hosea assis dans les bois, nettoyant son fusil",
       "Hosea cleaning his rifle at Horseshoe Overlook.", "Hosea nettoie son fusil à Horseshoe Overlook."),
    _g(5, "Hosea reading with Jack Marston while Abigail looks on", "Hosea lisant avec Jack Marston sous le regard d'Abigail",
       "Hosea teaching Jack to read.", "Hosea apprend à lire à Jack."),
    _g(6, "The Van der Linde gang standing together at sunset", "Le gang Van der Linde réuni au coucher du soleil",
       "The gang in the third trailer.", "Le gang dans la troisième bande-annonce."),
    _g(7, "Hosea being shot in a Saint Denis street", "Hosea abattu dans une rue de Saint-Denis",
       "Chapter 4, \"Banking, The Old American Art\": Milton kills Hosea.", "Chapitre 4, \"Banking, The Old American Art\" : Milton tue Hosea."),
    _g(8, "A grave marker in the grass", "Une pierre tombale dans l'herbe",
       "Hosea's grave.", "La tombe de Hosea."),
    _g(9, "A Silver Turkoman horse", "Un cheval Turkoman argenté",
       "A Silver Turkoman, the breed and coat of Silver Dollar, Hosea's horse.", "Un Turkoman argenté, la race et la robe de Silver Dollar, le cheval de Hosea."),
]
