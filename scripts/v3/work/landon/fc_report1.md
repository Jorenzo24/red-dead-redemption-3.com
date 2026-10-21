# Fact-check report 1: Landon Ricketts, half1 (intro, key facts, facts grid, Biography, Personality, In his own words, Names, Appearance)

## Sources used
- Transcripts: `_m/The_Gunslinger_s_Tragedy_dialogues.txt`, `_m/Landon_Ricketts_Rides_Again_dialogues.txt`, `_m/Lucky_in_Love_dialogues.txt`, `_m/The_Mexican_Wagon_Train_dialogues.txt`, `landon/fc/We_Shall_Be_Together_in_Paradise_dialogues.txt`.
- Mission pages: `_m/The_Gunslinger_s_Tragedy.txt`, `_m/Landon_Ricketts_Rides_Again.txt`, `_m/Lucky_in_Love.txt`, `_m/The_Mexican_Wagon_Train.txt`, `_m/Biographies_and_Lies.txt` (no transcript exists).
- Newspapers: `landon/fc/Landon_Ricketts_Rumored_Alive.txt`, `landon/fc/Landon_Ricketts_Dead.txt`, `landon/fc/Blackwater_Ledger.txt` (issue availability), `landon/fc/Blackwater_Massacre.txt`, `landon/fc/Casa_Madrugada.txt`.
- Character pages: `landon/en.txt`, `landon/fr.txt`; `landon/fc/wp_ross_hagen.txt`; gallery contact sheet `landon/gal/contact.jpg` (appearance).
- Rules: `rules/OWNERSHIP.md`, `rules/HOUSE_FACTS.md`; docstrings of `parts/landon_A.py`, `landon_B.py`, `landon_D.py`; full text `landon_full_en.txt` for duplicates.

## Verified OK
Every quotation in the chunk matches a transcript or the wiki quote box verbatim (GOTY description, "Living quietly, waiting.", "I didn't say I'd become a coward...", "Damn right they don't, my sarcastic little apprentice.", "Only a buzzard feeds on his friends.", "You know, you remind me a lot of myself...", "I always thought I'd lived a charmed life...", "Landon Ricketts. Not a name that means much anymore.", "an old goat like me", "My name means something.", "you are the savior of this town"). Both newspaper articles are summarised accurately (1896 Butcher Brothers, 1899 Blackwater, 1902 eastern California, Wild West show, "last week", "three years ago", autobiography never published, Johnny West rumour). Issue No. 55 is available after "Hanging Bonnie MacFarlane" (Act I). Irish ferries John across; the bandits' "taxation", hat and boots; socialist and orphanage exchange; bottles and vultures; Ramon and the bank wagon (three robbers, hostage driver, three more at the roadblock); whiskey; Emilio and the big American; the fence line; train or horse, Casa Madrugada, Carlos at the butchery, caves, dynamite, horses, Diez Coronas, Luisa on Javier; poker, champagne, impasse, Sanchez as second, duel advice, the Stranger's hostage, four accomplices, Santander's casualty attribution; the Wagon Train dialogue (relics, Castillo, the official, Escalera, rat, bad habit, family, bridge with fire bottles and Gatling gun, American soil, handshake, four named prisoners); "each takes control of a wagon" (character page); Undead Nightmare (sunshine and sand, elixir, two bait and two dynamite, Boom Bait x2, Chicago and Pittsburgh attributed); Ross Hagen; Zombie Ricketts and "Ricketts infecté"; appearance consistent with in-game shots. No em or en dashes.

## Problems

1. **WRONG** (Biography, Origins para 2): "Red Dead Redemption 2, which shows the gang's ferry robbery and its aftermath, never mentions him in connection with it." RDR2 does not show the robbery: the game opens after it, and the robbery is only told in dialogue (`fc/Blackwater_Massacre.txt`, Events: "According to Javier Escuella..."; `parts/dutch_A.py` tells it through Javier, Hosea and Trelawny). Fix: "Red Dead Redemption 2, which opens after the gang's failed ferry robbery and tells it through the gang's dialogue, never mentions him in connection with it."

