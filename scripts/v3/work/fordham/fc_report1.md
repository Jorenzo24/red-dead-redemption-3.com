# Fact-check report 1: Archer Fordham, half1 (intro, key facts, facts grid, biography, personality, names, appearance)

## Sources used
- Wiki: scripts/v3/work/fordham/en.txt (EN page), fr.txt (FR page).
- Transcripts (scripts/v3/work/_m/): Exodus_in_America_dialogues, The_Gates_of_El_Presidio_dialogues (both branches), Bear_One_Another_s_Burdens_dialogues, Great_Men_are_Not_Always_Wise_dialogues, And_You_Will_Know_The_Truth_dialogues, And_The_Truth_Will_Set_You_Free_dialogues, The_Last_Enemy_That_Shall_Be_Destroyed_dialogues.
- Mission pages: same titles + Ending_Credits.txt (RDR2, no transcript), Bureau_of_Investigation.txt.
- fc/ledger_No60_bank_robbery.txt, fc/ledger_No213_ross_retires.txt.
- scripts/v3/rules/HOUSE_FACTS.md; fact-checked parts edgar_A-D, john_B/D, nastas_A-D, macdougal_A-D, javier_A/B, micah_A/B (+ abigail_A, jack_B, reyes_A note in fordham_A docstring); fordham_A-D docstrings.
- Images: assets/characters/archer-fordham/gallery-1.jpeg (1907), gallery-4.jpeg (1911).
- Story guides: story/rdr1-act-1/2/3, story/rdr2-epilogue-part-2 + FR mirrors.

