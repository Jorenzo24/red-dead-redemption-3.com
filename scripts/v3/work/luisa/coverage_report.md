# Coverage report: Luisa Fortuna (v3, medium tier)

Inputs: Red Dead Wiki EN (`en.txt`, 1 222 words raw wikitext; coverage.py counts the FR wiki at 373 words) and FR (`fr.txt`),
fiche `luisa_full_en.txt` (Lnn), mission transcripts in `scripts/v3/work/_m/`.

coverage.py: our fiche EN = 6 516 words, FR = 7 738 words. Wiki EN page (wikitext) = 1 222 words, i.e. roughly
**5.3x the EN wiki (about 530 %)**; coverage.py reports 729 % against its own wiki count. Biography 2 130,
Relationships 973, Quotes 890, Personality 470, Missions 432, Trivia 296, Other media 238, Reception 199, Development 194.

Overall the fiche covers every non-speculative fact of both wiki pages (infobox, history, 7 missions, trivia, multiplayer,
Undead Nightmare model, pre-release look, Alejandro Fortuna grave, Peasent alias). Gaps are a few verbatim lines.

## 1. Wiki facts missing from the fiche

| # | Wiki excerpt | Status | Recommendation |
|---|---|---|---|
| 1 | Quote: "My heart is breaking, but I cry for Mexico." | CONFIRMED, `Must_a_Savior_Die_dialogues.txt` l.11 (on the porch, after Roca Madera) | C Quotes: add the porch exchange ("I don't weep for myself, but for my country!" ... "My heart is breaking, but I cry for Mexico."). A L36 already paraphrases "weeps for her country"; keep A as paraphrase. |
| 2 | Quote: "... I have no family, just the cause. Please. Good actions make you a good man." | CONFIRMED, `Father_Abraham_dialogues.txt` l.48 | A L38 paraphrases everything except the last sentence. Either add "and tells him that good actions make a good man" in A (paraphrase) or add the full line in C Quotes (preferred: mission line). |
| 3 | Quote: "Great and terrible things! The revolution is coming! The country will be in turmoil once more. This time, we hope is the last time." | CONFIRMED, `My_Sister_s_Keeper_dialogues.txt` l.13 | A L34 paraphrases "the revolution is coming"; the "turmoil once more / last time" part is missing. Optional C Quotes entry. |
| 4 | Trivia: Reyes considered her "some peasant girl with a tight c*nt." | NOT IN TRANSCRIPT. The line in `The_Gates_of_El_Presidio_dialogues.txt` l.25 is "some peasant girl with the hands of a farmer". | Do not add the wiki wording (see §2). Optionally extend C Quotes L135 with the real l.17-25 exchange ("I just say she was incredible ... Marry a peasant? My dear boy, don't be absurd. I'm going to be the next president of Mexico ... some peasant girl with the hands of a farmer"); this would also make the "(see Quotes)" pointer in B L60 true. |
| 5 | FR wiki: "tuée par balle par trois d'entre eux" (three soldiers) | WIKI-ONLY version | Not needed; see §2 #1 (prefer trimming the list of versions in A L43 rather than adding a fourth). |
| 6 | Trivia: parallel with Katherine Anne Porter's "Flowering Judas" (a woman named Laura in love with a boastful revolutionary) | SPECULATIVE (editors' comparison, no Rockstar or critic source in hand) | Do not add. Could only enter D Reception if a published critic makes the comparison. |
| 7 | "appears to be less friendly with him after ... missions for the Mexican Army" | SPECULATIVE (wiki says "may explain") | Do not add. B L63 already gives the confirmed line ("cannot forgive you for helping Allende"). |
| 8 | "remains endlessly faithful ... no matter what Reyes says or does"; last name "ironic considering her death" | Interpretation | Do not add. |

