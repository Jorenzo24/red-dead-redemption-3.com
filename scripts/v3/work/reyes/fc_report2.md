# Fact-check report 2: Abraham Reyes, chunk half2.txt (Relationships to Gallery)

## Sources used
- Transcripts in scripts/v3/work/_m/: Must_a_Savior_Die_dialogues, Cowards_Die_Many_Times_dialogues, The_Great_Mexican_Train_Robbery_dialogues, The_Gates_of_El_Presidio_dialogues, An_Appointed_Time_dialogues, Father_Abraham_dialogues, Captain_De_Santa_s_Downfall_dialogues, Civilization_at_Any_Price_dialogues, Mexican_Caesar_dialogues, The_Demon_Drink_dialogues, My_Sister_s_Keeper_dialogues, Landon_Ricketts_Rides_Again_dialogues, The_Gunslinger_s_Tragedy(_dialogues).
- Mission pages: the same missions plus A_Civilized_Man, On_a_Pale_Horse, Mother_Superior_Blues; Reyes_Rebels, Reyes_Rebels_Outfit, Drew_MacFarlane, Herbert_Moon, Casa_Madrugada, Liars_and_Cheats, Red_Dead_Redemption_Cut_Content.
- Wiki character page en.txt; live wiki API (John_Marston, Leigh_Johnson, Luisa_Fortuna, Bonnie_MacFarlane, Drew_MacFarlane, Red_Dead_Redemption, Cut Content, plus John_Marston revisions of Dec 2013, Dec 2017, Jun 2020, Dec 2023; file pages and fileusage of the gallery images).
- Real world: fc/wp_josh_segarra.txt (Wikipedia), Game Informer review (WebFetch, gameinformer.com, Matt Bertz, 17 May 2010), landon/fc/sportskeeda_2023-08-13.txt, Aldape article on Redalyc (redalyc.org/journal/6649/664974291002, WebFetch).
- Gallery: gal/out/gallery-1..5.jpeg viewed; gal/spec.txt + candidates.json to map each file.

## Verified OK
Every quoted line in the Quotes block matches a transcript or a wiki quote list verbatim (automated check, then manual), and each attributed context is right (speaker, mission, moment). No Quotes line repeats an "In his own words" line. The Relationships facts check out against the transcripts: the Laura/Luisa scenes, the "brother" invitation to Agave Viejo, the sarcasm exchange, the corrido, the staff offer, the silk sheets, Allende's "natural allies", De Santa's insults, Espinoza on recruiting gringos, Ricketts on Luisa, Zubieta, Victor on women and children, and Father Abraham ("destroy them! And kill everyone. Abraham wants to send a message"). The mission table checks out against the infoboxes: ordinals 26, 35, 36, 37, 38, 40, 41, rewards, Aztec Gold, the Sons of Mexico and No More Fancy Words achievements, Pardon Letter, Double-action Revolver and Throwing Knives. So do the failure conditions and the trivia from the mission pages (imaginary soldiers, the replay De Santa line, GOTY censorship, lasso, the rare Allende run, Undead Reyes body that cannot be looted), Drew MacFarlane's outfit (Drew_MacFarlane.txt), the Casa Madrugada poster alley (Casa_Madrugada.txt) and the cut bounty poster with an unused goatee. Liars and Cheats: released 21 Sep 2010, with the Damnation list. The 2023 and 2024 ports have no multiplayer. Segarra's biography matches his Wikipedia article. The Game Informer quotes, author, date and 9.75 score are verbatim. The Sportskeeda rank, author and quote are correct. All three Aldape quotes are verbatim. No em or en dashes.

## Problems

