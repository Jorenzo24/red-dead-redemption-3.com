# Coverage report: Harold MacDougal (v3, medium tier)

Length: our EN 5,933 words (coverage.py) vs wiki EN 1,983 words: **299 %** of the wiki (FR 7,101 words).
Sections (EN): intro/facts 441, Biography 2,081, Personality 473, Relationships 690, Research/weapons/horses 492,
Missions 338, Quotes 790, Development 168, Reception 87, Other media 136, Trivia 213, Gallery 24.

Overall: the fiche covers every non-speculative fact of the EN and FR wiki pages. Only one wiki fact is worth adding
(the GOTY guide's "writing a book" line); the rest are optional attributed additions or excluded speculation.

## 1. Wiki facts missing from the fiche

| # | Wiki excerpt | Status | Recommendation |
|---|---|---|---|
| 1 | GOTY guide: "on a sabbatical from Yale, writing a book about Native Americans and the last days of the old west" (EN wiki Background quote; FR wiki "Il a entrepris d'écrire un livre sur les Amérindiens et sur la fin de l'Ouest américain") | WIKI-ONLY (guide quoted by wiki EN + FR); consistent with his own transcript line about documenting "the last days of the Old West" (Prodigal Son dialogues l.90) | **Add** to B Personality L52, inside the existing GOTY-guide sentence, attributed ("according to the guide, as quoted by the Red Dead Wiki"). Owner B (official descriptions). |
| 2 | "Harold MacDougal was born circa 1869" (ref: GOTY guide) | WIKI-ONLY (derived from "42-year-old" in 1911) | Optional: D facts grid L13 could add "c. 1869 by the wiki's reckoning". Keep the "Not given in the game" wording. |
| 3 | "In May of that year, MacDougal moves to the town of Blackwater" (wiki deduces May from the 1914 article's "six months" + November 1911) | WIKI-ONLY deduction | Optional: A Act III L34, one clause attributed ("the Red Dead Wiki places his arrival around May 1911, six months before his missions"). Not required. |
| 4 | "he and a book he wrote are mentioned in 'Help a Brother Out' by the fence shopkeeper" | WIKI-ONLY, unconfirmed: the mission page (_m/Help_a_Brother_Out.txt) never mentions MacDougal or the book; no transcript cached | Do NOT add the shopkeeper mention. The prop (trivia L165, table L107) is enough. |
| 5 | Header quote: "The savage heart cannot be conventionally civilized! I was right all along!" | WIKI-ONLY: absent from all four transcripts (closest: "The Savage Mind Cannot Be Civilized", FPSP dialogues l.143) | Optional: C Quotes, RDR1 block, flagged "according to the Red Dead Wiki" like the UN lines. Low priority. |
| 6 | At the station "He shakes his hand but gives up and gives him a hug" | WIKI-ONLY (transcript only has "(hugging)", Prodigal dialogues l.103) | Skip, or a clause in A L42 attributed to the wiki. Low priority. |
| 7 | On the ride back he mourns Nastas as "a brilliant savage companion" | WIKI-ONLY, not in transcript (actual line: "This is very disheartening. My recent studies, Nastas, the blood samples...", already paraphrased L40) | Do not add (unverified quotation). |
| 8 | Trivia: Mantegazza/Boas/Tylor/Malinowski influence; Deloria's *Custer Died for Your Sins*; "mad scientist"; Damnation/Protestant/hypocrisy; irony of his undead death; "foreshadowing" | SPECULATIVE / interpretation | Exclude. (The "limb from limb" exchange is already quoted L119 without the foreshadowing reading: correct.) |
| 9 | Personality section ("naive and small-minded", "incompetent in practical matters") and FR wiki "toujours très optimiste" | Interpretation (only the GOTY "optimist" wording is sourced, already in L52) | Exclude. |

Not a wiki fact but worth noting for C: the station line "My research is complete; much as I thought, there's no civilizing
this savage land." (Prodigal dialogues l.99, CONFIRMED) is only paraphrased in A L42; it could replace a weaker C quote.

## 2. Places where the fiche differs from the wiki

1. **Grizzly bear** (FPSP). Wiki character page: MacDougal shoots, the bear attacks, John kills it. Mission page: "The professor begins shooting at the bear and it turns hostile, forcing the player to kill it." Transcript (FPSP dialogues l.59): "(Marston and MacDougal open fire at the bear, killing it)". The fiche is internally inconsistent: L39 follows the mission page ("he opens fire himself... John has to kill it"), L91 says "he and John open fire". Fix A L39 to the transcript: he shouts "Shoot it!", he and John open fire and kill it; keep the mission-page "turns hostile" only as gameplay if wanted.
2. **Obituary date.** Wiki trivia: obituary published "in the Blackwater Ledger in 1914". Wrong: it is in Ledger No. 59 (1911), available after "The Prodigal Son Returns (To Yale)" (fc/ireddead_Ledger_No59_text.txt). Fiche L43 is right.
3. **Obituary wording.** Wiki: "May you find God, dear friend". Ledger No. 59: "May you find God, my dear friend. Prof. Harold MacDougal Esq." Fiche right.
4. **"I don't want a bullet in my flippin' neck!"** (wiki quote). Transcript: "Not having a bullet in your flipping neck, sir." Fiche L134 right.
5. **1899 paper venue.** Wiki: presented "to his colleagues at Yale". Article: "to colleagues at a symposium last week", no place (fc/Prominent_Yale_Scientist_Speaks_Out.txt). Fiche L31 right.
6. **Fortisque vs Fortescue.** Wiki merges them (cites the 1899 article for arguments with "Lionel Fortisque"). Article names Benjamin Fortescue; Fortisque comes from the FPSP transcript and Ledger 213. Fiche L79/L168 right.
7. **1914 timing.** Wiki: "around November of 1914". Ledger 213 gives no month (fc/ireddead_Ledger_No213_text.txt). Fiche L47 right.
8. **Childhood/father/inheritance lines** the wiki cites from FPSP are absent from the transcript; fiche L27 reports them as wiki claims with that caveat. Correct handling.
9. **UN reappearance.** Character page: kill or hogtie in town; mission page: must be killed in town, may be left to roam outside the cemetery. Fiche L50/L95 reports both sources. Correct.
10. **FR wiki errors**: says he hit "un étudiant" (Ledger 213: colleague Lionel Fortisque); anecdote says MacDougal claims the bison are going extinct (it is Nastas; MacDougal calls extinction "a myth", At Home with Dutch). Fiche right on both.
11. Cross-fiche note: john_D.py L150 says MacDougal "helps him locate Dutch's hideout"; in the transcript it is Nastas who knows the way (At Home with Dutch l.37-43). Tolerable as summary, but "With Nastas, MacDougal helps..." could become "Nastas, MacDougal's informant, leads him..." if John is regenerated.

## 3. Duplicates inside the fiche

| # | Fact | Occurrences | Keep |
|---|---|---|---|
| 1 | Offers John cocaine | A L27, B Personality L53, B John L63 | B L53 (habit). Cut from A L27 ("and offers to share with John") and L63 ("and offers him cocaine, which John declines" -> keep only if needed for John's refusal, then cut from L53). One place only. |
| 2 | "Norse stock / white man with a savage spirit" | A L36, B John L63 | A L36. B L63: cut. |
| 3 | Ross told him about John's past with Dutch | A L37, B John L63 | A L37. Cut from L63. |
| 4 | Thanks John for his life; hug at Manzanita Post | A L40/L42, B John L64, C L132/L141 | A + C quotes. Cut L64's last sentence (already says "see Biography"). |
| 5 | Nastas: "for a wise man... very stupid man" | A L38, B Nastas L66, C L115 | C quote + A paraphrase. Cut from B L66. |
| 6 | Buffalo argument | A L37, B Nastas L66, C L126 | A + C. B L66: one clause at most ("they argue on the rides, see Biography"). |
| 7 | Ross cannot communicate with Natives; "good friend of the government" | A L35, B Ross L69 | A L35. B L69 keeps only "which should tell you something". |
| 8 | Fordham asks him to find out what Nastas knows | Key facts L5, A L35, B Fordham L71 | A L35 (+ key facts). Cut from B L71. |
| 9 | Thrown out of Yale for degeneracy | A L27, B Fordham L71, C L111 quote | C quote + B L71. A L27: shorten to a pointer or drop the Fordham sentence. |
| 10 | Dutch fascinates him (white man among Natives) | A L37, B Dutch L73, C L124 quote | A + C. B L73 keeps only the new names ("reverse integration", "regressive acculturation") and the Ledger line. |
| 11 | Ledger No. 59 names Dutch as suspected leader | A L43, B Dutch L73 | A L43. Cut from L73. |
| 12 | Fortisque minor scandal; croquet mallet | A L26/L46, B Fortisque L77 | A. B L77: one line ("colleague; see Biography"). |
| 13 | Fortescue/Fortisque spelling | B L79, C Trivia L168 | B L79. **Cut Trivia L168.** |
| 14 | "Explores with the mind / rarely leaves his room" | A L37, B quote L55, B Research L86 | B L55 quote + A. Cut the clause in L86. |
| 15 | Never sleep again; begs John not to leave him | A L40, B Personality L53 | A L40. Cut both from L53 (Personality then keeps tics: fast talk, stammer, cocaine). |
| 16 | Nashoba holds him hostage on the roof | A L41, B L75, B "In the game" L95 | A L41 + B L75. Cut from L95. |
| 17 | Mission failure conditions | B L95, C table L102/L103 | B L95 (gameplay). Cut the "fails if" sentences from the table rows. |
| 18 | UN reappearance / hogtie / cemetery | A L50, B L95 | A L50 (UN h3). Cut from L95. |
| 19 | Unarmed in Undead Nightmare | A L49, B Weapons L91 | A L49. Cut from L91. |

## 4. Summary for the correctors

**A (Biography)**
- L39: align the bear with the transcript (he shouts "Shoot it!", he and John open fire and kill it).
- L27: drop "offers to share with John"; shorten the Fordham "degeneracy" sentence to a clause.
- Optional: L34 attributed "around May 1911" (wiki deduction); L42 attributed handshake. Low priority.

**B (Personality, Relationships, Skills)**
- L52: add the GOTY guide line "writing a book about Native Americans and the last days of the old west" (attributed). Only real add.
- L53: remove "never sleep again" and "begs John not to leave him" (A owns them); keep cocaine offer here OR in L63, not both.
- L63-64 (John): cut Norse stock, Ross's story, thanks/hug.
- L66 (Nastas): cut the "wise man... stupid" line and shrink the buffalo clause.
- L69 (Ross), L71 (Fordham), L73 (Dutch), L77 (Fortisque): cut retold narrative, keep one pointer clause each.
- L86: cut "explores with the mind". L91: cut UN unarmed. L95: cut Nashoba and UN reappearance.

**C (Missions, Quotes, Trivia)**
- Cut Trivia L168 (Fortescue/Fortisque, told in B L79).
- Table L102/L103: drop the "fails if" sentences (B L95 owns them).
- Optional: add the station line "My research is complete; much as I thought, there's no civilizing this savage land." and/or the wiki header quote (attributed, not in transcripts).

**D (base, Development, Reception)**
- Optional: facts grid L13 "c. 1869 according to the Red Dead Wiki". Nothing else.

Excluded: wiki trivia speculation (Mantegazza, Deloria, mad scientist, Damnation/Protestant, irony, foreshadowing), wiki
personality judgments, "brilliant savage companion" (not in transcript), shopkeeper mention in Help a Brother Out (unconfirmed).
