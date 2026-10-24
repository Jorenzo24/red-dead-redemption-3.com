# Fact-check report 2: RDR2 Chapter 1 (Colter) story guide, chunk L65-L132

## Sources used
- Transcripts: `_m/Old_Friends_dialogues.txt`, `_m/Who_the_Hell_is_Leviticus_Cornwall_dialogues.txt`, `_m/Eastward_Bound_dialogues.txt`, `story-ch1/fc/gsw.txt` (lines 2597, 2768, 3222-3235, 3298-3426, 9554).
- Mission pages: `_m/Old_Friends.txt`, `_m/Who_the_Hell_is_Leviticus_Cornwall.txt`, `_m/Eastward_Bound.txt`, `_m/Outlaws_from_the_West.txt`, `_m/Enter_Pursued_by_a_Memory.txt`, `_m/The_Aftermath_of_Genesis.txt`, `_m/Missions_in_Redemption_2.txt`; `_m/Colter.txt`, `_m/Davey_Callander.txt`, `_m/Jenny_Kirk.txt`, `_m/Rains_Fall.txt`, `_m/Eagle_Flies.txt`; `sources/Camp_Events.txt` (Colter chapter).
- Fiches: `fiches/parts/lenny_A.py`, `micah_A.py`, `kieran_A.py`, `hosea_A/B/C.py`, `charles_A.py`, `javier_A.py`, `rains_A/C.py`, `eagle_C.py`, `leviticus_A.py`; `rules/HOUSE_FACTS.md`.
- Links in `story/rdr2-chapter-1-colter/index.html`: all `/characters/<slug>/` targets exist (checked against `characters/`). No em/en dashes in the chunk.

## Verified OK
- L65-66 Kieran's capture, name exchange, "couple of months", "get him hungry first", "I hate that feller", rewards, chaining into the train mission.
- L68-77 Cornwall mission: John's cabin scene (quotes verbatim), Bill sent to the water tower, Hosea's objections and quotes, the plan by car, Micah/Charles exchange, bonds line, the failed detonator, the tunnel jump, Lenny hanging and the sarcastic thanks, knife kill, the choice of who takes the guard, "but we won't mention that", the countdown, Arthur and Charles with Bill's dynamite, "We don't want to kill you...", Cornwall not on board, palace line, safe with papers, boat line, bearer bonds, "It's up to you", "we'll be moving on", honor-only choice, dynamite reward, two missable letters.
- L79-87 Eastward Bound: every quote checked verbatim; wagons, Micah and Lenny ahead, wheel, Javier's offer declined, three riders, Charles's line, Hosea on the Heartlands, Charles's family story, Valentine, yarrow/ginseng, Javier at the rock, camp speeches, Strauss, the box, Susan and the tent, title card, journal line, rewards.
- L89-98 camp events all match Camp_Events (Colter) and Colter.txt (butcher stand beside the stable, health drain).
- Table L101-107: givers, participants, locations and every Gold Medal objective match the mission pages; order matches Missions_in_Redemption_2.
- L109-112: Molly showing Dutch to his room (gsw 2768), Charles's hand, newcomers, Colm through binoculars, Cornwall absent, Davey/Jenny/Sean/Mac/Trelawny.
- L114-122 trivia: Davey's grave (Davey_Callander page: "small graveyard next to one of the houses"), Hosea's two callback lines (Outlaws page + Cornwall page; consistent with hosea_C), Dead Eye / Eagle Eye unlocks, avalanche, Winter's Tale title, Taima (thanks: gsw 3229), Train Robbed papers + journal entries, Colter in Red Dead Online.
- L124-130 key events consistent with the body and the fiches.

## Problems

1. **WRONG (misattribution)**. L75: "Lenny reads them: railroad contracts, invoices, sugar imports from the Spanish West Indies and 'Some fancy new boat he's ordered from Europe.'"
   Source: gsw.txt 3422-3423 and Who_the_Hell..._dialogues: MICAH says "Railroad contracts... invoices... blah blah blah. You got anything?"; Lenny answers "Not really. Sugar imports from the Spanish West Indies... Some fancy new boat he's ordered from Europe." Micah hands the papers to Lenny ("Least we all know you can read").
   Fix: "Micah hands the papers to Lenny, saying that at least Lenny can read, and skims railroad contracts and invoices himself. Lenny finds sugar imports from the Spanish West Indies and 'Some fancy new boat he's ordered from Europe.'" (lenny_A L88 and micah_A L45 are correct.) Same fix in FR.