2. **WRONG** (Biography, Mexican Wagon Train, last para): "Ricketts hopes John finds what he is looking for; John answers that he knows what that is." Transcript (`The_Mexican_Wagon_Train_dialogues.txt`): John: "You know what I'm looking for." Landon: "If you say so, Marston. If you say so." It is Ricketts whom John says knows. Fix: "Ricketts hopes John finds what he is looking for; John answers that Ricketts knows what that is, and Ricketts replies: if you say so."

3. **IMPRECISE** (Origins para 1): "The Red Dead Redemption Game of the Year guidebook places his birth around 1861." The 1861 date is the wiki's (`en.txt`: "Born circa 1861" with a ref to the guide); the only guide text available calls him "a 50-year-old" (quote box), and part B says the guide was not read. The facts grid gets the attribution right. Fix: "According to the Red Dead Wiki, which cites the Game of the Year guide, he was born around 1861." (or drop it from Origins, since the grid already has it).

4. **UNSUPPORTED** (Origins para 3): "the bank's clerk, Ramon". Nothing makes Ramon a clerk: the transcript only has "Our bank wagon's under attack", the mission page says "a scared bank employee", and the Ramon relationship entry says "This man of Chuparosa". Looked in the transcript, mission page, `_m/Chuparosa.txt` (inhabitants list, no role). Fix: "Ramon, a man of Chuparosa whose bank wagon is attacked," and align Personality's "the bank employee Ramon" with the same wording.

5. **IMPRECISE** (Origins para 3): "...and the rebel leader Abraham Reyes as one more local man promising the peasants their freedom". In "The Gunslinger's Tragedy" he says "another local guy running around promising the peasants their freedom" without a name. The Reyes relationship entry says so explicitly ("without giving a name"), so the two contradict each other. Fix: "...and speaks of another local man promising the peasants their freedom, like the two or three before him; he names Reyes only later, in 'Landon Ricketts Rides Again'."

6. **SPECULATION** (Origins para 3): "He follows the local politics closely." This is drawn from a single conversation. Fix: cut it; the next sentence gives the facts.

