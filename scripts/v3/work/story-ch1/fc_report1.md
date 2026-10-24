# Fact-check report 1: RDR2 Chapter 1 (Colter) story guide, chunk L1-L64

## Sources used
- Transcripts: work/story-ch1/fc/gsw.txt (lines 16-3262: opening, Outlaws from the West, Enter Pursued by a Memory, Old Friends, The Aftermath of Genesis; 3444-3540: Eastward Bound), work/_m/{Outlaws_from_the_West,Enter_Pursued_by_a_Memory,Old_Friends,The_Aftermath_of_Genesis,Eastward_Bound}_dialogues.txt
- Mission pages: work/_m/{Outlaws_from_the_West,Enter_Pursued_by_a_Memory,Old_Friends,The_Aftermath_of_Genesis}.txt, Colter.txt, Blackwater_Massacre.txt, Missions_in_Redemption_2.txt (chapter overview), sources/Camp_Events.txt (shortest chapter)
- Fiches: parts/dutch_A, micah_A/B/C, sadie_A/B/C, hosea_A/C, charles_A/B/C/D, bill_A, abigail_B, lenny_A, colm_B, arthur_A/D
- Images: assets/story/rdr2-chapter-1-colter/{hero,scene-1,scene-2}.jpeg (viewed)
- scripts/v3/story/SPEC.md, scripts/v3/rules/HOUSE_FACTS.md

## Verified OK
Opening text (L14) verbatim; overview text (L13) verbatim per Missions_in_Redemption_2.txt l.6. Dutch's speech, "We missed you", Taima, money/trap options, Micah's "blazing with light and noise", Davey/Jenny exchange, hiding positions, body in the wagon, Uncle Sam line, women and Jack, barn O'Driscoll (southwest, lake, train, three choices, reappears in "Old Friends"), Tennessee Walker, Sadie in the cellar (bottle, knife, Micah flips table, lantern, pushes), "We're bad men...", name on the ride, Lenny on watch, Hosea's reply, Tilly/Karen, three days without sleep, rooms and Micah's slur. Enter: Abigail Roberts infobox, two days, "little John", "two best fit men", sawed-off shotgun (page + wiki dialogues l.49; gsw stage direction says revolver, outvoted), river, "kept riding north", campsite, Javier's Blackwater account, dead mauled horse, bourbon (page Trivia), ledge, John's line, three wolves, water, scar, "idiotas"/leg, Abigail's "new low", Strauss, east/west, journal, free roam. Aftermath: all lines incl. both ride-back variants (wiki dialogues l.221-245), "go way back" (l.265), bear unkillable, five-six months, Charles's heritage line, twenty years, reading, Uncle, Navy rum, pelts line (Pearson per wiki dialogues l.429), bow/Eagle Eye/auto-continue. Old Friends: fight in cabin (Arthur, Javier, Lenny intervene), Dutch's lines, Carbine Repeater + lasso, who stays, Annabelle line, brother, positions, Colm hits a man (l.171), make-the-call, hold/advance choice, search assignments, roll of paper, Cornwall, "Outlaws for life", step behind. 150,000 dollars consistent with Blackwater_Massacre.txt l.8 and dutch_A. No dashes, US spelling OK. Captions L8 (hero) and L39 (scene-1) OK.

## Problems

1. IMPRECISE. L9 "a few days after a failed ferry robbery in Blackwater". Source: Arthur's journal, quoted by the guide itself at L47, "We have been running for weeks" (gsw 354); Blackwater_Massacre.txt l.3 dates the robbery April 1899; fiche dutch_A.py:79 "The ferry robbery took place in April 1899" while Colter is May. Fix: "It is set in May 1899 ..., weeks after a failed ferry robbery in Blackwater (April 1899, according to the Red Dead Wiki)."

2. UNSUPPORTED. L12 "The game's pause menu summarizes the chapter with this text". Source: Missions_in_Redemption_2.txt l.6 only labels it "Chapter overview"; no source says where it is displayed. Fix: "The game's chapter overview reads:" (matches the h2 "In-game chapter overview").

3. IMPRECISE. L21 "Asked by Arthur, Dutch says the money was ... In an optional answer, he says ...". Source: Outlaws_from_the_West_dialogues.txt l.140-153: the two lines are the two branches of one dialogue choice; the player hears one or the other, the money line is just as optional. Fix: "Depending on the question the player picks on the ride, Dutch says either that the money was ... or, about the Pinkertons: ...".

4. IMPRECISE. L22 "Susan Grimshaw tells Arthur that most of his belongings from Blackwater were saved, except his money." Source: gsw 3535-3536: Susan: "most of your stuff from Blackwater got saved." Arthur: "Everything apart from my money." Fix: "...tells Arthur that most of his belongings from Blackwater were saved; Arthur answers that his money was not."

5. DUPLICATE. L23 "At the new camp he tells Dutch: 'then Micah got you all excited about that ferry and here we are.'" is retold at L85 "Hosea blames Micah for the ferry job" (Eastward Bound section). Source: same line, Eastward_Bound_dialogues.txt l.239. Fix: keep it in one place (suggest: drop the second sentence of L23, keep L85, or quote it at L85 only).

