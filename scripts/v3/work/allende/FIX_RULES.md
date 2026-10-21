# Agustin Allende fixers: shared decisions (binding)

Reports in this folder (scripts/v3/work/allende/): fc_report1.md (half1: intro, facts, biography, personality), fc_report2.md (half2:
relationships, skills, missions, quotes, development, reception, media, trivia), coverage_report.md.
Fiche text: allende_full_en.txt.
Files: scripts/fiches/parts/allende_A.py (biography), allende_B.py (personality, names, appearance, skills,
relationships), allende_C.py (missions, quotes, trivia, media), allende_D.py (base: facts, intro, essentials,
development, reception). EN AND FR. SPEC.md rules apply. scripts/v3/rules/OWNERSHIP.md and scripts/v3/rules/HOUSE_FACTS.md apply.

Decisions (the lead writes them here after reading the reports: one line per disputed point, which source wins):
- Quotes ownership: the three "In his own words" lines ("perhaps you come to hunt me...", "You are in no position to negotiate", "rare find...") stay in B Personality ONLY and are cut from C Quotes. C Quotes adds the confirmed Demon Drink monologue ("We brought them God... These people need a ruler."), "Sorry? Why be sorry?... Que sera, sera... Force must be used.", "we'll make a patriot of you yet." / "I love patriots.", and the full last words in An Appointed Time ("Don't shoot! Here. Take Williamson... I will leave the country. I promise.").
- Landon's "feudal king" and "Some men need to be killed", Luisa's "Allende es pura maldad", Espinoza's "brazo derecho", Victor's line: C Quotes only; B Relationships paraphrase without quotation marks.
- Irish's "Colonel something or other" line: B Names only (cut from C Quotes).
- "Civilization, at Any Price" exchange ("Even I've heard about the Colonel...") takes place on the wagon ride to Chuparosa (fc2#1).
- Personality: delete "He is never seen near a fight" (John's line is "anywhere near a fight yet").
- "An Appointed Time": John blows the gate with the Gatling at the barrels and frees the prisoners; the coach is stopped, Allende hands Bill over, both are shot by John or Reyes (Reyes shoots both if John shoots neither). Escort details told once, in B "Weapons and stagecoach" (cut from A).
- Unpaid 20,000 pesos: transcript line (John to De Santa in "Cowards Die Many Times"); told once, in A Biography (cut from Relationships and Missions table).
- Who ordered John's execution: keep the current hedge.
- Smaller: "his uncle" (one uncle); facts grid "owned farmland" attributed to the wiki; "set the dogs on him"; insults De Santa (not "his officers"); Irish "Three Card Stud or perhaps Four Card Monty"; Reyes in indirect speech in the Ledger; Irish never says the name ("some Spanish name"); Luisa "he took the honor of two young girls" (no "that day"); De Santa condemns one rebel; Espinoza entry keeps the ambiguous "He asked" and Torquemada; cut the false reason "set before 1911" for absence from RDR2/RDO.
- COPIED Origins sentences rewritten (Escalera levels, land-grab, one fact per sentence; land-grab attributed as wiki-only).
- Delete B "In the game" sub-block (duplicates Missions intro and Trivia); keep only "Weapons and stagecoach" (section renamed). Rebel posters: Names owns lapdog/puppet (cut Trivia copy and the Biography "puppet" repeat).
- GALLERY in scripts/fiches/agustin_allende.py set from gal/captions.json (6 entries, already corrected).
- Cross-fiche (EN+FR, then _enrich.py john-marston): john_D.py ~l.144 "provisional governor" -> "provincial governor"; "dies at Escalera" -> "on the road out of Escalera"; "has his men try to kill him" -> hedged (De Santa betrays him in Chuparosa; the order is attributed to the wiki).
- Story guide act 2 (EN + FR, hand-written HTML, plain <a href>, no em dashes): apply fc_report1 G1-G4.
- US spelling. No em/en dashes. FR written natively.

Report back: fixes applied per report item, items not applied with reason.
