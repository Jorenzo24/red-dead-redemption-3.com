# Coverage report: Alberto Fussar (v3, medium tier)

Inputs: wiki EN `en.txt` (1,049 words per coverage.py), wiki FR `fr.txt` (476 words), our fiche `fussar_full_en.txt`
(4,877 EN words, 464 % of the wiki; FR 5,809 words). Transcript = fan transcript `fc/gsw.txt` (line numbers Gnnnn).
Binding lead decisions: `FIX_RULES.md` (cannon only; Hercule's diversion wiki-only; B owns the quoted lines; nationality
attributed; Ledger No. 68 = "a later issue").

Coverage is good: every non-speculative fact of the EN and FR wiki pages is in the fiche except the items below
(mostly quotes and small details). Wiki sections History, Personality, Appearance, Mission appearances, Trivia and
Gallery are all covered; the gaps are listed in section 1.

## 1. Wiki facts missing from the fiche

| # | Wiki excerpt | Status | Recommendation |
|---|---|---|---|
| 1 | Quotes: "You maggots are going to die. The US Navy is on the way." (wiki: "Alberto Fussar's last words") | CONFIRMED: G10975 "You maggots are going to die." and G10978 "The US Navy is on the way." (two separate lines, Dutch answers in between). These are his last spoken lines in the transcript; he says nothing at the tower. | **B**, "In his own words": quote both lines verbatim as two lines (in the cabin standoff, to Dutch and Arthur). A L37 keeps its paraphrase. Do not call them "last words" in a way that implies he speaks at the tower. Ties to Narciso's "Looks like fun, maggots" (D L124, already there). |
| 2 | Quotes: "The last few days have been very unsettling for all of us, but now is the time... to show our ferocity." | WIKI-ONLY (wiki quote list; absent from the fan transcript, probably an ambient line of the Aguasdulces speech) | **B**, "In his own words", optional, one sentence attributed: "The Red Dead Wiki's quote list adds a further line of the speech: ...". B already says it checks against the wiki quote list. |
| 3 | History: Simon "orders them to be locked up before leaving" | CONFIRMED: G10507 (in Spanish) "Corporal. Take these men to the jail, along with that peasant's group of cockroaches. Any nonsense from them... shoot them all." then G10508 "Welcome to Guarma, gentlemen. Now, if you'll excuse me." | **A**, "Welcome to the New World" paragraph (L32): one sentence, paraphrased (Simon orders a corporal to take them to the jail with the captured rebels and to shoot them all at the first trouble, then leaves). |
| 4 | History: Simon's men "chains them with captured rebels" | CONFIRMED: G10507 ("that peasant's group"); same wording already in javier_A, micah_A, bill_A ("chain them with captured local rebels") | **A** L32: add "together with captured rebels" to the chaining sentence (B L60 Leon entry already implies it; keep A as the narrative owner). |
| 5 | Appearance: "black jeans tucked into boots... a holster on his right hip" | WIKI-ONLY (visible in gallery screenshots FussarStandoff / FussarCanon) | **B**, Appearance (L51): optional, add "and a holster on his right hip" to the Guarma sentence. Stay at 3 sentences; no outfit catalogue. |
| 6 | Background: "likely born in Cuba... medals... probably served in the Spanish military... transferred his allegiance to the Cuban Military, where he rose to the rank of colonel" | SPECULATIVE (sourced to a Reddit post) | Do not add. A L24 already says the game gives nothing of his early life. |
| 7 | Background: "built up connections with political elites of the city of Saint Denis"; FR "établit rapidement une liaison avec la ville de Saint Denis" | SPECULATIVE / interpretation (the only fact is his presence at the mayor's party, already told) | Do not add. |
| 8 | Personality: "appears to take some amount of pleasure... with open delight"; "arrogant and prideful... personally manning a cannon" | SPECULATIVE (interpretation) | Do not add. The observable facts (mocking Javier, cages, manning the cannon) are already in A/B. |
| 9 | Trivia EN + FR: comparison with Agustin Allende (both colonels, governors of Spanish-speaking lands, main antagonists of a chapter abroad, similar uniform and hair, sabre, killed before the protagonist returns to the US) | SPECULATIVE / fan analysis | Do not add. Consistency: allende_B docstring explicitly excludes "Fussar comparisons of the FR wiki (fan analysis)". |
| 10 | Trivia: under McKnight "the workers being mistreated even worse than under Fussar" | Interpretation beyond the article text ("Unrest in the Tropics" only says the investors subject workers "to harsh conditions and penalties") | Do not add. A L41 already reports the article accurately. |
| 11 | (Primary text the wiki page links to) "Leader of Guarma Assassinated": third headline "GREAT SORROW AND SCENES OF RAGE IN GUARMA."; "the most intense of excitement on many of the islands in the Spanish West Indies"; "American businesses have done a great deal of trade with him in sugar" | CONFIRMED (`_m/Leader_of_Guarma_Assassinated.txt`) | **A** L39, optional: add the third headline and the Spanish West Indies reaction in paraphrase. Do not re-quote anything B quotes (FIX_RULES 3). |
| 12 | (Primary text) "Guarma Island Sugar Boom": headline "FUSSAR CALLED FRIEND THE OF THE US." (sic); Cornwall "stood next to a ship unloading Cuban sugar" and "hailed a new era of cooperation between the two countries"; the boom "is undercutting the US sugar industry and resulting in the loss of American jobs" | CONFIRMED (`_m/Guarma_Island_Sugar_Boom.txt`; the jobs point is also in leviticus_B) | **A** L26, optional: paraphrase the headline and the US-jobs criticism in one sentence each. |
| 13 | (Not on the Fussar page; needed by our own pointer) "Savagery Unleashed": Arthur, knocked out by a dart, is tied to a chair and beaten by a soldier (the wiki's "Angel", Fussar's interrogator), gives the false name "Leviticus Cornwall", then breaks free | CONFIRMED: G10600-10612 (captor beats Arthur; "I'm an American... my name is Leviticus Cornwall..."; Arthur breaks the chair and knocks him out). Guards name Angel and say he enjoys torturing (G10636-10646). Angel = Fussar's interrogator is WIKI-ONLY (`_m/Cuban_Military.txt`). | **A** L32: one sentence on the interrogation in "Savagery Unleashed" (no quote). Otherwise B L78's "(see Biography)" points to nothing. |

FR wiki: no fact missing beyond the above (its only extra trivia, "impossible to talk to him during the party", is in C L133).

## 2. Places where the fiche differs from the wiki

1. **Tower weapon.** Wiki character page: cannon. Mission page "Paradise Mercifully Departed": "Gatling Gun"; FR wiki:
   "Gatling"/"mitrailleuse". Decided by the transcript: G10997 "[Fussar loads the cannon.]", G10999 Hercule "He's
   shooting", plus the FussarCanon / FussarDeath screenshots. **Cannon is right** (FIX_RULES 1). The fiche's A L38 is
   right; **B Weapons L87 is wrong** ("Sources differ... Gatling gun"): rewrite as cannon only, drop the "sources differ"
   sentence. Also clean the "sources differ" note in the fussar_B and fussar_D docstrings. Cross-fiche (per FIX_RULES):
   arthur_C "machine gun", dutch_B "machine gun", dutch_C "Gatling gun" -> cannon.
2. **Hercule draws Fussar's fire.** Wiki-only: the transcript has only G10999 "He's shooting, we have to take him down!
   Arthur, there's another cannon up ahead on our left. Can you get to that?". A L38 attributes it correctly; **B L58
   (Hercule relationship) states it as fact: attribute or cut** (FIX_RULES 2; also arthur_D).
3. **The rifle to the captain.** Wiki and mission page: Arthur "kicks" it; arthur_C, arthur_D, dutch_B: "kicks"; the
   fan transcript's stage note G10985 says he "tosses the rifle... into the captain's hands"; the mission page's gold
   medal tips say "kick the gun to him". The fiche is inconsistent with itself: A L37 "pushes", B L72 "kicks". **Use
   "kicks" in A** (house wording, gameplay prompt).
4. **Who works the plantation.** Wiki: Fussar "enslaved nearly the entirety of the population". Transcript G10573,
   Leon: "They're little more than slaves shipped in from other islands." **The fiche is right** (L25, L83); do not adopt
   the wiki's wording.
5. **Newspapers call him "fair and just".** Wiki Personality. The articles say "a kind and effective leader", "a
   progressive leader and humanitarian" (`_m/Leader_of_Guarma_Assassinated.txt`); "fair and just" appears nowhere.
   **The fiche is right** (L43).
6. **First appearance.** Wiki: "Fussar himself is first seen when Dutch and Arthur sneak into Aguasdulces", which
   contradicts its own Saint Denis section. Transcript G9077 (Bronte at the party) and G10701 (Arthur remembers him).
   **The fiche is right** (L29, L33).
7. **"Last words" as one quote.** Wiki joins "You maggots are going to die. The US Navy is on the way." into one line.
   Transcript G10975 / G10978: two lines with Dutch's reply in between. If quoted (section 1 #1), quote as two lines.
8. **Standoff geometry.** EN wiki: Dutch held at gunpoint by Fussar; FR wiki: Dutch threatens Fussar. Transcript G10974:
   Dutch draws a second revolver as Fussar enters, and Arthur aims at Fussar from the floor. **The fiche matches the
   transcript** (L37). No change.
9. **Javier's animal.** Wiki and fiche: donkey; transcript stage note G10753: "tied to a horse"; Fussar's own line
   G10758: "even the mule". Fiche (donkey) matches javier_A/B/C: **keep "donkey"** for cross-fiche consistency; do not
   change.
10. **Navy.** Wiki: "alerts the Cuban Navy". Transcript G10853: "Fussar has called in the navy from Cuba". Fiche uses the
    transcript wording (L35). No change.
11. **How Fussar dies.** Mission page: cannon "or shoots him"; character page trivia: one shot from any gun "if the
    player stands in the correct angle". Fiche gives both (A L38, B L87). Consistent; but see duplicates (section 3 #9).
12. **Nationality.** Wiki infobox EN and FR: Cuban. Not stated in game. Fiche attributes it (L15, L81). Right
    (FIX_RULES 4).

## 3. Duplicates inside the fiche (per OWNERSHIP.md and FIX_RULES 3)

| # | Fact told more than once | Occurrences | Keep |
|---|---|---|---|
| 1 | Leon "A tyrant, driven by nothing but power and greed..." | B L44 (quoted), C L106 (quoted); A L25 paraphrase | Keep B L44. **Drop C L106.** A paraphrase OK. |
| 2 | Bronte "whore and despoil himself" | B L44 (quoted), C L102 (quoted, longer); A L29 paraphrase; B L74 pointer | Keep B L44. **Drop C L102.** |
| 3 | Micah "thorough, nasty and vindictive" | B L44, C L116 | Keep B. **Drop C L116.** |
| 4 | Hercule "It doesn't matter how many we kill. He will have the money to get more." | B L85 (Power on Guarma, quoted), C L112 (quoted); A L35 paraphrase | Keep B L85. **Drop C L112.** |
| 5 | Simon "Mr. Fussar has a lot of very powerful friends" | B L85 (quoted), C L104 (quoted); A L25 paraphrase | Keep one: B L85 per the B docstring ("Quoted in Power on Guarma (not elsewhere)"); **drop C L104** (or keep C and paraphrase B). |
| 6 | "Leader of Guarma Assassinated": "a kind and effective leader who brought peace and prosperity to the region" + workers' rights | A L39 (quoted verbatim) and B L43 (quoted verbatim) | Keep B L43 quoted. **A L39: paraphrase** the business leaders' praise (FIX_RULES 3). A keeps the headlines, "Reports conflict...", "several white men", locals. |
| 7 | "Guarma Island Sugar Boom": "a controversial figure who is flamboyant at times and cruel at others", "quasi-military rule" | A L26 (quoted) and B L43 (quoted) | Keep B L43. **A L26: paraphrase.** |
| 8 | Same article: "14 hour shifts", security force "feared across the island" | A L26 (quoted) and B L83 (quoted) | Keep B L83 (Power on Guarma). **A L26: drop or one-clause paraphrase.** |
| 9 | Tower kill can also be a gunshot | A L38 ("According to the mission page...") and B L87 (Weapons) | Keep B Weapons (gameplay). **A L38: drop the sentence.** |
| 10 | Fussar's estate (stone wall, manor, cages, factory, mill) | B L81 (attributed) and C L136 Trivia (attributed, longer) | Trivia must hold only facts told nowhere else: **drop C L136**, or keep C and cut the last sentence of B L81 (adding barn, well, tower-to-caves there). One place only. |
| 11 | Dutch draws his second revolver in the standoff | A L37, B L66 (Dutch entry), C L138 Trivia | **C L138: keep only the "American Venom" repeat**, drop the first sentence. B L66: "(see Biography)" clause is enough. |
| 12 | Hercule "I'll fight (Alberto) Fussar every day I can" | A L36 (paraphrase), B L58 (paraphrase), C L118 (quote) | Keep C quote and A paraphrase; **cut the sentence from B L58.** |
| 13 | Arthur "I got him for you, Javier" | A L38, B L62 (Javier entry), C L120 (quote) | Keep C quote + A paraphrase; **cut from B L62** (or reduce to "see Biography"). |
| 14 | Arthur recalls Fussar from Bronte's party | A L33, B L64 (Arthur entry), C L108 (quote) | Keep A + C; **B L64: cut the first sentence.** |
| 15 | Dutch "Very kind of you, Mr. Fussar!" | A L35, B L66 (partial quote "Mr. Fussar"), C L110 (quote) | Keep C quote + A paraphrase; **B L66: drop the sentence** (or paraphrase without quotation marks). |
| 16 | Hercule: Fussar knows who they are / price on their heads / navy called from Cuba | A L35 and B L85 | Keep A (narrative). **B L85: cut to one pointer clause.** |
| 17 | Micah's report (captain held, gun positions) | A L36, B L68 (Micah entry), B L85 | Keep A. **B L85: drop the sentence**; B L68 is already a short pointer. |
| 18 | Hercule's diversion at the tower | A L38 (attributed), B L58 (unattributed) | Keep A. **B L58: cut** (also fixes FIX_RULES 2 there). |
| 19 | Cornwall exclusive purchase order / "a great friend of America" | Intro L2, key fact L6, A L26 (quoted), B L54 (quoted), B L83 pointer | D intro/key facts are summary (OK). **Quote "a great friend of America" once**: keep B L54 (Relationships), paraphrase in A L26 (FIX_RULES 3). |
| 20 | Wiki: soldiers belong to the Cuban Military under his command | A L24 (attributed) and B L81 (attributed) | Keep B L81. **A L24: drop the sentence.** |
| 21 | Leon: workers "little more than slaves shipped in from other islands" + escaped group | A L25 + L32 (paraphrase), B L83 (quoted), key fact L5 | Quote only in B L83; A paraphrase OK. No change unless trimming. |
| 22 | Angel as Fussar's interrogator (wiki) | B L78 (relationship) and B L85 | Keep B L78. **B L85: drop the sentence.** |

## 4. Summary for the correctors

**Part A (Biography)**
- L32 "Welcome to the New World": chained together with captured rebels; Simon orders a corporal to take them to the
  jail and shoot them at the first trouble, then leaves (G10507-10508, paraphrase).
- L32 "Savagery Unleashed": one sentence on Arthur's interrogation (knocked out by a dart, tied to a chair, beaten,
  gives the false name Leviticus Cornwall, breaks free; G10600-10612), so B L78's pointer has a target.
