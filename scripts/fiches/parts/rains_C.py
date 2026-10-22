"""Rains Fall, reference fiche, PART C: Missions, Quotes, Trivia, Other media.

SOURCE REGISTER (fetched Oct 2026; local copies in scripts/v3/work/rains/ and scripts/v3/work/_m/):
- Red Dead Wiki EN "Rains Fall" (Mission appearances: nine entries, the last one the unlinked epilogue encounter
  "Rains Fall"; Quotes; Trivia) and FR "Pluie-Battante" (Apparitions dans les missions: eight entries).
- Mission pages (infobox chapter, story, trivia, mission failure): "Eastward Bound", "The Gilded Cage",
  "American Fathers I", "American Fathers II", "That's Murfree Country" (via charles_A), "A Rage Unleashed",
  "Archeology for Beginners" (trivia: Owl Feather Trinket 15 percent, herbs, wolves, free-roam site, Bacchus Bridge),
  "Honor, Amongst Thieves", "Favored Sons", "The Fine Art of Conversation", "The King's Son", "My Last Boy" (trivia:
  "implore"), "Ending Credits", "Red Dead Redemption (mission)".
- Red Dead Wiki pages "Lyndon Monroe" (trivia: first name said once by Rains Fall), "Honor" (meeting Rains Fall in the
  epilogue raises honor), "Annesburg", "Annesburg Station", "Wapiti Indian Reservation" (Red Dead Online: empty).
- TRANSCRIPT: "Red Dead Redemption 2 Full Transcript", Game Scripts Wiki
  (game-scripts-wiki.blogspot.com/2022/01/red-dead-redemption-2.html), scripts/v3/work/rains/fc/gsw.txt (gitignored).
  Every mission quote below is checked word for word against it (ellipses normalized to "..."), except the epilogue
  line, which has no transcript and comes from the Red Dead Wiki quote list.
- Rockstar's character descriptions of September 6, 2018: told once, in part B (Personality).

QUOTE OWNERSHIP (FIX_RULES 5, after the fact-check of 22 Oct 2026): lines quoted by part B ("In his own words",
Names, relationship entries: "Brutality and beauty...", "Even sacred things... matter more.", "People have lied to my
people... that's treason.", "The army aren't all bad men...", Arthur's journal) are NOT repeated here. This part keeps
the wiki quote-list lines, all checked against the transcript: the correct path and glory in death (Archeology for
Beginners, gsw l. 12319, 12321), the three treaties, the "My Last Boy" speech (gsw l. 13112, "The men I knew were slain"
given once, "cannot" in one word) and its continuation up to "I implore you" (gsw l. 13114), "bunch of families". The
King's Son line stops at "How could he commit treason?" (the end is quoted in B). Trivia keeps only facts found nowhere
else (Lakota = D; trinket, herbs, Monroe's first name, aged look = B). The 1907 encounter is wiki-only (FIX_RULES 3,
9): attributed in the table and the trivia.

EXCLUDED
- Sitting Bull / Red Cloud / Little Bighorn comparisons (wiki "appear to be based", mission page "similarities"):
  interpretation.
- Concept art name "Rains Come": development, left to part D.
- The outfit worn if "Archeology for Beginners" is failed during the ride: outfit detail.
- The Annesburg page's other placement ("near the Post Office"): contradicts the station placement of the same page and
  of "Annesburg Station"; not used.
- Any Red Dead Online appearance: none listed by the wiki.
"""


def two(en, fr): return {"en": en, "fr": fr}


M = lambda mission, chap, en, fr: [mission, chap, two(en, fr)]

C1 = two("1. Colter", "1. Colter")
C4 = two("4. Saint Denis", "4. Saint-Denis")
C5 = two("5. Guarma", "5. Guarma")
C6 = two("6. Beaver Hollow", "6. Beaver Hollow")
EP = two("Epilogue", "Épilogue")
EP2 = two("Epilogue 2: Beecher's Hope", "Épilogue 2 : Beecher's Hope")

