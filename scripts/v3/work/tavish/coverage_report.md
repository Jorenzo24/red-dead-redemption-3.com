# Coverage report: Tavish Gray v3 (EN)

Compared: Red Dead Wiki EN (`en.txt`, 438 words per coverage.py) and FR (`fr.txt`, 258 words) with `tavish_full_en.txt`
(Lnn = line numbers there). Also read: mission pages in `_m/` (Horse_Flesh_for_Dinner, Gray_s_Secret,
Gray_Family_History_Letter, Gray_Family, Caliga_Hall, Jock_Gray, Leigh_Gray, Beau_Gray, RDR2 Cut Content),
the full transcript `fc/gsw.txt` (gsw l.N = its line numbers), the images in `fc/` and `gal/out/`, Camp_Events,
HOUSE_FACTS and the authoritative parts (catherine, arthur, hosea, micah, javier, john, simon, sean).

coverage.py: our EN 4,263 words = **973 % of the wiki** (Biography 1,699; Personality 364; Relationships 663;
Caliga Hall 176; Missions 238; Quotes 344; Development 189; Other media 49; Trivia 134). FR 4,878 words.

The wiki page is short and the fiche covers almost all of it: background (patriarch, eldest, rival of the
Braithwaites, brother of Leigh, father of Beau, Murdo, Ross), the horse job (5,000 promised, 700 paid), the field
burning, the ambush without Tavish, the body at Gray's Secret, the Moffat letter, the mission list, both trivia
items (Leigh brother/son mismatch with Tavish not correcting Arthur; Moffat surname). The gaps are small.

## 1. Wiki facts missing from the fiche

