"""Catherine Braithwaite, reference fiche, PART C: Missions, Quotes, Trivia, Other media.

SOURCE REGISTER (fetched Oct 2026; local copies in scripts/v3/work/catherine/ and scripts/v3/work/_m/):
- Red Dead Wiki EN "Catherine Braithwaite" (mission appearances, trivia: brooch, Red Dead Online mention) and FR page
  (anecdote: the brooch sells for a good price).
- Red Dead Wiki mission pages: "The New South", "American Distillation", "Advertising, The New American Art",
  "The Fine Joys of Tobacco" (quote box), "Horse Flesh for Dinner" (trivia: Braithwaite brand on the horses), "A Short
  Walk in a Pretty Town", "Blood Feuds, Ancient and Modern" (trivia: brooch, Gareth/Bartholomew mix-up, second trailer;
  mission failure; missable items; music), "The Battle of Shady Belle", "Angelo Bronte, A Man of Honor", "The Course of
  True Love II" and "V".
- Red Dead Wiki pages "Braithwaite Manor" (gold bar lockbox, smoke in "The Battle of Shady Belle", Oak Alley and Houmas
  House), "Braithwaite Family" (Red Dead Online "A Life of 'Shine" missions; village of Braithwaite in Cumbria),
  "Gareth Braithwaite" (patch trivia), "Gertrude Braithwaite" (gallery caption quoting Arthur's journal; point of interest
  "Braithwaites' Secret"), "Gray Family" (Lucille Braithwaite and Douglas Gray graves in Rhodes), "Letter to Angelo
  Bronte" (nightstand, same room as the Gold Shield), "Bartholomew Braithwaite" (Red Dead Online: Hixon, 100 dollars).
- TRANSCRIPT: "Red Dead Redemption 2 Full Transcript", Game Scripts Wiki (game-scripts-wiki.blogspot.com), saved as
  scripts/v3/work/catherine/fc/gsw.txt: source of every quoted line below except Arthur's journal (Gertrude page caption)
  and Pearson's 1907 line (Simon Pearson quote list, as in simon_C). Speaker labels: the transcript labels Bartholomew's
  lines "Braithwaite" (manor scenes) or "Gareth Braithwaite" (front of the house in "Blood Feuds"); the wiki's
  Bartholomew quote list attributes all of them to Bartholomew, and the mission page says the subtitles label him Gareth.
  The source lines say so.
- Real world: Red Dead Online "Moonshiners" update, released December 13, 2019 (Xbox Wire, 13 Dec 2019; GTABase patch
  notes; note in scripts/v3/work/catherine/fc/moonshiners_release_date.txt). Second trailer of Red Dead Redemption 2,
  September 28, 2017 (date as in the fact-checked hosea_C and bill_C).
- Red Dead Online free roam: Trelawny's Horse Theft mission (character page trivia; josiah_C).

Ownership: narrative events are in part A (one line per mission here). Catherine's own lines (the 120 years, "Yankees",
"Ain't no rules in war", "as big and as dumb as he looks", "promotional expense", "Pay the man") are NOT quoted here:
they are left to part B "In her own words". Quotes here are lines by others about her or to her family.
Fix pass (22 Oct 2026, lead decisions): Bartholomew's name is attributed to the wiki in every quote source; the
"Gareth" subtitle is told once (Trivia); Archibald's thoroughbred line and Tavish's "hag" line stay in Quotes (part B
paraphrases them); the horse-brand and Bill-in-Rhodes trivia items are cut (told in part B Horses and part A).
Excluded: the gold medal objective that names who must shoot Gareth and Gerald (would name the killers, no transcript);
the stablehand's names for the three horses (Cerberus, Old Faithful, Old Father Time): they are horses at the stable, the
transcript does not say which three are taken; the YouTube title calling a Turkoman "courtesy of Catherine Braithwaite"
(not a source); the Django Unchained resemblance (wiki: "noted by many", opinion); the "Mister Braithwaite" in Undead
Nightmare (wiki: link unknown); Sean's vulgar lines about Catherine (kept out of Quotes, paraphrased in part A); the
Plantation Hat pickup (not about her).
"""


def two(en, fr): return {"en": en, "fr": fr}


M = lambda mission, chap, en, fr: [mission, chap, two(en, fr)]

C3 = two("3. Clemens Point", "3. Clemens Point")
C4 = two("4. Saint Denis", "4. Saint-Denis")
C6 = two("6. Beaver Hollow", "6. Beaver Hollow")

