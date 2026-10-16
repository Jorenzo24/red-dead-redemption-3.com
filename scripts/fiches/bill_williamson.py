"""Bill Williamson, full reference fiche (v3, Oct 2026).

Same pipeline as John, Arthur, Dutch, Sadie, Micah, Hosea and Charles. His phase-2 page was hand-written HTML
with no data source, so the base (meta, facts, intro, Development, Reception)
is rebuilt in scripts/fiches/parts/bill_D.py; the body comes from bill_A..C.
"""
import copy


def two(en, fr): return {"en": en, "fr": fr}


def build(cl, CH):
    import importlib
    P = {k: importlib.import_module(f"fiches.parts.bill_{k}") for k in "ABCD"}
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
    _g(1, "Bill Williamson firing a shotgun from behind a wooden wall in the snow", "Bill Williamson tirant au fusil derrière un mur de bois, dans la neige",
       "1899, \"Old Friends\": Bill fires on the O'Driscolls at their camp in Ewing Basin.", "1899, \"Old Friends\" : Bill tire sur les O'Driscoll dans leur camp d'Ewing Basin."),
    _g(2, "Bill standing on the porch of the Valentine saloon", "Bill debout sur le perron du saloon de Valentine",
       "\"Americans at Rest\": Bill outside the saloon during Arthur's fight with Tommy.", "\"Americans at Rest\" : Bill devant le saloon pendant la bagarre d'Arthur contre Tommy."),
    _g(3, "Bill Williamson in a brown coat holding a bottle, mountains behind him", "Bill Williamson en manteau brun, une bouteille à la main, devant des montagnes",
       "Bill at Horseshoe Overlook.", "Bill à Horseshoe Overlook."),
    _g(4, "Bill holding gelding tongs in camp at night", "Bill tenant une pince à castrer, la nuit au camp",
       "Bill with the gelding tongs, camp at Horseshoe Overlook.", "Bill et sa pince à castrer, au camp de Horseshoe Overlook."),
    _g(5, "Bill lying drunk on the grass next to an overturned barrel", "Bill ivre, étendu dans l'herbe près d'un tonneau renversé",
       "Bill drunk after falling off his seat at Horseshoe Overlook.", "Bill ivre, tombé de son siège à Horseshoe Overlook."),
    _g(6, "Bill reading a map under a tarp", "Bill lisant une carte sous une bâche",
       "Bill planning a coach robbery.", "Bill prépare l'attaque d'une diligence."),
    _g(7, "Hands holding a U.S. Army discharge document", "Des mains tenant un certificat de renvoi de l'armée américaine",
       "Bill's dishonorable discharge papers from the United States Army.", "Le certificat de renvoi pour faute grave de Bill, signé par l'armée des États-Unis."),
    _g(8, "Bill in a plaid suit and white mask, holding a rifle in a bank", "Bill en costume à carreaux et masque blanc, fusil en main dans une banque",
       "Bill's disguise for the Saint Denis bank robbery.", "Le déguisement de Bill pour le braquage de la banque de Saint-Denis."),
    _g(9, "Bill leaning back in a folding chair with his feet on a table", "Bill renversé sur une chaise pliante, les pieds sur une table",
       "Bill resting in camp.", "Bill se repose au camp."),
    _g(10, "Bill Williamson's Schofield revolver", "Le revolver Schofield de Bill Williamson",
       "Bill's Schofield revolver.", "Le revolver Schofield de Bill."),
    _g(11, "Close-up of an older Bill Williamson with a bandana around his neck", "Gros plan de Bill Williamson plus âgé, foulard au cou",
       "Bill in 1911, in Red Dead Redemption.", "Bill en 1911, dans Red Dead Redemption."),
    _g(12, "Bill aiming a rifle from the walls of Fort Mercer at sunset", "Bill pointant un fusil depuis les murs de Fort Mercer au coucher du soleil",
       "1911, \"Exodus in America\": Bill holds a rifle on John at Fort Mercer.", "1911, \"Exodus in America\" : Bill tient John en joue à Fort Mercer."),
    _g(13, "Bill Williamson and his men on a dry hillside with horses", "Bill Williamson et ses hommes sur une colline aride, avec des chevaux",
       "\"Spare the Rod, Spoil the Bandit\": Bill and his men in New Austin.", "\"Spare the Rod, Spoil the Bandit\" : Bill et ses hommes à New Austin."),
    _g(14, "Bill and Colonel Allende in a dark room in Mexico", "Bill et le colonel Allende dans une pièce sombre, au Mexique",
       "Bill with Colonel Allende in Mexico, 1911.", "Bill avec le colonel Allende au Mexique, 1911."),
]
