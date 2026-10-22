# Lead decisions for Eagle Flies (binding for checkers and fixer)

1. Publishes 2026-10-26 via _queue/49-eagle-flies. Links: live fiches + rains-fall (published 2026-10-23; a BROKEN warning for /characters/rains-fall/ before that date is expected). Never sister-calderon.
2. Arrival at Beaver Hollow ("A Rage Unleashed"): Karen and Javier escort him in (mission page, house fact); Charles introduces him to Arthur and Dutch ("Pardon me for interrupting. I've brought a friend, Arthur." transcript). Both, once.
3. Dies in his father's tent on the reservation ("in his father's arms" = wiki, attributed). Fort Wallace: Taima, Eagle Flies behind Charles. Charles told Rains Fall he would not fight over some horses.
4. 1907 grave: Red Dead Wiki only, attributed; west (EN wiki) vs east (FR wiki) of Donner Falls given once.
5. Oil-well explosion: who sets it off is wiki-only, attributed.
6. Quote ownership: lines quoted in B are not repeated in C (cut from C). "Father has confused wisdom with weakness..." goes in B In his own words if not already quoted anywhere.
7. Personality: cut to ~450 words (drop "He's a vile man..." first and fix the Favours pointer).
8. Scope: edit only eagle_* parts and scripts/fiches/eagle_flies.py; report cross-fiche errors. Never stage characters/eagle-flies or fr/personnages/eagle-flies (local build artefacts).
9. Paytah does NOT board the boat (transcript: "Paytah: Good luck." as they reach the steamboat). Arthur blows up the anchor mechanism on Dutch's order.
10. Cross-fiche (this fixer applies, EN+FR, minimal): charles_B l.152 Paytah "boards the army boat" -> he stays behind; charles_A l.80 "into the Van Horn lighthouse" -> the steamboat runs onto the rocks (transcript); the lighthouse may be mentioned only as the Red Dead Wiki's location. Then rebuild Charles with python3 scripts/_enrich.py charles-smith.