7. **IMPRECISE** (Biography, Gunslinger's Tragedy para 2): "He hands him a Schofield Revolver ... reminds him to keep his back straight ... Between two rounds he gives his name". In the transcript the order is reversed: first round of bottles, then the name ("Landon Ricketts..."), the talk about Escuella and Allende, and only then "keep that back straight" and "See if this Schofield makes a difference". (The mission page puts the Schofield at the start, but the transcript wins.) Fix: "After a first round of bottles he gives his name... Before the second round he tells John to keep his back straight and hands him a Schofield Revolver, which he calls a real gun."

8. **IMPRECISE** (Lucky in Love): "against the German Andreas Müller, a silver prospector, Manolo Santander and a man the mission calls the Stranger." The list reads as four opponents plus an unnamed prospector, but the prospector is Müller ("send you off prospecting for more silver"). The wiki also identifies the Stranger with Sanchez, Müller's second (`en.txt`: "[[The Stranger|Sanchez]]"), and the draft introduces Sanchez separately with no link. Fix: "against Andreas Müller, a German silver prospector, Manolo Santander and a man the mission calls the Stranger (named Sanchez on the Red Dead Wiki)". Then "with Sanchez, the Stranger according to the wiki, as his second".

9. **IMPRECISE** (Wagon Train, trail para): "he has heard that he is making new friends on both sides of the war". The transcript has "Rumor has it you've been making all kinds of new friends"; "both sides" comes only from the fence image that follows. Fix: "he has heard rumors that John is making all kinds of new friends, and warns him that if he keeps jumping from one side of the fence to the other he could end up impaled on it."

10. **IMPRECISE** (same para): "says John reminds him of himself when he was young, stubborn and angry." Transcript: "How I used to be. Stubborn and angry." No age is given. Fix: "of himself as he used to be, stubborn and angry."

11. **IMPRECISE** (Death 1914): "issue No. 213 ..., the 1914 issue that can be read after John's death, in the part of the game where Jack Marston is the playable character." `fc/Blackwater_Ledger.txt`: No. 213 is "Available after 'The Last Enemy That Shall Be Destroyed'", the final mission. Fix: "the 1914 issue that becomes available after the final mission, 'The Last Enemy That Shall Be Destroyed', with Jack Marston as the playable character."

12. **IMPRECISE** (Personality para 2): "In 'The Mexican Wagon Train' he jokes that some writers and officials need to be killed, then tells Luisa that he was joking. On the same ride he turns hard on John". The joke is made at the hotel, before the ride (transcript), so "On the same ride" is wrong. Fix: "Later, on the ride, he turns hard on John" (but see item 15, which cuts the passage).

13. **IMPRECISE** (Names): "The people of Chuparosa call him Señor Ricketts". In the transcripts only Ramon does ("Sr. Ricketts! ... Señor Ricketts!"). Fix: "Ramon calls him Señor Ricketts".

14. **COPIED** (Undead Nightmare): two sentences follow the wiki's wording closely.
   - Draft: "Unlike the other safe zones of the expansion, the town has no army or barricades, and some undead are still inside its limits when John arrives." Wiki (`fc/Casa_Madrugada.txt`): "unlike the other safe zones, Casa Madrugada is not blocked off or protected by an army ... Also, unlike the other safe zones, Casa Madrugada does have undead within its borders when Marston first arrives."
   - Draft: "Ricketts says he has seen and done ugly things in his life, but never anything like the dead walking." Wiki (`_m/Biographies_and_Lies.txt`): "despite having seen and done ugly and horrible things in his life, he'd never seen anything quite as ugly and horrible as the dead walking."
   Fix: rephrase, for example "It is the only safe zone of the expansion with no army guarding it, and undead still wander inside when John arrives." and "Ricketts tells John that the walking dead are worse than anything he has seen or done."

15. **DUPLICATE** (Personality para 2 vs Biography and Names): the paragraph retells events the Biography already narrates: Ramon's "savior" line (also Origins para 3), "He bets that he is still the fastest gun" (Gunslinger para 3), the writers-and-officials joke (Wagon Train para 1), and "calls him a rat and reminds him that his own name means something" (Wagon Train para 2, and the quote in Names). Keep them in the Biography, and keep "My name means something" quoted in Names. In Personality keep only the traits: he answers the townspeople's calls, he teases John, he drinks and plays poker, he speaks Spanish and translates.

16. **DUPLICATE** (Biography, Gunslinger para 2 vs Gunfighting and weapons, "What he teaches John"): "In the game, this sequence teaches the third level of Dead Eye, in which the player marks several targets before firing" is gameplay, and gameplay belongs to part B (OWNERSHIP: Skills/gameplay -> B), which says it again in full. Back straight and the "real gun" Schofield are told in both places too. Fix: cut the Dead Eye sentence from A and keep A's back-straight/Schofield clause as a bare paraphrase. The reverse case is in half2: Skills repeats the train-or-horse choice that Biography (Rides Again para 2) already tells, so trim it there to a pointer.

17. **DUPLICATE** (Origins para 1 and para 3 vs In his own words): Origins paraphrases lines from the missions that "In his own words" quotes one section later: the charmed life ("In the last mission of his strand he tells John that he once believed he had lived a charmed life...") and "living quietly and waiting", "will not stand by while people ... suffer ... gives them some hope". Para 3 also overlaps the Allende and Reyes relationship entries (feudal king, the local man promising freedom). These are 1911 mission scenes, not backstory. Fix: cut them from Origins (keep "twenty-five years killing men" as the only self-report there), and give Allende's "feudal king" and the unnamed rebel one sentence in the Gunslinger's Tragedy narrative.

18. **DUPLICATE** (Biography 1911 intro vs Death 1914 vs Skills): "Ricketts gives John four missions ... and appears in no mission of the first or third act" (Biography 1911 intro), then "Ricketts does not appear in the third act" (Death 1914), and "Ricketts gives the four missions of his strand" (Skills). Keep the 1911 intro sentence. Cut the first sentence of Death 1914, and in Skills point to the Missions table.

19. **DUPLICATE** (In his own words vs Quotes, half2): "Only a buzzard feeds on his friends." is quoted in "In his own words" and again in the Quotes block (`landon_full_en.txt` line 117). Part B's register owns it, so remove it from part C Quotes.

## Count per category
- WRONG: 2
- IMPRECISE: 9
- UNSUPPORTED: 1
- MISQUOTE: 0
- SPECULATION: 1
- COPIED: 1
- DUPLICATE: 5
- STYLE: 0
- Total: 19
