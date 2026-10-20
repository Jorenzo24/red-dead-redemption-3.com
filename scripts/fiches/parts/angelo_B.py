"""Angelo Bronte, part B: Personality (how others describe him, In his own words, Names, Appearance), The Saint
Denis organization (the men, the mansion, the weapon), Relationships (20 Oct 2026, medium tier).

Sources (register, fetched 20 Oct 2026 via the Red Dead Wiki API, saved in scratchpad cov/angelo/, cov/angelo/m/,
cov/angelo/fcb/):
- Rockstar's character descriptions of 6 Sep 2018 cover the Van der Linde gang only; none exists for Bronte.
- Red Dead Wiki EN "Angelo Bronte": infobox (aka Mister Big, Signor Bronte, Papa Bronte "by Jack (?)", weapon Mauser
  Pistol, affiliations), quote box (the "You are nothing" line, with an audio file), Quotes list (seven lines),
  Appearance, Trivia (Arthur's journal: "a lizard in a suit"; Bronte, a town in Sicily).
- Mission pages: "Angelo Bronte, A Man of Honor" (quote box "You, you, you twist words..."), "The Gilded Cage" (Dutch's
  quote box "the guest of honor is the worst crook in town"), "Revenge is a Dish Best Eaten". No transcript of these
  three missions exists on the wiki (API missingtitle, 20 Oct 2026): Bronte's lines are quoted ONLY from the wiki's
  quote box and Quotes list, with a mission named only when the situation is unique (the Wapiti remark = the party;
  "You are nothing" and the last words = the skiff; the bath and compassion lines and "I love you!" = the first
  meeting, placed there by the mission page's quote box and by part A).
- Documents: "Letter to Angelo Bronte" ("Dear Signor Bronte"), "Letter to Bronte from the Mayor" ("Mon Cher Angelo").
- Wiki pages "Saint Denis Mob" (guards on Flavian Street, hostile on the property, assisting the law when the player is
  wanted there, unique clothing, cross draw harnesses and black gun belts), "Angelo Bronte's Mansion" (accessible only in
  cutscenes and the raid), "Guido Martelli", "Luca" (Luca Napoli), "Benjamin Lambert", "Henri Lemieux".
- Camp Events (cov/hosea/m/Camp_Events.txt): Hosea and Jack at the Shady Belle fountain (circus, cage, palace in a
  story, little prince; Arthur's swamp remark).
- Fact-checked parts reused as is: arthur_D ("the angry cowboy"), dutch_C (Featherstone Chambers), jack_B (Papa Bronte
  without quotation marks), hosea_B, john_A, lenny_A, bill_A, abigail_A.

Ownership (FIX_RULES): Bronte's own quoted lines, how other characters describe him (Dutch's "worst crook in town",
Arthur's journal), names and aliases, appearance, the organization as gameplay (guards, mansion access, weapon) live
HERE. Narrative events and every document (Lawman Found Dead, the two letters, the List of Accounts, the Lambert
telegram) live in part A; this part points to them. Lines quoted here must not be repeated in parts A and C:
"So, you walk into my city..."; "You ask me to show compassion?..."; "You twist words... Give these men drinks!";
"Yes, hand a letter to the mayor..."; "You are nothing... what people are running from."; "The law will find you!
Already the dogs are on the way."; "a lizard in a suit"; "the worst crook in town"; "the angry cowboy".
The Shady Belle fountain scene (Jack, Hosea) is owned by the Jack Marston relationship entry.

WIKI-ONLY (kept, attributed): Mister Big and Papa Bronte (infobox, no context; Papa Bronte marked "(?)"); Arthur's
journal line (trivia); the guards' behavior on the property; the clothing of his men; the Mauser as his weapon.

Excluded: "devious", "ruthless", "deceptive", "false friendliness", "a kinder side when it came to children", "strong
sense of superiority" (wiki interpretation); the long Bastille Saloon insult in the infobox (flagged "(?)" by the wiki
itself); the Italian taunt at the party (part A: sources disagree on whom it targets); the Angelo Bruno and Charles
Matranga models and the Sicilian riot "foreshadowing" (wiki speculation); "middle-aged" (his age, 55, is in part A);
Lambert "in the pocket" of Bronte (wiki inference); the 150 or 155 dollars on his body and the Mauser pickup (part C
Trivia); Red Dead Online, Blood Money and Capitale (part C, Other media).
"""