| # | Wiki excerpt | Status | Recommendation |
|---|---|---|---|
| 1 | Lead quote: "We haven't recovered as much as I'd hoped from the war. My family try... my sons are good boys, but it's been hard. Like I said, some people in the area will hold us back forever. We need stability." | CONFIRMED, gsw l.7438 (speaker labelled "Stranger", same stable scene, before he is named). The fiche only paraphrases it (L26, L31, L43). | B, "In his own words": add it verbatim (transcript spelling "for ever"). A keeps its paraphrase at L31 only (see §3, item 4). |
| 2 | Infobox: Jock Gray = "relative" of Tavish | WIKI-ONLY for the relationship. Name "Jock" is CONFIRMED as a speaker label (gsw l.7911); the wiki's Jock page says the name comes from the game files. | A L35: one clause, "Jock Gray, a relative of Tavish according to the Red Dead Wiki". Optional: D facts grid, Family. |
| 3 | Infobox: Douglas Gray = "ancestor" | WIKI-ONLY (Leigh Gray page also says ancestor; the Gray family page only says "member"). | A L27: add to the 1806 sentence "whom the wiki lists among Tavish's ancestors" (attributed). |
| 4 | Gallery: "Tavish Gray's corpse" (Gray's secet.jpeg) | Image exists, verified: `fc/img_Grays_secet.jpeg.jpg`, also `fc/img_RDR2_POI_18_Grays_Secret_01/05` and the letter `fc/img_RDR2Gray_Family_history_letter.png`. Our gallery has 1 image. | Gallery (assembly/D): add the corpse image and the letter image. Captions neutral (where, what is visible); no cause of death. |
| 5 | Mission page (Horse Flesh, trivia): if "The Fine Joys of Tobacco" was played first, on the ride out Arthur tells John and Javier, who did not know, that he and Sean burned the Grays' fields, and that the job made Sean happy "like a pig in shit". | WIKI-ONLY (the transcript only covers the horses-first order). | A L33: one sentence added to the order-variant paragraph, attributed to the wiki, no quotation marks. |
| 6 | Mission page (trivia): the stolen horses carry the Braithwaite insignia on their hindquarters ("probably how Clay knew") | Insignia = WIKI-ONLY game content; "probably how Clay knew" = SPECULATIVE, drop. | Optional, A L32 one clause or C Trivia, attributed. |
| 7 | Mission page (trivia): Arthur removes the sheriff's badge given by Sheriff Gray during the mission ("seemingly to not tip off the Braithwaites") | Removal = WIKI-ONLY; the motive = SPECULATIVE, drop. | Optional, C Trivia, attributed; low value for Tavish. |
| 8 | Cut content page: Tavish speaks of thoroughbreds, but no Thoroughbred appears in the mission (the mission page calls the loose stallion a Black Arabian). | "thoroughbreds" CONFIRMED gsw l.7465 (already in L32). Breed mismatch = WIKI-ONLY; "neither knew the breed" = SPECULATIVE, drop. Arthur's "Arab chargers" line is not in the transcript: do not quote it. | Optional, C Trivia: "Tavish calls the horses thoroughbreds; according to the Red Dead Wiki, the stolen stallions are Arabians." |
| 9 | Mission page: the stablehand gives the horses' names and history | CONFIRMED gsw (Cerberus, Old Faithful, Old Father Time). | Optional, A L32: one clause naming the three stallions. |
| 10 | Wiki EN "back porch"; Caliga Hall page "the porch to the east of the main hall"; FR "porche arrière" | WIKI-ONLY (the two wiki pages agree on the back/east side). | Optional, A L37: "on the back porch of the main house, according to the Red Dead Wiki". |
| 11 | Gray family page: the Grays settled in Scarlett Meadows while it was still French territory, and grew tobacco and cotton with slave labor | First half WIKI-ONLY; the slave labor part is already in L26 (attributed). The page's "to cover up the true reasons for their flight from Scotland" = interpretation, drop. | Optional, A L26: one attributed clause on the French period. |
| - | "minor character" (EN), "personnage support" (FR), category Antagonists | Classification only. | Do not add. |
| - | Death "possibly due to suicide, but more likely from a heart attack judging by the state of his corpse"; "next to the cause of the presumed heart attack" | SPECULATIVE (see §2, D1). | Do not add, even attributed. |
| - | Trivia: "plausible that the gang received false information about the family" | SPECULATIVE. | Do not add (the fiche correctly keeps only the facts of the mismatch). |

Confirmed game facts found while checking, not on the wiki page and missing from the fiche:

| # | Fact | Source | Recommendation |
|---|---|---|---|
| T1 | Before John's pitch, Tavish challenges the newcomers: "You don't know me... you turn up in this town... and you're helping everybody. And everywhere... there's troubles. Who are you?"; after John's railway story he answers "Sure... and bad men." | gsw l.7436-7438 | A L31: paraphrase in one sentence (he is suspicious of the newcomers before the deal). C Quotes may take the line (it is not quoted anywhere else). |
| T2 | Trelawny, in "The New South": the town is trapped in the feud; the two old plantation families fall out "over rebel gold and... marrying cousins and not marrying" | gsw l.5860-5862; told the same way in catherine_A.py ("Confederate gold and marriages") | A L27: one sentence, before Archibald's version (consistency with Catherine). |
| T3 | Horses-first order: in "The Fine Joys of Tobacco", Arthur tells Sean "We just robbed their horses too", Sean answers "That was you? Jesus." | gsw l.7597-7598 | A L34: one clause, paraphrased (pairs with the order note at L33). |
| T4 | 1907, "A Quick Favor for an Old Friend": Sadie says the sheriff has done a lot to bring Rhodes into line "since the time of the Grays and Braithwaites" | gsw l.15452 | A L41: add it; it confirms in-game the change in Rhodes (Harmon Thomas's name and election stay attributed to the wiki). |
| T5 | Archibald MacGregor is among the men who come out of the sheriff's office with Leigh and Jock ("You wanna join your little friend there, do ya?") | gsw l.7915 | Optional, A L35: name him among the deputies. |
| - | Beau: "we bury our secrets and we bury them deep" (Course of True Love III, gsw l.6375) | CONFIRMED | Do not add: it would invite an interpretive link to Gray's Secret. |

## 2. Places where the fiche differs from the wiki

- **D1. Cause of death.** Wiki EN: "possibly suicide, more likely a heart attack". Gray's Secret page, Caliga Hall page and
  FR wiki: suicide. Gray family page: heart attack "implied". The game never states it. The images (`fc/img_Grays_secet`,
  `POI_18_01`) show him seated in a wicker chair, right hand on left forearm, coffee pot and cup on the table, no weapon
  and no visible wound; the letter (Gray_Family_History_Letter, text verified) says nothing about death. **The fiche is
  right** (L2, L13, L37). Keep "the cause is not shown" and keep the wiki's guesses out.
- **D2. When he dies.** Wiki Tavish page: "sometime after the battle" (the Rhodes ambush). Gray's Secret page: accessible after
  "Horse Flesh for Dinner". Caliga Hall page: "after the conclusion of the third chapter". No transcript decides. The fiche
  (L37) reports the first two, attributed. Acceptable as is; do not pick one.
- **D3. Ross Gray.** Wiki: "a spy ... forced to flee from Scotland after actual Jacobites began hunting down loyalists".
  The letter decides: "unquestionably a well-paid informer", paid in cattle and cash, given land confiscated from his
  neighbour, did not leave Scotland until 1755, "the year when a few Jacobite supporters began reprisals against known
  informers in the Highlands". **The fiche follows the letter (L38-39), correct.** But L8 (key facts) and L62 (Ross Gray
  entry) say "not an exiled Jacobite": the letter never uses these words (it speaks of his "ostracizing and emigration
  ... in the aftermath of the uprising of 1745" and of Mr. Gray as a self-described "Scot in exile"). Reword L8 and L62
  in the letter's terms (paid informer of the Duke of Cumberland, left Scotland in 1755).
- **D4. Ambush casualties.** Wiki EN: "most members of the Gray family are killed". FR: "tous les Gray ont été tués sauf Tavish".
  Transcript (gsw l.7852-7937): gunmen, Sheriff Leigh Gray, Jock, Archibald and deputies; Beau survives (The Course of True
  Love V). HOUSE_FACTS: never "the Grays are wiped out". **The fiche is right** (L35).
- **D5. Who plans the ambush.** FR: Tavish and Leigh want revenge and set the ambush together. Transcript: Micah says "a
  couple of the Grays" spoke to Bill; Leigh leads the fight; Tavish is never shown or named. **The fiche is right** (L35).
- **D6. Where the letter is.** Gray family page: the corpse "can be looted for a letter". Letter page: on a table on the porch.
  No transcript. The fiche follows the letter page (L38); keep.
- **D7. Appearance (L53, part B).** "long gray hair on the sides" does not match the images (`gal/out/gallery-1.jpeg`,
  `fc/img_Grays_secet`): bald crown, dark hair streaked with gray on the sides and back, heavy dark eyebrows, graying beard
  and sideburns; dark coat, white shirt, dark tie, plaid vest. Fix L53.
- **D8. Gallery caption (D/assembly).** The alt text of gallery-1 says "on a porch"; the image shows him at a wooden stall
  with tobacco fields behind (the stables scene). Use a neutral alt ("Close-up of Tavish Gray at Caliga Hall").
- **D9. Who receives the letter.** L2, L38 and L83 carefully say "a Mr. Gray"; L135 (Trivia) says "The historian who writes to
  Tavish". Harmonize L135 ("who writes to Mr. Gray").
- **D10. Pearson 1907 line (L41).** Stated as a game fact; the Simon fiche (simon_C.py) sources the same line to the wiki's
  quote list. Attribute it the same way here ("according to the Red Dead Wiki"), or quote it only in one fiche.
- Checked and correct against the transcript: railway speculation, Yankee/Scottish exchange, gold, 5,000 and "fifty cents on
  the dollar", "keep us away from this... publicly", south side stables, "Crazy old fool", "a third of that", Hosea and Sean
  warning (horses-first order), investment lie at the gate, 650 then 700, Arthur's journal; Hamish and "Mr. Gray's got a heap
  of problems" (gsw l.7624-7631); "Old Man Gray's doubled security after that business at the saloon"; Bill's "deals with
  them Gray boys" (gsw l.7106, L78); Leigh's "we know what you been doing" and "This is the Grays' town"; Dutch "Scots...
  degenerates... drunkards... Rich as Croesus" and "put in a word with his father" (Advertising, The New American Art,
  gsw l.6531-6544); Archibald on generations, businesses and the Parlor House (gsw l.5833-5840); Dutch's "make the Grays
  bleed" (Camp_Events l.326, chapter 4).

## 3. Duplicates inside the fiche (per OWNERSHIP.md)

1. **Leigh: brother or son.** L25 (A), L51 last sentence (B Names), L58 (B Leigh), plus L9/L18 (D summary, fine). Keep the
   discussion in **L58** (relationship fact). A L25: reduce to one clause pointing to Relationships. L51: cut the last
   sentence (it is not a name).
2. **Beau's self-introduction** (son of Tavish, nephew of Leigh, grandson of Murdo): A L24, B L56, B L60, C L118 (quote).
   Keep **C L118** (quote) and **A L24** (paraphrase). L56: keep "His son." and the Penelope sentence only. L60 may keep
   "grandson of old Murdo Gray" as the source for Murdo.
3. **Dutch, "put in a word with his father"**: C L116 (quote), A L25, B L58, B L72. Keep **C L116** and the one clause in
   **B L72**. Cut it from A L25 and B L58 (pointer only).
4. **Tavish on war, work and Scotland**: B L46-48 (quotes), A L26 (father taught him, war, stability), A L31 (complaints, Yankee,
   "Scottish too"), B L43 (Personality retells it). Keep **B L46-48** for the words and **A L31** for the scene. Cut from
   A L26 the sentences "He says his father taught him..." and "He also says the family has not recovered..." (keep "Tavish
   describes the Grays as an old Scottish family" only if wanted). B L43: keep the traits in a short form without retelling.
5. **Insults and the dead uncle**: A L24 ("Tavish also says that the Braithwaites killed his uncle"), A L31, B L43, B L64.
   Keep **A L31**; cut the L24 sentence; B L43 and L64 one clause each. **Broken pointer:** L43 and L64 say "(see Quotes)" but
   Quotes has no hag/inbred line. Add "That hag and her inbred sons... they've ruined this county. They killed my uncle, you
   know." (gsw l.7446) to **C Quotes**, or drop the pointers.
6. **5,000 / 700**: L2, L6 (D), A L32 (owner), B L43, B L66, B L82, C L92, C L105, C L112. Cut the B L43 sentence ("He values
   the stolen horses..."). L66 and L82: one clause at most.
7. **"Crazy old fool"**: A L32 (paraphrase), B L51 (Names, quoted), B L66. Keep **B L51**; cut the L66 sentence.
8. **Arthur's "prize idiots" journal**: C L113 (quote), A L32 (paraphrase + pointer), B L68 (last sentence). Cut **L68**.
9. **Archibald on Caliga Hall** (generations, all the businesses, the saloon): L5 (D), A L26, Caliga Hall L86. Keep **A L26**;
   in L86 replace the repeated sentence with the tobacco-field pointing and the layout of the estate.
10. **Security doubled after the saloon**: A L34, B L51, Caliga Hall L87. Keep **A L34**; L51 keeps only the name
    "Old Man Gray"; cut the sentence from L87 (keep the payroll/supply wagons only if not in A, else cut too).
11. **Caliga Hall in 1907** (family still owns it, workers, guards): A L41 and Caliga Hall L87. Keep **L87** (place);
    cut that sentence from A L41 (A keeps the body, Rhodes and the 1907 lines).
12. **"Tavish is not present"** at the ambush: A L35 says it twice ("takes no visible part" and "Tavish does not appear in the
    mission"). Cut the second. B L58 and L76 keep a short clause; C L100 fine (table).
13. **"Just keep us away from this... publicly"**: B L49 (quote), A L32 (paraphrase), B L43 (paraphrase). Cut it from L43.
14. Gray's Secret requiring the mission: A L37 (POI page) and C L134 ("the only point of interest..."). Borderline: the Trivia
    adds the "only one" fact; keep both, or cut the L37 clause and leave the timing discussion to the two-version sentence.

## 4. Summary for the correctors

**Part A (Biography)**
- L24: cut "Tavish also says that the Braithwaites killed his uncle" (told at L31).
- L25: reduce the son/brother discussion and Dutch's line to one pointer clause (owner: B Leigh; quote: C).
- L26: cut the father/war/stability sentences (told at L31 and B); optional: wiki-attributed clause on the French period.
- L27: add Trelawny's "rebel gold and marrying cousins" (gsw l.5862, as in catherine_A); add "whom the Red Dead Wiki lists
  among Tavish's ancestors" for Douglas Gray.
- L31: add Tavish's suspicion of the newcomers ("Who are you?", "and bad men"), paraphrased.
- L32: optional clauses: the stallions' names (Cerberus, Old Faithful, Old Father Time); Braithwaite insignia (wiki).
- L33: add the wiki-only reveal on the ride out when the fields were burned first (Arthur tells John and Javier he and Sean did it).
- L34: add, paraphrased, Arthur telling Sean they just stole the Grays' horses (horses-first order).
- L35: "Jock Gray, a relative according to the Red Dead Wiki"; optional: Archibald among the men; cut "Tavish does not appear in the mission."
- L37: optional "back porch" (wiki).
- L41: add Sadie's 1907 line (A Quick Favor for an Old Friend); attribute Pearson's line to the wiki as in simon_C; move the
  1907 estate sentence to Caliga Hall only.

**Part B (Personality, Names, Appearance, Relationships, Caliga Hall)**
- In his own words: add the wiki's lead quote "We haven't recovered as much as I'd hoped from the war..." (gsw l.7438).
- L43: trim to traits; cut the 5,000/700 sentence, the "keep us away" paraphrase and the retold insults.
- L51: cut the last sentence; keep only the name "Old Man Gray" from Sean's line.
- L53: fix the hair ("dark hair streaked with gray on the sides", not "long gray hair").
- L56: cut the genealogy recitation; L58: keep the brother/son discussion here, drop Dutch's line (pointer to Quotes);
  L62: reword "not an exiled Jacobite" to the letter's terms; L66: cut "crazy old fool"; L68: cut the "prize idiots" sentence.
- L86-87 (Caliga Hall): drop the Archibald and "security doubled" repeats; keep the 1907 estate sentence here.

**Part C (Missions, Quotes, Trivia, Other media)**
- Quotes: add "That hag and her inbred sons... they've ruined this county. They killed my uncle, you know." (gsw l.7446),
  which fixes the broken "(see Quotes)" pointers at L43/L64; optionally "You don't know me... Who are you?" (gsw l.7436).
- L135: "who writes to Mr. Gray" instead of "to Tavish".
- Optional Trivia (attributed): horses called thoroughbreds but Arabians per the wiki; Arthur removes the sheriff's badge.

**Part D (base, Development) and gallery**
- L8: reword "not an exiled Jacobite" to the letter's terms (paid informer, left Scotland in 1755).
- Gallery: add the corpse image and the letter image (verified files in `fc/`); neutral alt for gallery-1 (not "on a porch").
- Optional: facts grid Family, "Jock Gray (a relative, according to the Red Dead Wiki)".

Never add: suicide or heart attack (even attributed), "the Grays were wiped out", Tavish planning the ambush, the wiki's
"false information" theory, "probably how Clay knew".
