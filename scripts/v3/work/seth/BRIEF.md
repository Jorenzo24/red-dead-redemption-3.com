# Seth Briars v3 fiche (MEDIUM tier): shared brief for drafting agents

Repo root on this device: /Users/joseph/Documents/SITES/GIT/red-dead-redemption-3.com/ (all paths below are relative to it)
Work dir: scripts/v3/work/seth/   Shared cache of mission pages and transcripts: scripts/v3/work/_m/

READ FIRST: scripts/fiches/SPEC.md (binding rules), scripts/v3/rules/OWNERSHIP.md (each fact in ONE place) and
scripts/v3/rules/HOUSE_FACTS.md (shared-event decisions already settled on other fiches: never contradict them).
Model files to imitate (structure, block formats, tone): scripts/fiches/parts/uncle_A.py, uncle_B.py,
uncle_C.py, uncle_D.py (fully fact-checked), and a recent medium fiche such as leviticus_A..D.py.
This is a MEDIUM fiche: same sections, shorter, no padding.
Target total EN length: at least the wiki page length (Seth Briars wiki EN is in scripts/v3/work/seth/en.txt), typically 3,000 to 5,000 words.

Sources available locally:
- Wiki page wikitext: scripts/v3/work/seth/en.txt (EN), scripts/v3/work/seth/fr.txt (FR wiki, may be missing: fetch it if needed).
- Mission pages and transcripts: scripts/v3/work/seth/missions.txt lists the pages of this character's "Mission appearances" and
  their file in scripts/v3/work/_m/ (`*_dialogues.txt` = transcripts). The cache is shared by every fiche: other missions may
  already be there (ls scripts/v3/work/_m/). Missing page: python3 scripts/v3/fetchpage.py "<Title>" "<Title>/dialogues".
  Transcripts beat mission pages, which beat the character page. Camp Events: scripts/v3/sources/Camp_Events.txt.
- Save any other source you fetch (newspapers, letters, interviews, guide pages) in scripts/v3/work/seth/fc/ with a clear name.
- Current live fiche: characters/seth-briars/index.html and fr/personnages/seth-briars/index.html (v2 data in
  scripts/_enrich.py ENRICHED entry or a scripts/_waveN.py entry for "seth-briars", if any: reuse its verified real-world sources).
- Fact-checked fiches whose facts are AUTHORITATIVE: scripts/fiches/parts/<prefix>_[A-F].py for prefix in
  {abigail,andrew,angelo,arthur,bill,bonnie,charles,colm,dutch,edgar,hosea,jack,javier,john,josiah,karen,kieran,landon,lenny,leopold,leviticus,linton,mary,micah,molly,nigel,orville,sadie,sean,simon,susan,tilly,uncle}. Search them for "Seth" to stay consistent.
- Story guides: story/*/index.html. Live slugs (only these may be linked with [[slug|Name]]): scripts/v3/work/seth/live_slugs.txt.
  Never link seth-briars itself.
- WebSearch/WebFetch allowed for real-world sources (actor per credits/Wikipedia, dated interviews, Rockstar THR
  descriptions of 6 Sep 2018 at scripts/v3/sources/thr_descriptions.txt, official guides, reviews). Name outlet + date.

Seth Briars: RDR1 Act I grave robber/treasure hunter (Tumbleweed, Coot's Chapel, Twin Rocks), joins the Fort Mercer assault (already inside the fort, dances on the wall: see HOUSE_FACTS), treasure map strand ends with the 'treasure' (verify what it is). Survives RDR1. Undead Nightmare appearance (non-canon) if any. Actor per credits (verify: Kevin Glikmann). No RDR2 role unless sourced (check for references).

Chapter keys: RDR2 1-6, "E1", "E2"; RDR1 "A1", "A2", "A3".

Hard rules: no em/en dashes; never copy the wiki's sentences; FR written natively; quotation marks only around
words verified in a transcript/quote page; no speculation; one fact per sentence; no AI-poetic prose; no « » in
h3/h4; US spelling in EN; no outfit catalogue (2-3 sentence appearance at most); each fact in ONE place.
Validate with python3 -c "import ast;ast.parse(open(PATH).read())". Reply with EN/FR word counts and excluded facts.
