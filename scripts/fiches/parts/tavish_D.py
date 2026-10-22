"""Tavish Gray, reference fiche, PART D: base data, Development and performance, Reception (22 Oct 2026, medium tier).

His live page (characters/tavish-gray/) was generated from the v2 entry in scripts/_wave7.py ("slug": "tavish-gray";
no entry in _enrich.py). The base below is rebuilt from that entry. publishDate 2026-10-14 and the eyebrow
("Character &middot; Lemoyne") are kept as on the live page; reg_role matches characters_registry.py
("Gray patriarch &middot; RDR2"). Changes against v2:
- v2 "death": None, while its own Status said "Found dead at Caliga Hall". Now "1899": the body ("Gray's Secret") can be
  found by Arthur once "Horse Flesh for Dinner" is done (Red Dead Wiki, "Gray's Secret"; Arthur's journal drawing).
  Cause of death still not stated (the wiki's pages disagree: suicide vs heart attack).
- v2 "Leigh Gray ... belongs to the same family" kept with both versions (brother per Beau's line and both wikis; son per
  Dutch and Arthur): told in part B (Leigh entry), the facts grid lists both.
- v2 "feuding ... for generations" kept as the game says it (Archibald: "for as long as I can remember"; Beau).
- v2 "Scottish descent": Tavish says "I'm Scottish" and "We're an old Scottish family"; nationality stays "American"
  (both wikis), the grid adds his own claim.
- v2 said the letter "states that his ancestor ... was a paid informer"; the letter is addressed to "Mr. Gray" and found
  beside him: worded that way in the intro.
- Chips "Gray family / Lemoyne / RDR2" replaced by "Died 1899", "Gray patriarch", "Caliga Hall" and the actor. Facts
  grid gains Name, Also called, Born, Died, Nationality, Family (expanded), Enemies, Voiced by.
- "Behind the scenes" (v2 section) becomes Development and performance. The Jon Gravelli credit is kept, now sourced to
  Wikipedia's Grand Theft Auto IV article.

SOURCE REGISTER (fetched 22 Oct 2026, saved in scripts/v3/work/tavish/fc/ and scripts/v3/work/_m/):
- Red Dead Wiki EN "Madison Arnold" (_m/Madison_Arnold.txt): American actor, voice of Tavish Gray (stub; birth date
  given by the wiki only: not used). Red Dead Wiki EN "Tavish Gray" infobox (voice: Madison Arnold) and FR "Tavish Gray"
  (acteur : Madison Arnold).
- GTABase, "Tavish Gray" character page (gtabase.com, fetched 22 Oct 2026): "He is portrayed by Madison Arnold."
- Wikipedia, "List of Red Dead Redemption 2 characters" (scripts/v3/work/catherine/fc/wp_list_rdr2.txt, citing the
  credits): does NOT list Tavish or his actor. No Rockstar credits text could be read (the credits page is rendered by
  script): the casting is therefore attributed to the Red Dead Wiki, not to "the credits".
- Wikipedia, "Grand Theft Auto IV" (fc/wp_GTA_IV.txt): "Jon Gravelli (Madison Arnold), the aging head of the city's most
  powerful crime family". GTA Wiki "Jon Gravelli" (fc/gtawiki_Jon_Gravelli.txt): "He is voiced by Madison Arnold."
- Red Dead Wiki "Red Dead Redemption 2 Cut Content" (_m/Red_Dead_Redemption_2_Cut_Content.txt): Tavish's unused vest; an
  unused Gray named Adam placed in Caliga Hall's cut interior with other Grays; Gray and Braithwaite family members met
  in free roam; the three stallions of "Horse Flesh for Dinner" originally unique (files a_c_horse_grays2_01/02/03);
  "Grey" spelling in the files.
- Reception: searches on 22 Oct 2026 (his name, "Gray's Secret", the letter) found no review or article discussing him
  beyond guides and wikis. BLOCKS_RECEPTION is an empty list.
- In-game transcript (fc/gsw.txt, see part B) for the base facts.

EXCLUDED: Madison Arnold's birth date (Red Dead Wiki only); "motion capture" (no source says he did it: only "voice");
the cause of death (sources disagree, nothing shown); the Villains Wiki; fan podcasts and YouTube videos; Wikipedia's
Polygon review remark on the "entitlement and power of the Braithwaite and Gray families" (about both families, not
him: could go to Catherine or a family page, not here).
DUPLICATE ownership: actor, Jon Gravelli and cut content live HERE; part C Trivia must not repeat them (the wiki's
Malcolm Moffat / Houser surname item stays in C).

FIX PASS (22 Oct 2026): intro states the sequence only (no reprisal); essentials and Ross Gray worded in the letter's terms
(paid informer), no "Jacobite" reading; "based on the credits" removed; Jon Gravelli reworded from GTA Wiki (boss of the
Gambetti crime family); portrait alt = stables, not porch.
"""


