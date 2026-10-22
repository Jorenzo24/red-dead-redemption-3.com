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
  line, which has no transcript and comes from the Red Dead Wiki quote list, and Arthur's journal entry, given in the
  wording of the mission page's quote box (the transcript drops "him" in "Now I see him as wise").
- Real world: Rockstar's character descriptions of September 6, 2018 (The Hollywood Reporter, September 7, 2018;
  scripts/v3/sources/thr_descriptions.txt): the series covers the Van der Linde gang only, with no entry for Rains Fall.

QUOTES LEFT TO PART B (In his own words), not repeated here: "Sometimes the correct path, the bravest path... is the
least obvious, and also the gentlest", "My son thinks there is glory in death...", "My only boy... my precious boy... do
not mistake my strength for weakness", "I'm a great disappointment to my son", "I hope you can find peace within
yourself", "my whole life I have tried to bring peace", and the Favours exchange on his name ("In English they call me
Rains Fall"). If part B uses any of the lines below, the fixer removes it here.

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
          "Tries to stop his son's war party at Beaver Hollow, then begs Arthur for help. Eagle Flies dies in his tent at the end of the mission.",
          "Tente d'arrêter l'expédition guerrière de son fils à Beaver Hollow, puis supplie Arthur de l'aider. Eagle Flies meurt dans sa tente à la fin de la mission."),
        M("Ending Credits", EP2,
          "Last scene of the credits: he watches an eagle from a peak in the Grizzlies East.",
          "Dernière scène du générique : il regarde passer un aigle depuis un sommet des Grizzlies East."),
        M("Rains Fall (encounter)", EP,
          "Optional encounter with John at Annesburg station before he takes the train back to Canada.",
          "Rencontre facultative avec John à la gare d'Annesburg, avant qu'il ne reprenne le train pour le Canada."),
    ]}},
]

