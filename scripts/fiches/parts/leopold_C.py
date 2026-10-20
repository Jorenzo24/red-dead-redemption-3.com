"""Leopold Strauss, reference fiche, PART C: Missions, Quotes, Trivia, Other media.

Sources (internal register, fetched Oct 2026 via the MediaWiki API, saved in scratchpad cov/leopold/ and cov/leopold/m/):
- Red Dead Wiki EN "Leopold Strauss" (Mission Appearances: 19 entries; Quotes; Trivia) and FR "Leopold Strauss"
  (fr.txt: Apparitions dans les missions, 12 entries, which leave out Money Lending IV to VII, Sodom? Back to Gomorrah,
  Blood Feuds and The Battle of Shady Belle).
- Mission pages: Outlaws from the West; Enter, Pursued by a Memory; Eastward Bound (trivia: no new camp dialogue);
  Money Lending and Other Sins I & II (rewards 119 dollars, ledger), III, IV, V (reward 10 dollars, trivia), VI & VII
  (rewards, trivia: following Strauss after the exile, honor loss); The Sheep and the Goats (failure conditions,
  trivia: captor glitch, Dutch's impatience); A Strange Kindness; Sodom? Back to Gomorrah; Blood Feuds, Ancient and
  Modern; The Battle of Shady Belle; A Fine Night of Debauchery (Gold Medal objective, trivia: wine bottle, honor);
  Horsemen, Apocalypses (gallery caption); Fleeting Joy; That's Murfree Country; Bare Knuckle Friendships. Wiki page
  "Camp Events" (cov/hosea/m/Camp_Events.txt: Edith Downes's visit; Strauss unavailable while the money-lending and
  riverboat missions are open).
- Transcripts "/dialogues" used for every quotation below: Money Lending and Other Sins I & II, III, IV; Sodom? Back
  to Gomorrah; Eastward Bound. The wiki has no transcript for The Sheep and the Goats, A Fine Night of Debauchery or
  Money Lending and Other Sins VI & VII (checked Oct 2026): the three lines from those missions come from the quote
  list of the character page, as in kieran_C and sean_C.
- Real world: Rockstar's series of character portraits and descriptions posted on Twitter on September 6, 2018 and
  reproduced by The Hollywood Reporter the next day (../uncle/fc/thr_descriptions.txt: Strauss is included);
  Wikipedia "List of Red Dead Redemption 2 characters" (../abigail/m/wp_list.txt: composite of the 23 gang members,
  front row, between Jack and Trelawny); the official guide's biography (cov/leopold/fc/bio*.png).
Ownership (FIX_RULES), left to other parts: backstory, mission events, the alternative departure, the epilogue news,
the missing grave (A); personality, the official descriptions quoted word for word, names and what others call him
("the German", "Prussian", "Herr Strauss"), appearance, camp scenes and camp lines (Anna and his brother, Australia,
"a nasty world", Micah, Swanson, Bill, Hosea and the coffee, the party, the reactions to the exile), his illness line
to Arthur and his reply on the poker table if B quotes them (B); Howard Pinhasik, concept art, development (D).
Quotes: each line in ONE place; part A paraphrases them without quotation marks. Arthur's "You and me, we ain't
decent" is quoted in the Arthur fiche and is not repeated here. Camp lines from the wiki quote list ("Australia",
"By the age of twelve", "nasty world", "Your commitment to your duties") are left to part B.
Kills: the wiki credits him with none; the guard he can hit with a bottle in "A Fine Night of Debauchery" only
"possibly" dies (mission page), so there is no kills table.
Excluded: the Leo Strauss name origin and the Jewish identity discussion (speculation); the "vultures" allegory of
Money Lending III (interpretation); the FR wiki's resemblance to Friedrich Steiner of Call of Duty: Black Ops
(opinion) and its "redemption" reading (interpretation); Dutch never commenting on the exile (absence claim); the
list of other gang members with off-screen deaths or no grave (comparison with characters outside this fiche).
"""


def two(en, fr): return {"en": en, "fr": fr}


M = lambda mission, chap, en, fr: [mission, chap, two(en, fr)]