6. WRONG. L30 "Abigail, Bill Williamson and Arthur carry in Davey Callander on a stretcher". Source: Outlaws_from_the_West_dialogues.txt l.46: "Abigail Roberts then enters the cabin, followed by Bill Williamson and Arthur carrying Davey's now dead body on a stretcher"; fiches abigail_B.py:196 ("Bill and Arthur carry Davey's body into the Colter cabin behind Abigail") and bill_A.py:73 agree. Fix: "Abigail comes in, followed by Bill Williamson and Arthur carrying Davey Callander on a stretcher, already dead."

7. STYLE. L30 "already dead" then, two sentences later, "Abigail says: 'Davey's dead.'" says the same fact twice. Fix: keep one (e.g. drop "already dead" and keep the quote, or keep "already dead" and drop the quote).

8. IMPRECISE. L32 "Alone with Arthur, Micah complains that the gang has too many mouths to feed." Source: Outlaws_from_the_West_dialogues.txt l.213-235: optional branch ("Are you sure about this?"), Dutch is riding at the rear, not absent; the other branch ("You run into anyone else?") has no such line (gsw 101-104). Fix: "In one of two optional exchanges with Arthur, Micah says the gang has 'too many mouths to feed.'"

9. IMPRECISE. L33 "One of the men recognizes Dutch and shouts that Colm will be furious." Source: Outlaws_from_the_West_dialogues.txt l.347: "It's goddamn Dutch van der Linde, you morons! Colm is going to shit his pants!" ("furious" is an interpretation). Same wording in OUR FICHE dutch_A.py:90 ("shouts that Colm will be furious"; FR "va en faire une attaque" is fine). Fix (guide + dutch_A EN): "...recognizes him and shouts: 'It's goddamn Dutch van der Linde, you morons!'"

10. UNSUPPORTED. L44 "On a flat stretch of the mountain they find John's horse". Source: no transcript or page mentions a flat stretch (page: "find John's horse in the snow, mauled and dead"; dialogues l.151). Fix: "Higher up, they find John's horse, dead and mauled".

11. IMPRECISE. L44 "Javier fires a shot in the air". Source: gsw 262 "He shots several times in the air"; wiki dialogues l.161 "fires a shot into the air". Transcripts disagree. Fix: "Javier fires into the air".

12. IMPRECISE. L20 "by the time Arthur and the others reached the other side of town". Source: gsw 251 "By the time you boys showed up from the other side of town"; wiki dialogues l.117 "showed up on the other side of town". Transcripts disagree on the preposition; "reached" picks one reading. Fix: "by the time Arthur and the others showed up" (quote "we were only just holding on" stays).

13. IMPRECISE (order). L63 "The gang kills the O'Driscolls in the camp, then a second wave ...; Arthur chooses to advance or hold ground. Looking at the bodies, Dutch says Colm 'doesn't give a damn about his men'". Source: gsw 483-486 and Old_Friends_dialogues.txt l.285-306: Dutch orders the bodies searched and makes the remark BEFORE the second wave comes out of the trees. Fix: "The gang kills the O'Driscolls in the camp. While the bodies are searched, Dutch says Colm 'doesn't give a damn about his men' and only cares about numbers. A second wave then comes out of the trees; Arthur chooses to advance or hold ground."

14. DUPLICATE. L56 "the mission unlocks Eagle Eye" is repeated in Trivia L116 (together with Dead Eye, already in L66). Fix: drop L116, or drop the unlocks from L56/L66.

15. DUPLICATE (minor). L31 "Arthur rides Charles's mare, Taima" and L119 (Trivia) restates it. L119 adds a new fact (only mission where a gang member's horse is meant to be ridden). Fix: L119 can start "Taima is the only gang member's horse meant to be ridden..." without re-explaining; or keep as is if Trivia repetition is accepted.

16. UNSUPPORTED (caption). L26 "Dutch holds up a lantern in the blizzard during 'Outlaws from the West'." Source: scene-2.jpeg shows Dutch with a lantern under light snowfall, in daylight/dusk, with a fence line behind him; the mission scenes are a night blizzard (Outlaws_from_the_West.txt; dialogues l.~200 "They both hold up their lights"). The shot looks like promotional/trailer material, not a verifiable mission frame. Fix: "Dutch van der Linde holds up a lantern in the snow, in his Chapter 1 winter coat." (or confirm the frame's origin before naming the mission).

## Errors in our fiches
- dutch_A.py:90 (EN): "shouts that Colm will be furious" -> not verbatim/interpretive (see #9). Source: Outlaws_from_the_West_dialogues.txt l.347.

## Counts
- WRONG: 1 (#6)
- IMPRECISE: 8 (#1, #3, #4, #8, #9, #11, #12, #13)
- UNSUPPORTED: 3 (#2, #10, #16)
- MISQUOTE: 0
- SPECULATION: 0
- COPIED: 0
- DUPLICATE: 3 (#5, #14, #15)
- STYLE: 1 (#7)
- Total: 16 (plus 1 fiche issue, dutch_A.py:90, same as #9)