BLOCKS_MISSIONS = [
    {"h3": two("Missions", "Missions")},
    {"p": two("Catherine Braithwaite appears in three missions of Red Dead Redemption 2, all in chapter 3. Other missions take place on her land, bring up her family or deal with what follows her death; they are listed in the second table. The events themselves are told in the Biography.",
              "Catherine Braithwaite apparaît dans trois missions de Red Dead Redemption 2, toutes au chapitre 3. D'autres missions se déroulent sur ses terres, évoquent sa famille ou traitent des suites de sa mort ; elles figurent dans le second tableau. Le déroulé des événements se trouve dans la Biographie.")},
    {"h4": two("Appearances", "Apparitions")},
    {"table": {"head": [two("Mission", "Mission"), two("Chapter", "Chapitre"), two("Catherine's role", "Rôle de Catherine")], "rows": [
        M("Advertising, The New American Art", C3,
          "Pays [[hosea-matthews|Hosea]] and [[arthur-morgan|Arthur]] for her own stolen moonshine, then ten dollars more to give it away in the Grays' saloon in Rhodes.",
          "Paie [[hosea-matthews|Hosea]] et [[arthur-morgan|Arthur]] pour son propre alcool volé, puis dix dollars de plus pour qu'ils le distribuent dans le saloon des Gray, à Rhodes."),
        M("The Fine Joys of Tobacco", C3,
          "Plays cribbage with Hosea and [[sean-macguire|Sean]] and hires Arthur and Sean to burn the Grays' tobacco fields at Caliga Hall.",
          "Joue au cribbage avec Hosea et [[sean-macguire|Sean]] et charge Arthur et Sean de brûler les champs de tabac des Gray à Caliga Hall."),
        M("Blood Feuds, Ancient and Modern", C3,
          "Loses her sons and her house to [[dutch-van-der-linde|Dutch]]'s gang, reveals that her sons gave [[jack-marston|Jack]] to [[angelo-bronte|Angelo Bronte]] and runs back into the burning manor.",
          "Perd ses fils et sa maison face à la bande de [[dutch-van-der-linde|Dutch]], révèle que ses fils ont livré [[jack-marston|Jack]] à [[angelo-bronte|Angelo Bronte]] et retourne dans le manoir en flammes."),
    ]}},
    {"h4": two("Other missions linked to Catherine", "Autres missions liées à Catherine")},
    {"table": {"head": [two("Mission", "Mission"), two("Chapter", "Chapitre"), two("Link with Catherine", "Lien avec Catherine")], "rows": [
        M("The New South", C3,
          "Dutch gives Hosea the Braithwaites to work on.",
          "Dutch confie les Braithwaite à Hosea."),
        M("American Distillation", C3,
          "Arthur, Dutch and [[bill-williamson|Bill]] destroy a Braithwaite still and keep the moonshine.",
          "Arthur, Dutch et [[bill-williamson|Bill]] détruisent un alambic des Braithwaite et gardent l'alcool."),
        M("The Course of True Love II", C3,
          "Arthur slips onto the Braithwaite estate to deliver Beau Gray's letter to her niece Penelope.",
          "Arthur se glisse sur le domaine des Braithwaite pour remettre la lettre de Beau Gray à sa nièce Penelope."),
        M("Horse Flesh for Dinner", C3,
          "Arthur, [[john-marston|John]] and [[javier-escuella|Javier]] steal her prized horses for [[tavish-gray|Tavish Gray]].",
          "Arthur, [[john-marston|John]] et [[javier-escuella|Javier]] volent ses chevaux de prix pour [[tavish-gray|Tavish Gray]]."),
        M("A Short Walk in a Pretty Town", C3,
          "Sean is killed in a Gray ambush in Rhodes; back at camp, Jack has disappeared.",
          "Sean est tué dans une embuscade des Gray à Rhodes ; au retour, Jack a disparu du camp."),
        M("The Battle of Shady Belle", C3,
          "Opens at Clemens Point the morning after the raid on her manor.",
          "S'ouvre à Clemens Point au lendemain de l'assaut contre son manoir."),
        M("Angelo Bronte, A Man of Honor", C4,
          "Bronte returns Jack, whom her sons had handed to him.",
          "Bronte rend Jack, que ses fils lui avaient livré."),
        M("The Course of True Love V", C6,
          "Arthur helps Penelope escape from the ruined estate and fights off the Braithwaite riders chasing her train.",
          "Arthur aide Penelope à fuir le domaine en ruine et repousse les cavaliers Braithwaite qui poursuivent son train."),
    ]}},
]


