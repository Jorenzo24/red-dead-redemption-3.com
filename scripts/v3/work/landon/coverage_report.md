# Coverage report: Landon Ricketts (v3, medium tier)

Compared: Red Dead Wiki EN (en.txt, 2 689 words raw; coverage.py counts the article body) and FR (fr.txt, 1 132 words)
against landon_full_en.txt (L-numbers). coverage.py: our EN 6 895 words = **310 % of the wiki EN**; FR 8 057 words
(711 % of the FR wiki). Sections: Biography 2 305, Personality 540, Relationships 696, Gunfighting 340, Missions 405,
Quotes 869, Development 200, Reception 206, Other media 645, Trivia 316.

Overall: coverage of the wiki is near complete. Every narrative paragraph, mission, newspaper, RDR2 / RDO / multiplayer
reference and almost every trivia item is present. What is missing is either speculative (left out on purpose) or
small wiki-only gameplay trivia.

## 1. Wiki facts missing from the fiche

| # | Wiki excerpt | Status | Recommendation |
|---|---|---|---|
| 1 | Ledger No. 55: "amongst many other rumored and verified killings" (the wiki quotes the article; our L26 summarises it without this clause) | CONFIRMED (fc/Landon_Ricketts_Rumored_Alive.txt, newspaper text) | A, L26: add one clause ("the article adds that he is credited with many other killings, some rumored, some verified"). |
| 2 | Lucky in Love mission page, trivia: "Ricketts may sometimes say he knows the girl the stranger is holding hostage" | WIKI-ONLY (_m/Lucky_in_Love.txt; no line in the transcript) | C Trivia (RDR section), attributed to the mission page. |
| 3 | Zombie Ricketts: "He has a 1/4th chance appearing alongside zombies in regular hordes" | WIKI-ONLY (character page) | C, L203: add the frequency, attributed ("according to the Red Dead Wiki, about one in four hordes"). Optional. |
| 4 | Two Landons in "Biographies and Lies" (character page: if Merche Coronado is rescued for Missing Persons before the mission; mission page Glitches: one acts normally, one sits smoking in a chair) | WIKI-ONLY (_m/Biographies_and_Lies.txt, Glitches) | C Trivia (Undead Nightmare), one sentence, attributed. Keep the Merche Coronado trigger attributed to the character page. |
| 5 | Jack's combat line "My pa knew Landon Ricketts, friend!" (not on the Ricketts page but on Jack's quote list; already in jack_C.py) | WIKI-ONLY (quote list), consistent with Jack fiche | B, Jack Marston entry (L75): add it next to "eat your heart out" so both fiches agree. Optional. |
| 6 | Jack fiche trivia: in "Wolves, Dogs and Sons" John gives Jack the same tense-back advice Ricketts gives him (jack_C.py L404) | CONFIRMED in Jack fiche (transcripts) | C Trivia (RDR), one line, same wording as jack_C. Optional. |
| 7 | Irish (We Shall Be Together in Paradise): "Guy here, not funny, but he's real nice" | CONFIRMED (fc/We_Shall_Be_Together_in_Paradise_dialogues.txt) | B, Irish entry L73: optional half-clause. Low value. |
| 8 | Multiplayer quotes: 6 more lines ("Don't worry, this'll be all over soon", "This ends right now!", etc.); UN "If you see me when I was so fast, you couldn't see me" | WIKI-ONLY (quote list); UN line is garbled | Do not add (4 MP lines already quoted; the garbled UN line is unusable). |
| 9 | Trivia General: modelled on Wyatt Earp (autobiography parallel), resembles Wild Bill Hickok, possibly named after Michael Landon, inspired by Frank Talby / Lee Van Cleef (Day of Anger) | SPECULATIVE (wiki editors' comparisons, no source) | Do not add. (The red sash, the only observable detail, is already in L57.) |
| 10 | Trivia RDR: "In The Gunslinger's Tragedy, Landon claims that he has never been married" | NOT SUPPORTED: no such line in _m/The_Gunslinger_s_Tragedy_dialogues.txt | Do not add (see section 2). |
| 11 | Background: "The massacre was allegedly part of the reason Ricketts chose to move to Chuparosa" | SPECULATIVE (neither Ledger article says so) | Do not add. |
| 12 | FR wiki: "John Marston mentionne que Ricketts était l'homme le plus rapide de l'Ouest" | NOT SUPPORTED (John only says men argue over who is fastest; it is Ricketts who bets he is) | Do not add. |
| 13 | FR wiki allies: Irish "(anciennement)" | SPECULATIVE (Irish never names him) | Do not add; L73 already hedges. |

## 2. Places where the fiche differs from the wiki

1. **"Never been married" (EN wiki trivia)**: the fiche ignores it. The transcript of "The Gunslinger's Tragedy" has no such
   line; the only marital line is "Thank God my wife died" in "Lucky in Love" (_m/Lucky_in_Love_dialogues.txt L11).
   Fiche is right.
2. **Sanchez / the Stranger (L37)**: the wiki character page writes "[[The Stranger|Sanchez]]", i.e. one person. The
   transcript only has Müller say "Sanchez will be my second" and separately names "The Stranger" (who folds at the table
   and later takes the hostage); the mission page calls the Stranger "a friend of Müller". Our L37 introduces "the
   Stranger", then drops "with Sanchez as his second" as if Sanchez were a new person, which reads as a contradiction.
   Fix (A): "and names a man called Sanchez as his second; the Red Dead Wiki identifies him as the Stranger".
3. **Reason for moving to Mexico**: wiki says the massacre was "allegedly part of the reason". Neither Ledger article
   (fc/Landon_Ricketts_Rumored_Alive.txt, Landon_Ricketts_Dead.txt) says so. Fiche (L26-27) is right.
4. **Date of death**: wiki says "a week before Remember My Family" and "returned in 1911 (presumably after The Mexican
   Wagon Train)". The Ledger No. 213 says only "died last week" and "returned to the US three years ago". Fiche (L44)
   follows the article. Fiche is right; the wiki adds an inference.
