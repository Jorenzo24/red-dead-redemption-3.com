# Coverage report: Hercule Fontaine v3 (medium tier), 22 Oct 2026

Inputs: Red Dead Wiki EN (`en.txt`) and FR (`fr.txt`), our fiche `hercule_full_en.txt` (Lnn = its line numbers),
`python3 scripts/coverage.py hercule-fontaine "Hercule Fontaine"`, mission pages in `scripts/v3/work/_m/`
(Welcome_to_the_New_World, Hell_Hath_No_Fury, Paradise_Mercifully_Departed, A_Kind_and_Benevolent_Despot, Guarma_Rebels,
Cinco_Torres, El_Nido, La_Capilla, Baptiste, Leon_Fuentes, Leader_of_Guarma_Assassinated), the fan transcript
`fc/gsw.txt` (lines 10480-11010), authoritative parts (fussar_A/B, arthur_C/D, dutch_B, micah_B), HOUSE_FACTS.md,
FIX_RULES.md (binding).

Word counts (coverage.py): wiki EN 593 words (intro 96, Background 34, Guarma chapter 431, missions 20); wiki FR 267.
Our fiche EN 4,792 words = **808 % of the wiki EN**; FR 5,424 words (2,031 % of the wiki FR).
EN by section: intro/key facts/facts 382, Biography 1,764, Personality 382, Relationships 754, Smuggling and fighting 384,
Missions 191, Quotes 402, Development 196, Reception 63, Other media 83, Trivia 191, Gallery 0 (FIX_RULES 4: no gallery).

Every non-speculative fact of the EN character page is covered (lead, Background, all three Guarma paragraphs, infobox:
affiliations, weapons, occupation, location, voice, nationality as attributed). The gaps below are small; most come from
the FR wiki or from neighbouring wiki pages, and four of them must NOT be added.

## 1. Wiki facts missing from the fiche

| # | Wiki excerpt | Status | Recommendation |
|---|---|---|---|
| 1 | EN: "With Fussar dead, Hercule celebrates, seeing it as a great victory for the rebellion." | SPECULATIVE. The transcript (gsw.txt 10996-11006) gives Hercule no line between the tower shot and "We'll be like you..."; no celebration, no "victory" word. Interpretation of the wiki. | Do NOT add. |
| 2 | FR: "étant défini comme 'problématique' par les responsables cubains, il est envoyé sur l'île de Guarma" | SPECULATIVE / unsourced (no line in the transcript; contradicts his own "I am not from here. I bring things in and off the islands", gsw 10572). Already excluded in hercule_B docstring. | Do NOT add. |
| 3 | FR infobox: "activité : Esclave (Anciennement)" | Unsourced, nothing in the transcript. | Do NOT add. |
| 4 | EN/Guarma Rebels: soldiers called "Cuban troops" / "Cuban Military" | WIKI-ONLY label. The game shows Levi Simon's soldiers speaking Spanish and Hercule says Fussar "called in the navy from Cuba" (gsw 10853); it never calls the land troops Cuban. Fiche says "Fussar's soldiers". | No change (fiche wording is the safe one). |
| 5 | Paradise infobox `location = Aguasdulces`; EN: "they launch an assault on Aguasdulces to rescue the captain" | WIKI-ONLY (mission page infobox; the transcript names no place). Our intro (L2) and the captain entry (L73) already say "attack on Aguasdulces", but the Biography (L35) never places the blue building there. | A: add "at Aguasdulces, according to the mission page" in L35 so the intro and L73 are backed by the Biography. |
| 6 | EN char page: La Capilla = "a church turned rebel outpost"; La Capilla page: "an outpost for Fusar's soldiers", where Arthur is held prisoner in "Savagery Unleashed"; Welcome mission page: "La Capilla, the rebels' camp" | WIKI-ONLY, self-contradictory (FIX_RULES 6). Fiche L29 gives only the mission page's "rebels' camp". | A (L29): either drop the label ("near La Capilla") or give both wiki descriptions, attributed, in that one place. |
| 7 | Guarma Rebels page: after the warship sinks, "the gang members regroup at Manicato"; Paradise infobox `start = Manicato` | WIKI-ONLY (location data). | A (L34), optional: one clause, "at Manicato, where the next mission starts according to the wiki". Low priority. |
| 8 | El Nido page: "it became an outpost for rebels loyal to Hercule Fontaine" | WIKI-ONLY. Fiche L22 names El Nido only as the wiki's name for the gun cache. | A (L22), optional: extend the existing attribution ("which the Red Dead Wiki names El Nido and describes as an outpost of his rebels"). |
| 9 | Guarma Rebels page: the warship arrives "at the mouth of Bahía de la Paz" | WIKI-ONLY (map name). | Optional, A (L31), one attributed clause. Low priority. |
| 10 | Mission page Welcome: "Hercule also points out ... Cinco Torres, a hideout used by him and the rebels" | CONFIRMED (gsw 10574: "That old fort, Cinco Torres… my men and I use that as a hideout when we are here"). Told in A Origins (L22) but not at its moment in the narrative. | No add needed (A Origins owns it); see duplicate D2. |
| 11 | Transcript line (not on the wiki page, listed in B docstring for C): "The workers are somewhere in the jungle. Hopefully we can get to them before Fussar does." | CONFIRMED (gsw 10582). | C: candidate replacement quote (see section 3, Q-duplicates). |

