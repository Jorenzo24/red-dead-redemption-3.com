# v3 fiches: status (read this first in any new session, keep it up to date at the end of every step)

Last update: 2026-10-20. Counter: run `python3 scripts/v3/counter.py` (done = build( entries in _FULL of
scripts/_enrich.py; total = characters/*/ folders + _queue/ items).

**Counter: 28 done / 50 total, 22 remaining (2 of them in progress).**

## In progress (one line per fiche: key, step, device, WIP branch)
| Fiche | key | Step | Where | WIP branch |
|---|---|---|---|---|
| Angelo Bronte | angelo | drafting (parts A and C written so far); gallery built (8 images in assets/, module scripts/fiches/angelo_bronte.py) | local Mac session, old scratchpad pipeline | none yet: NOT pushed |
| Mary Linton | linton | drafted (parts A..D), being assembled (wired into _enrich.py locally, uncommitted); gallery built (4 images in assets/, module scripts/fiches/mary_linton.py) | local Mac session, old scratchpad pipeline | none yet: NOT pushed |

Do not start either of these from another device until they are pushed to a `wip/v3-<key>` branch (or merged).

## Done (28, in _FULL order)
Full tier: John Marston, Arthur Morgan, Dutch van der Linde, Sadie Adler, Micah Bell, Hosea Matthews, Charles Smith,
Bill Williamson, Javier Escuella, Abigail Marston, Jack Marston, Uncle.
Medium tier, gang: Sean MacGuire, Lenny Summers, Kieran Duffy, Susan Grimshaw, Karen Jones, Tilly Jackson,
Simon Pearson, Mary-Beth Gaskill, Orville Swanson, Leopold Strauss, Molly O'Shea, Josiah Trelawny.
Medium tier, outside the gang: Colm O'Driscoll, Edgar Ross, Andrew Milton, Leviticus Cornwall.

## Remaining (22)
Live, not v3 yet (19): abraham-reyes, agustin-allende, alberto-fussar, angelo-bronte (in progress), archer-fordham,
bonnie-macfarlane, catherine-braithwaite, harold-macdougal, hercule-fontaine, irish, landon-ricketts, leigh-johnson,
luisa-fortuna, mary-linton (in progress), nastas, nigel-west-dickens, seth-briars, tavish-gray, vincente-de-santa.
Queued in _queue/, not published yet (3): rains-fall, eagle-flies, sister-calderon. Do them after the drip has published them
(the v3 rebuild regenerates characters/<slug>/ through _enrich.py), never publish them early.

Notes: Nastas and Fordham need re-checking (claims without a source, see CLAUDE.md). Pick the next fiche with
`python3 scripts/v3/counter.py` and write it in the table above BEFORE starting.
