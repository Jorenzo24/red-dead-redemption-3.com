# Coverage report: Sister Calderón (v3, medium tier)

Compared: Red Dead Wiki EN "Mother Superior Calderón" (en.txt), Red Dead Wiki FR "Mère Supérieure Calderón" (fr.txt),
our fiche text calderon_full_en.txt (Lnn = its line numbers). Binding lead decisions: FIX_RULES.md.

`python3 scripts/coverage.py sister-calderon "Mother Superior Calderón"`:
wiki EN 1,208 words (prose sections); our fiche EN 5,627 words (**465 %** of the wiki), FR 6,429 words.
Per section (EN): intro+facts 390, Biography 1,798, Personality 537, Relationships 791, Charity work and gameplay 308,
Missions 326, Quotes 578, Development 300, Reception 157, Other media 115, Trivia 313.

Every non-speculative fact of the EN wiki page is covered: background (husband, mother, crucifix), Saint Denis reading
lesson and crucifix chase, "Of Men and Angels" collection, Emerald Station scene and its conditions, RDR1 "I Know You"
(alms, rob/donate, random nun encounters, daily routine and second-floor meals at Las Hermanas), Undead Nightmare
(station fight, clearing the convent, fresh undead, holy water, Sepulcro, Ayauhtéotl, Reyes insult, Escalera),
appearance, mission list (incl. voice-only "Red Dead Redemption"), all 9 wiki quotes (quoted or paraphrased from the
transcripts), all 5 trivia items, voice (attributed), infobox weapon (attributed). Gaps below are all marginal.

## 1. Wiki facts missing from the fiche

