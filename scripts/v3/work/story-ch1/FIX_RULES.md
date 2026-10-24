# Lead decisions for the v3 Chapter 1 guide (binding for the fixer)

1. scene-2.jpeg: Dutch holding a lantern in a snowstorm. Caption it plainly ("Dutch van der Linde with a lantern in the snowstorm, Chapter 1") without tying it to a specific mission.
2. Davey: carried in already dead on a stretcher by Bill and Arthur; Abigail walks in first and says "Davey's dead." Say it once.
3. Timing: Arthur's journal says "running for weeks"; give the journal line, no "a few days after"; April/May dates only if attributed (dutch_A / wiki).
4. Where two transcripts disagree (number of Javier's shots, "from"/"other side of town"), keep it vague or give the line one way without a precise detail.
5. "Chapter overview" (not "pause menu").
6. Heidi McCourt: name attributed to the Red Dead Wiki, once.
7. Fiche fixes (the fixer applies, EN+FR, minimal, ast check, then python3 scripts/_enrich.py <slug> for each fiche touched):
   - dutch_A.py:90 "Colm will be furious" -> his line is "Colm is going to shit his pants!" (paraphrase as: he shouts that Colm will be terrified / quote exactly).
   - arthur_A.py and dutch_A.py: "Heidi McCourt" stated as fact -> attribute the name to the Red Dead Wiki.
   - micah_A.py: burial of Jake Adler by Micah -> attribute to the Red Dead Wiki's Jake Adler page.
   - lenny_A.py:88: add the engineer variant (if Lenny is ahead, the engineer goes for Lenny), attributed to the mission page.
   - rains_A.py:79 and rains_C.py:58: "he saw him" -> Rains Fall says "We saw you" (rains-fall is live: rebuild it).
   - kieran_A.py:63: Dutch's actual line ("now all we'll get is lies") instead of "a beating would only produce lies".
8. Coverage adds: all CONFIRMED story items (priority: the Eastward Bound final scene after the "Chapter II" title card; Kieran struck by Colm and his horse Branwen; the full "Colm can wait..." line; Dutch's third option for the train employees; Hosea's "dying" line in the mission text so Trivia can point to it). WIKI-ONLY rewards/trophies/items: compact, one "Rewards" sentence per mission or in the table, attributed. Camp events: complete the Colter list concisely (one sentence each). Newspaper issue numbers for the "Train Robbed" articles: yes. No walkthrough minutiae, no Gold Medal tips, nothing from the "never add" rows.
9. Duplicates: apply the coverage report's section 3 (delete L116; Micah ferry quote once; Rains Fall identification once; trim L112).
