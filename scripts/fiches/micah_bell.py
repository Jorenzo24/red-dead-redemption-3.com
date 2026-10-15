"""Micah Bell, full reference fiche (v3, Oct 2026).

Same pipeline as John, Arthur, Dutch and Sadie. His phase-2 page was hand-written HTML
with no data source, so the base (meta, facts, intro, Development, Reception)
is rebuilt in scripts/fiches/parts/micah_D.py; the body comes from micah_A..C.
"""
import copy


def two(en, fr): return {"en": en, "fr": fr}


def build(cl, CH):
    import importlib
    P = {k: importlib.import_module(f"fiches.parts.micah_{k}") for k in "ABCD"}
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
    d["updated"] = "2026-10-15"
    return d


# Gallery: official art and in-game captures sourced from the Red Dead Wiki
# (rights checked by Joseph before publication), chronological.
def _g(n, alt_en, alt_fr, cap_en, cap_fr):
    return {"img": f"gallery-{n}.jpeg", "alt": two(alt_en, alt_fr), "cap": two(cap_en, cap_fr)}

GALLERY = [
    _g(1, "Red Dead Redemption 2 character poster of Micah Bell with two revolvers", "Affiche du personnage de Micah Bell pour Red Dead Redemption 2, un revolver dans chaque main",
       "Official character poster, Red Dead Redemption 2.", "Affiche officielle du personnage, Red Dead Redemption 2."),
    _g(2, "Micah holding a lantern on horseback in the snow", "Micah à cheval dans la neige, une lanterne à la main",
       "Chapter 1, \"Outlaws from the West\": Micah's first appearance.", "Chapitre 1, \"Outlaws from the West\" : première apparition de Micah."),
    _g(3, "Close-up of Micah Bell in 1899", "Gros plan sur Micah Bell en 1899",
       "Micah in 1899.", "Micah en 1899."),
    _g(4, "Micah sitting by his tent at camp", "Micah assis près de sa tente, au camp",
       "Micah at Horseshoe Overlook.", "Micah à Horseshoe Overlook."),
    _g(5, "Micah and Hosea at a table in camp", "Micah et Hosea à une table du camp",
       "Micah and Hosea at camp.", "Micah et Hosea au camp."),
    _g(6, "Micah firing two revolvers", "Micah tirant avec deux revolvers",
       "Micah fighting in Strawberry.", "Micah en pleine fusillade à Strawberry."),
    _g(7, "Micah and Arthur firing side by side at night", "Micah et Arthur tirant côte à côte, de nuit",
       "Micah fighting alongside Arthur.", "Micah se bat aux côtés d'Arthur."),
    _g(8, "Micah and Arthur Morgan on horseback", "Micah et Arthur Morgan à cheval",
       "Micah and Arthur, third trailer.", "Micah et Arthur, troisième bande-annonce."),
    _g(9, "Micah in a pale suit", "Micah en costume clair",
       "Micah in the suit he wears for the Saint Denis bank robbery.", "Micah dans le costume qu'il porte pour le braquage de la banque de Saint-Denis."),
    _g(10, "Micah with an open shirt holding a rifle in the jungle", "Micah, chemise ouverte, un fusil à la main dans la jungle",
       "Chapter 5: Micah on Guarma.", "Chapitre 5 : Micah à Guarma."),
    _g(11, "Micah aiming an engraved revolver on Mount Hagen", "Micah braquant un revolver gravé au mont Hagen",
       "1907: Micah's duel with John on Mount Hagen.", "1907 : le duel de Micah contre John au mont Hagen."),
    _g(12, "Micah's engraved Double-Action Revolver", "Le Double-Action Revolver gravé de Micah",
       "Micah's Double-Action Revolver.", "Le Double-Action Revolver de Micah."),
    _g(13, "Micah's body lying in the snow", "Le corps de Micah dans la neige",
       "Micah's body on Mount Hagen.", "Le corps de Micah au mont Hagen."),
]
