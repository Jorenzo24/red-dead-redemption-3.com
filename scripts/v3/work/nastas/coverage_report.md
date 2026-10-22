# Coverage report: Nastas (v3, medium tier)

Wiki EN page: 1 179 words raw (coverage.py counts sections after stripping markup). Our fiche: 4 947 words EN
(coverage.py: **507 % of the wiki**), 5 717 words FR (650 % of the FR wiki).
Section scores from `python3 scripts/coverage.py nastas "Nastas"`: every wiki section has a counterpart
(History -> Biography; Undead Nightmare -> h3; Mission appearances -> Missions; Murders -> Weapons; Quotes +
Multiplayer -> Quotes; Trivia -> Trivia / Names / In the game; Gallery -> Gallery).

## 1. Wiki facts missing from the fiche

| # | Wiki excerpt | Status | Recommendation |
|---|---|---|---|
| 1 | Quotes: "For a wise man, you are a very stupid man, mister." (Nastas criticizing MacDougal) | CONFIRMED, transcript `_m/At_Home_with_Dutch_dialogues.txt` l.170 | The line is NOT quoted anywhere, yet L43 (Personality) and L55 (MacDougal) both say "(see Quotes)". Part C: add it to Quotes (At Home with Dutch, after MacDougal's Yale story), in place of the duplicated "Enjoy it while you still can..." (see §3, D1). |
| 2 | Multiplayer taunts "Come on, then!", "Stay and fight!", "I don't care who you are!", "You shouldn't have done this!" | WIKI-ONLY (wiki list of lines) | Optional. Part C: the fiche says "a few of which are quoted above" (L133); either add the four remaining lines to the Multiplayer quote block (attributed to the wiki, like the three already there) or leave as is. Low priority. |
| 3 | Trivia: "When Nastas dies and the cutscene ends, if the player were to look at his body, his face would sometimes become deformed. This is the result of a glitch." (+ gallery caption "Strange looking face as the result of a visual glitch") | WIKI-ONLY | Part C, Trivia: one line, attributed ("According to the Red Dead Wiki, ..."). |
| 4 | Mission page "At Home with Dutch" trivia: Nastas's Tobiano Pinto sometimes stays in a canter while the other two horses gallop (glitch) | WIKI-ONLY (`_m/At_Home_with_Dutch.txt` l.98) | Optional. Part B, Horses: one clause after the Tobiano Pinto sentence (L71). Low priority. |
| 5 | Background: "It can be assumed that he agreed to infiltrate the gang in an attempt to 'rescue' his tribesmen" | SPECULATIVE (wiki's own hedge; no line in any transcript says he infiltrated the gang) | Do not add. |
| 6 | Trivia: modelled on an Apache rather than Navajo; buffalo hunted by Apache and Comanche; Athabaskan languages | SPECULATIVE | Do not add (fiche L139 already says the games never name his tribe). |
| 7 | "Marston identifies with this..."; "John appears to sympathize with Nastas"; "John appears to view Nastas with respect" | Interpretation | Do not add. |
| 8 | Undead Nightmare: "This hints towards Undead Nightmare taking place in an alternate timeline" | Interpretation | Do not add (L40 already reports the factual part: neck bite wound, survived the cabin per the expansion page). |
| 9 | FR wiki: Nastas says he likes the professor because "c'est un grand homme, au fond" | Not found in any transcript (grep "great man / good man / heart" in the three dialogue files) | Do not add. |
| 10 | FR wiki: Nastas is "un ancien membre de la bande" who infiltrated it | Contradicted by silence of the transcripts | Do not add (see §2). |
| 11 | FR wiki trivia: comparison with Eagle Flies (both killed, both sympathize with protagonists...) | Interpretation | Do not add. |

All other wiki facts are covered: reservation + boarding-school education (L23, attributed), informant for the Bureau
(L24), Serendipity trap and car escape (L28-29), arguments with MacDougal on buffalo / forests (L31), "There is no
respect for the land anymore" (L45), MacDougal's Yale/natives exchange (L34), Enepay's shot and John's revenge (L36),
Ledger notice (L37), Undead Nightmare (L39-40), miner killed in self-defense (L32, L69), flute (L69), bastard line
(L73), loot 4-7 dollars (L73), Hassun/Chogan (L144), shared voice actor (L123), pronunciations (L47), moccasins
(L49), Navajo name meaning (L47), Myths and Mavericks (L133), mission list (L78-81), bump line (L99), last words (L97).

## 2. Places where the fiche differs from the wiki

1. **Ledger tribute wording.** Wiki: "May you find God, dear friend". Fiche L37: "May you find God, my dear friend."
   **Fiche is right**: in-game text of Blackwater Ledger No. 59, Miscellany column (ireddead newspapers guide,
   `work/reyes/fc/ireddead_newspapers.html`): "Nastas (Surname Unknown), of Indian descent, has passed away at Bear
   Claw Cabin in Tall Trees. May you find God, my dear friend. Prof. Harold MacDougal Esq." (Note: the twin file
   `work/nastas/fc/ireddead_Ledger_No59_text.txt` is truncated after its header; the HTML copy is the one to cite.)
2. **Where the bullet hits.** Wiki: "shot in the face". Fiche L36: "shoots him in the head". **Fiche is right**:
   transcript `_m/For_Purely_Scientific_Purposes_dialogues.txt` l.101 "(Enepay shoots Nastas in the head, killing
   him)"; the mission page says "forehead". Keep "head".
