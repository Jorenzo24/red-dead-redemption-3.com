"""Hercule Fontaine, part B: Personality (no official description, In his own words, Names, Appearance), Smuggling
and fighting (skills equivalent), Relationships (22 Oct 2026, medium tier).

Coverage: the Red Dead Wiki page "Hercule Fontaine" (en.txt) has no Personality, Appearance or Relationships section;
its infobox (affiliations: Guarma Rebels, Baptiste, Leon Fuentes, Dutch, Arthur, Bill, Micah "temporarily"; weapons:
Bolt Action Rifle, Carcano Rifle, Springfield Rifle, Rolling Block Rifle; occupation: Revolutionary, Smuggler;
nationality: Haitian) is covered here (Skills, Relationships) and in part D (facts grid). Everything he says comes from
"Welcome to the New World", "Hell Hath No Fury" and "Paradise Mercifully Departed".

SOURCE REGISTER (read 22 Oct 2026):
- Full game transcript, "Red Dead Redemption 2 Full Transcript", Game Scripts Wiki (blogspot), fan transcript
  (scripts/v3/work/hercule/fc/gsw.txt, not committed), lines 10480-11010: "Welcome to the New World" (labelled
  "Stranger 2" until "Aren't we all. Hercule Fontaine."; "I am not from here. I bring things in and off the islands...
  behind Colonel Fussar's back."; "my men and I use that as a hideout when we are here"; "I have some guns stashed
  here"; "It's not my island."; "I don't see you have any choice. I am the only one who can arrange a boat for you.
  But... I need something in return."; the cave below the cliffs), "Savagery Unleashed" (Leon: "One of Hercule's
  men"; Baptiste: "I work with Hercule", "Hercule is getting a boat lined up"), "A Kind and Benevolent Despot" (Dutch
  "found the cave Hercule spoke of"; Arthur: "Are you sure this Hercule feller ain't just using us?"; Dutch: "Almost
  certainly"), "Hell Hath No Fury" (Micah: "He's using us!"; Bill/Hercule exchange; "Grab the shotgun, Arthur.";
  "Guess I'm following you, Arthur!"; "It doesn't matter how many we kill. He will have the money to get more.";
  French lines; "I found a boat for you"; Dutch: "it was a great pleasure to make your acquaintance"), "Paradise
  Mercifully Departed" ("Oh, I'll fight Alberto Fussar every day I can."; "En allez."; "connards"; the tower;
  "We'll be like you. We'll disappear probably... back to Haiti. Believe me, we'll be long gone by morning.").
- Red Dead Wiki EN mission pages (scripts/v3/work/_m/): "Welcome to the New World" (mission fails if Hercule or Leon
  is assaulted or killed; deaths list), "Hell Hath No Fury" (giver: Hercule; Arthur helps him push the cannon into
  position; trivia: Hercule runs very fast back to the roof), "Paradise Mercifully Departed".
- Red Dead Wiki EN "Baptiste" (Hercule's associate, $450 to Arthur), "Leon Fuentes", "Guarma Rebels", "Cinco Torres".
- Rockstar's character descriptions of 6 Sep 2018 (scripts/v3/sources/thr_descriptions.txt): gang only, none for him.
  No official-guide description of him was found.
- Live portrait (assets/characters/hercule-fontaine/portrait.jpeg) for Appearance.
- Authoritative fiches checked for consistency: fussar_A..D (cannon, offer, "Red Dead Wiki only" diversion, nationality
  wording), arthur_C/D, dutch_B, micah, bill, javier parts.

OWNERSHIP: lines quoted in "In his own words" must NOT be repeated in part C Quotes: "I am not from here...";
"I don't see you have any choice...", "It doesn't matter how many we kill...", "Oh, I'll fight Alberto Fussar every day
I can.", "We'll be like you... long gone by morning." Quoted in Relationships (not for C): Bill's "You said you were
getting us a goddamn boat, Hercule!" and Hercule's "I am! What do you want me to do? We are trapped up here!";
Micah's "Why the hell are we doing this? This ain't our fight!" / "Do you want to get off this island or not?" /
"He's using us!"; Arthur's "Nice island you got here." / "It's not my island."; Arthur's "this Hercule feller" line
and Dutch's "Almost certainly"; Dutch's "it was a great pleasure to make your acquaintance"; Baptiste's "I work with
Hercule". Left to C: "Okay. Well, Fussar will be desperate to find you...", "Leon wants the people to stand up...",
"But, if we can silence him...", "You man the cannon... Aim at the waterline...", "Fussar is up there I think" exchange,
"I found a boat for you...", "Gentlemen, goodbye.", "So now we have a real problem...", "We fight or we run.".
Narrative events (ambush, El Nido, deal, Cinco Torres battle, batteries, standoff, tower) belong to part A; entries
point to them. Cut content (unused coat, horse fail text) lives in part D.

FIXER (22 Oct 2026): Personality reduced to the no-description sentence + pointer (FIX_RULES 11); Names no longer quotes
"this Hercule feller" (quoted in Relationships, Arthur) and no longer carries Leon's "One of Hercule's men" (paraphrased in
A Origins); Smuggling and Fighting reduced to what A does not tell; Languages per FIX_RULES 12; Relationships trimmed to
pointers; Leon's rank told once in A; the captain's engagement (Captain C. page) lives here, not in A. The mission-fail and
fast-run items live here, not in C Trivia.

WIKI-ONLY (kept, attributed): his four rifles (infobox); Baptiste's $450 (Baptiste page; the transcript only shows a
gift); Leon as a member of a rebel faction led by Hercule (Leon page); the fast run back to the roof (mission trivia).

EXCLUDED: "Haitian" as a stated nationality (the game never says it: only his "back to Haiti" line and Levi Simon's
"Haitian pirates", whose target the game does not name; both wikis say Haitian, attributed in part D); the FR wiki's
"Esclave (anciennement)" and "sent to Guarma as troublesome by the Cuban officials" (unsourced, and at odds with his own
"I am not from here. I bring things in and off the islands"); "Hercule draws Fussar's fire" (Red Dead Wiki only:
told once, attributed, in part A); the transcript stage note "[They pull up a machine gun.]" in "Hell Hath No Fury" (the
mission page and the dialogue are about the cannon); any fate after Guarma; the "Haitian rebel" label of the live fiche.
"""


