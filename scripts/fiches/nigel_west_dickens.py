"""Nigel West Dickens, reference fiche (v3, Oct 2026, medium tier).

Same pipeline as the other v3 fiches (scripts/v3/PROCEDURE.md). The base (meta, facts, intro, Development,
Reception) is rebuilt in scripts/fiches/parts/nigel_D.py; the body comes from nigel_A..C.
"""
import copy


def two(en, fr): return {"en": en, "fr": fr}


def build(cl, CH):
    import importlib
    P = {k: importlib.import_module(f"fiches.parts.nigel_{k}") for k in "ABCD"}
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
        sec("Trade and the elixir", "Le commerce et l'élixir", P["B"].BLOCKS_SKILLS),
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
    d["updated"] = "2026-10-21"
    return d


# Gallery: official art and in-game captures sourced from the Red Dead Wiki
# (rights checked by Joseph before publication), chronological.
def _g(n, alt_en, alt_fr, cap_en, cap_fr):
    return {"img": f"gallery-{n}.jpeg", "alt": two(alt_en, alt_fr), "cap": two(cap_en, cap_fr)}

GALLERY = [
    _g(1, "Close-up of Nigel West Dickens in a top hat", "Gros plan de Nigel West Dickens en haut-de-forme",
       "Nigel West Dickens, as rendered in the 2023 port of Red Dead Redemption.", "Nigel West Dickens dans le portage de Red Dead Redemption sorti en 2023."),
    _g(2, "Dickens pitching bottles from a table", "Dickens vantant ses flacons derrière une table",
       "Dickens selling his elixir.", "Dickens vend son élixir."),
    _g(3, "Dickens beside a sign bearing his initials", "Dickens près d'une enseigne à ses initiales",
       "Dickens by his \"N.W. Dickens\" sign.", "Dickens près de son enseigne \"N.W. Dickens\"."),
    _g(4, "Dickens and John Marston side by side in a town", "Dickens et John Marston côte à côte en ville",
       "Dickens with John Marston.", "Dickens avec John Marston."),
    _g(5, "A covered wagon painted with Dickens's name", "Un chariot bâché peint au nom de Dickens",
       "Dickens's wagon.", "Le chariot de Dickens."),
    _g(6, "Dickens speaking with men outside a fort", "Dickens parlant à des hommes devant un fort",
       "Dickens during the operation against Fort Mercer.", "Dickens pendant l'opération contre Fort Mercer."),
    _g(7, "Dickens beside a uniformed lawman", "Dickens à côté d'un homme de loi en uniforme",
       "Dickens with a lawman.", "Dickens avec un homme de loi."),
]
