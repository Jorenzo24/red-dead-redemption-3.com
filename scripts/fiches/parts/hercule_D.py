"""Hercule Fontaine, reference fiche, PART D: base data, Development and performance, Reception (22 Oct 2026, medium tier).

His live page (characters/hercule-fontaine/) was generated from the v2 entry in scripts/_wave7.py (order 47,
"slug": "hercule-fontaine"; no entry in _enrich.py). The base below is rebuilt from that entry. publishDate 2026-10-20
(live byline "Updated October 20, 2026") and the eyebrow ("Character &middot; Guarma") are kept as on the live page;
reg_role matches characters_registry.py ("Guarma rebel leader &middot; RDR2"). Changes against v2:
- v2 "nationality": "Haitian" and "Origin: Haitian", "Haitian rebel leader" in meta/schema/intro: the game never states
  his nationality. He says he is "not from here" and that his men will "disappear probably... back to Haiti" (transcript).
  Both Red Dead Wikis say Haitian. Now nationality None; the facts grid gives his line and attributes "Haitian" to the
  wiki; "Haitian" removed from meta, og, schema and intro.
- v2 "Hercule's men ambush the convoy" kept (mission page: "the leader of the ambush, Hercule Fontaine").
- v2 "free workers captured by Fussar's men": his request is to help Leon with a group of escaped workers whom Fussar's
  men are hunting (transcript). Corrected.
- v2 "Fussar has asked Cuba for help and a warship is on its way, so they cannot leave safely until Fussar is dealt with":
  now worded as the house fact: Fussar knows who they are and has called in the navy from Cuba; if he is silenced,
  Hercule can get them away before anyone arrives from America.
- v2 "Hercule loads the fort's cannon, and Arthur fires it": kept (Arthur helps push it into position; Hercule brings
  the shot). v2 "explains how Fussar runs the island through slave labour": Leon's words ("little more than slaves"),
  now attributed to Leon in part B.
- v2 "he and his men will be gone before anyone arrives": transcript says "long gone by morning", "back to Haiti".
- v2 "Behind the scenes" becomes Development and performance; Guyviaud Joseph now sourced to Wikipedia (credits).
- Chips "Guarma rebels / Leader / RDR2" replaced by Smuggler, Guarma rebels, Chapter 5 and the actor. Facts grid gains
  Name, Born, Status, Nationality (hedged), Occupation, Base, Allies, Enemies, Voiced by.

SOURCE REGISTER (fetched 22 Oct 2026, saved in scripts/v3/work/hercule/fc/):
- Wikipedia, "List of Red Dead Redemption 2 characters" (fc/wp_list_rdr2_hercule_line.txt; full copy in
  scripts/v3/work/catherine/fc/wp_list_rdr2.txt): "Guarman rebellion leader Hercule Fontaine (Guyviaud Joseph)", citing
  the game's credits (ref name "Credits"); the plot summary says Dutch "befriends revolutionary leader Hercule Fontaine".
- Red Dead Wiki EN "Hercule Fontaine" (infobox: voice Guyviaud Joseph) and FR "Hercule Fontaine" (acteur : Guyviaud
  Joseph). Red Dead Wiki "Baptiste" (voice Babs Olusanmokun) and "Leon Fuentes" (voice Andhy Méndez).
- Red Dead Wiki "Red Dead Redemption 2 Cut Content" (_m/Red_Dead_Redemption_2_Cut_Content.txt): "Hercule has an unused
  coat" (+ file HerculeCoat.PNG); mission-fail text for attacking Baptiste's and Hercule's horses although there are no
  horses on Guarma, and vehicle records for a horse-drawn wagon in "Paradise Mercifully Departed"; cut mission "smg1" /
  "Smuggler1" (Arthur and Bill rescue Leon's niece); cut Guarma character Senor Andreas Colon, whose trousers are nearly
  identical to Hercule's.
- WhatCulture, Dustin Crawford, "Red Dead Redemption 2: 10 Single Player Expansions We'd LOVE To See", June 16, 2020
  (fc/whatculture_2020-06-16.txt).
- Transcript (fc/gsw.txt, not committed) for the base facts.
Searched without result (22 Oct 2026): any interview in which Guyviaud Joseph discusses the role; any motion-capture
credit; any review or article about Hercule beyond the WhatCulture item, guides and wikis.

EXCLUDED: Guyviaud Joseph's biography (Haitian-American, born in Linden, New Jersey, John Wick: Chapter 2 credit) found
only on a scraped film-database mirror, not a reliable source; motion capture (no source); "Haitian" as a game fact;
the FR wiki's "formerly a slave" and "sent to Guarma as troublesome" (unsourced); any fate after Guarma; the Fussar
newspaper "Leader of Guarma Assassinated" (about Fussar; it does not name Hercule).
DUPLICATE ownership: actor, cut content and the WhatCulture item live HERE; part C Trivia must not repeat them.
"""


