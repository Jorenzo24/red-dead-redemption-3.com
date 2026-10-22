# Coverage report: Rains Fall (v3, medium tier), 22 Oct 2026

Inputs: Red Dead Wiki EN (`en.txt`, 1 358 words per `coverage.py`) and FR (`fr.txt`), our fiche
`rains_full_en.txt` (Lnn below), full fan transcript `fc/gsw.txt` (gsw line numbers), mission pages in `_m/`,
FIX_RULES.md, OWNERSHIP.md. `python3 scripts/coverage.py rains-fall "Rains Fall"` ran against the local build:
**our EN 6 667 words = 490 % of the wiki** (FR 7 836 words). Section words: Biography 2 443, Personality 423,
Relationships 1 088, Chief/remedies/horses 270, Missions 492, Quotes 579, Development 465, Reception 192,
Other media 77, Trivia 271.

Line ranges by part: D = L2-L21 (intro, key facts, facts) and L145-L157 (Development, Reception);
A = L22-L50 (Biography); B = L51-L93 (Personality, Names, Appearance, Relationships, Chief/remedies/horses);
C = L94-L144 (Missions, Quotes) and L158-L169 (Other media, Trivia).

Every wiki section is covered (Background, Colter, Saint Denis, Beaver Hollow, Epilogue, Personality, Appearance,
Mission appearances, Trivia, infobox: family, mounts, alias, voice, locations). The FR wiki adds nothing new
(its list of 8 missions is correctly described in L95). The gaps are four quoted lines the lead assigned to C.

## 1. Wiki facts missing from the fiche

| # | Wiki excerpt | Status | Recommendation |
|---|---|---|---|
| 1 | Lead quote: "Sometimes the correct path, the bravest path, is the least obvious... and also the gentlest." (Archeology for Beginners) | CONFIRMED, gsw 12319 (in the tent, right after Favours' revenge on the two women): "Yes, sometimes the correct path, the bravest path… is the least obvious, and also the gentlest. I'm… I'm a great disappointment to my son." | **C Quotes**, chapter 6, before "See the wolves" (FIX_RULES 5 gives this line to C). Source line: Archeology for Beginners, to Arthur, in his tent. |
| 2 | Quote: "My son thinks there is glory in death. Maybe he's right... but for me... I saw death being handed out so freely by the most foolish of men... I never could equate it with victory." | CONFIRMED, gsw 12321 (continues: "Glory has come in service… maybe not, I don't know."), answer to Arthur's "Your son seems to want a war." | **C Quotes**, after #1 (FIX_RULES 5). A L36 and B L52 keep their paraphrases. |
| 3 | Quote: the "My Last Boy" speech, "My son, my last son... When I was your age... I fought... endure we must." | CONFIRMED, gsw 13112 (note: the transcript repeats "The men I knew were slain." twice; quote it once, with an ellipsis if needed; "cannot" in one word, wiki has "can not"). | **C Quotes**, chapter 6, before "The earth, the water..." (FIX_RULES 5: C keeps the My Last Boy line). A L24 and L44 keep their paraphrases. |
| 4 | Personality header quote: "My only boy... my precious boy... do not mistake my strength for weakness." (to Eagle Flies) | CONFIRMED, gsw 13114, same speech: "Do not die for pride, my son. We have suffered too much in this trick. The earth, the water… they have no pride. They endure, and we must endure. My only boy… my precious boy… do not mistake my strength for weakness. As your chief, I implore you." | **C Quotes**: extend the existing L133 quote to the end of this line ("...they have no pride. They endure, and we must endure. My only boy... my precious boy... do not mistake my strength for weakness. As your chief, I implore you."). That also anchors the "implore" trivia (L167). Not in B (B leaves wiki quote-list lines to C). |
| 5 | Appearance: second outfit "brown coat, a light-green waistcoat, a blue shirt, and no hat"; first outfit "red shirt" | WIKI-ONLY | No action. House rule: no outfit catalogue; outfits only as gallery captions, and none of the 3 gallery images shows the second outfit. |
| 6 | Trivia: "appear to be based on" Sitting Bull and Red Cloud | SPECULATIVE | Do not add (already excluded in rains_B docstring). |
| 7 | Trivia: Favours' "silly name" means he "was given the information of his name in Lakotan" | SPECULATIVE (inference) | Do not add. The line itself is in B Names (L57). |
| 8 | "Rains Fall forgives Arthur"; "willing to put up with decades of abuse"; "seems to admit his pacifism" | Interpretation, not shown in gsw 12300-12312 | Do not add. |
| 9 | "he offers Arthur money to recover them ... Arthur gladly volunteers to do so without payment" | CONTRADICTED (see section 2, item a) | Do not add. |

Optional (not wiki facts, transcript-verified, only if C/A want them): "I suppose I lack the grandeur of a conventional
king?" (gsw 12305, Archeology, ties to the title of "The King's Son"); in My Last Boy, "After you helped me, after we
spoke… this is just a trap. My son, my people, will all die." (gsw 13120; A L44 currently paraphrases only the
"helped me" part).

