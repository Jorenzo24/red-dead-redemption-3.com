# Fact-check report 2: half2.txt (Relationships, Weapons and gameplay, Missions, Quotes, Development and performance, Reception, Other media, Trivia, Gallery)

## Sources used
- Transcripts in `scripts/v3/work/_m/`: Landon Ricketts Rides Again, The Mexican Wagon Train, My Sister's Keeper, Must a Savior Die?, Father Abraham, Captain De Santa's Downfall, The Gates of El Presidio, An Appointed Time (`*_dialogues.txt`).
- Mission pages (same names, `.txt`): infoboxes (givers, rewards, prereqs, next), ordinal sentences, Mission Failure lists, Trivia, Bugs, Gallery.
- Other wiki pages in cache: Carlos.txt, Campo_Mirada.txt, Liars_and_Cheats.txt, Sepulcro.txt, Red_Dead_Redemption_Cut_Content.txt; work dir en.txt / fr.txt.
- Real world: `fc/newswire_2010-05-03_artwork_luisa_irish.txt`, `fc/whatculture_2013-11-16_memorable_p2.txt`; Aldape 2022 read online (redalyc.org/journal/6649/664974291002/html/); Wikipedia "Red Dead Redemption" wikitext (raw, 21 Oct 2026); IMDb (403, not readable).
- Gallery: `scripts/fiches/luisa_fortuna.py` GALLERY vs `gal/out/gallery-1..5.jpeg`, `gal/spec.txt` + `candidates.json` (source files), wiki file usage API, wiki LRRA gallery image Rdr_landon_ricketts_rides_again38.jpg, Father Abraham Rdr_banditos.jpg.

## Verified OK
Every quote in the Quotes block matches its transcript word for word (incl. "Déjen mi hombre!", "Children see more than you think" without full stop, "seemed"), and its context labels are right. None of the four "In her own words" lines ("living in history", "Revolutions are always won with blood", "Be honest with yourself", "Every time Allende hits us") is repeated in Quotes. Mission ordinals (31, 33, 34, 35, 38, 39, 41), rewards, givers, prerequisites ("Civilization, at Any Price" from the prerequisites section), "Aztec Gold" unlock, West Elizabeth opening all match the mission pages. Failure conditions, the crash note, the loot and face-down note, the PS3 explosives remark, "her prompts are not always accurate" (Father Abraham walkthrough), "first time John says Jack's name", Alejandro Fortuna's grave (Sepulcro list), Campo Mirada intact in multiplayer, Liars and Cheats (21 Sep 2010, 15 characters, Redemption list of 8, chaps note), the cut-content page not naming her: all OK. Newswire 3 May 2010 text ("19-year old Mexican teacher and revolutionary", People of the West, character videos, Downloads) and "two weeks before" release (18 May 2010) OK. WhatCulture: David Michael Hughes, 16 Nov 2013, entry no. 5, all three quotations verbatim, paraphrase of the dictator point OK. Aldape: Revista Panamericana de Comunicación vol. 4 no. 2 (2022), Texas A&M, "a staunch Reyista who firmly believes Abraham is the true savior of the country" verbatim; "forgets his followers' names" is in the next paragraph of the same section ("The Mexican Caudillo"), corridos/soldaderas line OK. Wikipedia's RDR article: 0 occurrences of "Luisa" (claim OK). No em/en dashes in the chunk.

## Problems

1. DUPLICATE. Quotes: "Victor: It is good that you are helping Luisa. / ... / Victor: She can fight as well as any man." The line is already quoted in Personality ("She can fight as well as any man."), paraphrased in Origins and in the Victor Melendez relationship ("praises her fighting (see Personality)"). OWNERSHIP: lines quoted in B are not repeated in C. Fix: cut this exchange from Quotes (keep the Personality quote).

2. DUPLICATE. Quotes: "Abraham: How do you know my young lover, Laura? / Marston: It's Luisa. ..." Names already quotes "my young lover, Laura" (Must a Savior Die?). Fix: cut from Quotes or keep only "Money, women... Luisa, if you want her" part if wanted (but then the exchange is unclear); simplest is to cut.

