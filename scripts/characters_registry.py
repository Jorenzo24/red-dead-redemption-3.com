#!/usr/bin/env python3
"""Single source of truth for the Characters listing pages.

Drives scripts/gen_listing.py: which characters exist, how they're grouped, and
the card label per language. Add new characters here (matching the fiche slug);
gen_listing renders only those whose fiche is actually published (live dir exists).
"""

# (slug, name, role_en, role_fr, group)
CHARACTERS = [
    # --- The Van der Linde gang ---
    ("arthur-morgan",       "Arthur Morgan",       "Van der Linde gang &middot; RDR2",       "Gang Van der Linde &middot; RDR2",       "gang"),
    ("dutch-van-der-linde", "Dutch van der Linde", "Gang leader &middot; RDR1 &amp; 2",      "Chef de gang &middot; RDR1 &amp; 2",     "gang"),
    ("hosea-matthews",      "Hosea Matthews",      "Gang co-founder &middot; RDR2",          "Cofondateur du gang &middot; RDR2",      "gang"),
    ("micah-bell",          "Micah Bell",          "Main antagonist &middot; RDR2",          "Antagoniste principal &middot; RDR2",    "gang"),
    ("sadie-adler",         "Sadie Adler",         "Bounty hunter &middot; RDR2",            "Chasseuse de primes &middot; RDR2",      "gang"),
    ("bill-williamson",     "Bill Williamson",     "Outlaw &middot; RDR1 &amp; 2",           "Hors-la-loi &middot; RDR1 &amp; 2",      "gang"),
    ("charles-smith",       "Charles Smith",       "Tracker &middot; RDR2",                  "Pisteur &middot; RDR2",                  "gang"),
    ("javier-escuella",     "Javier Escuella",     "Van der Linde gang &middot; RDR1 &amp; 2","Gang Van der Linde &middot; RDR1 &amp; 2","gang"),
    ("lenny-summers",       "Lenny Summers",       "Van der Linde gang &middot; RDR2",       "Gang Van der Linde &middot; RDR2",       "gang"),
    ("sean-macguire",       "Sean MacGuire",       "Van der Linde gang &middot; RDR2",       "Gang Van der Linde &middot; RDR2",       "gang"),
    ("kieran-duffy",        "Kieran Duffy",        "Van der Linde gang &middot; RDR2",       "Gang Van der Linde &middot; RDR2",       "gang"),
    ("leopold-strauss",     "Leopold Strauss",     "Van der Linde gang &middot; RDR2",       "Gang Van der Linde &middot; RDR2",       "gang"),
    ("susan-grimshaw",      "Susan Grimshaw",      "Van der Linde gang &middot; RDR2",       "Gang Van der Linde &middot; RDR2",       "gang"),
    ("josiah-trelawny",     "Josiah Trelawny",     "Van der Linde gang &middot; RDR2",       "Gang Van der Linde &middot; RDR2",       "gang"),
    ("molly-oshea",         "Molly O'Shea",        "Van der Linde gang &middot; RDR2",       "Gang Van der Linde &middot; RDR2",       "gang"),
    ("uncle",               "Uncle",               "Van der Linde gang &middot; RDR1 &amp; 2","Gang Van der Linde &middot; RDR1 &amp; 2","gang"),
    # --- The Marston family ---
    ("john-marston",        "John Marston",        "Van der Linde gang &middot; RDR1",       "Gang Van der Linde &middot; RDR1",       "marston"),
    ("abigail-marston",     "Abigail Marston",     "Marston family &middot; RDR1 &amp; 2",   "Famille Marston &middot; RDR1 &amp; 2",  "marston"),
    ("jack-marston",        "Jack Marston",        "Marston family &middot; RDR1 &amp; 2",   "Famille Marston &middot; RDR1 &amp; 2",  "marston"),
    # --- Rivals & the law ---
    ("colm-odriscoll",      "Colm O'Driscoll",     "O'Driscoll Boys &middot; RDR2",          "Gang O'Driscoll &middot; RDR2",          "enemies"),
    ("angelo-bronte",       "Angelo Bronte",       "Crime lord &middot; RDR2",               "Chef de la pègre &middot; RDR2",         "enemies"),
    ("leviticus-cornwall",  "Leviticus Cornwall",  "Industrialist &middot; RDR2",            "Industriel &middot; RDR2",               "enemies"),
    ("andrew-milton",       "Andrew Milton",       "Pinkerton agent &middot; RDR2",          "Agent Pinkerton &middot; RDR2",          "enemies"),
    ("edgar-ross",          "Edgar Ross",          "Antagonist &middot; RDR1",               "Antagoniste &middot; RDR1",              "enemies"),
    # --- Other figures ---
    ("mary-linton",         "Mary Linton",         "Arthur's former love &middot; RDR2",     "Ancien amour d'Arthur &middot; RDR2",    "other"),
]

# group key -> (title_en, title_fr, note_en, note_fr)
GROUPS = [
    ("gang", "The Van der Linde gang", "Le gang Van der Linde",
     "Dutch van der Linde's outlaws and the people who rode, cooked and schemed alongside them.",
     "Les hors-la-loi de Dutch van der Linde et celles et ceux qui chevauchaient, cuisinaient et manigançaient à leurs côtés."),
    ("marston", "The Marston family", "La famille Marston",
     "John, Abigail and Jack, the family at the heart of both Red Dead Redemption games.",
     "John, Abigail et Jack, la famille au cœur des deux Red Dead Redemption."),
    ("enemies", "Rivals &amp; the law", "Rivaux et forces de l'ordre",
     "The rival gangs, industrialists and lawmen hunting the Van der Lindes across the West.",
     "Les gangs rivaux, industriels et représentants de la loi qui traquent les Van der Linde à travers l'Ouest."),
    ("other", "Other figures", "Autres figures",
     "Figures from beyond the gang whose lives cross the Red Dead story.",
     "Des figures extérieures au gang dont la vie croise l'histoire de Red Dead."),
]