Section 1 count: 11 rows (4 "do not add / no change", 3 recommended adds in A [#5, #6, and #8 optional], 3 optional/low, 1 quote candidate).

## 2. Places where the fiche differs from the wiki

| # | Wiki says | Fiche says | Who is right, and the deciding source |
|---|---|---|---|
| D1 | EN lead: Hercule gets them the boat "after defeating Alberto Fussar in 'Hell Hath No Fury'" | Fussar dies in "Paradise Mercifully Departed" (L36) | Fiche. Transcript gsw 10992-10999 and Paradise mission page (Deaths: Fussar killed by Arthur). The warship sinks in Hell Hath; Fussar is not there. |
| D2 | EN: "Arthur manages to unlock the shackles on the gang, and arms himself" | Arthur takes a gun from a dead guard and kills the soldiers while the others free themselves (L27) | Fiche. Welcome mission page ("Arthur is able to steal one of their guns ... while the others free themselves"); transcript stage note "he jumps to the corpse and takes the revolver", Micah: "You gotta crank it, Bill!" (gsw 10527-10531). **Cross-fiche: arthur_D.py L203/204 says "Arthur frees the gang's shackles" / "Arthur défait les fers du gang": fix.** |
| D3 | EN: "He and the gang fall back to an old tower, which has been stocked with Bolt Action Rifles" | "an old building where he has guns hidden" (L27) | Fiche. Mission page and El Nido page: "old building"; transcript: "an old ruined castle", "I have some guns stashed here" (gsw 10551-10552). "Tower" is unsupported. **Cross-fiche: arthur_D L203/204 "leads them to a tower" / "les conduit à une tour": change to "an old building (El Nido)".** The Bolt Action Rifle detail is not in the transcript (it shows "rifles and revolvers hidden in boxes"); fiche's "rifles from the crates" is right. |
| D4 | EN: "Hercule then spots reinforcements approaching" | "When enemy reinforcements appear, Hercule tells everyone to follow him" (L27) | Fiche. Dutch says "Damn… reinforcements."; Hercule (Stranger 2): "We need to get out of here" (gsw 10535-10537). |
| D5 | La Capilla: "church turned rebel outpost" (char page) vs "outpost for Fusar's soldiers" (La Capilla page) vs "the rebels' camp" (Welcome page) | Only "rebels' camp" (L29) | Wiki contradicts itself; nothing in the transcript names the rest place ("I know somewhere you men can rest", gsw 10574). Apply FIX_RULES 6 (section 1 #6). arthur_D ("rebel outpost of La Capilla") and dutch_B ("La Capilla, the rebels' camp") also label it; optional harmonisation. |
| D6 | Mission page Welcome: Hercule asks help "freeing a group of slaves captured by Fussar's men while trying to escape" | Help Leon with the escaped workers whom Fussar's men are hunting (L28-L29) | Fiche. Transcript: "A group escaped yesterday into the jungle" (Leon), "Now Fussar's men are out hunting them down", "Help Leon with that group of escaped workers" (gsw 10573-10576). They are caught only later (Savagery Unleashed). arthur_C / dutch_B summarise the mission page ("captured", "taken"); minor, optional. |
| D7 | Mission page Hell Hath: help him kill Fussar "before he sends word about them to America" | "If they can silence Fussar, he can get them away before anyone has time to arrive from America" (L7, L31) | Fiche. Transcript gsw 10851; HOUSE_FACTS (Fussar) and FIX_RULES 1. |
| D8 | Transcript stage note Hell Hath: "[They pull up a machine gun.]" | Arthur helps Hercule push the cannon into position (L32) | Fiche. Hercule: "I will go get the cannon ready" (gsw 10864); mission page "Arthur helps Hercule push the cannon into position". Already excluded in B docstring. |
| D9 | Mission page Hell Hath: "Arthur assigns Dutch and Hercule different positions" | Arthur gives Dutch a position; Hercule follows Arthur (L32, L59) | Fiche. Arthur: "You cover the left side." Hercule: "Guess I'm following you, Arthur!" (gsw 10902-10904). |
| D10 | Paradise mission page and FR wiki: Fussar "mans a Gatling Gun" / "s'arme d'une Gatling" | Fussar loads a cannon and opens fire (L36) | Fiche. Transcript stage note "[Fussar loads the cannon.]" (gsw 10997); HOUSE_FACTS; FIX_RULES 1. |
| D11 | EN: "Hercule and Dutch draw Fussar's fire, allowing Arthur to access a cannon" | Told once, attributed to the wiki (L36) | Not in the transcript; fiche follows FIX_RULES 1 (A only, attributed). OK. |
| D12 | Transcript stage note: Arthur "tosses the rifle ... into the captain's hands" | Arthur kicks the rifle to the captain (L35) | FIX_RULES 1 / HOUSE_FACTS: "kicks" (mission page). Keep fiche. |
| D13 | EN lead: "Dutch and Arthur thank him as they leave for America" | Dutch thanks him at the dock (L37); Arthur thanks him earlier for the rescue (L27) | Fiche. At the dock only Dutch speaks: "Good. Thank you." (gsw 11007). Arthur's thanks are in Welcome: "Thanks for getting us out of there" (gsw 10556). **Cross-fiche: arthur_D L203/204 "Dutch and Arthur thank him" / "Dutch et Arthur le remercient": rewrite (Dutch thanks him at the dock; Arthur had thanked him for the rescue in "Welcome to the New World").** |
| D14 | EN: Micah reports gun batteries "around the island" | "gun positions cover the harbor" (L34) | Transcript: "Got us surrounded with gun positions… so when we try to sail out… he's gonna blow holes in us" (gsw 10939). "Cover the harbor" is a slight inference; A may reword to "surround them, so that any boat trying to sail out would be shot to pieces". Minor. |
| D15 | Infobox and FR: nationality "Haitian" | Not stated in game; "back to Haiti" line quoted; Haitian attributed to the wiki (L13, L23) | Fiche (FIX_RULES 3). **Cross-fiche still open: fussar_B L114/115 "The Haitian smuggler" / "Ce contrebandier haïtien" and arthur_D L203/204 "The Haitian rebel" / "Le rebelle haïtien": drop "Haitian" or attribute (EN+FR).** |
| D16 | Wiki: Hercule's later fate unknown; FR "statut : vivant" | Alive when the gang leaves; fate not shown (L12, L39) | Consistent; FIX_RULES 2. |

Section 2 count: 16 rows; 0 cases where the wiki is right against the fiche; 3 cross-fiche fixes required (arthur_D: shackles, tower, "Dutch and Arthur thank him", plus "Haitian"; fussar_B: "Haitian"), 2 optional wording tweaks (D5 labels in other fiches, D14).

## 3. Duplicates inside the fiche (OWNERSHIP.md, FIX_RULES 5)

### Quotes quoted twice (rule: each line in exactly ONE place; B owns these per hercule_B docstring)
| # | Line | Occurrences | Keep | Cut |
|---|---|---|---|---|
| Q1 | "It's not my island." | L58 (B Arthur), L98 (C Quotes) | L58 | C L98 |
| Q2 | "I don't see you have any choice. I am the only one who can arrange a boat for you. But... I need something in return." | L45 (B own words), L100 (C) | L45 | C L100 |
| Q3 | "I am! What do you want me to do? We are trapped up here!" | L63 (B Bill), L106 (C) | L63 | C L106 |
| Q4 | "We'll be like you. We'll disappear probably... back to Haiti..." | L48 (B own words), L112 (C) | L48 | C L112 |
| Q5 | "Almost certainly, but he's the best chance..." | L55 (B Dutch, "Almost certainly"), L115-116 (C, full line) | B L55 | C L115-116 |
| Q6 | "He's using us!" | L61 (B Micah), L119 (C) | L61 | C L119 |
| Q7 | "Hercule... it was a great pleasure to make your acquaintance." | L56 (B Dutch), L121 (C) | L56 | C L121 |
| Q8 | "this Hercule feller" | L50 (B Names) and L58 (B Arthur, full line) | L58 (Arthur) | L50: no quotation marks; e.g. "Arthur refers to him by his first name when he asks Dutch whether Hercule is using them (see Relationships)." |

Replacement quotes for C (verified in gsw, listed as "left to C" in the B docstring): "Okay. Well, Fussar will be desperate to find you. We must be very careful." (10567); "The workers are somewhere in the jungle. Hopefully we can get to them before Fussar does." (10582); "But, if we can silence him… then I can help you escape before anyone has time… to get here from America. That way, we all get what we want." (10851); "So now we have a real problem. This must be the boat he called in from Cuba." (10857); "Two of us must go and use the cannon." (10908); "Oh, they'll be back… but, I found a boat for you… and he should be arriving on the dock anytime now." (10929); "Gentlemen, goodbye." (10584). Keep the C "About Hercule" Baptiste line (L117), which B only paraphrases.

### Facts told twice
| # | Fact | Occurrences | Keep | Action |
|---|---|---|---|---|
| F1 | Smuggler, not from Guarma, moves goods behind Fussar's back | L5 (key facts), L22 (A Origins), L41 (B Personality), L44 (B quote), L67 (B Fussar), L78 (B Smuggling) | L22 (A, paraphrase) + L44 (quote) + L5 (key facts) | Cut from L41 ("He says plainly that he is not from Guarma..."), L67 ("Hercule smuggles goods behind his back"), L78 first sentence (point to Biography). |
| F2 | Cinco Torres = hideout of him and his men | L5, L15 (grid), L22 (A), L78 (B) | L22 + grid | Cut from L78. |
| F3 | Deal: boat in return for help with Leon's workers | L6, L29 (A), L41 (B), L45 (quote), L55 (B Dutch), L69 (B Leon), L78 (B "only one who can arrange a boat") | L29 (A) + L45 quote | L41 already says "see Biography" but retells; trim to pointer. L55, L69, L78: one clause or cut. |
| F4 | Cave below the cliffs leading to Fussar's compound | L29 (A), L65 (B Javier), L78 (B Smuggling), L94 (C table) | L29 + table | Cut from L78; L65 to a pointer. |
| F5 | Gun cache in the old building, castaways arm themselves | L22 (A Origins), L27 (A), L78 (B), L88 (table) | L27 (+ El Nido attribution once, L22) | Cut retelling in L78. |
| F6 | Mission fails if the player attacks or kills Hercule or Leon | L81 (B Fighting), L133 (C Trivia) | L81 (gameplay = B Skills) | Cut Trivia L133 (Trivia keeps only facts found nowhere else). |
| F7 | Hercule runs fast back to the roof, follow him on the mini-map | L81 (B), L137 (C Trivia) | L81 | Cut Trivia L137. |
| F8 | French lines (rebel calls him in French, swears, "En allez", "connards") | L83 (B Languages), L134 (C Trivia), L96 (C Quotes note) | L83 | Cut Trivia L134; L96 note may stay (it explains a quoting choice, not a fact) or shorten to "French lines: see Languages". |
| F9 | Cinco Torres combat details: "take the shotgun", shoots soldier heading for Dutch, reloads cannon while Arthur aims | L32-33 (A), L59 (B Arthur), L80 (B Fighting), L89 (table), L108 (C quote) | L32-33 (A) + L108 quote + table line | L80: cut the retelling, point to Biography. L59: one clause ("they fight side by side at Cinco Torres, see Biography"). |
| F10 | Leon wants the people to rise but most are too afraid | L28 (A), L69 (B Leon) | L28 | L69: cut that clause. |
| F11 | Dutch introduces Micah, Bill, Arthur; asks if Hercule can be trusted | L28-29 (A), L55 (B Dutch) | A | L55: pointer clause. |
| F12 | Baptiste: works with Hercule, boat lined up at Cinco Torres, money ($450 per wiki) | L30 (A), L71 (B Baptiste), L93 (table), L117 (C quote) | L71 for "I work with Hercule" and the $450 attribution; L117 quote; table line | A L30: drop the $450 clause (told in L71). |
| F13 | The ship's captain found by Hercule, seized by Fussar, freed | L33-35 (A), L73 (B captain) | A | L73: shorten to one clause + "see Biography". |
| F14 | "Fussar can always pay for more men" | L33 (A), L42 (B Personality), L46 (B quote) | L46 quote; A paraphrase may stay | Cut L42 "He knows that killing soldiers will not end Fussar's hold on the island" (repeat + mild interpretation). |
| F15 | Gone by morning / back to Haiti | L9, L13, L23, L37 (A), L42 (B Personality), L48 (quote) | L37 (A) + L48 quote + grid L13 | Cut L42 last sentence ("he does not claim the island for the rebels..."), which also reads as interpretation. |
| F16 | Levi Simon's "Haitian pirates" | L23 (A Origins, paraphrase), L75 (B Levi, quoted) | L75 (quote) | A L23: one clause pointing to it, or keep A and drop it from L75; not both. |
| F17 | Leadership of the rebels per the wiki | L22 ("runs his rebel movement from Cinco Torres"), L23 ("lists Hercule and Leon as the two leaders"), L69 ("rebel faction led by Hercule") | L22-23 (A) | L69: cut the wiki attribution. |
| F18 | Rockstar's Sept 2018 descriptions do not include him | L41 (B Personality), L131 (C Other media) | L41 (B owns official descriptions) | C L131: cut that sentence. |
| F19 | "Appears only in Red Dead Redemption 2" | L18 (grid), L125 (D Casting), L131 (C) | grid + L131 | D L125: drop "appears only in Red Dead Redemption 2 (2018), in chapter 5". |
| F20 | Missions in which he is mentioned | L30 ("does not appear in the next two missions, but both refer to him"), L85 ("Two more Guarma missions mention him"), L91-94 (table) | L30 + table | L85 last sentence can go (the table heading says it). Minor. |

Section 3 count: 8 quote duplicates + 20 fact duplicates = 28.

## 4. Summary for the correctors (EN + FR each time)

**Part A (Biography)**
1. L35: place the captain rescue at Aguasdulces, attributed to the mission page (backs L2 and L73).
2. L29: La Capilla, apply FIX_RULES 6 (no label, or both wiki descriptions attributed in this one place).
3. L34: optional "regroup at Manicato" (wiki); L34 reword "gun positions cover the harbor" -> they surround the gang so any boat sailing out would be shot to pieces (gsw 10939).
4. L22: optional, El Nido "an outpost of his rebels" inside the existing attribution.
5. L30: drop the "$450 according to the Red Dead Wiki" clause (kept in B Baptiste).
6. L23 or B L75: keep Levi's "Haitian pirates" in one place only (F16).
7. Do NOT add: "Hercule celebrates a great victory", FR "problématique / envoyé sur Guarma", FR "ancien esclave", "Cuban troops" label.

**Part B (Personality, Names, Appearance, Smuggling and fighting, Relationships)**
8. L41: remove the "not from Guarma / behind Fussar's back" sentence and the terms-of-help retelling (F1, F3).
9. L42: remove "He knows that killing soldiers..." and "Once Fussar is dead, he does not claim the island..." (F14, F15; both lean interpretive).
10. L50: unquote "this Hercule feller" (quoted in L58) (Q8).
11. L55, L59, L65, L67, L69, L73: reduce to pointer clauses (F3, F4, F9, F10, F11, F13, F1, F17).
12. L78: cut the retelling of not-from-here, Cinco Torres hideout, gun cache, cave (F1, F2, F4, F5); keep the wiki occupations and the boat-arranging role as one clause.
13. L80: cut the Cinco Torres combat retelling, point to Biography (F9).

**Part C (Missions, Quotes, Trivia, Other media)**
14. Quotes: remove L98, L100, L106, L112, L115-116, L119, L121 (Q1-Q7); replace with lines from the verified list in section 3 (e.g. "Okay. Well, Fussar will be desperate...", "Hopefully we can get to them before Fussar does.", "But, if we can silence him...", "So now we have a real problem...", "Two of us must go and use the cannon.", "Oh, they'll be back... I found a boat for you...", "Gentlemen, goodbye.").
15. Trivia: cut L133 (mission fail), L134 (French lines), L137 (fast run) (F6, F7, F8).
16. Other media L131: cut the THR sentence (F18). Missions L85: optional cut of the last sentence (F20).

**Part D (base, Development, Reception)**
17. L125: drop "appears only in Red Dead Redemption 2 (2018), in chapter 5" (F19). No other change.

**Cross-fiche (fixer, EN + FR, HTML regenerated, note in CLAUDE.md)**
18. arthur_D.py L203/204 (Hercule relation): "The Haitian rebel" -> drop or attribute (FIX_RULES 3); "Arthur frees the gang's shackles" -> Arthur takes a dead guard's gun while the others free themselves; "leads them to a tower" -> an old building (El Nido); "Dutch and Arthur thank him" -> Dutch thanks him at the dock (Arthur had thanked him for the rescue in "Welcome to the New World").
19. fussar_B.py L114/115: "The Haitian smuggler" / "Ce contrebandier haïtien" -> drop "Haitian" or attribute.
20. Optional: dutch_B ("rescue workers taken by Fussar's men"; "La Capilla, the rebels' camp") and arthur_C ("workers captured while trying to escape"): the transcript says the workers had escaped and were being hunted when Hercule made the deal.