BLOCKS_QUOTES = [
    {"h3": two("Quotes", "Citations")},
    {"p": two("The lines below are given as spoken in the game, in the original English, with the mission and the person addressed. Mission lines are checked against a full transcript of the game; the epilogue line, which has no transcript, comes from the Red Dead Wiki's quote list. Lines already quoted under Personality do not appear again here.",
              "Les répliques ci-dessous sont reproduites telles qu'elles sont prononcées dans le jeu, en anglais, avec la mission et la personne à qui elles s'adressent. Les répliques de mission sont vérifiées sur une transcription complète du jeu ; celle de l'épilogue, sans transcription, provient de la liste de citations du Red Dead Wiki. Les répliques déjà citées dans la rubrique Personnalité ne sont pas reprises ici.")},
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
        {"q": two("See the wolves over there feasting on that horse? Brutality and beauty are both all around us, yet so often we're unable to see past our own grievances. This is what I try to teach my son.",
                  "See the wolves over there feasting on that horse? Brutality and beauty are both all around us, yet so often we're unable to see past our own grievances. This is what I try to teach my son."),
         "src": two("Archeology for Beginners (RDR2, chapter 6), to Arthur, on the ride to the sacred site",
                    "Archeology for Beginners (RDR2, chapitre 6), à Arthur, sur la route du site sacré. Traduction : « Vous voyez les loups là-bas, qui dévorent ce cheval ? La brutalité et la beauté nous entourent, et pourtant nous sommes si souvent incapables de voir au-delà de nos propres griefs. C'est ce que j'essaie d'apprendre à mon fils. »")},
        {"q": two("The army aren't all bad men, just as my people aren't all good.",
                  "The army aren't all bad men, just as my people aren't all good."),
         "src": two("Archeology for Beginners (RDR2, chapter 6), to Arthur, about Captain Monroe and Colonel Favours",
                    "Archeology for Beginners (RDR2, chapitre 6), à Arthur, au sujet du capitaine Monroe et du colonel Favours. Traduction : « L'armée n'est pas faite que de mauvais hommes, tout comme mon peuple n'est pas fait que de bons. »")},
        {"q": two("They moved us here. They've taken everything we had. I signed three treaties myself, and they've broken each one. Now they've taken the last hope... Now my people are gonna want a war. A war they can't win.",
                  "They moved us here. They've taken everything we had. I signed three treaties myself, and they've broken each one. Now they've taken the last hope... Now my people are gonna want a war. A war they can't win."),
         "src": two("Archeology for Beginners (RDR2, chapter 6), at the burned sacred site",
                    "Archeology for Beginners (RDR2, chapitre 6), devant le site sacré incendié. Traduction : « Ils nous ont installés ici. Ils nous ont pris tout ce que nous avions... J'ai signé moi-même trois traités, et ils les ont tous rompus. Maintenant, ils nous ont pris le dernier espoir... Maintenant, mon peuple va vouloir la guerre. Une guerre qu'il ne peut pas gagner. »")},
        {"q": two("Even sacred things... are only things. People... the heart... matter more. Was anyone hurt?",
                  "Even sacred things... are only things. People... the heart... matter more. Was anyone hurt?"),
         "src": two("Archeology for Beginners (RDR2, chapter 6), when Arthur brings back the Chanupa",
                    "Archeology for Beginners (RDR2, chapitre 6), quand Arthur rapporte le Chanupa. Traduction : « Même les choses sacrées... ne sont que des choses. Les gens... le cœur... comptent davantage. Quelqu'un a-t-il été blessé ? »")},
        {"q": two("Now, he has lied to me more times than I care to remember... but maybe this time... he must want peace. Why could he possibly want to humiliate us further?",
                  "Now, he has lied to me more times than I care to remember... but maybe this time... he must want peace. Why could he possibly want to humiliate us further?"),
         "src": two("The Fine Art of Conversation (RDR2, chapter 6), to Arthur at Beaver Hollow, about Colonel Favours",
                    "The Fine Art of Conversation (RDR2, chapitre 6), à Arthur à Beaver Hollow, au sujet du colonel Favours. Traduction : « Il m'a menti plus souvent que je ne veux m'en souvenir... mais peut-être que cette fois... il veut vraiment la paix. Pourquoi voudrait-il nous humilier davantage ? »")},
        {"q": two("My son... my son is foolish but he's... still my son.",
                  "My son... my son is foolish but he's... still my son."),
         "src": two("The King's Son (RDR2, chapter 6), to Arthur, in his tent after Eagle Flies' capture",
                    "The King's Son (RDR2, chapitre 6), à Arthur, dans sa tente après la capture d'Eagle Flies. Traduction : « Mon fils... mon fils est un insensé, mais il reste... mon fils. »")},
        {"q": two("He is the chief's son of a proud nation. How could he commit treason? People have lied to my people for a hundred years or more... that's treason.",
                  "He is the chief's son of a proud nation. How could he commit treason? People have lied to my people for a hundred years or more... that's treason."),
         "src": two("The King's Son (RDR2, chapter 6), to Arthur",
                    "The King's Son (RDR2, chapitre 6), à Arthur. Traduction : « C'est le fils du chef d'une nation fière. Comment pourrait-il commettre une trahison ? On ment à mon peuple depuis cent ans ou plus... voilà la trahison. »")},
        {"q": two("The earth, the water... they have no pride. They endure, and we must endure.",
                  "The earth, the water... they have no pride. They endure, and we must endure."),
         "src": two("My Last Boy (RDR2, chapter 6), to Eagle Flies, at Beaver Hollow",
                    "My Last Boy (RDR2, chapitre 6), à Eagle Flies, à Beaver Hollow. Traduction : « La terre, l'eau... elles n'ont pas d'orgueil. Elles endurent, et nous devons endurer. »")},
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
        {"q": two("He's a man who, not so long ago, I would have found weak and pathetic. Now I see him as wise and thoughtful and sensible. I would love to help him... or at least stop Dutch from pushing his son to do something real stupid.",
                  "He's a man who, not so long ago, I would have found weak and pathetic. Now I see him as wise and thoughtful and sensible. I would love to help him... or at least stop Dutch from pushing his son to do something real stupid."),
         "src": two("Arthur Morgan's journal, after Archeology for Beginners (RDR2, chapter 6)",
                    "Journal d'Arthur Morgan, après Archeology for Beginners (RDR2, chapitre 6). Traduction : « C'est un homme que, il n'y a pas si longtemps, j'aurais trouvé faible et pitoyable. Aujourd'hui, je le vois comme un homme sage, réfléchi et sensé. J'aimerais beaucoup l'aider... ou au moins empêcher Dutch de pousser son fils à faire une grosse bêtise. »")},
        {"q": two("Father has confused wisdom with weakness.",
                  "Father has confused wisdom with weakness."),
         "src": two("Eagle Flies, in A Rage Unleashed (RDR2, chapter 6), when Arthur asks how his father is",
                    "Eagle Flies, dans A Rage Unleashed (RDR2, chapitre 6), quand Arthur lui demande des nouvelles de son père. Traduction : « Père a confondu la sagesse et la faiblesse. »")},
    ]},
]

