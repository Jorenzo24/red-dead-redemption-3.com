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
        "Rockstar's character descriptions of September 2018 cover the Van der Linde gang and do not include him, and no official guide description of him was found. What is known of his character comes from his three missions. He asks the castaways what they are doing on the island before he gives his own name. He says plainly that he is not from Guarma and that he works behind Fussar's back. He sets the terms of his help at once: a boat for the gang, in return for help with Leon's escaped workers (see Biography).",
        "Les descriptions de personnages publiées par Rockstar en septembre 2018 portent sur le gang Van der Linde et ne le concernent pas, et aucun guide officiel consulté ne le décrit. Son caractère se lit donc dans ses trois missions. Il demande aux naufragés ce qu'ils font sur l'île avant de donner son propre nom. Il dit sans détour qu'il n'est pas de Guarma et qu'il travaille dans le dos de Fussar. Il pose aussitôt ses conditions : un bateau pour la bande, en échange d'un coup de main auprès des ouvriers en fuite de Leon (voir la biographie).")},
    {"p": two(
        "Under fire at Cinco Torres he answers Bill's and Micah's complaints sharply, then follows Arthur's lead in the fighting on the beach. He knows that killing soldiers will not end Fussar's hold on the island. Once Fussar is dead, he does not claim the island for the rebels: he says they will disappear, like the gang, before morning.",
        "Sous le feu, à Cinco Torres, il répond sèchement aux reproches de Bill et de Micah, puis se range derrière Arthur pendant les combats sur la plage. Il sait que tuer des soldats ne suffira pas à briser l'emprise de Fussar sur l'île. Une fois Fussar mort, il ne revendique pas l'île pour les rebelles : il annonce qu'ils vont disparaître, comme la bande, avant le lendemain matin.")},
    {"h4": two("In his own words", "Dans ses propres mots")},
    {"ul": [
        two("\"I am not from here. I bring things in and off the islands... behind Colonel Fussar's back.\" (to Dutch, \"Welcome to the New World\")",
            "\"I am not from here. I bring things in and off the islands... behind Colonel Fussar's back.\" (je ne suis pas d'ici ; je fais entrer et sortir des marchandises des îles… dans le dos du colonel Fussar), à Dutch, dans \"Welcome to the New World\"."),
        two("\"I don't see you have any choice. I am the only one who can arrange a boat for you. But... I need something in return.\" (when Dutch asks if he can be trusted)",
            "\"I don't see you have any choice. I am the only one who can arrange a boat for you. But... I need something in return.\" (je ne vois pas bien quel choix vous avez ; je suis le seul à pouvoir vous trouver un bateau, mais… j'attends quelque chose en retour), quand Dutch lui demande s'il peut lui faire confiance."),
        two("\"That is the problem. It doesn't matter how many we kill. He will have the money to get more.\" (to Arthur, who asks how many men Fussar has, \"Hell Hath No Fury\")",
            "\"That is the problem. It doesn't matter how many we kill. He will have the money to get more.\" (c'est bien le problème : peu importe combien on en tue, il aura l'argent pour en payer d'autres), à Arthur, qui demande combien d'hommes a Fussar, dans \"Hell Hath No Fury\"."),
        two("\"Oh, I'll fight Alberto Fussar every day I can.\" (when Dutch asks if he is in, \"Paradise Mercifully Departed\")",
            "\"Oh, I'll fight Alberto Fussar every day I can.\" (oh, je combattrai Alberto Fussar tant que je le pourrai), quand Dutch lui demande s'il en est, dans \"Paradise Mercifully Departed\"."),
        two("\"We'll be like you. We'll disappear probably... back to Haiti. Believe me, we'll be long gone by morning.\" (when Dutch asks if he will be all right, at the harbor)",
            "\"We'll be like you. We'll disappear probably... back to Haiti. Believe me, we'll be long gone by morning.\" (on fera comme vous : on va disparaître, sans doute… retourner en Haïti ; croyez-moi, demain matin on sera loin), quand Dutch lui demande s'il va s'en sortir, sur le port."),
    ]},
    {"h4": two("Names", "Noms")},
    {"p": two(
        "He introduces himself as Hercule Fontaine to Dutch after the escape. The gang and the rebels call him Hercule. In \"A Kind and Benevolent Despot\", Arthur refers to him as \"this Hercule feller\" (see Relationships). Leon Fuentes describes Baptiste as \"One of Hercule's men\". The Red Dead Wiki lists no alias for him.",
        "Il se présente à Dutch sous le nom d'Hercule Fontaine après l'évasion. La bande comme les rebelles l'appellent Hercule. Dans \"A Kind and Benevolent Despot\", Arthur parle de lui comme de \"this Hercule feller\" (ce type, Hercule) (voir Relations). Leon Fuentes présente Baptiste comme \"One of Hercule's men\" (un des hommes d'Hercule). Le Red Dead Wiki ne lui connaît aucun surnom.")},
    {"h4": two("Appearance", "Apparence")},
    {"p": two(
        "He is a Black man with short, thick curly hair and a full black beard, and a small scar on his left cheek. He wears several strings of colored beads around his neck.",
        "C'est un homme noir aux cheveux courts, épais et frisés, à la barbe noire fournie, avec une petite cicatrice sur la joue gauche. Il porte plusieurs colliers de perles de couleur.")},
]