C1 = two("1. Colter", "1. Colter")
C2 = two("2. Horseshoe Overlook", "2. Horseshoe Overlook")
C3 = two("3. Clemens Point", "3. Clemens Point")
C4 = two("4. Saint Denis", "4. Saint-Denis")
C5 = two("5. Guarma", "5. Guarma")
C6 = two("6. Beaver Hollow", "6. Beaver Hollow")
E2 = two("Epilogue 2", "Épilogue 2")


BLOCKS_MISSIONS = [
    {"h3": two("Missions", "Missions")},
    {"p": two("The English Red Dead Wiki lists 19 story missions of Red Dead Redemption 2 for Strauss, seven of them in the \"Money Lending and Other Sins\" strand he gives to Arthur. The French Red Dead Wiki lists 12. The table below follows the English list and adds the epilogue mission in which his death is reported.",
              "Le Red Dead Wiki anglais recense pour Strauss 19 missions principales de Red Dead Redemption 2, dont sept dans la série \"Money Lending and Other Sins\" qu'il confie à Arthur. Le Red Dead Wiki français en compte 12. Le tableau ci-dessous suit la liste anglaise et y ajoute la mission de l'épilogue où l'on apprend sa mort.")},
    {"table": {"head": [two("Mission", "Mission"), two("Chapter", "Chapitre"), two("Strauss's role", "Rôle de Strauss")], "rows": [
        M("Outlaws from the West", C1,
          "Listed by the wiki for the gang's flight from Blackwater into the mountains. Neither the mission page nor the transcript names him.",
          "Citée par le wiki pour la fuite de la bande depuis Blackwater jusque dans les montagnes. Ni la page de la mission ni la transcription ne le nomment."),
        M("Enter, Pursued by a Memory", C1,
          "At camp with [[hosea-matthews|Hosea]] when [[arthur-morgan|Arthur]] and [[javier-escuella|Javier]] bring back [[john-marston|John]].",
          "Au camp avec [[hosea-matthews|Hosea]] quand [[arthur-morgan|Arthur]] et [[javier-escuella|Javier]] ramènent [[john-marston|John]]."),
        M("Eastward Bound", C1,
          "Arrives at Horseshoe Overlook with the gang and leaves for Valentine to start lending money.",
          "Arrive à Horseshoe Overlook avec la bande et part pour Valentine prêter de l'argent."),
        M("Money Lending and Other Sins I", C2,
          "Mission giver. Hands Arthur three debtors: Chick Matthews, Mr. Wróbel and Lilly Millet.",
          "Donneur de la mission. Confie trois débiteurs à Arthur : Chick Matthews, M. Wróbel et Lilly Millet."),
        M("Money Lending and Other Sins II", C2,
          "Mission giver. Arthur collects the three debts; the first deposit opens the camp ledger. Reward for parts I and II: 119 dollars.",
          "Donneur de la mission. Arthur recouvre les trois dettes ; le premier dépôt donne accès au registre du camp. Récompense pour les parties I et II : 119 dollars."),
        M("Money Lending and Other Sins III", C2,
          "Mission giver. Sends Arthur to Thomas Downes, who coughs blood into Arthur's face. Required to advance the story.",
          "Donneur de la mission. Envoie Arthur chez Thomas Downes, qui lui crache du sang au visage. Obligatoire pour faire avancer l'histoire."),
        M("The Sheep and the Goats", C2,
          "Taken hostage with John by [[leviticus-cornwall|Cornwall]]'s men outside Keane's Saloon, then shot in the leg during the escape from Valentine.",
          "Pris en otage avec John par les hommes de [[leviticus-cornwall|Cornwall]] devant le Keane's Saloon, puis blessé à la jambe pendant la fuite de Valentine."),
        M("A Strange Kindness", C2,
          "Moves with the gang to Clemens Point.",
          "Suit la bande à Clemens Point."),
        M("Money Lending and Other Sins IV", C3,
          "Mission giver. Hands Arthur two debtors: Winton Holmes, killed by the white cougar he was hunting, and Gwyn Hughes, who pays with a dead woman's brooch.",
          "Donneur de la mission. Confie deux débiteurs à Arthur : Winton Holmes, tué par le puma blanc qu'il chassait, et Gwyn Hughes, qui paie avec la broche d'une morte."),
        M("Sodom? Back to Gomorrah", C3,
          "Tells Arthur that Thomas Downes has died and that his widow, Edith, owes the debt. Arthur collects it after the bank robbery.",
          "Annonce à Arthur la mort de Thomas Downes et précise que sa veuve, Edith, doit reprendre la dette. Arthur la recouvre après le braquage."),
        M("Blood Feuds, Ancient and Modern", C3,
          "Listed by the English wiki only; the mission page does not mention him.",
          "Citée par le seul wiki anglais ; la page de la mission ne le mentionne pas."),
        M("The Battle of Shady Belle", C3,
          "Listed by the English wiki only. The gang refuses the deal [[andrew-milton|Milton]] offers at Clemens Point and moves to Shady Belle.",
          "Citée par le seul wiki anglais. La bande refuse le marché que [[andrew-milton|Milton]] propose à Clemens Point et s'installe à Shady Belle."),
        M("Money Lending and Other Sins V", C4,
          "Mission giver. Sends Arthur to Algie Davison at Catfish Jacksons. Reward for the player: 10 dollars.",
          "Donneur de la mission. Envoie Arthur chez Algie Davison, à Catfish Jacksons. Récompense pour le joueur : 10 dollars."),
        M("A Fine Night of Debauchery", C4,
          "Boards the Grand Korrigan with Arthur, Javier and [[josiah-trelawny|Trelawny]], signals Arthur's play at the poker table, escapes by swimming ashore and confirms the value of Blythe's watch.",
          "Monte à bord du Grand Korrigan avec Arthur, Javier et [[josiah-trelawny|Trelawny]], indique à Arthur comment jouer au poker, s'échappe à la nage et confirme la valeur de la montre de Blythe."),
        M("Horsemen, Apocalypses", C4,
          "Takes cover inside the Shady Belle house during the O'Driscoll attack.",
          "S'abrite dans la maison de Shady Belle pendant l'attaque des O'Driscoll."),
        M("Fleeting Joy", C5,
          "At Lakay, tells [[dutch-van-der-linde|Dutch]] that the group owes its survival mostly to [[sadie-adler|Sadie]].",
          "À Lakay, explique à [[dutch-van-der-linde|Dutch]] que le groupe doit surtout sa survie à [[sadie-adler|Sadie]]."),
        M("That's Murfree Country", C5,
          "Moves with the gang to Beaver Hollow.",
          "Suit la bande à Beaver Hollow."),
        M("Money Lending and Other Sins VI", C6,
          "Mission giver. Hands Arthur his last two debtors, J. John Weathers and Arthur Londonderry. Reward for the player: honor, and a silver locket if Arthur takes it from Weathers.",
          "Donneur de la mission. Confie à Arthur ses deux derniers débiteurs, J. John Weathers et Arthur Londonderry. Récompense pour le joueur : de l'honneur, et un médaillon en argent si Arthur l'accepte de Weathers."),
        M("Money Lending and Other Sins VII", C6,
          "Thrown out of the gang by Arthur, who packs his bag and throws money at him.",
          "Chassé de la bande par Arthur, qui fait son sac et lui jette de l'argent."),
        M("Bare Knuckle Friendships", E2,
          "Mentioned. [[charles-smith|Charles]] tells John that Strauss died in Pinkerton custody without giving up the gang.",
          "Mentionné. [[charles-smith|Charles]] apprend à John que Strauss est mort aux mains de la Pinkerton sans rien livrer sur la bande."),
    ]}},
]