BLOCKS_MISSIONS = [
    {"h3": two("Missions", "Missions")},
    {"p": two("The English Red Dead Wiki lists seven story missions of Red Dead Redemption 2 for Rains Fall, plus the ending credits and an epilogue encounter named after him. The French edition lists eight entries: it leaves out the credits and the encounter, and adds the mission \"Red Dead Redemption\", in which neither the mission page nor the transcript shows him. The table also adds missions where he is only mentioned or where his people's affairs move forward without him; it says so case by case.",
              "Le Red Dead Wiki anglais recense pour Rains Fall sept missions principales de Red Dead Redemption 2, plus le générique de fin et une rencontre de l'épilogue qui porte son nom. L'édition française compte huit entrées : elle laisse de côté le générique et la rencontre, et ajoute la mission \"Red Dead Redemption\", où ni la page de la mission ni la transcription ne le montrent. Le tableau ajoute aussi les missions où il est seulement mentionné, ou dans lesquelles les affaires de son peuple avancent sans lui ; il le précise au cas par cas.")},
    {"table": {"head": [two("Mission", "Mission"), two("Chapter", "Chapitre"), two("Rains Fall's role", "Rôle de Rains Fall")], "rows": [
        M("Eastward Bound", C1,
          "One of three riders watching the gang's wagons from a cliff, according to the wiki. He later tells Arthur that he saw the wagon train cross the river at Cumberland Falls.",
          "L'un des trois cavaliers qui observent les chariots de la bande du haut d'une falaise, d'après le wiki. Il dit plus tard à Arthur avoir vu le convoi traverser la rivière aux Cumberland Falls."),
        M("The Gilded Cage", C4,
          "Guest at the mayor's garden party with Eagle Flies. Bronte mocks the pair as they hand a letter to the mayor.",
          "Invité à la garden-party du maire avec Eagle Flies. Bronte se moque d'eux pendant qu'ils remettent une lettre au maire."),
        M("American Fathers I", C4,
          "Meets Arthur through Evelyn Miller outside the Saint Denis courthouse and promises to pay him for the Cornwall documents.",
          "Rencontre Arthur par l'intermédiaire d'Evelyn Miller devant le palais de justice de Saint-Denis et promet de le payer pour les documents de Cornwall."),
        M("American Fathers II", C4,
          "Not on the wiki's list and absent. Arthur steals the papers with Eagle Flies, who pays him; the mission page gives a reward of 125 dollars.",
          "Absente de la liste du wiki, et Rains Fall n'y apparaît pas. Arthur dérobe les papiers avec Eagle Flies, qui le paie ; la page de la mission indique une récompense de 125 dollars."),
        M("That's Murfree Country", C5,
          "Mentioned only: on the way to Beaver Hollow, Charles tells Arthur he has met Rains Fall and Eagle Flies and has been helping at the reservation.",
          "Seulement mentionné : en route vers Beaver Hollow, Charles raconte à Arthur qu'il a rencontré Rains Fall et Eagle Flies et qu'il aide sur la réserve."),
        M("A Rage Unleashed", C6,
          "Mentioned only. Charles reminds Eagle Flies of his promise to Rains Fall, then asks Arthur to go and see the chief.",
          "Seulement mentionné. Charles rappelle à Eagle Flies la promesse faite à Rains Fall, puis demande à Arthur d'aller voir le chef."),
        M("Archeology for Beginners", C6,
          "Mission giver (optional). Rides with Arthur to a sacred site, gathers herbs for him and, if no soldier is killed, gives him the Owl Feather Trinket for recovering the Chanupa.",
          "Donneur de mission (facultative). Chevauche avec Arthur jusqu'à un site sacré, cueille des herbes pour lui et, si aucun soldat n'est tué, lui offre l'Owl Feather Trinket pour avoir récupéré le Chanupa."),
        M("Honor, Amongst Thieves", C6,
          "Not on the wiki's list and absent. Arthur and Captain Monroe recover vaccines meant for the reservation; Rains Fall thanks Arthur for it in the next mission.",
          "Absente de la liste du wiki, et Rains Fall n'y apparaît pas. Arthur et le capitaine Monroe récupèrent des vaccins destinés à la réserve ; Rains Fall en remercie Arthur dans la mission suivante."),
        M("Favored Sons", C6,
          "Not on the wiki's list and absent. Eagle Flies is captured after an ambush on an Army patrol with Dutch and Arthur.",
          "Absente de la liste du wiki, et Rains Fall n'y apparaît pas. Eagle Flies est capturé après une embuscade contre une patrouille de l'armée menée avec Dutch et Arthur."),
        M("The Fine Art of Conversation", C6,
          "Mission giver with Trelawny, per the mission page. Asks Arthur and Charles to attend his talks with Colonel Favours, which fail.",
          "Donneur de mission avec Trelawny, selon la page de la mission. Demande à Arthur et à Charles d'assister à ses pourparlers avec le colonel Favours, qui échouent."),
        M("The King's Son", C6,
          "Receives Arthur in his tent after his son's capture and opposes a rescue, which Arthur and Charles carry out anyway.",
          "Reçoit Arthur dans sa tente après la capture de son fils et s'oppose à un sauvetage, qu'Arthur et Charles mènent malgré tout."),
        M("My Last Boy", C6,
          "Tries to stop his son's war party at Beaver Hollow, then begs Arthur for help. Eagle Flies dies in Rains Fall's tent at the end of the mission.",
          "Tente d'arrêter l'expédition guerrière de son fils à Beaver Hollow, puis supplie Arthur de l'aider. Eagle Flies meurt sous la tente de son père à la fin de la mission."),
        M("Ending Credits", EP2,
          "Last scene of the credits: he watches an eagle from a peak in the Grizzlies East.",
          "Dernière scène du générique : il regarde passer un aigle depuis un sommet des Grizzlies East."),
        M("Rains Fall (encounter)", EP,
          "Optional encounter with John at Annesburg station; according to the Red Dead Wiki, he then takes the train back to Canada.",
          "Rencontre facultative avec John à la gare d'Annesburg ; d'après le Red Dead Wiki, il reprend ensuite le train pour le Canada."),
    ]}},
]