| # | Wiki excerpt | Status | Recommendation |
|---|---|---|---|
| 1 | RDR1 Cut Content page: "Mother Superior had her own stranger mission called rcm18 in which the player would retrieve four missing relics and return them to her... the dialogue files for it can be accessed in the game files"; unused items "Sacred Relic" (for her cut mission) and "Scripture Book" ("possibly" linked) | WIKI-ONLY (Red Dead Wiki, citing a game-files video) | **Add** to D, Development > Cut content, attributed: one sentence on rcm18 (four relics, dialogue left in the files) + Sacred Relic item. Leave out the "possibly" Scripture Book (speculative). |
| 2 | RDR2 Cut Content page: "Despite Sister Calderón being the only nun to appear in the game, more were planned" (unused generic nun assets, deleted random-encounter animations "street_kids... nun") | WIKI-ONLY | Optional, D Cut content, one attributed sentence ("according to the Red Dead Wiki, she is the only nun in RDR2; unused nun assets suggest more were planned" without the "suggest": state "unused generic nun assets remain in the files"). |
| 3 | Character page (UN): after the holy water test, "Mother Superior informs him that spiritual infections are confusing things that no one can ever understand" | WIKI-ONLY, no transcript; the Italian localisation and ireddead.com give a different line (her faith may not be strong enough), already in A L45 | Do not add (unconfirmed wording; the confirmed equivalent is already there). |
| 4 | Background: "She immigrated to Mexico in June 1899" | SPECULATIVE (month derived from the mission's place in the story; "immigrated" is not what she says) | Do not add. Fiche keeps "on her way to Mexico... sent on a mission" (A L35). |
| 5 | Background: "sent on a mission, presumably by the church" | SPECULATIVE (the wiki's own "presumably") | Do not add. |
| 6 | Trivia: Swanson prayed with "a Catholic lady", "implied to be Sister Calderón" | First half covered (B L69, attributed); "implied to be her" = SPECULATIVE | Keep as is (fiche correctly says the game does not say who she is). |
| 7 | Intro: "tritagonist" of Undead Nightmare; Personality: "kind and bittersweet... one of the only characters in the Red Dead series to have such a special mindset" | Interpretation | Do not add. |
| 8 | Undead Nightmare page: John buried with a flask that "is the bottle of holy water Mother Superior Calderón gave him. It explains why John was able to keep his memories" | SPECULATIVE | Do not add. |
| 9 | FR wiki: she appears in RDR1 "Eva in Peril" and tells John Eva left with a man for Sepulcro | CONTRADICTED: EN mission page "Eva in Peril" (_m/Eva_in_Peril.txt L39) names the nun as Sister Ana (Ana Calomarde) | Do not add (already excluded, fc/undead_nightmare_sources.txt item 6). |
| 10 | FR wiki infobox: "Père non-nommé" (unnamed father) | CONTRADICTED by transcript ("My husband died a long time ago", gsw.txt L12652) | Do not add. |
| 11 | RDR2 Cut Content page: a cut higher-class sleeping car "is used during the missions where Captain Monroe, Reverend Swanson, or Mother Superior Calderón board the train" | WIKI-ONLY, about a train car, not her | Skip (no value for the fiche). |

## 2. Places where the fiche differs from the wiki (and internal errors found while checking)

**Fiche right, wiki wrong or incomplete (no change):**
- Crucifix: wiki says her mother gave it "when she was a novice"; the transcript has both statements, "when I was a girl"
  (gsw.txt L8712, during the theft) and "when I was a novice... shortly before she passed" (L8754). Fiche gives both
  (A L25), per FIX_RULES 5.
- Family: FR wiki "father", EN wiki "husband". Transcript (L12652): husband. Fiche right.
- RDR1 setup: wiki says she collects outside Las Hermanas "and so the Strange Man sends Marston to her". Transcript
  (_m/I_Know_You_dialogues.txt L93): the Strange Man hears "an old nun is traveling from the monastery, taking the money
  she raised to the bank... Either that or rob her yourself." Fiche follows the transcript. **Small internal mismatch:**
  A L40 says "from the convent", B L85 says "from the monastery": use the transcript's word (monastery) or a neutral
  phrasing in both, consistently.
- FR wiki makes the station scene depend on "Tous frères et sœurs" (Brothers and Sisters). The FAOC mission page
  (Trivia), the Honor page and the "Red Dead Redemption" mission page all say "Of Men and Angels" + high honor. Fiche right.
- FR wiki "Eva in Peril": see section 1 #9 (Sister Ana). Fiche right to omit.
- Undead Nightmare first meeting: character page says she is "outside Las Hermanas fighting off an Undead... repeater
  shot"; the mission page "Mother Superior Blues" says Las Hermanas train station, being choked, shoots it in the head.
  Fiche follows the mission page (A L44); the Winchester Repeater is attributed to the wiki (B L97). OK.
- Informant: character page names Ayauhtéotl ("a woman"); the in-game mission description (FR localisation) says a
  passing nun; ireddead.com a young nun of a holy order in Escalera. Fiche gives the game wording and attributes the
  Ayauhtéotl identification (A L46, B L87). OK.
- Wiki quote wording ("ridiculous!", "We've all live bad lives...") differs from the transcripts; fiche quotes follow
  the transcripts (_m/Of_Men_and_Angels_dialogues.txt, gsw.txt L12640-12662). OK.

**Fiche wrong against the transcript (fix):**
- **A L31 and B L81 (Father O'Leary):** the fiche says that, as Arthur leaves, she tells the priest "that Dorkins had been
  right about him". Transcript (gsw.txt L8750-8756): "Brother Dorkins was right about you... you are the most wonderful
  man" is said TO ARTHUR, before the hug. As he leaves, she tells the priest: "See, Father... Brother Dorkins found
  him... I told you... Brother Dorkins was fantastic." Fix both places (A: she tells Arthur Dorkins was right about him;
  to the priest, after he leaves, that Dorkins had found him / was fantastic; B L81: replace accordingly or cut, since A
  owns the scene).
- **A L34 (order of "Of Men and Angels"):** transcript order is: dignified exit -> "I shall pray for you" -> Arthur: "I'm
  not a religious man, Sister... I'm an outlaw" -> she laughs, "Well, what fun!", religion is just a word -> God is
  people, find them food, actions lead, heart follows -> "I'll still think of you in very nasty terms... as you wish"
  -> Arthur donates -> "You are wonderful" -> "Oh, I meant wonderful, but... so very frightening... as you wish" ->
  Sister Ethel's stew. The fiche has her laugh and say "she will pray for him anyway" AFTER the outlaw line (wrong: the
  prayer comes before), and places the "thinking badly of him" joke after "wonderful" (wrong: it comes before the
  donation; after "wonderful" the joke is "so very frightening, as you wish"). Also "she does not believe him" -> she
  asks whether he is sure. Rewrite L34 in transcript order.

**Cross-fiche inconsistency (report to lead; out of this fiche's scope per FIX_RULES 7):**
- scripts/fiches/parts/orville_B.py L121: "a sober Swanson later tells Arthur that he prayed with **a nun**". The only
  source (Red Dead Wiki Calderón page, trivia, with video ref) quotes "a Catholic lady"; B L69 here says "a Catholic
  woman". Align Orville (EN+FR) on "a Catholic lady" (attributed to the wiki), and keep L69 as is (or quote "a Catholic
  lady" exactly).
- Checked consistent: arthur_A.py L53 (Isaac mentioned to her), arthur_C.py L111 (station conditions, "I'm afraid",
  life clearly), arthur_B.py L97, orville_A.py L104, arthur_D.py L44 ("Mr. Morgan").

## 3. Duplicates inside the fiche (OWNERSHIP.md + FIX_RULES 6)

| # | Fact | Occurrences | Keep | Cut / reduce |
|---|---|---|---|---|
| 1 | Lawmen may shoot her and O'Leary, two shots, lootable, Burdock Root | B L92; C Trivia L162 | B L92 | Cut L162 (FIX_RULES 6) |
| 2 | PC replay: Swanson by default | B L93; C Trivia L163 | B L93 | Cut L163 (FIX_RULES 6) |
| 3 | Well over 300 dollars if robbed | B L95; C Trivia L164 | B L95 | Cut L164 (FIX_RULES 6) |
| 4 | Rains Fall and her: the only ones Arthur tells about his son | B L71 (Rains Fall); C Trivia L158 | B L71 | Cut L158 (FIX_RULES 6) |
| 5 | Drunk at Doyle's Tavern: "Spanish nun" | B Names L59; C Trivia L159 | B L59 | Cut it from L159 (FIX_RULES 2); L159 keeps only the Spanish words. |
| 6 | "Gracias, señor" | C Quotes L137; C Trivia L159 (quoted again); A L41 paraphrase | L137 quote | In L159 drop the quotation of "Gracias, señor" (say she thanks John in Spanish) or keep only "Por favor". |
| 7 | Undead Nightmare: she gives her name as Mother Superior Calderón (ireddead + Italian) | A L24; B Names L59; D L146 | B L59 (Names owns names) | A L24: one clause without the sources; D L146: cut the sentence. |
| 8 | Name "Calderón" given in "Of Men and Angels" | A L24, A L33, B L59, D L146 | B L59 + A L33 (narrative clause) | Cut from D L146; A L24 may keep a pointer. |
| 9 | "On my way to Mexico... sent on a mission" | A L35; D L146 | A L35 | D L146: cut. With #7 and #8 removed, the D subsection "From the 2010 game to the prequel" only restates A L24/L40 and the intro: reduce it to one sentence (the wiki merge of the two characters, attributed) or cut it. |
| 10 | Wiki treats 1899 nun and 1911 Mother Superior as one character | Intro L3; A L24; A L40; B L59 (page title); D L146 | Intro (D) + A L24 | A L40 keeps only the "twelve years earlier" detail; D L146 cut (see #9). |
| 11 | Sister Ethel cooks for the poor | A L26; B L83 (Sister Ethel); B L92 (Skills) | B L83 | Cut from A L26 and B L92. |
| 12 | Dorkins wants to be sent overseas as a missionary / frustrated with the order | A L26; A L33; B L79 | B L79 | A L26: cut; A L33 keeps "says Dorkins is frustrated with their order" or points to B. |
| 13 | Dorkins "very jealous" | A L35; B L79 | A L35 | B L79: cut the sentence (or "see Biography"). |
| 14 | Old church on Gaspar Street | A L29; B L92 | A L29 | B L92: cut the location. |
| 15 | Reading lesson; she corrects the boy and Dorkins | A L29; B L48 (Personality); B L79 (Dorkins) | A L29 | B L48 and B L79: one clause each at most, no retelling. |
| 16 | Dorkins told her of Arthur's good turn; Arthur: Dorkins talks nonsense / greatly deceived; "most wonderful man" | A L29, A L31; B L64 | A | B L64: replace the retelling with "see Biography". |
| 17 | "Don't hurt him" / asks after the boy | A L30-31; B L48; B L52 (quote) | A + B L52 quote | B L48: cut. |
| 18 | Arthur says he is an outlaw, she laughs | A L34; B L49; B L54 (quote "Well, what fun!") | A + B L54 | B L49: cut. |
| 19 | She "once did terrible things" | A L25 (Origins); A L34 pointer; B L49; C L113-115 quotes | A L25 paraphrase + C quotes | B L49: cut (already a pointer in A L34). |
| 20 | "Often neither do I" | A L37; B L49; C L132 quote | A L37 + C L132 | B L49: cut. |
| 21 | Not in Rockstar's 6 Sep 2018 descriptions | B L48; C L155 | B L48 (official descriptions = B) | C L155: cut the sentence. |
| 22 | Son, girl, mother, father told at the station; husband died long ago | A L36; B L65 (Arthur); B L73 (Mary Linton); B L89; C L128-129 quote + context | A L36 + C L128 | B L65: cut the retelling (keep "see Biography"); B L89: keep the two-sentence "Her mother and her husband" entry only as a pointer. B L73 is distinct (Mary-page attribution), keep. |
| 23 | Line recalled on the last ride | A L37; B L65; C L105 (table); C L131 (quote context) | A L37 + table line | B L65: cut. |
| 24 | Arthur / John call her "Sister" | B L59 (Names); B L65 (Arthur); B L67 (John); A L45 (John calls her sister, she corrects him) | B L59 | Cut from L65 and L67; A L45 keeps the correction only as a clause or points to Names. |
| 25 | Strange Man's pitch (old nun, money to the bank, help or rob) | A L40; B L85 (Strange Man) | A L40 | B L85: one clause + "see Biography". |
| 26 | Random nun encounters after donating / honor loss | A L41; B L95 | B L95 (gameplay) | A L41: cut the random-encounter sentence. |
| 27 | Reyes insult (vain, ambitious parasite, womanizer) | A L46; B L75 | B L75 (relationship) | A L46: cut the insult; keep the Bill Williamson exchange there (or move it to B L75 too). |
| 28 | Ayauhtéotl as a nun, identified as the informant | A L46; B L87 | B L87 | A L46: keep "the mission description calls the informant a nun passing through" + "see Ayauhtéotl". |
| 29 | Mortal sin after shooting the undead | A L44; B L49 | A L44 | B L49: cut. |
| 30 | Holy water test and unlock | A L45; B L97; C L107 (table) | A L45 + table | B L97: keep only the weapon (Winchester, attributed); drop the holy water retelling. |
| 31 | Station conditions ("Of Men and Angels" + high honor; else Swanson) | Intro L2; Key facts L8; A L35; B L69; B L93; C L104 | A L35 + table + B L69 (Swanson relation) | B L93: cut the first sentence, keep the PC-replay sentence. |
| 32 | De Santa rises at Sepulcro | A L45; B L77 | A L45 | B L77: fine as is ("see Biography"); no change needed. |

## 4. Summary for the correctors (ordered by part)

**A (Biography)**
1. L31: "Brother Dorkins was right about you... most wonderful man" is said to Arthur before the hug; to the priest, as
   he leaves, she says Dorkins had found him and was fantastic (gsw.txt L8750-8756).
2. L34: rewrite in transcript order: prayer before the outlaw line; "nasty terms" joke before the donation; after
   "wonderful", the "so very frightening, as you wish" joke; "she asks if he is sure" instead of "does not believe him".
3. L40: "from the monastery" (Strange Man's word) instead of "from the convent", consistent with B L85.
4. Dedup: L26 cut Sister Ethel and Dorkins-overseas sentences; L24 shorten the Undead Nightmare naming to a clause;
   L41 cut the random-encounter sentence; L45 point to Names for the sister/Mother Superior correction;
   L46 cut the Reyes insult (B L75 owns it) and the Ayauhtéotl identification (B L87 owns it).

**B (Personality, Names, Appearance, Relationships, Charity work and gameplay)**
5. L81 (Father O'Leary): fix the "Dorkins was right" line as in A #1 (or reduce to a pointer).
6. L85 (Strange Man): reduce to one clause + "see Biography".
7. Dedup: L48-49 Personality: remove retold events (reading lesson, crucifix, outlaw laugh, terrible things, "neither do I",
   mortal sin) and keep traits + pointers; L64-L65 Arthur: cut the retelling (wonderful/deceived, station confessions,
   last ride, "calls her Sister"); L67 John: cut "he calls her sister"; L79 Dorkins: cut "very jealous"; L92 cut Gaspar
   Street and Sister Ethel; L93 cut the conditions sentence; L97 cut the holy water retelling.
8. Optional (lead): L69 quote the wiki's exact "a Catholic lady".

**C (Missions, Quotes, Other media, Trivia)**
9. Trivia: cut L158 (Rains Fall), L162 (lawmen), L163 (PC replay), L164 (300 dollars); L159 cut the drunk's "Spanish nun"
   and the repeated "Gracias, señor" quotation.
10. L155: cut the "not among Rockstar's 2018 descriptions" sentence (B L48 owns it).

**D (base, Development, Reception)**
11. Cut content (L148): add, attributed to the Red Dead Wiki, the RDR1 cut stranger mission rcm18 (retrieve four missing
    relics for the Mother Superior; its dialogue remains in the game files) and the unused Sacred Relic item. Optional:
    the RDR2 cut-content note that unused generic nun assets remain in the files (she is the only nun in RDR2).
12. L146 "From the 2010 game to the prequel": cut the name/Mexico/merge sentences that repeat A and B Names; keep at most
    one sentence or remove the subsection.

**Out of scope, report to lead:** orville_B.py L121 "prayed with a nun" should match the source's "a Catholic lady" (EN+FR).