5. **Who proposes the duel (Lucky in Love)**: the mission page says "Ricketts convinces Müller to accept a duel"; the
   transcript has Müller propose it ("Outside, winner takes the pot"). Fiche L37 follows the transcript. Fiche is right.
6. **Playing cards under the table**: character page says "secret card", mission page "cheat card ... since he has
   already beaten Müller". Fiche (L195) reports only what is visible. Right per the no-interpretation rule.
7. **Undead lookalike**: character page says it "behaves as a Bolter"; the Undead Nightmare page says "Bolters and
   Retchers ... the Retchers having differences in design" (fc/Undead_Nightmare.txt L225). Fiche L203 follows the UN page.
   Both are wiki-only; fine as attributed.
8. **Seven taunts (L190)**: Myths and Mavericks page says the pack's characters "only have 7 taunts"
   (fc/Myths_and_Mavericks.txt L64), but the Ricketts page lists ten multiplayer lines. The fiche states seven as fact.
   Fix (C): attribute it ("according to the wiki's Myths and Mavericks page") or cut the sentence.
9. **FR wiki, Undead Nightmare**: "Il faudra alors abattre ce Ricketts zombifié". He is not undead when he attacks after
   the mission (EN page, L202). Fiche is right.
10. **FR wiki, farewell**: "souhaitant bonne chance ... dans sa quête de la rédemption". Transcript: he hopes John finds
    what he is looking for. Fiche L41 is right.
11. **Cross-fiche consistency (not a wiki difference)**: john_D.py relationship entry for Ricketts says "the two attack
    Mexican Army patrols together". No mission shows patrols; they fight the soldiers at the caves near El Matadero and
    the prison convoy. Recommend rewording john_D (EN + FR) to "fight Mexican soldiers together to free Luisa Fortuna and
    a convoy of prisoners".

## 3. Duplicates inside the fiche