def two(en, fr): return {"en": en, "fr": fr}

# ---------------------------------------------------------------- PERSONALITY
BLOCKS_PERSONALITY = [
    {"h3": two("Personality", "Personnalité")},
    {"p": two(
        "Rockstar's character descriptions of September 2018 cover the Van der Linde gang and do not include him, and no official guide description of him was found. What is known of his character comes from what he says and does in his three missions: his actions are told in the Biography, and the lines below give his own account of his trade, his fight with Fussar and his plans.",
        "Les descriptions de personnages publiées par Rockstar en septembre 2018 portent sur le gang Van der Linde et ne le concernent pas, et aucun guide officiel consulté ne le décrit. Son caractère ne se lit donc que dans ce qu'il dit et fait au fil de ses trois missions : ses actes sont racontés dans la biographie, et les répliques citées ci-dessous portent sur son métier, sa lutte contre Fussar et ses projets.")},
    {"h4": two("In his own words", "Dans ses propres mots")},
    {"ul": [
        two("\"I am not from here. I bring things in and off the islands... behind Colonel Fussar's back.\" (to Dutch, \"Welcome to the New World\")",
            "\"I am not from here. I bring things in and off the islands... behind Colonel Fussar's back.\" (je ne suis pas d'ici ; je fais entrer et sortir des marchandises des îles… dans le dos du colonel Fussar), à Dutch, dans \"Welcome to the New World\"."),
        two("\"I don't see you have any choice. I am the only one who can arrange a boat for you. But... I need something in return.\" (when Dutch asks if he can be trusted)",
            "\"I don't see you have any choice. I am the only one who can arrange a boat for you. But... I need something in return.\" (je ne vois pas bien quel choix vous avez ; je suis le seul à pouvoir vous trouver un bateau, mais… j'attends quelque chose en retour), quand Dutch lui demande s'il peut lui faire confiance."),
        two("\"That is the problem. It doesn't matter how many we kill. He will have the money to get more.\" (to Arthur, who asks how many men Fussar has, \"Hell Hath No Fury\")",
            "\"That is the problem. It doesn't matter how many we kill. He will have the money to get more.\" (c'est bien le problème : peu importe combien on en tue, il aura l'argent pour en payer d'autres), à Arthur, qui demande combien d'hommes a Fussar, dans \"Hell Hath No Fury\"."),
        two("\"Oh, I'll fight Alberto Fussar every day I can.\" (when Dutch turns to him after Micah's report, \"Paradise Mercifully Departed\")",
            "\"Oh, I'll fight Alberto Fussar every day I can.\" (oh, je combattrai Alberto Fussar tant que je le pourrai), quand Dutch se tourne vers lui après le rapport de Micah, dans \"Paradise Mercifully Departed\"."),
        two("\"We'll be like you. We'll disappear probably... back to Haiti. Believe me, we'll be long gone by morning.\" (when Dutch asks if he will be all right, at the harbor)",
            "\"We'll be like you. We'll disappear probably... back to Haiti. Believe me, we'll be long gone by morning.\" (on fera comme vous : on va disparaître, sans doute… retourner en Haïti ; croyez-moi, demain matin on sera loin), quand Dutch lui demande s'il va s'en sortir, sur le port."),
    ]},
    {"h4": two("Names", "Noms")},
    {"p": two(
        "He introduces himself as Hercule Fontaine to Dutch after the escape. The gang and the rebels call him Hercule. In \"A Kind and Benevolent Despot\", Arthur refers to him only by his first name when he asks Dutch whether Hercule is using them (see Relationships). The Red Dead Wiki lists no alias for him.",
        "Il se présente à Dutch sous le nom d'Hercule Fontaine après l'évasion. La bande comme les rebelles l'appellent Hercule. Dans \"A Kind and Benevolent Despot\", Arthur ne le désigne que par son prénom quand il demande à Dutch si Hercule se sert d'eux (voir Relations). Le Red Dead Wiki ne lui connaît aucun surnom.")},
    {"h4": two("Appearance", "Apparence")},
    {"p": two(
        "He is a Black man with short, thick curly hair and a full black beard, and a small scar on his left cheek. Around his neck he wears a string of colored beads and thin cords, one of them with a pendant.",
        "C'est un homme noir aux cheveux courts, épais et frisés, à la barbe noire fournie, avec une petite cicatrice sur la joue gauche. Il porte au cou un collier de perles de couleur et de fins cordons, dont l'un retient un pendentif.")},
]

