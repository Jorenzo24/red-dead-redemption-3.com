# Coverage report: Vincente de Santa (v3, medium tier)

Wiki EN (coverage.py): 1 712 words. Our fiche EN: 7 666 words (447 %). FR wiki (raw wikitext, ~900 words) adds almost nothing new.
Line numbers Lnn refer to `desanta_full_en.txt`. Transcripts = `scripts/v3/work/_m/*_dialogues.txt`.

## 1. Wiki facts missing from the fiche

| # | Wiki excerpt | Status | Recommendation |
|---|---|---|---|
| 1 | "I am the government, or what is left of it." (Quotes) | CONFIRMED, Civilization_at_Any_Price_dialogues L53 | C Quotes, Civilization block (mission line). |
| 2 | "This isn't America, Señor. We are poor. Kindness must take a different form." (Quotes) | CONFIRMED, Civilization dialogues L89 (continues: "What is better, to put your arm around a hungry man, or to beat him until he grows some food to eat?") | C Quotes. |
| 3 | FR wiki quote: "Abraham Reyes est un traître, un menteur, un lâche et un pêcheur..." | CONFIRMED, Civilization dialogues L163 ("He is a traitor, a liar, a coward and a sinner. A hero who has done nothing. I have more respect for the shit I took this morning than I ever will for that pathetic worm.") | C Quotes. L66 (B, Reyes entry) already says "(see Quotes)" but the line is absent: dangling pointer. |
| 4 | "Colonel Allende controls any situation..." (wiki prose, not quote list) | CONFIRMED, The_Demon_Drink_dialogues L83 | C Quotes. L60 (B, Allende entry) says "(see Quotes)" but nothing matches: dangling pointer. |
| 5 | "My country is in pain, John Marston. Terrible pain." (Quotes) | CONFIRMED, Civilization dialogues L35 | Paraphrased at L30; optional quote in B "In his own words" or C. |
| 6 | "The peasants are stupid and like cows they can be herded. It only takes a few men to move many." | CONFIRMED, Civilization dialogues L129 | Paraphrased at L51; quote it in B "In his own words" (strong characterising line). |
| 7 | "Go get drunk! Go get a woman! Enjoy life! It's a beautiful struggle!" | CONFIRMED, Empty_Promises_dialogues L59 ("It is a beautiful struggle!") | C Quotes (paraphrased at L36 and L51 only). |
| 8 | "If my men are dead, the rebels will all die, if they're alive, they have failed me..." | CONFIRMED, Demon Drink dialogues L91 | Paraphrased L33; optional C Quotes. |
| 9 | "When I put on this uniform I swore a sacred oath ... One day soon I will be a general." (Personality, attributed to Civilization) | WIKI-ONLY (not in the wiki's own Civilization transcript) | C "Lines from the wiki's quote list", flagged "no transcript"; B may add one clause "he says he will one day be a general" attributed to the wiki. |
| 10 | "Sometimes we must be brutal to be kind. It is what men do." (Demon Drink) | WIKI-ONLY (not in transcript) | C wiki-list block, "no transcript". |
| 11 | "My friend, I bleed red, white and green. I love my God and country, before I love myself..." (Demon Drink) | WIKI-ONLY (not in transcript) | C wiki-list block, "no transcript". |
| 12 | (not in wiki prose; transcript) John: "Are you married? Or do you rape young girls like your Colonel?" De Santa: "No, I could never touch a woman like that! It is not my way! But, for them, it is an honor to please their leader." | CONFIRMED, Cowards_Die_Many_Times_dialogues L45-47 | A Origins L26, one sentence before "I am married to my country" (the paragraph currently starts from John's question without its content). Also supports wiki's "procuring women" theme. |
| 13 | Espinoza: "I am Allende's brazo derecho" / "The Coronel needs a maid, a woman he cannot fuck. De Santa is that woman." | CONFIRMED, Mexican_Caesar_dialogues L89, L93 | B Espinoza entry, paraphrase (contradicts the wiki trivia that De Santa is Allende's right hand; see §2). |
| 14 | Allende berates him (Demon Drink opening) | CONFIRMED, Demon Drink dialogues L3: "You talk of loyalty but you are transparent. You'll be applauding when my head is impaled, won't you?" | B Allende entry, one clause (only the slurs are given today, under Names). |
| 15 | Quique and De Santa "leave with arms around each other" when bringing women to Allende | WIKI-ONLY (transcript only says "shepherding a couple of girls") | Optional, B Quique entry, attributed to the wiki, no inference. |
| 16 | Escalera gunsmith says De Santa often kisses him "as if I were his brother" (in Spanish) | WIKI-ONLY (no transcript, ambient line) | Optional, C Trivia, attributed, the reported line only; drop the wiki's "implied feelings". |
| 17 | Infobox: "Deputy governor of Nuevo Paraíso" | WIKI-ONLY, unsupported by any transcript | Do not add (or mention only as the wiki's infobox claim in the facts grid; low value). |
| 18 | FR wiki: his uniform differs from Espinoza's and resembles Allende's | WIKI-ONLY (FR) observation | Optional, B Appearance, one clause. |
| 19 | Rebel/Victor: "De Santa likes to do a lot of things to men on their knees" | WIKI-ONLY and self-contradictory (Personality gives a rebel, Trivia gives John to Victor); the Downfall transcript has only "I don't like to kill a man on his knees" | Do not add. |
| 20 | Executed rebel at Sepulcro = Chico Renovales | WIKI-ONLY, contradicted (Chico's own wiki page does not list Downfall) | Do not add. |
| 21 | Burgundy patches = general staff; Brian Jeremy comparison; guards whispering, "look of longing", caressing a woman; Scarface inspiration (FR); "admires Allende as saviour"; "tries to have John killed a few times" | SPECULATIVE / interpretation | Do not add. |

Everything else in the wiki (GOTY description, 1877 grave and inscription, family/English/father dialogue, rank, Chuparosa betrayal, Sepulcro and Casa Madrugada trap, Undead Nightmare, mission list, multiplayer pack and lines, civilian kill, lazy eye, "Coronel" subtitles, Michael De Santa, Reyes's two remarks, mariconcito, Espinoza's barmen line, Volcanic Pistol from FR) is covered.

## 2. Places where the fiche differs from the wiki

1. **Family / English / father dialogue** (wiki: in Civilization and Demon Drink). Neither wiki transcript contains it. The fiche (L25) attributes it to the wiki and says so: correct handling, keep.
2. **Chuparosa betrayal**. Wiki: John wakes "on the ground, hands tied", saved by "a lone bullet" from Reyes. Transcript (Cowards L117-125): his head is dunked in a horse trough, De Santa has him lifted up, Reyes kills the would-be executioner, then cuts his ropes. Fiche (L40) follows the transcript: fiche right.
3. **Execution at Sepulcro**. Wiki quote list: "El nombre es Colonel Allende, ahora cavar su tumba" and names the victim Chico Renovales. Transcript (Downfall dialogues): "En al nombre del gobierno no provincial del Coronel Allende ... te condeno a muerte por traición! Tienes algunas últimas palabras?" Fiche (L41) follows the transcript and leaves the rebel unnamed: fiche right.
4. **Reyes's line**. Wiki trivia: "sleep safe in their beds". Transcript (Gates of El Presidio L50): "A lot of young boys will sleep safer in their beds now." Fiche right.
5. **"Men on their knees"**. Wiki gives the line to a rebel (Personality) or to John talking with Victor (Trivia). The Downfall transcript has only John's "I don't like to kill a man on his knees, even if he did deserve it" (rebels' version). Fiche (L43) right; do not import the wiki line.
6. **Right hand of Allende**. Wiki trivia (burgundy patches) calls De Santa Allende's right hand. In Mexican Caesar (L89) Espinoza claims that role for himself ("I am Allende's brazo derecho"). The fiche makes no claim: keep it that way; at most quote Espinoza's claim (§1 #13).
7. **Escape at Chuparosa**. Wiki: De Santa "manages to escape". No transcript line shows it; fiche (L40) attributes it to the wiki: correct.
8. **Age**. GOTY guide 33 (1911), Ledger No. 58 "age 34", grave 1877-1911. Not a contradiction (birthday timing); fiche gives all three with sources: keep.
9. **Weapon**. EN wiki Cattleman + Repeater Carbine, FR wiki Volcanic Pistol. Fiche L86 gives both, attributed: keep.
10. **Mexican Caesar "suicide mission"**. Wiki states De Santa sent John and Espinoza on a suspected suicide mission. Fiche gives it only through John's and Espinoza's lines (L38, L118): correct (it is their suspicion, not a fact).

No case found where the fiche is wrong against a transcript.

## 3. Duplicates inside the fiche

| # | Fact | Occurrences | Keep |
|---|---|---|---|
| 1 | Mission fails if John assaults/kills/abandons him | L87 (B), L191 (C Trivia) | B L87; cut L191 (keep only "Downfall fails if he is killed before he talks" if moved into L87). |
| 2 | Counted as a civilian kill | L87, L192 | B L87; cut L192. |
| 3 | Downfall chase behaviour (steals horse, herded like cattle, new revolver/rifle, shoots rebels) | L87, L196 | B L87 (add "if close to the rebels he fights them and ignores John" there); cut L196. |
| 4 | Fistfight: rebels shoot, dialogue as if John killed him | L87, L197 | B L87; cut L197. |
| 5 | Shooting contest (5 shots, 25 dollars, three times) | L39 (A), L86 (B), L195 (C), L96 (table) | B L86 for mechanics, A one clause, table reward; cut L195. |
| 6 | "Dumb and loyal to his awful master" | L44 (A paraphrase), L64 (B quoted), L143 (C quoted) | C L143 as the quote; B L64 drops the quotation (pointer to Biography). |
| 7 | Reyes "two men / too much time with Captain de Santa" | L67 (B quoted), L133 (C quoted), L101 (table) | C L133; B L67 paraphrases without quotation marks. |
| 8 | Reyes "young boys will sleep safer" | L44 (A), L67 (B quoted), L181 (D, Reception, as quoted by the archive) | Mission line -> move the quote to C (Gates of El Presidio block); A paraphrases; B one clause; D keeps its mention (it describes the archive). |
| 9 | Reyes's reactions at El Presidio (glad it was John's bullet / why not you) | L44 (A), L67 (B), L141 (C) | A + C; B reduced to "see Biography". |
| 10 | Victor at Sepulcro (kill or pleasure, glad it was you / should have been you, hundreds of deaths, army without leaders) | L42-43 (A), L80 (B), L135-137 (C) | A + C; B L80 trimmed to his role (leads John to Sepulcro) + pointer. |
| 11 | Espinoza on the escort ("two men De Santa hates most", "kill him or should I", praise at Torquemada) | L38 (A), L76 (B), L129/L131 (C) | A + C; cut L76 first two sentences. |
| 12 | Reyes as rich man / golden cradle / balcony speeches / coward who writes poems | L31, L39 (A), L66 (B) | B L66 (it is a relationship), A one clause each. |
| 13 | Married to his country, never took a wife, avoids women, mother as example | L26 (A Origins), L51 (B Personality), L53 (B own words), L82 (B parents) | A L26 (self-told backstory) + L53 quote; cut the wife/women sentence from L51 and the mother sentence from L82 (pointer). |
| 14 | "Enjoy wine and women / enjoy life" after Torquemada | L36 (A), L51 (B) | A L36 (and C quote per §1 #7); cut from L51. |
| 15 | "Colonel needs recreation like anyone else" | L33 (A), L61 (B) | A L33; B L61 pointer. |
| 16 | Allende tells him he is not his shadow / scolds him for standing behind | L33 (A), L60 (B) | B L60; A pointer. |
| 17 | Ledger spelling "Vicente" | L10 (grid), L45 (A), L55 (B Names) | Names L55 + grid; cut "The paper spells his first name without the second n" from L45. |
| 18 | Hogtie and carry to cemetery entrance | L42 (A), L87 (B) | A for narrative, B for objective; acceptable, trim one. |
| 19 | Intro L2 recap (decoy train, Tesoro Azul, Torquemada) vs Key facts L5-6 | D, D | Acceptable (same owner), optionally shorten L2. |

## 4. Summary for the correctors

**A (Biography)**
- L26: add John's question and De Santa's answer ("I could never touch a woman like that ... an honor to please their leader", Cowards L45-47).
- L33: replace the "not my shadow" retelling by a pointer; L36/L33 keep the narrative.
- L45: cut the spelling sentence (owned by Names).
- L44: keep Reyes/John exchange as paraphrase only.

**B (Personality, Relationships, Skills)**
- L51: cut the wife/women and "enjoy wine and women" sentences (A/L53 own them); optionally quote the "herded like cows" line in "In his own words".
- L60 Allende: add Allende's "you are transparent ... applauding when my head is impaled" (Demon Drink L3), paraphrased; fix the dangling "(see Quotes)" once C has the line.
- L64: remove the quotation marks around "dumb and loyal..." (C owns it).
- L66 Reyes: dangling "(see Quotes)" resolved by C adding the insult line; trim golden cradle/balcony from A or here (keep here).
- L67: paraphrase the two Reyes lines, pointer to Biography/Quotes.
- L75-76 Espinoza: add his "brazo derecho" and "De Santa is that woman" remarks (Mexican Caesar L89, L93); cut the escort retelling in L76.
- L80 Victor, L82 parents: trim to pointers.
- L87: absorb "fights the rebels and ignores John" from L196.
- Optional WIKI-ONLY: Quique arms-around exit (attributed); "one day soon I will be a general" (attributed).

**C (Missions, Quotes, Trivia, Other media)**
- Quotes, add from transcripts: "I am the government, or what is left of it" + "This isn't America ... Kindness must take a different form" + the Reyes insult "a traitor, a liar, a coward and a sinner ..." (Civilization); "Colonel Allende controls any situation ..." (Demon Drink); "Go get drunk! ... It is a beautiful struggle!" (Empty Promises); optionally "My country is in pain" and "If my men are dead...".
- Quotes, wiki-list block ("no transcript"): sacred oath / "One day soon I will be a general", "brutal to be kind", "I bleed red, white and green".
- Quotes: move "A lot of young boys will sleep safer in their beds now" into the Gates of El Presidio block.
- Trivia: cut L191, L192, L195, L196, L197 (told in B L86-87). Optional WIKI-ONLY: Escalera gunsmith's "as if I were his brother" line, attributed.

**D (base, Development, Reception)**
- Nothing missing. Do not add "deputy governor" (unsupported) or the Scarface inspiration (speculative). Optionally shorten the intro recap that repeats the Key facts.
