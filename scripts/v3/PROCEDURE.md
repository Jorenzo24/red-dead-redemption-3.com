# v3 fiche pipeline, MEDIUM tier: step-by-step (works from any device / any Claude Code session)

Everything lives in the repo: tools in `scripts/v3/`, per-fiche work in `scripts/v3/work/<key>/`, shared mission
cache in `scripts/v3/work/_m/`, rules in `scripts/v3/rules/`, prompt templates in `scripts/v3/templates/prompts/`.
`scripts/` is never served (`.htaccess`: `RedirectMatch 404 ^/(scripts|_queue|...)` and `\.(md|py)$`).
`<key>` = the parts prefix (`scripts/fiches/parts/<key>_A.py`), always passed explicitly: Mary-Beth = `mary`,
Mary Linton = `linton`. Needs python3 + Pillow (`pip install pillow`) and network access to reddead.fandom.com.

## 0. Resume rules (READ FIRST, every session)
1. `git checkout main && git pull`, then read `scripts/v3/STATUS.md`.
2. If the fiche you continue has a `wip/v3-<key>` branch: `git fetch && git checkout wip/v3-<key> && git pull`, then
   `python3 scripts/v3/setup_medium.py <key>` (re-reads `work/<key>/setup.json`, re-fetches the gitignored cache and
   rewrites prompts with this device's paths). Gallery downloads are not committed: re-run `galfetch.py` if needed.
3. **Never work on the same fiche from two devices at once.** STATUS.md says who has it; claim it there (commit + push)
   before starting, release it when done.
4. **At the end of EVERY step below**: commit the parts + `scripts/v3/work/<key>/` (reports, briefs, FIX_RULES,
   captions.json, spec.txt) + any assets/module on the WIP branch, push it (`git push -u origin wip/v3-<key>`), and update
   the fiche's row in STATUS.md (step done, next step). Stage files explicitly, never `git add -A` (other fiches'
   uncommitted files may be in the tree).

