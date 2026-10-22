# Archer Fordham fixers: shared decisions (binding)

Reports in this folder (scripts/v3/work/fordham/): fc_report1.md (half1: intro, facts, biography, personality), fc_report2.md (half2:
relationships, skills, missions, quotes, development, reception, media, trivia), coverage_report.md.
Fiche text: fordham_full_en.txt.
Files: scripts/fiches/parts/fordham_A.py (biography), fordham_B.py (personality, names, appearance, skills,
relationships), fordham_C.py (missions, quotes, trivia, media), fordham_D.py (base: facts, intro, essentials,
development, reception). EN AND FR. SPEC.md rules apply. scripts/v3/rules/OWNERSHIP.md and scripts/v3/rules/HOUSE_FACTS.md apply.

Decisions (the lead writes them here after reading the reports: one line per disputed point, which source wins):
- Beecher's Hope 1911 (The Last Enemy That Shall Be Destroyed): ONE standard hedge, same wording everywhere (Key facts, Fate, Relationships, Mechanics, Missions table, Biography). EN: "According to the English-language Red Dead Wiki, Fordham is visible among the men facing John through the barn doors at Beecher's Hope in 1911 (he can be shot in the final Dead Eye and may disappear from the cutscene that follows); the French-language wiki says he does not take part in the mission." FR: "D'après le Red Dead Wiki anglophone, on aperçoit Fordham parmi les hommes qui font face à John entre les portes de la grange de Beecher's Hope en 1911 (il peut être abattu pendant le Dead Eye final et disparaître de la cinématique qui suit) ; le wiki francophone affirme qu'il ne participe pas à la mission." Shortened forms keep both versions. Same hedge in edgar_A.py (EN+FR+docstring: "may disappear", never "does not appear in the cutscene") and HOUSE_FACTS.md.
- The full EN-vs-FR wiki dispute (McKinnon) is told once, in Trivia; other places use the standard hedge only.
- Appearance: 1907 charcoal three-piece suit, black tie, bowler hat, clean-shaven; 1911 brown three-piece suit and dark red tie (gallery-4). Never "dark suit, black tie in both games". Pinkerton badge: Trivia only.
- Quotes block: remove "Our armed forces have no equal..." and "...simple prototype... Virginia" (they stay in B "In his own words"); remove "office clerk or social secretary" (stays in B Names, quoted). Add: "Marston, you're a public menace. We should've had you killed."; "Like you always say, sir, the higher the stakes...", "It ends when we say it ends...", "See, this is what happens when you fraternize with savages..."; John's "Dutch was a good man once, a far better man than you." Every "(see Quotes)" must resolve, else point to Biography.
- Personality: "often calls Ross sir" (not "almost every line"); John is called "John" once (border bridge); "savages"/"insane" point to Biography. No thanks sentence, no "watch his mouth".
- Relationships > Dutch: Fordham also mentions Dutch neutrally ("Dutch van der Linde is in the area", "Van Der Linde is the priority", "Has he changed?"); no "only insults". Bill: Fordham reproaches JOHN for the detour through Mexico. Ross: "almost all his scenes"; drop "calls him sir".
- Biography: Ross sets the body back down; "Fordham does not think he can walk"; Dutch about to call on the bank manager; armored-vehicle lines before camp/supplies lines; Ross tells Fordham to search Micah's cabin (Ending Credits page). Mission count told once (Missions), cut from Biography.
- Missions table: John finds Nastas, Fordham identifies him. Failure conditions ONLY in the Missions table (cut from B "In the game" and the Missions intro sentence).
- Trivia: Javier is talking to the women (not drinking). Ignition fact once, in B "Behind the wheel" (reworded, not copied); cut from Trivia. McKinnon trivia reworded.
- Cut content: fbi03 "newspaper story" removed (Ross scoffs at women wanting the vote). FR-wiki "Bureau fella" line: quoted and attributed to the French-language wiki, names no one, no 1899 inference.
- Gallery: archer_fordham.py GALLERY = gal/captions.json (7 entries, corrected per fc_report2 items 14-18).
- Story guides: RDR1 act 1 l.109 (escort ferry to train, no "brought west", no "take Abigail and Jack"), EN l.138 "take" -> "hold"; RDR1 act 3 l.117/l.145 (captain commands; "Ross and Fordham arrive moments later"). RDR2 ch. 3/4 guides and catherine_* untouched (other agent).
- US spelling, no em/en dashes, FR written natively.

Report back: fixes applied per report item, items not applied with reason.
