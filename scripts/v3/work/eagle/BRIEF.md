# Eagle Flies v3 fiche (MEDIUM tier): shared brief for drafting agents

Repo root on this device: /Users/joseph/Documents/SITES/GIT/red-dead-redemption-3.com/ (all paths below are relative to it)
Work dir: scripts/v3/work/eagle/   Shared cache of mission pages and transcripts: scripts/v3/work/_m/

READ FIRST: scripts/fiches/SPEC.md (binding rules), scripts/v3/rules/OWNERSHIP.md (each fact in ONE place) and
scripts/v3/rules/HOUSE_FACTS.md (shared-event decisions already settled on other fiches: never contradict them).
Model files to imitate (structure, block formats, tone): scripts/fiches/parts/uncle_A.py, uncle_B.py,
uncle_C.py, uncle_D.py (fully fact-checked), and a recent medium fiche such as leviticus_A..D.py.
This is a MEDIUM fiche: same sections, shorter, no padding.
Target total EN length: at least the wiki page length (Eagle Flies wiki EN is in scripts/v3/work/eagle/en.txt), typically 3,000 to 5,000 words.

Sources available locally:
- Wiki page wikitext: scripts/v3/work/eagle/en.txt (EN), scripts/v3/work/eagle/fr.txt (FR wiki, may be missing: fetch it if needed).
- Mission pages and transcripts: scripts/v3/work/eagle/missions.txt lists the pages of this character's "Mission appearances" and
  their file in scripts/v3/work/_m/ (`*_dialogues.txt` = transcripts). The cache is shared by every fiche: other missions may
  already be there (ls scripts/v3/work/_m/). Missing page: python3 scripts/v3/fetchpage.py "<Title>" "<Title>/dialogues".
  Transcripts beat mission pages, which beat the character page. Camp Events: scripts/v3/sources/Camp_Events.txt.
- Save any other source you fetch (newspapers, letters, interviews, guide pages) in scripts/v3/work/eagle/fc/ with a clear name.
- Current live fiche: characters/eagle-flies/index.html and fr/personnages/eagle-flies/index.html (v2 data in
  scripts/_enrich.py ENRICHED entry or a scripts/_waveN.py entry for "eagle-flies", if any: reuse its verified real-world sources).
- Fact-checked fiches whose facts are AUTHORITATIVE: scripts/fiches/parts/<prefix>_[A-F].py for prefix in
  {abigail,allende,andrew,angelo,arthur,bill,bonnie,catherine,charles,colm,desanta,dutch,edgar,fordham,fussar,hercule,hosea,irish,jack,javier,john,josiah,karen,kieran,landon,leigh,lenny,leopold,leviticus,linton,luisa,macdougal,mary,micah,molly,nastas,nigel,orville,rains,reyes,sadie,sean,seth,simon,susan,tavish,tilly,uncle}. Search them for "Eagle" to stay consistent.
- Story guides: story/*/index.html. Live slugs (only these may be linked with [[slug|Name]]): scripts/v3/work/eagle/live_slugs.txt.
  Never link eagle-flies itself.
- WebSearch/WebFetch allowed for real-world sources (actor per credits/Wikipedia, dated interviews, Rockstar THR
  descriptions of 6 Sep 2018 at scripts/v3/sources/thr_descriptions.txt, official guides, reviews). Name outlet + date.

RDR2 only, chapter 6 (+ epilogue grave?). Son of Rains Fall, Wapiti warrior. HOUSE FACTS: Eagle Flies dies in his father's tent on the reservation (My Last Boy); at the Fort Wallace escape it is Taima, with Eagle Flies seated behind Charles; Karen and Javier bring Eagle Flies to Beaver Hollow; Charles told Rains Fall he would not fight over some horses. Verify voice actor from a real source. QUEUED fiche, publishDate 2026-10-26: link only fiches live by then (rains-fall OK, NOT sister-calderon). Authoritative parts: rains_*, charles_*, arthur_*, dutch_*, micah_*. Full fan transcript: work/eagle/fc/gsw.txt (gitignored).

Chapter keys: RDR2 1-6, "E1", "E2"; RDR1 "A1", "A2", "A3".

Hard rules: no em/en dashes; never copy the wiki's sentences; FR written natively; quotation marks only around
words verified in a transcript/quote page; no speculation; one fact per sentence; no AI-poetic prose; no « » in
h3/h4; US spelling in EN; no outfit catalogue (2-3 sentence appearance at most); each fact in ONE place.
Validate with python3 -c "import ast;ast.parse(open(PATH).read())". Reply with EN/FR word counts and excluded facts.