1. **WRONG** (line 60, Captain De Santa's Downfall row): "If the rebels shoot De Santa, Victor Melendez cheers for Reyes."
   Source: Captain_De_Santa_s_Downfall_dialogues.txt, tabber: "Viva Abraham Reyes!" is in the branch "If Marston kills De Santa". In the rebels branch Victor says "Esto es para Mexico! ... It really should have been you."
   Fix: "If John shoots De Santa himself, Victor Melendez cheers for Reyes."

2. **WRONG** (line 50, A Civilized Man row: "Final mission of the expansion."; line 42: "In Undead Nightmare, he is the target of the final mission.")
   Source: A_Civilized_Man.txt infobox, next = "On a Pale Horse". On_a_Pale_Horse.txt: "is the final mission featured in the ... Undead Nightmare DLC pack."
   Fix: "Second-to-last mission of the expansion" / "he is the target of the second-to-last mission". The same error is in half1 (Biography: "In "A Civilized Man", the expansion's final mission"), so the lead should fix it there too.

3. **UNSUPPORTED** (line 131): "Javier Aldape, a doctoral student in Hispanic studies at Texas A&M University".
   Source: the Redalyc article page gives only "Texas A&M University, USA" (email @mays.tamu.edu). It mentions no doctoral status and no department. Searched web_notes_BD.txt (which says "Hispanic Studies" with no source) and Redalyc.
   Fix: "Javier Aldape, of Texas A&M University,".

4. **IMPRECISE** (line 131): "(vol. 4, no. 2, 2022, online in April 2023)".
   Source: Redalyc gives received 30 Sep 2022, published 21 Oct 2022. The April 2023 date comes from the SciELO indexing only.
   Fix: "(vol. 4, no. 2, 2022)".

5. **IMPRECISE** (line 129): "published by Sportskeeda on August 13, 2023".
   Source: landon/fc/sportskeeda_2023-08-13.txt shows "Modified Aug 13, 2023 12:48 GMT". That is the update date, not necessarily the publication date.
   Fix: "updated by Sportskeeda on August 13, 2023" (or just "in August 2023").

6. **IMPRECISE** (gallery caption 4): "John and Reyes at Escalera." / "John et Reyes à Escalera."
   Source: spec 6 = "File:Rdr Marston and Reyes kill Allende.png", used on the wiki's An Appointed Time page. The image shows Reyes bloodied (after Zubieta's beating) aiming beside John in open scrub, which is the stagecoach ending on the road out of Escalera (HOUSE_FACTS: Bill dies "near Escalera", on the road, not in the town).
   Fix: "John and Reyes take aim at Allende on the road out of Escalera ("An Appointed Time")." FR: "John et Reyes mettent Allende en joue sur la route d'Escalera (\"An Appointed Time\")."

7. **UNSUPPORTED** (gallery caption 1): "Abraham Reyes, as rendered in the 2023 port of Red Dead Redemption."
   Source: spec 0 = "File:Abraham Reyes PS5.jpg" (uploaded Feb 2025, no description). The file name says PS5, not "2023 port". It is plausible but not stated anywhere.
   Fix: "Abraham Reyes in Red Dead Redemption." Or keep it only if the lead accepts the file-name inference.
   Images 2 and 3 (Rdr 0490/0494, 590x335, no description, used only on the Reyes page) cannot be tied to a mission. Image 3 is a night town square with a "POSADA" sign, and Reyes's face is barely visible. Both are probably pre-release frames. The generic captions "with John Marston in Nuevo Paraíso" and "at night" claim nothing wrong, so keep them. Do not name a mission or town.

8. **IMPRECISE** (line 148): "He is also the only undead with two sets of sounds".
   Source: en.txt Trivia: "Reyes also appears to be the only undead to have more than one set of audio files". Line 38 hedges correctly ("seems").
   Fix: "He also appears to be the only undead with two sets of sounds".

9. **SPECULATION** (line 19): "Reyes calls him the country's kind and generous dictator, with heavy irony".
   Source: The_Great_Mexican_Train_Robbery_dialogues.txt has the words but no stage direction. "With heavy irony" is the drafter's reading.
   Fix: delete "with heavy irony" (the quoted words speak for themselves), or put them in quotation marks: calls him "Our country's kind and generous dictator".

10. **IMPRECISE** (line 122): "played Adrian Chase in the fifth season of Arrow (2016)".
    Source: wp_josh_segarra.txt: cast June 2016 for season 5, which aired 2016 to 2017.
    Fix: "(2016 to 2017)", or drop the year.

