"""Nastas, reference fiche (v3, medium tier), PART C: Missions, Quotes, Trivia, Other media.

SOURCE REGISTER (Red Dead Wiki EN and FR, fetched Oct 2026; shared cache scripts/v3/work/_m/, copies in
scripts/v3/work/nastas/fc/):
- Character page "Nastas" (Mission appearances, Quotes, Multiplayer lines, Trivia, Gallery captions) and FR page
  "Nastas" (Anecdotes), nastas/en.txt and nastas/fr.txt.
- Mission pages (infobox rewards, order numbers, prerequisites, unlocks, failure conditions, encounters, trivia):
  "Bear One Another's Burdens" (42nd mission, first of West Elizabeth), "At Home with Dutch" (44th), "For Purely
  Scientific Purposes" (45th), "Curious Tales from Blackwater" (Undead Nightmare).
- Transcripts used word for word for every mission quote: "Bear One Another's Burdens/dialogues", "At Home with
  Dutch/dialogues", "For Purely Scientific Purposes/dialogues". Lines without a transcript ("That was my fault.",
  the multiplayer taunts) come from the quote list of the character page.
- Other wiki pages: "Myths and Mavericks" (eight characters added to the Revolution section, Nastas among them;
  released September 13, 2011; announcements of June 6, July 27 and September 1, 2011; seven taunts per pack
  character; promotional screenshot of a Gang Shootout in Gaptooth Breach with Uncle, Landon Ricketts and Nastas),
  "Undead Nightmare" (promotional artwork of the undead Nastas, gallery of the character page).
- Real world: Myths and Mavericks dates as in desanta_C and uncle_C (Engadget, July 27, 2011, cited there); RDR1
  ports PS4/Switch August 17, 2023 and PC October 29, 2024 without multiplayer (as in irish_C, allende_C).

VERIFIED POINTS: "I think they are interested to find out..." is quoted in the transcript's wording, with "[has]"
for the transcript's "was" (typo); the wiki's quote list adds "our", which the transcript does not have. "This is not what we agreed." is in the transcript and the quote list. The At Home
with Dutch "bastard" line, the loot amount (four to seven dollars on the character page, "around 7 dollars" on the
mission page) and the horse-kill failure come from the wiki: attributed. The FR wiki's "wounded in every mission"
remark checks against the transcripts (shot and beaten, hurt in the mine, shot dead, undead).

EXCLUDED: the Navajo/Apache discussion (speculation by the wiki's own words: "more likely", "it is possible"); the
FR wiki's comparison with Eagle Flies and Rains Fall (interpretation); the FR wiki's "certainly due to the
colonising nature of the United States" (interpretation); the Navajo meaning of the name, the "bastard" line, the loot and the horse (part B only);
the shared voice actor with Dutch (part D, Development, already in dutch_D Trivia); the beta model
"NativeAmericanContact" (part D, cut content); the pronunciations "Nosstas" / "Nastoss", the moccasins, the flute
and the Tobiano Pinto horse (part B: Names, Appearance, Skills); "an enraged John" (interpretation).

OWNERSHIP: narrative events live in part A (one line per mission here); the Ledger No. 59 notice is told in part A
only. Lines left to part B "In his own words" or Names and therefore NOT quoted here: "No, sir. I grew up on a reservation
and attended school.", "But we hunt to eat, not for sport.", "Enjoy it while you still can...", "There is no
respect for the land anymore.", "My people have already endured many disasters. Before, this was all our land.",
"Kid got shot in the leg...", Enepay's "treacherous snake" line, Ross's "this savage" and "the Indian". Quoted
HERE only: "For a wise man, you are a very stupid man, mister." and Fordham's "our informant". Trivia adds the
face glitch after his death (character page trivia, attributed). If part B uses a line quoted below, the fixer removes it from one place.
"""


def two(en, fr): return {"en": en, "fr": fr}


M = lambda mission, chap, en, fr: [mission, chap, two(en, fr)]

A3 = two("Act III: West Elizabeth", "Acte III : West Elizabeth")
UN = two("Undead Nightmare", "Undead Nightmare")


