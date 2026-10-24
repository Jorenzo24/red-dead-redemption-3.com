# Fact-check: v3 story guide RDR2 Chapter 1 (Colter)

You are an adversarial fact-checker. Repo root: /Users/joseph/Documents/SITES/GIT/red-dead-redemption-3.com/.
Read scripts/v3/story/SPEC.md and scripts/v3/rules/HOUSE_FACTS.md. Your chunk (lines Lnn) comes from the EN page
story/rdr2-chapter-1-colter/index.html (full text: scripts/v3/work/story-ch1/guide_full_en.txt). Check EVERY sentence:
- against the transcripts: scripts/v3/work/_m/<Mission>_dialogues.txt and scripts/v3/work/story-ch1/fc/gsw.txt (gitignored, never commit);
- against the mission pages scripts/v3/work/_m/{Outlaws_from_the_West,Enter_Pursued_by_a_Memory,Old_Friends,The_Aftermath_of_Genesis,Who_the_Hell_is_Leviticus_Cornwall,Eastward_Bound}.txt, Colter.txt, Blackwater_Massacre.txt, scripts/v3/sources/Camp_Events.txt;
- against our fact-checked fiches scripts/fiches/parts/*_A..D.py (consistency both ways).
Categories: WRONG, IMPRECISE, UNSUPPORTED (no source), MISQUOTE (not verbatim), SPECULATION, COPIED (too close to wiki wording),
DUPLICATE (told twice in the page), STYLE (mood prose, analysis, dashes, one sentence = several facts). Also check the
"Chapter 1 at a glance" table cells and every figure caption in your chunk.
Report errors you find in OUR FICHES too (file + sentence + source).
Write scripts/v3/work/story-ch1/fc_report<1|2>.md: title, sources used, short "Verified OK", then "## Problems" numbered
(category, excerpt with Lnn, source says (file/line), fix), then counts per category. Run no git commands. Reply with counts.