11. **COPIED** (line 136): "his goatee and hair are slightly shorter in these screenshots than in the final game".
    Wiki (en.txt Trivia): "As seen in pre-release screenshots, Reyes had a rather neater appearance, as his goatee and hair were slightly shorter."
    Fix: delete. It is also a duplicate of line 124 (see 15).

12. **DUPLICATE**: the poster list is at line 35 (Speeches, songs and posters) and again at line 145 (Trivia).
    Fix: keep line 35 and add "(in the alley leading to the shooting gallery)" there if wanted. Delete line 145 (OWNERSHIP: trivia only what is nowhere else).

13. **DUPLICATE**: line 37 ("In the game": does not fight in Must a Savior Die?/Train Robbery; ties up drivers; lassoes Bill) repeats lines 141 and 143.
    Fix: keep line 37. In 141 keep only the horse-bump fail sentence. In 143 keep only the rare "Allende runs into the brush" sentence.

14. **DUPLICATE**: line 38 (rebels replace the army as the law; last outfit piece on sale in Escalera) repeats line 144.
    Fix: delete line 144.

15. **DUPLICATE**: pre-release look at line 124 (Before release) and line 136 (Marketing).
    Fix: keep 124. In 136 keep only the artwork and screenshots sentence without the hair/goatee clause.

16. **DUPLICATE**: Undead Reyes as the slimmest Bruiser with two sets of sounds (line 38 and line 148). The Semi-auto Shotgun with "Reyes brought protection" appears at line 38, line 40 and line 149.
    Fix: keep each fact once. Suggestion: keep the Bruiser and sounds in Trivia 148 and the shotgun in 149, and cut both from line 38. Line 40 may keep "plus the Semi-auto Shotgun of Undead Nightmare" as a weapon-list item.

17. **DUPLICATE**: the multiplayer model speaking of himself in the third person appears at line 134 (Multiplayer) and in half1 Names (full text line 62).
    Fix: keep it in Names (personality owns names), delete it from 134 or the other way round. Keep one.

18. **DUPLICATE**: the Herbert Moon "Napoleon" quote appears verbatim in Relationships (line 30) and in Quotes (line 73).
    Fix: keep it in Quotes. In Relationships, give the second line only, or paraphrase with "(see Quotes)".

19. **DUPLICATE**: Luisa's "his family does not approve" appears in Biography (full text line 26), Relationships Luisa (line 6), His family (line 22) and as a quote (line 71).
    Fix: keep the quote and one mention (His family). Drop the clause from the Luisa paragraph.

20. **DUPLICATE**: the Relationships paragraphs retell Biography events in detail. John (lines 3-4: thought John was Allende's man, money/women/Luisa, corrido, staff offer), Luisa (line 6: Laura's Day), Dutch (line 16) and Landon (line 18) repeat full-text lines 33, 37, 39 and 45.
    Fix: per OWNERSHIP (biography owns events), cut these to one-line summaries with "(see Biography)". Keep only what Biography lacks, such as the sarcasm exchange and the staff offer if they are absent there.

21. **UNSUPPORTED (outside the chunk, john_E.py line 130)**: "The same early trailers use different voices for several characters: John, Leigh Johnson, Abraham Reyes, Luisa Fortuna, Bonnie MacFarlane and her father Drew MacFarlane."
    Searched: the current wiki pages of John, Leigh, Luisa, Bonnie, Drew, Red Dead Redemption and Cut Content (no such line). John_Marston revisions of 2013, 2017, 2020 and 2023 (only "John looked much younger and thinner" in trailers). Wiki full-text search. Two web searches. Nothing found.
    The only partial support: Colin Nissan says he voiced the Marshal in a pre-release trailer (Kotaku, Owen Good, 17 Aug 2010, used in leigh_D.py). That covers Leigh only.
    Fix: john_E.py (and the live John fiche EN+FR) must drop the sentence, or reduce it to the Leigh/Nissan fact. reyes_D.py correctly excludes it; keep it excluded.

## Count per category
- WRONG: 2
- IMPRECISE: 5
- UNSUPPORTED: 3 (including the john_E.py claim, outside the chunk)
- MISQUOTE: 0
- SPECULATION: 1
- COPIED: 1
- DUPLICATE: 9
- STYLE: 0
- Total: 21