BLOCKS_MISSIONS = [
    {"h3": two("Missions", "Missions")},
    {"p": two("Nastas appears in three story missions at the start of the third act of Red Dead Redemption, numbered 42, 44 and 45 in the story order. He gives none of them: the first belongs to Edgar Ross's strand, the next two to Harold MacDougal's. \"Bear One Another's Burdens\" becomes available after Abraham Reyes's \"An Appointed Time\" and is the first mission set in West Elizabeth; it unlocks MacDougal's strand, which begins with \"At Home with Dutch\" and continues with \"For Purely Scientific Purposes\". He also appears in one mission of Undead Nightmare.",
              "Nastas apparaît dans trois missions principales au début du troisième acte de Red Dead Redemption, numérotées 42, 44 et 45 dans l'ordre de l'histoire. Il n'en confie aucune : la première appartient à la série d'Edgar Ross, les deux suivantes à celle de Harold MacDougal. \"Bear One Another's Burdens\" se débloque après \"An Appointed Time\", une mission d'Abraham Reyes, et c'est la première mission située dans l'État de West Elizabeth ; elle débloque la série de MacDougal, qui commence avec \"At Home with Dutch\" et se poursuit avec \"For Purely Scientific Purposes\". Il apparaît aussi dans une mission d'Undead Nightmare.")},
    {"h4": two("Appearances", "Apparitions")},
    {"table": {"head": [two("Mission", "Mission"), two("Act", "Acte"), two("Nastas's role", "Rôle de Nastas")], "rows": [
        M("Bear One Another's Burdens", A3,
          "Found tied up in the wreck of the Serendipity; John carries him to Ross's automobile under fire, and the player must keep his health gauge from running out. Mission giver: Edgar Ross. Rewards: High Power Pistol, 150 fame (200 with the Gold Medal) and 25 honor.",
          "Retrouvé ligoté dans l'épave du Serendipity ; John le porte jusqu'à l'automobile de Ross sous les balles, et le joueur doit veiller à sa jauge de santé. Donneur de mission : Edgar Ross. Récompenses : pistolet High Power, 150 points de célébrité (200 avec la médaille d'or) et 25 d'honneur."),
        M("At Home with Dutch", A3,
          "Guides John and MacDougal to Tall Trees, climbs the cliffs towards Cochinay with John until he is wounded in a mine, then carries the stunned John down. Mission giver: Harold MacDougal. Rewards: Binoculars, 25 honor (50 fame with the Gold Medal); unlocks the A Savage Soul achievement.",
          "Guide John et MacDougal jusqu'à Tall Trees, escalade les falaises vers Cochinay avec John jusqu'à sa blessure dans une mine, puis redescend John assommé. Donneur de mission : Harold MacDougal. Récompenses : jumelles, 25 points d'honneur (50 de célébrité avec la médaille d'or) ; débloque le succès A Savage Soul."),
        M("For Purely Scientific Purposes", A3,
          "Arranges the meeting with Dutch's men at the Bear Claw cabin and is shot dead there by Enepay. Mission giver: Harold MacDougal. Rewards: 25 honor (50 fame with the Gold Medal).",
          "Organise la rencontre avec les hommes de Dutch à la cabane de Bear Claw, où Enepay l'abat. Donneur de mission : Harold MacDougal. Récompenses : 25 points d'honneur (50 de célébrité avec la médaille d'or)."),
        M("Curious Tales from Blackwater", UN,
          "Non-canon. As one of the undead, attacks and devours MacDougal in an alley of Blackwater; the player kills or avoids them both.",
          "Hors canon. Devenu mort-vivant, attaque et dévore MacDougal dans une ruelle de Blackwater ; le joueur les tue ou les évite."),
    ]}},
]