# ---------------------------------------------------------------- SMUGGLING AND FIGHTING (skills equivalent)
# Suggested section title: "Smuggling and fighting" / "Contrebande et combat".
BLOCKS_SKILLS = [
    {"h4": two("Smuggling", "Contrebande")},
    {"p": two(
        "Hercule describes himself as a smuggler who moves goods on and off the islands without Fussar's knowledge. The Red Dead Wiki lists his occupations as revolutionary and smuggler. He has weapons hidden on the island: during the escape in \"Welcome to the New World\" he leads the group to an old building where he says he has guns stashed, and the castaways arm themselves there. He and his men use the old fort of Cinco Torres as a hideout whenever they are on Guarma. He tells Dutch that he is the only one who can arrange a boat off the island, and in \"Hell Hath No Fury\" he finds a ship's captain for the gang (see Biography). He also knows the island's paths: he tells Dutch about the cave below the cliffs that leads to Fussar's compound.",
        "Hercule se présente comme un contrebandier qui fait entrer et sortir des marchandises des îles à l'insu de Fussar. Le Red Dead Wiki le classe parmi les révolutionnaires et les contrebandiers. Il a des armes cachées sur l'île : pendant la fuite, dans \"Welcome to the New World\", il conduit le groupe jusqu'à un vieux bâtiment où il dit avoir planqué des fusils, et les naufragés s'y arment. Ses hommes et lui se servent du vieux fort de Cinco Torres comme repaire chaque fois qu'ils sont à Guarma. Il affirme à Dutch être le seul à pouvoir leur trouver un bateau, et dans \"Hell Hath No Fury\" il déniche un capitaine pour la bande (voir la biographie). Il connaît aussi les passages de l'île : c'est lui qui indique à Dutch la grotte, sous les falaises, qui mène au domaine de Fussar.")},
    {"h4": two("Fighting", "Combat")},
    {"p": two(
        "The Red Dead Wiki credits him with four rifles: a Bolt Action Rifle, a Carcano Rifle, a Springfield Rifle and a Rolling Block Rifle. He fights beside the gang in all three of his missions; the mission pages list him among those who kill soldiers in \"Welcome to the New World\", \"Hell Hath No Fury\" and \"Paradise Mercifully Departed\". At Cinco Torres he readies the fort's cannon, tells Arthur to take the shotgun before going down to the beach, shoots a soldier who is running at Dutch, and keeps the cannon supplied with shot while Arthur aims at the warship. In \"Paradise Mercifully Departed\" he leads Dutch, Arthur and Micah to Fussar's gun positions and spots Fussar in the tower (see Biography, and the Missions table).",
        "Le Red Dead Wiki lui attribue quatre fusils : un Bolt Action Rifle, un Carcano Rifle, un Springfield Rifle et un Rolling Block Rifle. Il se bat aux côtés de la bande dans ses trois missions ; les pages de missions le comptent parmi ceux qui abattent des soldats dans \"Welcome to the New World\", \"Hell Hath No Fury\" et \"Paradise Mercifully Departed\". À Cinco Torres, il prépare le canon du fort, dit à Arthur de prendre le fusil à pompe avant de descendre sur la plage, abat un soldat qui fonce sur Dutch, puis alimente le canon en boulets pendant qu'Arthur vise le navire de guerre. Dans \"Paradise Mercifully Departed\", il guide Dutch, Arthur et Micah jusqu'aux batteries de Fussar et repère Fussar dans la tour (voir la biographie et le tableau des missions).")},
    {"p": two(
        "In \"Welcome to the New World\", the mission fails if the player attacks or kills Hercule or Leon. The Red Dead Wiki notes that in \"Hell Hath No Fury\" he runs very fast on the way back up to the roof, along a path with sharp turns and drops, and advises players to follow him on the mini-map.",
        "Dans \"Welcome to the New World\", la mission échoue si le joueur attaque ou tue Hercule ou Leon. Le Red Dead Wiki relève que dans \"Hell Hath No Fury\", il court très vite pour remonter sur le toit, par un chemin plein de virages serrés et de dénivelés, et conseille de le suivre sur la mini-carte.")},
    {"h4": two("Languages", "Langues")},
    {"p": two(
        "He speaks English with the gang and French with his men. In the transcript, a rebel calls him in French when the warship appears, Hercule swears in French during the fighting at Cinco Torres, and he sets off toward the gun positions with \"En allez\". On the run to the harbor in \"Paradise Mercifully Departed\", he calls the soldiers \"connards\".",
        "Il parle anglais avec la bande et français avec ses hommes. D'après la transcription, un rebelle l'appelle en français quand le navire de guerre apparaît, Hercule jure en français pendant les combats de Cinco Torres, et il lance \"En allez\" au moment de partir vers les batteries. Pendant la course vers le port, dans \"Paradise Mercifully Departed\", il traite les soldats de \"connards\".")},
]