3. DUPLICATE. Quotes: "Abraham: Oh yes, she was very brave ... Laura's Day! / Marston: Luisa. / Abraham: What? Oh yes. I knew a Laura as well." Names quotes "Laura's Day" and paraphrases "knew a Laura as well"; Biography (last paragraph of Act II) retells the whole exchange. Fix: either remove the quotation marks in Names (paraphrase) and keep the Quotes block, or cut it from Quotes. Pick one; do not keep both.

4. IMPRECISE (broken pointers). Four relationship entries send the reader to "(see Quotes)" for lines that are NOT in the Quotes block: Abraham Reyes ("married in their hearts ... cannot accept a peasant girl (see Quotes)"; the line is in Names/Biography), Abraham Reyes 2nd para ("she was incredible, recommends her ... laughs at the idea of marrying a peasant (see Quotes)"; Quotes only has "Who? / The girl from Campo Mirada"), John Marston ("would rather die than be a cynic ... (see Quotes)"; not in Quotes), Agustin Allende ("calls him pure evil and says she will one day cut his heart out (see Quotes)"; "Allende es pura maldad ... One day I will cut his heart out" is nowhere in the fiche as a quote). Fix: point to Biography/Names, or drop the pointer (or, for Allende, add the Father Abraham line to Quotes, it is verbatim in Father_Abraham_dialogues.txt).

5. DUPLICATE. Relationships, Abraham Reyes: "At Agave Viejo, in 'The Gates of El Presidio', he tells John that she was incredible, recommends her to him and laughs at the idea of marrying a peasant." Biography (Gates paragraph) tells the same scene in full, and the Missions table row repeats it. OWNERSHIP: relationships refer to events in one clause. Fix: "At Agave Viejo he dismisses her as a peasant he will never marry (see Biography)."

6. DUPLICATE. Weapons and gameplay vs Trivia: four items are told twice: (a) never rides a horse (Skills: "one of three major characters who never ride a horse, with Agustin Allende and Nigel West Dickens"; Trivia: "Luisa never rides a horse ... Agustin Allende and Nigel West Dickens"); (b) failure conditions (Skills: "The missions she takes part in fail if John kills her ..."; Trivia: "'Landon Ricketts Rides Again' fails if the player kills Luisa ..."); (c) the crash (Skills: "she can crash it if the player watches the journey"; Trivia: "Luisa can crash the vehicle, which fails the mission"); (d) "her body cannot be looted" (both). OWNERSHIP: Trivia keeps only facts told nowhere else. Fix: cut the four from Trivia; keep in Skills.