## 2. Places where the fiche differs from the wiki

a. **Money offered for the Chanupa (wiki EN "History"; FR wiki "il implore Arthur d'aller furtivement récupérer").**
   Fiche is right. gsw 12384-12387: Arthur volunteers ("Not if I get it back... I'm gonna go in, get your Chanupa");
   no money is offered. Mission page `_m/Archeology_for_Beginners.txt` l.29: Rains Fall "is initially hesitant but
   allows Arthur to do so. However, he tells him not to harm any of the soldiers", which supports A L39 ("agrees on
   condition that no soldier is harmed"). Rains Fall only says he gives "very little" for a "great debt" (gsw 12403).
b. **Who arranged the truce meeting.** Wiki: Favours "has arranged a truce meeting". gsw 12512-12513: "I believe I've
   made progress brokering peace... Colonel Favours has agreed to a meeting"; Monroe earlier "still hoping a meeting can
   be arranged" (gsw 12456). A L40 is exact. **B L89 "He arranges the meeting with Colonel Favours himself" overstates**:
   use his own word, "he brokers the meeting; Favours agrees to it".
c. **The King's Son.** Wiki: "despondent... initially prompting a negative response... the tribe's conflict with the
   Army is already bad enough". gsw 12982-12996: he only says "No." Fiche (A L43) is right; do not add the wiki's reason.
d. **Eagle Flies' return.** Wiki: "Arthur and Charles bring his body back to him. Rains Fall weeps as he watches his
   last son die." gsw 13300-13303: he arrives alive ("Bring him to me"), dies in the tent while his father holds his
   hand. Fiche (A L45) is right; the weeping stays attributed to the wiki, as now.
e. **"Arthur and Charles leave him alone to mourn."** gsw 13305-13311: Charles stays to help the tribe and tells the chief
   they must pack and move; only Arthur leaves. Fiche (A L45) is right.
f. **Order in the tent.** Wiki: chastises for the raid, then condolences "after discovering his illness". gsw 12300-12305:
   cough and "I think I'm dying" first, then the raid. Fiche (A L36) is right.
g. **Document vs letter at the mayor's party.** Wiki: "giving a document". Bronte (per rains_B source register, The Gilded
   Cage transcript) says "hand a letter to the mayor". Fiche (A L30, B L84) follows the transcript; keep.
h. **Lakota line, placement.** L151 "speaks to his men on the way to the peace talks" vs L161 "at the peace talks".
   gsw 12530-12534: "There's my men up ahead." then "Rains Fall In Lakota: These men are our friends… come on… let's go."
   just before they ride into Favours' camp. When L161 is cut (section 3), make L151 say: on arrival at the meeting place,
   he tells his waiting men in Lakota that Arthur and Charles are friends.
i. **Wolves: "approves" (A L38) vs "thanks" (B L53, mission page l.59).** gsw 12352: "Good. There was no need to harm
   them." Both are defensible; harmonize to "approves" if L53 is kept (see section 3, D-11).
j. **Arthur's journal wording.** gsw 12409 reads "Now I see as wise" and "stop Dutch pushing"; the fiche (L141, B L66)
   has "Now I see him as wise" and "stop Dutch from pushing", identical to arthur_F.py l.139. The fan transcript drops
   words; keep the fiche wording (consistent across fiches).