Count: 3 confirmed lines worth adding (#1-#3), 1 optional real-transcript replacement (#4), 4 rejected (#5-#8).

## 2. Places where the fiche differs from the wiki

1. **How she is shot (A L43).** EN character page: Zubieta and his two men shoot her three times in the chest. EN mission page
   l.34: "shot by two of the soldiers watching over Reyes"; same page l.79: "Killed by Raul Zubieta and two of his soldiers".
   FR wiki: "trois d'entre eux". The dialogue transcript (`An_Appointed_Time_dialogues.txt` l.25-33) has no stage direction on
   the shooters. Nothing decides it: the fiche's neutral wording ("the soldiers guarding Reyes shoot her dead") is right.
   Suggest shortening the closing sentence of L43 to one line ("Red Dead Wiki pages disagree on how many soldiers fire and
   whether Zubieta shoots") instead of listing three versions; note the mission page contradicts itself.
2. **Reyes's crude line (wiki Trivia).** Wiki quotes "some peasant girl with a tight c*nt"; the transcript of "The Gates of
   El Presidio" (l.25) reads "some peasant girl with the hands of a farmer". Fiche is right not to use the wiki line.
3. **"At the behest of her brother Emilio" (wiki History) vs fiche B L65 "Ricketts learns of her capture from her brother
   Emilio".** Transcript `Landon_Ricketts_Rides_Again_dialogues.txt` l.11-27: Ricketts questions Emilio about Javier, Emilio
   only answers "No sé"/"Yo no se", then Ricketts tells John "they do have his sister". Neither the wiki's "behest" nor the
   fiche's "learns ... from Emilio" is shown. Fix L65: "Ricketts, who has been questioning her brother Emilio about Javier,
   tells John the army holds her" (A L31 already says it this way).
4. **Sister's departure (wiki: "so she can escape to the Yucatan").** Transcript: "We are sending her to work for a kind man
   in the Yucatán" (C L117). Fiche (A L35, B L78) is more exact; keep.
5. **Father Abraham ambush (wiki: Luisa "persuades him to join a guerrilla attack on the Army to avenge her father").**
   Transcript l.44: Reyes "asked personally" that John stop Allende's reinforcements on the old trail. Fiche (A L38) is right.
6. **Sepulcro (wiki: she "organizes an assault on Sepulcro in order to kill Captain de Santa").** Transcript
   `Captain_De_Santa_s_Downfall_dialogues.txt` l.3: De Santa is sent to oversee a massacre, she sends her men to stop it and
   kill him, and stays at the camp. Fiche (A L41) is right.
7. **Internal accuracy, A L37:** "She tells John that the revolution will live on thanks to him and cries out for Mexico."
   At the river she says "Viva México!" (`Must_a_Savior_Die_dialogues.txt` l.109); "I cry for Mexico" is the porch line
   (l.11). Reword to "and shouts 'Viva México!'" (or "cheers Mexico") so it is not confused with the porch line.

## 3. Duplicates inside the fiche (per OWNERSHIP.md)

Broken pointers first (B points to Quotes, but the line is not in Quotes):
- L59 "married in their hearts ... (see Quotes)": only in A L36. Change to "(see Biography)".
- L60 "laughs at the idea of marrying a peasant (see Quotes)": C L135 stops before that line. Either extend L135 (§1 #4) or point to Biography.
- L62 "cynic ... (see Quotes)": only in A L34. Point to Biography.
- L63 "people like Luisa who gave their lives (see Quotes)": C L139 starts after that line. Point to Biography.
- L66 "jokes ... (see Quotes)": only in A L33. Point to Biography.
- L68 "pure evil ... cut his heart out (see Quotes)": not in Quotes and not in A (Father Abraham l.78). Either add the line to C Quotes or drop the parenthesis (B may keep the paraphrase).

Facts told twice:
1. Never rides a horse: B L90 and C Trivia L160. Keep B L90, cut L160.
2. Mission failure conditions: B L91 and C Trivia L161. Keep B L91, cut L161.
3. Wagon crash when the ride is watched: B L90 and C Trivia L162. Keep B L90, cut L162.
4. Body cannot be looted: B L91 and C Trivia L166. Keep in L166 (with the fall-on-back detail) and cut from L91, or vice versa; once only.
5. Official-site background image (FR wiki): D L145 and C Marketing L156. Keep D L145 (with the Newswire post), delete the C "Marketing" subsection.
6. Church prayer in Chuparosa: A L33 and B L49. Keep A L33, cut from L49.
7. "She can fight as well as any man" quoted twice: B L48 and C L133 (also paraphrased A L27, pointer B L86). Same line in two quoted places: keep C L133 (mission line), cut the Victor sentence from B L48 (B keeps the Newswire description).
8. "How do you know my young lover, Laura?" quoted in B Names L53 and C L121; "Laura's Day" quoted in L53 and C L139. Keep the full exchanges in C, paraphrase them in L53 without quotation marks (keep "Laura, dame la fuerza..." and "Mi amiga" quoted in L53, they are not in C).
9. "Stays at the camp" (De Santa mission): A L41, B L70, B L91, C L101. Keep A L41 and the table L101; cut from L70 and L91.
10. Explosives at Frontera Bridge: A L40 and B L91 retell the same detail (no experience, John places charges, she watches from the ridge). Keep A L40; B L91 one clause with pointer.
11. Javier question after the rescue: A L32, B L72 (retold verbatim), C L111 (quoted). Keep A paraphrase + C quote; L72 shortened to one clause with "(see Quotes)".
12. Thanks "friends of the people of this land": A L32, B L62, C L111. Cut from L62 (pointer).
13. Ricketts "talk to Luisa, she is well connected": A L33, B L66, C L115. Cut from L66.
14. Agave Viejo scene: A L42 and B L60 (retold) and C L105 (table, fine). Shorten L60 to one clause.
15. Miranda sent to the Yucatán, "too young for revolution": A L35, B L78, C L117. Shorten L78.
16. Mother in the US / thanks for helping her and Miranda escape / neither knows of the father's death: A L38-L39 and B L82 (retold), plus B L80 ("wishes she had sent him away"). Shorten L80 and L82 to pointers.
17. Emilio driver/stagecoach/eldest: A L26 and B L76. Keep in B L76 (family entry), keep one clause in A L26.
18. Son's name Jack: A L39, B L63 and B L74 (both), C L129, C L164 (trivia: first mission he says it). Keep B L74 (Jack entry) and drop the name from L63; L164 can stay (distinct fact).

## 4. Summary for the correctors

**A (Biography)**
- L37: "cries out for Mexico" -> "shouts 'Viva México!'" (§2 #7).
- L38: add the paraphrase "good actions make a good man", unless C takes the line (§1 #2).
- L43: compress the three wiki versions of the shooting to one sentence noting the wiki pages disagree (§2 #1).
- L26: keep only one clause on Emilio (details live in B L76).

**B (Personality, Names, Relationships, Skills)**
- Fix six broken "(see Quotes)" pointers: L59, L60, L62, L63, L66, L68 (§3).
- L65: replace "learns of her capture from her brother Emilio" with the transcript wording (§2 #3).
- L48: cut the Victor quote (kept in C L133). L49: cut the church prayer (kept in A L33).
- L53: paraphrase "my young lover, Laura" and "Laura's Day" (kept in C).
- Shorten retellings: L60, L62, L66, L70, L72, L78, L80, L82; L63 drop Jack's name (kept in L74).
- L91: drop "stays at the camp", the explosives retelling, and either the "cannot be looted" sentence or its trivia twin.

**C (Missions, Quotes, Trivia, Other media)**
- Quotes: add the porch line "My heart is breaking, but I cry for Mexico" (Must a Savior Die? l.11) and "Good actions make you a good man" (Father Abraham l.48); optionally "Great and terrible things!..." and "Allende es pura maldad ... One day I will cut his heart out" (Father Abraham l.78, fixes B L68).
- Optionally extend L135 with Reyes's real lines (l.17-25, "hands of a farmer"), never the wiki's crude misquote.
- Trivia: cut L160, L161, L162 (owned by B); keep only one of L166/L91 for "cannot be looted".
- Other media: delete the "Marketing" subsection L156 (owned by D L145).

**D (base, Development, Reception)**
- No additions. Keep the site-background note in L145 as the single occurrence.
