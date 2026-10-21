# Coverage report: Abraham Reyes (v3, medium tier)

Compared: Red Dead Wiki EN (`en.txt`) + FR (`fr.txt`) vs `reyes_full_en.txt` (Lnn).
`coverage.py abraham-reyes "Abraham Reyes"`: our EN 8,191 words = **312 % of the wiki** (FR 9,856 words, 568 % of the FR wiki).
Raw-file ratio (our 8,146 words / wikitext 3,424 words incl. markup) = 238 %.
Section sizes EN: intro+facts 427, Biography 3,033, Personality 498, Relationships 988, Propaganda/weapons/horse 424,
Missions 626, Quotes 1,045, Development 210, Reception 258, Other media 211, Trivia 433, Gallery 38.

Overall the wiki is very well covered: every History, Undead Nightmare, Mission, Personality and Trivia point that is
non-speculative is already in the fiche (often better sourced). Gaps are small.

## 1. Wiki facts missing from the fiche

| # | Wiki excerpt | Status | Recommendation |
|---|---|---|---|
| 1 | Personality: after the Chinese-workers remark, "John sarcastically remarks 'You have the makings of a true leader, Abraham.'" | CONFIRMED, but transcript wording differs: "You have all the makings of a great leader, Abraham." (`_m/The_Gates_of_El_Presidio_dialogues.txt` l.141) | B, "In his own words" (L59): add John's reply right after the Chinese quote, with the transcript wording. Not repeated in C. |
| 2 | Quote: "These peasant girls, they believe every word a fellow says! So naive! It is really quite charming. I love peasants." | CONFIRMED (Gates dialogues l.21: "...It's really quite charming. I love peasants. Don't you love peasants? I love them, they have such purity.") | C Quotes, Gates of El Presidio block, transcript wording. A L39 keeps its paraphrase. |
| 3 | (wiki quotes "Their energy... it is like food to me!" in Quotes; fiche paraphrases it L36). Same speech, not in wiki but adjacent: "A man like you, or me, with just a few such men, I tell you I could rule the entire country." | CONFIRMED (`_m/The_Great_Mexican_Train_Robbery_dialogues.txt` l.9) | C Quotes, Train Robbery block (quote "Their energy... it is like food to me. I feel I was sent for them, and they were sent to me." and/or the "rule the entire country" line). A keeps the paraphrase. |
| 4 | "Reyes will shoot whichever one was not killed by John (or both if the player kills neither of the two)." | CONFIRMED (`_m/An_Appointed_Time.txt` l.53) | A L45: add "or both if John fires at neither". |
| 5 | History: "his charisma making him an excellent recruiter" | Interpretation in the wiki; the primary text is Ledger No. 56: "It is this foresight and intelligence that has endeared him to a large section of Mexico and which is bringing the country to the brink of bloody anarchy." CONFIRMED (`fc/newspapers_reyes.txt` l.6) | A Origins (L28): one sentence quoting the Ledger's assessment. Do not add the wiki's "charisma" wording. |
| 6 | Ledger No. 56 dated "late October" 1911; massacre of 1914 dated "around October", article "published in November of 1914" | WIKI-ONLY (the wiki's own deduction from issue numbering / election article) | Optional, A L28 and L51, attributed ("the Red Dead Wiki dates the article to late October 1911 / November 1914"). Can be skipped. |
| 7 | "Williamson being forced by Allende at sword's point to exit" | WIKI-ONLY (not in the dialogue transcript or walkthrough) | Optional, A L45, attributed. Low value; skip is acceptable. |
| 8 | FR wiki: aged 27 in 1911, born 1884; "un des rebelles mentionne que Reyes a 27 ans" in Gates of El Presidio | WIKI-ONLY (FR), not found in the Gates transcript; contradicts the GOTY guide's 30 | Do not add as fact. Optional in D facts grid (L12): "the French-language wiki gives 27". Recommend skipping. |
| 9 | Mission page An Appointed Time: Reyes does not wear his green poncho in that mission | WIKI-ONLY game content (mission page trivia; its explanation is speculation) | Optional, B Appearance (L64): one clause, without the "confiscated" explanation. |
| 10 | Trivia: modelled on Madero / Villa / Zapata / Carranza; Appointed Time mirrors Ciudad Juarez and Cuautla; Bernardo Reyes | SPECULATIVE (fan comparison; the Bernardo Reyes claim is also historically wrong) | Do not add. |
| 11 | Trivia: "like food" phrase "almost identical" to Mussolini | SPECULATIVE / interpretation | Do not add. |
| 12 | Trivia: in Damnation "most likely because he was a hypocrite who became a tyrant" | SPECULATIVE | Do not add (Damnation section itself is in D/C L198). |
| 13 | Trivia/Personality: Reyes "admits to John he would have liked to have met" Dutch | NOT in the transcript (Train Robbery dialogues l.53-67 end on "Where is he now?" / "he went insane") | Do not add. Fiche L37/L80 are correct. |
| 14 | Personality: eugenics, "sees himself in a romantic light", "respects John and Dutch", accusations "greatly exaggerated" | Interpretation | Do not add; the underlying lines are already quoted. |
| 15 | Multiplayer quote list (24 lines) | WIKI-ONLY | Fiche keeps 5 (L174-183); the rest are insults. No change needed. |

## 2. Places where the fiche differs from the wiki

1. **Cannon at El Presidio.** Wiki Personality: Reyes "mans a cannon during the assault on El Presidio". Fiche L42: John drives off the reinforcements with the cannon. **Fiche is right**: Gates dialogues l.335 "(John takes down the reinforcements by manning a cannon.)", walkthrough l.40/50.
2. **Dutch.** Wiki Trivia/Personality: Reyes says he would have liked to meet Dutch, "had the latter not completely lost his mind and disappeared from public view several years ago". **Fiche is right** (L37, L80): the transcript has no such line.
3. **Who kills Luisa.** Wiki History implies Zubieta killed her ("in revenge for killing Luisa"); mission page "Deaths" says "Zubieta and two of his soldiers". Fiche L43: the soldiers guarding Reyes shoot her. **Fiche matches the walkthrough** (`An_Appointed_Time.txt` l.34: shot by two of the soldiers watching over Reyes). Keep; optionally note that the mission page credits Zubieta's men.
4. **"Marry a peasant" quote.** Wiki version contains "some peasant girl with a tight c*nt, and the hands of a farmer"; the transcript (Gates dialogues l.25) has no such words. **Fiche follows the transcript** (L60). Note: L60 stops before "My mother, qué Dios la cuide, will turn in her grave." That is fine (the mother line is paraphrased in L26), but there is no ellipsis marking the cut; add "[...]" or end the quote cleanly.
5. **"Now find your weapons and let's fight these dogs!"** (wiki) vs fiche L142 "Now find your weapons and fight these dogs!" **Fiche is right** (Cowards dialogues l.131).
6. **"Sarcasm should be beneath a man such as you"** (wiki) vs fiche L146 "Sarcasm, my friend...should be beneath a man such as you. Don't you think?" Fiche uses the transcript; fine.
7. **Nursemaid line** ("Abraham, one day everybody will know you", wiki, Train Robbery). Not in the transcript; fiche L27 attributes it to the wiki and says so. Correct handling.
8. **Executioner in Chuparosa.** Wiki: Reyes "snipes the executioner". Fiche L34: "kills the man about to shoot John". Neutral wording, compatible; no change.
9. **Seth steals the mask "a few months later"** (wiki) vs fiche L54 "three months later". **Fiche is right** (`_m/On_a_Pale_Horse.txt` l.26).
10. **Birth.** EN wiki "circa 1881" (from the GOTY guide's 30); FR wiki 1884 / 27 years. Fiche L12 gives the guide's 30 and the wiki's 1881 with attribution. Acceptable; no canon date exists.
11. **1914 article.** Wiki: Reyes "allegedly ordered soldiers to execute" protesters and "delayed democratic elections". The article (`_m/President_Reyes_Denies...txt` l.14) says neither: troops shot protesters, the order is not attributed, and Reyes says the path to democracy is slower than he wished. **Fiche L51 is right** ("The article does not say who gave the order").

## 3. Duplicates inside the fiche

| Fact | Occurrences | Keep | Action |
|---|---|---|---|
| Posters list (Casa Madrugada, Escalera x3, Tesoro Azul, Solomon's Folly, Benedict Point, Tumbleweed) | L99 (B) and L209 (C Trivia) | L99 | Cut L209; move its one extra detail ("in the alley leading to the shooting gallery") into L99. |
| Rebels replace the army / last Reyes' Rebels outfit piece on sale in Escalera | L102 (B) and L208 (C Trivia) | L102 | Cut L208. |
| Undead Reyes: thinnest Bruiser, only undead with two sets of sounds | L102 (B) and L212 (C Trivia) | L212 (Trivia, more detail) or L102 | Keep one; recommended: keep L102 (gameplay = B Skills), fold in L212's idle/charge detail, cut L212. |
| Semi-auto Shotgun, "Reyes brought protection" | L102, L104 (B) and L213 (C) | L102 | Cut the sentence from L213; L104 keeps only the weapon in the list. |
| Stagecoach drivers tied up / lasso on Bill makes Reyes shoot both | L101 (B) and L207 (C) | L101 | Cut the first two sentences of L207, keep only the rare Allende-in-the-brush case. |
| Reyes does not fight in "Must a Savior Die?" / "Train Robbery" | L101 (B) and L205 (C) | L101 | L205 keeps only the "hitting Reyes with the horse fails the mission" detail. |
| Pre-release screenshots: neater, shorter hair and goatee | L188 (D Development) and L200 (C Marketing) | L188 | Cut from L200 (keep "Rockstar released artwork and screenshots"). |
| Multiplayer model speaks of himself in the third person | L62 (B Names) and L198 (C Other media) | L62 | Cut from L198. |
| Herbert Moon "as revolutionary as Napoleon" quote | L94 (B relationship) and L137 (C Quotes) | L94 (quote rule: one place; it holds both Moon lines) | Cut L137-L138 from Quotes. |
| Luisa: his family disapproves of a peasant girl | L26 (A), L70 (B), L86 (B), L135 (C quote) | L135 quote + L26 | L70: pointer only; L86: cut. |
| Mother would turn in her grave | L26 (A) and L86 (B) | L26 | Cut from L86 (keep "see Biography"). |
| "Laura": he once knew another Laura | L45 (A) and L70 (B) | L45 | L70: one clause pointing to Biography, no retelling. |
| Dutch conversation (violent idealist, where is he now) | L37 (A) and L80 (B) | L37 | L80: one clause + "see Biography". |
| "Two old friends reunited" | L42 (A), L76 (B), L162 (C quote) | L162 quote + L42 | Cut the sentence from L76. |
| Corridos, over a hundred written about him | L37 (A), L57 (B), L99 (B) | L37 + L99 | Cut from L57 (or reduce to "see Propaganda"). |
| Ricketts: come back to Mexico like Landon, join his staff | L41 (A), L68 (B), L82 (B) | L41 + L82 | Cut the staff offer from L68. |
| Javier: bounty hunter, early revolutionary, from the province | L27 (A) and L76 (B) | L27 | L76 already says "see Biography"; trim the restatement. |

## 4. Summary for the correctors

**A (Biography)**
- L45: add "or both, if John fires at neither" (mission page l.53).
- L28: add the Ledger No. 56 line "It is this foresight and intelligence that has endeared him to a large section of Mexico..." (one sentence).
- Optional, attributed: wiki dating of Ledger No. 56 (late Oct 1911) and No. 213 (Nov 1914); Allende pushes Bill out at sword point.

**B (Personality, Names, Appearance, Skills, Relationships)**
- L59: add John's reply "You have all the makings of a great leader, Abraham." (transcript wording, not the wiki's "true leader").
- L60: mark the cut at the end of the quote ("[...]") or end it on a full sentence.
- Optional L64: no poncho in "An Appointed Time" (mission page), without the wiki's explanation.
- L99: absorb the shooting-gallery alley detail from L209. L102: absorb L212's idle/charge sound detail.
- Dedup: L57 (corridos), L68 (staff offer), L70 (family, Laura), L76 (Javier background, two old friends), L80 (Dutch), L86 (mother, family disapproval).

**C (Missions, Quotes, Trivia, Other media)**
- Quotes, Gates block: add "These peasant girls. They believe every word a fellow says. So naive! It's really quite charming. I love peasants." (Gates dialogues l.21).
- Quotes, Train Robbery block: add "A man like you, or me, with just a few such men, I tell you I could rule the entire country." and/or "Their energy... it is like food to me." (Train dialogues l.9).
- Cut L137-L138 (Moon quote, kept in B).
- Trivia: cut L208, L209, L212, L213 shotgun sentence; trim L205 and L207 to their unique details.
- L198: cut the third-person sentence. L200: cut the pre-release appearance sentence.

**D (base, Development, Reception)**
- Nothing to add. Do not add the FR wiki's age 27 / 1884. Keep L188 as the only place for the pre-release look.
