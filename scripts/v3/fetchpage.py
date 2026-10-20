#!/usr/bin/env python3
"""fetchpage.py "<Wiki title>" ["<Wiki title>/dialogues" ...] -> shared cache work/_m/ (skips pages already cached).

For agents who need a page that setup did not fetch (a mission outside "Mission appearances", a newspaper,
a letter, Camp Events is already in scripts/v3/sources/). Prints the cache path or MISSING.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _paths import fetch_cached, rel
if len(sys.argv) < 2:
    raise SystemExit(__doc__)
for t in sys.argv[1:]:
    f = fetch_cached(t)
    print(t, '->', rel(f) if f else 'MISSING')