## 1. Setup
```
git checkout -b wip/v3-<key> origin/main
python3 scripts/v3/setup_medium.py <key> <slug> "<Wiki page title>" "<blurb>" [--name "Display Name"] [--model uncle]
```
Blurb = 2-5 lines for the drafters: games, key missions, death, actor(s) to verify, known traps (see HOUSE_FACTS.md).
Creates `work/<key>/`: en.txt, fr.txt, missions.txt, live_slugs.txt, BRIEF.md, FC_PROMPT.md, FIX_RULES.md (skeleton),
prompts/*.txt (filled templates), assemble.py, setup.json. Mission pages + transcripts go to `work/_m/`.
Extra pages: `python3 scripts/v3/fetchpage.py "<Title>" "<Title>/dialogues"`.

## 2. Gallery
1. `python3 scripts/v3/galfetch.py <key> "<Wiki page title>"` -> `work/<key>/gal/contact.jpg` (numbered).
2. READ the contact sheet. Reject: cards, promo visuals with text/logos, unreadable interiors, the wrong person
   (check `prop=fileusage` when unsure). Image rights are checked by Joseph before publication.
3. `python3 scripts/v3/galbuild.py <key> <slug> '3:fill,7:fill,12:obj,...'` (chronological order) -> assets +
   `gal/review.jpg` (READ it: faces not cut) + `gal/spec.txt`.
4. Write `work/<key>/gal/captions.json`: `[["alt EN","alt FR","caption EN","caption FR"], ...]`, one per image, in order
   (outfits go here, not in the text; FR written natively).
5. `python3 scripts/v3/mkmodule.py <key> <module_name> "<Display Name>" [--model uncle]` -> `scripts/fiches/<module>.py`
   (build() copied from the model, `updated` = today). Rename section titles in it if the fiche needs it.
Commit + push (resume rule 4).

## 3. Drafting: 2 agents in parallel
- Agent 1 = parts A + C: prompt `work/<key>/prompts/1_drafter_AC.txt` (template `templates/prompts/1_drafter_AC.txt`).
- Agent 2 = parts B + D: prompt `work/<key>/prompts/2_drafter_BD.txt`.
Give each agent the whole prompt file content as its task. Check their replies (word counts, excluded facts),
validate with `python3 -c "import ast;ast.parse(open(PATH).read())"`. Commit + push.

## 4. Build, assemble, split
```
python3 scripts/v3/mkrel.py <key> <slug> <module_name> <alias>   # rel portraits + wiring into scripts/_enrich.py
python3 scripts/v3/work/<key>/assemble.py                         # rebuild EN+FR, checks, <key>_full_en.txt
python3 scripts/v3/split2.py <key>                                # half1.txt / half2.txt for the 2 fact-checkers
```
assemble must print 0 dashes, no BROKEN / MISSING, no heading guillemets. Commit + push.
mkrel appends to the single `_FULL = [...]` line of `scripts/_enrich.py`: two fiches on two branches conflict there;
resolve by keeping both entries (imports and build calls).

## 5. Verification: 3 agents in parallel
- Fact-checker 1: `prompts/3_factcheck.txt` with chunk `half1.txt`, report `fc_report1.md`.
- Fact-checker 2: same prompt with chunk `half2.txt`, report `fc_report2.md`.
- Coverage agent: `prompts/4_coverage.txt` -> `coverage_report.md`.
(The fact-check rules themselves are in `work/<key>/FC_PROMPT.md`, from `templates/FC_PROMPT.md`.) Commit + push.

## 6. Fix: 1 agent
1. The lead reads the 3 reports and writes the binding decisions for disputed points in `work/<key>/FIX_RULES.md`
   (one line each: which source wins). Check every shared event against `rules/HOUSE_FACTS.md`.
2. Fixer: `prompts/5_fixer.txt` (contains the standard decision list per report category).
3. Re-run `assemble.py`; re-read the fixer's "not applied" list and its cross-fiche errors; fix those other fiches /
   story guides too (EN + FR, regenerate). Commit + push.

## 7. Ship
1. Final rebuild: `python3 scripts/_enrich.py <slug>`; spot-check EN + FR pages in a browser if possible.
2. Add new shared-event decisions to `rules/HOUSE_FACTS.md`.
3. CLAUDE.md: add the fiche's entry under the matching v3 list (words EN, relations, gallery, corrections, errors fixed
   elsewhere), in the same style as the existing entries.
4. Branch + PR + merge, without asking (site has no traffic yet; a merge on main is live within ~15 min):
   `git checkout -b content/<key>-v3` (or reuse the WIP branch), stage files explicitly, commit, push,
   `gh pr create`, `gh pr merge --merge --delete-branch`. Delete the WIP branch. Commit footer:
   `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`; PR body ends with
   `🤖 Generated with [Claude Code](https://claude.com/claude-code)`.
5. STATUS.md: move the fiche to Done, update the counter (`python3 scripts/v3/counter.py`).
6. Report to Joseph with the progress counter: "v3: N done / T total, R remaining".

## House rules (apply to every published word)
- No em dashes or en dashes in published content (commas, colons, parentheses instead). Internal docs are exempt.
- Neutral, factual media tone: one sentence = one fact; no AI-poetic or mood prose, no cheap analysis or rhetorical
  analogies, no defensive tics. Cite outlet + date and figures when relevant, in the text, without outbound links.
- FR is written natively, never a literal translation of the EN (no calques); mission, item and place names stay in
  English as Rockstar publishes them ("Saint-Denis" in FR prose).
- No "Sources" section citing Fandom/Wikipedia: EEAT comes from the author byline + "Updated" date. The source
  register lives in the parts' docstrings only.
- Never « » in h1-h6: the Chinese Rock heading font has empty glyphs for them (straight quotes and curly quotes are fine).
- Never copy or closely paraphrase the wiki (CC BY-SA). Quotation marks only for verbatim, verified lines.
- No speculation; wiki-only game content attributed; real names/ages/dates only from sources.
- Verified changes are shipped live (PR + merge) without asking.
- Image rights are checked by Joseph; never hotlink.
- After each shipped v3 fiche: report the progress counter to Joseph.

## Files
| Path | What |
|---|---|
| `_paths.py` | repo-derived paths (R, W, M), wiki API, cache, live slugs, v3 done list |
| `setup_medium.py` | step 1 (idempotent, also the resume command) |
| `fetchpage.py` | fetch extra wiki pages into the shared cache |
| `galfetch.py`, `galbuild.py`, `mkmodule.py` | step 2 |
| `mkrel.py`, `split2.py`, `templates/assemble.py` | step 4 |
| `counter.py` | progress counter |
| `templates/BRIEF.md`, `templates/FC_PROMPT.md`, `templates/FIX_RULES.md`, `templates/prompts/*.txt` | filled by setup into `work/<key>/` (`{{PLACEHOLDERS}}`) |
| `rules/OWNERSHIP.md`, `rules/HOUSE_FACTS.md` | binding rules for every agent |
| `sources/Camp_Events.txt`, `sources/thr_descriptions.txt` | wiki Camp Events page; Rockstar descriptions (THR, 6 Sep 2018) |
| `work/<key>/` | committed on the WIP branch (reports, prompts, captions); `work/_m/` and `gal/` downloads are gitignored |

Full tier (12 majors, done): same steps with 4-6 drafters, 3-4 fact-checkers on `check1..4.txt` (assemble's thirds,
skip split2) and 4 fixers; see the CLAUDE.md entries for John, Arthur, Dutch.