BLOCKS_TRIVIA = [
    {"h3": two("Trivia", "Anecdotes")},
    {"ul": [
        two("When Rains Fall speaks a Native American language instead of English, the in-game captions identify it as Lakota. He uses it at the peace talks to tell his men that Arthur and Charles are friends.",
            "Quand Rains Fall parle une langue amérindienne au lieu de l'anglais, les sous-titres du jeu indiquent qu'il s'agit du lakota. Il s'en sert pendant les pourparlers de paix pour dire à ses hommes qu'Arthur et Charles sont des amis."),
        two("The Owl Feather Trinket he gives Arthur slows the drain of all of Arthur's cores by 15 percent, according to the mission page.",
            "L'Owl Feather Trinket qu'il offre à Arthur ralentit de 15 % la baisse de toutes ses jauges de base, d'après la page de la mission."),
        two("The two herbs he picks during \"Archeology for Beginners\", English mace and ginseng, are two of the three ingredients of a Special Health Cure; only yarrow is missing.",
            "Les deux plantes qu'il cueille dans \"Archeology for Beginners\", la muscade anglaise et le ginseng, sont deux des trois ingrédients d'un Special Health Cure ; il ne manque que l'achillée."),
        two("The wolves that Arthur scares off on the ride with Rains Fall are, according to the mission page, the only wolves in the game that are not hostile to the player.",
            "Les loups qu'Arthur fait fuir pendant la chevauchée avec Rains Fall sont, d'après la page de la mission, les seuls loups du jeu qui ne sont pas hostiles au joueur."),
        two("Before a game update, the sacred site was already burned when visited in free roam, even as early as chapter 2. Since the update, the site is intact if visited before the mission becomes available.",
            "Avant une mise à jour du jeu, le site sacré était déjà incendié quand on le visitait en exploration libre, dès le chapitre 2. Depuis cette mise à jour, il est intact si on s'y rend avant que la mission soit disponible."),
        two("According to the Red Dead Wiki, Rains Fall is the only character to say Captain Monroe's first name, once, in \"The Fine Art of Conversation\", and only if Arthur has not met Monroe before.",
            "D'après le Red Dead Wiki, Rains Fall est le seul personnage à prononcer le prénom du capitaine Monroe, une seule fois, dans \"The Fine Art of Conversation\", et seulement si Arthur n'a pas encore rencontré Monroe."),
        two("In \"My Last Boy\", Rains Fall uses the word \"implore\" to try to stop Eagle Flies, with John present. John uses the same word at Fort Mercer in 1911 when he tries to make Bill Williamson give himself up. Neither plea works.",
            "Dans \"My Last Boy\", Rains Fall emploie le mot \"implore\" (implorer) pour tenter d'arrêter Eagle Flies, en présence de John. John utilise le même mot à Fort Mercer en 1911 quand il tente de convaincre Bill Williamson de se rendre. Aucune des deux suppliques n'aboutit."),
        two("Meeting Rains Fall in the epilogue gives the player a sizable honor gain.",
            "Rencontrer Rains Fall dans l'épilogue rapporte au joueur un gain d'honneur important."),
        two("According to the Red Dead Wiki, Rains Fall looks visibly older in the 1907 credits scene, while at Annesburg station the same year he looks as he did in 1899.",
            "D'après le Red Dead Wiki, Rains Fall paraît nettement plus âgé dans la scène du générique de 1907, alors qu'à la gare d'Annesburg, la même année, il a la même apparence qu'en 1899."),
    ]},
]

BLOCKS_MEDIA = [
    {"h3": two("Other media and legacy", "Autres médias et postérité")},
    {"p": two("Rains Fall appears only in Red Dead Redemption 2. He was not part of the series of character portraits and descriptions that Rockstar posted on September 6, 2018, and that The Hollywood Reporter reproduced the next day: that series covered the members of the Van der Linde gang. The Red Dead Wiki lists no Red Dead Online appearance for him. In Red Dead Online, the Wapiti Indian Reservation is empty and abandoned, as it is in 1907.",
              "Rains Fall n'apparaît que dans Red Dead Redemption 2. Il ne figure pas dans la série de portraits et de descriptions que Rockstar a publiée le 6 septembre 2018, et que The Hollywood Reporter a reprise le lendemain : cette série portait sur les membres de la bande de Van der Linde. Le Red Dead Wiki ne lui attribue aucune apparition dans Red Dead Online. Dans Red Dead Online, la réserve indienne wapiti est vide et abandonnée, comme en 1907.")},
]
