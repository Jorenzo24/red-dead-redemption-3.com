# Luisa Fortuna v3 fiche (MEDIUM tier): shared brief for drafting agents

Repo root on this device: /Users/joseph/Documents/SITES/GIT/red-dead-redemption-3.com/ (all paths below are relative to it)
Work dir: scripts/v3/work/luisa/   Shared cache of mission pages and transcripts: scripts/v3/work/_m/

READ FIRST: scripts/fiches/SPEC.md (binding rules), scripts/v3/rules/OWNERSHIP.md (each fact in ONE place) and
scripts/v3/rules/HOUSE_FACTS.md (shared-event decisions already settled on other fiches: never contradict them).
Model files to imitate (structure, block formats, tone): scripts/fiches/parts/uncle_A.py, uncle_B.py,
uncle_C.py, uncle_D.py (fully fact-checked), and a recent medium fiche such as leviticus_A..D.py.
This is a MEDIUM fiche: same sections, shorter, no padding.
Target total EN length: at least the wiki page length (Luisa Fortuna wiki EN is in scripts/v3/work/luisa/en.txt), typically 3,000 to 5,000 words.

Sources available locally:
- Wiki page wikitext: scripts/v3/work/luisa/en.txt (EN), scripts/v3/work/luisa/fr.txt (FR wiki, may be missing: fetch it if needed).
- Mission pages and transcripts: scripts/v3/work/luisa/missions.txt lists the pages of this character's "Mission appearances" and
  their file in scripts/v3/work/_m/ (`*_dialogues.txt` = transcripts). The cache is shared by every fiche: other missions may
  already be there (ls scripts/v3/work/_m/). Missing page: python3 scripts/v3/fetchpage.py "<Title>" "<Title>/dialogues".
  Transcripts beat mission pages, which beat the character page. Camp Events: scripts/v3/sources/Camp_Events.txt.
- Save any other source you fetch (newspapers, letters, interviews, guide pages) in scripts/v3/work/luisa/fc/ with a clear name.
- Current live fiche: characters/luisa-fortuna/index.html and fr/personnages/luisa-fortuna/index.html (v2 data in
  scripts/_enrich.py ENRICHED entry or a scripts/_waveN.py entry for "luisa-fortuna", if any: reuse its verified real-world sources).
- Fact-checked fiches whose facts are AUTHORITATIVE: scripts/fiches/parts/<prefix>_[A-F].py for prefix in
  {abigail,allende,andrew,angelo,arthur,bill,bonnie,charles,colm,desanta,dutch,edgar,hosea,jack,javier,john,josiah,karen,kieran,landon,leigh,lenny,leopold,leviticus,linton,mary,micah,molly,nigel,orville,reyes,sadie,sean,seth,simon,susan,tilly,uncle}. Search them for "Luisa" to stay consistent.
- Story guides: story/*/index.html. Live slugs (only these may be linked with [[slug|Name]]): scripts/v3/work/luisa/live_slugs.txt.
  Never link luisa-fortuna itself.
- WebSearch/WebFetch allowed for real-world sources (actor per credits/Wikipedia, dated interviews, Rockstar THR
  descriptions of 6 Sep 2018 at scripts/v3/sources/thr_descriptions.txt, official guides, reviews). Name outlet + date.

Luisa Fortuna: RDR1 Act II, young rebel in Chuparosa allied with Reyes (his lover); held in caves near El Matadero, freed by John and Ricketts (HOUSE_FACTS); dies at Escalera in 'An Appointed Time', shot by the soldiers guarding Reyes (HOUSE_FACTS), not at El Presidio. Family (Fortuna, brother Emilio? verify). Actress per credits (verify). Undead Nightmare if any.

Chapter keys: RDR2 1-6, "E1", "E2"; RDR1 "A1", "A2", "A3".

Hard rules: no em/en dashes; never copy the wiki's sentences; FR written natively; quotation marks only around
words verified in a transcript/quote page; no speculation; one fact per sentence; no AI-poetic prose; no « » in
h3/h4; US spelling in EN; no outfit catalogue (2-3 sentence appearance at most); each fact in ONE place.
Validate with python3 -c "import ast;ast.parse(open(PATH).read())". Reply with EN/FR word counts and excluded facts.
