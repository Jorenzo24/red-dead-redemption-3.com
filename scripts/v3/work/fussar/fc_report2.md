# Fact-check report: Alberto Fussar, chunk half2.txt (Relationships to Gallery)

## Sources used
- Fan transcript, Game Scripts Wiki: `fc/gsw.txt` (The Gilded Cage l. 9077; Welcome to the New World l. 10480-10590; Savagery Unleashed l. 10590-10660; A Kind and Benevolent Despot l. 10663-10840; Hell Hath No Fury l. 10845-10930; Paradise Mercifully Departed l. 10935-11010; Just a Social Call l. 11743).
- Red Dead Wiki: `en.txt`, `fr.txt`; `_m/` pages The_Gilded_Cage, A_Kind_and_Benevolent_Despot, Paradise_Mercifully_Departed, Guarma, Guarma_Island_Sugar_Boom, Mayor_s_Gala_Was_Grand, Levi_Simon, Hercule_Fontaine, Cuban_Military, Aguasdulces, Red_Dead_Redemption_2_Cut_Content.
- Real world: `fc/wp_alfredo_narciso.txt`, `fc/narciso_rdr2_post.txt`, `fc/narciso_home_2024-05-20.txt`, `fc/wc_villains_p1.txt`, `scripts/v3/work/catherine/fc/wp_list_rdr2.txt` (l. 213, `<ref name="Credits"/>`).
- `FIX_RULES.md`, `HOUSE_FACTS.md`, docstrings of `fussar_A..D.py`, `arthur_E.py` (kill list), `half1.txt` / `fussar_full_en.txt` for duplicates.

