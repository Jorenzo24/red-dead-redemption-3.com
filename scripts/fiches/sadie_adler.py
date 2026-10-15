"""Sadie Adler, full reference fiche (v3, Oct 2026).

Same pipeline as John, Arthur and Dutch. Her phase-2 page was hand-written HTML
with no data source, so the base (meta, facts, intro, Development, Reception)
is rebuilt in scripts/fiches/parts/sadie_D.py; the body comes from sadie_A..C.
"""
import copy


def two(en, fr): return {"en": en, "fr": fr}


def build(cl, CH):
    import importlib
    P = {k: importlib.import_module(f"fiches.parts.sadie_{k}") for k in "ABCD"}
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
    _g(1, "Red Dead Redemption 2 key art of Sadie Adler with two revolvers", "Artwork de Red Dead Redemption 2 : Sadie Adler, un revolver dans chaque main",
       "Official Red Dead Redemption 2 key art.", "Artwork officiel de Red Dead Redemption 2."),
    _g(2, "Sadie sitting on a rock at Horseshoe Overlook in a widow's dress", "Sadie assise sur un rocher à Horseshoe Overlook, en robe de veuve",
       "1899, chapter 2: Sadie at Horseshoe Overlook.", "1899, chapitre 2 : Sadie à Horseshoe Overlook."),
    _g(3, "Sadie reading a book in the woods", "Sadie lisant un livre dans les bois",
       "Sadie reading at camp.", "Sadie lisant au camp."),
    _g(4, "Sadie by the campfire with members of the gang", "Sadie près du feu de camp avec des membres du gang",
       "Sadie listening to Hosea Matthews by the campfire.", "Sadie écoute Hosea Matthews près du feu de camp."),
    _g(5, "Close-up of Sadie in her hat and blue neckerchief", "Gros plan sur Sadie, chapeau et foulard bleu",
       "Sadie in 1899.", "Sadie en 1899."),
    _g(6, "Close-up of Sadie looking up", "Gros plan sur Sadie, le regard levé",
       "Sadie looking up.", "Sadie, le regard levé."),
    _g(7, "Sadie carrying a rifle in the forest", "Sadie, un fusil sur l'épaule, en forêt",
       "Sadie with a rifle.", "Sadie et son fusil."),
    _g(8, "Sadie in a yellow shirt aiming a revolver indoors", "Sadie en chemise jaune braquant un revolver en intérieur",
       "Sadie aiming a revolver.", "Sadie braque un revolver."),
    _g(9, "Sadie raising a knife in a dark barn", "Sadie levant un couteau dans une grange sombre",
       "Sadie with a knife.", "Sadie, un couteau à la main."),
    _g(10, "Sadie and Arthur Morgan beside a horse at sunset", "Sadie et Arthur Morgan près d'un cheval au coucher du soleil",
       "Sadie and Arthur Morgan.", "Sadie et Arthur Morgan."),
    _g(11, "Sadie and Arthur Morgan talking in the woods", "Sadie et Arthur Morgan discutant dans les bois",
       "Sadie and Arthur, third trailer.", "Sadie et Arthur, troisième bande-annonce."),
    _g(12, "Sadie and John Marston back to back among flames", "Sadie et John Marston dos à dos au milieu des flammes",
       "Sadie and John Marston, back to back.", "Sadie et John Marston, dos à dos."),
    _g(13, "Sadie and Abigail on horseback leaving Arthur behind", "Sadie et Abigail à cheval quittant Arthur",
       "\"Red Dead Redemption\": Arthur sends Sadie and Abigail on to Copperhead Landing.", "\"Red Dead Redemption\" : Arthur envoie Sadie et Abigail à Copperhead Landing."),
    _g(14, "Sadie in 1907 wearing a bandolier and a brown coat", "Sadie en 1907, cartouchière et manteau brun",
       "1907: Sadie the bounty hunter.", "1907 : Sadie chasseuse de primes."),
    _g(15, "Sadie in a hooded scarf holding a rifle", "Sadie, capuche et écharpe, un fusil à la main",
       "Sadie in Red Dead Online.", "Sadie dans Red Dead Online."),
]