3. **Date of the tribute.** FR wiki: 1914. Fiche L37 already notes the discrepancy and places it in 1911 (issue
   No. 59, sold after "The Prodigal Son Returns (To Yale)"). Fiche is right; keep as written.
4. **Infiltrator / former gang member.** EN wiki "it can be assumed" he infiltrated the gang; FR wiki states he was
   a former member who infiltrated it. No transcript says so: in "Bear One Another's Burdens" he is "our informant"
   (Fordham); in "At Home with Dutch" he only says that friends of his ride with Dutch. Fiche (L24 "The games never
   show how he came to work for them") is right.
5. **Who arranged the Serendipity meeting.** Wiki: "Nastas has arranged for Dutch to be present on the wreck".
   Fiche L24/L28: the agents act on his tip about Dutch's location. The transcript only has Fordham's "the informant
   had better not have lied"; the fiche's wording is the safer one. Keep.
6. **Undead Nightmare bag.** EN wiki: MacDougal "left his bag with Nastas"; FR wiki: bag left "in his office";
   mission page `_m/Curious_Tales_from_Blackwater.txt` l.24: "his medical bag which he'd left down the alley", and its
   trivia l.91: "says that he left his stuff with Nastas". Fiche L39 attributes the "with Nastas" line to "the wiki's
   Undead Nightmare page". Acceptable; better to attribute it to the mission page (l.91), which is the closer source.
   Part A, minor.
7. **Weapons.** EN wiki: three weapons; FR wiki: Cattleman only. Fiche L69 reports both, attributed. Fine.

## 3. Duplicates inside the fiche (per OWNERSHIP.md)

| # | Fact | Occurrences | Keep / action |
|---|---|---|---|
| D1 | Quote "Enjoy it while you still can. Soon you will have cut down all of these trees." | B L45 (In his own words, quoted) + C L89 (Quotes) | Rule: a line quoted in B is not repeated in C. Cut from C L89-90 and put the missing "For a wise man..." line there (§1 #1). |
| D2 | Quote "Kid got shot in the leg, beat up pretty good." | B L47 (Names, quoted) + C L104 (What others say) | Keep C (mission line); Names paraphrases ("John calls him a kid") without the quote. |
| D3 | "treacherous snake" | A L36 (paraphrase, OK) + B L47 (Names, quoted) + B L64 ("calls Nastas a traitor") + C L110 (quoted) | Keep C quote; Names says Enepay calls him a snake/traitor without quotation marks; L64 cut to "(see Biography)". |
| D4 | Navajo name meaning "curve-like foxtail grass" | B L47 (Names) + C L139 (Trivia) | Keep B Names. Cut the trivia item L139 (move "The games never name his tribe" into Names if wanted; already in A L23). |
| D5 | Bastard line if John shoots an animal | B L73 (In the game) + C L141 (Trivia) | Keep B; cut C L141. |
| D6 | Miner uses Quick Tom Candle's model | B L69 (Weapons) + C L142 (Trivia) | Keep C (not a skill); cut from B L69. |
| D7 | Loot 4-7 dollars; horse killed after death fails the mission; fast horses | B L71 + L73 + C L143 | Keep B; cut C L143 entirely. |
| D8 | Mission-failure conditions (assault/kill; letting Dutch's men kill him) | B L73 + C L75 (Missions intro) | Keep B; cut the sentence in C L75. |
| D9 | "For a wise man... stupid man" | A L34 (paraphrase) + B L43 + B L55 (both paraphrase, both "see Quotes") | Keep A (event) and one B mention (Relationships MacDougal, L55); Personality L43 keeps a bare "see Quotes" or drops it. Fix the dangling pointer by adding the quote to C (D1). |
| D10 | MacDougal admits Nastas carried John down | A L33 + B L55 + C L106 (quote) + intro L26 | Keep A + C; cut the sentence from B L55. |
| D11 | MacDougal "relieved, especially you, Nastas" + acculturation remark | A L35-36 + B L56 + C L108 (relief quote) | Keep A + C; B L56 reduced to "(see Biography)" plus the Ledger pointer. |
| D12 | Grizzly "showed no signs of aggression" | A L35 + B L67 (Skills) + C L95 (quote) | Keep A + C; B L67 cut the clause (or one short pointer). |
| D13 | Grew up on a reservation and attended school | A L23 + A L30 + B L45 (quoted) + B L67 | A tells it twice: keep L23 (Origins), cut the repetition in L30 to the action only. B L67 drop the clause (keep "speaks fluent English" + Ross/MacDougal point). |
| D14 | Dutch drew young men from the reservation; friends of his ride with Dutch | A L23 + A L30 + A L33 + B L62 + B L67 + C L87 (quote) | A: keep L30 (+ L33 for "friends"), shorten L23 to a pointer. B L62 retells in full: cut to one clause. B L67 "Because friends of his ride with Dutch" acceptable as one clause. |
| D15 | Ross calls him "this savage" / "the Indian"; asks whether he speaks English | A L29 (quoted) + B L47 (Names) + B L58 (Ross) + B L60 (Fordham) + B L67 | Names owns the epithets; A paraphrases without quotation marks (rule "A always paraphrases"); B L58 keeps the "cannot communicate with Natives" point only; L67 drop "Ross still asks whether he speaks it". |
| D16 | Ledger notice "Nastas (Surname Unknown), of Indian descent" | A L23 (quoted) + A L37 (full quote) + B L47 (Names, quoted) | Names owns the name; A L37 keeps the full notice (primary text of an event; acceptable as a document quote) and L23 drops its quote ("the notice of his death gives no surname"). |
| D17 | "our informant" | A L24 (quoted) + B L60 (quoted) + C L102 (Fordham quote) | Keep C; A and B paraphrase. |
| D18 | Miner cuts his arm before Nastas kills him | A L32 + B L69 | Keep A; B L69 says only "he kills the miner who attacks him (see Biography)" plus the Murders-Committed note. |
| D19 | Character card one-liner | B L42 (quoted) + D L125 (pointer) | Already compliant. |

## 4. Summary for the correctors

**Part A (Biography)**
- L23: drop the quote of the Ledger notice (keep it in L37) and shorten the "young men from the reservation / friends"
  sentence to a clause, since L30/L33 tell it (D14, D16).
- L24, L29: paraphrase "our informant", "this savage", "the Indian" without quotation marks (D15, D17).
- L30: don't repeat "grew up on a reservation and went to school" (told in L23) (D13).
- L39 (optional): attribute "left his stuff with Nastas" to the mission page of "Curious Tales from Blackwater".
- Keep "head" (not "face") and "my dear friend": both verified against primary text.

**Part B (Personality, Names, Appearance, Relationships, Skills)**
- L43: "see Quotes" pointer for the wise-man line only works once C adds it (D9).
- L47 Names: paraphrase "Kid got shot..." and "treacherous snake" without quotation marks (D2, D3).
- L55: cut the "In the professor's own account, it is Nastas... who carries John down" sentence (D10).
- L56: cut relief/acculturation retelling to a pointer (D11).
- L58, L60, L62, L64: cut retellings to one clause + "(see Biography)" (D14, D15, D17, D3).
- L67: drop the grizzly clause, the reservation-school clause and "Ross still asks whether he speaks it" (D12, D13, D15).
- L69: remove Quick Tom Candle (stays in Trivia) and the arm cut detail (stays in A) (D6, D18).
- Optional: Tobiano Pinto canter glitch in Horses (§1 #4).

**Part C (Missions, Quotes, Trivia, Other media)**
- Quotes: REPLACE "Enjoy it while you still can..." (L89, already quoted in B) with "For a wise man, you are a very
  stupid man, mister." (At Home with Dutch, to MacDougal, transcript l.170) (§1 #1, D1).
- Quotes: remove "Kid got shot in the leg..." from C OR from B Names (D2; recommended: keep in C, paraphrase in B).
- Optional: add the four remaining multiplayer taunts, attributed to the wiki (§1 #2).
- Missions L75: cut the failure-conditions sentence (D8).
- Trivia: cut L139 (Navajo name, in Names), L141 (bastard line), L143 (loot/horse, in B) (D4, D5, D7). Add the
  post-death face glitch, attributed to the Red Dead Wiki (§1 #3).

**Part D (base, Development, Reception)**
- No change required. Intro L25-26 and key facts are summaries, not duplicates under OWNERSHIP.md.
- Note for the fact-check log: `fc/ireddead_Ledger_No59_text.txt` is truncated; cite `work/reyes/fc/ireddead_newspapers.html`.
