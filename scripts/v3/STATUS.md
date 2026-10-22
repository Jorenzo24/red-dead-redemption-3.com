# v3 fiches: status (read this first in any new session, keep it up to date at the end of every step)

Last update: 2026-10-22. Counter: run `python3 scripts/v3/counter.py` (done = build( entries in _FULL of
scripts/_enrich.py; total = characters/*/ folders + _queue/ items).

**Counter: 48 done / 50 total, 2 remaining.**

## In progress (one line per fiche: key, step, device, WIP branch)
| Fiche | key | Step | Where | WIP branch |
|---|---|---|---|---|
| Eagle Flies | eagle | gallery+modules done, drafting (queued 2026-10-26: final build writes _queue/49-eagle-flies) | Mac session | wip/v3-eagle-calderon |
| Sister Calderón | calderon | gallery+modules done, drafting (queued 2026-10-29; wiki page = "Mother Superior Calderón") | Mac session | wip/v3-eagle-calderon |

A fiche listed here with a WIP branch can be resumed from any device: check out the branch first.

## Done (48, in _FULL order)
Full tier: John Marston, Arthur Morgan, Dutch van der Linde, Sadie Adler, Micah Bell, Hosea Matthews, Charles Smith,
Bill Williamson, Javier Escuella, Abigail Marston, Jack Marston, Uncle.
Medium tier, gang: Sean MacGuire, Lenny Summers, Kieran Duffy, Susan Grimshaw, Karen Jones, Tilly Jackson,
Simon Pearson, Mary-Beth Gaskill, Orville Swanson, Leopold Strauss, Molly O'Shea, Josiah Trelawny.
Medium tier, outside the gang: Colm O'Driscoll, Edgar Ross, Andrew Milton, Leviticus Cornwall, Mary Linton, Angelo Bronte, Bonnie MacFarlane, Landon Ricketts, Nigel West Dickens, Seth Briars, Leigh Johnson, Abraham Reyes, Agustin Allende, Vincente de Santa, Luisa Fortuna, Irish, Nastas, Harold MacDougal, Archer Fordham, Catherine Braithwaite, Tavish Gray, Alberto Fussar, Hercule Fontaine, Rains Fall (v3 written into its _queue item, published by the drip on 2026-10-23).

## Remaining (2)
Queued in _queue/, not published yet: eagle-flies (2026-10-26), sister-calderon (2026-10-29).
They can be done NOW: `python3 scripts/_enrich.py <slug>` rewrites the fiche's _queue/NN-<slug>/ en.html + fr.html when the
fiche is not live yet (never creates characters/<slug>/), so the drip publishes the v3 version on its date. For the
assemble/coverage steps, build a local copy first (mkdir + touch characters/<slug>/index.html and fr/personnages/<slug>/index.html,
run assemble.py, never stage those two files, delete them before the final `_enrich.py <slug>`).
