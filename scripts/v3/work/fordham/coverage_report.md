# Coverage report: Archer Fordham (v3, medium tier)

Wiki EN: 1,646 words (raw wikitext; coverage.py counts the prose sections), wiki FR: 609 words (coverage.py).
Our fiche EN: 5,662 words per coverage.py (5,642 by wc on fordham_full_en.txt). Ratio EN: **441 % of the wiki** (coverage.py).
Section counts (coverage.py): Biography 2,357; Personality 453; Relationships 426; Weapons and the automobile 241;
Missions 477; Quotes 568; Development and performance 354; Other media 148; Trivia 246; Gallery 53.

Coverage is near complete: every History, Mission appearance, Trivia and Gallery fact of the EN wiki is present or
deliberately excluded with a reason in the part docstrings. The real gap is the Quotes section (see 1.1 and 3.1).

## 1. Wiki facts missing from the fiche

| # | Wiki excerpt | Status | Recommendation |
|---|---|---|---|
| 1 | Quote box (headline): "Marston, you're a public menace. We should've had you killed." | CONFIRMED (And_You_Will_Know_The_Truth_dialogues l.9) | Paraphrased at L43 only, quoted nowhere. Part C docstring says it was left to B, but B never quotes it. Add to C Quotes (And You Will Know The Truth). |
| 2 | Quotes: "Like you always say, sir, the higher the stakes, the smarter you have to play the game." | CONFIRMED (Bear One Another's Burdens dialogues) | Paraphrased at L37 only. Add to C Quotes. |
| 3 | Quotes: "It ends when we say it ends. You're in no position to make demands." | CONFIRMED (Bear One Another's Burdens dialogues) | Paraphrased at L37 only. Add to C Quotes. |
| 4 | Quotes: "See, this is what happens when you fraternize with savages. How could you ever follow a man like that?" | CONFIRMED (And_The_Truth_Will_Set_You_Free_dialogues l.31) | L52 (B) says "see Quotes" but the line is not in Quotes. Add to C Quotes, with "Van der Linde is a psychopath. A murderer and a rapist." (l.33) as a second line if wanted. |
| 5 | (transcript, not wiki prose) John: "Dutch was a good man once, a far better man than you." | CONFIRMED (same file, l.34) | L75 (B, Dutch entry) says "see Quotes" but it is absent. Add to C "What others say to him", or drop the "(see Quotes)" pointer. |
| 6 | FR wiki trivia: unused NPC line "I hear that Bureau fella's never been the same since his mother got shot in the massacre" | WIKI-ONLY (FR wiki, game files); the link to Fordham and to the 1899 massacre is the wiki's inference = SPECULATIVE | Part C docstring routes it to D (cut content) but D's cut-content paragraph (L142-143) does not have it. Either add to D, attributed to the FR wiki, quoting the line and saying it names no one (no massacre inference), or list it explicitly as excluded. Optional. |
| 7 | FR wiki: mother named "Maybelle Foreman" (vs EN "Maybelle Fordham") | WIKI-ONLY, conflicting | Excluded in B docstring. Fine; optionally one clause in A Origins noting the FR wiki spelling. Not required. |
| 8 | Infobox affiliations: Blackwater Police Department, U.S. Marshals (FR: also U.S. Army as ally) | WIKI-ONLY (infobox) | Facts grid could list "Affiliation: Bureau of Investigation; works with the Blackwater police, marshals and the Army (Red Dead Wiki)". Part D. Optional. |
| 9 | Ending Credits page: "Ross instructs Fordham to search the cabin while he investigates the corpse" | WIKI-ONLY (Ending Credits page, no transcript) | L26 says Fordham goes inside; add "on Ross's instruction". Part A, one clause. |
| 10 | Appearance 1907: "a young man with a clean-shaven face" | WIKI-ONLY (visible in-game) | Add "clean-shaven" to L58 (Part B Appearance). |
| 11 | Transcript, Cochinay ride: Fordham asks "So, what made him this way?" / "Make no mistake, we have been watching." | CONFIRMED (l.35, l.41) | L45 already says the Bureau has been watching. The "what made him this way" exchange (John: "Bastards like you") is missing; one clause in A L45 if wanted. Optional. |
| 12 | Gates of El Presidio (killed branch): Fordham "snickers"; captured branch "get in the damn automobile!" | CONFIRMED (dialogues) | Covered in substance (L33-34). No action. |

Not added, on purpose (correctly excluded by the parts): wiki Personality ("hot-headed and impulsive", "develops a
respect of sorts for Marston"): interpretation. Trivia contrast with Ross ("deceitful vs honest and blunt"):
interpretation (only the height difference is kept, L58). 1911 "immodest, lighter three-piece suit": see 2.2.
"Leave to plan their next move" (1907): interpretation. Ford Model T (FR infobox): unsupported.

## 2. Places where the fiche differs from the wiki

2.1 **End of "And The Truth Will Set You Free"**. Wiki History: Fordham and Ross inform John "that he is free to return
to his ranch, where his family is waiting". Fiche L46: Ross (after a joke about a prison riot) tells John the family
was sent back to Beecher's Hope; Fordham only thanks him. **Fiche is right**: And_The_Truth_Will_Set_You_Free_dialogues,
last lines (Ross: "I'm only joking, dear boy. They were sent back to that scrabble ranch of yours in Beecher's Hope").
Optional: L46 could mention the "prison riot" joke (A), it is in the transcript.

2.2 **1911 suit**. Wiki Appearance: "an immodest, lighter three-piece suit"; wiki Trivia (same page): "Fordham wears
dark clothes" vs Ross's light clothes. The wiki contradicts itself. Fiche L58: dark suit with waistcoat in both games.
Part B docstring says the live portrait shows a dark jacket. **Fiche kept the visually checked version**; acceptable.

2.3 **Presence in "The Last Enemy That Shall Be Destroyed"**. EN wiki: present (barn doors, Dead Eye, may vanish).
FR wiki: absent, the man is Isaac McKinnon. Transcript names no one. Fiche L47 and L154 attribute both readings.
**Undecidable from text sources**; the fiche's hedged treatment is correct. Facts grid L12 "he can be shot at Beecher's
Hope" is stated a bit more firmly than L47; keep the attribution ("according to the mission page") as it is.

2.4 **Joining the Bureau**. EN wiki: joined in 1907 on its foundation, Ross's protégé; FR wiki: before 1907. Fiche L22
gives both, attributed. Correct.

2.5 **Exodus in America**. Wiki: Ross and Fordham escort John to the station. Transcript: "two lawmen", unnamed;
mission page names Ross and Fordham. Fiche L31 hedges correctly.

2.6 **Valentine saloon (credits)**. Wiki gallery caption: they "question Smithfield". Ending Credits page: the bartender
points them to a woman and Morris Peyton. Fiche L27 follows the Ending Credits page. Fiche right (A docstring logs it).

No factual error found against the transcripts.

## 3. Duplicates inside the fiche (OWNERSHIP.md)

3.1 **Quotes in B and C**: "Our armed forces have no equal..." and "And this isn't much more than a simple
prototype..." are quoted in B "In his own words" (L54) AND in C Quotes (L116, L118). Rule: one place; mission lines
prefer C. **Keep in C, remove from B** (B keeps "I don't understand you people..." and "There's always somebody
watching..."). In exchange, C takes the four wiki quotes of section 1 (items 1-4).

3.2 **"office clerk or social secretary or some such"**: quoted in B Names (L56) and C "What others say" (L127), also
paraphrased L39. **Keep the quote in C (L127); B Names paraphrases without quotation marks.**

3.3 **Ignition / crank of the car**: B "Behind the wheel" (L84) and Trivia (L151), same mission-page sentence.
**Keep L84 (B Skills), cut L151 (Trivia).**

3.4 **Mission failure conditions**: B "In the game" (L86) and the Missions table (L93-95) list the same conditions;
L88 also says "Several missions fail...". **Keep them in the C table; L86 reduces to a pointer** ("several missions
fail if John attacks him, see Missions") plus the only new fact (Ross cannot be killed in the final mission, if
sourced). The Dead Eye fact is in L9, L12, L47, L86, L97: keep A L47 + C table L97 + grid; cut it from L86.

3.5 **Pinkerton badge 1907**: B Appearance (L58: "a badge is pinned to his lapel") and Trivia (L152: Ross and Fordham
both wear Pinkerton badges despite Ross heading the Bureau). Trivia holds the new fact (it is a Pinkerton badge, and
the inconsistency). **Keep L152; L58 can drop the badge or say "a Pinkerton badge (see Trivia)".** L143 (unused 1899
Pinkerton model) is a different fact.

3.6 **"we're the bad guys"**: B Names (L56, Ross uses "Archer" when he says he and Archer are the bad guys) and B
Relationships Ross (L61, "counts him on his own side when he tells John that the two of them are the ones who enforce
the rules"). Same scene twice in B, both paraphrased; tolerable, or trim L61's clause.

3.7 **Wiki vs FR wiki on the last mission**: told fully in L47 and again in L154. L47 should keep the EN wiki
details and point to Trivia for the McKinnon/FR-wiki dispute ("see Trivia" already present); drop "The French-language
wiki says he does not take part in the mission" from L47 or the last sentence of L154.

3.8 **Weapons**: grid (L17) + B Weapons (L82). Fine (grid allowed).

3.9 **Broken pointers** (not duplicates but same fix): L52 "(see Quotes)" for "savages and insane" and L75 "(see
Quotes)" for John's "better man" reply point to lines that are not in Quotes. Fixed by items 1.4, 1.5 (or remove the
pointers). Note "insane" ("That man is insane", l.7) is also not quoted anywhere.

## 4. Summary for the correctors (by part)

**A (Biography)**
- L26: Fordham searches the cabin on Ross's instruction (Ending Credits page).
- L47: trim the FR-wiki sentence, keep "see Trivia" (3.7).
- Optional: L45 add the "what made him this way?" exchange; L46 add Ross's prison-riot joke before the real answer.

**B (Personality, Names, Appearance, Skills, Relationships)**
- L54: remove the two "armed forces / prototype" quotes (kept in C).
- L56: paraphrase the "office clerk" line without quotation marks (kept in C).
- L58: add "clean-shaven"; badge -> "a Pinkerton badge (see Trivia)" or drop.
- L52 / L75: keep "(see Quotes)" only if C adds the lines below; otherwise remove the pointers.
- L86: cut the failure conditions and the Dead Eye fact, point to Missions.
- L61: optional trim of the "enforce the rules" clause (told in Names).

**C (Missions, Quotes, Trivia, Other media)**
- Quotes, add (all CONFIRMED in transcripts): "Marston, you're a public menace. We should've had you killed." (And You
  Will Know The Truth); "Like you always say, sir, the higher the stakes, the smarter you have to play the game." and
  "It ends when we say it ends. You're in no position to make demands." (Bear One Another's Burdens); "See, this is
  what happens when you fraternize with savages. How could you ever follow a man like that?" (And The Truth Will Set
  You Free); optionally "That man is insane."
- "What others say": add John's "Dutch was a good man once, a far better man than you." (And The Truth Will Set You Free).
- Trivia: cut L151 (ignition, told in B L84).
- Fix the docstring note ("lines left to B") to match what B actually quotes.

**D (base, Development)**
- Optional: cut content, the FR wiki's unused NPC line about the "Bureau fella" whose mother was shot in a massacre,
  quoted and attributed, stating that it names no one (no 1899 inference). Or record it as excluded.
- Optional: facts grid affiliation line (Blackwater police, U.S. Marshals, Army, per the wiki infobox).
