# Rains Fall v3 fiche (MEDIUM tier): shared brief for drafting agents

Repo root on this device: /Users/joseph/Documents/SITES/GIT/red-dead-redemption-3.com/ (all paths below are relative to it)
Work dir: scripts/v3/work/rains/   Shared cache of mission pages and transcripts: scripts/v3/work/_m/

READ FIRST: scripts/fiches/SPEC.md (binding rules), scripts/v3/rules/OWNERSHIP.md (each fact in ONE place) and
scripts/v3/rules/HOUSE_FACTS.md (shared-event decisions already settled on other fiches: never contradict them).
Model files to imitate (structure, block formats, tone): scripts/fiches/parts/uncle_A.py, uncle_B.py,
uncle_C.py, uncle_D.py (fully fact-checked), and a recent medium fiche such as leviticus_A..D.py.
This is a MEDIUM fiche: same sections, shorter, no padding.
Target total EN length: at least the wiki page length (Rains Fall wiki EN is in scripts/v3/work/rains/en.txt), typically 3,000 to 5,000 words.

Sources available locally:
- Wiki page wikitext: scripts/v3/work/rains/en.txt (EN), scripts/v3/work/rains/fr.txt (FR wiki, may be missing: fetch it if needed).
- Mission pages and transcripts: scripts/v3/work/rains/missions.txt lists the pages of this character's "Mission appearances" and
  their file in scripts/v3/work/_m/ (`*_dialogues.txt` = transcripts). The cache is shared by every fiche: other missions may
  already be there (ls scripts/v3/work/_m/). Missing page: python3 scripts/v3/fetchpage.py "<Title>" "<Title>/dialogues".
  Transcripts beat mission pages, which beat the character page. Camp Events: scripts/v3/sources/Camp_Events.txt.
- Save any other source you fetch (newspapers, letters, interviews, guide pages) in scripts/v3/work/rains/fc/ with a clear name.
- Current live fiche: characters/rains-fall/index.html and fr/personnages/rains-fall/index.html (v2 data in
  scripts/_enrich.py ENRICHED entry or a scripts/_waveN.py entry for "rains-fall", if any: reuse its verified real-world sources).
- Fact-checked fiches whose facts are AUTHORITATIVE: scripts/fiches/parts/<prefix>_[A-F].py for prefix in
  {abigail,allende,andrew,angelo,arthur,bill,bonnie,catherine,charles,colm,desanta,dutch,edgar,fordham,fussar,hosea,irish,jack,javier,john,josiah,karen,kieran,landon,leigh,lenny,leopold,leviticus,linton,luisa,macdougal,mary,micah,molly,nastas,nigel,orville,reyes,sadie,sean,seth,simon,susan,tavish,tilly,uncle}. Search them for "Rains" to stay consistent.
- Story guides: story/*/index.html. Live slugs (only these may be linked with [[slug|Name]]): scripts/v3/work/rains/live_slugs.txt.
  Never link rains-fall itself.
- WebSearch/WebFetch allowed for real-world sources (actor per credits/Wikipedia, dated interviews, Rockstar THR
  descriptions of 6 Sep 2018 at scripts/v3/sources/thr_descriptions.txt, official guides, reviews). Name outlet + date.

RDR2 only, chapters 4 to 6 + epilogue mentions. Chief of the Wapiti, father of Eagle Flies. Missions with Charles/Arthur: Fleeting Joy? Verify every mission name from the wiki and transcripts (Charles side missions, 'The Noblest of Men, and a Woman', 'Archeology for Beginners'? etc.). HOUSE FACTS: Eagle Flies dies at the reservation (chapter 6), Charles carries/fights alongside; c'est Taima qui sert a la fuite (Charles fiche). Epilogue: what happens to the Wapiti (Canada?) must be sourced (Charles's 1907 lines). Actor: Graham Greene (Oneida, died September 1, 2025, Toronto, age 73 - verify). The fiche is QUEUED (publishDate 2026-10-23): links only to fiches live on or before 2026-10-23 (NOT eagle-flies 10-26, NOT sister-calderon). Authoritative related parts: charles_*, arthur_*, dutch_*, sadie_*, micah_*, john_*. Full fan transcript: copy scripts/v3/work/fussar/fc/gsw.txt to work/rains/fc/ (gitignored).

Chapter keys: RDR2 1-6, "E1", "E2"; RDR1 "A1", "A2", "A3".

Hard rules: no em/en dashes; never copy the wiki's sentences; FR written natively; quotation marks only around
words verified in a transcript/quote page; no speculation; one fact per sentence; no AI-poetic prose; no « » in
h3/h4; US spelling in EN; no outfit catalogue (2-3 sentence appearance at most); each fact in ONE place.
Validate with python3 -c "import ast;ast.parse(open(PATH).read())". Reply with EN/FR word counts and excluded facts.
