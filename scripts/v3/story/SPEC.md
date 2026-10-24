# v3 story guides: spec (pilot = RDR2 Chapter 1: Colter, 24 Oct 2026)

Same standard as the v3 fiches: the Red Dead Wiki is the structural base (here: the chapter's MISSION pages + their
/dialogues transcripts, the "Missions in Redemption 2" chapter section, the location page, Camp Events), we cover
everything it says that is not speculation, rewritten in our own structure, never copied; then add (full fan transcript
gsw.txt, official guide facts already in our fiches, real-world sources only when relevant). Then 2 adversarial
fact-checks + coverage check + fixer, like the fiches.

## Sources, in order of authority
1. Transcripts: work/_m/<Mission>_dialogues.txt (wiki) and work/<key>/fc/gsw.txt (full fan transcript; gitignored, never
   commit). Speaker labels trusted; stage directions only when a wiki page agrees.
2. Our v3 fiches (scripts/fiches/parts/*_A..D.py) and scripts/v3/rules/HOUSE_FACTS.md: they are fact-checked; the guide
   must NEVER contradict them. If you think a fiche is wrong, report it (file + sentence), do not diverge silently.
3. Wiki mission pages (work/_m/<Mission>.txt), Camp Events (scripts/v3/sources/Camp_Events.txt), location pages.
Wiki-only game content (gameplay, objectives, unlocks) may be stated with attribution when not contradicted. Never
interpretation, theories, "this foreshadows", fan readings.

## Page structure (h2 = section, h3 = mission). Keep the existing page shell (head, header, breadcrumb, hero figure,
byline, story nav, footer); rewrite only the article body. Update "Updated" byline + dateModified to today.
1. Lede: 2-3 factual sentences (which chapter, where, when, how many missions).
2. In-game chapter overview: the verbatim overview text (blockquote; FR: original EN in quotes + "Traduction : ...").
3. Background: what the game itself says about what came before (Blackwater), sourced to lines/documents.
4. Missions: one h3 per main mission, in game order (note alternative orders when the wiki says so). For each: who starts
   it and where; who takes part; the full story of the mission, event by event, one sentence = one fact; how it ends;
   player choices if any; 1-3 short verbatim lines max when they matter (EN; FR adds a translation in parentheses).
   Optional/side content of the chapter (camp events, chores, hunting requests, stranger missions available in the
   chapter) in its own h2 after the missions.
5. "Chapter 1 at a glance": a table (Mission | Started by | With | Location | Gold medal objectives (wiki, attributed in
   the table caption)).
6. Characters in this chapter: who appears, first appearances, links to fiches.
7. Trivia: non-speculative, attributed when wiki-only. No real-world filler.
8. Key events: the existing scannable bullet recap, updated.
Length: as long as the content requires; the whole set of the chapter's mission pages is the coverage base.

## Writing rules (CLAUDE.md, binding)
- Neutral media tone, one sentence = one fact, no mood/"poetic" prose, no analysis ("the game's frozen prologue",
  "the open world finally breathes" are banned), no em/en dashes anywhere, no « » in h1-h6, US spelling.
- FR written natively (not translated); mission and item names stay in English as Rockstar publishes them.
- Links: direct <a href="/characters/<slug>/"> (FR /fr/personnages/<slug>/), first mention per section at most; only
  fiches that are live (ls characters/). NO [[tokens]] (hand-written pages). Missions are not linked (no mission pages).
- No outbound links to sources; attribution in the text ("according to the Red Dead Wiki", "the mission page").
- Keep existing images/figures of the page; captions factual.