BLOCKS_QUOTES = [
    {"h3": two("Quotes", "Citations")},
    {"p": two("The lines below are given in the original English. Catherine's own words are quoted under Personality.",
              "Les répliques ci-dessous sont citées en version originale. Les paroles de Catherine elle-même figurent dans la rubrique Personnalité.")},
    {"h4": two("Her family", "Sa famille")},
    {"quotes": [
        {"q": two("The alternative is you get shot.", "The alternative is you get shot."),
         "src": two("A Braithwaite son (Bartholomew according to the Red Dead Wiki) to Hosea, who suggests selling the moonshine elsewhere, Advertising, The New American Art (RDR2, chapter 3)",
                    "Un fils Braithwaite (Bartholomew selon le Red Dead Wiki) à Hosea, qui propose de vendre l'alcool ailleurs, Advertising, The New American Art (RDR2, chapitre 3). Traduction : « L'autre solution, c'est qu'on vous abatte. »")},
        {"q": two("She ain't gonna pay you with a certified check... you Yankee numbskull.", "She ain't gonna pay you with a certified check... you Yankee numbskull."),
         "src": two("A Braithwaite son (Bartholomew according to the Red Dead Wiki) to Hosea, who asks how his mother will pay, The Fine Joys of Tobacco (RDR2, chapter 3)",
                    "Un fils Braithwaite (Bartholomew selon le Red Dead Wiki) à Hosea, qui demande comment sa mère compte payer, The Fine Joys of Tobacco (RDR2, chapitre 3). Traduction : « Elle va pas vous payer par chèque certifié... espèce d'abruti de Yankee. »")},
        {"q": two("Shouldn't have messed with our business now, should you?", "Shouldn't have messed with our business now, should you?"),
         "src": two("A Braithwaite son to Dutch in front of the manor (Bartholomew according to the Red Dead Wiki), Blood Feuds, Ancient and Modern (RDR2, chapter 3)",
                    "Un fils Braithwaite à Dutch, devant le manoir (Bartholomew selon le Red Dead Wiki), Blood Feuds, Ancient and Modern (RDR2, chapitre 3). Traduction : « Fallait pas vous mêler de nos affaires, hein ? »")},
        {"q": two("The main house and all it stood for are thankfully no more.", "The main house and all it stood for are thankfully no more."),
         "src": two("Penelope Braithwaite, her niece, in her letter to Arthur, The Course of True Love V (RDR2, chapter 6)",
                    "Penelope Braithwaite, sa nièce, dans sa lettre à Arthur, The Course of True Love V (RDR2, chapitre 6). Traduction : « La maison principale, et tout ce qu'elle représentait, n'existent plus, Dieu merci. »")},
    ]},
    {"h4": two("About Catherine and the Braithwaites", "Au sujet de Catherine et des Braithwaite")},
    {"quotes": [
        {"q": two("Not to mention the fact that Catherine Braithwaite has a rather... expensive interest in thoroughbred horses to maintain.",
                  "Not to mention the fact that Catherine Braithwaite has a rather... expensive interest in thoroughbred horses to maintain."),
         "src": two("Deputy Archibald MacGregor to Arthur, American Distillation (RDR2, chapter 3)",
                    "L'adjoint Archibald MacGregor à Arthur, American Distillation (RDR2, chapitre 3). Traduction : « Sans compter que Catherine Braithwaite a une passion plutôt... coûteuse pour les pur-sang à entretenir. »")},
        {"q": two("That hag and her inbred sons... they've ruined this county. They killed my uncle, you know.",
                  "That hag and her inbred sons... they've ruined this county. They killed my uncle, you know."),
         "src": two("[[tavish-gray|Tavish Gray]] to Arthur and John, Horse Flesh for Dinner (RDR2, chapter 3)",
                    "[[tavish-gray|Tavish Gray]] à Arthur et John, Horse Flesh for Dinner (RDR2, chapitre 3). Traduction : « Cette vieille sorcière et ses fils dégénérés... ils ont ruiné ce comté. Ils ont tué mon oncle, vous savez. »")},
        {"q": two("Ain't childbirth just the most beautiful miracle? Seems a lady can birth monkeys after all.",
                  "Ain't childbirth just the most beautiful miracle? Seems a lady can birth monkeys after all."),
         "src": two("Hosea, replying to Bartholomew's insult in front of Catherine, The Fine Joys of Tobacco (RDR2, chapter 3)",
                    "Hosea, en réponse à l'insulte de Bartholomew, devant Catherine, The Fine Joys of Tobacco (RDR2, chapitre 3). Traduction : « La naissance, quel miracle merveilleux, n'est-ce pas ? Il semble qu'une dame puisse bel et bien mettre des singes au monde. »")},
        {"q": two("Do you think that woman set us up?", "Do you think that woman set us up?"),
         "src": two("Arthur to Hosea after the saloon shootout, Advertising, The New American Art (RDR2, chapter 3)",
                    "Arthur à Hosea après la fusillade du saloon, Advertising, The New American Art (RDR2, chapitre 3). Traduction : « Tu crois que cette femme nous a piégés ? »")},
        {"q": two("I guess that's the end of the goddamn cribbage game.", "I guess that's the end of the goddamn cribbage game."),
         "src": two("Hosea, as the manor is set on fire, Blood Feuds, Ancient and Modern (RDR2, chapter 3)",
                    "Hosea, pendant que le manoir est incendié, Blood Feuds, Ancient and Modern (RDR2, chapitre 3). Traduction : « J'imagine que c'est la fin de cette fichue partie de cribbage. »")},
        {"q": two("I told you she was crazy.", "I told you she was crazy."),
         "src": two("Hosea, as the gang leaves Catherine in front of her burning house, Blood Feuds, Ancient and Modern (RDR2, chapter 3)",
                    "Hosea, au moment où la bande abandonne Catherine devant sa maison en flammes, Blood Feuds, Ancient and Modern (RDR2, chapitre 3). Traduction : « Je t'avais dit qu'elle était folle. »")},
        {"q": two("Found a crazy young woman, real strange looking. Locked in a kind of outhouse, hidden on Braithwaite Manor. World ain't a kind place to folk like her.",
                  "Found a crazy young woman, real strange looking. Locked in a kind of outhouse, hidden on Braithwaite Manor. World ain't a kind place to folk like her."),
         "src": two("Arthur's journal, on finding Catherine's daughter (RDR2; caption on the Red Dead Wiki's Gertrude Braithwaite page)",
                    "Journal d'Arthur, après la découverte de la fille de Catherine (RDR2 ; légende de la page Gertrude Braithwaite du Red Dead Wiki). Traduction : « Trouvé une jeune femme folle, à l'allure vraiment étrange. Enfermée dans une sorte de cabanon, cachée sur le domaine Braithwaite. Le monde n'est pas tendre avec les gens comme elle. »")},
        {"q": two("You know, sometimes people here still talk about the brutal demise of the Grays and the Braithwaites. I just smile and keep quiet.",
                  "You know, sometimes people here still talk about the brutal demise of the Grays and the Braithwaites. I just smile and keep quiet."),
         "src": two("[[simon-pearson|Simon Pearson]] to John Marston in his Rhodes store (RDR2, 1907 epilogue; quote list of his Red Dead Wiki page)",
                    "[[simon-pearson|Simon Pearson]] à John Marston, dans son magasin de Rhodes (RDR2, épilogue de 1907 ; liste de citations de sa page du Red Dead Wiki). Traduction : « Vous savez, les gens d'ici parlent encore parfois de la fin brutale des Gray et des Braithwaite. Moi, je souris et je me tais. »")},
    ]},
]


