"""Uncle, full reference fiche (v3, Oct 2026).

Same pipeline as John, Arthur, Dutch, Sadie, Micah, Hosea, Charles, Bill, Javier, Abigail and Jack. His page came from
the v2 entry in _enrich.py, so the base (meta, facts, intro, Development, Reception)
is rebuilt in scripts/fiches/parts/uncle_D.py; the body comes from uncle_A..C.
"""
import copy


def two(en, fr): return {"en": en, "fr": fr}


def build(cl, CH):
    import importlib
    P = {k: importlib.import_module(f"fiches.parts.uncle_{k}") for k in "ABCD"}
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
    _g(1, "Uncle in a fur-collared coat in the snow", "Uncle en manteau à col de fourrure dans la neige",
       "Uncle at Colter, 1899.", "Uncle à Colter, 1899."),
    _g(2, "Uncle riding on a wagon seat", "Uncle assis sur le banc d'un chariot",
       "\"Polite Society, Valentine Style\": Uncle riding shotgun.", "\"Polite Society, Valentine Style\" : Uncle sur le siège du passager."),
    _g(3, "Uncle standing on a boardwalk in Valentine", "Uncle sur un trottoir de planches à Valentine",
       "Uncle in Valentine.", "Uncle à Valentine."),
    _g(4, "Arthur and Uncle talking outside a store", "Arthur et Uncle discutant devant un magasin",
       "With Arthur outside Worths General Store.", "Avec Arthur devant le Worths General Store."),
    _g(5, "Javier, Uncle and Arthur around a campfire at night", "Javier, Uncle et Arthur autour d'un feu de camp, la nuit",
       "Javier, Uncle and Arthur by the fire, third trailer.", "Javier, Uncle et Arthur autour du feu, troisième bande-annonce."),
    _g(6, "Close-up of Uncle in a red shirt", "Gros plan d'Uncle en chemise rouge",
       "Uncle at Clemens Point.", "Uncle à Clemens Point."),
    _g(7, "Uncle sitting on a crate with a bottle", "Uncle assis sur une caisse, une bouteille à la main",
       "Sitting at a camp table.", "Assis à une table du camp."),
    _g(8, "Uncle firing a revolver in a yard", "Uncle tirant au revolver dans une cour",
       "Uncle firing his custom Schofield Revolver.", "Uncle tire avec son revolver Schofield personnalisé."),
    _g(9, "Uncle's custom Schofield revolver", "Le revolver Schofield personnalisé d'Uncle",
       "His custom Schofield Revolver.", "Son revolver Schofield personnalisé."),
    _g(10, "Uncle holding a broom inside a dark building", "Uncle tenant un balai dans un bâtiment sombre",
       "1907: sweeping at Beecher's Hope.", "1907 : il balaie à Beecher's Hope."),
    _g(11, "Uncle without his hat, indoors", "Uncle sans chapeau, à l'intérieur",
       "1907: without his hat.", "1907 : sans son chapeau."),
    _g(12, "Close-up of Uncle outdoors in 1907", "Gros plan d'Uncle en extérieur, en 1907",
       "1907, \"A Quick Favor for an Old Friend\".", "1907, \"A Quick Favor for an Old Friend\"."),
    _g(13, "Close-up of an older Uncle in Red Dead Redemption", "Gros plan d'Uncle plus âgé dans Red Dead Redemption",
       "Uncle in 1911, in Red Dead Redemption.", "Uncle en 1911, dans Red Dead Redemption."),
    _g(14, "Uncle with his arms wide open in front of the ranch house", "Uncle les bras grands ouverts devant la maison du ranch",
       "1911: Uncle welcomes John home.", "1911 : Uncle accueille John à son retour."),
    _g(15, "John facing Uncle outdoors", "John face à Uncle en plein air",
       "1911: John threatening Uncle.", "1911 : John menace Uncle."),
    _g(16, "Uncle and John armed, side by side at the ranch", "Uncle et John armés, côte à côte au ranch",
       "1911: Uncle and John preparing for the last stand.", "1911 : Uncle et John se préparent au dernier combat."),
    _g(17, "Uncle lying wounded with Jack and John nearby", "Uncle étendu, blessé, près de Jack et de John",
       "1911, \"The Last Enemy That Shall Be Destroyed\": Uncle's death.", "1911, \"The Last Enemy That Shall Be Destroyed\" : la mort d'Uncle."),
    _g(18, "Undead Uncle at night", "Uncle mort-vivant, la nuit",
       "Undead Nightmare (non-canon): Uncle as one of the undead.", "Undead Nightmare (hors canon) : Uncle devenu mort-vivant."),
]