2. **IMPRECISE (variant stated as fixed)**. L73: "Near the engine, the engineer comes out of the coal bin and hits Arthur with a shovel."
   Source: Who_the_Hell_is_Leviticus_Cornwall.txt, Trivia: "If Lenny is ahead of Arthur, he will get ambushed by the train conductor and Arthur will have to save him instead." The transcript shows the Arthur version only.
   Fix: keep the sentence and add: "According to the mission page, if Lenny is ahead, the engineer attacks him instead and Arthur has to save him." Same gap in **lenny_A.py L88** ("the engineer jumps out of the coal bin and attacks Arthur with a shovel"): add the variant or "in the usual version".

3. **IMPRECISE (order of events)**. L71: "As they leave the snow, Arthur says: 'Out of the snow, finally.'" is placed after the Micah/Charles/Dutch exchange about Blackwater and the bonds.
   Source: Who_the_Hell..._dialogues and gsw 3312 (Arthur's line) vs 3319 (Micah exchange): Arthur's line comes BEFORE the Micah question.
   Fix: move the sentence before "Micah keeps asking...".

4. **IMPRECISE**. L121: "Rains Fall later tells Arthur, in Saint Denis, that he saw him with the wagon train crossing the river at Cumberland Falls."
   Source: gsw 9554 (American Fathers, Saint Denis, with Evelyn Miller and Eagle Flies present): "We saw you on the wagon train… crossing the river at Cumberland Falls… and at the party, you were upstairs."
   Fix: "Rains Fall later tells Arthur in Saint Denis: 'We saw you on the wagon train… crossing the river at Cumberland Falls.'" Same "he saw him" wording in **rains_A.py L79** ("he tells Arthur that he saw him with the wagon train") and **rains_C.py L58** ("he saw the wagon train cross the river"): change to "we saw you" / "his people saw".

5. **IMPRECISE**. L81: "After a stream crossing, a wheel comes off Arthur and Hosea's wagon."
   Source: Eastward_Bound_dialogues: the wagons ride into the river next to Cumberland Falls (Dakota River), and the wheel breaks once they are over the river in the Heartlands; Rains Fall's own line (gsw 9554) names Cumberland Falls; javier_A L93 says "after a river crossing". The mission page says "stream" (and Hosea says "Get us out the stream").
   Fix: "After the wagons ford the river next to Cumberland Falls, a wheel comes off..." (also ties in with L121).

6. **IMPRECISE (interpretation)**. L65: "Dutch refuses to have him beaten, since that would only produce lies."
   Source: Old_Friends_dialogues 514-516: Arthur: "Want me to make him talk?" Dutch: "Oh no, now all we'll get is lies." "Beaten" is not said.
   Fix: "Arthur offers to make him talk; Dutch refuses, saying that all they would get is lies." Same wording in **kieran_A.py L63** ("saying that a beating would only produce lies"): align.

7. **IMPRECISE (incomplete options)**. L76: "Arthur can kill them or put them back on the train, start the engine and jump off."
   Source: dialogues: Dutch lists "Kill em', leave em' here... take 'em with you on the train"; mission page Trivia: if Arthur neglects them they run away.
   Fix: "Arthur can kill them, or put them back on the train, start the engine and jump off; according to the mission page, if he does neither, they run away."

8. **UNSUPPORTED (partly)**. L114: "Both count toward the 'Paying Respects' trophy."
   Source: Colter.txt and Davey_Callander.txt tie only Davey's grave to the trophy; Jenny_Kirk.txt says only "The player can locate her grave to pay their respects."
   Fix: "Davey's grave counts toward the 'Paying Respects' trophy, according to the wiki; Jenny's grave can also be visited to pay respects." (or source Jenny via the Paying Respects page if available).
   Also IMPRECISE: "Jenny Kirk's lies north of Colter, near Spider Gorge": Jenny_Kirk.txt says "north of Colter around the area of Spider Gorge", Colter.txt "at Spider Gorge". Acceptable; optional "in the Spider Gorge area".

9. **DUPLICATE**. L116 ("Old Friends" unlocks Dead Eye targeting, "The Aftermath of Genesis" unlocks Eagle Eye) repeats L56 (Eagle Eye) and L66 (Dead Eye targeting reward).
   Fix: delete L116 (or delete the two mentions in L56/L66 and keep the trivia line; keep one).

10. **DUPLICATE**. L85: "Hosea blames Micah for the ferry job." repeats L23 (Background), which already quotes the same line verbatim ("then Micah got you all excited about that ferry and here we are").   Fix: keep L85 short with a back-reference ("Hosea repeats his complaint about Micah's ferry job") or trim L23 to the "didn't feel right" line.

11. **DUPLICATE (minor)**. Rains Fall at the cliff is stated in L82, again in L111 (Characters) and L121 (Trivia). L111 is an acceptable recap; L82 + L121 could be merged by moving the Cumberland Falls line into L82.
   Fix: optional; move L121's content into L82 and drop L121.

12. **STYLE (filler)**. L109: "Every member of the gang at Colter makes a first appearance in the game in this chapter."
   Tautological for Chapter 1 (it is the game's first chapter); no information.
   Fix: delete, or replace with a factual line ("Chapter 1 introduces the whole gang at Colter.") if a lead sentence is wanted.

13. **COPIED (close to wiki wording, low)**.
   - L117: "an avalanche blocks the mountainside north of the ravine" vs Enter_Pursued page: "an avalanche covers much of the mountainside north of the ravine". Fix: "an avalanche closes the mountain north of the ravine where John was found, so the area can no longer be reached, according to the mission page."
   - L119: "the only mission in which a gang member's horse ... is meant to be ridden by the player" vs Outlaws page: "the only mission in the game when a gang member's horse (Taima, Charles' horse) is intended to be ridden". Fix: "Charles's mare Taima is the only gang member's horse the player rides in a mission, according to the mission page."
   - L90 / L92 follow the Camp Events sentence order closely ("Dutch feels Hosea doubts him, but Hosea reassures him that he's only worried"; "telling everyone to stay warm and that they will be off the mountains in a few days... the gang must stick together. Tilly Jackson hopes she's right"). Light rewording advised.

14. **IMPRECISE (coverage, optional)**. L87: rewards omit the gunsmith unlocks listed in the Eastward Bound infobox (Volcanic Pistol, Varmint Rifle, Springfield Rifle available in gunsmiths).
   Fix: add "and makes the Volcanic Pistol, Varmint Rifle and Springfield Rifle available at gunsmiths".

15. **Consistency note (HOUSE_FACTS)**. L118 writes "Exit Pursued by a Bruised Ego" (no comma), as the wiki and arthur_D do; `rules/HOUSE_FACTS.md` (Trelawny line) writes "Exit, Pursued by a Bruised Ego". Pick one spelling (wiki/arthur_D: no comma) and align HOUSE_FACTS.

## Errors found in our fiches (summary)
- lenny_A.py L88: engineer attack stated as Arthur only; mission page gives a Lenny variant (problem 2).
- rains_A.py L79 and rains_C.py L58: "he saw him / he saw the wagon train", transcript says "We saw you" (problem 4).
- kieran_A.py L63: "a beating would only produce lies", Dutch only says "now all we'll get is lies" (problem 6).

## Counts
- WRONG: 1
- IMPRECISE: 8 (problems 2, 3, 4, 5, 6, 7, 14, plus the Spider Gorge sub-point of 8)
- UNSUPPORTED: 1
- MISQUOTE: 0
- SPECULATION: 0
- COPIED: 1 (3 passages)
- DUPLICATE: 3
- STYLE: 1
- Consistency note: 1
- Fiche errors reported: 3 (lenny_A, rains_A/rains_C, kieran_A)
