# Coverage report: Nigel West Dickens (v3, medium tier)

Length: our EN 6,921 words vs Red Dead Wiki EN 1,848 words = **374 %** (FR wiki 899 words). Every wiki section has a counterpart in the fiche (Background -> Origins; RDR2 -> 1907 article + Moncrief letter; RDR1 New Austin / West Elizabeth -> Acts I and III; Undead Nightmare -> own h3; Mission appearances -> Missions; Personality; Quotes; Trivia; multiplayer -> Other media). Coverage is near complete: the gaps below are small.

## 1. Wiki facts missing from the fiche

| # | Wiki excerpt | Status | Recommendation |
|---|---|---|---|
| 1 | "Bill Williamson had escaped yesterday morning" (RDR1 section) | CONFIRMED: Fort Mercer dialogues l.95, Jonah: "Bill's already run off to Mexico yesterday morning" | A, L39: "says he left for Mexico the morning before". |
| 2 | 1907 article: vowed to uncover "Hippocratic frauds" | CONFIRMED: fc/Man_Exposes_Medical_Frauds.txt l.11/15 (subhead "HIPPOCRATIC FAKERS PLAGUING SMALL CITIES") | A, L28: optional, quote the two words "Hippocratic frauds" in place of "these frauds". |
| 3 | "Today, we are gladiators! Motivation, dear boy!" (quote list) | CONFIRMED: Liars, Cheats dialogues l.89 (full line: "...you are not an aging bounty hunter and I am not an avant-garde business pioneer. No sir. Today, we are gladiators!") | C Quotes, Act I: good add (not quoted anywhere in the fiche). |
| 4 | "I refuse to let the blind stupidity of the proletariat derail my calling in life!" | CONFIRMED: Sport of Kings dialogues l.25 | C Quotes, Act I: optional add. |
| 5 | "I have a soft spot for life's flotsam and jetsam." | CONFIRMED: Liars, Cheats dialogues l.39 (continues the "I see the good in everybody" line) | B "In his own words", L50: extend the existing quote with this sentence (no new entry in C). |
| 6 | Answers "Voltaire" with "Mais comme ça comme oui" | WIKI-ONLY (conversation not in the transcript) | A, L24 already says "answer John in French"; may quote the line with the existing wiki attribution. Optional. |
| 7 | UN, "American Imperialism": Dickens's age prevents him from posing as a soldier himself | WIKI-ONLY (no transcript) | A, UN h3, L45: optional clause, attributed to the wiki. |
| 8 | Nationality "American (English descent)" | WIKI-ONLY, no in-game source | Do not add (the fiche's "American, speaks with an English accent" is safer). |
| 9 | W.C. Fields / Mr. Micawber model; "Carpetbagger" of The Outlaw Josey Wales | SPECULATIVE (wiki says "seem to be based", "appear to be influenced") | Do not add. |
| 10 | Scar on the neck = lynching | SPECULATIVE ("It seems", "likely") | Keep as is (B L55 reports the scar without the lynching inference). |
| 11 | Father died before 1911 (from "I'm coming home, Daddy") | SPECULATIVE inference | Keep as is (C L176 gives only the line). |
| 12 | Elixir "may be a laxative" | interpretation | Keep as is (John's "dose of salts" line already given). |
| 13 | FR infobox nicknames ("Le gras escroc", "N.W.D", "Le charlatan") | WIKI-ONLY (FR), no game source | Do not add. |

Everything else in the wiki (Fort Wayne, mother at the theater, Paris/London, Voltaire/Emerson/Homer, children and dead son, Moncrief letter c. 1898, 1907 article, Eli's report, Old Swindler Blues, the Trojan horse, Seth and Irish, Brittlebrush Trawl and "Europe or China", Blackwater arrest and Ross's "hero", UN tonic at 100 coins, free samples, man killed, plants, Blunderbuss, train, Scratching Post, Baghdad, leaves on foot, multiplayer Liars and Cheats, Cueva Seca urinating, Bollard/Walton recognition, small box, Blackwater wall writing, Seth not fighting undead, no horse riding, MacFarlane's Ranch anecdote, RDR2 shotgun catalogue, absent from 1914 Ledger) is covered.

## 2. Places where the fiche differs from the wiki

1. **Where John finds him** (wiki EN: "south of Coot's Chapel"; fiche L33: "Cholla Springs, on the outskirts of Armadillo"). The mission page Old_Swindler_Blues.txt l.4/8 gives "outskirts of Armadillo, in Cholla Springs". Fiche is right; no change.
2. **"Shot"** (wiki) vs "wounded" (fiche L33). Mission page l.28 says "wounded"; the cause is not stated. Fiche right.
3. **"Having exhausted customers in New Austin, he intends to travel abroad"** (wiki EN). No transcript line says this; at Brittlebrush Trawl (Paradise dialogues l.29-33) he says "this land is much too small" and men of science are not loved here. Fiche (L40) follows the transcript: right.
4. **FR wiki: he "can no longer go to China or Europe because of his scams"**. Wrong: the transcript has him leaving for "London or Paris or maybe Peking". Fiche right.
5. **FR wiki: John asks for his release because he helped capture Williamson AND Escuella.** Wrong: transcript line (fiche L151) is "he helped me get Williamson". Fiche right.
6. **FR wiki: two people eaten outside Fort Mercer**; EN wiki and mission page A_Cure... l.23: "A man walks out to test it". Fiche (one man) right.
7. **Blunderbuss remark: "1850" (EN Blunderbuss page) vs "1890" (FR quote box)**. No UN transcript exists; fiche L45 attributes "1850" to the EN wiki's weapon page. Acceptable; keep the attribution.
8. **Baghdad: "or his maker by way of the undead" (EN) vs "to meet one of his collaborators" (FR)**. No transcript; fiche follows EN with attribution. Acceptable.
9. **FR wiki: "West Dickens n'utilise pas d'armes"** vs EN infobox Cattleman Revolver. Fiche L93 gives both sides correctly (wiki lists the Cattleman; he never fires in the transcripts).
10. **Cross-fiche consistency (not a wiki difference, to fix):**
    - `scripts/fiches/parts/john_D.py` l.14 states as fact that John calls Emerson "another fool with his head in the clouds" when Dickens quotes him. The Nigel fiche (L23-24) says that conversation is WIKI-ONLY (absent from the Liars, Cheats transcript; grep confirms no "Emerson"/"Fort Wayne" in it). John's line should be attributed to the Red Dead Wiki, or the Nigel fiche must find a source.
    - First recorded scene: john_D.py l.126 says "according to producer Rob Nelson"; Nigel D (L162) says "IGN retrospective by Luke Reilly, 22 May 2020". Harmonize to one wording (e.g. "producer Rob Nelson, interviewed by IGN for its 22 May 2020 retrospective") after checking which is accurate.

## 3. Duplicates inside the fiche (per OWNERSHIP.md)

Quotes told twice (rule: each line in ONE place; B lines not repeated in C):
1. Leigh Johnson "narcotic and bat piss salesman..." : B Trade L88 AND C Quotes L119. Keep in C (mission line); B paraphrases without quotation marks.
2. "A Robin Hood with spurs. How romantic!" : B John L58 AND C Quotes L134. Keep in C; B paraphrases ("Dickens mocks him as a Robin Hood").
3. "I'm only an ageing vendor of exotic elixirs, not the bloody U.S. cavalry!" : B In his own words L51 AND C Quotes L140. Keep in B (already framed); cut the C entry, replace with #3 or #4 of section 1.
4. "2 dollars an ounce / 1.95 an ounce" : B Trade L86 AND C Quotes L126. Keep in C; B paraphrases the bulk discount.
5. "Because he's a harmless old fraud. The kind of man that built this country" : B John L59 AND C Quotes L152. Keep in C; B paraphrases.
6. Jonah "I can't understand a goddamn word he says" : B Jonah L69 AND C Quotes L121. Keep in B (it is the whole Jonah entry); C keeps only John's "flannel-mouthed bunko artist" line.

Facts told twice:
7. MacFarlane's Ranch anecdote: B Bonnie L75 AND C Trivia L180. Keep B, cut the trivia item.
8. Undead Bait recipe (Wild Feverfew + Prairie Poppy): B Trade L89 AND C Trivia L183. Keep B; trivia keeps only "only way to obtain the tonic" and Landon's Boom Bait.
9. Never rides a horse: B Wagon L91 AND C Trivia L179 (Trivia adds Allende and Luisa). Keep C (fuller), cut the sentence in B, or keep B and add the two names there.
10. Blackwater Ledger No. 53 article (one-legged woman in Plainview, old man to the brothel, list of ailments): A L32 AND B Trade L88. Keep in B Trade; A keeps one clause ("the Ledger already runs an article on his tonic, see Trade and the elixir").
11. John's "went through me like a dose of salts": A L37 (paraphrase) AND B L88 (quote). Allowed by the rule (A paraphrases), but A can drop the sentence.
12. "I will never give up on science": A L37 paraphrase + B L50 quote. Allowed; no change needed.
13. Dead Eye level 2 unlocked by the elixir: B L89 AND Missions table L99. Acceptable (table = rewards); optional cut in B.
14. Seth "old friend ... Coot's Chapel": A L35 AND B Seth L61. B can drop the location (already in A).

## 4. Summary for the correctors

**A (Biography)**
- L39: add "the morning before" to Bill's flight (Fort Mercer dialogues l.95).
- L28: optional, quote "Hippocratic frauds".
- L32: reduce the Ledger No. 53 retelling to one clause pointing to Trade and the elixir (dup #10).
- L37: optional, drop the "dose of salts" sentence (dup #11).
- L45 (UN): optional wiki-attributed clause on his age ruling out a soldier disguise.

**B (Personality, Trade and the elixir, Relationships)**
- L50: extend the quote with "I have a soft spot for life's flotsam and jetsam."
- L58, L59, L86, L88: turn the quoted lines (Robin Hood, harmless old fraud, 2 dollars/1.95, Johnson's bat piss line) into paraphrase; they stay quoted in C (dups #1, 2, 4, 5).
- L61: drop "Coot's Chapel" (dup #14). L91: drop "never rides a horse" or merge Trivia #9 here.

**C (Missions, Quotes, Trivia, Other media)**
- Quotes: cut L140 (cavalry, kept in B) and the Jonah half of L121 (kept in B); add "Today, we are gladiators!" (Liars, Cheats) and optionally the "proletariat" line (Sport of Kings).
- Trivia: cut L180 (MacFarlane's Ranch) and the recipe sentence of L183; resolve L179 against B L91.

**D (base, Development, Reception)**
- L162: harmonize the "first recorded scene" attribution with john_D.py l.126 (Rob Nelson vs IGN/Luke Reilly).
- Cross-fiche: john_D.py l.14 states the Emerson line as fact; attribute it to the Red Dead Wiki (EN + FR) to match the Nigel fiche.