BLOCKS_QUOTES = [
    {"h3": two("Quotes", "Citations")},
    {"p": two("The lines below are given in the original English. Mission lines are checked against the transcripts of the Red Dead Wiki. The line said when he is bumped into and the multiplayer lines come from the wiki's list of his lines, as no transcript exists for them.",
              "Les répliques ci-dessous sont citées dans leur version originale anglaise, suivies d'une traduction. Les répliques de mission sont vérifiées sur les transcriptions du Red Dead Wiki. La réplique prononcée quand on le bouscule et celles du multijoueur proviennent de la liste de ses répliques publiée par le wiki, faute de transcription.")},
    {"h4": two("Red Dead Redemption, Act III", "Red Dead Redemption, acte III")},
    {"quotes": [
        {"q": two("It's a trap!", "It's a trap!"),
         "src": two("Bear One Another's Burdens (RDR1, Act III), when Fordham recognizes him on the wreck",
                    "Bear One Another's Burdens (RDR1, acte III), quand Fordham le reconnaît sur l'épave. Traduction : « C'est un piège ! »")},
        {"q": two("But I can show you what you want to see. I know where the group of bandits you seek are hiding. Both of you. Van der Linde has attracted a following of young men on the reservation. They are turning to bad things.", "But I can show you what you want to see. I know where the group of bandits you seek are hiding. Both of you. Van der Linde has attracted a following of young men on the reservation. They are turning to bad things."),
         "src": two("At Home with Dutch (RDR1, Act III), in MacDougal's office",
                    "At Home with Dutch (RDR1, acte III), dans le bureau de MacDougal. Traduction : « Mais je peux vous montrer ce que vous voulez voir. Je sais où se cache la bande que vous cherchez. Tous les deux. Van der Linde a rallié de jeunes hommes de la réserve. Ils tournent mal. »")},
        {"q": two("I'll be fine, but you go ahead. I don't want to slow you down.", "I'll be fine, but you go ahead. I don't want to slow you down."),
         "src": two("At Home with Dutch (RDR1, Act III), wounded, outside the mine",
                    "At Home with Dutch (RDR1, acte III), blessé, à la sortie de la mine. Traduction : « Ça ira, mais continuez sans moi. Je ne veux pas vous ralentir. »")},
        {"q": two("For a wise man, you are a very stupid man, mister.", "For a wise man, you are a very stupid man, mister."),
         "src": two("At Home with Dutch (RDR1, Act III), to MacDougal, after the professor's story of the Yale acquaintance",
                    "At Home with Dutch (RDR1, acte III), à MacDougal, après l'histoire de sa connaissance de Yale. Traduction : « Pour un homme si savant, vous êtes bien stupide, monsieur. »")},
        {"q": two("I think they are interested to find out what conclusions a white man [has] reached on hundreds of years of culture and society from the comfort of his hotel room.", "I think they are interested to find out what conclusions a white man [has] reached on hundreds of years of culture and society from the comfort of his hotel room."),
         "src": two("For Purely Scientific Purposes (RDR1, Act III), when John asks why Dutch's men would agree to meet the professor",
                    "For Purely Scientific Purposes (RDR1, acte III), quand John demande pourquoi les hommes de Dutch accepteraient de rencontrer le professeur. Traduction : « Je crois qu'ils sont curieux de savoir à quelles conclusions un Blanc est arrivé sur des siècles de culture et de société, sans quitter le confort de sa chambre d'hôtel. »")},
        {"q": two("That bear showed no signs of aggression. If we hadn't shot first, it most likely would have ignored us and moved on.", "That bear showed no signs of aggression. If we hadn't shot first, it most likely would have ignored us and moved on."),
         "src": two("For Purely Scientific Purposes (RDR1, Act III), after the grizzly is killed",
                    "For Purely Scientific Purposes (RDR1, acte III), après la mort du grizzly. Traduction : « Cet ours ne montrait aucun signe d'agressivité. Si nous n'avions pas tiré les premiers, il nous aurait très probablement ignorés et serait reparti. »")},
        {"q": two("This is not what we agreed.", "This is not what we agreed."),
         "src": two("For Purely Scientific Purposes (RDR1, Act III), his last words, in the Bear Claw cabin",
                    "For Purely Scientific Purposes (RDR1, acte III), ses derniers mots, dans la cabane de Bear Claw. Traduction : « Ce n'est pas ce qui était convenu. »")},
        {"q": two("That was my fault.", "That was my fault."),
         "src": two("Red Dead Redemption, when the player bumps into him, according to the Red Dead Wiki",
                    "Red Dead Redemption, quand le joueur le bouscule, d'après le Red Dead Wiki. Traduction : « C'est ma faute. »")},
    ]},
    {"h4": two("What others say about him", "Ce que les autres disent de lui")},
    {"quotes": [
        {"q": two("Good god, that's our informant. Nastas, what the hell's going on here?", "Good god, that's our informant. Nastas, what the hell's going on here?"),
         "src": two("Archer Fordham, Bear One Another's Burdens (RDR1, Act III), on the wreck of the Serendipity",
                    "Archer Fordham, Bear One Another's Burdens (RDR1, acte III), dans l'épave du Serendipity. Traduction : « Bon Dieu, c'est notre informateur. Nastas, qu'est-ce qui se passe ici ? »")},
        {"q": two("Well, Nastas heard the shots and he hurried up to rescue you, and he carried you down. I improvised an escape plan. I'm more of a planner than a man of action.", "Well, Nastas heard the shots and he hurried up to rescue you, and he carried you down. I improvised an escape plan. I'm more of a planner than a man of action."),
         "src": two("Harold MacDougal, At Home with Dutch (RDR1, Act III), when John wakes in Blackwater",
                    "Harold MacDougal, At Home with Dutch (RDR1, acte III), au réveil de John à Blackwater. Traduction : « Enfin, Nastas a entendu les coups de feu, il s'est dépêché de monter vous secourir et il vous a porté jusqu'en bas. Moi, j'ai improvisé un plan de repli. Je suis plus un stratège qu'un homme d'action. »")},
        {"q": two("It's no small relief to have the two of you along with me. Especially you, Nastas.", "It's no small relief to have the two of you along with me. Especially you, Nastas."),
         "src": two("Harold MacDougal, For Purely Scientific Purposes (RDR1, Act III), on the ride to the cabin",
                    "Harold MacDougal, For Purely Scientific Purposes (RDR1, acte III), en route vers la cabane. Traduction : « C'est un vrai soulagement de vous avoir tous les deux avec moi. Vous surtout, Nastas. »")},
        {"q": two("Holy shit... Damn you, Dutch!", "Holy shit... Damn you, Dutch!"),
         "src": two("John Marston, For Purely Scientific Purposes (RDR1, Act III), when Enepay shoots Nastas",
                    "John Marston, For Purely Scientific Purposes (RDR1, acte III), quand Enepay abat Nastas. Traduction : « Bordel... Maudit sois-tu, Dutch ! »")},
        {"q": two("They killed Nastas! Marston, you have to get us out of here!", "They killed Nastas! Marston, you have to get us out of here!"),
         "src": two("Harold MacDougal, For Purely Scientific Purposes (RDR1, Act III), during the shootout at the cabin",
                    "Harold MacDougal, For Purely Scientific Purposes (RDR1, acte III), pendant la fusillade de la cabane. Traduction : « Ils ont tué Nastas ! Marston, il faut nous sortir de là ! »")},
    ]},
    {"h4": two("Multiplayer", "Multijoueur")},
    {"quotes": [
        {"q": two("I don't back down from nobody!", "I don't back down from nobody!"),
         "src": two("Multiplayer taunt, according to the Red Dead Wiki",
                    "Provocation du multijoueur, d'après le Red Dead Wiki. Traduction : « Je ne recule devant personne ! »")},
        {"q": two("Last chance to put the gun down!", "Last chance to put the gun down!"),
         "src": two("Multiplayer taunt, according to the Red Dead Wiki",
                    "Provocation du multijoueur, d'après le Red Dead Wiki. Traduction : « Dernière chance de lâcher ton arme ! »")},
        {"q": two("Come on, then!", "Come on, then!"),
         "src": two("Multiplayer taunt, according to the Red Dead Wiki",
                    "Provocation du multijoueur, d'après le Red Dead Wiki. Traduction : « Allez, viens ! »")},
        {"q": two("Stay and fight!", "Stay and fight!"),
         "src": two("Multiplayer taunt, according to the Red Dead Wiki",
                    "Provocation du multijoueur, d'après le Red Dead Wiki. Traduction : « Reste et bats-toi ! »")},
        {"q": two("I don't care who you are!", "I don't care who you are!"),
         "src": two("Multiplayer taunt, according to the Red Dead Wiki",
                    "Provocation du multijoueur, d'après le Red Dead Wiki. Traduction : « Je me fiche de savoir qui tu es ! »")},
        {"q": two("You shouldn't have done this!", "You shouldn't have done this!"),
         "src": two("Multiplayer taunt, according to the Red Dead Wiki",
                    "Provocation du multijoueur, d'après le Red Dead Wiki. Traduction : « Tu n'aurais pas dû faire ça ! »")},
        {"q": two("You're making a big mistake!", "You're making a big mistake!"),
         "src": two("Multiplayer taunt, according to the Red Dead Wiki",
                    "Provocation du multijoueur, d'après le Red Dead Wiki. Traduction : « Tu fais une grosse erreur ! »")},
    ]},
]