BLOCKS_TRIVIA = [
    {"h3": two("Trivia", "Anecdotes")},
    {"ul": [
        two("A unique item, Catherine's brooch, can be looted from her body in the ruins of the manor and sold to a fence.",
            "Un objet unique, la broche de Catherine, peut être récupéré sur son corps dans les ruines du manoir et revendu à un receleur."),
        two("According to the Red Dead Wiki, a lockbox holding a gold bar can be found under a wall in the room east of Catherine's body, from chapter 4 onward.",
            "Selon le Red Dead Wiki, un coffret contenant un lingot d'or se trouve sous un mur, dans la pièce située à l'est du corps de Catherine, à partir du chapitre 4."),
        two("Her letter to Angelo Bronte is a missable document: it can only be picked up during \"Blood Feuds, Ancient and Modern\", from the nightstand in the room that also holds a Gold Shield.",
            "Sa lettre à Angelo Bronte est un document manquable : on ne peut la ramasser que pendant \"Blood Feuds, Ancient and Modern\", sur la table de nuit de la pièce où se trouve aussi un Gold Shield."),
        two("Killing Catherine before her scripted death fails \"Blood Feuds, Ancient and Modern\".",
            "Tuer Catherine avant sa mort scénarisée fait échouer \"Blood Feuds, Ancient and Modern\"."),
        two("According to the Red Dead Wiki, Gareth originally appeared twice during the raid while Bartholomew was missing; this was later fixed, and Bartholomew now appears at the front of the house, but his subtitles still read \"Gareth\", and his body is labeled Bartholomew when looted.",
            "Selon le Red Dead Wiki, Gareth apparaissait à l'origine deux fois pendant l'assaut, tandis que Bartholomew manquait à l'appel ; le problème a depuis été corrigé et Bartholomew se tient désormais devant la maison, mais ses sous-titres indiquent toujours \"Gareth\", et son corps porte le nom de Bartholomew quand on le fouille."),
        two("Smoke from the burning manor can still be seen in the sky when Arthur and John ride out to Shady Belle in \"The Battle of Shady Belle\", according to the Red Dead Wiki.",
            "La fumée du manoir en flammes est encore visible dans le ciel quand Arthur et John partent pour Shady Belle dans \"The Battle of Shady Belle\", selon le Red Dead Wiki."),
        two("Gertrude's outhouse is the point of interest called \"Braithwaites' Secret\". Only Arthur can record it: John can visit it in the epilogue but cannot mark it, according to the Red Dead Wiki.",
            "Les latrines de Gertrude correspondent au point d'intérêt appelé \"Braithwaites' Secret\". Seul Arthur peut le consigner : John peut s'y rendre pendant l'épilogue mais pas le marquer, selon le Red Dead Wiki."),
        two("The graves of Lucille Braithwaite and Douglas Gray, the two lovers the Red Dead Wiki places at the origin of the feud, can be found in the Rhodes cemetery.",
            "Les tombes de Lucille Braithwaite et de Douglas Gray, les deux amants que le Red Dead Wiki place à l'origine de la querelle, se trouvent dans le cimetière de Rhodes."),
        two("The Red Dead Wiki compares Braithwaite Manor to two Louisiana plantation houses, Oak Alley and Houmas House. Braithwaite is also the name of a village in Cumbria, England.",
            "Le Red Dead Wiki rapproche Braithwaite Manor de deux maisons de plantation de Louisiane, Oak Alley et Houmas House. Braithwaite est aussi le nom d'un village du Cumbria, en Angleterre."),
        two("The score of Red Dead Redemption 2 includes a two-part piece named after \"Blood Feuds, Ancient and Modern\": part I plays as the gang moves on the manor, part II during the assault and its aftermath.",
            "La bande originale de Red Dead Redemption 2 comprend un morceau en deux parties qui porte le nom de \"Blood Feuds, Ancient and Modern\" : la première accompagne l'approche du manoir, la seconde l'assaut et ce qui suit."),
    ]},
]


