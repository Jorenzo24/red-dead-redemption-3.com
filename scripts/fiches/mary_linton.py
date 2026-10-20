"""Mary Linton, reference fiche (v3, Oct 2026, medium tier).

Same pipeline as John, Arthur, Dutch, Sadie, Micah, Hosea, Charles, Bill, Javier, Abigail and Jack. His page came from
the v2 entry in _enrich.py, so the base (meta, facts, intro, Development, Reception)
is rebuilt in scripts/fiches/parts/linton_D.py; the body comes from linton_A..C.
"""
import copy


def two(en, fr): return {"en": en, "fr": fr}


def build(cl, CH):
    import importlib
    P = {k: importlib.import_module(f"fiches.parts.linton_{k}") for k in "ABCD"}
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
    _g(1, "Close-up of Mary Linton in a teal blouse", "Gros plan de Mary Linton en chemisier bleu-vert",
       "Mary at Chadwick Farm, in chapter 2 (1899).", "Mary à Chadwick Farm, au chapitre 2 (1899)."),
    _g(2, "Old photograph of a young man and woman", "Vieille photographie d'un jeune homme et d'une jeune femme",
       "The \"Young Mary & Arthur Photograph\", which comes with her goodbye letter.",
       "La photographie \"Young Mary & Arthur Photograph\", jointe à sa lettre d'adieu."),
    _g(3, "Mary in a black hat on a hillside", "Mary en chapeau noir sur une colline",
       "Mary in mourning, during the end credits.", "Mary en deuil, pendant le générique de fin."),
    _g(4, "Mary standing beside a flower-covered grave cross", "Mary debout près d'une croix de tombe couverte de fleurs",
       "Mary at Arthur's grave in the end credits; the flowers appear when Arthur finished chapter 6 with high honor.",
       "Mary devant la tombe d'Arthur, dans le générique de fin ; la tombe n'est fleurie que si Arthur a terminé le chapitre 6 avec un honneur élevé."),
]