def two(en, fr): return {"en": en, "fr": fr}


BLOCKS_DEV = [
    {"h3": two("Casting", "Le casting")},
    {"p": two("Tavish Gray appears only in Red Dead Redemption 2 (2018). Wikipedia's list of the game's characters does not include him. The Red Dead Wiki, in English and in French, gives his voice to Madison Arnold, an American actor, and GTABase credits him with the role as well. Madison Arnold had already worked for Rockstar Games: Wikipedia's article on Grand Theft Auto IV (2008) credits him as the voice of Jon Gravelli, the elderly boss of the Gambetti crime family (GTA Wiki). No source states that he also performed the motion capture.",
              "Tavish Gray n'apparaît que dans Red Dead Redemption 2 (2018). La liste des personnages du jeu publiée par Wikipédia ne le mentionne pas. Le Red Dead Wiki, en anglais comme en français, attribue sa voix à Madison Arnold, un acteur américain, et GTABase lui prête aussi le rôle. Madison Arnold avait déjà travaillé pour Rockstar Games : l'article de Wikipédia consacré à Grand Theft Auto IV (2008) le crédite dans le rôle de Jon Gravelli, le vieux parrain de la famille Gambetti (GTA Wiki). Aucune source n'indique qu'il ait aussi assuré la capture de mouvement.")},
    {"h3": two("Cut content", "Contenu coupé")},
    {"p": two("The Red Dead Wiki's page on cut content lists an unused vest for Tavish. The game files also contain an unused member of the Gray family named Adam, who was to appear with other Grays inside Caliga Hall, an interior that was cut. According to the same page, members of the Gray and Braithwaite families could originally be met in free roam. The three stallions stolen in \"Horse Flesh for Dinner\" were first meant to be unique horses, and the family's name is sometimes spelled \"Grey\" in the files.",
              "La page du Red Dead Wiki consacrée au contenu coupé signale un gilet inutilisé pour Tavish. Les fichiers du jeu contiennent aussi un membre inutilisé de la famille Gray, prénommé Adam, qui devait apparaître avec d'autres Gray à l'intérieur de Caliga Hall, un intérieur finalement supprimé. Selon la même page, il devait à l'origine être possible de croiser des membres des familles Gray et Braithwaite en exploration libre. Les trois étalons volés dans \"Horse Flesh for Dinner\" devaient d'abord être des chevaux uniques, et le nom de la famille est parfois écrit \"Grey\" dans les fichiers.")},
]

# No review or article discussing Tavish Gray was found (searches of 22 Oct 2026): empty list, and the Reception
# section is left out of BASE["sections"] (never an empty section).
BLOCKS_RECEPTION = []