def two(en, fr): return {"en": en, "fr": fr}

# ---------------------------------------------------------------- PERSONALITY
BLOCKS_PERSONALITY = [
    {"h3": two("Personality", "Personnalité")},
    {"p": two(
        "Rockstar's character descriptions of September 2018 cover the Van der Linde gang and do not include Bronte. In the game, the gang's view of him is blunt. On the way to the mayor's party in \"The Gilded Cage\", Dutch tells Arthur, Bill and Hosea that \"the guest of honor is the worst crook in town\". According to the Red Dead Wiki, Arthur describes him in his journal as \"a lizard in a suit\". Bronte himself calls Arthur \"the angry cowboy\". His public image is the one given by the press and by the mayor's letter (see Biography).",
        "Les descriptions de personnages publiées par Rockstar en septembre 2018 portent sur le gang Van der Linde et ne comprennent pas Bronte. Dans le jeu, la bande ne prend pas de gants avec lui. En route pour la réception du maire, dans \"The Gilded Cage\", Dutch lance à Arthur, Bill et Hosea que \"the guest of honor is the worst crook in town\" (l'invité d'honneur est le pire escroc de la ville). Selon le Red Dead Wiki, Arthur le décrit dans son journal comme \"a lizard in a suit\" (un lézard en costume). Bronte, lui, surnomme Arthur \"the angry cowboy\" (le cow-boy en colère). Son image publique est celle que donnent la presse et la lettre du maire (voir la biographie).")},
    {"h4": two("In his own words", "Dans ses propres mots")},
    {"p": two(
        "No transcript of his scenes is published on the Red Dead Wiki; the lines below come from the wiki's quote list and quote box. At the first meeting he scolds Dutch: \"So, you walk into my city...stinking of shit and looking like this...and you come into my house, before you have a bath...and you tell me how to act?\" He adds: \"You ask me to show compassion? Have I not shown you almost infinite compassion already...by simply allowing you to breathe in my presence?\" Then his tone turns: \"You twist words. You lie shamelessly. You think you are better than everyone else... I love you! Give these men drinks!\" At the party, watching Rains Fall and Eagle Flies approach the mayor, he says: \"Yes, hand a letter to the mayor. Oh yeah, that will save you.\"",
        "Aucune transcription de ses scènes n'est publiée sur le Red Dead Wiki ; les répliques qui suivent viennent de la liste de citations et de l'encadré du wiki. À la première rencontre, il sermonne Dutch : \"So, you walk into my city...stinking of shit and looking like this...and you come into my house, before you have a bath...and you tell me how to act?\" (alors vous entrez dans ma ville en puant la merde, avec cette allure, vous entrez chez moi avant même de prendre un bain, et vous m'apprenez à me tenir ?). Il ajoute : \"You ask me to show compassion? Have I not shown you almost infinite compassion already...by simply allowing you to breathe in my presence?\" (vous me demandez de la compassion ? Ne vous en ai-je pas déjà montré une quasi infinie, rien qu'en vous laissant respirer en ma présence ?). Puis il change de ton : \"You twist words. You lie shamelessly. You think you are better than everyone else... I love you! Give these men drinks!\" (vous tordez les mots, vous mentez sans vergogne, vous vous croyez meilleur que tout le monde… Je vous adore ! Servez à boire à ces messieurs !). Pendant la réception, en voyant Rains Fall et Eagle Flies s'approcher du maire, il glisse : \"Yes, hand a letter to the mayor. Oh yeah, that will save you.\" (c'est ça, remettez une lettre au maire ; voilà qui va vous sauver).")},
    {"p": two(
        "In the skiff, after his abduction, he tells Dutch: \"You are nothing. You do nothing. You mean nothing. You stand for nothing. Me? I run a city... and when the law catch up to you... you will die like nothing. I am this country. You... you... you are what people are running from.\" His last words are: \"The law will find you! Already the dogs are on the way.\"",
        "Dans la barque, après son enlèvement, il lance à Dutch : \"You are nothing. You do nothing. You mean nothing. You stand for nothing. Me? I run a city... and when the law catch up to you... you will die like nothing. I am this country. You... you... you are what people are running from.\" (vous n'êtes rien, vous ne faites rien, vous ne valez rien, vous ne défendez rien. Moi ? Je dirige une ville, et quand la loi vous rattrapera, vous mourrez comme un rien. Ce pays, c'est moi. Vous, vous êtes ce que les gens fuient). Ses derniers mots sont : \"The law will find you! Already the dogs are on the way.\" (la loi vous retrouvera ! Les chiens sont déjà en route).")},
    {"h4": two("Names", "Noms")},
    {"p": two(
        "Catherine Braithwaite opens her letter with \"Dear Signor Bronte\", and the mayor writes to him as \"Mon Cher Angelo\" (see Biography). The Red Dead Wiki lists Mister Big among his aliases without saying who uses it. It also says that Jack calls him Papa Bronte, a name it marks as unconfirmed. Bronte is also the name of a small town in Sicily, the wiki notes.",
        "Catherine Braithwaite ouvre sa lettre par \"Dear Signor Bronte\", et le maire lui écrit \"Mon Cher Angelo\" (voir la biographie). Le Red Dead Wiki range Mister Big parmi ses surnoms, sans dire qui l'emploie. Il indique aussi que Jack l'appelle Papa Bronte, un nom qu'il signale comme non confirmé. Bronte est par ailleurs le nom d'une petite ville de Sicile, relève le wiki.")},
    {"h4": two("Appearance", "Apparence")},
    {"p": two(
        "Bronte has black hair and a tanned complexion. At home he receives his visitors in a crimson smoking jacket edged in gold and a smoking cap with a floral pattern, over a white shirt and black trousers. At the mayor's party he wears white-tie evening dress with a black bow tie.",
        "Bronte a les cheveux noirs et le teint hâlé. Chez lui, il reçoit ses visiteurs en veste d'intérieur cramoisie bordée d'or, coiffé d'une calotte à motifs floraux, sur une chemise blanche et un pantalon noir. À la réception du maire, il porte l'habit de soirée, avec un nœud papillon noir.")},
]