- L37: "pushes a rifle" -> "kicks a rifle" (house wording, arthur_C/D, dutch_B).
- L24: drop the "Cuban military under his command" sentence (owned by B L81).
- L26: paraphrase "controversial... flamboyant... cruel... quasi-military rule", "14 hour shifts", "feared" and "a great
  friend of America" (quoted in B). Optional: headline and US-jobs criticism of the article (paraphrase).
- L38: drop "According to the mission page, Arthur can also kill him with a gunshot..." (owned by B Weapons).
- L39: paraphrase the business leaders' praise (quoted in B L43). Optional: third headline "great sorrow and scenes of
  rage" and the Spanish West Indies reaction (paraphrase). Keep "a later issue" (FIX_RULES 5).

**Part B (Personality, Power on Guarma, Relationships)**
- In his own words: add "You maggots are going to die." and "The US Navy is on the way." as two lines (cabin standoff,
  G10975/G10978). Optional: the wiki-only "...show our ferocity" line, attributed to the wiki's quote list.
- Weapons L87: cannon only; delete "Sources differ... Gatling gun" (FIX_RULES 1). Clean docstrings of B (and D).
- Appearance L51 (optional): holster on his right hip (wiki-only, visible in screenshots).
- Hercule L58: cut "He draws Fussar's fire..." (or attribute to the Red Dead Wiki) and cut the "every day I can"
  sentence.