BLOCKS_TRIVIA = [
    {"h3": two("Trivia", "Anecdotes")},
    {"ul": [
        two("The title \"Bear One Another's Burdens\" quotes the Epistle to the Galatians (6:2), as its mission page notes.",
            "Le titre \"Bear One Another's Burdens\" cite l'épître aux Galates (6:2), comme le relève sa page de mission (\"portez les fardeaux les uns des autres\")."),
        two("According to the mission page of \"At Home with Dutch\", the miner who attacks Nastas in the cave uses the model of Quick Tom Candle, a character of the multiplayer mode.",
            "D'après la page de la mission \"At Home with Dutch\", le mineur qui attaque Nastas dans la grotte utilise le modèle de Quick Tom Candle, un personnage du multijoueur."),
        two("According to the Red Dead Wiki, a glitch sometimes deforms his face when the player looks at his body after the cutscene of his death.",
            "D'après le Red Dead Wiki, un bug déforme parfois son visage quand le joueur regarde son corps à la fin de la cinématique de sa mort."),
        two("According to the Red Dead Wiki, Nastas, Hassun and Chogan are the only Native American characters in the game who are not hostile to the player.",
            "D'après le Red Dead Wiki, Nastas, Hassun et Chogan sont les seuls personnages amérindiens du jeu qui ne sont pas hostiles au joueur."),
        two("The French-language Red Dead Wiki notes that he is wounded in every mission in which he appears: shot and beaten on the wreck, hurt in the mine, then killed at the cabin.",
            "Le Red Dead Wiki francophone relève qu'il est blessé dans chacune des missions où il apparaît : blessé par balle et roué de coups sur l'épave, touché dans la mine, puis tué à la cabane."),
    ]},
]