k. **Epilogue meeting** (wiki): no transcript; A L48 attributes it to the wiki, correct per FIX_RULES 3. But **A L47
   "Rains Fall himself confirms the destination... tells John that his people are no longer really a tribe... now in
   Canada" is unattributed**; FIX_RULES 3 requires "(Red Dead Wiki quote list, attributed)". Fix: "According to the
   Red Dead Wiki's quote list, Rains Fall tells John...".

No case where the wiki proves the fiche wrong. No correction needed in other fiches or guides from this check.

## 3. Duplicates inside the fiche

Quotes (OWNERSHIP: each line in one place; A paraphrases; FIX_RULES 5: cut from C, not B):
- D-1 "Brutality and beauty..." B L55 and C L119. Keep B; cut C L119.
- D-2 "Even sacred things... matter more." B L55 and C L125. Keep B; cut C L125 (or keep only "Was anyone hurt?" if C wants it; it is narrated in A L39 already, so cut).
- D-3 "The army aren't all bad men..." B L55 and C L121. Keep B; cut C L121.
- D-4 "People have lied to my people... that's treason." B L55 and C L131. Keep B; cut C L131 (C may keep only "He is the chief's son of a proud nation. How could he commit treason?" if it wants the mission line; otherwise cut the whole entry).
- D-5 Arthur's journal: B L66 ("wise and thoughtful and sensible") and C L141 (full entry), plus A L39 paraphrase. Keep B; cut C L141 (FIX_RULES 5). A L39 keeps one paraphrase clause.
- D-6 "the impetuous Prince" quoted in A L36 and B L62. A must paraphrase ("calls his son an impetuous prince" without quotation marks, or "mocks his son as a prince").
- D-7 "a great chief" quoted in A L31 and B L57. A paraphrase (drop the quotation marks).
- D-8 "Good day, Colonel Favours" quoted in A L41 and B L72. A paraphrase ("he ends the talks with a curt good day"); B keeps the quote.
- After D-1 to D-5, C L112 ("Lines already quoted under Personality do not appear again here") becomes true; reword to "under Personality or Relationships".

Trivia (C keeps only facts found nowhere else; FIX_RULES 6):
- D-9 Lakota captions: D L151 and C L161. Keep D (FIX_RULES 6); cut C L161 (fold its "friends" detail into L151, see 2h).
- D-10 Aged look in the 1907 credits: B L59 and C L169. Keep B (FIX_RULES 6); cut C L169.
- D-11 Owl Feather Trinket 15 percent: B L91 and C L162. Keep B; cut C L162.
- D-12 English mace + ginseng = Special Health Cure: B L91 and C L163. Keep B; cut C L163.
- D-13 Monroe's first name said once: B L74 and C L166. Keep B (relationship entry); cut C L166.

