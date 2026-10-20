#!/usr/bin/env python3
"""counter.py -> v3 progress: done (build( entries in _FULL of scripts/_enrich.py) / total (characters/*/ + _queue/).

Prints the counter line to report to Joseph after each shipped v3 fiche, then the remaining slugs.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _paths import v3_done, live_slugs, queue_slugs
done = [s for *_, s in v3_done()]
live, queue = live_slugs(), queue_slugs()
total = sorted(set(live) | set(queue))
rest = [s for s in total if s not in done]
print(f"v3: {len(done)} done / {len(total)} total ({len(live)} live + {len(queue)} queued), {len(rest)} remaining")
print("remaining live:", ", ".join(s for s in rest if s in live))
print("remaining queued:", ", ".join(s for s in rest if s not in live))
unknown = [s for s in done if s not in total]
if unknown:
    print("WARNING, done entries with no characters/ folder:", unknown)
