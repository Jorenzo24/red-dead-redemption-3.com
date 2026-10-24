# Adversarial fact-check: RDR2 Chapter 1 mission pages (24 Oct 2026)

Scope: the 6 EN pages missions/<slug>/index.html (every sentence) + FR spot-check (facts grid, Choices, Gold, Trivia, intros).
Sources used: wiki mission pages and transcripts in scripts/v3/work/_m/ (cited as `<Mission>.txt:line`, `<Mission>_dialogues.txt:line`),
story-ch1/fc/gsw.txt, scripts/v3/sources/Camp_Events.txt, HOUSE_FACTS.md, the fact-checked Chapter 1 guide.

Overall: no WRONG fact on the story side; story text matches the guide and the transcripts (all quoted lines checked verbatim,
including the new ones: "Mind away, Reverend", "Of course I do, but... look at you", "Least we all know you can read",
"a raised spot there that should give us good vantage", "You sure you're ready for this, kid?", "the poor bastard was married too",
"If we can't eat it or drink it, put it down", "Do I get to skin you?", "they always said you were a butcher", "Oh, whatever you say, son",
"this is a real bad day for you, Kieran Duffy", "a long way from our dream of virgin land in the west", the journal entries).
Gold Medal objectives, rewards, failure conditions and trophies match the wiki pages on all six pages. Prev/next chain is
consistent (Outlaws > Enter > Aftermath > Old Friends > Cornwall > Eastward > Who is Not Without Sin, as documented in the data
docstrings). No dashes, no « » in headings, all character links point to live fiches. FR says the same facts as EN except where noted.
The problems below are mostly duplication and a few unsupported details in the NEW material.

## Outlaws from the West