# ---------------------------------------------------------------- SMUGGLING AND FIGHTING (skills equivalent)
# Suggested section title: "Smuggling and fighting" / "Contrebande et combat".
BLOCKS_SKILLS = [
    {"h4": two("Smuggling", "Contrebande")},
    {"p": two(
        "The Red Dead Wiki lists his occupations as revolutionary and smuggler. On Guarma he is the gang's only means of getting a boat off the island. His trade, his gun cache, his hideout at Cinco Torres and the cave he points out to Dutch are covered in the Biography.",
        "Le Red Dead Wiki le classe parmi les révolutionnaires et les contrebandiers. À Guarma, il est le seul à pouvoir procurer un bateau à la bande pour quitter l'île. Son trafic, sa cache d'armes, son repaire de Cinco Torres et la grotte qu'il indique à Dutch sont racontés dans la biographie.")},
    {"h4": two("Fighting", "Combat")},
    {"p": two(
        "The Red Dead Wiki credits him with four rifles: a Bolt Action Rifle, a Carcano Rifle, a Springfield Rifle and a Rolling Block Rifle. He fights beside the gang in all three of his missions; the mission pages list him among those who kill soldiers in \"Welcome to the New World\", \"Hell Hath No Fury\" and \"Paradise Mercifully Departed\" (see Biography, and the Missions table). In \"Welcome to the New World\", the mission fails if the player attacks or kills Hercule or Leon. According to the Red Dead Wiki, Hercule is hard to keep up with on the climb back to the roof of Cinco Torres in \"Hell Hath No Fury\", because his route twists and drops through the undergrowth; the wiki suggests tracking him on the mini-map.",
        "Le Red Dead Wiki lui attribue quatre fusils : un Bolt Action Rifle, un Carcano Rifle, un Springfield Rifle et un Rolling Block Rifle. Il se bat aux côtés de la bande dans ses trois missions ; les pages de missions le comptent parmi ceux qui abattent des soldats dans \"Welcome to the New World\", \"Hell Hath No Fury\" et \"Paradise Mercifully Departed\" (voir la biographie et le tableau des missions). Dans \"Welcome to the New World\", la mission échoue si le joueur attaque ou tue Hercule ou Leon. D'après le Red Dead Wiki, Hercule est difficile à suivre quand il remonte vers le toit de Cinco Torres dans \"Hell Hath No Fury\" : son itinéraire serpente et dégringole à travers les broussailles, et le wiki recommande de garder un œil sur la mini-carte.")},
    {"h4": two("Languages", "Langues")},
    {"p": two(
        "He speaks English with the gang. In the transcript, a rebel calls to him in French when the warship appears; Hercule's own French lines are exclamations during the fighting. He swears in French at Cinco Torres, and he sets off toward the gun positions with \"En allez\". On the run to the harbor in \"Paradise Mercifully Departed\", he calls the soldiers \"connards\".",
        "Il parle anglais avec la bande. D'après la transcription, un rebelle l'appelle en français quand le navire de guerre apparaît ; Hercule, lui, ne passe au français que pour des exclamations en plein combat. Il jure en français à Cinco Torres, et il lance \"En allez\" au moment de partir vers les batteries. Pendant la course vers le port, dans \"Paradise Mercifully Departed\", il traite les soldats de \"connards\".")},
]

