#!/usr/bin/env python3
"""Build mission pages from the data modules in scripts/missions/.

    python3 scripts/build_missions.py              # every mission
    python3 scripts/build_missions.py <slug> ...   # only these slugs

Two passes: [[m:<slug>|...]] tokens and the prev/next links only link pages that
already exist, so a second pass lets missions built in the same run link each
other. When building a subset, the missions they point to (prev/next) are
rebuilt too, so their own links to the new page appear.
The Story hub (/story/ + /fr/histoire/) is regenerated at the end, so new
mission pages appear in their chapter's accordion.
"""
import importlib, os, pkgutil, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import gen_mission
import missions


def load_all():
    out = {}
    for info in pkgutil.iter_modules(missions.__path__):
        mod = importlib.import_module(f"missions.{info.name}")
        m = getattr(mod, "MISSION", None)
        if m:
            m = dict(m, _module=info.name)
            out[m["slug"]] = m
    return out


def main(argv):
    allm = load_all()
    wanted = argv or sorted(allm)
    unknown = [s for s in wanted if s not in allm]
    if unknown:
        raise SystemExit(f"ERROR: no mission module for {', '.join(unknown)}")
    todo = list(wanted)
    if argv:  # neighbours of the requested pages get their links refreshed too
        for s in wanted:
            for k in ("prev", "next"):
                ref = allm[s].get(k)
                if ref and ref["slug"] in allm and ref["slug"] not in todo:
                    todo.append(ref["slug"])
    for _pass in (1, 2):
        for s in todo:
            paths = gen_mission.build(allm[s])
            if _pass == 2:
                print("built", s, "->", ", ".join(paths))
    import gen_story_hub
    gen_story_hub.main()


if __name__ == "__main__":
    main(sys.argv[1:])
