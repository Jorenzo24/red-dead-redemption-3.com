# Landon Ricketts fixers: shared decisions (binding)

Reports in this folder (scripts/v3/work/landon/): fc_report1.md (half1: intro, facts, biography, personality), fc_report2.md (half2:
relationships, skills, missions, quotes, development, reception, media, trivia), coverage_report.md.
Fiche text: landon_full_en.txt.
Files: scripts/fiches/parts/landon_A.py (biography), landon_B.py (personality, names, appearance, skills,
relationships), landon_C.py (missions, quotes, trivia, media), landon_D.py (base: facts, intro, essentials,
development, reception). EN AND FR. SPEC.md rules apply. scripts/v3/rules/OWNERSHIP.md and scripts/v3/rules/HOUSE_FACTS.md apply.

Decisions (the lead writes them here after reading the reports: one line per disputed point, which source wins):
- RDR2 never shows the ferry robbery (told only in dialogue). Parting in "The Mexican Wagon Train": John says "You know what I'm looking for", Ricketts answers "If you say so".
- Birth around 1861: attributed to the Red Dead Wiki citing the guide (the guide we have says 50 years old). No "Abraham Reyes" named in the Gunslinger's Tragedy conversation. Order: name first, then the advice and the Schofield.
- "Lucky in Love": the prospector IS Müller; the Stranger = Sanchez, Müller's second, per the wiki (attributed). Ledger No. 213 available after "The Last Enemy That Shall Be Destroyed". Death in 1914, in his sleep, "last week" per the article; never "old age".
- Personality must not retell events; Dead Eye gameplay sentence once; "buzzard", "coward", "remind me of myself" and the wife line quoted once (In his own words) and cut from Quotes; "Not a name that means much" only in Names. Sadie "new pair of pants": paraphrase (no transcript), no quotation marks, once. Relationships = one-clause pointers for events (Allende, Reyes, Javier, Müller, Luisa, John). Myths and Mavericks/Hagen line reuse once (Development); cards on thigh once (Trivia); "nearly invincible" once (Skills); camp poker mention once (Other media); Schofield/Dead Eye reward once.
- Ramon not "clerk"; cut "follows local politics closely"; reword COPIED Undead Nightmare sentences; "plantation in Bayou Nwa" attributed to the Red Dead Wiki; Zombie Ricketts playable since 2010 (before Myths and Mavericks); John never names the Bureau; keep the wiki's "seem" for the prisoners trivia; Wild West Heroes knife shot passive as in the novel; "seven taunts" attributed or cut; add Ledger No. 55 "amongst many other rumored and verified killings"; add wiki-only (attributed) Ricketts sometimes says he knows the hostage.
- GALLERY: images already rebuilt; set GALLERY in scripts/fiches/landon_ricketts.py from scripts/v3/work/landon/gal/captions.json (7 entries, in order; same _g() format as the existing GALLERY).
- Cross-fiche: scripts/fiches/parts/john_D.py (EN+FR) says Ricketts and John "attack Mexican Army patrols together": replace with the fights at the caves near El Matadero and the prison convoy (per transcripts), then run python3 scripts/_enrich.py john-marston.

Report back: fixes applied per report item, items not applied with reason.
