# Bonnie MacFarlane v3 fiche (MEDIUM tier): shared brief for drafting agents

Repo root on this device: /Users/joseph/Documents/SITES/GIT/red-dead-redemption-3.com/ (all paths below are relative to it)
Work dir: scripts/v3/work/bonnie/   Shared cache of mission pages and transcripts: scripts/v3/work/_m/

READ FIRST: scripts/fiches/SPEC.md (binding rules), scripts/v3/rules/OWNERSHIP.md (each fact in ONE place) and
scripts/v3/rules/HOUSE_FACTS.md (shared-event decisions already settled on other fiches: never contradict them).
Model files to imitate (structure, block formats, tone): scripts/fiches/parts/uncle_A.py, uncle_B.py,
uncle_C.py, uncle_D.py (fully fact-checked), and a recent medium fiche such as leviticus_A..D.py.
This is a MEDIUM fiche: same sections, shorter, no padding.
Target total EN length: at least the wiki page length (Bonnie MacFarlane wiki EN is in scripts/v3/work/bonnie/en.txt), typically 3,000 to 5,000 words.

Sources available locally:
- Wiki page wikitext: scripts/v3/work/bonnie/en.txt (EN), scripts/v3/work/bonnie/fr.txt (FR wiki, may be missing: fetch it if needed).
- Mission pages and transcripts: scripts/v3/work/bonnie/missions.txt lists the pages of this character's "Mission appearances" and
  their file in scripts/v3/work/_m/ (`*_dialogues.txt` = transcripts). The cache is shared by every fiche: other missions may
  already be there (ls scripts/v3/work/_m/). Missing page: python3 scripts/v3/fetchpage.py "<Title>" "<Title>/dialogues".
  Transcripts beat mission pages, which beat the character page. Camp Events: scripts/v3/sources/Camp_Events.txt.
- Save any other source you fetch (newspapers, letters, interviews, guide pages) in scripts/v3/work/bonnie/fc/ with a clear name.
- Current live fiche: characters/bonnie-macfarlane/index.html and fr/personnages/bonnie-macfarlane/index.html (v2 data in
  scripts/_enrich.py ENRICHED entry or a scripts/_waveN.py entry for "bonnie-macfarlane", if any: reuse its verified real-world sources).
- Fact-checked fiches whose facts are AUTHORITATIVE: scripts/fiches/parts/<prefix>_[A-F].py for prefix in
  {abigail,andrew,angelo,arthur,bill,charles,colm,dutch,edgar,hosea,jack,javier,john,josiah,karen,kieran,lenny,leopold,leviticus,linton,mary,micah,molly,orville,sadie,sean,simon,susan,tilly,uncle}. Search them for "Bonnie" to stay consistent.
- Story guides: story/*/index.html. Live slugs (only these may be linked with [[slug|Name]]): scripts/v3/work/bonnie/live_slugs.txt.
  Never link bonnie-macfarlane itself.
- WebSearch/WebFetch allowed for real-world sources (actor per credits/Wikipedia, dated interviews, Rockstar THR
  descriptions of 6 Sep 2018 at scripts/v3/sources/thr_descriptions.txt, official guides, reviews). Name outlet + date.

Bonnie MacFarlane: RDR1 (MacFarlane's Ranch, Hennigan's Stead, New Austin; Act I; kidnapped and nearly hanged by Walton's Gang in 'Hanging Bonnie MacFarlane'; nurses John after Bill shoots him) and RDR2 epilogue? NO: RDR2 has her only in 1907 epilogue? verify: in RDR2, Bonnie appears in the epilogue 'Old Friends, New Problems'? (house fact: Abigail meets Bonnie at her home in 'Old Friends, New Problems', corn delivery). Survives RDR1. Actress Anna Garduno? verify credits. Father Drew MacFarlane, brother Jimmy? verify.

Chapter keys: RDR2 1-6, "E1", "E2"; RDR1 "A1", "A2", "A3".

Hard rules: no em/en dashes; never copy the wiki's sentences; FR written natively; quotation marks only around
words verified in a transcript/quote page; no speculation; one fact per sentence; no AI-poetic prose; no « » in
h3/h4; US spelling in EN; no outfit catalogue (2-3 sentence appearance at most); each fact in ONE place.
Validate with python3 -c "import ast;ast.parse(open(PATH).read())". Reply with EN/FR word counts and excluded facts.
