#!/usr/bin/env python3
"""split2.py <key> -> work/<key>/half1.txt (intro to Relationships) and half2.txt (Relationships to the end).

Medium tier: 2 fact-checkers. Run after assemble.py (needs <key>_full_en.txt); removes the check1-4.txt chunks.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _paths import kdir
if len(sys.argv) < 2:
    raise SystemExit(__doc__)
key = sys.argv[1]; D = kdir(key)
L = open(f'{D}{key}_full_en.txt', encoding='utf-8').read().split('\n')
i = next(k for k, l in enumerate(L) if l.strip() == 'Relationships')
for f in ('check1.txt', 'check2.txt', 'check3.txt', 'check4.txt'):
    if os.path.exists(D + f):
        os.remove(D + f)
open(D + 'half1.txt', 'w', encoding='utf-8').write('\n'.join(L[:i])); open(D + 'half2.txt', 'w', encoding='utf-8').write('\n'.join(L[i:]))
print(key, len(' '.join(L[:i]).split()), len(' '.join(L[i:]).split()))