## Verified OK
All quoted lines of "In his own words", the Ledger No. 60 and No. 213 quotations, the GOTY guide quote (via the wiki quote box), the forms of address ("Mr. Fordham", "Agent Fordham", "Archer" twice, MacDougal's "Mr. Fordham") match their sources verbatim. The Exodus escort (transcript "two lawmen", named by the mission page), Jake's telegram ("Blackwater big bugs"), both El Presidio branches ("nothing is cleared" capture-only), the whole Serendipity sequence, the bank roof/Hopkins/Manning/Muriel Scranton, "neither"/"authority over both", the armored-vehicle exchange, the Cochinay ride lines (hedged "may", mission page trivia), the gate, the thanks and "Come on, Archer" all match the transcripts. Credits scenes (Mount Hagen, Smithfield's with Morris Peyton, the Rhodes stagecoach, binoculars at Beecher's Hope) match Ending_Credits.txt; June 1907 dating and Maybelle (24 July 1900, Blackwater cemetery) match the EN wiki. Micah's shared shot, Uncle's death, one horse, 1914 non-appearance, Reyes absent at the bridge (reyes_A) are consistent with HOUSE_FACTS and the fact-checked parts. No dashes found.

## Problems

1. IMPRECISE (Beecher's Hope hedge, Key facts). Draft: "According to the Red Dead Wiki, he is among the men who come for John at Beecher's Hope later in 1911." Source: only the EN wiki says so (barn doors, en.txt Trivia); FR wiki says he is absent (fr.txt Anecdotes). Fix (standard hedge): "According to the English-language Red Dead Wiki, he is visible among the men facing John through the barn doors at Beecher's Hope later in 1911; the French-language wiki says he is not there." FR: "D'après le Red Dead Wiki anglophone, on l'aperçoit parmi les hommes qui font face à John, entre les portes de la grange de Beecher's Hope, plus tard en 1911 ; le wiki francophone affirme qu'il n'y est pas."

2. IMPRECISE (hedge, facts grid Fate). Draft: "Not given after 1911; he can be shot at Beecher's Hope, according to the mission page of ..." Source: the mission page is an EN-wiki page, and FR wiki contradicts. Fix: "Not given after 1911; according to the English-language Red Dead Wiki, he can be shot at Beecher's Hope (the French-language wiki says he is not there)". FR: "Inconnu après 1911 ; d'après le Red Dead Wiki anglophone, il peut être abattu à Beecher's Hope (le wiki francophone le dit absent)".

3. IMPRECISE (hedge, other occurrences in half2, for the fixer of part B/C). Four more wordings: Relationship John "according to the Red Dead Wiki, he is also among the men who come for him there in 1911"; Mechanics "According to the page of ..., Fordham is among the men John can shoot"; Missions table "According to the English-language Red Dead Wiki only: among the firing squad at the barn"; Trivia McKinnon (OK). Fix: align all on "according to the English-language Red Dead Wiki ... (seen through the barn doors / can be shot in the final Dead Eye); the French-language wiki says he does not take part" (FR: "d'après le Red Dead Wiki anglophone ... ; le wiki francophone affirme qu'il ne participe pas à la mission"). Missions table: replace "among the firing squad at the barn" with "seen among the men through the barn doors".

4. WRONG (cross-fiche, edgar_A.py). edgar_A: "According to the Red Dead Wiki, Fordham is among the men facing John at the barn, although he does not appear in the cutscene that follows." / FR "...même s'il n'apparaît pas dans la cinématique qui suit." Source: en.txt Trivia and the mission page casualties: he "may disappear in the following cutscene regardless of whether or not he is shot"; FR wiki says he is absent. Fix EN: "According to the English-language Red Dead Wiki, Fordham is visible among the men facing John through the barn doors and may be missing from the cutscene that follows; the French-language wiki says he does not take part in the mission." FR: "D'après le Red Dead Wiki anglophone, on aperçoit Fordham parmi les hommes qui font face à John entre les portes de la grange, et il peut être absent de la cinématique qui suit ; le wiki francophone affirme qu'il ne participe pas à la mission." (Same fix for the edgar_A docstring line "he is not in the cutscene that follows".)

5. IMPRECISE. Draft: "Ross crouches by the body, lifts it and lets it drop." Source: Ending_Credits.txt "lifts the corpse before promptly setting it down"; edgar_A "raises it and puts it back down". Fix: "lifts it and sets it back down" (FR: "le soulève puis le repose").

6. IMPRECISE. Draft: "Fordham orders John to carry Nastas, who cannot walk." Source: transcript "I don't think he can walk." Fix: "Fordham tells John to carry Nastas, saying he does not think he can walk."

7. IMPRECISE. Draft: "an informant tells Ross that Dutch is about to visit the Blackwater bank." Source: transcript "about to pay call on his bank manager"; edgar_A "visit the manager of the Blackwater bank". Fix: "is about to call on the manager of the Blackwater bank".

8. IMPRECISE (order). Draft: "The army has set up a camp outside Blackwater as bait, and Fordham explains that Dutch's gang needs constant supplies. On the way there in a vehicle armed with a machine gun, ..., Fordham praises the progress of the armed forces, calls the vehicle a simple prototype..." Source: transcript, the "armed forces"/"prototype"/"Virginia" lines come first, then Ross's camp/bait line and Fordham's supplies line, all during the drive. Fix: swap the two sentences (vehicle and prototype first, then "Ross explains that the army has made camp outside town as bait, and Fordham adds that Dutch's gang needs constant supplies.").

9. IMPRECISE. Draft: "he calls Ross 'sir' in almost every line he speaks to him". Source: transcripts; several lines to Ross have no "sir" ("It was a trap...", "We found him tied up...", "Indeed, but he's been helping us...", "Exactly, what's the alternative?"). Fix: "he often calls Ross 'sir'".

10. IMPRECISE. Draft: "He addresses John as Mr. Marston, and switches to Marston or John when he gives him orders." Source: he says "John" only once, at El Presidio ("nothing is cleared, John"), which is not an order; "Marston" is also used outside orders ("Marston, you're a public menace"). Fix: "He mostly addresses John as Mr. Marston, uses plain Marston in orders and insults, and calls him John once, at the border bridge."

11. IMPRECISE (wrong pointer). Draft: "He calls Dutch van der Linde and his Native recruits savages and insane (see Quotes)." Source: the Quotes block (half2) contains neither "fraternize with savages" nor "That man is insane"; both are in the Biography. Fix: "(see Biography)". Also reword: he says Dutch is "insane" and calls Dutch's followers "savages".

12. DUPLICATE. Personality: "He threatens John several times and tells him to watch his mouth" and "He is also the one who thanks John on behalf of his country once Dutch is dead (see Biography)." Both are told in the Biography (Bear One Another's Burdens; Cochinay) and the thanks again in Relationships/John. Fix: delete the thanks sentence from Personality; keep "He threatens John several times" without "tells him to watch his mouth".

13. DUPLICATE. "In his own words" quotes "Our armed forces have no equal..." and "And this isn't much more than a simple prototype..."; the Quotes block (part C) repeats both. Rule: Quotes block does not repeat "In his own words" lines (OWNERSHIP + fordham_B note). Fix: remove both from the part C Quotes block (keep in part B).

14. DUPLICATE. Names: "John describes one of the two men sent onto the wreck as 'an office clerk or social secretary or some such', and Fordham tells him to shut his mouth." Same exchange told in the Biography ("one of them an office clerk, and Fordham tells him to shut his mouth") and quoted again in Quotes "What others say to him". Fix: keep the quote in Names only, drop "and Fordham tells him to shut his mouth" there; remove the line from the part C Quotes block; Biography keeps the event.

15. DUPLICATE (minor). Personality "he calls Ross 'sir'" and Relationships/Ross "He calls him sir, drives for him". Fix: drop "He calls him sir" from the relationship entry.

16. WRONG/IMPRECISE (appearance). Draft: "In both games he is a dark-haired man dressed in a dark suit with a waistcoat, a white shirt and a black tie, under a bowler hat." Source: gallery-1.jpeg (1907) charcoal three-piece suit, black tie, badge; gallery-4.jpeg (1911) brown suit and dark red tie; EN wiki: 1911 "lighter three-piece suit". Fix: "In 1907 he wears a charcoal three-piece suit, a white shirt, a black tie and a bowler hat; in Red Dead Redemption (1911) his three-piece suit is brown and his tie dark red." FR: "En 1907, il porte un costume trois pièces anthracite, une chemise blanche, une cravate noire et un chapeau melon ; dans Red Dead Redemption (1911), son costume trois pièces est brun et sa cravate rouge sombre."

### Story guides (fixes outside the fiche)

17. IMPRECISE (story/rdr1-act-1-new-austin/index.html, l.109 and l.138). EN "John is brought west by Edgar Ross and Archer Fordham, two agents of the Bureau of Investigation." and key event "Federal agents Edgar Ross and Archer Fordham take Abigail and Jack Marston, and send John west after his former gang." Source: Exodus transcript/mission page (they escort him from the ferry to the train); the games do not show who took the family (fiche Biography). Fix EN l.109: "In Blackwater, <a>Edgar Ross</a> and <a>Archer Fordham</a>, two agents of the Bureau of Investigation, walk John from the ferry to the train for Armadillo." FR l.109: "À Blackwater, <a>Edgar Ross</a> et <a>Archer Fordham</a>, deux agents du Bureau of Investigation, escortent John du ferry jusqu'au train pour Armadillo." EN l.138: "Federal agents Edgar Ross and Archer Fordham hold Abigail and Jack Marston, and send John west after his former gang." (FR l.138 already says "retiennent": no change.)

18. IMPRECISE (story/rdr1-act-3-west-elizabeth/index.html l.117 and l.145 + FR). "John leads an army assault on Cochinay." / "Ross arrives moments later." / key event "John leads the assault on Cochinay". Source: And The Truth Will Set You Free transcript: the captain commands ("Forward! Move in!"), Ross and Fordham ride with them, and both agents meet John at the foot of the cliff. Fix EN l.117: "John rides to Cochinay with Ross, Fordham and an army detachment." and "Ross and Fordham arrive moments later." EN l.145: "John joins the army assault on Cochinay; Dutch steps off a cliff rather than be taken." FR l.117: "John part à l'assaut de Cochinay avec Ross, Fordham et un détachement de l'armée." and "Ross et Fordham arrivent quelques instants plus tard." FR l.145: "John prend part à l'assaut de l'armée sur Cochinay ; Dutch se jette de la falaise plutôt que d'être pris."

Act 2 guides (EN+FR) and RDR2 epilogue part 2 guides (EN+FR): nothing wrong about Fordham.

Not flagged: "soldiers and lawmen led by Ross" (same wording as fact-checked john_B; HOUSE_FACTS only bars putting Ross at the head of the column, which the draft does not).

## Count per category
- WRONG: 2 (items 4, 16)
- IMPRECISE: 12 (items 1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 17, 18)
- UNSUPPORTED: 0
- MISQUOTE: 0
- SPECULATION: 0
- COPIED: 0
- DUPLICATE: 4 (items 12, 13, 14, 15)
- STYLE: 0
Total: 18