- Javier L62: cut "When the tower falls, Arthur says he got Fussar for Javier."
- Arthur L64: cut the first sentence (party recollection).
- Dutch L66: cut the "Mr. Fussar" sarcastic thanks sentence.
- Power on Guarma L85: cut the Angel sentence, the Hercule "knows who they are / navy" sentence and the Micah report
  sentence (pointers only); keep "powerful friends" and "more money" quotes here.
- L81 vs C L136: estate description in one place only (coordinate with C).

**Part C (Missions, Quotes, Trivia, Other media)**
- Quotes: drop Bronte (L102), Leon (L106), Micah (L116), Hercule "more money" (L112) and Simon "powerful friends"
  (L104): all quoted in B. Keep Arthur (L108), Dutch (L110), Dutch/Arthur (L114), Hercule "every day" (L118), Arthur
  "I got him for you" (L120). Replace with other verified mission lines if the list gets thin (e.g. Hercule G10572
  "I bring things in and off the islands... behind Colonel Fussar's back", G10567 "Fussar will be desperate to find
  you", G10994-10998 "Fussar is up there I think." / Arthur "In the tower?").
- Trivia L136: drop (estate already in B L81) or move its extra details into B and drop.
- Trivia L138: keep only the "American Venom" repeat of the standoff.
- No Allende comparison (fan analysis, excluded on the Allende fiche too).

**Part D (base, Development, Reception)**
- Docstring: "sources differ: cannon vs Gatling gun" -> cannon (FIX_RULES 1). No visible text change needed.

**Cross-fiche (per FIX_RULES)**: arthur_C "machine gun" -> cannon; dutch_B "machine gun" -> cannon; dutch_C "Gatling
gun" -> cannon; arthur_D Hercule's diversion attributed to the Red Dead Wiki. EN + FR, HTML regenerated.