BLOCKS_QUOTES = [
    {"h3": two("Quotes", "Citations")},
    {"p": two("The lines below are given as spoken in the game, in the original English, with the mission and the person addressed. Mission lines are checked against a full transcript of the game; the epilogue line, which has no transcript, comes from the Red Dead Wiki's quote list. Lines already quoted under Personality or Relationships do not appear again here.",
              "Les répliques ci-dessous sont reproduites telles qu'elles sont prononcées dans le jeu, en anglais, avec la mission et la personne à qui elles s'adressent. Les répliques de mission sont vérifiées sur une transcription complète du jeu ; celle de l'épilogue, sans transcription, provient de la liste de citations du Red Dead Wiki. Les répliques déjà citées dans les rubriques Personnalité ou Relations ne sont pas reprises ici.")},
    {"h4": two("Chapter 4", "Chapitre 4")},
    {"quotes": [
        {"q": two("Yes, my people, if we are even a people anymore... we fought hard... we've made peace treaties... and those treaties were broken... and we've been moved and punished and... punished and moved.",
                  "Yes, my people, if we are even a people anymore... we fought hard... we've made peace treaties... and those treaties were broken... and we've been moved and punished and... punished and moved."),
         "src": two("American Fathers I (RDR2, chapter 4), to Arthur, outside the Saint Denis courthouse",
                    "American Fathers I (RDR2, chapitre 4), à Arthur, devant le palais de justice de Saint-Denis. Traduction : « Oui, mon peuple, si nous sommes encore un peuple... nous nous sommes battus durement... nous avons signé des traités de paix... et ces traités ont été rompus... et on nous a déplacés et punis, et... punis et déplacés. »")},
        {"q": two("No, my son, it will not. We cannot fight another war. They have got stronger... and we have become far weaker, Mr. Morgan.",
                  "No, my son, it will not. We cannot fight another war. They have got stronger... and we have become far weaker, Mr. Morgan."),
         "src": two("American Fathers I (RDR2, chapter 4), after Eagle Flies predicts that a new move will lead to war",
                    "American Fathers I (RDR2, chapitre 4), après qu'Eagle Flies a prédit qu'un nouveau déplacement mènerait à la guerre. Traduction : « Non, mon fils, ce ne sera pas le cas. Nous ne pouvons pas mener une autre guerre. Ils sont devenus plus forts... et nous, bien plus faibles, monsieur Morgan. »")},
    ]},
    {"h4": two("Chapter 6", "Chapitre 6")},
    {"quotes": [
        {"q": two("Yes, sometimes the correct path, the bravest path... is the least obvious, and also the gentlest.",
                  "Yes, sometimes the correct path, the bravest path... is the least obvious, and also the gentlest."),
         "src": two("Archeology for Beginners (RDR2, chapter 6), to Arthur, in his tent, after telling him of Colonel Favours' revenge",
                    "Archeology for Beginners (RDR2, chapitre 6), à Arthur, sous sa tente, après lui avoir appris la vengeance du colonel Favours. Traduction : « Oui, parfois le bon chemin, le plus courageux... est le moins évident, et aussi le plus doux. »")},
        {"q": two("My son thinks there is glory in death. Maybe he's right... but for me... I saw death being handed out so freely by the most foolish of men... I never could equate it with victory.",
                  "My son thinks there is glory in death. Maybe he's right... but for me... I saw death being handed out so freely by the most foolish of men... I never could equate it with victory."),
         "src": two("Archeology for Beginners (RDR2, chapter 6), to Arthur, who has just said that his son seems to want a war",
                    "Archeology for Beginners (RDR2, chapitre 6), à Arthur, qui vient de lui dire que son fils semble vouloir la guerre. Traduction : « Mon fils pense qu'il y a de la gloire dans la mort. Il a peut-être raison... mais moi... j'ai vu la mort distribuée si librement par les plus insensés des hommes... je n'ai jamais pu y voir une victoire. »")},
        {"q": two("They moved us here. They've taken everything we had. I signed three treaties myself, and they've broken each one. Now they've taken the last hope... Now my people are gonna want a war. A war they can't win.",
                  "They moved us here. They've taken everything we had. I signed three treaties myself, and they've broken each one. Now they've taken the last hope... Now my people are gonna want a war. A war they can't win."),
         "src": two("Archeology for Beginners (RDR2, chapter 6), at the burned sacred site",
                    "Archeology for Beginners (RDR2, chapitre 6), devant le site sacré incendié. Traduction : « Ils nous ont installés ici. Ils nous ont pris tout ce que nous avions... J'ai signé moi-même trois traités, et ils les ont tous rompus. Maintenant, ils nous ont pris le dernier espoir... Maintenant, mon peuple va vouloir la guerre. Une guerre qu'il ne peut pas gagner. »")},
        {"q": two("Now, he has lied to me more times than I care to remember... but maybe this time... he must want peace. Why could he possibly want to humiliate us further?",
                  "Now, he has lied to me more times than I care to remember... but maybe this time... he must want peace. Why could he possibly want to humiliate us further?"),
         "src": two("The Fine Art of Conversation (RDR2, chapter 6), to Arthur at Beaver Hollow, about Colonel Favours",
                    "The Fine Art of Conversation (RDR2, chapitre 6), à Arthur à Beaver Hollow, au sujet du colonel Favours. Traduction : « Il m'a menti plus souvent que je ne veux m'en souvenir... mais peut-être que cette fois... il veut vraiment la paix. Pourquoi voudrait-il nous humilier davantage ? »")},
        {"q": two("My son... my son is foolish but he's... still my son.",
                  "My son... my son is foolish but he's... still my son."),
         "src": two("The King's Son (RDR2, chapter 6), to Arthur, in his tent after Eagle Flies's capture",
                    "The King's Son (RDR2, chapitre 6), à Arthur, dans sa tente après la capture d'Eagle Flies. Traduction : « Mon fils... mon fils est un insensé, mais il reste... mon fils. »")},
        {"q": two("All my life, I've tried to bring peace... but I love my son. They'll hang him for treason. He is the chief's son of a proud nation. How could he commit treason?",
                  "All my life, I've tried to bring peace... but I love my son. They'll hang him for treason. He is the chief's son of a proud nation. How could he commit treason?"),
         "src": two("The King's Son (RDR2, chapter 6), to Arthur, after his son's capture",
                    "The King's Son (RDR2, chapitre 6), à Arthur. Traduction : « Toute ma vie, j'ai cherché à apporter la paix... mais j'aime mon fils. Ils vont le pendre pour trahison. C'est le fils du chef d'une nation fière. Comment pourrait-il trahir ? »")},
        {"q": two("My son, my last son... When I was your age... I fought... I saw death. I have killed. The men I knew were slain. My first born, your brother... had his head smashed by a drunken soldier. My wife had her throat slit. We made peace. I knew not to trust, yet I had no choice. Maybe you were right... maybe the slow death is worse than a fast one. Maybe none of these men are good. Maybe a world in which they came to us... is a world that we cannot endure. But endure we must.",
                  "My son, my last son... When I was your age... I fought... I saw death. I have killed. The men I knew were slain. My first born, your brother... had his head smashed by a drunken soldier. My wife had her throat slit. We made peace. I knew not to trust, yet I had no choice. Maybe you were right... maybe the slow death is worse than a fast one. Maybe none of these men are good. Maybe a world in which they came to us... is a world that we cannot endure. But endure we must."),
         "src": two("My Last Boy (RDR2, chapter 6), to Eagle Flies, at Beaver Hollow",
                    "My Last Boy (RDR2, chapitre 6), à Eagle Flies, à Beaver Hollow. Traduction : « Mon fils, mon dernier fils... Quand j'avais ton âge... je me suis battu... j'ai vu la mort. J'ai tué. Les hommes que je connaissais ont été massacrés. Mon premier-né, ton frère... a eu le crâne fracassé par un soldat ivre. Ma femme a été égorgée. Nous avons fait la paix. Je savais qu'il ne fallait pas leur faire confiance, mais je n'avais pas le choix. Tu avais peut-être raison... peut-être que la mort lente est pire qu'une mort rapide. Peut-être qu'aucun de ces hommes n'est bon. Peut-être qu'un monde où ils sont venus jusqu'à nous... est un monde que nous ne pouvons pas endurer. Mais endurer, nous le devons. »")},
        {"q": two("Do not die for pride, my son. We have suffered too much in this trick. The earth, the water... they have no pride. They endure, and we must endure. My only boy... my precious boy... do not mistake my strength for weakness. As your chief, I implore you.",
                  "Do not die for pride, my son. We have suffered too much in this trick. The earth, the water... they have no pride. They endure, and we must endure. My only boy... my precious boy... do not mistake my strength for weakness. As your chief, I implore you."),
         "src": two("My Last Boy (RDR2, chapter 6), to Eagle Flies, who has just told him he is tired",
                    "My Last Boy (RDR2, chapitre 6), à Eagle Flies, qui vient de lui dire qu'il est fatigué. Traduction : « Ne meurs pas par orgueil, mon fils. Nous avons trop souffert de cette ruse. La terre, l'eau... elles n'ont pas d'orgueil. Elles endurent, et nous devons endurer. Mon fils unique... mon fils chéri... ne prends pas ma force pour de la faiblesse. En tant que ton chef, je t'implore. »")},
        {"q": two("The wars are over... we have lost. These young men will be annihilated. Please.",
                  "The wars are over... we have lost. These young men will be annihilated. Please."),
         "src": two("My Last Boy (RDR2, chapter 6), to Arthur, after Eagle Flies rides off",
                    "My Last Boy (RDR2, chapitre 6), à Arthur, après le départ d'Eagle Flies. Traduction : « Les guerres sont finies... nous avons perdu. Ces jeunes hommes vont être anéantis. Je vous en prie. »")},
    ]},
    {"h4": two("Epilogue", "Épilogue")},
    {"quotes": [
        {"q": two("Ah, well... my people aren't really a tribe, we're just a... bunch of families, I suppose... but we're in Canada now.",
                  "Ah, well... my people aren't really a tribe, we're just a... bunch of families, I suppose... but we're in Canada now."),
         "src": two("Epilogue encounter at Annesburg station (RDR2, 1907), to John Marston (Red Dead Wiki quote list)",
                    "Rencontre de l'épilogue à la gare d'Annesburg (RDR2, 1907), à John Marston (liste de citations du Red Dead Wiki). Traduction : « Ah, eh bien... mon peuple n'est plus vraiment une tribu, nous ne sommes plus qu'un... groupe de familles, je suppose... mais nous sommes au Canada, maintenant. »")},
    ]},
    {"h4": two("About Rains Fall", "À propos de Rains Fall")},
    {"quotes": [
        {"q": two("Father has confused wisdom with weakness.",
                  "Father has confused wisdom with weakness."),
         "src": two("Eagle Flies, in A Rage Unleashed (RDR2, chapter 6), when Arthur asks how his father is",
                    "Eagle Flies, dans A Rage Unleashed (RDR2, chapitre 6), quand Arthur lui demande des nouvelles de son père. Traduction : « Père a confondu la sagesse et la faiblesse. »")},
    ]},
]