BASE = {
    "slug": "tavish-gray", "name": "Tavish Gray",
    "publishDate": "2026-10-14", "updated": "2026-10-22", "schema_game": "Red Dead Redemption 2",
    "reg_role_en": "Gray patriarch &middot; RDR2", "reg_role_fr": "Patriarche des Gray &middot; RDR2",
    "gender": "Male", "death": "1899", "nationality": "American",
    "portrait_alt": two("Tavish Gray at the Caliga Hall stables in Red Dead Redemption 2",
                        "Tavish Gray aux écuries de Caliga Hall dans Red Dead Redemption 2"),
    "eyebrow": two("Character &middot; Lemoyne", "Personnage &middot; Lemoyne"),
    "meta_desc": two("Tavish Gray, head of the Gray family of Caliga Hall in RDR2: the feud with the Braithwaites, the stolen horses, the fire in his tobacco fields, the letter found beside his body, Madison Arnold.",
                     "Tavish Gray, patriarche de la famille Gray à Caliga Hall dans RDR2 : la guerre avec les Braithwaite, les chevaux volés, l'incendie de ses champs de tabac, la lettre retrouvée près de son corps, Madison Arnold."),
    "og_desc": two("The complete reference on Tavish Gray: life, family, Caliga Hall, quotes and development.",
                   "La référence complète sur Tavish Gray : vie, famille, Caliga Hall, citations et conception."),
    "schema_desc": two("Head of the Gray family of Caliga Hall, in Lemoyne, who hires Arthur Morgan, John Marston and Javier Escuella to steal the Braithwaites' horses, and who is found dead on his estate in 1899, in Red Dead Redemption 2.",
                       "Patriarche de la famille Gray, à Caliga Hall, en Lemoyne, qui charge Arthur Morgan, John Marston et Javier Escuella de voler les chevaux des Braithwaite, et qui est retrouvé mort sur son domaine en 1899, dans Red Dead Redemption 2."),
    "chips": [two("Died <strong>1899</strong>", "Mort en <strong>1899</strong>"), two("Gray patriarch", "Patriarche des Gray"),
              two("Caliga Hall", "Caliga Hall"),
              two("Voiced by <strong>Madison Arnold</strong>", "Voix : <strong>Madison Arnold</strong>")],
    "facts": [
        {"label": two("Name", "Nom"), "value": two("Tavish Gray", "Tavish Gray")},
        {"label": two("Also called", "Autres noms"), "value": two("Mr. Gray", "Mr. Gray")},
        {"label": two("Born", "Naissance"), "value": two("Not given in the game", "Non précisée dans le jeu")},
        {"label": two("Died", "Mort"), "value": two("1899, found dead on a porch at Caliga Hall; the cause is not shown", "1899, retrouvé mort sous un porche de Caliga Hall ; la cause n'est pas montrée")},
        {"label": two("Status", "Statut"), "value": two("Deceased", "Décédé")},
        {"label": two("Nationality", "Nationalité"), "value": two("American; he calls himself Scottish", "Américaine ; il se dit écossais")},
        {"label": two("Residence", "Résidence"), "value": two("Caliga Hall, east of Rhodes, Lemoyne", "Caliga Hall, à l'est de Rhodes, en Lemoyne")},
        {"label": two("Occupation", "Activité"), "value": two("Head of the Gray family; tobacco planter", "Chef de la famille Gray ; planteur de tabac")},
        {"label": two("Family", "Famille"), "value": two("Son Beau Gray; Sheriff Leigh Gray (his brother according to Beau, his son according to Dutch and Arthur); father Murdo Gray (Beau calls himself Murdo's grandson); ancestor Ross Gray", "Son fils Beau Gray ; le shérif Leigh Gray (son frère selon Beau, son fils selon Dutch et Arthur) ; son père, Murdo Gray (Beau se dit petit-fils de Murdo) ; son ancêtre Ross Gray")},
        {"label": two("Enemies", "Ennemis"), "value": two("The Braithwaite family of [[catherine-braithwaite|Catherine Braithwaite]]", "La famille Braithwaite de [[catherine-braithwaite|Catherine Braithwaite]]")},
        {"label": two("Games", "Jeux"), "value": two("Red Dead Redemption 2", "Red Dead Redemption 2")},
        {"label": two("Voiced by", "Voix"), "value": two("Madison Arnold (according to the Red Dead Wiki)", "Madison Arnold (d'après le Red Dead Wiki)")},
    ],
    "intro": [
        two("Tavish Gray is the head of the Gray family, tobacco planters at Caliga Hall near Rhodes, in Red Dead Redemption 2 (2018), set in 1899. His family has long feuded with the Braithwaites of [[catherine-braithwaite|Catherine Braithwaite]]. In chapter 3 he asks [[arthur-morgan|Arthur Morgan]], [[john-marston|John Marston]] and [[javier-escuella|Javier Escuella]] to steal the Braithwaites' prized horses, which he says will fetch 5,000 dollars; the fence pays 700. Working for the other side, Arthur and [[sean-macguire|Sean MacGuire]] burn his tobacco fields. The Grays later lure the gang into an ambush in Rhodes, at which Tavish is not present. He is later found dead on a porch of Caliga Hall, beside a letter addressed to \"Mr. Gray\" which says that the family's ancestor, Ross Gray, was a paid informer for the Duke of Cumberland. The game does not show how he died.",
            "Tavish Gray est le chef de la famille Gray, planteurs de tabac à Caliga Hall, près de Rhodes, dans Red Dead Redemption 2 (2018), dont l'action se déroule en 1899. Sa famille mène une guerre ancienne contre les Braithwaite de [[catherine-braithwaite|Catherine Braithwaite]]. Au chapitre 3, il charge [[arthur-morgan|Arthur Morgan]], [[john-marston|John Marston]] et [[javier-escuella|Javier Escuella]] de voler les chevaux de prix des Braithwaite, qui vaudraient selon lui 5 000 dollars ; le receleur en donne 700. Pour le compte du camp adverse, Arthur et [[sean-macguire|Sean MacGuire]] incendient ses champs de tabac. Les Gray attirent ensuite la bande dans une embuscade à Rhodes, à laquelle Tavish n'assiste pas. Il est ensuite retrouvé mort sous un porche de Caliga Hall, à côté d'une lettre adressée à \"Mr. Gray\", selon laquelle l'ancêtre de la famille, Ross Gray, était un informateur payé par le duc de Cumberland. Le jeu ne montre pas les circonstances de sa mort."),
        two("According to the Red Dead Wiki, he is voiced by Madison Arnold.",
            "D'après le Red Dead Wiki, il a la voix de Madison Arnold."),
    ],
    "essentials": [
        two("He heads the Gray family of Caliga Hall, a tobacco plantation east of Rhodes; his relatives hold the sheriff's office and, according to Archibald MacGregor, own all the businesses in town.",
            "Il dirige la famille Gray de Caliga Hall, une plantation de tabac à l'est de Rhodes ; les siens tiennent le bureau du shérif et, selon Archibald MacGregor, possèdent tous les commerces de la ville."),
        two("In \"Horse Flesh for Dinner\", his only scene, he asks Arthur, John and Javier to steal Catherine Braithwaite's prized horses and says they will fetch 5,000 dollars; the fence Clay Davies pays 700.",
            "Dans \"Horse Flesh for Dinner\", sa seule scène, il charge Arthur, John et Javier de voler les chevaux de prix de Catherine Braithwaite, qui leur rapporteront selon lui 5 000 dollars ; le receleur Clay Davies en donne 700."),
        two("In \"The Fine Joys of Tobacco\", Arthur and Sean burn his tobacco fields for the Braithwaites; the Grays' ambush in Rhodes follows in \"A Short Walk in a Pretty Town\", without him.",
            "Dans \"The Fine Joys of Tobacco\", Arthur et Sean incendient ses champs de tabac pour les Braithwaite ; l'embuscade des Gray à Rhodes suit dans \"A Short Walk in a Pretty Town\", sans lui."),
        two("He is found dead on a porch at Caliga Hall, next to a historian's letter saying that the Gray ancestor, Ross Gray, was a paid informer for the Duke of Cumberland.",
            "Il est retrouvé mort sous un porche de Caliga Hall, à côté de la lettre d'un historien selon laquelle l'ancêtre des Gray, Ross Gray, était un informateur à la solde du duc de Cumberland."),
        two("His son Beau calls Sheriff Leigh Gray his uncle, while Dutch and Arthur call the sheriff Tavish's son.",
            "Son fils Beau appelle le shérif Leigh Gray son oncle, tandis que Dutch et Arthur font du shérif le fils de Tavish."),
    ],
    "rel_after": 1,
    "sections": [
        {"summary": two("Development and performance", "Conception et interprétation"), "blocks": BLOCKS_DEV},
    ],
    "relationships": [],
    "gallery": [],
    "related": ["catherine-braithwaite", "arthur-morgan", "john-marston", "javier-escuella"],
}
