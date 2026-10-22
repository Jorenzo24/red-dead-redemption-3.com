# Catherine Braithwaite fixers: shared decisions (binding)

Reports in this folder (scripts/v3/work/catherine/): fc_report1.md (half1: intro, facts, biography, personality), fc_report2.md (half2:
relationships, skills, missions, quotes, development, reception, media, trivia), coverage_report.md.
Fiche text: catherine_full_en.txt.
Files: scripts/fiches/parts/catherine_A.py (biography), catherine_B.py (personality, names, appearance, skills,
relationships), catherine_C.py (missions, quotes, trivia, media), catherine_D.py (base: facts, intro, essentials,
development, reception). EN AND FR. SPEC.md rules apply. scripts/v3/rules/OWNERSHIP.md and scripts/v3/rules/HOUSE_FACTS.md apply.

Decisions (the lead writes them here after reading the reports: one line per disputed point, which source wins):
- Sons' deaths ("Blood Feuds, Ancient and Modern"): NO shot at the door. The son at the door tells the gang to get off
  their land, then a firefight starts (transcript). Per the mission page, two sons die when the room is stormed and
  Dutch finishes off one who is barely alive, in front of her. Never name who kills Gareth and Gerald (house rule:
  shooter not stated). Same fix in dutch_A.py and dutch_D.py (EN+FR), then python3 scripts/_enrich.py dutch-van-der-linde.
- Outside the burning house Catherine says "My sons gave him to Angelo Bronte" (never "sold"). Dutch drags her off the
  stairs and carries her out on his shoulder, gun to her head. Arthur goes back out to fight off reinforcements, then
  helps John break down the door. No promise of gold.
- Motive: the gang reads the kidnapping as revenge for the stolen horses. In ch. 4 Arthur GUESSES ransom and keeping Jack
  out of the gang's reach; never "for money".
- Bartholomew: his name comes from the wiki (transcript labels "Braithwaite"): "according to the Red Dead Wiki" in his
  relationship entry and in the quote attributions. "Subtitles say Gareth" ONCE, in Trivia only.
- Sheriff Leigh Gray deputized Dutch, Arthur and Bill to shut down her still. Hosea's "vouch" for Arthur is a joke
  (jibe answered with a jibe). The Lemoyne Raiders link is in the game (Archibald "in business with them"; the Raider
  in the saloon): no wiki attribution.
- Personality: she laughs, says "Pay the man" and "Hush now" (never "tells them to stand down"); no retelling of events.
  "You filth." (to Dutch) added to In her own words. Archibald's thoroughbred line and Tavish's "hag" line: quoted in
  Quotes (C), paraphrased without quotation marks in Personality. "120 years" once (In her own words).
- Origins: canon only (Red Dead Online Danny-Lee/moonshine -> Other media). 1806 Lucille/Douglas sentence rewritten
  (was COPIED). "British descent" (wiki-attributed). Jack "about four". No "cabins behind the ruins" (workers' cabins on
  the plantation). 1907: "seems to have died out" keeps the wiki hedge. Kieran's apology: he saw the Braithwaites come
  to camp (Relationships entry owns it).
- Estate sections do not retell the Biography (moonshine price, stills, Raiders, letter to Bronte, guards, fishing
  community). Cribbage room unstated. Gertrude, Kieran, Penelope, horse brand told once.
- WhatCulture is a countdown: she is placed between Colm (7th) and the Murfree Brood (5th).
- Appearance: add the cream nightgown during the raid.
- Gallery captions from gal/captions.json (2 entries).
- Story guides ch. 3 and ch. 4 (EN+FR): fc_report1 fix blocks A-F; every "sold Jack" (body, key events, meta/og/twitter,
  JSON-LD); Sean dies in "A Short Walk in a Pretty Town"; no horse-breaking for the Grays; no Hosea warning; "Sheriff
  Gray is killed" instead of "the Grays are wiped out".
- US spelling. No em/en dashes. FR written natively.

Report back: fixes applied per report item, items not applied with reason.