BLOCKS_TRIVIA = [
    {"h3": two("Trivia", "Anecdotes")},
    {"ul": [
        two("The wolves that Arthur scares off on the ride with Rains Fall are, according to the mission page, the only wolves in the game that are not hostile to the player.",
            "Les loups qu'Arthur fait fuir pendant la chevauchée avec Rains Fall sont, d'après la page de la mission, les seuls loups du jeu qui ne sont pas hostiles au joueur."),
        two("In early versions of the game, the sacred site could be found already burned in free roam from chapter 2 onward; according to the mission page, a later update leaves it standing until the mission is available.",
            "Dans les premières versions du jeu, on pouvait trouver le site sacré déjà incendié en exploration libre dès le chapitre 2 ; d'après la page de la mission, une mise à jour l'a ensuite laissé intact tant que la mission n'est pas disponible."),
        two("In \"My Last Boy\", Rains Fall uses the word \"implore\" to try to stop Eagle Flies, with John present. John uses the same word at Fort Mercer in 1911 when he tries to make Bill Williamson give himself up. Neither plea works.",
            "Dans \"My Last Boy\", Rains Fall emploie le mot \"implore\" (implorer) pour tenter d'arrêter Eagle Flies, en présence de John. John utilise le même mot à Fort Mercer en 1911 quand il tente de convaincre Bill Williamson de se rendre. Aucune des deux suppliques n'aboutit."),
        two("The Annesburg meeting in 1907 raises John's honor by a large amount, according to the Red Dead Wiki.",
            "D'après le Red Dead Wiki, la rencontre d'Annesburg en 1907 fait nettement monter l'honneur de John."),
    ]},
]

BLOCKS_MEDIA = [
    {"h3": two("Other media and legacy", "Autres médias et postérité")},
    {"p": two("Rains Fall appears only in Red Dead Redemption 2. The Red Dead Wiki lists no Red Dead Online appearance for him. According to the Red Dead Wiki, the reservation has no inhabitants in Red Dead Online, the same state in which John finds it in 1907.",
              "Rains Fall n'apparaît que dans Red Dead Redemption 2. Le Red Dead Wiki ne lui attribue aucune apparition dans Red Dead Online. Toujours d'après le Red Dead Wiki, la réserve n'y compte aucun habitant, comme lorsque John la découvre en 1907.")},
]