# ---------------------------------------------------------------- SKILLS
BLOCKS_SKILLS = [
    {"h3": two("The Saint Denis organization", "L'organisation de Saint-Denis")},
    {"p": two(
        "His only weapon, according to the Red Dead Wiki, is a Mauser pistol, the one that jams in the raid on his house (see Biography). His power rests on men and money. The Red Dead Wiki calls his organization the Saint Denis Mob. Guido Martelli is his underboss and Luca Napoli one of his servants; both are with him at the mayor's party. The documents found at the party and in his house show his ties to the mayor, to the Saint Denis police chief Benjamin Lambert and to a list of city businesses (see Biography).",
        "Sa seule arme, selon le Red Dead Wiki, est un pistolet Mauser, celui qui s'enraye lors de l'assaut contre sa maison (voir la biographie). Son pouvoir repose sur des hommes et sur de l'argent. Le Red Dead Wiki baptise son organisation la Saint Denis Mob. Guido Martelli est son second et Luca Napoli l'un de ses domestiques ; tous deux l'accompagnent à la réception du maire. Les documents trouvés à la réception et chez lui montrent ses liens avec le maire, avec le chef de la police de Saint-Denis, Benjamin Lambert, et avec une liste de commerces de la ville (voir la biographie).")},
    {"h4": two("The mansion and its guards", "La demeure et ses gardes")},
    {"p": two(
        "His mansion stands on Flavian Street, in Saint Denis, and members of his organization guard it. According to the Red Dead Wiki, they turn hostile if the player walks onto the property in free roam. If the player is wanted while on the grounds, they join the lawmen in the pursuit. The doors of the house stay locked outside the cutscenes and the raid, the wiki adds. His men wear what look like ordinary suits; the wiki points out that most of their clothes are unique to them, including cross draw holsters and black gun belts.",
        "Sa demeure se dresse sur Flavian Street, à Saint-Denis, et des membres de son organisation la gardent. Selon le Red Dead Wiki, ils deviennent hostiles si le joueur pénètre dans la propriété en exploration libre. Si le joueur est recherché alors qu'il s'y trouve, ils se joignent aux hommes de loi pour le poursuivre. En dehors des cinématiques et de l'assaut, les portes de la maison restent fermées à clé, ajoute le wiki. Ses hommes portent ce qui ressemble à de simples costumes ; le wiki souligne que la plupart de leurs vêtements leur sont propres, notamment des holsters croisés et des ceinturons noirs.")},
]

