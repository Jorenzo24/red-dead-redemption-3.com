# {{NAME}} v3 fiche (MEDIUM tier): shared brief for drafting agents

Repo root on this device: {{R}} (all paths below are relative to it)
Work dir: {{KD}}/   Shared cache of mission pages and transcripts: {{M}}/

READ FIRST: scripts/fiches/SPEC.md (binding rules), {{RULES}}/OWNERSHIP.md (each fact in ONE place) and
{{RULES}}/HOUSE_FACTS.md (shared-event decisions already settled on other fiches: never contradict them).
Model files to imitate (structure, block formats, tone): scripts/fiches/parts/{{MODEL}}_A.py, {{MODEL}}_B.py,
{{MODEL}}_C.py, {{MODEL}}_D.py (fully fact-checked), and a recent medium fiche such as leviticus_A..D.py.
This is a MEDIUM fiche: same sections, shorter, no padding.
Target total EN length: at least the wiki page length ({{TITLE}} wiki EN is in {{KD}}/en.txt), typically 3,000 to 5,000 words.

Sources available locally:
- Wiki page wikitext: {{KD}}/en.txt (EN), {{KD}}/fr.txt (FR wiki, may be missing: fetch it if needed).
- Mission pages and transcripts: {{KD}}/missions.txt lists the pages of this character's "Mission appearances" and
  their file in {{M}}/ (`*_dialogues.txt` = transcripts). The cache is shared by every fiche: other missions may
  already be there (ls {{M}}/). Missing page: python3 scripts/v3/fetchpage.py "<Title>" "<Title>/dialogues".
  Transcripts beat mission pages, which beat the character page. Camp Events: {{SOURCES}}/Camp_Events.txt.
- Save any other source you fetch (newspapers, letters, interviews, guide pages) in {{KD}}/fc/ with a clear name.
- Current live fiche: characters/{{SLUG}}/index.html and fr/personnages/{{SLUG}}/index.html (v2 data in
  scripts/_enrich.py ENRICHED entry or a scripts/_waveN.py entry for "{{SLUG}}", if any: reuse its verified real-world sources).
- Fact-checked fiches whose facts are AUTHORITATIVE: scripts/fiches/parts/<prefix>_[A-F].py for prefix in
  {{AUTH}}. Search them for "{{FIRST}}" to stay consistent.
- Story guides: story/*/index.html. Live slugs (only these may be linked with [[slug|Name]]): {{KD}}/live_slugs.txt.
  Never link {{SLUG}} itself.
- WebSearch/WebFetch allowed for real-world sources (actor per credits/Wikipedia, dated interviews, Rockstar THR
  descriptions of 6 Sep 2018 at {{SOURCES}}/thr_descriptions.txt, official guides, reviews). Name outlet + date.

{{BLURB}}

Chapter keys: RDR2 1-6, "E1", "E2"; RDR1 "A1", "A2", "A3".

Hard rules: no em/en dashes; never copy the wiki's sentences; FR written natively; quotation marks only around
words verified in a transcript/quote page; no speculation; one fact per sentence; no AI-poetic prose; no « » in
h3/h4; US spelling in EN; no outfit catalogue (2-3 sentence appearance at most); each fact in ONE place.
Validate with python3 -c "import ast;ast.parse(open(PATH).read())". Reply with EN/FR word counts and excluded facts.