BLOCKS_QUOTES = [
    {"h3": two("Quotes", "Citations")},
    {"p": two("The lines below are given as spoken in the game, in the original English, with the mission and the person addressed; [...] marks a cut.",
              "Les répliques ci-dessous sont reproduites telles qu'elles sont prononcées dans le jeu, en anglais, avec la mission et la personne à qui elles s'adressent ; [...] signale une coupe.")},
    {"h4": two("The money-lending business", "Le commerce de l'usure")},
    {"quotes": [
        {"q": two("Herr Morgan, Herr Morgan. [...] Busy, my friend?", "Herr Morgan, Herr Morgan. [...] Busy, my friend?"),
         "src": two("Money Lending and Other Sins I (RDR2, chapter 2), to Arthur, who answers \"Mr. Strauss.\" between the two lines, before Strauss offers him a cut",
                    "Money Lending and Other Sins I (RDR2, chapitre 2), à Arthur, qui répond \"Mr. Strauss.\" entre les deux phrases, avant que Strauss ne lui propose une part. Traduction : « Herr Morgan, Herr Morgan. [...] Vous êtes occupé, mon ami ? »")},
        {"q": two("You know how it is... people is happy to borrow off someone like me, but... more enthusiastic paying back to someone like you.", "You know how it is... people is happy to borrow off someone like me, but... more enthusiastic paying back to someone like you."),
         "src": two("Money Lending and Other Sins I (RDR2, chapter 2), to Arthur, who asks whether he is lending already",
                    "Money Lending and Other Sins I (RDR2, chapitre 2), à Arthur, qui s'étonne qu'il prête déjà. Traduction : « Vous savez ce que c'est... les gens empruntent volontiers à quelqu'un comme moi, mais... ils remboursent avec plus d'entrain quelqu'un comme vous. »")},
        {"q": two("Put the debts in the deed box and try not to kill them... it's very bad for business.", "Put the debts in the deed box and try not to kill them... it's very bad for business."),
         "src": two("Money Lending and Other Sins I (RDR2, chapter 2), to Arthur",
                    "Money Lending and Other Sins I (RDR2, chapitre 2), à Arthur. Traduction : « Mettez l'argent dans la caisse et tâchez de ne pas les tuer... c'est très mauvais pour les affaires. »")},
        {"q": two("He's more slippery than he seems. I've tried being polite... don't take any nonsense.", "He's more slippery than he seems. I've tried being polite... don't take any nonsense."),
         "src": two("Money Lending and Other Sins III (RDR2, chapter 2), to Arthur, about Thomas Downes",
                    "Money Lending and Other Sins III (RDR2, chapitre 2), à Arthur, à propos de Thomas Downes. Traduction : « Il est plus retors qu'il n'en a l'air. J'ai essayé la politesse... ne vous laissez pas faire. »")},
        {"q": two("Well, it turns out the pursuit of freedom... is not a cheap business. Not for us... and not for some of the locals.", "Well, it turns out the pursuit of freedom... is not a cheap business. Not for us... and not for some of the locals."),
         "src": two("Money Lending and Other Sins IV (RDR2, chapter 3), to Arthur at Clemens Point",
                    "Money Lending and Other Sins IV (RDR2, chapitre 3), à Arthur, à Clemens Point. Traduction : « Eh bien, il se trouve que la quête de la liberté... n'est pas bon marché. Ni pour nous... ni pour certains habitants du coin. »")},
        {"q": two("With enough encouragement... both of them.", "With enough encouragement... both of them."),
         "src": two("Money Lending and Other Sins IV (RDR2, chapter 3), when Arthur asks how many of the two debtors will be able to pay",
                    "Money Lending and Other Sins IV (RDR2, chapitre 3), quand Arthur demande combien des deux débiteurs pourront payer. Traduction : « Avec assez d'encouragements... les deux. »")},
        {"q": two("That man, the debtor, Thomas Downes... apparently he's dead.", "That man, the debtor, Thomas Downes... apparently he's dead."),
         "src": two("Sodom? Back to Gomorrah (RDR2, chapter 3), to Arthur, who answers that Downes did not seem very well",
                    "Sodom? Back to Gomorrah (RDR2, chapitre 3), à Arthur, qui répond que Downes n'avait pas l'air bien. Traduction : « Cet homme, le débiteur, Thomas Downes... il est mort, apparemment. »")},
        {"q": two("His wife... I believe he has a wife and child. She will assume the debt of course.", "His wife... I believe he has a wife and child. She will assume the debt of course."),
         "src": two("Sodom? Back to Gomorrah (RDR2, chapter 3), to Arthur, just before the Valentine bank robbery",
                    "Sodom? Back to Gomorrah (RDR2, chapitre 3), à Arthur, juste avant le braquage de la banque de Valentine. Traduction : « Sa femme... je crois qu'il a une femme et un enfant. C'est elle qui reprendra la dette, bien entendu. »")},
    ]},
    {"h4": two("Elsewhere in the story", "Ailleurs dans l'histoire")},
    {"quotes": [
        {"q": two("Gentlemen, I'm going to head into the local town, and you know... see if I can strike up a little business.", "Gentlemen, I'm going to head into the local town, and you know... see if I can strike up a little business."),
         "src": two("Eastward Bound (RDR2, chapter 1), to Dutch, Hosea and Arthur at Horseshoe Overlook",
                    "Eastward Bound (RDR2, chapitre 1), à Dutch, Hosea et Arthur, à Horseshoe Overlook. Traduction : « Messieurs, je vais faire un tour en ville et, vous savez... voir si je peux lancer quelques affaires. »")},
        {"q": two("I don't believe in absolutes, just shades of gray. Compromises.", "I don't believe in absolutes, just shades of gray. Compromises."),
         "src": two("The Sheep and the Goats (RDR2, chapter 2), to Dutch (quote list of the Red Dead Wiki)",
                    "The Sheep and the Goats (RDR2, chapitre 2), à Dutch (liste de citations du Red Dead Wiki). Traduction : « Je ne crois pas aux absolus, seulement aux nuances de gris. Aux compromis. »")},
        {"q": two("Nice watch. Yes, it's a Reutlinger alright.", "Nice watch. Yes, it's a Reutlinger alright."),
         "src": two("A Fine Night of Debauchery (RDR2, chapter 4), on the riverbank, about Blythe's watch (quote list of the Red Dead Wiki)",
                    "A Fine Night of Debauchery (RDR2, chapitre 4), sur la berge, à propos de la montre de Blythe (liste de citations du Red Dead Wiki). Traduction : « Belle montre. Oui, c'est bien une Reutlinger. »")},
        {"q": two("You know... they-they say the sick delude themselves. I was your friend.", "You know... they-they say the sick delude themselves. I was your friend."),
         "src": two("Money Lending and Other Sins VII (RDR2, chapter 6), to Arthur, who is throwing him out (quote list of the Red Dead Wiki)",
                    "Money Lending and Other Sins VII (RDR2, chapitre 6), à Arthur, qui le chasse (liste de citations du Red Dead Wiki). Traduction : « Vous savez... on-on dit que les malades se font des illusions. J'étais votre ami. »")},
    ]},
    {"h4": two("Said about him", "Ce qu'on dit de lui")},
    {"quotes": [
        {"q": two("I prefer robbing banks to usury... seems more dignified somehow.", "I prefer robbing banks to usury... seems more dignified somehow."),
         "src": two("Dutch van der Linde, Eastward Bound (RDR2, chapter 1), as Strauss leaves for Valentine",
                    "Dutch van der Linde, Eastward Bound (RDR2, chapitre 1), quand Strauss part pour Valentine. Traduction : « Je préfère braquer des banques que faire de l'usure... ça me paraît plus digne, en un sens. »")},
        {"q": two("And Strauss came back with that creepy little smile on his face. I'm sure there's a whole list of unfortunates... he's forced money upon.", "And Strauss came back with that creepy little smile on his face. I'm sure there's a whole list of unfortunates... he's forced money upon."),
         "src": two("Hosea Matthews to Arthur, Eastward Bound (RDR2, chapter 1)",
                    "Hosea Matthews à Arthur, Eastward Bound (RDR2, chapitre 1). Traduction : « Et Strauss est revenu avec son petit sourire inquiétant. Je suis sûr qu'il y a déjà toute une liste de malheureux... à qui il a fourgué de l'argent. »")},
    ]},
]