# ---------------------------------------------------------------- RELATIONSHIPS
RELATIONSHIPS = [
    {"img": "dutch-van-der-linde.jpeg", "slug": "dutch-van-der-linde", "name": "Dutch van der Linde", "text": two(
        "Dutch negotiates Jack's return with Bronte in chapter 4 and wins him over. Bronte invites him to the mayor's party and points him to the trolley station, which turns out to be a trap. Dutch then has him abducted and drowns him (see Biography). Bronte's words to Dutch are quoted under Personality.",
        "Dutch négocie avec Bronte le retour de Jack au chapitre 4 et gagne sa sympathie. Bronte l'invite à la réception du maire et lui indique la station de tramway, qui se révèle être un piège. Dutch le fait alors enlever et le noie (voir la biographie). Les paroles de Bronte à Dutch sont citées dans la rubrique Personnalité.")},
    {"img": "jack-marston.jpeg", "slug": "jack-marston", "name": "Jack Marston", "text": two(
        "The Braithwaites hand the kidnapped boy over to Bronte, who returns him to Dutch, Arthur and John (see Biography). At the Shady Belle fountain, according to the Red Dead Wiki's list of camp events, Hosea jokes that he thought Jack had run off with the circus. Jack says that life at Bronte's house was different but nice, that the people were nice too, and that he slept in a bed in a room. Hosea compares it to a cage; Jack answers that it was more like a palace in a story. Hosea calls him their little prince. If Arthur is nearby, Hosea remarks that the boy has grown used to fine living, and Arthur asks what could beat a house in a swamp surrounded by alligators.",
        "Les Braithwaite livrent l'enfant enlevé à Bronte, qui le rend à Dutch, Arthur et John (voir la biographie). À la fontaine de Shady Belle, d'après la liste des événements de camp du Red Dead Wiki, Hosea plaisante : il croyait que Jack s'était enfui avec le cirque. Jack raconte que la vie chez Bronte était différente mais agréable, que les gens y étaient gentils, et qu'il dormait dans un lit, dans une chambre. Hosea compare l'endroit à une cage ; Jack répond que c'était plutôt un palais de conte. Hosea le surnomme leur petit prince. Si Arthur est dans les parages, Hosea remarque que le garçon a pris goût à la belle vie, et Arthur demande ce qu'on pourrait rêver de mieux qu'une maison dans un marais entourée d'alligators.")},
    {"img": "john-marston.jpeg", "slug": "john-marston", "name": "John Marston", "text": two(
        "Jack's father goes to the mansion with Dutch and Arthur and clears the cemetery for Bronte; he tells Arthur on the way that he does not trust him. In the raid, it is John who knocks Bronte out (see Biography).",
        "Le père de Jack se rend à la demeure avec Dutch et Arthur et nettoie le cimetière pour le compte de Bronte ; en chemin, il confie à Arthur qu'il ne lui fait pas confiance. Lors de l'assaut, c'est John qui assomme Bronte (voir la biographie).")},
    {"img": "arthur-morgan.jpeg", "slug": "arthur-morgan", "name": "Arthur Morgan", "text": two(
        "Arthur finds Bronte's address, goes to the mansion and the party, takes part in the trolley station job and carries the unconscious Bronte to the skiff (see Biography). The nickname Bronte gives him and Arthur's journal entry on Bronte are quoted under Personality.",
        "Arthur trouve l'adresse de Bronte, se rend à sa demeure puis à la réception, participe au coup de la station de tramway et porte Bronte inconscient jusqu'à la barque (voir la biographie). Le surnom que lui donne Bronte et la note d'Arthur sur Bronte dans son journal sont cités dans la rubrique Personnalité.")},
    {"img": "hosea-matthews.jpeg", "slug": "hosea-matthews", "name": "Hosea Matthews", "text": two(
        "Hosea attends the mayor's party but mingles with the guests while Dutch and Arthur meet Bronte. He calls Dutch's plan to kill Bronte foolhardy (see Biography).",
        "Hosea assiste à la réception du maire mais se mêle aux invités pendant que Dutch et Arthur rencontrent Bronte. Il juge insensé le projet de Dutch de tuer Bronte (voir la biographie).")},
    {"img": "lenny-summers.jpeg", "slug": "lenny-summers", "name": "Lenny Summers", "text": two(
        "Lenny drives the coach to the mayor's party, is the third man of the trolley station job Bronte suggested, and takes part in the raid on his mansion (see Biography).",
        "Lenny conduit la voiture jusqu'à la réception du maire, sert de troisième homme pour le coup de la station de tramway suggéré par Bronte et participe à l'assaut contre sa demeure (voir la biographie).")},
    {"img": "bill-williamson.jpeg", "slug": "bill-williamson", "name": "Bill Williamson", "text": two(
        "Bill goes to the mayor's party and takes part in the raid on Bronte's mansion (see Biography).",
        "Bill se rend à la réception du maire et participe à l'assaut contre la demeure de Bronte (voir la biographie).")},
    {"img": "catherine-braithwaite.jpeg", "slug": "catherine-braithwaite", "name": "Catherine Braithwaite", "text": two(
        "The Braithwaite matriarch has done business with Bronte for five years, according to her letter to him, and her sons hand Jack over to him. She gives his name to Dutch at Braithwaite Manor (see Biography).",
        "La matriarche des Braithwaite fait affaire avec Bronte depuis cinq ans, d'après la lettre qu'elle lui adresse, et ses fils lui livrent Jack. Elle livre son nom à Dutch à Braithwaite Manor (voir la biographie).")},
    {"img": "alberto-fussar.jpeg", "slug": "alberto-fussar", "name": "Alberto Fussar", "text": two(
        "Bronte points out the governor of Guarma to Dutch and Arthur at the mayor's party (see Biography).",
        "Bronte désigne le gouverneur de Guarma à Dutch et à Arthur lors de la réception du maire (voir la biographie).")},
    {"img": None, "slug": None, "name": "Guido Martelli", "text": two(
        "His underboss stands beside him at the mayor's party, according to the Red Dead Wiki, and runs the organization by 1907 (see Biography).",
        "Son second se tient à ses côtés lors de la réception du maire, selon le Red Dead Wiki, et dirige l'organisation en 1907 (voir la biographie).")},
    {"img": None, "slug": None, "name": "Luca Napoli", "text": two(
        "This servant of Bronte takes the gang's weapons at the entrance of the mayor's party and leads Dutch and Arthur to him. The Red Dead Wiki notes that his surname is heard when the mayor's butler, Pierre, greets him.",
        "Ce domestique de Bronte récupère les armes de la bande à l'entrée de la réception du maire et conduit Dutch et Arthur jusqu'à lui. Le Red Dead Wiki note que son nom de famille se fait entendre quand le majordome du maire, Pierre, le salue.")},
    {"img": None, "slug": None, "name": "Henri Lemieux", "text": two(
        "The mayor of Saint Denis hosts the party where Bronte is the guest of honor and thanks him in writing for a gift to the city (see Biography).",
        "Le maire de Saint-Denis organise la réception dont Bronte est l'invité d'honneur et le remercie par écrit d'un don à la ville (voir la biographie).")},
    {"img": None, "slug": None, "name": "Benjamin Lambert", "text": two(
        "The police chief of Saint Denis is the addressee of Bronte's telegram about the trolley station (see Biography).",
        "Le chef de la police de Saint-Denis est le destinataire du télégramme de Bronte au sujet de la station de tramway (voir la biographie).")},
    {"img": None, "slug": None, "name": "Hector Fellowes", "text": two(
        "At the mayor's party, Bronte shows Dutch this newspaperman and suggests that Dutch might kill him for him one day (see Biography).",
        "À la réception du maire, Bronte montre ce patron de presse à Dutch et suggère qu'il pourrait un jour le tuer pour son compte (voir la biographie).")},
    {"img": None, "slug": None, "name": "Rains Fall and Eagle Flies", "text": two(
        "Bronte mocks the Wapiti chief and his son as they hand a letter to the mayor at the party (see In his own words).",
        "Bronte se moque du chef wapiti et de son fils quand ils remettent une lettre au maire pendant la réception (voir Dans ses propres mots).")},
    {"img": None, "slug": None, "name": "Henry Jenkins", "text": two(
        "This Saint Denis police officer had led an investigation into Bronte before he was found shot dead, according to a newspaper article (see Biography).",
        "Cet agent de la police de Saint-Denis avait mené une enquête sur Bronte avant d'être retrouvé abattu, selon un article de presse (voir la biographie).")},
]