## Verified OK
Every quote in the Quotes block matches the transcript verbatim (ellipses normalized). Sugar-boom details (two trips, exclusive purchase order, "a great friend of America", Cuban sugar, 14-hour shifts, "reportedly feared across the island") match the article. Dutch's chapter 6 line on Cornwall's sugar business is in the transcript ("Just a Social Call"). Simon's lines, Leon's "little more than slaves shipped in from other islands", Hercule's "Fussar's compound", the warship, Micah's report, the standoff, the captain's rifle (mission page: "kicks"), the "surprise interviews" line, Bill guarding Javier, Bronte on the balcony: all supported. Levi Simon American and Angel as interrogator: wiki-only, attributed. Mission list, chapters, Savagery Unleashed and Hell Hath No Fury rows: OK. Cut content (Madeline Fussar, GulFussars, unused hair, Fussar1 lady, Leon's niece in the FUS1 audio bank): matches the cut-content page. Red Dead Online flag at rank 59 of the third Outlaw Pass: Guarma page trivia. Trivia: FR wiki party note, Ledger No. 67 gala guest list and same-issue sugar article, mission-fail cutscene, Gold Medal 1:45 timer, American Venom, Arthur's three imposed kills: all match sources.
Casting: Wikipedia's list credits "Colonel Alberto Fussar (Alfredo Narciso)" with the Credits ref; Red Dead Wiki infobox agrees. The November 6, 2018 post is quoted verbatim ("Check me out as the villain, Alberto Fussar, in Red Dead Redemption 2! Looks like fun, maggots."); the game came out October 26, 2018, so "shortly after" holds. "can also be heard voicing Alberto Fussar" is verbatim from the 2024 snapshot. Broadway and TV credits match Wikipedia / his site. No interview or motion-capture source exists: the cautious sentence is correct.
WhatCulture: Matt Thompson, February 7, 2022, list of fifteen villains, Fussar at No. 15 (the countdown's first and lowest entry). The three quoted phrases ("a lulling low-point in the game", "a nothing character; a nameless, almost faceless villain", "a loose tie to Leviticus Cornwall does make the villain more three-dimensional") are verbatim; the paraphrases (no impact on the story, horde of militiamen, tortured and amputated rebels, no glee or malice, more made of Levi Simon) are accurate.

## Problems

1. **WRONG** (FIX_RULES 1). Weapons: "Sources differ on the gun he uses from the tower over the harbor: the Red Dead Wiki's page on Fussar and the stage notes of the fan transcript speak of a cannon, while the wiki's mission page and the French Red Dead Wiki describe a Gatling gun." Source: transcript l. 10997 "[Fussar loads the cannon.]", Hercule "He's shooting", screenshots FussarCanon/FussarDeath; lead decision: cannon only, no "both versions". Fix: "From the tower over the harbor he loads and fires a cannon."

2. **DUPLICATE**. Weapons: "According to the mission page, Arthur can either bring down the tower with a cannon or shoot Fussar directly. The character page adds that a single shot from any gun kills him if the player finds the right angle." Already in Biography (half1: "According to the mission page, Arthur can also kill him with a gunshot instead of the cannon"); fussar_C docstring assigns the gunshot kill to part A. Fix: drop the mission-page sentence from Weapons; keep the one-shot/angle detail only once (either append it to the Biography sentence or keep it here alone).

3. **UNSUPPORTED / attribution** (FIX_RULES 2). Hercule Fontaine relationship: "He draws Fussar's fire at the harbor so that Arthur can reach a cannon (see Biography)." Wiki character page only; transcript has Hercule sending Arthur to the cannon, no line on drawing fire. Fix: "According to the Red Dead Wiki, he draws Fussar's fire at the harbor so that Arthur can reach a cannon (see Biography)."

4. **IMPRECISE**. Hercule relationship: "He promises the gang a boat if they help him silence Fussar." The boat is promised in "Welcome to the New World" in exchange for helping Leon with the escaped workers ("I am the only one who can arrange a boat for you. But… I need something in return. Help Leon…", l. 10577). "If we can silence him… then I can help you escape" comes later, in "Hell Hath No Fury" (l. 10851). Fix: "He promises the gang a boat in return for helping Leon's escaped workers; later he tells them that if Fussar can be silenced, he can get them off the island."

5. **WRONG** (count). Missions intro: "Two other Guarma missions are driven by his regime without showing him; they are listed in the second table." The second table lists three missions (Welcome to the New World, Savagery Unleashed, Hell Hath No Fury). Fix: "Three other Guarma missions…".

6. **DUPLICATE** (FIX_RULES 3). Quotes block: Bronte "That is... Alberto Fussar. He owns a sugar plantation… whore and despoil himself.", Leon "A tyrant, driven by nothing but power and greed…", Micah "I like the man's style... he's thorough, nasty and vindictive." All three are quoted in Personality (half1). Fix: drop the three from Quotes (C).

7. **DUPLICATE** (FIX_RULES 3). Quotes block: Levi Simon "Not half as upsetting… Mr. Fussar has a lot of very powerful friends." and Hercule "That is the problem. It doesn't matter how many we kill. He will have the money to get more." Both are quoted in Power on Guarma (same chunk: "Sugar plantation"/"Soldiers, navy and guns"), which B owns. Fix: drop both from Quotes. (After items 6-7 the Quotes block keeps Arthur's Bronte question, Dutch's "Very kind of you", Dutch/Arthur after Micah's report, Hercule's "every day I can" and "I got him for you, Javier", which is enough.)

8. **DUPLICATE** (FIX_RULES 3, affects half1). Cornwall relationship quotes "a great friend of America"; Biography Origins (half1) quotes it too, and also quotes verbatim "His security force is reportedly feared across the island, with plantation workers often working 14 hour shifts to keep up", which Power on Guarma (B) owns. Fix: keep the quotes in B; paraphrase both in A Origins (half1). Also the Cornwall relationship repeats A's "two trips to tour the plantations": acceptable as relationship recap, but shorten to "(see Biography)" if the fixer trims.

9. **DUPLICATE**. Power on Guarma, Governor and colonel: "Fussar holds two titles: governor of Guarma, in the newspapers, and colonel, in Hercule's mouth." Names (half1) already says "Hercule calls him Colonel Fussar… The newspapers call him the governor of Guarma." Fix: drop from Power or reduce to "(see Names)". Also **STYLE**: "in Hercule's mouth" is a calque; if kept, write "as Hercule calls him".

10. **DUPLICATE + COPIED**. Trivia: "According to the Red Dead Wiki, Fussar's estate in Aguasdulces is enclosed by a stone wall and comprises a large manor surrounded by cages, the sugar factory, a mill, a barn, a well and a dilapidated tower that gives access to the caves." Already in Power on Guarma ("the estate is enclosed by a stone wall and includes a manor, cages for prisoners, a sugar factory and a mill"). Wiki Aguasdulces: "A stone fence encloses it and consists of a large manor around which there are several cages and stone ledges, a sugar factory, a dilapidated tower through which you can go to the caves, a mill, a several buildings, a barn and a well." The Trivia sentence follows the wiki's list and order closely. Fix: drop the Trivia item (trivia only holds what is nowhere else); keep Power's shorter version.

11. **DUPLICATE**. Trivia: "In the cabin standoff, Dutch draws his second revolver when Fussar walks in." Told in Biography (half1: "Dutch draws his second revolver to cover him") and in the Dutch relationship ("faces Fussar and Simon with a revolver in each hand"). Fix: keep only "According to the Red Dead Wiki, the double-revolver standoff in the cabin happens again in "American Venom", the last mission of the 1907 epilogue."

12. **DUPLICATE**. Power on Guarma, Soldiers: "Hercule tells the gang that Fussar knows who they are and the price on their heads, and that he has called in the navy from Cuba; a warship then shells the fort of Cinco Torres. After it sinks, Micah reports that Fussar holds the ship's captain and has set up gun positions to fire on any boat that tries to sail." These events are told in Biography (half1), again in the Micah and captain relationships, and in the Missions table. Biography owns events (OWNERSHIP.md). Fix: reduce to one line: "He calls in a warship from Cuba and sets gun positions around the harbor (see Biography)."

13. **IMPRECISE**. Power on Guarma, Sugar plantation: "…and that a group of them has just fled into the jungle." Leon: "A group escaped yesterday into the jungle" (l. 10573). Fix: "…and that a group of them fled into the jungle the day before."

14. **IMPRECISE**. Dutch relationship: "Dutch gives Simon a false name to keep Fussar from learning who the castaways are." Dutch gives "Aiden O'Malley" before Fussar's name is spoken; his stated reason afterwards is "they can't find out who we are" (l. 10512), not Fussar specifically. Fix: "Dutch gives Simon a false name, Aiden O'Malley, so that their captors cannot find out who the castaways are."

15. **IMPRECISE**. Micah relationship: "…and rigs the batteries with dynamite (see Biography)." Arthur plants the dynamite in the first gun ("[Arthur puts the dynamite inside the cannon.]", l. 10954); Micah rigs the next set ("I'll get the dynamite rigged on these cannons", l. 10959). Fix: "…and rigs the second set of guns with dynamite."

16. **IMPRECISE** (cross-reference). Angel relationship: "…wakes up tied to a chair in front of him and frees himself (see Biography)." The Biography does not tell the interrogation scene (it only says Arthur and Leon save workers from the gallows). Fix: drop "(see Biography)" or add one clause to the Biography's Savagery Unleashed sentence.

17. **IMPRECISE**. Quotes intro: "checked against a full transcript of the game." It is a fan transcript (Game Scripts Wiki); half1 says "a fan transcript of the game". Fix: "checked against a fan transcript of the game."

18. **UNSUPPORTED** (weak source, birth year). Casting: "Narciso, born in Milwaukee, Wisconsin, in 1973…". Milwaukee is in Wikipedia's body text next to a reference (UWEC) and in the Red Dead Wiki stub. The year 1973 (July 8) is only in Wikipedia's infobox and lead, with no citation; the article carries a "BLP sources" tag and the category "Year of birth missing (living people)". Fix: "Narciso, born in Milwaukee, Wisconsin, …" without the year (or attribute: "born in 1973 according to Wikipedia").

19. **IMPRECISE** (heading). Reception heading "Ranked last among the series' villains" generalizes one list. Fix: "Last in WhatCulture's villain ranking" (body is correct).

## Count per category
- WRONG: 2 (items 1, 5)
- IMPRECISE: 7 (items 4, 13, 14, 15, 16, 17, 19)
- UNSUPPORTED: 2 (items 3, 18)
- MISQUOTE: 0
- SPECULATION: 0
- COPIED: 1 (item 10, counted with its duplicate)
- DUPLICATE: 8 (items 2, 6, 7, 8, 9, 10, 11, 12)
- STYLE: 1 (item 9, "in Hercule's mouth")