BLOCKS_MEDIA = [
    {"h3": two("Other media and legacy", "Autres médias et postérité")},
    {"h4": two("Marketing", "Promotion")},
    {"p": two("The second trailer of Red Dead Redemption 2, released on September 28, 2017, includes a shot of Arthur, Hosea and Bill walking away from the burning Braithwaite Manor. According to the mission page, Catherine's screams can be heard in the background.",
              "La deuxième bande-annonce de Red Dead Redemption 2, publiée le 28 septembre 2017, montre Arthur, Hosea et Bill s'éloignant de Braithwaite Manor en flammes. Selon la page de la mission, on entend les cris de Catherine en arrière-plan.")},
    {"h4": two("Red Dead Online", "Red Dead Online")},
    {"p": two("Catherine does not appear in Red Dead Online, whose story is set in 1898, but she is mentioned there. [[josiah-trelawny|Josiah Trelawny]], one of the strangers who give free roam missions, asks the player to steal a horse belonging to her and deliver it to his contact at Hill Haven Ranch, in Scarlett Meadows. Her family plays a larger part in the Moonshiners update, released on December 13, 2019. In its story missions, the bootlegger Maggie Fike and the player take on the Braithwaites' moonshine business. Bartholomew Braithwaite and the cook Danny-Lee Caton confront the player at the moonshine shack, and Bartholomew later escapes the revenue agent Reid Hixon with a 100-dollar bribe, leaving Danny-Lee to be arrested.",
              "Catherine n'apparaît pas dans Red Dead Online, dont l'histoire se déroule en 1898, mais elle y est mentionnée. [[josiah-trelawny|Josiah Trelawny]], l'un des inconnus qui proposent des missions en exploration libre, demande au joueur de voler un cheval qui lui appartient et de le livrer à son contact au ranch Hill Haven, dans les Scarlett Meadows. Sa famille tient un rôle plus important dans la mise à jour Moonshiners, sortie le 13 décembre 2019. Dans ses missions scénarisées, la bouilleuse clandestine Maggie Fike et le joueur s'attaquent au commerce d'alcool des Braithwaite. Bartholomew Braithwaite et le cuisinier Danny-Lee Caton viennent intimider le joueur jusque dans sa cabane de bouilleur, puis Bartholomew échappe à l'agent du fisc Reid Hixon en lui glissant un pot-de-vin de 100 dollars, et laisse arrêter Danny-Lee.")},
]
