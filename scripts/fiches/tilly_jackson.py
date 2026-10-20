"""Tilly Jackson, reference fiche (v3, Oct 2026, medium tier).

Same pipeline as John, Arthur, Dutch, Sadie, Micah, Hosea, Charles, Bill, Javier, Abigail and Jack. His page came from
the v2 entry in _enrich.py, so the base (meta, facts, intro, Development, Reception)
is rebuilt in scripts/fiches/parts/tilly_D.py; the body comes from tilly_A..C.
"""
import copy


def two(en, fr): return {"en": en, "fr": fr}


def build(cl, CH):
    import importlib
    P = {k: importlib.import_module(f"fiches.parts.tilly_{k}") for k in "ABCD"}
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
        sec("Camp work and activities", "Travaux et activités au camp", P["B"].BLOCKS_SKILLS),
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
    _g(1, "Close-up of Tilly Jackson in a red shawl", "Gros plan de Tilly Jackson en châle rouge",
       "Tilly in 1899.", "Tilly en 1899."),
    _g(2, "Tilly washing clothes in a tub, a rifle on her back", "Tilly lavant du linge dans une bassine, un fusil dans le dos",
       "Tilly with a Carbine Repeater.", "Tilly et sa Carbine Repeater."),
    _g(3, "Tilly sitting on the ground in camp", "Tilly assise par terre au camp",
       "Tilly at Clemens Point.", "Tilly à Clemens Point."),
    _g(4, "Tilly standing beside a wagon", "Tilly debout à côté d'un chariot",
       "Tilly at Shady Belle.", "Tilly à Shady Belle."),
    _g(5, "Close-up of Tilly in a striped dress and red bow", "Gros plan de Tilly en robe rayée et nœud rouge",
       "Tilly in 1907.", "Tilly en 1907."),
    _g(6, "Tilly in a city street", "Tilly dans une rue de la ville",
       "1907: Tilly bids John farewell.", "1907 : Tilly dit au revoir à John."),
    _g(7, "Tilly with a man and a child in a park", "Tilly avec un homme et un enfant dans un parc",
       "Tilly with her husband and child in the end credits.", "Tilly avec son mari et son enfant dans le générique de fin."),
]