BLOCKS_TRIVIA = [
    {"h3": two("Trivia", "Anecdotes")},
    {"ul": [
        two("After \"Eastward Bound\", Strauss and Uncle, who is asleep, are the only people in camp with no new dialogue.",
            "Après \"Eastward Bound\", Strauss et Uncle, endormi, sont les seuls au camp à n'avoir aucun nouveau dialogue."),
        two("According to the Red Dead Wiki's camp events page, Strauss's camp events do not play while \"Money Lending and Other Sins I & II\" is available, nor, like those of Javier and Trelawny, while \"A Fine Night of Debauchery\" is available.",
            "D'après la page du Red Dead Wiki consacrée aux événements de camp, les scènes de camp de Strauss ne se déclenchent pas tant que \"Money Lending and Other Sins I & II\" est disponible, ni, comme celles de Javier et de Trelawny, tant que \"A Fine Night of Debauchery\" l'est."),
        two("In \"The Sheep and the Goats\", the mission fails if Arthur waits too long to shoot the men holding John and Strauss: Dutch loses patience, and both hostages are killed. If Arthur shoots Strauss's captor in the head, the man does not fall, and Strauss still wrestles the gun out of his hand.",
            "Dans \"The Sheep and the Goats\", la mission échoue si Arthur tarde trop à tirer sur les hommes qui tiennent John et Strauss : Dutch perd patience, et les deux otages sont tués. Si Arthur tire dans la tête de l'homme qui tient Strauss, celui-ci ne tombe pas, et Strauss lui arrache quand même son arme."),
        two("According to the character page, while \"The Sheep and the Goats\" is still open, Strauss and Dutch may come out and fire on anyone attacking Arthur near the mission marker in Valentine, such as bounty hunters.",
            "D'après la page du personnage, tant que \"The Sheep and the Goats\" n'est pas terminée, Strauss et Dutch peuvent sortir tirer sur quiconque attaque Arthur près du point de départ de la mission à Valentine, des chasseurs de primes par exemple."),
        two("One of the Gold Medal objectives of \"A Fine Night of Debauchery\" is to win the poker game without Strauss's help. If Arthur shoots the guard that Strauss can knock out with a bottle before Strauss reaches him, the player loses honor.",
            "L'un des objectifs de médaille d'or de \"A Fine Night of Debauchery\" consiste à gagner la partie de poker sans l'aide de Strauss. Si Arthur abat le garde que Strauss peut assommer d'un coup de bouteille avant que Strauss ne l'atteigne, le joueur perd de l'honneur."),
        two("According to the mission page of \"Money Lending and Other Sins VII\", if Arthur follows Strauss as he leaves, Strauss and his horse vanish and leave his bag behind; a player who is fast enough, or uses mods, can kill him, which costs half of the player's honor.",
            "D'après la page de la mission \"Money Lending and Other Sins VII\", si Arthur suit Strauss quand il s'en va, Strauss et son cheval disparaissent en laissant son sac ; un joueur assez rapide, ou qui utilise des mods, peut le tuer, ce qui lui coûte la moitié de son honneur."),
        two("Parts I to III of \"Money Lending and Other Sins\" are not optional, but completing them unlocks the rest of the strand. According to the mission pages, the later parts are optional honor story missions and count toward the Lending a Hand trophy, which requires completing every optional honor story mission in the game.",
            "Les trois premières parties de \"Money Lending and Other Sins\" ne sont pas facultatives, mais les terminer débloque la suite de la série. D'après les pages des missions, les parties suivantes sont des missions d'honneur facultatives et comptent pour le trophée Lending a Hand, qui exige de terminer toutes les missions d'honneur facultatives du jeu."),
    ]},
]


BLOCKS_MEDIA = [
    {"h3": two("Other media and legacy", "Autres médias et postérité")},
    {"h4": two("Marketing", "Promotion")},
    {"p": two("On September 6, 2018, Rockstar posted Strauss's portrait and character description on Twitter, in a series covering the members of the gang, and The Hollywood Reporter reproduced the series the next day. In the composite image of the 23 gang members that illustrates Wikipedia's list of the game's characters, Strauss stands in the front row, between Jack and Trelawny.",
              "Le 6 septembre 2018, Rockstar publie sur Twitter le portrait et la description de Strauss, dans une série consacrée aux membres de la bande, et The Hollywood Reporter reprend la série le lendemain. Sur l'image des 23 membres de la bande qui illustre la liste des personnages du jeu sur Wikipédia, Strauss figure au premier rang, entre Jack et Trelawny.")},
]
