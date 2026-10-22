# Coverage report: Eagle Flies (v3, medium tier)

Compared: Red Dead Wiki EN (`en.txt`, 2,069 words) and FR (`fr.txt`) against `eagle_full_en.txt` (Lnn).
`python3 scripts/coverage.py eagle-flies "Eagle Flies"`: our EN 7,046 words (340 % of the wiki EN), FR 8,390 words.
EN sections: intro/facts 421, Biography 2,512, Personality 601, Relationships 1,349, Raids/weapons/horses 344,
Missions 425, Quotes 614, Development 238, Reception 227, Other media 87, Trivia 188, Gallery 40.

Sources used to decide: fan transcript `fc/gsw.txt` (gsw), mission pages in `scripts/v3/work/_m/`,
`scripts/v3/sources/Camp_Events.txt`, `HOUSE_FACTS.md`, `FIX_RULES.md`.

Overall: every non-speculative section of the wiki (Background, Colter, Saint Denis, Beaver Hollow, Legacy, mission
list, trivia on grave and horse, infobox weapons/mounts/voice) is covered. Gaps are small transcript details; the
main work for the correctors is in sections 2 and 3.

## 1. Wiki facts missing from the fiche

| # | Wiki excerpt | Status | Recommendation |
|---|---|---|---|
| 1 | "they quickly knock out the guards, drop the anchor" (A Rage Unleashed) | CONFIRMED in a corrected form: gsw l. 12267-12270, Dutch: "Arthur, deal with that anchor"; Arthur: "You think I have the first idea how this anchor works?"; Dutch: "Just blow it up then"; [Arthur blows up the mechanism with dynamite] | A, L37: one clause before "Dutch crashes the boat": Arthur blows up the anchor mechanism with dynamite on Dutch's order. Paraphrase, no quote. |
| 2 | "he rides into the Beaver Hollow with Charles" | CONFIRMED (in part): gsw l. 12210, Charles: "Pardon me for interrupting. I've brought a friend, Arthur." Escort by Karen and Javier = mission page `A_Rage_Unleashed.txt` l. 25 + house fact | A, L36: keep Karen and Javier, add that Charles presents him to Arthur, then Arthur introduces him to Dutch (FIX_RULES 2: both, once). |
| 3 | Wiki trivia: Favours "violated the treaty that they signed" | CONFIRMED (the treaty, not who broke it): gsw l. 9559, Evelyn Miller on the new removal: "Clearly contravening the peace treaty signed three years ago." | A, L29: one sentence after "his people are to be moved again": Miller says this breaks the peace treaty signed three years earlier. Do NOT say Favours violated it (that is the wiki's reading). |
| 4 | Arthur "calling him a 'silly fool'" (My Last Boy) | CONFIRMED: gsw l. 13249 "Ah, you, you silly fool." | C, Quotes "About Eagle Flies": add as Arthur's line (My Last Boy, after Favours shoots him). A L45 keeps the paraphrase "scolds". |
| 5 | "Arthur blows down a weak spot in the wall" (The King's Son) | CONFIRMED in a corrected form: gsw l. ~13060 "[He makes a new hole in the wall with a cannon.]" and "let's use this thing" | A, L41: "Arthur blows a new breach with a cannon". |
| 6 | "during which heavy losses were sustained" (Personality) | CONFIRMED: gsw l. 13156, Charles on arrival: "It's a massacre." Also "Pump Jacks Sit Silent" (already in A L48) | A, L44: optional clause: on arrival Charles calls the scene a massacre. |
| 7 | "he dies in his father's arms shortly afterwards" | Already attributed to the wiki (L46). The transcript stage direction (gsw l. 13300) says "His father takes him by the hand however... Eagle Flies dies." | A, L46: optional, state the transcript fact (Rains Fall takes his hand) and keep the wiki's "in his father's arms" attributed (FIX_RULES 3). |
| 8 | Legacy: the Wapiti reduced to a "bunch of families" by 1907 | WIKI-ONLY (quote on the wiki's Rains Fall page, `_m/Rains_Fall.txt` l. 74; no transcript of the Annesburg encounter) | A, L49: optional, one attributed clause ("according to the wiki, he tells John his people are now just a bunch of families, living in Canada"). Belongs mainly to the Rains Fall fiche; skip if A is already long. |
| 9 | Eagle Flies kills "the three soldiers" about to kill Arthur | WIKI-ONLY number (mission page and gsw give no number) | Do not add. |
| 10 | Wiki trivia: the Army stole "their medicine for smallpox" | SPECULATIVE / unsupported: gsw l. 12240 says only "withhold medicine and supplies"; no "smallpox" anywhere in gsw | Do not add. |
| 11 | Infobox: affiliation "Van der Linde gang" | Wiki categorisation; he is never a member, only an ally | Do not add (facts grid "Allies" is correct). |
| 12 | "is a major character" | Wiki editorial label | Do not add. |
| 13 | Trivia: comparison with Nastas (four bullets) | SPECULATIVE / interpretation | Do not add. |
| 14 | Legacy: Dutch's 1911 Native gang "echoes" his use of Eagle Flies | Interpretation (the link) | Do not add. |
| 15 | Legacy/Personality: Arthur "began to see Dutch had been taking advantage of him all those years"; Dutch's abandonment "indirectly killed" him; he gained "honor and glory in death"; "prideful", "nihilistically" | Interpretation | Do not add. The factual anchors (Arthur's "Another angry fool he used", "Dutch just stood and watched") are already in. |

## 2. Places where the fiche differs from the wiki (or from its own sources)

1. **Arrival at Beaver Hollow (A L36).** Wiki EN: he rides in with Charles. Mission page: escorted by Karen and Javier.
   Transcript gsw l. 12210: Charles presents him ("I've brought a friend, Arthur."). Both are right; the fiche drops
   Charles's role. Fix A L36 (FIX_RULES 2).
2. **The boat (A L37).** Wiki EN: they "drop the anchor". Transcript gsw l. 12267-12276: Arthur blows up the anchor
   mechanism with dynamite, Dutch then loses control and runs the boat into the rocks. The fiche's "Dutch crashes the
   boat into the rocks" is right but incomplete; the wiki's "drop the anchor" is wrong. Add item 1 of section 1.
3. **Does Paytah board the boat? (L6, B L76, C table L107).** Wiki EN: "the four men" (Dutch, Arthur, Charles, Eagle
   Flies) board; wiki page of Paytah says he boards. Transcript gsw l. 12257: as they come up to the steamboat,
   "Paytah: Good luck." The knock-outs are done by Arthur and Charles ([Arthur and Charles sneak around the steamboat
   knocking out the guards]). The transcript does not support Paytah boarding. Fix: L6 (D) "with Dutch, Arthur and
   Charles, helped by Paytah's canoes"; B L76 drop "and boards the boat with him" (keep "waits with the canoes");
   C L107 "with Dutch, Arthur and Charles; Paytah brings the canoes".
4. **Wall at Fort Wallace (A L41).** Wiki: "blows down a weak spot". Transcript: the old hole has been fixed, Arthur
   makes a new hole with a cannon. Fiche right on the repaired hole; add "with a cannon".
5. **Canoe escape (A L41).** Wiki EN: Charles puts Eagle Flies in a canoe "while Arthur covers them". Mission objectives
   ("Get in the canoe", "Follow Charles down the river") and gsw ("get in the other canoe ... Arthur"): all three go
   down the river. Fiche is right; nothing to change.
6. **Payment at the end of American Fathers II (A L31).** Wiki EN: he hopes the papers help them "with lobbying the
   army". gsw l. 9656: "I don't know what I hope... maybe these will be of some use." No lobbying. Fiche is right.
7. **Who helps whom up after Favours's shot (A L45).** Wiki EN: Arthur kills Favours "before helping Eagle Flies up".
   Mission page `My_Last_Boy.txt` l. 36: Eagle Flies "begins to help Arthur up" and is shot; afterwards Arthur helps
   him out. gsw l. 13248-13250 agrees. Fiche follows the mission page; correct.
8. **Paytah's reply on the ride (A L45).** Fiche: "Paytah tells him to save his breath" as the answer to the bodies
   line. gsw l. 13258: "Our men... we must go back for the bodies..." / Paytah: "We will. Save your strength." The
   "save your breath" line comes later, when Eagle Flies calls his name (l. 13290). Fix A L45: "Paytah promises they
   will and tells him to save his strength." (B L76 quotes "save your breath" correctly in its own context.)
9. **Mission of "Another angry fool he used" (B L68 vs A L46, C L116/L163).** B says "Our Best Selves"; A and C say the
   "Red Dead Redemption" mission. The wiki's `Red_Dead_Redemption_mission_dialogues.txt` l. 88 and l. 106 place the
   line in "Red Dead Redemption" (two variants, the second adds John). gsw has no heading between "Our Best Selves"
   (l. 13314) and the line (l. 13489), which caused B's error. Fix B L68 to "Red Dead Redemption" (and B's source
   docstring line 20).
10. **Reform-school camp scene (A L31 vs B L70).** Camp Events l. 350: Charles was tasked by Eagle Flies "to rescue some
    Native children from a reform school". A matches; B L70 says "free members of the tribe being sent to a reform
    school". Fix B wording to "Native children" (and see duplicate D3).
11. **Explosion at the refinery (C table L106).** Mission page says Eagle Flies set off the blast; the transcript only
    has [An oil rig suddenly explodes]. A L31 and B L95 attribute it; the Missions table states it as fact. Fix C L106:
    "covers his escape (the wiki credits him with the oil well explosion)" or drop the explosion from the row
    (FIX_RULES 5).
12. **Appointment in Saint Denis (FR wiki).** FR wiki: Rains Fall is trying to be received by Colonel Favours. gsw
    l. 9580-9589: the appointment is with "the senator" (a councillor's clerk comes out). Fiche (A L29, B L82) is right.
13. **Grave (A L48).** EN wiki and `Donner_Falls.txt` l. 18: west side of the falls; FR wiki: east. Fiche gives both,
    attributed, once (FIX_RULES 4). Correct.
14. **Death of brother and mother (A L23).** Wiki: killed by the U.S. Army. gsw l. 13112 (Rains Fall): the first-born
    "had his head smashed by a drunken soldier", "My wife had her throat slit" (no killer named). Fiche gives the
    transcript and attributes the wiki. Correct.
15. **Capture in Favored Sons (A L40).** Wiki EN: captured while rescuing Paytah. Mission page: Eagle Flies goes to help
    the wounded Paytah, Arthur and Dutch flee, the capture is not shown; Dutch "assumes" capture. Fiche attributes;
    "Paytah got away" is from the wiki's Paytah page (`_m/Paytah.txt` l. 19), so "The Red Dead Wiki says" holds.
    Correct.
16. **Hospitality of the reservation (C Trivia L181).** `Wapiti_Indian_Reservation.txt` l. 31: inhabitants may be
    "openly hostile ... although they will never attack Arthur". "Hostile" alone over-reads it; suggest "may tell him
    to leave at first".

## 3. Duplicates inside the fiche

Quotes (OWNERSHIP + FIX_RULES 6: a line quoted in B is not repeated in C; cut from C):

| # | Line | Occurrences | Keep |
|---|---|---|---|
| Q1 | "Told you, they're all mercenaries." | B L54, C L120 | B; cut C L120-121 |
| Q2 | "It's a waste of our time and his." | B L82 (Miller), C L122 | B; cut C L122-123 |
| Q3 | "Colonel Favours is a liar and a murderer..." | B L56, C L131 | B; cut C L131-132 |
| Q4 | "Father need not know anything... he'd rather live in ignorance." | B L64 (Rains Fall), C L133; A L37 paraphrase | B; cut C L133-134 |
| Q5 | "Sure... I enjoy being tortured... clears the mind." | B L57, C L139 | B; cut C |
| Q6 | "They'll pay for this. They'll wish they killed me..." | B L57, C L141 | B; cut C |
| Q7 | "Where would we go?" | B L57, C L143 | B; cut C |
| Q8 | "Any men we see... we must save them." | B L57, C L149 | B; cut C |
| Q9 | "Our men... we must go back for the bodies..." | B L57, C L153; A L45 paraphrase | B; cut C |
| Q10 | "He's very brave... very angry." | B L54 (Personality, with "He's me."), C L156 | B; cut C L156-157 |
| Q11 | "He saw Eagle Flies burned hot, and he fanned the flames." | B L70 (Charles), C L158 | B; cut C L158-159 |
| Q12 | "Fearless, always has been." | B L76 (Paytah), C L160 | B; cut C L160-161 |
| Q13 | "Another angry fool he used..." | B L68 (Arthur), C L162; A L46 paraphrase | B (with the mission fixed, section 2 #9); cut C L162-163 |
| Q14 | "Father has confused wisdom with weakness" | B L56 (In his own words, full line), B L64 (Rains Fall, partial); A L36 paraphrase | B L56; B L64 paraphrase without quotes |
| Q15 | "He's a vile man..." | B L56 quote; A L37 and B L78 paraphrase | FIX_RULES 7: cut from B L56 first (keep A L37), fix the Favours pointer in B L78 ("see In his own words" no longer valid: point to Biography) |

After these cuts, C's intro sentence (L118, "Lines already quoted under Personality and Relationships do not appear
again here") becomes true; today it is false. C keeps L124, L126, L128, L135, L137, L145, L147, L151 (+ "silly fool"
if added). Consider moving one cut line back to C instead of B where B is overloaded (OWNERSHIP prefers C for mission
lines), but never both.

Facts:

| # | Fact | Occurrences | Keep |
|---|---|---|---|
| D1 | Fail conditions (attack, kill, abandon, let him die) | B L95, C Trivia L176 | B L95 (gameplay = Skills); cut Trivia L176 (move "killed by the guards" detail to B if wanted) |
| D2 | Sadie pulls the soldier off him if Arthur does not | B L84 (Sadie), C Trivia L178 | B; cut Trivia L178 |
| D3 | Charles's reform-school camp scene (Camp Events) | A L31, B L70, D L168 (cut content, pointer) | B L70 (camp scene = relationship); A L31 cut to nothing or a pointer; D keeps its pointer |
| D4 | Refinery plan (Danbury, office window, Leland report, fence or wagon, "call for me") | A L30, B L95 | A; B L95 one clause + pointer |
| D5 | Wiki: he set off the explosion | A L31, B L95, C L106 | A (attributed); B pointer; C hedged (section 2 #11) |
| D6 | Ambush role (lookout, spotter, signal, "wait for my lead", search the bodies) | A L39, B L96 | A; B L96 trim to a pointer clause |
| D7 | Escape on Taima behind Charles | A L41, B L98, C table L109 | A + table line; cut from B L98 |
| D8 | Asks for a gun in the canoe | A L41, B L54 (Personality), B L98 | A; cut from B L98 and B L54 |
| D9 | "Even his father may have to fight" | A L42, B L65 | A; cut from B L65 |
| D10 | Rains Fall: "easily led", "great disappointment", "glory in death", "too much of a mind of his own" | A L38, B L53 (Personality quotes), B L65 | A L38 narrative + B L53 quotes; cut the repeat in B L65 |
| D11 | Arthur warns Rains Fall that Dutch does not have his son's interests at heart | A L38, B L67 | A; cut from B L67 (pointer already there) |
| D12 | Charles told Rains Fall he would not fight over some horses | A L36 (paraphrase), B L70 (quote) | B quote; A can keep a short clause (needed for the scene) without detail |
| D13 | "a great favor" (pretending to be mercenaries) | A L36, B L54 (Personality), B L67 (quote) | B L67 quote + A paraphrase; cut from Personality L54 |
| D14 | Waste of time / senator appointment | A L29, B L53 (Personality), B L82 | A + B L82; cut from Personality L53 |
| D15 | Bronte mocks them from the balcony | A L28, B L92 | A; B L92 shorten to one clause, keep "the redskins" quote only there |
| D16 | Rockstar's 6 Sep 2018 descriptions do not include him | B L53, C Other media L174 | B; cut from C L174 |
| D17 | Appears only in RDR2 / no other game | C L100 (Missions intro), C L174 | C L174; cut from L100 |

## 4. Summary for the correctors (by part)

**A (Biography)**
- L36: add Charles presenting him ("I've brought a friend") while Karen and Javier escort him; shorten the Charles/horses clause (D12).
- L37: add that Arthur blows up the anchor mechanism with dynamite before Dutch runs the boat onto the rocks.
- L29: add Miller's remark that the removal breaks the peace treaty signed three years earlier (no blame on Favours).
- L41: "with a cannon".
- L45: Paytah answers "We will" and tells him to save his strength (not "save his breath").
- L31: drop the camp-scene sentence (owned by B Charles, D3).
- Optional: L44 Charles calls the scene a massacre; L46 Rains Fall takes his hand (transcript) beside the attributed "in his father's arms"; L49 "bunch of families" (wiki-only, attributed).

**B (Personality, Relationships, Skills)**
- Personality to ~450 words (FIX_RULES 7): drop "He's a vile man..." from L56 first; cut the repeats in L53 (waste of time, D14) and L54 (great favor, gun: D8, D13).
- L64: paraphrase "confused wisdom with weakness" (Q14); L65: cut repeats D9, D10.
- L67: cut the Rains Fall warning repeat (D11). L68: mission is "Red Dead Redemption", not "Our Best Selves" (also the docstring).
- L70: "Native children" instead of "members of the tribe" (Camp Events).
- L76: Paytah does not board the boat (keep "waits with the canoes").
- L78: fix the pointer after the "vile man" cut.
- L92: shorten Bronte (D15).
- L95-L98: trim refinery plan, explosion, ambush roles, Taima, gun to pointers (D4-D8); keep fail conditions here (D1).

**C (Missions, Quotes, Trivia, Other media)**
- Quotes: cut L120, L122, L131, L133, L139, L141, L143, L149, L153, L156, L158, L160, L162 (Q1-Q13); add Arthur's "Ah, you, you silly fool." in About Eagle Flies.
- Table L106: hedge the explosion (wiki) or remove it. L107: Paytah brings the canoes, the boarding is Dutch, Arthur, Charles and Eagle Flies.
- Trivia: cut L176 (D1) and L178 (D2); L181 soften "hostile" to the page's wording.
- L100: drop "He appears in no other game of the series" (D17). L174: drop the Rockstar-descriptions sentence (D16).

**D (base, Development, Reception)**
- L6 (key facts): "with Dutch, Arthur and Charles", Paytah only as the man with the canoes.
- Nothing else; Development and Reception have no overlap with B/C beyond D's pointer to the camp scene.

Cross-fiche (report to the lead, do not edit): `charles_B.py` l. 152 says Paytah "boards the army boat with Eagle Flies
in "A Rage Unleashed"" (follows the wiki's Paytah page, contradicted by gsw l. 12257 "Paytah: Good luck."). `charles_A.py`
l. 80 and `arthur_C.py` l. 95 say "they"/"the group" board after meeting Paytah, ambiguous but acceptable. Settle one
wording for HOUSE_FACTS. Note also `charles_A.py` l. 80: Dutch crashes the boat "into the Van Horn lighthouse" (the
Eagle Flies fiche says "rocks", gsw: [The steamboat runs into the rocks.]).
