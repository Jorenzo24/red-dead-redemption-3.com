"""Edgar Ross, reference fiche (v3, Oct 2026, medium tier).

Same pipeline as John, Arthur, Dutch, Sadie, Micah, Hosea, Charles, Bill, Javier, Abigail and Jack. His page came from
the v2 entry in _enrich.py, so the base (meta, facts, intro, Development, Reception)
is rebuilt in scripts/fiches/parts/edgar_D.py; the body comes from edgar_A..C.
"""
import copy


def two(en, fr): return {"en": en, "fr": fr}


def build(cl, CH):
    import importlib
    P = {k: importlib.import_module(f"fiches.parts.edgar_{k}") for k in "ABCD"}
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
        sec("Bureau work, weapons and horses", "Méthodes du Bureau, armes et chevaux", P["B"].BLOCKS_SKILLS),
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
    d["updated"] = "2026-10-20"
    return d


# Gallery: official art and in-game captures sourced from the Red Dead Wiki
# (rights checked by Joseph before publication), chronological.
def _g(n, alt_en, alt_fr, cap_en, cap_fr):
    return {"img": f"gallery-{n}.jpeg", "alt": two(alt_en, alt_fr), "cap": two(cap_en, cap_fr)}

GALLERY = [
    _g(1, "Close-up of Edgar Ross with a badge", "Gros plan d'Edgar Ross avec son insigne",
       "Edgar Ross in Red Dead Redemption 2.", "Edgar Ross dans Red Dead Redemption 2."),
    _g(2, "Two agents in bowler hats, one raising a hand", "Deux agents en chapeau melon, l'un levant la main",
       "Agents Milton and Ross in 1899.", "Les agents Milton et Ross en 1899."),
    _g(3, "Two agents facing armed men at a camp", "Deux agents face à des hommes armés dans un camp",
       "Milton and Ross at the gang's camp in 1899.", "Milton et Ross au camp du gang en 1899."),
    _g(4, "Two men walking towards a body in the snow", "Deux hommes marchant vers un corps dans la neige",
       "Ross and Archer Fordham after Micah's death, 1907.", "Ross et Archer Fordham après la mort de Micah, en 1907."),
    _g(5, "Ross in a bowler hat in an office", "Ross en chapeau melon dans un bureau",
       "Ross in Red Dead Redemption.", "Ross dans Red Dead Redemption."),
    _g(6, "Three men walking in a town street", "Trois hommes marchant dans une rue",
       "Ross, John Marston and Archer Fordham in 1911.", "Ross, John Marston et Archer Fordham en 1911."),
    _g(7, "Ross raising his hands in the snow", "Ross levant les mains dans la neige",
       "Ross in the mountains in 1911.", "Ross dans les montagnes en 1911."),
    _g(8, "Ross gesturing with a cigar", "Ross faisant un geste, un cigare à la main",
       "Ross in 1911.", "Ross en 1911."),
    _g(9, "Close-up of Ross in a dark room", "Gros plan de Ross dans une pièce sombre",
       "Ross in 1911.", "Ross en 1911."),
    _g(10, "Ross in a wide-brimmed hat and neckerchief", "Ross en chapeau à large bord et foulard",
       "Ross retired, in 1914.", "Ross à la retraite, en 1914."),
    _g(11, "Ross standing by a river", "Ross au bord d'une rivière",
       "Ross at the river in 1914.", "Ross au bord de la rivière en 1914."),
]