Narrative told twice (A owns events; B one clause at most; Skills points rather than repeats):
- D-14 B L89 "Chief and negotiator" repeats A L31-L32 (councillor and senator, pay), A L37 (Monroe, mayor and Bureau), A L40 (outsiders at the table). Keep the "very handsomely" quote and one pointer sentence; cut the rest.
- D-15 B L74 Monroe repeats A L37 (reassigned from the north, Washington, drilling approval) and A L40 (vaccines). Keep the quote "He's a good man, he wants to help" and the first-name fact; replace the rest with "see Biography".
- D-16 B L76 Evelyn Miller repeats A L25 (treaty signed three years earlier) and A L31 (prospectors' reports); B L78 Leviticus Cornwall repeats the prospectors' reports a third time. Keep A; B L76 one clause + pointer; B L78 keep only the Leland Oil file location and "never meets him on screen".
- D-17 Three riders in "Eastward Bound": A L28, B L80 (Paytah), B L82 (Hosea), plus C L97 (table, allowed). Keep A; B L80 and L82 drop the riders sentence (Paytah keeps his My Last Boy line; Hosea keeps his Heartlands remark only if A L25 drops it, else cut B L82 entirely: A L25 already tells Hosea's account).
- D-18 B L65 Arthur repeats A L28 (Cumberland Falls), A L36 ("hopes he finds peace"), A L37 (Isaac, Dutch warning), A L42 (his father). Reduce to the relationship arc in two sentences with "see Biography".
- D-19 B L68 Charles repeats A L35 (helping on Guarma), A L42 (reprisals), A L45 (pack and move, stays). Keep "Do it for me" and the "we must pack" quote (B owns the quote; A L45 already paraphrases); cut the reprisals sentence.
- D-20 B L70 Dutch repeats A L36 ("talks a lot", easily led) and A L43 (five years). Keep the quoted lines, cut the paraphrases duplicating A.
- D-21 B L72 Favours repeats A L36 (two women assaulted) and A L41 (treaty void). Keep the "old line" quote and the wiki Cornwall agreement; point to Biography for the rest.
- D-22 B L84 Bronte repeats A L30 (balcony, letter, mocking). Acceptable as B owns Bronte's words; A L30 can shorten to "Bronte mocks them from a balcony".
- D-23 B L53 wolves and "was anyone hurt" repeat A L38-L39. Cut from Personality or reduce to one clause without the events.
- D-24 A L38 herbs (with paraphrased advice) and B L91 (quoted advice, ingredients). Keep B; A L38 one clause ("he picks herbs for Arthur's cough, see Herbs and remedies").
- D-25 "Appears only in RDR2": D L147 (first sentence) and C L159 (first sentence). Keep C L159 (Other media); cut D L147 first sentence.
- D-26 Rockstar's descriptions of Sept 2018 do not include him: B L52 and C L159. Keep B (OWNERSHIP: official descriptions = B); C L159 cut that sentence.

## 4. Summary for the correctors

**Part A (Biography)**
1. L47: attribute the epilogue line to the Red Dead Wiki's quote list (FIX_RULES 3).
2. L31 "a great chief", L36 "the impetuous Prince", L41 "Good day, Colonel Favours": paraphrase, no quotation marks (D-6, D-7, D-8).
3. L38: reduce the herbs to one clause with a pointer to B "Herbs and remedies" (D-24).
4. Optional: L44 add "this is just a trap... my son, my people, will all die" (gsw 13120), paraphrased.

**Part B (Personality, Names, Appearance, Relationships, Chief/remedies/horses)**
5. L89: "arranges the meeting himself" -> "brokers the meeting, which Favours agrees to" (2b); cut the repeats of A (D-14).
6. L53: cut the wolves/"anyone hurt" events or reduce to one clause; if kept, "approves" not "thanks" (D-23, 2i).
7. Trim the relationship entries that retell A: L65 Arthur, L68 Charles, L70 Dutch, L72 Favours, L74 Monroe, L76 Miller, L78 Cornwall, L80 Paytah, L82 Hosea (D-15 to D-21). Quotes listed in rains_B docstring stay.

**Part C (Missions, Quotes, Other media, Trivia)**
8. Quotes, chapter 6: ADD "Yes, sometimes the correct path, the bravest path... is the least obvious, and also the gentlest." and "My son thinks there is glory in death... I never could equate it with victory." (Archeology for Beginners, in his tent, gsw 12319, 12321).
9. Quotes, chapter 6: ADD the My Last Boy speech "My son, my last son... But endure we must." (gsw 13112) and EXTEND L133 to "...My only boy... my precious boy... do not mistake my strength for weakness. As your chief, I implore you." (gsw 13114).
10. Quotes: CUT L119, L121, L125, L131, L141 (quoted in B; FIX_RULES 5) and reword L112 accordingly.
11. Trivia: CUT L161 (Lakota), L162 (trinket), L163 (herbs), L166 (Monroe's first name), L169 (aged look). Remaining trivia: wolves non-hostile, free-roam site update, "implore", epilogue honor.
12. Other media L159: cut the Rockstar descriptions sentence (kept in B L52).

**Part D (intro/facts, Development, Reception)**
13. L151: on cutting C L161, state that he speaks Lakota to his men on arrival at the meeting place, telling them Arthur and Charles are friends (gsw 12533).
14. L147: cut the first sentence ("appears only in RDR2", kept in C L159).

Counts: section 1 = 9 rows (4 to add, all CONFIRMED, all C; 5 not to add); section 2 = 11 items (wiki wrong in 7,
fiche fixes needed in 2: B L89, A L47; 2 harmonizations); section 3 = 26 duplicates. Length ratio EN = 490 % of the
wiki (6 667 / 1 358 words); FR fiche 7 836 words.