# ---------------------------------------------------------------- RELATIONSHIPS
RELATIONSHIPS = [
    {"img": "dutch-van-der-linde.jpeg", "slug": "dutch-van-der-linde", "name": "Dutch van der Linde", "text": [
        two("Dutch makes the deal with him after the escape (see Biography). Later, he tells Arthur that Hercule is \"Almost certainly\" using them, but that he is their best chance of leaving the island.",
            "Dutch conclut le marché avec lui après l'évasion (voir la biographie). Plus tard, il confie à Arthur qu'Hercule se sert d'eux, \"Almost certainly\" (très certainement), mais qu'il reste leur meilleure chance de quitter l'île."),
        two("At Cinco Torres, Dutch reminds Hercule that the gang has done what he asked and argues with him over the promised boat (see Biography). After the warship sinks, he tells him: \"Hercule... it was a great pleasure to make your acquaintance.\" Before the attack on the gun positions he lets Hercule lead (\"Hercule, we follow you.\"), and at the harbor he asks whether Hercule will be all right, then thanks him.",
            "À Cinco Torres, Dutch rappelle à Hercule que la bande a fait ce qu'il demandait et lui réclame le bateau promis (voir la biographie). Une fois le navire de guerre coulé, il lui lance : \"Hercule... it was a great pleasure to make your acquaintance.\" (Hercule… ce fut un grand plaisir de faire votre connaissance). Avant l'attaque des batteries, il lui laisse la tête du groupe (\"Hercule, we follow you.\", Hercule, on vous suit), et sur le port il lui demande s'il va s'en sortir, puis le remercie."),
    ]},
    {"img": "arthur-morgan.jpeg", "slug": "arthur-morgan", "name": "Arthur Morgan", "text": [
        two("At the old building where they fight off the soldiers, Arthur thanks Hercule for getting them out and remarks: \"Nice island you got here.\" Hercule replies: \"It's not my island.\" In \"A Kind and Benevolent Despot\", Arthur asks Dutch: \"Are you sure this Hercule feller ain't just using us?\"",
            "Dans le vieux bâtiment où ils repoussent les soldats, Arthur remercie Hercule de les avoir tirés de là et lâche : \"Nice island you got here.\" (jolie île que vous avez là). Hercule répond : \"It's not my island.\" (ce n'est pas mon île). Dans \"A Kind and Benevolent Despot\", Arthur demande à Dutch : \"Are you sure this Hercule feller ain't just using us?\" (t'es sûr que ce type, Hercule, se sert pas juste de nous ?)."),
        two("At Cinco Torres the two men fight side by side (see Biography). On the beach, when Arthur sends Dutch to cover the left, Hercule says he will follow Arthur. At the harbor, Hercule points Arthur to a second cannon to bring down Fussar's tower.",
            "À Cinco Torres, les deux hommes se battent côte à côte (voir la biographie). Sur la plage, quand Arthur envoie Dutch couvrir le flanc gauche, Hercule annonce qu'il le suit. Sur le port, Hercule indique à Arthur un second canon pour abattre la tour de Fussar."),
    ]},
    {"img": "micah-bell.jpeg", "slug": "micah-bell", "name": "Micah Bell", "text": two(
        "During the battle at Cinco Torres, Micah asks: \"Why the hell are we doing this? This ain't our fight!\" Hercule answers: \"Do you want to get off this island or not?\", and Micah shouts: \"He's using us!\" Micah later guards the cannon with Bill, and joins Hercule, Dutch and Arthur in the raid on the gun positions, where he rigs the dynamite (see Biography).",
        "Pendant la bataille de Cinco Torres, Micah s'emporte : \"Why the hell are we doing this? This ain't our fight!\" (qu'est-ce qu'on fout là ? c'est pas notre combat !). Hercule réplique : \"Do you want to get off this island or not?\" (vous voulez quitter cette île, oui ou non ?), et Micah crie : \"He's using us!\" (il se sert de nous !). Micah garde ensuite le canon avec Bill, puis accompagne Hercule, Dutch et Arthur à l'assaut des batteries, qu'il piège à la dynamite (voir la biographie).")},
    {"img": "bill-williamson.jpeg", "slug": "bill-williamson", "name": "Bill Williamson", "text": two(
        "When the soldiers close in on the fort, Bill shouts: \"You said you were getting us a goddamn boat, Hercule!\" Hercule answers: \"I am! What do you want me to do? We are trapped up here!\" Bill stays on the roof to guard the cannon, then on the ship to guard Javier while the others attack the gun positions (see Biography).",
        "Quand les soldats se rapprochent du fort, Bill hurle : \"You said you were getting us a goddamn boat, Hercule!\" (vous deviez nous trouver un foutu bateau, Hercule !). Hercule rétorque : \"I am! What do you want me to do? We are trapped up here!\" (c'est ce que je fais ! qu'est-ce que vous voulez que j'y fasse ? on est coincés là-haut !). Bill reste sur le toit pour garder le canon, puis sur le navire pour veiller sur Javier pendant que les autres attaquent les batteries (voir la biographie).")},
    {"img": "javier-escuella.jpeg", "slug": "javier-escuella", "name": "Javier Escuella", "text": two(
        "Javier is shot in the leg and captured as the group, led by Hercule, flees the soldiers' reinforcements after the ambush. Hercule tells Dutch where Javier will be held and how to reach him (see Biography). Javier leaves Guarma on the same ship as the others.",
        "Javier est touché à la jambe et capturé alors que le groupe, guidé par Hercule, fuit les renforts arrivés après l'embuscade. Hercule indique à Dutch où Javier sera détenu et comment l'atteindre (voir la biographie). Javier quitte Guarma sur le même navire que les autres.")},
    {"img": "alberto-fussar.jpeg", "slug": "alberto-fussar", "name": "Alberto Fussar", "text": two(
        "The colonel who governs Guarma, and the man Hercule's rebels fight. Hercule calls him Colonel Fussar and Aguasdulces \"Fussar's compound\". Arthur kills Fussar with a cannon shot at the tower Hercule points out (see Biography). The two men never speak to each other on screen.",
        "Le colonel qui gouverne Guarma, et que combattent les rebelles d'Hercule. Celui-ci l'appelle le colonel Fussar et désigne Aguasdulces comme \"Fussar's compound\" (le domaine de Fussar). Arthur tue Fussar d'un coup de canon sur la tour qu'Hercule lui a désignée (voir la biographie). Les deux hommes ne s'adressent jamais la parole à l'écran.")},
    {"img": None, "slug": None, "name": "Leon Fuentes", "text": two(
        "A rebel chained with the castaways and freed in the ambush. Hercule asks the gang to help Leon with a group of escaped workers, and Arthur later fights beside Leon in \"Savagery Unleashed\" (see Biography). His rank among the rebels is discussed under Origins.",
        "Rebelle enchaîné avec les naufragés et libéré lors de l'embuscade. Hercule demande à la bande d'aider Leon à retrouver un groupe d'ouvriers en fuite, et Arthur se bat ensuite à ses côtés dans \"Savagery Unleashed\" (voir la biographie). Sa place parmi les rebelles est abordée dans les Origines.")},
    {"img": None, "slug": None, "name": "Baptiste", "text": two(
        "A one-armed rebel whom Arthur frees in \"Savagery Unleashed\". He introduces himself to Arthur with \"I work with Hercule\", passes on Hercule's message about the boat (see Biography) and gives him money. The Red Dead Wiki puts the sum at 450 dollars and describes Baptiste as a smuggler working with Hercule.",
        "Rebelle manchot qu'Arthur libère dans \"Savagery Unleashed\". Il se présente à Arthur par un \"I work with Hercule\" (je travaille avec Hercule), lui transmet le message d'Hercule au sujet du bateau (voir la biographie) et lui remet de l'argent. Le Red Dead Wiki chiffre la somme à 450 dollars et fait de Baptiste un contrebandier associé à Hercule.")},
    {"img": None, "slug": None, "name": "The ship's captain", "text": two(
        "The captain whose ship Hercule finds for the gang. According to the Red Dead Wiki, Hercule engaged him to take the five gang members off the island in return for their help with the workers. Fussar's men hold him until the gang frees him (see Biography).",
        "Le capitaine du navire qu'Hercule trouve pour la bande. Selon le Red Dead Wiki, c'est Hercule qui l'a engagé pour faire quitter l'île aux cinq membres de la bande, en échange de leur aide auprès des ouvriers. Les hommes de Fussar le retiennent jusqu'à ce que la bande le libère (voir la biographie).")},
    {"img": None, "slug": None, "name": "Levi Simon", "text": two(
        "Fussar's senior overseer, whose patrol chains the castaways on the beach. Before the ambush, he tells Dutch that a \"Bunch of Haitian pirates\" will not frighten Fussar and will soon be hanged in the streets; the game does not say whom he means. He is killed in the cabin standoff (see Biography). He and Hercule never share a scene.",
        "Le contremaître principal de Fussar, dont la patrouille enchaîne les naufragés sur la plage. Avant l'embuscade, il affirme à Dutch qu'une \"Bunch of Haitian pirates\" (bande de pirates haïtiens) ne fera pas peur à Fussar et finira bientôt pendue dans les rues ; le jeu ne précise pas qui il vise. Il meurt lors du face-à-face dans la cabane (voir la biographie). Hercule et lui n'apparaissent jamais ensemble.")},
]
