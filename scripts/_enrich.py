#!/usr/bin/env python3
"""Enriched rewrites of fiches that are ALREADY live. Run: python scripts/_enrich.py [slug ...]
Not deployed (scripts/ is excluded from .cpanel.yml).

Format (Oct 2026, pilot: Molly O'Shea): biography laid out chapter by chapter,
each chapter subheading carrying a "Chapter guide ->" link to its story guide;
one sentence = one fact; facts checked per character, contested points left out.
`updated` drives the byline date; `publishDate` is kept as first publication.
Each entry fully replaces the fiche's data from its original wave driver.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_fiche import build_live, reg

def two(en, fr): return {"en": en, "fr": fr}

CH = {  # (en guide slug, fr guide slug)
 1: ("rdr2-chapter-1-colter", "rdr2-chapitre-1-colter"),
 2: ("rdr2-chapter-2-horseshoe-overlook", "rdr2-chapitre-2-horseshoe-overlook"),
 3: ("rdr2-chapter-3-clemens-point", "rdr2-chapitre-3-clemens-point"),
 4: ("rdr2-chapter-4-saint-denis", "rdr2-chapitre-4-saint-denis"),
 5: ("rdr2-chapter-5-guarma", "rdr2-chapitre-5-guarma"),
 6: ("rdr2-chapter-6-beaver-hollow", "rdr2-chapitre-6-beaver-hollow"),
}

ENRICHED = [
# ============================ MOLLY O'SHEA ============================
# Fix vs the July version: she dies at Beaver Hollow ("That's Murfree Country"),
# not at Shady Belle. Left out: how/when she joined (no canon), the Karen fight
# (sources disagree on who hit whom), "wealthy family" as fact (her own claim).
{
 "slug": "molly-oshea", "name": "Molly O'Shea",
 "publishDate": "2026-07-13", "updated": "2026-10-05", "schema_game": "Red Dead Redemption 2",
 "reg_role_en": "Van der Linde gang &middot; RDR2", "reg_role_fr": "Gang Van der Linde &middot; RDR2",
 "gender": "Female", "death": "1899", "nationality": "Irish",
 "portrait_alt": two("Molly O'Shea in Red Dead Redemption 2", "Molly O'Shea dans Red Dead Redemption 2"),
 "eyebrow": two("Character &middot; Van der Linde gang", "Personnage &middot; Gang Van der Linde"),
 "meta_desc": two("Molly O'Shea: Dutch van der Linde's Irish companion in Red Dead Redemption 2. Biography chapter by chapter, her false confession at Beaver Hollow, and how Agent Milton later clears her.",
                  "Molly O'Shea : la compagne irlandaise de Dutch van der Linde dans Red Dead Redemption 2. Biographie chapitre par chapitre, son faux aveu à Beaver Hollow, et comment l'agent Milton la blanchit."),
 "og_desc": two("Dutch's companion from Dublin, shot after a false confession and later cleared by the Pinkertons themselves.",
                "La compagne dublinoise de Dutch, abattue après un faux aveu puis blanchie par les Pinkerton eux-mêmes."),
 "schema_desc": two("Irish companion of Dutch van der Linde and member of the Van der Linde gang in Red Dead Redemption 2.",
                    "Compagne irlandaise de Dutch van der Linde et membre du gang Van der Linde dans Red Dead Redemption 2."),
 "chips": [two("Died <strong>1899</strong>", "Morte en <strong>1899</strong>"), two("Deceased", "Décédée"),
           two("Van der Linde gang", "Gang Van der Linde"), two("Dutch's companion", "Compagne de Dutch")],
 "facts": [
   {"label": two("Origin","Origine"), "value": two("Dublin, Ireland","Dublin, Irlande")},
   {"label": two("Died","Mort"), "value": two("1899, Beaver Hollow","1899, Beaver Hollow")},
   {"label": two("Status","Statut"), "value": two("Deceased","Décédée")},
   {"label": two("Affiliation","Affiliation"), "value": two("Van der Linde gang","Gang Van der Linde")},
   {"label": two("Relationship","Relation"), "value": two("[[dutch-van-der-linde|Dutch van der Linde]] (companion)","[[dutch-van-der-linde|Dutch van der Linde]] (compagne)")},
   {"label": two("Voiced by","Voix"), "value": two("Penny O'Brien","Penny O'Brien")},
   {"label": two("Games","Jeux"), "value": two("Red Dead Redemption 2","Red Dead Redemption 2")},
 ],
 "intro": [
   two("Molly O'Shea is an Irish member of the Van der Linde gang in Red Dead Redemption 2, and the companion of [[dutch-van-der-linde|Dutch van der Linde]]. Rockstar describes her as \"a Dublin girl and the object of Dutch's affection, for now at least\".",
       "Molly O'Shea est une Irlandaise membre du gang Van der Linde dans Red Dead Redemption 2, et la compagne de [[dutch-van-der-linde|Dutch van der Linde]]. Rockstar la présente comme une jeune femme de Dublin, objet de l'affection de Dutch, \"pour le moment du moins\"."),
   two("She dies in 1899, shot by [[susan-grimshaw|Susan Grimshaw]] after falsely claiming to have informed the Pinkertons about the gang.",
       "Elle meurt en 1899, abattue par [[susan-grimshaw|Susan Grimshaw]] après avoir faussement affirmé avoir renseigné les Pinkerton sur le gang."),
 ],
 "sections": [
   {"summary": two("Biography","Biographie"), "open": True, "blocks": [
     {"h3": two("Background","Origines")},
     {"p": two("Molly comes from Dublin and has a working-class Dublin accent, like [[sean-macguire|Sean MacGuire]]. She says she comes from a wealthy family. She came to America in search of adventure and met Dutch before 1899. The game never says how or when she joined the gang.",
               "Molly vient de Dublin et parle avec l'accent populaire de la ville, comme [[sean-macguire|Sean MacGuire]]. Elle affirme être issue d'une famille aisée. Elle est venue en Amérique en quête d'aventure et a rencontré Dutch avant 1899. Le jeu ne dit jamais comment ni quand elle a rejoint le gang.")},
     {"h3": two("Chapter 1: Colter","Chapitre 1 : Colter"), "chapter": CH[1]},
     {"p": two("In \"Outlaws from the West\", Susan Grimshaw tells Dutch that \"Miss O'Shea\" will show him the way to his cabin.",
               "Dans \"Outlaws from the West\", Susan Grimshaw annonce à Dutch que \"Miss O'Shea\" va le conduire à sa cabane.")},
     {"h3": two("Chapter 2: Horseshoe Overlook","Chapitre 2 : Horseshoe Overlook"), "chapter": CH[2]},
     {"p": two("Molly spends most of her time in Dutch's tent. A poem she wrote, titled \"Uaibhreach\", can be read there; the word is Irish for pride or arrogance.",
               "Molly passe l'essentiel de son temps dans la tente de Dutch. On peut y lire un poème qu'elle a écrit, intitulé \"Uaibhreach\", mot irlandais qui signifie orgueil ou arrogance.")},
     {"p": two("When [[arthur-morgan|Arthur]] carries a drunken [[orville-swanson|Reverend Swanson]] back to camp in \"Who is Not Without Sin\", she remarks that she was wondering when he would show up.",
               "Quand [[arthur-morgan|Arthur]] ramène au camp un [[orville-swanson|révérend Swanson]] ivre, dans \"Who is Not Without Sin\", elle lance qu'elle se demandait quand il finirait par réapparaître.")},
     {"p": two("She does not join the women's trip to Valentine in \"Polite Society, Valentine Style\". When [[tilly-jackson|Tilly]] asks whether they should have invited her, [[karen-jones|Karen]] answers that Molly is \"far too high and mighty now\" and calls her \"a society lady\".",
               "Elle ne participe pas à la sortie des femmes à Valentine, dans \"Polite Society, Valentine Style\". Quand [[tilly-jackson|Tilly]] se demande s'il aurait fallu l'inviter, [[karen-jones|Karen]] répond que Molly est devenue bien trop hautaine et la traite de dame de la haute société.")},
     {"h3": two("Chapter 3: Clemens Point","Chapitre 3 : Clemens Point"), "chapter": CH[3]},
     {"p": two("In \"An Honest Mistake\", Molly starts to confide in Arthur about Dutch. [[uncle|Uncle]] interrupts them with a tip about a supply wagon.",
               "Dans \"An Honest Mistake\", Molly commence à se confier à Arthur au sujet de Dutch. [[uncle|Uncle]] les interrompt avec un tuyau sur un chariot de ravitaillement.")},
     {"p": two("In this chapter only, she can ask Arthur for a pocket mirror, which can be found at Martha's Swain in Ambarino. She gives him a cigar in return. The request is optional and can be missed.",
               "Dans ce chapitre uniquement, elle peut demander à Arthur un miroir de poche, à trouver à Martha's Swain, en Ambarino. Elle lui offre un cigare en échange. La demande est facultative et peut être manquée.")},
     {"h3": two("Chapter 4: Saint Denis","Chapitre 4 : Saint-Denis"), "chapter": CH[4]},
     {"p": two("At the Shady Belle camp, Molly shares the master bedroom with Dutch. In \"The Battle of Shady Belle\", she asks Dutch for a word and he answers \"Not now\". Riding off, Dutch tells Arthur he has \"far more important things to worry about right now than Molly O'Shea\".",
               "Au camp de Shady Belle, Molly partage la chambre principale avec Dutch. Dans \"The Battle of Shady Belle\", elle demande à lui parler et il répond \"Pas maintenant\". En partant à cheval, Dutch confie à Arthur qu'il a des soucis bien plus importants que Molly O'Shea.")},
   ]},
   {"summary": two("Death","Mort"), "blocks": [
     {"h3": two("That's Murfree Country","That's Murfree Country"), "chapter": CH[6]},
     {"p": two("After the gang returns from Guarma, it moves to a new camp at Beaver Hollow, in Roanoke Ridge. At the end of \"That's Murfree Country\", Uncle brings Molly back drunk; he says he found her in Saint Denis.",
               "Au retour de Guarma, le gang s'installe dans un nouveau camp à Beaver Hollow, dans le Roanoke Ridge. À la fin de \"That's Murfree Country\", Uncle ramène Molly ivre ; il dit l'avoir trouvée à Saint-Denis.")},
     {"p": two("In front of the camp, she claims she told the Pinkertons about the Saint Denis bank plan so that they would kill Dutch. Dutch draws his revolver, and Arthur tries to stop him. Susan Grimshaw shoots Molly in the stomach with a shotgun.",
               "Devant tout le camp, elle affirme avoir parlé aux Pinkerton du plan du braquage de Saint-Denis pour qu'ils tuent Dutch. Dutch sort son revolver, Arthur tente de l'arrêter. Susan Grimshaw abat Molly d'un coup de fusil dans le ventre.")},
     {"p": two("Grimshaw tells Arthur that Molly \"knew the rules\", and orders [[bill-williamson|Bill]] and [[simon-pearson|Pearson]] to burn the body. The scene is part of the main story.",
               "Grimshaw déclare à Arthur que Molly connaissait les règles, et ordonne à [[bill-williamson|Bill]] et à [[simon-pearson|Pearson]] de brûler le corps. La scène fait partie de l'histoire principale.")},
     {"h3": two("A false confession","Un faux aveu")},
     {"p": two("Her confession was false. In the mission \"Red Dead Redemption\", Pinkerton agent [[andrew-milton|Andrew Milton]] tells Arthur that they questioned Molly a couple of times, that she \"never talked\", and that they had to let her go. Milton names [[micah-bell|Micah Bell]] as the informant.",
               "Son aveu était faux. Dans la mission \"Red Dead Redemption\", l'agent Pinkerton [[andrew-milton|Andrew Milton]] apprend à Arthur qu'ils ont interrogé Molly à deux reprises, qu'elle n'a jamais rien dit et qu'ils ont dû la relâcher. Milton désigne [[micah-bell|Micah Bell]] comme l'informateur.")},
     {"p": two("In the final confrontation, Arthur tells Dutch that Micah is the rat: \"Not Molly, Dutch. Him.\"",
               "Lors de l'affrontement final, Arthur lance à Dutch que le traître est Micah, et non Molly.")},
   ]},
   {"summary": two("In the camp","Au camp"), "blocks": [
     {"ul": [
       two("She never does camp chores. Her line to Arthur: \"I'm nobody's servant girl, Mr. Morgan.\"",
           "Elle ne fait jamais les corvées du camp. Elle le dit à Arthur : elle n'est la servante de personne."),
       two("She never rides a horse and never joins Arthur on a mission.",
           "Elle ne monte jamais à cheval et n'accompagne jamais Arthur en mission."),
       two("She has red hair and wears a green corseted top with gold trim, a red skirt and white boots.",
           "Elle a les cheveux roux et porte un corsage vert à liserés dorés, une jupe rouge et des bottines blanches."),
       two("Tilly is the first to wonder whether Molly should have been invited to Valentine. After her death, Karen turns on Grimshaw.",
           "Tilly est la première à se demander s'il aurait fallu inviter Molly à Valentine. Après sa mort, Karen s'en prend à Grimshaw."),
     ]},
   ]},
   {"summary": two("Behind the scenes","Coulisses"), "blocks": [
     {"p": two("Molly O'Shea is played by Penny O'Brien, an Irish actress born in County Wicklow, who provided both the voice and the motion capture. A grave for Molly exists in the game files but is not used in the game.",
               "Molly O'Shea est interprétée par Penny O'Brien, actrice irlandaise née dans le comté de Wicklow, qui assure la voix et la capture de mouvement. Une tombe à son nom existe dans les fichiers du jeu, mais n'est pas utilisée.")},
   ]},
 ],
 "rel_after": 1,
 "relationships": [
   {"img": "dutch.jpeg", "slug": "dutch-van-der-linde", "name": "Dutch van der Linde", "text": two(
     "Her companion. He grows dismissive of her over the course of 1899.",
     "Son compagnon, de plus en plus distant avec elle au fil de 1899.")},
   {"img": "susan.jpeg", "slug": "susan-grimshaw", "name": "Susan Grimshaw", "text": two(
     "Shoots her at Beaver Hollow after her confession.",
     "L'abat à Beaver Hollow après son aveu.")},
   {"img": "arthur.jpeg", "slug": "arthur-morgan", "name": "Arthur Morgan", "text": two(
     "The one she starts to confide in, and the one who tries to save her.",
     "Celui à qui elle commence à se confier, et qui tente de la sauver.")},
   {"img": "karen.jpeg", "slug": "karen-jones", "name": "Karen Jones", "text": two(
     "Mocks her in chapter 2, then turns on Grimshaw after her death.",
     "Se moque d'elle au chapitre 2, puis s'en prend à Grimshaw après sa mort.")},
   {"img": "uncle.jpeg", "slug": "uncle", "name": "Uncle", "text": two(
     "Brings her back drunk from Saint Denis on the night she dies.",
     "La ramène ivre de Saint-Denis le soir de sa mort.")},
 ],
 "gallery": [
   {"img": "gallery-1.jpeg", "alt": two("Molly O'Shea at the camp","Molly O'Shea au camp"),
    "cap": two("Molly O'Shea at the gang's camp.","Molly O'Shea au camp du gang.")},
 ],
 "related": ["dutch-van-der-linde", "susan-grimshaw", "karen-jones", "arthur-morgan"],
},
]

if __name__ == "__main__":
    from characters_registry import CHARACTERS as REG
    for s, n, en, fr, _g in REG:
        reg(s, n, en, fr)
    only = set(sys.argv[1:])
    for c in ENRICHED:
        if only and c["slug"] not in only:
            continue
        print("rebuilt", build_live(c))