def two(en, fr): return {"en": en, "fr": fr}


BLOCKS_DEV = [
    {"h3": two("Casting", "Le casting")},
    {"p": two("Hercule Fontaine appears only in Red Dead Redemption 2 (2018), in chapter 5. He is voiced by Guyviaud Joseph: Wikipedia's list of the game's characters, which cites the game's credits, names him as the actor of the \"Guarman rebellion leader Hercule Fontaine\", and the Red Dead Wiki, in English and in French, gives the same credit. No interview in which Guyviaud Joseph discusses the role has been found, and no source names him for the character's motion capture. According to the Red Dead Wiki, the two other named rebels are voiced by Babs Olusanmokun (Baptiste) and Andhy Méndez (Leon Fuentes).",
              "Hercule Fontaine n'apparaît que dans Red Dead Redemption 2 (2018), au chapitre 5. Il a la voix de Guyviaud Joseph : la liste des personnages du jeu publiée par Wikipédia, qui s'appuie sur le générique, le crédite dans le rôle du \"Guarman rebellion leader Hercule Fontaine\" (le chef de la rébellion de Guarma), et le Red Dead Wiki, en anglais comme en français, lui attribue le même rôle. Aucun entretien où l'acteur évoquerait ce rôle n'a été trouvé, et aucune source ne lui attribue la capture de mouvement du personnage. D'après le Red Dead Wiki, les deux autres rebelles nommés ont la voix de Babs Olusanmokun (Baptiste) et d'Andhy Méndez (Leon Fuentes).")},
    {"h3": two("Cut content", "Contenu coupé")},
    {"p": two("The Red Dead Wiki's page on cut content lists an unused coat for Hercule. Although there are no horses on Guarma in the final game, the files contain mission-fail text for attacking Hercule's and Baptiste's horses, and vehicle records for a horse-drawn wagon in \"Paradise Mercifully Departed\". The same page describes a cut mission whose internal name is \"Smuggler1\", in which Arthur and Bill would have rescued the niece of the rebel Leon Fuentes and taken her off the island. A cut Guarma character, Senor Andreas Colon, wears trousers nearly identical to Hercule's.",
              "La page du Red Dead Wiki consacrée au contenu coupé signale un manteau inutilisé pour Hercule. Bien qu'il n'y ait aucun cheval à Guarma dans la version finale, les fichiers contiennent un message d'échec de mission en cas d'attaque des chevaux d'Hercule et de Baptiste, ainsi que des données de véhicule pour un chariot attelé dans \"Paradise Mercifully Departed\". La même page décrit une mission coupée, de nom interne \"Smuggler1\", dans laquelle Arthur et Bill auraient sauvé la nièce du rebelle Leon Fuentes avant de lui faire quitter l'île. Un personnage de Guarma supprimé, Senor Andreas Colon, porte un pantalon presque identique à celui d'Hercule.")},
]

BLOCKS_RECEPTION = [
    {"p": two("Hercule has drawn little press attention. In a WhatCulture list of single-player expansions published on June 16, 2020, Dustin Crawford called him \"an interesting character\" and described him as a \"Haitian-born freedom fighter leading a revolt\" against Colonel Fussar. He suggested an expansion set on Guarma after the fall of Fussar's regime, noting that the Cuban Navy's involvement left room for international conflict.",
              "Hercule a peu retenu l'attention de la presse. Dans une liste d'extensions solo publiée par WhatCulture le 16 juin 2020, Dustin Crawford le qualifie d'\"interesting character\" (personnage intéressant) et le décrit comme un \"Haitian-born freedom fighter leading a revolt\" (combattant de la liberté né en Haïti, à la tête d'une révolte) contre le colonel Fussar. Il imagine une extension consacrée à Guarma après la chute du régime de Fussar, en relevant que l'intervention de la marine cubaine ouvrirait la porte à un conflit international.")},
]


