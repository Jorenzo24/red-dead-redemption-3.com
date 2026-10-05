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
     {"h3": two("Origins","Origines")},
     {"p": two("According to the game's official guide, Molly was born in Dublin to a wealthy family and came to America in search of excitement, where she met Dutch. The game itself never shows how or when she joined the gang.",
               "Selon le guide officiel du jeu, Molly est née à Dublin dans une famille aisée et a rejoint l'Amérique en quête d'aventure, où elle a rencontré Dutch. Le jeu ne montre jamais comment ni quand elle a intégré le gang.")},
     {"h3": two("Life in the gang","Au sein du gang")},
     {"p": two("Molly lives in Dutch's tent and refuses camp chores (\"I'm nobody's servant girl, Mr. Morgan\"). The other women resent her for it: during the outing in <a href=\"/story/rdr2-chapter-2-horseshoe-overlook/\">chapter 2</a>, [[karen-jones|Karen Jones]] calls her \"far too high and mighty\". A poem she wrote, titled \"Uaibhreach\" (Irish for pride), can be read in Dutch's tent.",
               "Molly vit dans la tente de Dutch et refuse les corvées du camp (\"je ne suis la servante de personne\", lance-t-elle à Arthur). Les autres femmes le lui reprochent : lors de la sortie du <a href=\"/fr/histoire/rdr2-chapitre-2-horseshoe-overlook/\">chapitre 2</a>, [[karen-jones|Karen Jones]] la juge devenue bien trop hautaine. Un poème de sa main, intitulé \"Uaibhreach\" (l'orgueil, en irlandais), se trouve dans la tente de Dutch.")},
     {"p": two("As Dutch's plans take over, he pays her less and less attention. From <a href=\"/story/rdr2-chapter-3-clemens-point/\">chapter 3</a> onwards, she tries to confide in [[arthur-morgan|Arthur]] about it.",
               "À mesure que ses plans l'accaparent, Dutch la délaisse. À partir du <a href=\"/fr/histoire/rdr2-chapitre-3-clemens-point/\">chapitre 3</a>, elle tente de s'en ouvrir à [[arthur-morgan|Arthur]].")},
     {"h3": two("False confession and death","Faux aveu et mort")},
     {"p": two("After the gang's return from Guarma, at the new camp at <a href=\"/story/rdr2-chapter-6-beaver-hollow/\">Beaver Hollow</a>, [[uncle|Uncle]] brings Molly back drunk from Saint Denis. In front of everyone, she claims she told the Pinkertons about the Saint Denis bank job so that they would kill Dutch. Dutch draws his revolver and Arthur tries to calm things down, but [[susan-grimshaw|Susan Grimshaw]] shoots her with a shotgun. Grimshaw says Molly \"knew the rules\" and has the body burned.",
               "Après le retour de Guarma, au nouveau camp de <a href=\"/fr/histoire/rdr2-chapitre-6-beaver-hollow/\">Beaver Hollow</a>, [[uncle|Uncle]] ramène Molly ivre de Saint-Denis. Devant tout le camp, elle affirme avoir renseigné les Pinkerton sur le braquage de Saint-Denis pour qu'ils tuent Dutch. Dutch dégaine, Arthur tente de calmer le jeu, mais [[susan-grimshaw|Susan Grimshaw]] l'abat d'un coup de fusil. Grimshaw explique que Molly connaissait les règles, et fait brûler le corps.")},
     {"p": two("The confession was false. Shortly before his death, Pinkerton agent [[andrew-milton|Andrew Milton]] tells Arthur that they questioned Molly and that she \"never talked\". The informant was [[micah-bell|Micah Bell]].",
               "L'aveu était faux. Peu avant sa mort, l'agent Pinkerton [[andrew-milton|Andrew Milton]] révèle à Arthur qu'ils ont interrogé Molly et qu'elle n'a jamais rien dit. L'informateur était [[micah-bell|Micah Bell]].")},
   ]},
   {"summary": two("Development and performance","Conception et interprétation"), "blocks": [
     {"p": two("Molly is played by Penny O'Brien, an Irish actress born in County Wicklow and a 2012 graduate of the American Academy of Dramatic Arts in New York. She provided both the voice and the motion capture. It was her first motion capture role.",
               "Molly est interprétée par Penny O'Brien, actrice irlandaise née dans le comté de Wicklow et diplômée en 2012 de l'American Academy of Dramatic Arts de New York. Elle assure la voix et la capture de mouvement. C'était son premier rôle en capture de mouvement.")},
     {"p": two("In 2019 interviews, O'Brien said she auditioned on Saint Patrick's Day 2015, with the instruction to play a \"really Irish\" accent and personality, and that she had not played the first Red Dead Redemption. She has said she only felt she understood Molly about a year into production, a process directed by Rod Edge and shot in secret, with the script revealed shortly before each session.",
               "Dans des interviews données en 2019, Penny O'Brien raconte avoir passé l'audition le jour de la Saint-Patrick 2015, avec pour consigne un accent et un tempérament \"vraiment irlandais\", sans avoir joué au premier Red Dead Redemption. Elle dit n'avoir vraiment cerné Molly qu'au bout d'un an de production, un tournage dirigé par Rod Edge et mené dans le secret, le texte n'étant révélé que peu avant chaque séance.")},
     {"p": two("Speaking to GamesRadar in March 2019, she described a lasting friendship with Benjamin Byron Davis, who plays Dutch: \"some jokes that were made while we were in our tent\" are ones they \"still make together when we're sitting at dinner\". A grave for Molly exists in the game files but is not used.",
               "Auprès de GamesRadar, en mars 2019, elle évoque une amitié durable avec Benjamin Byron Davis, l'interprète de Dutch : certaines plaisanteries nées sous leur tente de tournage sont restées entre eux, jusque dans leurs dîners. Une tombe au nom de Molly existe dans les fichiers du jeu, mais n'est pas utilisée.")},
   ]},
 ],
 "rel_after": 0,
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
