# v3 fiches: status (read this first in any new session, keep it up to date at the end of every step)

Last update: 2026-10-22. Counter: run `python3 scripts/v3/counter.py` (done = build( entries in _FULL of
scripts/_enrich.py; total = characters/*/ folders + _queue/ items).

**Counter: 47 done / 50 total, 3 remaining.**

## In progress (one line per fiche: key, step, device, WIP branch)
| Fiche | key | Step | Where | WIP branch |
|---|---|---|---|---|
| Rains Fall | rains | FIXED, ready. Ship AFTER the drip publishes it (2026-10-23 09:00 UTC): delete local untracked characters/rains-fall + fr/personnages/rains-fall, merge origin/main into the WIP branch, run python3 scripts/_enrich.py rains-fall, add CLAUDE.md entry is already done, PR + merge | Mac session | wip/v3-hercule-rains |

A fiche listed here with a WIP branch can be resumed from any device: check out the branch first.

## Done (47, in _FULL order)
Full tier: John Marston, Arthur Morgan, Dutch van der Linde, Sadie Adler, Micah Bell, Hosea Matthews, Charles Smith,
Bill Williamson, Javier Escuella, Abigail Marston, Jack Marston, Uncle.
Medium tier, gang: Sean MacGuire, Lenny Summers, Kieran Duffy, Susan Grimshaw, Karen Jones, Tilly Jackson,
Simon Pearson, Mary-Beth Gaskill, Orville Swanson, Leopold Strauss, Molly O'Shea, Josiah Trelawny.
Medium tier, outside the gang: Colm O'Driscoll, Edgar Ross, Andrew Milton, Leviticus Cornwall, Mary Linton, Angelo Bronte, Bonnie MacFarlane, Landon Ricketts, Nigel West Dickens, Seth Briars, Leigh Johnson, Abraham Reyes, Agustin Allende, Vincente de Santa, Luisa Fortuna, Irish, Nastas, Harold MacDougal, Archer Fordham, Catherine Braithwaite, Tavish Gray, Alberto Fussar, Hercule Fontaine.

## Remaining (3)
Live, not v3 yet: none.
Queued in _queue/, not published yet (3): rains-fall, eagle-flies, sister-calderon. Do them after the drip has published them
(the v3 rebuild regenerates characters/<slug>/ through _enrich.py), never publish them early.

 Pick the next fiche with
`python3 scripts/v3/counter.py` and write it in the table above BEFORE starting.