BLOCKS_MEDIA = [
    {"h3": two("Other media and legacy", "Autres médias et postérité")},
    {"h4": two("Multiplayer", "Multijoueur")},
    {"p": two("Nastas became a playable character model in the multiplayer mode of Red Dead Redemption with the Myths and Mavericks Bonus Pack. According to the Red Dead Wiki, Rockstar first hinted at this free pack on June 6, 2011, set a September release on July 27 and gave the date and contents on September 1. It was released free on September 13, 2011 on PlayStation 3 and Xbox 360. It added eight characters to the Revolution section of the Outfitter: Drew MacFarlane, Eli, [[javier-escuella|Javier Escuella]], Jonah, [[landon-ricketts|Landon Ricketts]], Nastas, [[uncle|Uncle]] and [[vincente-de-santa|Vincente de Santa]]. Like the other characters of the pack, he has only seven taunts, all quoted above. The versions of Red Dead Redemption released on PlayStation 4 and Nintendo Switch on August 17, 2023, then on PC on October 29, 2024, do not include the multiplayer mode.",
              "Nastas devient un modèle de personnage jouable du multijoueur de Red Dead Redemption avec le Myths and Mavericks Bonus Pack. D'après le Red Dead Wiki, Rockstar évoque ce pack gratuit pour la première fois le 6 juin 2011, annonce une sortie en septembre le 27 juillet, puis en dévoile la date et le contenu le 1er septembre. Il sort gratuitement le 13 septembre 2011 sur PlayStation 3 et Xbox 360. Il ajoute huit personnages à la section Revolution de l'Outfitter : Drew MacFarlane, Eli, [[javier-escuella|Javier Escuella]], Jonah, [[landon-ricketts|Landon Ricketts]], Nastas, [[uncle|Uncle]] et [[vincente-de-santa|Vincente de Santa]]. Comme les autres personnages du pack, il ne dispose que de sept provocations, toutes citées plus haut. Les versions de Red Dead Redemption sorties sur PlayStation 4 et Nintendo Switch le 17 août 2023, puis sur PC le 29 octobre 2024, ne comprennent pas le multijoueur.")},
    {"h4": two("Promotional material", "Supports promotionnels")},
    {"p": two("Rockstar published a promotional screenshot of Nastas for Red Dead Redemption. For Myths and Mavericks, a promotional screenshot shows a Gang Shootout in Gaptooth Breach with Uncle, Landon Ricketts and Nastas. For Undead Nightmare, a promotional artwork shows him as one of the undead.",
              "Rockstar a diffusé une capture promotionnelle de Nastas pour Red Dead Redemption. Pour Myths and Mavericks, une capture promotionnelle montre une partie de Gang Shootout à Gaptooth Breach avec Uncle, Landon Ricketts et Nastas. Pour Undead Nightmare, une illustration promotionnelle le représente en mort-vivant.")},
    {"h4": two("Later games", "Jeux suivants")},
    {"p": two("Nastas does not appear in Red Dead Redemption 2 or Red Dead Online.",
              "Nastas n'apparaît ni dans Red Dead Redemption 2 ni dans Red Dead Online.")},
]