BASE = {
    "slug": "hercule-fontaine", "name": "Hercule Fontaine",
    "publishDate": "2026-10-20", "updated": "2026-10-22", "schema_game": "Red Dead Redemption 2",
    "reg_role_en": "Guarma rebel leader &middot; RDR2", "reg_role_fr": "Chef rebelle de Guarma &middot; RDR2",
    "gender": "Male", "death": None, "nationality": None,
    "portrait_alt": two("Hercule Fontaine in the jungle of Guarma in Red Dead Redemption 2",
                        "Hercule Fontaine dans la jungle de Guarma dans Red Dead Redemption 2"),
    "eyebrow": two("Character &middot; Guarma", "Personnage &middot; Guarma"),
    "meta_desc": two("Hercule Fontaine, the smuggler and rebel leader of Guarma in RDR2: the ambush, his deal with Dutch, the battle of Cinco Torres, the death of Alberto Fussar, Guyviaud Joseph.",
                     "Hercule Fontaine, contrebandier et chef rebelle de Guarma dans RDR2 : l'embuscade, son marché avec Dutch, la bataille de Cinco Torres, la mort d'Alberto Fussar, Guyviaud Joseph."),
    "og_desc": two("The complete reference on Hercule Fontaine: life, deal with the gang, quotes, development and reception.",
                   "La référence complète sur Hercule Fontaine : vie, marché avec la bande, citations, conception et accueil."),
    "schema_desc": two("Smuggler and rebel leader on the Caribbean island of Guarma who frees the shipwrecked members of the Van der Linde gang, fights Alberto Fussar with them and finds them a ship back to America in 1899, in Red Dead Redemption 2.",
                       "Contrebandier et chef rebelle sur l'île caribéenne de Guarma, qui libère les membres naufragés du gang Van der Linde, combat Alberto Fussar à leurs côtés et leur trouve un navire pour rentrer en Amérique en 1899, dans Red Dead Redemption 2."),
    "chips": [two("Smuggler", "Contrebandier"), two("Guarma rebels", "Rebelles de Guarma"),
              two("Chapter <strong>5</strong>", "Chapitre <strong>5</strong>"),
              two("Voiced by <strong>Guyviaud Joseph</strong>", "Voix : <strong>Guyviaud Joseph</strong>")],
    "facts": [
        {"label": two("Name", "Nom"), "value": two("Hercule Fontaine", "Hercule Fontaine")},
        {"label": two("Born", "Naissance"), "value": two("Not given in the game", "Non précisée dans le jeu")},
        {"label": two("Status", "Statut"), "value": two("Alive when the gang leaves Guarma (1899); his fate afterwards is not shown", "En vie quand la bande quitte Guarma (1899) ; la suite n'est pas montrée")},
        {"label": two("Nationality", "Nationalité"), "value": two("Not stated in the game; he says he is not from Guarma and that his men will probably go back to Haiti. Haitian according to the Red Dead Wiki", "Non précisée dans le jeu ; il dit ne pas être de Guarma et que ses hommes rentreront sans doute en Haïti. Haïtienne selon le Red Dead Wiki")},
        {"label": two("Occupation", "Activité"), "value": two("Smuggler; leader of a band of rebels against Fussar", "Contrebandier ; chef d'une bande de rebelles opposée à Fussar")},
        {"label": two("Base", "Base"), "value": two("The old fort of Cinco Torres, Guarma", "Le vieux fort de Cinco Torres, à Guarma")},
        {"label": two("Allies", "Alliés"), "value": two("Leon Fuentes, Baptiste; [[dutch-van-der-linde|Dutch]], [[arthur-morgan|Arthur]], [[micah-bell|Micah]] and [[bill-williamson|Bill]] (on Guarma)", "Leon Fuentes, Baptiste ; [[dutch-van-der-linde|Dutch]], [[arthur-morgan|Arthur]], [[micah-bell|Micah]] et [[bill-williamson|Bill]] (à Guarma)")},
        {"label": two("Enemies", "Ennemis"), "value": two("[[alberto-fussar|Alberto Fussar]], his overseer Levi Simon and their soldiers", "[[alberto-fussar|Alberto Fussar]], son contremaître Levi Simon et leurs soldats")},
        {"label": two("Games", "Jeux"), "value": two("Red Dead Redemption 2", "Red Dead Redemption 2")},
        {"label": two("Voiced by", "Voix"), "value": two("Guyviaud Joseph", "Guyviaud Joseph")},
    ],
    "intro": [
        two("Hercule Fontaine is a smuggler who leads a band of rebels against [[alberto-fussar|Alberto Fussar]], the colonel who governs the Caribbean island of Guarma, in Red Dead Redemption 2 (2018), set in 1899. In chapter 5 his ambush frees [[dutch-van-der-linde|Dutch van der Linde]], [[arthur-morgan|Arthur Morgan]], [[micah-bell|Micah Bell]] and [[bill-williamson|Bill Williamson]], shipwrecked on the island and marched in chains by Fussar's soldiers; [[javier-escuella|Javier Escuella]] is captured during the escape. Hercule promises them a boat in return for their help. Fussar calls in a warship from Cuba, which Arthur sinks with Hercule's cannon at the fort of Cinco Torres. Hercule then joins the attack on Aguasdulces, where Arthur kills Fussar, and the gang sails away on the ship he found for them. The game does not show what becomes of him.",
            "Hercule Fontaine est un contrebandier à la tête d'une bande de rebelles qui combat [[alberto-fussar|Alberto Fussar]], le colonel qui gouverne l'île caribéenne de Guarma, dans Red Dead Redemption 2 (2018), dont l'action se déroule en 1899. Au chapitre 5, son embuscade libère [[dutch-van-der-linde|Dutch van der Linde]], [[arthur-morgan|Arthur Morgan]], [[micah-bell|Micah Bell]] et [[bill-williamson|Bill Williamson]], naufragés sur l'île et emmenés enchaînés par les soldats de Fussar ; [[javier-escuella|Javier Escuella]] est capturé pendant la fuite. Hercule leur promet un bateau en échange de leur aide. Fussar fait venir un navire de guerre de Cuba, qu'Arthur coule avec le canon d'Hercule au fort de Cinco Torres. Hercule participe ensuite à l'attaque d'Aguasdulces, où Arthur tue Fussar, et la bande prend la mer sur le navire qu'il lui a trouvé. Le jeu ne montre pas ce qu'il devient."),
        two("He is voiced by Guyviaud Joseph.",
            "Il a la voix de Guyviaud Joseph."),
    ],
    "essentials": [
        two("A smuggler who moves goods on and off the islands behind Fussar's back and uses the old fort of Cinco Torres as a hideout with his men.",
            "Contrebandier, il fait entrer et sortir des marchandises des îles dans le dos de Fussar et se sert du vieux fort de Cinco Torres comme repaire avec ses hommes."),
        two("In \"Welcome to the New World\", his ambush frees the chained castaways; he promises them a boat if they help Leon Fuentes with a group of escaped workers.",
            "Dans \"Welcome to the New World\", son embuscade libère les naufragés enchaînés ; il leur promet un bateau s'ils aident Leon Fuentes à retrouver un groupe d'ouvriers en fuite."),
        two("In \"Hell Hath No Fury\", he tells Dutch that if Fussar is silenced, he can get them away before anyone arrives from America; Arthur then sinks Fussar's warship with Hercule's cannon.",
            "Dans \"Hell Hath No Fury\", il explique à Dutch que si l'on fait taire Fussar, il pourra les faire partir avant que quiconque n'arrive d'Amérique ; Arthur coule ensuite le navire de guerre de Fussar avec le canon d'Hercule."),
        two("In \"Paradise Mercifully Departed\", he leads the attack on Fussar's gun positions and spots Fussar in the tower that Arthur brings down with a second cannon.",
            "Dans \"Paradise Mercifully Departed\", il guide l'attaque des batteries de Fussar et repère Fussar dans la tour qu'Arthur abat avec un second canon."),
        two("His last line to the gang: the rebels will probably disappear back to Haiti and be gone by morning. His fate after Guarma is not shown.",
            "Sa dernière réplique à la bande : les rebelles vont sans doute disparaître, rentrer en Haïti, et seront partis au matin. Son sort après Guarma n'est pas montré."),
    ],
    "rel_after": 1,
    "sections": [
        {"summary": two("Development and performance", "Conception et interprétation"), "blocks": BLOCKS_DEV},
        {"summary": two("Reception", "Accueil"), "blocks": BLOCKS_RECEPTION},
    ],
    "relationships": [],
    "gallery": [],
    "related": ["alberto-fussar", "dutch-van-der-linde", "micah-bell", "bill-williamson"],
}
