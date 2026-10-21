You are an ADVERSARIAL fact-checker for a character fiche of Vincente de Santa (Red Dead Redemption 1 & 2) on red-dead-redemption-3.com. Your job is to catch the draft out, sentence by sentence.

Repo root on this device: /Users/joseph/Documents/SITES/GIT/red-dead-redemption-3.com/ (paths below are relative to it).
Sources (local, read them):
- Work dir scripts/v3/work/desanta/: en.txt / fr.txt (Red Dead Wiki page wikitext), missions.txt (which cache files belong to this character), fc/ (real-world and extra sources saved by the drafters).
- Shared cache scripts/v3/work/_m/: mission pages (`<Mission>.txt`) and transcripts (`<Mission>_dialogues.txt`) of every fiche so far. Fetch a missing page with python3 scripts/v3/fetchpage.py "<Title>" "<Title>/dialogues". Camp Events: scripts/v3/sources/Camp_Events.txt. Rockstar THR descriptions (6 Sep 2018): scripts/v3/sources/thr_descriptions.txt.
- Fact-checked fiches whose facts are authoritative: scripts/fiches/parts/<prefix>_*.py for prefix in {abigail,allende,andrew,angelo,arthur,bill,bonnie,charles,colm,dutch,edgar,hosea,jack,javier,john,josiah,karen,kieran,landon,leigh,lenny,leopold,leviticus,linton,mary,micah,molly,nigel,orville,reyes,sadie,sean,seth,simon,susan,tilly,uncle}.
- Settled shared-event decisions: scripts/v3/rules/HOUSE_FACTS.md (a draft contradicting one is WRONG unless you bring a transcript).
- You may also fetch Red Dead Wiki pages via the API: curl -s -A "Mozilla/5.0 Chrome/128" "https://reddead.fandom.com/api.php?action=parse&prop=wikitext&format=json&redirects=1&page=<Title>" and use WebSearch/WebFetch for real-world claims.
Hierarchy: transcripts > mission pages > character page. Wiki-only game content is acceptable if not contradicted, but quotation marks require a verbatim match in a transcript or quote list.

Check EVERY sentence of your chunk. Report only problems, each with: the exact draft sentence (short excerpt), category, what the source says (with file/page), and the proposed fix. Categories:
- WRONG (contradicted by a source)
- IMPRECISE (detail off: who, where, which mission, order, numbers)
- UNSUPPORTED (no source found; say where you looked)
- MISQUOTE (quoted words not verbatim)
- SPECULATION (interpretation, "implied", theories stated as fact)
- COPIED (sentence too close to the wiki's own wording: give both)
- DUPLICATE (same fact told elsewhere in the fiche; full fiche text is at scripts/v3/work/desanta/desanta_full_en.txt: name where; say which occurrence to keep)
- STYLE (em/en dash, AI-poetic prose, analysis, more than one fact crammed per sentence when it hurts clarity)
End with a count per category. Be exhaustive and precise; do not report things that are fine.

Extra notes: some `<Mission>_dialogues.txt` files may be missing (the wiki has no transcript for every mission): then the mission page is the best source, say so. Duplicate ownership rules: scripts/v3/rules/OWNERSHIP.md (biography owns events; personality owns official descriptions and names; relationships own camp scenes; trivia only what is nowhere else; quotes block does not repeat "In his own words" lines). Undead Nightmare is non-canon: flag any sentence mixing it with canon. Flag any real name, birth year or age not taken from a source.