# ---------------------------------------------------------------- RELATIONSHIPS
RELATIONSHIPS = [
    {"img": "dutch-van-der-linde.jpeg", "slug": "dutch-van-der-linde", "name": "Dutch van der Linde", "text": [
        two("Dutch gives his name and the names of Micah, Bill and Arthur after the escape, and asks whether Hercule can be trusted; Hercule answers that they have no choice. Dutch accepts the deal, a boat in return for their help. Later, he tells Arthur that Hercule is \"Almost certainly\" using them, but that he is their best chance of leaving the island.",
            "Après l'évasion, Dutch se présente, présente Micah, Bill et Arthur, puis demande s'il peut faire confiance à Hercule ; celui-ci répond qu'ils n'ont pas le choix. Dutch accepte le marché : un bateau contre leur aide. Plus tard, il confie à Arthur qu'Hercule se sert d'eux, \"Almost certainly\" (très certainement), mais qu'il reste leur meilleure chance de quitter l'île."),
        two("At Cinco Torres, Dutch reminds Hercule that the gang has done what he asked and argues with him over the promised boat (see Biography). After the warship sinks, he tells him: \"Hercule... it was a great pleasure to make your acquaintance.\" Before the attack on the gun positions he lets Hercule lead (\"Hercule, we follow you.\"), and at the harbor he asks whether Hercule will be all right, then thanks him.",
            "À Cinco Torres, Dutch rappelle à Hercule que la bande a fait ce qu'il demandait et lui réclame le bateau promis (voir la biographie). Une fois le navire de guerre coulé, il lui lance : \"Hercule... it was a great pleasure to make your acquaintance.\" (Hercule… ce fut un grand plaisir de faire votre connaissance). Avant l'attaque des batteries, il lui laisse la tête du groupe (\"Hercule, we follow you.\", Hercule, on vous suit), et sur le port il lui demande s'il va s'en sortir, puis le remercie."),
    ]},
    {"img": "arthur-morgan.jpeg", "slug": "arthur-morgan", "name": "Arthur Morgan", "text": [
        two("At the old building where they fight off the soldiers, Arthur thanks Hercule for getting them out and remarks: \"Nice island you got here.\" Hercule replies: \"It's not my island.\" In \"A Kind and Benevolent Despot\", Arthur asks Dutch: \"Are you sure this Hercule feller ain't just using us?\"",
            "Dans le vieux bâtiment où ils repoussent les soldats, Arthur remercie Hercule de les avoir tirés de là et lâche : \"Nice island you got here.\" (jolie île que vous avez là). Hercule répond : \"It's not my island.\" (ce n'est pas mon île). Dans \"A Kind and Benevolent Despot\", Arthur demande à Dutch : \"Are you sure this Hercule feller ain't just using us?\" (t'es sûr que ce type, Hercule, se sert pas juste de nous ?)."),
        two("At Cinco Torres the two men fight side by side. Arthur helps Hercule push the cannon into position; on the beach, when Arthur sends Dutch to cover the left, Hercule says he will follow Arthur. Back on the roof, Arthur fires the cannon while Hercule brings the shot, and the warship sinks. At the harbor, Hercule points Arthur to a second cannon to bring down Fussar's tower (see Biography).",
            "À Cinco Torres, les deux hommes se battent côte à côte. Arthur aide Hercule à mettre le canon en position ; sur la plage, quand Arthur envoie Dutch couvrir le flanc gauche, Hercule annonce qu'il le suit. De retour sur le toit, Arthur tire au canon pendant qu'Hercule apporte les boulets, et le navire de guerre sombre. Sur le port, Hercule indique à Arthur un second canon pour abattre la tour de Fussar (voir la biographie)."),
    ]},
    {"img": "micah-bell.jpeg", "slug": "micah-bell", "name": "Micah Bell", "text": two(
        "During the battle at Cinco Torres, Micah asks: \"Why the hell are we doing this? This ain't our fight!\" Hercule answers: \"Do you want to get off this island or not?\", and Micah shouts: \"He's using us!\" Micah later guards the cannon with Bill, and joins Hercule, Dutch and Arthur in the raid on the gun positions, where he rigs the dynamite (see Biography).",
        "Pendant la bataille de Cinco Torres, Micah s'emporte : \"Why the hell are we doing this? This ain't our fight!\" (qu'est-ce qu'on fout là ? c'est pas notre combat !). Hercule réplique : \"Do you want to get off this island or not?\" (vous voulez quitter cette île, oui ou non ?), et Micah crie : \"He's using us!\" (il se sert de nous !). Micah garde ensuite le canon avec Bill, puis accompagne Hercule, Dutch et Arthur à l'assaut des batteries, qu'il piège à la dynamite (voir la biographie).")},
    {"img": "bill-williamson.jpeg", "slug": "bill-williamson", "name": "Bill Williamson", "text": two(
        "When the soldiers close in on the fort, Bill shouts: \"You said you were getting us a goddamn boat, Hercule!\" Hercule answers: \"I am! What do you want me to do? We are trapped up here!\" Bill stays on the roof to guard the cannon, then on the ship to guard Javier while the others attack the gun positions (see Biography).",
        "Quand les soldats se rapprochent du fort, Bill hurle : \"You said you were getting us a goddamn boat, Hercule!\" (vous deviez nous trouver un foutu bateau, Hercule !). Hercule rétorque : \"I am! What do you want me to do? We are trapped up here!\" (c'est ce que je fais ! qu'est-ce que vous voulez que j'y fasse ? on est coincés là-haut !). Bill reste sur le toit pour garder le canon, puis sur le navire pour veiller sur Javier pendant que les autres attaquent les batteries (voir la biographie).")},
    {"img": "javier-escuella.jpeg", "slug": "javier-escuella", "name": "Javier Escuella", "text": two(
        "Javier is shot in the leg and captured as the group flees the ambush led by Hercule. Hercule tells Dutch that if he is still alive, he will be held at Fussar's compound, and points him to the cave that leads there (see Biography). Javier leaves Guarma on the same ship as the others.",
        "Javier est touché à la jambe et capturé pendant la fuite qui suit l'embuscade menée par Hercule. Hercule explique à Dutch que, s'il est encore en vie, il sera retenu au domaine de Fussar, et lui indique la grotte qui y mène (voir la biographie). Javier quitte Guarma sur le même navire que les autres.")},
    {"img": "alberto-fussar.jpeg", "slug": "alberto-fussar", "name": "Alberto Fussar", "text": two(
        "The colonel who governs Guarma. Hercule smuggles goods behind his back and fights him with the rebels. He calls him Colonel Fussar and Aguasdulces \"Fussar's compound\". At Cinco Torres he tells Dutch that Fussar knows who the gang are and has called in the navy from Cuba. Arthur kills Fussar with a cannon shot at the tower Hercule points out (see Biography). The two men never speak to each other on screen.",
        "Le colonel qui gouverne Guarma. Hercule fait sa contrebande dans son dos et le combat aux côtés des rebelles. Il l'appelle le colonel Fussar et désigne Aguasdulces comme \"Fussar's compound\" (le domaine de Fussar). À Cinco Torres, il apprend à Dutch que Fussar sait qui ils sont et a fait venir la marine de Cuba. Arthur tue Fussar d'un coup de canon sur la tour qu'Hercule lui a désignée (voir la biographie). Les deux hommes ne s'adressent jamais la parole à l'écran.")},
    {"img": None, "slug": None, "name": "Leon Fuentes", "text": two(
        "A rebel chained with the castaways and freed in the ambush. With Hercule, he explains Fussar's rule to the gang; Hercule adds that Leon wants the people to rise against Fussar but that most are too afraid. Hercule asks the gang to help Leon with a group of escaped workers. The Red Dead Wiki describes Leon as a member of the rebel faction led by Hercule.",
        "Rebelle enchaîné avec les naufragés et libéré lors de l'embuscade. Avec Hercule, il explique à la bande comment Fussar règne sur l'île ; Hercule précise que Leon voudrait voir le peuple se soulever contre Fussar, mais que la plupart ont trop peur. Hercule demande à la bande d'aider Leon à retrouver un groupe d'ouvriers en fuite. Le Red Dead Wiki fait de Leon un membre de la faction rebelle dirigée par Hercule.")},
    {"img": None, "slug": None, "name": "Baptiste", "text": two(
        "A one-armed rebel whom Arthur frees in \"Savagery Unleashed\". He introduces himself to Arthur with \"I work with Hercule\", tells him that Hercule is lining up a boat for the gang at Cinco Torres, and gives him money; the Red Dead Wiki puts the sum at 450 dollars and describes him as a smuggler working with Hercule.",
        "Rebelle manchot qu'Arthur libère dans \"Savagery Unleashed\". Il se présente à Arthur par un \"I work with Hercule\" (je travaille avec Hercule), lui annonce qu'Hercule leur prépare un bateau à Cinco Torres et lui remet de l'argent ; le Red Dead Wiki chiffre la somme à 450 dollars et en fait un contrebandier associé à Hercule.")},
    {"img": None, "slug": None, "name": "The ship's captain", "text": two(
        "After the warship sinks, Hercule tells Dutch that he has found a boat and that its captain should reach the dock at any moment. Micah goes to meet him. Fussar's men seize the captain before the gang can sail, and the attack on Aguasdulces frees him (see Biography).",
        "Une fois le navire de guerre coulé, Hercule annonce à Dutch qu'il a trouvé un bateau et que son capitaine devrait arriver au quai d'un moment à l'autre. Micah part à sa rencontre. Les hommes de Fussar s'emparent du capitaine avant le départ, et l'attaque d'Aguasdulces le libère (voir la biographie).")},
    {"img": None, "slug": None, "name": "Levi Simon", "text": two(
        "Fussar's senior overseer, whose patrol chains the castaways on the beach. Before the ambush, he tells Dutch that a \"Bunch of Haitian pirates\" will not frighten Fussar and will soon be hanged in the streets; the game does not say whom he means. He is killed in the cabin standoff (see Biography). He and Hercule never share a scene.",
        "Le contremaître principal de Fussar, dont la patrouille enchaîne les naufragés sur la plage. Avant l'embuscade, il affirme à Dutch qu'une \"Bunch of Haitian pirates\" (bande de pirates haïtiens) ne fera pas peur à Fussar et finira bientôt pendue dans les rues ; le jeu ne précise pas qui il vise. Il meurt lors du face-à-face dans la cabane (voir la biographie). Hercule et lui n'apparaissent jamais ensemble.")},
]