7. WRONG (as stated in Trivia). "According to the Red Dead Wiki, Luisa never rides a horse in the game." Contradicted: Landon_Ricketts_Rides_Again.txt (walkthrough and bug "when Landon Ricketts puts her on his horse"; she is carried out on Ricketts's horse) and Carlos.txt ("Carlos takes Luisa back home on horseback"; gallery "Carlos and Luisa ride off"). Skills already hedges with Carlos; Trivia does not. Fix: cut the Trivia item (see 6); in Skills, add that she is carried on Ricketts's horse, or say "never rides a horse herself".

8. IMPRECISE. Skills: "... fail if John ... assaults or kills her ('Must a Savior Die?', 'Father Abraham', 'Captain De Santa's Downfall', where hurting any rebel also counts)". The pages list "Assaults or kills any rebel(s)" for Must a Savior Die? and Father Abraham too, not only De Santa's Downfall. Fix: "... in all three, hurting any rebel also fails the mission".

9. DUPLICATE. Other media, Marketing: "According to the French-language Red Dead Wiki, an image of Luisa was one of the background images of Rockstar's official website" repeats Design and promotion: "The French-language Red Dead Wiki notes that she is one of the backgrounds of the official site." Fix: keep one (Design and promotion), cut the Marketing subsection.

10. IMPRECISE. Relationships, Landon Ricketts: "Ricketts learns of her capture from her brother Emilio". Transcript: Emilio only answers "No se" / "Yo no se"; Ricketts says "these men were just telling me about Mr. Escuella" then "But they do have his sister. Emilio's I mean." Nobody says Emilio told him. Fix: "Ricketts is questioning her brother Emilio about Escuella at the Chuparosa hotel when he tells John that the army holds her."

11. IMPRECISE. Relationships, Her father: "he thanks John in English for saving his daughter and apologizes for his English." Transcript: "Muchas gracias! My family is indebted to you. Forgive my English." He thanks in Spanish then speaks English, and never mentions saving his daughter (Luisa introduces John as "the gringo who saved me"). Fix: "he thanks John ('Muchas gracias'), says his family is indebted to him and apologizes for his English."

12. DUPLICATE. The Father Abraham line thanking John for helping her mother and Miranda escape (and the regret about her father / they know nothing of his death) is told in Biography (Father Abraham para), Miranda entry, Her father entry and Her mother entry. Fix: keep in Biography + Her mother entry; cut from Miranda and Her father entries.

13. UNSUPPORTED. Missions intro: "Her own strand has four missions, which begin at Campo Mirada or, once the house has burned, at the rebel camp beside it." All four infoboxes give start = Campo Mirada; Captain De Santa's Downfall page says "Luisa Fortuna's temporary camp"; nothing says the camp is "beside" the house (Father Abraham: rebels stop John "on his way to meet" her). Fix: "which all start at Campo Mirada (the family house, then, once it has burned, a rebel camp)".

14. IMPRECISE. Trivia: "none of the four prisoners it names at the border seems to be that writer or the local official". The_Mexican_Wagon_Train.txt names four rescued prisoners (Carruthers, De la Barra, Ichinaga, Gutierrez) plus an Ontiveros, and does not say "at the border". Fix: "none of the prisoners it names seems to be that writer or the official". Also partial DUPLICATE of Biography (Castillo already named there): keep only the spelling note and the prisoners note.

15. UNSUPPORTED. Development: "the game's credits on IMDb list Galeas in the role." IMDb returned 403 (fullcredits and nm2277691); no copy saved in fc/. Only the wiki infobox (voice = IMDb link nm2277691 "Francesca Galeas") is verifiable. Fix: save an IMDb copy to fc/ or drop the IMDb clause and keep "The Red Dead Wiki credits Francesca Galeas".

16. IMPRECISE (gallery captions, not wrong but vague; checked against images and source files). gallery-2 (Rdr 0466) and gallery-3 (wiki tumblr co3, "Luisa and Marston talk about the future of Nuevo Paraíso"): night, seated, rebels in sombreros behind John: the campfire talk of "Father Abraham" (the only seated Luisa/John scene, "They sit by the campfire"). gallery-4 (Rdr 0474): open supply wagon at dusk, John on foot: most likely the "Father Abraham" departure ("You can ride with me in the wagon or follow on your horse"); "Must a Savior Die?" uses a stagecoach. gallery-5 (tumblr co7, wiki caption "Luisa is assisted by Marston"): daylight, she holds John's arm in open desert; matches the end of "Landon Ricketts Rides Again" where the freed Luisa is supported (cf. wiki LRRA gallery no. 38), but not certain. Fix (optional): captions "Luisa and John by the rebels' campfire in 'Father Abraham'." / "Luisa on the wagon before the ride to the Frontera Bridge." / "Luisa, just freed, with John Marston." Keep generic for 5 if unsure. Current alt texts are accurate.

17. DUPLICATE. Development, Design and promotion retells the 3 May 2010 Newswire artwork post; Personality (half 1) already opens with "When it added her artwork to the official Red Dead Redemption website, Rockstar described her on its Newswire on May 3, 2010". OWNERSHIP: B owns the quote, D may point. Fix: in Personality keep just "Rockstar described her on its Newswire on May 3, 2010:" + quote; D keeps the post details.

18. DUPLICATE. Trivia, Castillo: "Luisa names a writer, Castillo, among the prisoners in 'The Mexican Wagon Train'" repeats Biography (Wagon Train para). Fix: open the item with the new fact only: "The mission page spells the writer's name Castilla, ..." (merge with 14).

## Count per category
- WRONG: 1
- IMPRECISE: 6 (4, 8, 10, 11, 14, 16)
- UNSUPPORTED: 2 (13, 15)
- MISQUOTE: 0
- SPECULATION: 0
- COPIED: 0
- DUPLICATE: 9 (1, 2, 3, 5, 6, 9, 12, 17, 18)
- STYLE: 0
- Total: 18