| # | Fact | Occurrences | Keep | Cut / change |
|---|---|---|---|---|
| 1 | John mentions Ricketts at a camp poker game (RDR2) | L61 (B John) and L184 (C Other media) | L184 | Cut the sentence from L61. |
| 2 | Playing cards on his right thigh at the poker table | L93 (B Weapons) and L195 (C Trivia) | L195 | Cut from L93 (not a weapon / skill). |
| 3 | "Nearly invincible" in Landon Ricketts Rides Again | L91 (B) and L197 (C Trivia) | L91 (gameplay = B Skills) | Cut L197. |
| 4 | Rockstar reused single-player lines out of respect for Hagen | L176 (D) and L190 (C) | L176 | Cut the sentence from L190 (keep a pointer at most). |
| 5 | "Only a buzzard feeds on his friends." | L52 (B own words) and L117 (C) | L117 (mission line, C) | B paraphrases or picks another line. |
| 6 | "I didn't say I'd become a coward. I'm not going to stand by..." | L52 (B) and L119 (C) | L119 | B paraphrases (A L27 already does). |
| 7 | "Landon Ricketts. Not a name that means much anymore." | L55 (B Names) and L113 (C) | L55 (name line, B Names owns it) | Cut L113-114 from Quotes. |
| 8 | "You know, you remind me a lot of myself... Stubborn and angry." | L53 (B) and L139 (C) | L139 | B paraphrases; L53 keeps the "charmed life" line (not in C). |
| 9 | "Thank God my wife died. Unlucky in love, lucky in cards." | L79 (B wife) and L127 (C) | L127 | L79 paraphrases ("he jokes at the poker table that his wife's death has brought him luck at cards"). |
| 10 | "A new pair of pants and you think you're Landon Ricketts" | L77 (B Sadie) and L107 (C mentioned-missions table) | L77 | L107 paraphrases without quotation marks. |
| 11 | How Ricketts addresses John (partner, Mr. Marston, sarcastic little apprentice) | L60 (B John) and L52/L55 (B own words / Names) | L55 Names | Move the list from L60 into Names, or cut from L60. |
| 12 | John tells him how he left the gang (Wagon Train) | L39 (A) and L60 (B John) | L39 | L60: "see Biography" pointer only. |
| 13 | Bottle and vulture training / Schofield / Dead Eye 3 | L32 (A), L90 (B), L95 + L98 (C), L5 (key facts) | A for the scene; L90 for the gameplay detail (marks three bottles, at least two vultures) | L90: drop the retelling of the scene ("he hands John... keep his back straight") already in A, keep the Schofield quote and the Dead Eye mechanics. L95 and L98 both list the reward: keep L98 (table), cut it from L95. |
| 14 | Ramon calls him the savior of the town | L27 (A), L50 (B quote), L87 (B Ramon) | L50 quote + L87 | A L27 keeps it as a short clause (acceptable); no action needed beyond not adding more. |
| 15 | Released 2010 / Undead Nightmare / played by Ross Hagen | L3 intro and L174 (D) | both (intro summary is allowed) | No action. |

## 4. Summary for the correctors

**A (Biography)**
- L26: add the Ledger No. 55 clause "amongst many other rumored and verified killings" (paraphrased).
- L37: fix Sanchez: "names a man called Sanchez as his second; the Red Dead Wiki identifies him as the Stranger".

**B (Personality, Names, Relationships, Skills)**
- L52, L53: replace quoted lines that are also in Quotes ("buzzard", "coward", "remind me of myself") with paraphrase,
  keep "Living quietly, waiting", "sarcastic little apprentice" and "charmed life" exchanges.
- L60: cut the list of names (belongs in Names L55), cut the retelling of the gang story (pointer), cut the RDR2 camp
  poker sentence (L61; kept in L184).
- L79: paraphrase the wife line (quoted in L127).
- L90: trim the scene retelling, keep the Schofield quote and Dead Eye mechanics.
- L93: cut the playing-cards sentence (kept in L195).
- L75 (optional): add Jack's "My pa knew Landon Ricketts, friend!" (consistent with jack_C).

**C (Missions, Quotes, Trivia, Other media)**
- Quotes: cut L113-114 (Names owns it); keep L117, L119, L127, L139 (B paraphrases them).
- L95: drop the reward list (kept in table L98).
- L107: paraphrase the Sadie line (quoted in L77).
- L190: attribute "seven taunts" to the wiki's Myths and Mavericks page (or cut); cut the Hagen-respect sentence (in L176).
- L197: cut (in L91).
- Trivia adds (attributed, WIKI-ONLY): Ricketts may say he knows the hostage (Lucky in Love mission page); two
  Landons in the Biographies and Lies cutscene (glitch; Merche Coronado trigger per the character page); optional
  "about one in four hordes" for the lookalike (L203); optional tense-back parallel with Jack (same wording as jack_C).

**D (base, Development, Reception)**
- No change. Development and Reception cover everything the wiki has (Hagen, Myths and Mavericks) plus external sources.

**Other fiche**
- john_D.py, Landon Ricketts relationship (EN + FR): replace "attack Mexican Army patrols together" with the actual
  fights (the caves near El Matadero, the prison convoy); regenerate John's HTML.