1. IMPRECISE. Trivia: "Charles's mare Taima is the only gang member's horse the player rides in a mission, according to the mission page."
   Source: Outlaws_from_the_West.txt:122 "the only mission in the game when a gang member's horse (Taima) is **intended** to be ridden".
   Fix: "...is the only gang member's horse the game intends the player to ride in a mission, according to the mission page." (FR idem: "le seul cheval ... que le jeu fait monter au joueur").
   Field: `sections.trivia` (rdr2_outlaws_from_the_west.py:231), EN+FR. (Same sentence in the guide's Trivia; fix there too if wanted.)
2. DUPLICATE. "Arthur or Micah fires first" is in Story ("The shootout at the Adler Ranch") and again as the first sentence of Choices > "The shootout and the search" ("Arthur or Micah fires the first shot.").
   Fix: drop the first sentence of the Choices paragraph; start at "According to the Red Dead Wiki, if Arthur does not shoot...".
   Field: `sections.choices`, paragraph at rdr2_outlaws_from_the_west.py:154, EN+FR.
3. DUPLICATE (structural, applies to every page). All 8 entries of the Quotes block are already quoted verbatim in Story (Hosea "If we don't stop soon...", "Stay strong...", "He's the last one...", "One lonely man...", "It's goddamn Dutch...", "Wanting Colm dead...", "We're bad men...", "They turned her into a widow..."). Trivia 1 repeats the Hosea line a third time.
   Fix (editorial decision): either keep the Quotes block as a deliberate recap (then say so in DATA-SCHEMA §4) or fill it with lines NOT used in the story (candidates, all verbatim in Outlaws_from_the_West_dialogues.txt: "Can't believe we lost Davey too." l.130; "Davey was a real fighter. Both of them Callander boys is, or... was." l.189; "Didn't see much of anything once this storm came in." l.207; "Well, he started it!" l.395; "Get the hell outta here. Go." l.431).
   Field: `quotes` (rdr2_outlaws_from_the_west.py:193).

Checked and correct (new vs guide): Deaths list (Outlaws_from_the_West.txt:69-76), failure list (:78-86, "his own horse" ok), Gold table (:61-63), trophies (:145-160), map markers (:99), Old Lantern + compendium (:102, :120), invisible wall + horses (:115, :117), wrong-cover remark + Micah shoots (:110-111), horse offered back to Sadie (:119), wedding photo + Dutch's "put it down" (gsw.txt:2708-2709), "(to Abigail)" (gsw.txt:2767), both ride answers (dialogues :144-152), "too many mouths" in the optional branch (:231), spared O'Driscoll line (Old_Friends.txt:96, quoted there by the wiki). Facts grid ok. FR consistent.

## Enter, Pursued by a Memory

1. UNSUPPORTED. Deaths: "The wolves on the slope and on the ride down, killed by Arthur and Javier."
   Source: Enter_Pursued_by_a_Memory_dialogues.txt:367 (Arthur kills the three wolves), :379 (Javier carries John on his own horse), :393-405 (Javier only shouts at the second pack; no line or direction has him shoot). Enter_Pursued_by_a_Memory.txt:34 "Arthur ... distracts and kills the wolves".
   Fix: "The wolves on the slope and on the ride down, killed by Arthur." FR: "abattus par Arthur."
   Field: `sections.story` Deaths list (rdr2_enter_pursued_by_a_memory.py:140), EN+FR.
2. DUPLICATE. The bourbon scene is told twice: Story > "John's horse and the climb" ("If the player does not use provisions on the climb, Javier shares a bottle of Kentucky bourbon with Arthur, according to the mission page.") and Choices > "On the climb" ("...a short scene plays in which Javier gives Arthur a swig of Kentucky bourbon").
   Fix: remove the sentence from the Story paragraph (rdr2_enter_pursued_by_a_memory.py:95); keep the Choices version (it has the stamina-core context, Enter_Pursued_by_a_Memory.txt:75). EN+FR.
3. IMPRECISE. Facts "Next mission: The Aftermath of Genesis", while the wiki infobox lists both "Old Friends" and "The Aftermath of Genesis" as next (Enter_Pursued_by_a_Memory.txt:18) and our own Unlocks cell says either order.
   Fix: keep the link (chain order) but the generated cell could read "The Aftermath of Genesis (or Old Friends, either order)". If the generator cannot qualify prev/next, leave it: the Unlocks cell already carries the nuance. Field: `next` (+ gen_mission rendering), low priority.
4. DUPLICATE (structural). Quotes: "Never thought I'd say this...", "See, I told Dutch...", "That bullet in Blackwater, now this?", "We had the money...", "This is a new low..." are already quoted in Story; "dumb as rocks" is quoted in both. Same decision as Outlaws #3. Field: `quotes` (:188).

Checked and correct: Abigail Roberts note (Enter_Pursued_by_a_Memory.txt:8), Tilly and Mary-Beth at the fireplace (dialogues :7, :11), "little John"/"dumb as rocks" (:27, :31), "on the other side of town" (:117), "idiotas ... his leg" (:459), failure list incl. the Sawed-Off Shotgun replay note (:55, :57-63), trampling, single-shot wolf, unique death scene, revolver remark (:48, :80-82), wolf-bite rule (:51), "Just a Scratch" (:105-111), Northern Grizzlies attributed (:77), avalanche (:76), repaired clothes (:79), camp events (Camp_Events.txt:10-24, correctly attributed to the Camp Events page here). FR consistent except #1 (same error).

## The Aftermath of Genesis

1. DUPLICATE + IMPRECISE. Trivia: "When Arthur asks whether they should take the bear for its meat, Charles says the deer are enough and, according to the mission page, that they could not carry both." Story > "The grizzly" already has the exchange from the transcript ("Arthur notes that it has a lot of meat on it. Charles answers: 'We've got enough here, no need to push our luck.'"), and the two versions disagree on framing (asks vs notes; "could not carry both" is not in the transcript, The_Aftermath_of_Genesis_dialogues.txt:273-275; it is wiki-only, The_Aftermath_of_Genesis.txt:100).
   Fix: delete the trivia bullet; optionally append to the Story sentence: "According to the mission page, Charles also says they could not carry both." Field: `sections.trivia` (rdr2_the_aftermath_of_genesis.py:204), EN+FR.
2. DUPLICATE. Eagle Eye appears four times: Unlocks cell ("Eagle Eye."), Rewards cell ("Eagle Eye ability"), Story ("which introduces Eagle Eye") and Trivia 1 ("The mission unlocks Eagle Eye, but...").
   Fix: remove "Eagle Eye." from `facts.unlocks` (it is a reward on the wiki infobox, The_Aftermath_of_Genesis.txt:16), and shorten Trivia 1 to "The first deer can be tracked by its prints in the snow without Eagle Eye, according to the mission page." Fields: `facts.unlocks` (:67), `sections.trivia` (:200), EN+FR.
3. STYLE. Choices: "Played before Old Friends, the mission leaves Hosea at the butcher's table, where Arthur can have a conversation with him" ("leaves Hosea" reads as if the mission places him; the wiki only says he can be found there, The_Aftermath_of_Genesis.txt:103).
   Fix: "If it is played before Old Friends, Hosea can be found at the butcher's table for a conversation, according to the mission page." FR: "Jouée avant Old Friends, Hosea peut être trouvé près de l'étal du boucher pour une conversation, selon la page de la mission." Field: `sections.choices`, EN+FR.
4. DUPLICATE (structural). Quotes: 7 of 10 entries already quoted in Story ("Enough of this...", "Spring storms...", "Sooner or later...", "And for a feller...", "Twenty years...", "Dutch saved me...", "Do I get to skin you?"). Same decision as Outlaws #3. Field: `quotes` (:166).

Checked and correct: rewards incl. Assorted Salted Offal and 22 arrows (The_Aftermath_of_Genesis.txt:13-16), failure list (:68-74), Gold table (:80-82), Deaths (:77), other weapon / bleeding deer / bear unkillable / shooting the bear (:95-101), order-of-play variants (dialogues :223-245, wiki :102-105), "fattest", "Assorted, salted offal", "miles around", "That's a bad idea", "off the trail", "him and Hosea", "burnt hand", "butcher", "off this mountain alive" (dialogues :19, :51, :77, :283, :293, :333, :417, :425, :433). No cause given for the hand (correct, docstring). FR consistent.

## Old Friends

1. IMPRECISE (order). "Outside, Arthur asks whether a raid is wise ..., and reminds Dutch that he always said revenge is a luxury they cannot afford. Dutch tells him he is doubting him, and answers that the O'Driscolls 'were talking about trains and detonators'..."
   Source: Old_Friends_dialogues.txt:69-75: Dutch's "No, you're just doubting me" comes BEFORE Arthur's "I would never doubt you, Dutch, you always said revenge is a luxury we can't afford".
   Fix: "Outside, Arthur says the gang is barely back on its feet. Dutch tells him he is doubting him. Arthur denies it and reminds Dutch that he always said revenge is a luxury they cannot afford. Dutch answers that the O'Driscolls 'were talking about trains and detonators', and that Colm always had good information." Field: `sections.story` (rdr2_old_friends.py:92), EN+FR.
2. DUPLICATE. Trivia "When the gang watches the hideout from a distance, the man Colm scolds is Kieran, according to the mission page." repeats Story > "Kieran Duffy" ("The man is the one Colm struck."). Fix: delete the trivia bullet (rdr2_old_friends.py:219) or move the attribution into the Story sentence ("...the one Colm struck, according to the mission page" per Old_Friends.txt:100). EN+FR.
3. DUPLICATE. Dead Eye targeting appears in Unlocks, Rewards and Trivia 1 ("The mission unlocks Dead Eye targeting, according to the mission page.").
   Fix: remove "Dead Eye targeting." from `facts.unlocks` (:74; the wiki lists it as a reward, Old_Friends.txt:14) and delete Trivia 1 (:217). EN+FR.
4. IMPRECISE. Facts "Characters": "at camp, Uncle and Hosea Matthews". In the opening scene Dutch also addresses Charles and Pearson, who stay to guard the camp (Old_Friends_dialogues.txt:97-99), and the Story says so.
   Fix: "at camp, Hosea Matthews, Charles Smith, Simon Pearson and Uncle". Field: `facts.characters` (:71), EN+FR.
5. DUPLICATE (structural). Quotes: all 8 entries already quoted in Story. Same decision as Outlaws #3. Field: `quotes` (:189).

Checked and correct: giver/location/rewards (Old_Friends.txt:9-14), Gold table (:49-53), Dead Eye flashing tip (:108), failure list (:63-69), Deaths (:72; Branwen conditional ok), Carbine remark (:94), spared O'Driscoll + interrogation talk (:96-97), Micah's revolver (:98), six markers incl. Hosea (:101), instant death near the borders (:102), Branwen honor/no story effect (:107; "later in the game" = after "Just a Social Call", acceptable), second-wave choice wording (dialogues :302-317), Kieran in the stable (Camp_Events + :104). Annabelle/brother not ordered (house rule respected). FR consistent.

## Who the Hell is Leviticus Cornwall?

1. STYLE. Facts "Started by": "John Marston / Dutch van der Linde on the Red Dead Wiki mission page: the mission starts in John's cabin, where Dutch announces the job" (slash + colon, hard to read).
   Fix: "John Marston and Dutch van der Linde, according to the mission page (it starts in John's cabin, where Dutch announces the job)". FR: "John Marston et Dutch van der Linde, selon la page de la mission (elle commence dans la cabane de John, où Dutch annonce le coup)". Field: `facts.giver` (rdr2_who_the_hell_is_leviticus_cornwall.py:64).
2. IMPRECISE (omission). Deaths lists the guards and (optionally) the employees, but not the engineer, whom Arthur throws off the train over the bridge (Story, "Stopping the train"). The transcript's stage direction says "he falls to his death" (Who_the_Hell_is_Leviticus_Cornwall_dialogues.txt:358); the wiki Deaths list omits him and its trivia only says Arthur "can throw the train conductor off of the bridge" (Who_the_Hell_is_Leviticus_Cornwall.txt:107).
   Fix (SPEC: stage directions only with wiki support): either add "The engineer, thrown off the train by Arthur as it crosses a bridge (the transcript's stage directions say he falls to his death)" or leave the list as is. Field: `sections.story` Deaths (:129), EN+FR. Low priority.
3. DUPLICATE. Lenny hanging from the car is told in Story > "Boarding the train" ("Lenny ends up hanging ..., and Arthur can pull him up; otherwise Lenny climbs up alone and thanks him sarcastically.") and again in Choices > "On the train" (same facts + honor). The "Arthur chooses whether he or Lenny takes the next one" sentence is also in both (Story :108, Choices :141).
   Fix: in Story keep only "Lenny ends up hanging from the side of a car (see Choices and variants)." and "Inside the first car, Lenny kills a guard with his knife, which starts the gunfight along the train" (or drop the Choices duplicate instead). Fields: `sections.story` (:106, :108), EN+FR.
4. DUPLICATE. Trivia 1 (Hosea's plea on Arthur's last ride) repeats a line quoted in Story ("Hosea's objection") and in Quotes. Acceptable as trivia (new fact = the callback), but the Quotes entry can go. Field: `quotes` (:181).
5. IMPRECISE (FR only). Trivia on the journal: EN "first with an X, the mark usually kept for jobs that brought no money" (Who_the_Hell_is_Leviticus_Cornwall.txt:103 "usually reserved"); FR "d'abord avec une croix, la marque des coups qui n'ont rien rapporté" drops "usually".
   Fix FR: "d'abord avec une croix, la marque habituellement réservée aux coups qui n'ont rien rapporté". Field: `sections.trivia` FR (:224).
6. DUPLICATE (structural). Quotes: 8 of 9 entries already quoted in Story (only "I am not robbing another boat..." is new, and the Story paraphrases it). Same decision as Outlaws #3. Field: `quotes` (:181).

Checked and correct: giver/start/end/rewards/next (Who_the_Hell_is_Leviticus_Cornwall.txt:6-15), Gold table (:54-58) and the no-damage tip (:61), failure list (:65-72; "fails to save Lenny" deliberately left out, documented in the docstring), Deaths of guards/employees (:75-76), missable letters (:89-90), honor-only choice (:48, :116), Lenny sarcastic thanks costs honor (:114), engineer attacks Lenny (:115), Granite Pass cutscene (:107), Micah's Carbine + shotguns (:109-110), dynamite explodes when shot (:101), Cattleman swap (:108), newspapers + Valentine clerk (:81, :106), journal entries (:103). All new quotes verbatim (dialogues :9, :19, :27, :81, :109, :151, :526, :536, :582). FR consistent except #5.

## Eastward Bound

1. UNSUPPORTED. Choices > "Javier at the entrance": "once Javier is picked up, abandoning him or letting him be killed fails the mission."
   Source: Eastward_Bound.txt:43 "Assaults, kills, or abandons Hosea, Charles (and Javier if picked up)"; nothing about letting him be killed.
   Fix: "once Javier is picked up, assaulting, killing or abandoning him fails the mission." FR: "une fois Javier à bord, l'agresser, le tuer ou l'abandonner fait échouer la mission." Field: `sections.choices` (rdr2_eastward_bound.py:128), EN+FR.
2. IMPRECISE. Intro: "The mission opens Chapter 2." It is the last mission of Chapter 1 (Eastward_Bound.txt:27); it ends with the "Chapter II: Horseshoe Overlook" title card and the first scene at the new camp.
   Fix: "It ends with the title card of Chapter 2." FR: "Elle se termine sur le carton du chapitre 2." Field: `intro[1]` (:74), EN+FR.
3. IMPRECISE. Facts "Next mission: Who is Not Without Sin", while the infobox lists three next missions (Eastward_Bound.txt:23) and our Unlocks cell names all three. The choice is documented in the docstring (first listed for Chapter 2 in "Missions in Redemption 2"), but the cell presents it as the only next mission.
   Fix: if the generator allows, "Who is Not Without Sin (first listed for Chapter 2)"; otherwise leave, the Unlocks cell carries the nuance. Field: `next`, low priority.
4. DUPLICATE. "Horseshoe Overlook becomes the gang's camp" is in both Unlocks and Rewards; "Back in the Mud" is in Rewards and again in the Gold "after" paragraph; "Picking up Javier ... is one of the two Gold Medal objectives" (Choices) repeats the Gold table.
   Fix: drop "Horseshoe Overlook as the gang's camp" from `facts.rewards` (:70) or from `facts.unlocks` (:68); in Choices keep only the failure rule ("According to the mission page, once Javier is picked up, assaulting, killing or abandoning him fails the mission."), since Gold already lists the objective. EN+FR.
5. DUPLICATE (structural). Quotes: all 9 entries already quoted in Story. Same decision as Outlaws #3. Field: `quotes` (:167).

Checked and correct: giver/start/end/rewards/next list (Eastward_Bound.txt:6-23), Gold table (:38-39), failure list (:43-46), trophies (:74-97), Lenny and Micah sent west, Lenny back at "A Quiet Time" (:52), absences and returns of Swanson/Charles/Javier/Bill (:54), Uncle (:55), Strauss+Uncle without new dialogue (:53), the girls' boredom and Hosea (:56), two-page journal (:58), riders identified by the wiki (attributed), "virgin land" and journal continuation (Eastward_Bound_dialogues.txt:257, :349; gsw.txt:3522, :3543), "the boy"/whisky (:41, :47). Micah's return point deliberately left out (docstring). FR consistent except #1-#2 (same wording).

## Aside (not a mission page)

- Chapter 1 guide, "Camp life at Colter", last paragraph: "The same page notes that Bill, Javier, Charles and Pearson have no camp events in this chapter." "The same page" refers back to the mission page of "Outlaws from the West", which does not say this; the source is the Camp Events page (Camp_Events.txt:24). The Enter mission page attributes it correctly. Fix in story/rdr2-chapter-1-colter (+ FR): "According to the Camp Events page, Bill, Javier, Charles and Pearson have no camp events in this chapter."

## Totals

| Category | Outlaws | Enter | Aftermath | Old Friends | Cornwall | Eastward | Total |
|---|---|---|---|---|---|---|---|
| WRONG | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| IMPRECISE | 1 | 1 | 0 | 2 | 2 | 2 | 8 |
| UNSUPPORTED | 0 | 1 | 0 | 0 | 0 | 1 | 2 |
| MISQUOTE | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| SPECULATION | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| COPIED | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| DUPLICATE | 2 | 2 | 3 | 3 | 3 | 2 | 15 |
| STYLE | 0 | 0 | 1 | 0 | 1 | 0 | 2 |
| **Page total** | 3 | 4 | 4 | 5 | 6 | 5 | **27** |

(Aftermath #1 counted as DUPLICATE; the six structural "Quotes block repeats the Story" items are included in DUPLICATE, one per page, and need one editorial decision, not six fixes. Plus 1 aside on the guide.)
