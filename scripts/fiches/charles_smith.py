"""Charles Smith, full reference fiche (v3, Oct 2026).

Same pipeline as John, Arthur, Dutch, Sadie, Micah and Hosea. His phase-2 page was hand-written HTML
with no data source, so the base (meta, facts, intro, Development, Reception)
is rebuilt in scripts/fiches/parts/charles_D.py; the body comes from charles_A..C.
"""
import copy


def two(en, fr): return {"en": en, "fr": fr}


def build(cl, CH):
    import importlib
    P = {k: importlib.import_module(f"fiches.parts.charles_{k}") for k in "ABCD"}
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
    _g(1, "Red Dead Redemption 2 character poster of Charles Smith", "Affiche du personnage de Charles Smith pour Red Dead Redemption 2",
       "Official character poster, Red Dead Redemption 2.", "Affiche officielle du personnage, Red Dead Redemption 2."),
    _g(2, "A hand holding an oval photograph of a couple with an infant", "Une main tenant une photographie ovale d'un couple avec un nourrisson",
       "The photograph of an infant Charles with his mother and father.", "La photographie de Charles bébé avec sa mère et son père."),
    _g(3, "Charles Smith standing in a field in a blue coat", "Charles Smith debout dans un champ, en manteau bleu",
       "Charles in chapter 2.", "Charles au chapitre 2."),
    _g(4, "Charles drawing a bow, his face covered by a bandana", "Charles bandant un arc, le visage couvert d'un foulard",
       "Charles aiming his bow.", "Charles vise à l'arc."),
    _g(5, "Charles in a disguise and mask inside a bank", "Charles déguisé et masqué dans une banque",
       "Charles's disguise for the Saint Denis bank robbery.", "Le déguisement de Charles pour le braquage de la banque de Saint-Denis."),
    _g(6, "The Van der Linde gang standing together at sunset", "Le gang Van der Linde réuni au coucher du soleil",
       "The gang in the third trailer.", "Le gang dans la troisième bande-annonce."),
    _g(7, "Charles sitting wounded against a rock in the snow", "Charles assis contre un rocher dans la neige, blessé",
       "1907, \"American Venom\": Charles wounded by a sniper on Mount Hagen.", "1907, \"American Venom\" : Charles blessé par un tireur embusqué au mont Hagen."),
    _g(8, "Charles's sawed-off shotgun", "Le fusil à canon scié de Charles",
       "Charles's Sawed-Off Shotgun.", "Le fusil à canon scié de Charles."),
]
