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
 "E1": ("rdr2-epilogue-part-1-pronghorn-ranch", "rdr2-epilogue-partie-1-pronghorn-ranch"),
 "E2": ("rdr2-epilogue-part-2-beechers-hope", "rdr2-epilogue-partie-2-beechers-hope"),
 "A1": ("rdr1-act-1-new-austin", "rdr1-acte-1-new-austin"),
 "A2": ("rdr1-act-2-nuevo-paraiso", "rdr1-acte-2-nuevo-paraiso"),
 "A3": ("rdr1-act-3-west-elizabeth", "rdr1-acte-3-west-elizabeth"),
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

# ---- Batch 1 (6 Oct 2026): Karen, Tilly, Mary-Beth, Pearson ----
def cl(n, text, lang):
    en, fr = CH[n]
    href = f"/story/{en}/" if lang == "en" else f"/fr/histoire/{fr}/"
    return f'<a href="{href}">{text}</a>'

BATCH1 = [
# ============================ KAREN JONES ============================
{
 "slug": "karen-jones", "name": "Karen Jones",
 "publishDate": "2026-08-14", "updated": "2026-10-06", "schema_game": "Red Dead Redemption 2",
 "reg_role_en": "Van der Linde gang &middot; RDR2", "reg_role_fr": "Gang Van der Linde &middot; RDR2",
 "gender": "Female", "death": None, "nationality": "American",
 "portrait_alt": two("Karen Jones in Red Dead Redemption 2", "Karen Jones dans Red Dead Redemption 2"),
 "eyebrow": two("Character &middot; Van der Linde gang", "Personnage &middot; Gang Van der Linde"),
 "meta_desc": two("Karen Jones: con artist and gunwoman of the Van der Linde gang in Red Dead Redemption 2. The Valentine bank job, her affair with Sean MacGuire, and what Tilly says about her fate.",
                  "Karen Jones : arnaqueuse et femme d'action du gang Van der Linde dans Red Dead Redemption 2. Le braquage de Valentine, sa liaison avec Sean MacGuire, et ce que Tilly dit de son sort."),
 "og_desc": two("The gang's scam artist, who plans the Valentine bank job and falls apart after Sean's death.",
                "L'arnaqueuse du gang, qui monte le braquage de Valentine et sombre après la mort de Sean."),
 "schema_desc": two("Con artist and gunwoman of the Van der Linde gang in Red Dead Redemption 2.",
                    "Arnaqueuse et femme d'action du gang Van der Linde dans Red Dead Redemption 2."),
 "chips": [two("Van der Linde gang", "Gang Van der Linde"), two("Con artist", "Arnaqueuse"),
           two("Fate unknown", "Sort inconnu"), two("RDR2", "RDR2")],
 "facts": [
   {"label": two("Affiliation","Affiliation"), "value": two("Van der Linde gang","Gang Van der Linde")},
   {"label": two("Role","Rôle"), "value": two("Con artist and robber","Arnaqueuse et braqueuse")},
   {"label": two("Status","Statut"), "value": two("Unknown after 1899","Inconnu après 1899")},
   {"label": two("Nationality","Nationalité"), "value": two("American","Américaine")},
   {"label": two("Voiced by","Voix"), "value": two("Jo Armeniox","Jo Armeniox")},
   {"label": two("Games","Jeux"), "value": two("Red Dead Redemption 2","Red Dead Redemption 2")},
 ],
 "intro": [
   two("Karen Jones is a thief and gunwoman of the Van der Linde gang in Red Dead Redemption 2. The game's official guide presents her as a skilled scam artist who enjoys the outlaw life and looks out for the other women of the gang.",
       "Karen Jones est voleuse et femme d'action au sein du gang Van der Linde dans Red Dead Redemption 2. Le guide officiel du jeu la présente comme une arnaqueuse douée, qui aime la vie de hors-la-loi et veille sur les autres femmes du gang."),
   two("Her fate after the gang breaks up is never shown.",
       "Son sort après l'éclatement du gang n'est jamais montré."),
 ],
 "sections": [
   {"summary": two("Biography","Biographie"), "open": True, "blocks": [
     {"h3": two("Scams and robberies","Arnaques et braquages")},
     {"p": two(f"Karen often plays a part in the gang's scams. During the trip to Valentine in {cl(2,'chapter 2','en')}, a man she tries to rob at the Saints Hotel hits her, and [[arthur-morgan|Arthur]] deals with him. After [[sean-macguire|Sean MacGuire]] is rescued and brought back to camp, the two begin a brief affair.",
               f"Karen tient souvent un rôle dans les arnaques du gang. Lors de la virée à Valentine du {cl(2,'chapitre 2','fr')}, un homme qu'elle tente de dépouiller au Saints Hotel la frappe, et [[arthur-morgan|Arthur]] s'occupe de lui. Après le sauvetage de [[sean-macguire|Sean MacGuire]] et son retour au camp, tous deux entament une brève liaison.")},
     {"p": two(f"In {cl(3,'chapter 3','en')}, she robs the Valentine bank with Arthur, [[bill-williamson|Bill Williamson]] and [[lenny-summers|Lenny Summers]], in the mission \"Sodom? Back to Gomorrah\". She planned the job with Bill. The player chooses whether she distracts the staff by playing a drunk or a lost young woman.",
               f"Au {cl(3,'chapitre 3','fr')}, elle braque la banque de Valentine avec Arthur, [[bill-williamson|Bill Williamson]] et [[lenny-summers|Lenny Summers]], dans la mission \"Sodom? Back to Gomorrah\". C'est elle qui a préparé le coup avec Bill. Le joueur choisit si elle détourne l'attention du personnel en jouant l'ivrogne ou la jeune femme égarée.")},
     {"h3": two("After Sean","Après Sean")},
     {"p": two(f"Sean is shot dead in Rhodes in \"A Short Walk in a Pretty Town\". From then on, Karen drinks heavily and is often found drunk in camp. She leaves the gang as it falls apart at {cl(6,'Beaver Hollow','en')}.",
               f"Sean est abattu à Rhodes dans \"A Short Walk in a Pretty Town\". Dès lors, Karen boit beaucoup et on la trouve souvent ivre au camp. Elle quitte le gang au moment où il se disloque, à {cl(6,'Beaver Hollow','fr')}.")},
     {"h3": two("Fate","Sort")},
     {"p": two("The game never shows what becomes of Karen. In a letter to John Marston in 1907, [[tilly-jackson|Tilly Jackson]] writes that she has had no news of her and believes drink killed her. This is Tilly's guess, not a fact established by the game.",
               "Le jeu ne montre jamais ce que devient Karen. Dans une lettre adressée à John Marston en 1907, [[tilly-jackson|Tilly Jackson]] écrit être sans nouvelles et penser que l'alcool l'a tuée. C'est une supposition de Tilly, pas un fait établi par le jeu.")},
   ]},
   {"summary": two("Development and performance","Conception et interprétation"), "blocks": [
     {"p": two("Karen is played by Jo Armeniox, who provided both the voice and the motion capture.",
               "Karen est interprétée par Jo Armeniox, qui assure la voix et la capture de mouvement.")},
     {"p": two("In a joint interview with the gang's actresses published by GamesRadar in March 2019, Armeniox recalled her scenes with Roger Clark, who plays Arthur: \"it was really rare also to have my own time with Roger and that was really special.\" In the same piece, Penny O'Brien, who plays Molly O'Shea, says Armeniox had to slap her twice in one scene.",
               "Dans un entretien croisé avec les actrices du gang, publié par GamesRadar en mars 2019, Jo Armeniox revient sur ses scènes avec Roger Clark, l'interprète d'Arthur, des moments rares en tête-à-tête qu'elle qualifie de \"vraiment à part\". Dans le même article, Penny O'Brien, l'interprète de Molly O'Shea, raconte qu'Armeniox devait la gifler deux fois dans une scène.")},
     {"p": two("In a video interview with Popternative in November 2019, she said she drew on an angry, rebellious side of herself for the role.",
               "Dans une interview vidéo accordée à Popternative en novembre 2019, elle explique avoir puisé dans une part colérique et rebelle d'elle-même pour le rôle.")},
   ]},
 ],
 "rel_after": 0,
 "relationships": [
   {"img": "sean.jpeg", "slug": "sean-macguire", "name": "Sean MacGuire", "text": two(
     "Her brief lover. His death in Rhodes sends her into heavy drinking.",
     "Son amant d'un temps. Sa mort à Rhodes la fait sombrer dans l'alcool.")},
   {"img": "bill.jpeg", "slug": "bill-williamson", "name": "Bill Williamson", "text": two(
     "Plans the Valentine bank job with her.",
     "Prépare avec elle le braquage de la banque de Valentine.")},
   {"img": "arthur.jpeg", "slug": "arthur-morgan", "name": "Arthur Morgan", "text": two(
     "Rides with her on the Valentine bank job.",
     "Participe avec elle au braquage de Valentine.")},
   {"img": "tilly.jpeg", "slug": "tilly-jackson", "name": "Tilly Jackson", "text": two(
     "Her close friend, who later writes that she fears Karen drank herself to death.",
     "Son amie proche, qui écrira plus tard craindre que l'alcool l'ait emportée.")},
   {"img": "susan.jpeg", "slug": "susan-grimshaw", "name": "Susan Grimshaw", "text": two(
     "Runs the camp's women; Karen turns on her after Molly's death.",
     "Dirige les femmes du camp ; Karen s'en prend à elle après la mort de Molly.")},
 ],
 "gallery": [
   {"img": "gallery-1.jpeg", "alt": two("Karen Jones at the gang's camp","Karen Jones au camp du gang"),
    "cap": two("Karen Jones at the gang's camp.","Karen Jones au camp du gang.")},
 ],
 "related": ["tilly-jackson", "sean-macguire", "mary-beth-gaskill", "bill-williamson"],
},
# ============================ TILLY JACKSON ============================
{
 "slug": "tilly-jackson", "name": "Tilly Jackson",
 "publishDate": "2026-08-17", "updated": "2026-10-06", "schema_game": "Red Dead Redemption 2",
 "reg_role_en": "Van der Linde gang &middot; RDR2", "reg_role_fr": "Gang Van der Linde &middot; RDR2",
 "gender": "Female", "death": None, "nationality": "American",
 "portrait_alt": two("Tilly Jackson in Red Dead Redemption 2", "Tilly Jackson dans Red Dead Redemption 2"),
 "eyebrow": two("Character &middot; Van der Linde gang", "Personnage &middot; Gang Van der Linde"),
 "meta_desc": two("Tilly Jackson: member of the Van der Linde gang in Red Dead Redemption 2. Her past with the Foreman Brothers, her kidnapping, her role in the gang's last days, and her life in Saint Denis in 1907.",
                  "Tilly Jackson : membre du gang Van der Linde dans Red Dead Redemption 2. Son passé chez les frères Foreman, son enlèvement, son rôle dans les derniers jours du gang, et sa vie à Saint-Denis en 1907."),
 "og_desc": two("An outlaw since the age of 12, who survives the gang and builds a new life in Saint Denis.",
                "Hors-la-loi depuis ses 12 ans, elle survit au gang et refait sa vie à Saint-Denis."),
 "schema_desc": two("Member of the Van der Linde gang in Red Dead Redemption 2, later living in Saint Denis as Tilly Pierre.",
                    "Membre du gang Van der Linde dans Red Dead Redemption 2, installée plus tard à Saint-Denis sous le nom de Tilly Pierre."),
 "chips": [two("Van der Linde gang", "Gang Van der Linde"), two("Alive in 1907", "Vivante en 1907"),
           two("Later Tilly Pierre", "Plus tard Tilly Pierre"), two("RDR2", "RDR2")],
 "facts": [
   {"label": two("Affiliation","Affiliation"), "value": two("Van der Linde gang; Foreman Brothers before","Gang Van der Linde ; frères Foreman auparavant")},
   {"label": two("Status","Statut"), "value": two("Alive in 1907","Vivante en 1907")},
   {"label": two("Later name","Nom plus tard"), "value": two("Tilly Pierre","Tilly Pierre")},
   {"label": two("Nationality","Nationalité"), "value": two("American","Américaine")},
   {"label": two("Voiced by","Voix"), "value": two("Meeya Davis","Meeya Davis")},
   {"label": two("Games","Jeux"), "value": two("Red Dead Redemption 2","Red Dead Redemption 2")},
 ],
 "intro": [
   two("Tilly Jackson is a member of the Van der Linde gang in Red Dead Redemption 2. Rockstar describes her as an outlaw from the age of 12, \"savvy, resilient and dependable\".",
       "Tilly Jackson est membre du gang Van der Linde dans Red Dead Redemption 2. Rockstar la décrit comme une hors-la-loi depuis l'âge de 12 ans, débrouillarde, solide et fiable."),
   two("She survives the gang's collapse and is living in Saint Denis by 1907.",
       "Elle survit à l'effondrement du gang et vit à Saint-Denis en 1907."),
 ],
 "sections": [
   {"summary": two("Biography","Biographie"), "open": True, "blocks": [
     {"h3": two("Origins","Origines")},
     {"p": two("According to the official guide, the Foreman Brothers gang took Tilly from her mother when she was 12. She spent several years with them and was mistreated, then killed one of their members and fled. [[dutch-van-der-linde|Dutch]] took her in and taught her to read.",
               "D'après le guide officiel, le gang des frères Foreman arrache Tilly à sa mère quand elle a 12 ans. Elle passe plusieurs années avec eux et y est maltraitée, puis tue l'un de leurs membres et s'enfuit. [[dutch-van-der-linde|Dutch]] la recueille et lui apprend à lire.")},
     {"h3": two("In the gang","Au sein du gang")},
     {"p": two(f"At camp, Tilly works under [[susan-grimshaw|Susan Grimshaw]] alongside [[karen-jones|Karen]] and [[mary-beth-gaskill|Mary-Beth]]. During the trip to Valentine in {cl(2,'chapter 2','en')}, Anthony Foreman recognises her and harasses her until [[arthur-morgan|Arthur]] steps in.",
               f"Au camp, Tilly travaille sous les ordres de [[susan-grimshaw|Susan Grimshaw]] avec [[karen-jones|Karen]] et [[mary-beth-gaskill|Mary-Beth]]. Lors de la virée à Valentine du {cl(2,'chapitre 2','fr')}, Anthony Foreman la reconnaît et la harcèle jusqu'à ce qu'[[arthur-morgan|Arthur]] intervienne.")},
     {"p": two(f"In {cl(4,'chapter 4','en')}, in \"No, No and Thrice, No\", the Foremans kidnap her near the Shady Belle camp and hold her at Radley's House. Grimshaw and Arthur rescue her. Arthur captures Anthony Foreman and decides whether to kill or spare him, with Grimshaw urging him to kill.",
               f"Au {cl(4,'chapitre 4','fr')}, dans \"No, No and Thrice, No\", les Foreman l'enlèvent près du camp de Shady Belle et la retiennent à Radley's House. Grimshaw et Arthur la libèrent. Arthur capture Anthony Foreman et décide de le tuer ou de l'épargner, Grimshaw le poussant à en finir.")},
     {"h3": two("The gang's last days","Les derniers jours du gang")},
     {"p": two(f"During the Pinkerton raid on {cl(6,'Beaver Hollow','en')}, Tilly hides Jack Marston. When the gang returns, she tells them that Agent Milton has taken Abigail. Arthur gives her money and sends her with Jack to Copperhead Landing, where Abigail and [[sadie-adler|Sadie]] later join them.",
               f"Pendant le raid des Pinkerton sur {cl(6,'Beaver Hollow','fr')}, Tilly cache Jack Marston. Au retour du gang, elle annonce que l'agent Milton a enlevé Abigail. Arthur lui remet de l'argent et l'envoie avec Jack à Copperhead Landing, où Abigail et [[sadie-adler|Sadie]] les rejoignent plus tard.")},
     {"h3": two("1907","1907")},
     {"p": two("By 1907, Tilly lives in Saint Denis and has married a lawyer from Haiti. John can meet her on a bench in the city; she is pregnant. In a later letter to John and Abigail, signed \"Tilly Pierre\", she writes that she has had a daughter, that she still sees Mary-Beth, and that Hosea had been \"like a father\" to her.",
               "En 1907, Tilly vit à Saint-Denis et a épousé un avocat originaire d'Haïti. John peut la croiser sur un banc de la ville ; elle est enceinte. Dans une lettre envoyée plus tard à John et Abigail, signée \"Tilly Pierre\", elle annonce la naissance de sa fille, dit voir toujours Mary-Beth, et écrit que Hosea avait été comme un père pour elle.")},
   ]},
   {"summary": two("Development and performance","Conception et interprétation"), "blocks": [
     {"p": two("Tilly is played by Meeya Davis, an actress from Detroit who moved to New Jersey in 2012 to study acting. She provided the voice and the motion capture. Speaking to Fuzzable in March 2019, she said she was first called in for what was presented as a commercial audition, and only learned about the character on her shooting days. She also said she went to high school with Harron Atkins, who plays Lenny Summers.",
               "Tilly est interprétée par Meeya Davis, actrice originaire de Detroit, installée dans le New Jersey en 2012 pour étudier le jeu. Elle assure la voix et la capture de mouvement. Auprès de Fuzzable, en mars 2019, elle raconte avoir été convoquée pour ce qu'on lui présentait comme une audition pour une publicité, et n'avoir découvert le personnage qu'aux jours de tournage. Elle y précise aussi avoir fréquenté le même lycée que Harron Atkins, l'interprète de Lenny Summers.")},
     {"p": two("In the GamesRadar interview with the gang's actresses (March 2019), Davis said the scene where Tilly tells how she killed Anthony Foreman's cousin made her emotional on set. She was seven or eight months pregnant when she shot Tilly's pregnancy scene, which she called \"art imitating life\".",
               "Dans l'entretien croisé de GamesRadar avec les actrices du gang (mars 2019), Meeya Davis confie que la scène où Tilly raconte le meurtre du cousin d'Anthony Foreman l'a émue sur le plateau. Elle était enceinte de sept ou huit mois lorsqu'elle a tourné la scène de grossesse de Tilly, un cas où \"l'art imite la vie\", dit-elle.")},
   ]},
 ],
 "rel_after": 0,
 "relationships": [
   {"img": "karen.jpeg", "slug": "karen-jones", "name": "Karen Jones", "text": two(
     "\"A sister to me\", as Tilly writes in 1907.",
     "\"Une sœur\" pour elle, écrit Tilly en 1907.")},
   {"img": "marybeth.jpeg", "slug": "mary-beth-gaskill", "name": "Mary-Beth Gaskill", "text": two(
     "Her friend in camp; they stay in touch after the gang.",
     "Son amie au camp ; elles restent proches après le gang.")},
   {"img": "susan.jpeg", "slug": "susan-grimshaw", "name": "Susan Grimshaw", "text": two(
     "Runs the camp's women and leads her rescue from the Foremans.",
     "Dirige les femmes du camp et mène son sauvetage chez les Foreman.")},
   {"img": "arthur.jpeg", "slug": "arthur-morgan", "name": "Arthur Morgan", "text": two(
     "Rescues her, then sends her to safety with Jack.",
     "La sauve, puis la met à l'abri avec Jack.")},
   {"img": "dutch.jpeg", "slug": "dutch-van-der-linde", "name": "Dutch van der Linde", "text": two(
     "Takes her into the gang and teaches her to read.",
     "La fait entrer dans le gang et lui apprend à lire.")},
 ],
 "gallery": [
   {"img": "gallery-1.jpeg", "alt": two("Tilly Jackson at the gang's camp","Tilly Jackson au camp du gang"),
    "cap": two("Tilly Jackson at the gang's camp.","Tilly Jackson au camp du gang.")},
 ],
 "related": ["karen-jones", "mary-beth-gaskill", "susan-grimshaw", "arthur-morgan"],
},
# ============================ MARY-BETH GASKILL ============================
{
 "slug": "mary-beth-gaskill", "name": "Mary-Beth Gaskill",
 "publishDate": "2026-08-20", "updated": "2026-10-06", "schema_game": "Red Dead Redemption 2",
 "reg_role_en": "Van der Linde gang &middot; RDR2", "reg_role_fr": "Gang Van der Linde &middot; RDR2",
 "gender": "Female", "death": None, "nationality": "American",
 "portrait_alt": two("Mary-Beth Gaskill in Red Dead Redemption 2", "Mary-Beth Gaskill dans Red Dead Redemption 2"),
 "eyebrow": two("Character &middot; Van der Linde gang", "Personnage &middot; Gang Van der Linde"),
 "meta_desc": two("Mary-Beth Gaskill: pickpocket of the Van der Linde gang in Red Dead Redemption 2 who becomes a novelist. Her role in the gang, Arthur's confession, and her pen name Leslie Dupont.",
                  "Mary-Beth Gaskill : pickpocket du gang Van der Linde dans Red Dead Redemption 2, devenue romancière. Son rôle dans le gang, la confidence d'Arthur, et son nom de plume, Leslie Dupont."),
 "og_desc": two("The gang's pickpocket and would-be writer, who publishes romance novels as Leslie Dupont by 1907.",
                "La pickpocket du gang qui rêvait d'écrire, et qui publie des romans sentimentaux sous le nom de Leslie Dupont en 1907."),
 "schema_desc": two("Pickpocket of the Van der Linde gang in Red Dead Redemption 2, later a novelist writing as Leslie Dupont.",
                    "Pickpocket du gang Van der Linde dans Red Dead Redemption 2, devenue romancière sous le nom de Leslie Dupont."),
 "chips": [two("Van der Linde gang", "Gang Van der Linde"), two("Alive in 1907", "Vivante en 1907"),
           two("Pickpocket, novelist", "Pickpocket, romancière"), two("RDR2", "RDR2")],
 "facts": [
   {"label": two("Affiliation","Affiliation"), "value": two("Van der Linde gang","Gang Van der Linde")},
   {"label": two("Role","Rôle"), "value": two("Pickpocket and thief","Pickpocket et voleuse")},
   {"label": two("Later","Plus tard"), "value": two("Novelist (pen name Leslie Dupont)","Romancière (nom de plume Leslie Dupont)")},
   {"label": two("Status","Statut"), "value": two("Alive in 1907","Vivante en 1907")},
   {"label": two("Voiced by","Voix"), "value": two("Samantha Strelitz","Samantha Strelitz")},
   {"label": two("Games","Jeux"), "value": two("Red Dead Redemption 2","Red Dead Redemption 2")},
 ],
 "intro": [
   two("Mary-Beth Gaskill is a young pickpocket in the Van der Linde gang in Red Dead Redemption 2, who wants to become a novelist. Rockstar describes her as kind and good-natured, \"which makes her the perfect criminal\".",
       "Mary-Beth Gaskill est une jeune pickpocket du gang Van der Linde dans Red Dead Redemption 2, qui rêve de devenir romancière. Rockstar la décrit comme gentille et bienveillante, ce qui ferait d'elle \"la criminelle idéale\"."),
   two("She survives the gang and, by 1907, publishes romance novels under the pen name Leslie Dupont.",
       "Elle survit au gang et, en 1907, publie des romans sentimentaux sous le nom de plume de Leslie Dupont."),
 ],
 "sections": [
   {"summary": two("Biography","Biographie"), "open": True, "blocks": [
     {"h3": two("Origins","Origines")},
     {"p": two("According to the official guide, Mary-Beth's mother died of typhoid. She was placed in an orphanage, ran away and lived by her wits. She met the gang while fleeing men she had robbed. She has loved reading and writing since childhood.",
               "D'après le guide officiel, la mère de Mary-Beth meurt du typhus. Placée dans un orphelinat, elle s'enfuit et vit d'expédients. Elle croise la route du gang en fuyant des hommes qu'elle avait volés. Elle aime lire et écrire depuis l'enfance.")},
     {"h3": two("In the gang","Au sein du gang")},
     {"p": two(f"During the trip to Valentine in {cl(2,'chapter 2','en')}, Mary-Beth gives [[arthur-morgan|Arthur]] a tip about a train carrying wealthy passengers through Scarlett Meadows. The tip leads to the gang's train robbery, in which she does not take part. In {cl(3,'chapter 3','en')}, she helps [[sean-macguire|Sean]] rob a stagecoach by faking amnesia to distract the guards.",
               f"Lors de la virée à Valentine du {cl(2,'chapitre 2','fr')}, Mary-Beth donne à [[arthur-morgan|Arthur]] un tuyau sur un train de voyageurs fortunés qui traverse les Scarlett Meadows. Ce tuyau mène à l'attaque du train par le gang, à laquelle elle ne participe pas. Au {cl(3,'chapitre 3','fr')}, elle aide [[sean-macguire|Sean]] à dévaliser une diligence en feignant l'amnésie pour distraire les gardes.")},
     {"p": two(f"In {cl(6,'chapter 6','en')}, Arthur can tell her that he has tuberculosis; she encourages him to make his remaining time count. She then leaves the gang at Beaver Hollow. At the start of \"Our Best Selves\", Dutch names her, Pearson and Uncle among those who have left, and calls them cowards.",
               f"Au {cl(6,'chapitre 6','fr')}, Arthur peut lui confier qu'il est atteint de tuberculose ; elle l'encourage à faire en sorte que le temps qui lui reste compte. Elle quitte ensuite le gang à Beaver Hollow. Au début de \"Our Best Selves\", Dutch la cite, avec Pearson et Uncle, parmi ceux qui sont partis, et les traite de lâches.")},
     {"h3": two("1907","1907")},
     {"p": two("In the epilogue, John Marston can meet her on the platform of Valentine station. She now writes romance novels as Leslie Dupont, gives him a copy of \"The Lady of the Manor\" and boards her train. A newspaper in the game calls the book Dupont's \"fourth tome\". A letter from [[tilly-jackson|Tilly]] confirms that the two women are still close.",
               "Dans l'épilogue, John Marston peut la croiser sur le quai de la gare de Valentine. Elle écrit désormais des romans sentimentaux sous le nom de Leslie Dupont, lui offre un exemplaire de \"The Lady of the Manor\" et monte dans son train. Un journal du jeu présente ce livre comme le quatrième de Dupont. Une lettre de [[tilly-jackson|Tilly]] confirme que les deux femmes sont restées proches.")},
   ]},
   {"summary": two("Development and performance","Conception et interprétation"), "blocks": [
     {"p": two("Mary-Beth is played by Samantha Strelitz, a Long Beach native based in New York, who provided both the voice and the motion capture.",
               "Mary-Beth est interprétée par Samantha Strelitz, originaire de Long Beach et installée à New York, qui assure la voix et la capture de mouvement.")},
     {"p": two("In GamesRadar's interview with the gang's actresses (March 2019), she singled out the scene in which Arthur confides that he is dying: \"I'm always very overwhelmed when I see the scene where Arthur sort of becomes my confidant, and he tells me that he's dying.\"",
               "Dans l'entretien croisé de GamesRadar avec les actrices du gang (mars 2019), elle retient la scène où Arthur lui confie qu'il va mourir, une scène qui la bouleverse encore à chaque fois, dit-elle, par son innocence.")},
   ]},
   {"summary": two("Reception","Accueil"), "blocks": [
     {"p": two("In a December 2018 ranking of the gang's members, Game Informer placed Mary-Beth 13th. The magazine praised her \"honest, gentle\" conversations with Arthur and called her epilogue scene \"a necessary bright spot in this epic, dark tale\", while noting her absence from the story missions.",
               "Dans un classement des membres du gang publié en décembre 2018, Game Informer place Mary-Beth en 13e position. Le magazine salue la douceur et la franchise de ses échanges avec Arthur, et voit dans sa scène d'épilogue une éclaircie bienvenue dans un récit sombre, tout en regrettant son absence des missions principales.")},
   ]},
 ],
 "rel_after": 0,
 "relationships": [
   {"img": "arthur.jpeg", "slug": "arthur-morgan", "name": "Arthur Morgan", "text": two(
     "Confides in her that he is dying.",
     "Lui confie qu'il va mourir.")},
   {"img": "tilly.jpeg", "slug": "tilly-jackson", "name": "Tilly Jackson", "text": two(
     "Her friend; they stay in touch after the gang.",
     "Son amie ; elles restent en contact après le gang.")},
   {"img": "sean.jpeg", "slug": "sean-macguire", "name": "Sean MacGuire", "text": two(
     "Robs a stagecoach with her in chapter 3.",
     "Dévalise une diligence avec elle au chapitre 3.")},
   {"img": "karen.jpeg", "slug": "karen-jones", "name": "Karen Jones", "text": two(
     "Goes to Valentine with her and Tilly in chapter 2.",
     "L'accompagne à Valentine avec Tilly au chapitre 2.")},
 ],
 "gallery": [
   {"img": "gallery-1.jpeg", "alt": two("Mary-Beth Gaskill at the gang's camp","Mary-Beth Gaskill au camp du gang"),
    "cap": two("Mary-Beth Gaskill at the gang's camp.","Mary-Beth Gaskill au camp du gang.")},
 ],
 "related": ["tilly-jackson", "karen-jones", "sean-macguire", "arthur-morgan"],
},
# ============================ SIMON PEARSON ============================
{
 "slug": "simon-pearson", "name": "Simon Pearson",
 "publishDate": "2026-08-23", "updated": "2026-10-06", "schema_game": "Red Dead Redemption 2",
 "reg_role_en": "Gang cook &middot; RDR2", "reg_role_fr": "Cuisinier du gang &middot; RDR2",
 "gender": "Male", "death": None, "nationality": "American",
 "portrait_alt": two("Simon Pearson in Red Dead Redemption 2", "Simon Pearson dans Red Dead Redemption 2"),
 "eyebrow": two("Character &middot; Van der Linde gang", "Personnage &middot; Gang Van der Linde"),
 "meta_desc": two("Simon Pearson: cook and butcher of the Van der Linde gang in Red Dead Redemption 2. Former US Navy sailor, his role in the camp, his departure, and his general store in Rhodes in 1907.",
                  "Simon Pearson : cuisinier et boucher du gang Van der Linde dans Red Dead Redemption 2. Ancien marin de l'US Navy, son rôle au camp, son départ, et son magasin général de Rhodes en 1907."),
 "og_desc": two("The gang's cook and former Navy sailor, who runs the Rhodes general store by 1907.",
                "Le cuisinier du gang, ancien marin, qui tient le magasin général de Rhodes en 1907."),
 "schema_desc": two("Cook and butcher of the Van der Linde gang in Red Dead Redemption 2, later owner of the Rhodes general store.",
                    "Cuisinier et boucher du gang Van der Linde dans Red Dead Redemption 2, devenu propriétaire du magasin général de Rhodes."),
 "chips": [two("Van der Linde gang", "Gang Van der Linde"), two("Alive in 1907", "Vivant en 1907"),
           two("Cook", "Cuisinier"), two("RDR2", "RDR2")],
 "facts": [
   {"label": two("Affiliation","Affiliation"), "value": two("Van der Linde gang","Gang Van der Linde")},
   {"label": two("Role","Rôle"), "value": two("Cook and butcher","Cuisinier et boucher")},
   {"label": two("Past","Passé"), "value": two("US Navy","US Navy")},
   {"label": two("In 1907","En 1907"), "value": two("Owner of the Rhodes general store","Propriétaire du magasin général de Rhodes")},
   {"label": two("Voiced by","Voix"), "value": two("Jim Santangeli","Jim Santangeli")},
   {"label": two("Games","Jeux"), "value": two("Red Dead Redemption 2","Red Dead Redemption 2")},
 ],
 "intro": [
   two("Simon Pearson is the cook and butcher of the Van der Linde gang in Red Dead Redemption 2. A former US Navy sailor, he keeps the camp fed and supplied.",
       "Simon Pearson est le cuisinier et le boucher du gang Van der Linde dans Red Dead Redemption 2. Ancien marin de l'US Navy, il assure les vivres et l'intendance du camp."),
   two("He leaves the gang before its collapse and, by 1907, runs the general store in Rhodes.",
       "Il quitte le gang avant sa chute et tient, en 1907, le magasin général de Rhodes."),
 ],
 "sections": [
   {"summary": two("Biography","Biographie"), "open": True, "blocks": [
     {"h3": two("Origins","Origines")},
     {"p": two("According to the official guide, Pearson's father and grandfather hunted sperm whales. He meant to follow them, but the trade was dying out by the time he left school. He served briefly in the US Navy, moved west, ran into money trouble, and was invited into the gang by [[dutch-van-der-linde|Dutch]].",
               "D'après le guide officiel, le père et le grand-père de Pearson chassaient le cachalot. Il comptait suivre leurs traces, mais le métier disparaissait déjà à sa sortie de l'école. Il sert brièvement dans l'US Navy, part vers l'Ouest, s'y endette, et Dutch lui propose de rejoindre le gang.")},
     {"h3": two("The camp's cook","Le cuisinier du camp")},
     {"p": two(f"Pearson sets up each new camp with [[susan-grimshaw|Susan Grimshaw]] and regularly sends [[arthur-morgan|Arthur]] out for meat. Through the camp ledger, he also crafts satchels and camp decorations. In {cl(1,'chapter 1','en')}, with food running out in the mountains, he sends Arthur and [[charles-smith|Charles]] to hunt deer, then helps Arthur butcher the carcasses.",
               f"Pearson installe chaque nouveau camp avec [[susan-grimshaw|Susan Grimshaw]] et envoie régulièrement [[arthur-morgan|Arthur]] chercher de la viande. Grâce au registre du camp, il fabrique aussi des sacoches et des aménagements. Au {cl(1,'chapitre 1','fr')}, alors que les vivres manquent dans les montagnes, il envoie Arthur et [[charles-smith|Charles]] chasser le cerf, puis aide Arthur à dépecer les bêtes.")},
     {"p": two(f"In {cl(3,'chapter 3','en')}, an argument with [[sadie-adler|Sadie Adler]] ends with Arthur taking her to Rhodes for supplies and to post Pearson's letter to his aunt. In {cl(4,'chapter 4','en')}, Dutch orders him, Charles and Reverend Swanson to bury [[kieran-duffy|Kieran Duffy]].",
               f"Au {cl(3,'chapitre 3','fr')}, une dispute avec [[sadie-adler|Sadie Adler]] se conclut par une course à Rhodes, où Arthur l'emmène se ravitailler et poster une lettre de Pearson à sa tante. Au {cl(4,'chapitre 4','fr')}, Dutch le charge, avec Charles et le révérend Swanson, d'enterrer [[kieran-duffy|Kieran Duffy]].")},
     {"h3": two("Leaving the gang","Le départ")},
     {"p": two(f"At {cl(6,'Beaver Hollow','en')}, Susan Grimshaw orders Pearson and [[bill-williamson|Bill]] to burn the body of [[molly-oshea|Molly O'Shea]]. Shortly afterwards, Pearson leaves with Uncle and Mary-Beth. At the start of \"Our Best Selves\", Dutch announces their departure and calls them cowards.",
               f"À {cl(6,'Beaver Hollow','fr')}, Susan Grimshaw ordonne à Pearson et à [[bill-williamson|Bill]] de brûler le corps de [[molly-oshea|Molly O'Shea]]. Peu après, Pearson s'en va avec Uncle et Mary-Beth. Au début de \"Our Best Selves\", Dutch annonce leur départ et les traite de lâches.")},
     {"h3": two("1907","1907")},
     {"p": two("By 1907, Pearson is married and runs the general store in Rhodes, where John Marston can talk to him.",
               "En 1907, Pearson est marié et tient le magasin général de Rhodes, où John Marston peut discuter avec lui.")},
   ]},
   {"summary": two("Development and performance","Conception et interprétation"), "blocks": [
     {"p": two("Pearson is played by Jim Santangeli, an American actor, writer and director, who provided both the voice and the motion capture. Santangeli had previously voiced a pedestrian in Grand Theft Auto IV. He took part in a panel with the game's cast at SacAnime in Sacramento in June 2019.",
               "Pearson est interprété par Jim Santangeli, acteur, scénariste et réalisateur américain, qui assure la voix et la capture de mouvement. Santangeli avait auparavant prêté sa voix à un passant dans Grand Theft Auto IV. Il a participé à une table ronde avec la distribution du jeu à la SacAnime de Sacramento, en juin 2019.")},
     {"p": two("In 2026, Santangeli said during a TikTok livestream that he has a small part in Grand Theft Auto VI, as reported by GTA BOOM in June 2026.",
               "En 2026, Santangeli a indiqué lors d'un direct sur TikTok tenir un petit rôle dans Grand Theft Auto VI, selon GTA BOOM en juin 2026.")},
   ]},
 ],
 "rel_after": 0,
 "relationships": [
   {"img": "susan.jpeg", "slug": "susan-grimshaw", "name": "Susan Grimshaw", "text": two(
     "Sets up each camp with him.",
     "Installe chaque camp avec lui.")},
   {"img": "arthur.jpeg", "slug": "arthur-morgan", "name": "Arthur Morgan", "text": two(
     "Keeps the camp supplied with meat at his request.",
     "Ravitaille le camp en viande à sa demande.")},
   {"img": "charles.jpeg", "slug": "charles-smith", "name": "Charles Smith", "text": two(
     "Hunts for the camp with Arthur in chapter 1.",
     "Chasse pour le camp avec Arthur au chapitre 1.")},
   {"img": "sadie.jpeg", "slug": "sadie-adler", "name": "Sadie Adler", "text": two(
     "Clashes with him in camp in chapter 3.",
     "Se heurte à lui au camp au chapitre 3.")},
 ],
 "gallery": [
   {"img": "gallery-1.jpeg", "alt": two("Simon Pearson at the gang's camp","Simon Pearson au camp du gang"),
    "cap": two("Simon Pearson at the gang's camp.","Simon Pearson au camp du gang.")},
 ],
 "related": ["susan-grimshaw", "sadie-adler", "charles-smith", "arthur-morgan"],
},
]
ENRICHED += BATCH1

# ---- Batch 2 (6 Oct 2026): Sean, Lenny, Kieran, Swanson ----
BATCH2 = [
# ============================ SEAN MACGUIRE ============================
{
 "slug": "sean-macguire", "name": "Sean MacGuire",
 "publishDate": "2026-06-26", "updated": "2026-10-06", "schema_game": "Red Dead Redemption 2",
 "reg_role_en": "Van der Linde gang &middot; RDR2", "reg_role_fr": "Gang Van der Linde &middot; RDR2",
 "gender": "Male", "death": "1899", "nationality": "Irish",
 "portrait_alt": two("Sean MacGuire in Red Dead Redemption 2", "Sean MacGuire dans Red Dead Redemption 2"),
 "eyebrow": two("Character &middot; Van der Linde gang", "Personnage &middot; Gang Van der Linde"),
 "meta_desc": two("Sean MacGuire: young Irish thief of the Van der Linde gang in Red Dead Redemption 2. His rescue, the Gray feud, his death in Rhodes, and Michael Mellamphy's performance.",
                  "Sean MacGuire : jeune voleur irlandais du gang Van der Linde dans Red Dead Redemption 2. Son sauvetage, la guerre des Gray, sa mort à Rhodes, et l'interprétation de Michael Mellamphy."),
 "og_desc": two("The gang's Irish stick-up man, rescued in chapter 2 and shot dead in the Rhodes ambush.",
                "Le braqueur irlandais du gang, sauvé au chapitre 2 et abattu dans l'embuscade de Rhodes."),
 "schema_desc": two("Irish thief and member of the Van der Linde gang in Red Dead Redemption 2.",
                    "Voleur irlandais, membre du gang Van der Linde dans Red Dead Redemption 2."),
 "chips": [two("Died <strong>1899</strong>", "Mort en <strong>1899</strong>"), two("Deceased", "Décédé"),
           two("Van der Linde gang", "Gang Van der Linde"), two("Irish", "Irlandais")],
 "facts": [
   {"label": two("Origin","Origine"), "value": two("Irish","Irlandais")},
   {"label": two("Died","Mort"), "value": two("1899, Rhodes","1899, Rhodes")},
   {"label": two("Status","Statut"), "value": two("Deceased","Décédé")},
   {"label": two("Affiliation","Affiliation"), "value": two("Van der Linde gang","Gang Van der Linde")},
   {"label": two("Role","Rôle"), "value": two("Thief and stick-up man","Voleur et braqueur")},
   {"label": two("Voiced by","Voix"), "value": two("Michael Mellamphy","Michael Mellamphy")},
   {"label": two("Games","Jeux"), "value": two("Red Dead Redemption 2","Red Dead Redemption 2")},
 ],
 "intro": [
   two("Sean MacGuire is a young Irish thief in the Van der Linde gang in Red Dead Redemption 2. Rockstar describes him as coming from \"a long line of criminals and political dissidents\".",
       "Sean MacGuire est un jeune voleur irlandais du gang Van der Linde dans Red Dead Redemption 2. Rockstar le présente comme l'héritier d'une longue lignée de criminels et de dissidents politiques."),
   two("He is shot dead in Rhodes in 1899, in an ambush set up by the Gray family.",
       "Il est abattu à Rhodes en 1899, dans une embuscade montée par la famille Gray."),
 ],
 "sections": [
   {"summary": two("Biography","Biographie"), "open": True, "blocks": [
     {"h3": two("Origins","Origines")},
     {"p": two("According to the official guide, Sean's father was wanted by the government; he fled to America with his son and was caught and killed there. Sean joined the gang after failing to steal [[dutch-van-der-linde|Dutch]]'s pocket watch in an alley.",
               "D'après le guide officiel, le père de Sean était recherché par les autorités ; il s'est réfugié en Amérique avec son fils, où il a été rattrapé et tué. Sean entre dans le gang après avoir raté le vol de la montre de gousset de [[dutch-van-der-linde|Dutch]] dans une ruelle.")},
     {"h3": two("Capture and return","Capture et retour")},
     {"p": two(f"Separated from the gang after the failed Blackwater robbery, Sean is captured by bounty hunters. In {cl(2,'chapter 2','en')}, in \"The First Shall Be Last\", [[arthur-morgan|Arthur]], [[charles-smith|Charles]] and [[javier-escuella|Javier]] free him, with [[josiah-trelawny|Josiah Trelawny]] creating a diversion. The camp throws a party for his return, during which he and [[karen-jones|Karen Jones]] begin an affair.",
               f"Séparé du gang après le braquage raté de Blackwater, Sean est capturé par des chasseurs de primes. Au {cl(2,'chapitre 2','fr')}, dans \"The First Shall Be Last\", [[arthur-morgan|Arthur]], [[charles-smith|Charles]] et [[javier-escuella|Javier]] le libèrent, pendant que [[josiah-trelawny|Josiah Trelawny]] fait diversion. Le camp fête son retour, et c'est ce soir-là qu'il entame une liaison avec [[karen-jones|Karen Jones]].")},
     {"p": two("He then joins Arthur, John and Charles on the gang's train robbery, in \"Pouring Forth Oil IV\".",
               "Il participe ensuite avec Arthur, John et Charles à l'attaque de train du gang, dans \"Pouring Forth Oil IV\".")},
     {"h3": two("The Gray feud and his death","La guerre des Gray et sa mort")},
     {"p": two(f"In {cl(3,'chapter 3','en')}, the gang works both sides of the feud between the Grays and the Braithwaites. In \"The Fine Joys of Tobacco\", Sean and Arthur burn the Grays' tobacco fields for Catherine Braithwaite.",
               f"Au {cl(3,'chapitre 3','fr')}, le gang joue sur les deux tableaux de la guerre entre les Gray et les Braithwaite. Dans \"The Fine Joys of Tobacco\", Sean et Arthur incendient les champs de tabac des Gray pour le compte de Catherine Braithwaite.")},
     {"p": two("In \"A Short Walk in a Pretty Town\", the Grays offer the gang a job in Rhodes. It is a trap. As Sean walks down the street with Arthur, [[bill-williamson|Bill]] and [[micah-bell|Micah]], a sniper shoots him in the head and he dies instantly. After his death, Karen starts drinking heavily.",
               "Dans \"A Short Walk in a Pretty Town\", les Gray proposent un travail au gang à Rhodes. C'est un piège. Alors que Sean remonte la rue avec Arthur, [[bill-williamson|Bill]] et [[micah-bell|Micah]], un tireur embusqué l'atteint à la tête et le tue sur le coup. Après sa mort, Karen se met à boire.")},
   ]},
   {"summary": two("Development and performance","Conception et interprétation"), "blocks": [
     {"p": two("Sean is played by Michael \"Mick\" Mellamphy, who provided the voice and the motion capture. According to a cast panel at SacAnime in June 2019, Mellamphy was the second actor cast in the role, replacing another actor during production.",
               "Sean est interprété par Michael \"Mick\" Mellamphy, qui assure la voix et la capture de mouvement. Selon une table ronde de la distribution à la SacAnime, en juin 2019, Mellamphy est le second acteur à avoir tenu le rôle, en remplacement d'un premier interprète en cours de production.")},
     {"p": two("In January 2021, Mellamphy, Roger Clark (Arthur) and Penny O'Brien (Molly O'Shea) took part in an online panel organised by Origin Theatre's First Irish Festival, reported by TheGamer. He recalled asking Benjamin Byron Davis, who plays Dutch, whether Sean was really part of the gang, and being told: \"Mick, my man. Sean's part of the gang.\" On the accent, he said: \"There was just something very Dublin about [Sean] - working class, a bit of fun.\"",
               "En janvier 2021, Mellamphy, Roger Clark (Arthur) et Penny O'Brien (Molly O'Shea) participent à une table ronde en ligne du First Irish Festival de l'Origin Theatre, rapportée par TheGamer. Il raconte avoir demandé à Benjamin Byron Davis, l'interprète de Dutch, si Sean faisait vraiment partie du gang, et s'être vu répondre qu'il en faisait bien partie. Sur l'accent, il explique que Sean lui a paru d'emblée très dublinois, issu du peuple et blagueur.")},
     {"p": two("He also said that, as a player, he missed the party celebrating Sean's return, because he went hunting with Arthur and came back to a hungover camp the next morning.",
               "Il confie aussi avoir manqué, en tant que joueur, la fête organisée pour le retour de Sean : parti chasser avec Arthur, il est revenu au camp le lendemain matin, au milieu d'une troupe gueule de bois.")},
   ]},
   {"summary": two("Reception","Accueil"), "blocks": [
     {"p": two("In November 2018, Eurogamer published an article by Cian Maher titled \"Why Red Dead Redemption 2's Sean MacGuire is the best Irish character in a video game yet\". It ranks Sean above earlier Irish characters from Rockstar, including Irish in Red Dead Redemption and the McReary family in Grand Theft Auto IV, and praises the historical grounding of his background.",
               "En novembre 2018, Eurogamer publie un article de Cian Maher qui fait de Sean le meilleur personnage irlandais de l'histoire du jeu vidéo. Il le place au-dessus des précédents personnages irlandais de Rockstar, dont Irish dans Red Dead Redemption et la famille McReary dans Grand Theft Auto IV, et salue l'ancrage historique de son passé.")},
   ]},
 ],
 "rel_after": 0,
 "relationships": [
   {"img": "karen.jpeg", "slug": "karen-jones", "name": "Karen Jones", "text": two(
     "Begins an affair with him after his rescue.",
     "Entame une liaison avec lui après son sauvetage.")},
   {"img": "arthur.jpeg", "slug": "arthur-morgan", "name": "Arthur Morgan", "text": two(
     "Rescues him, then burns the Gray fields with him.",
     "Le libère, puis incendie avec lui les champs des Gray.")},
   {"img": "lenny.jpeg", "slug": "lenny-summers", "name": "Lenny Summers", "text": two(
     "A fellow young member of the gang.",
     "Autre jeune membre du gang.")},
   {"img": "dutch.jpeg", "slug": "dutch-van-der-linde", "name": "Dutch van der Linde", "text": two(
     "Takes him in after Sean fails to steal his watch.",
     "L'accueille après que Sean a raté le vol de sa montre.")},
 ],
 "gallery": [
   {"img": "gallery-1.jpeg", "alt": two("Sean MacGuire","Sean MacGuire"), "cap": two("Sean MacGuire.","Sean MacGuire.")},
 ],
 "related": ["karen-jones", "lenny-summers", "arthur-morgan", "bill-williamson"],
},
# ============================ LENNY SUMMERS ============================
{
 "slug": "lenny-summers", "name": "Lenny Summers",
 "publishDate": "2026-06-27", "updated": "2026-10-06", "schema_game": "Red Dead Redemption 2",
 "reg_role_en": "Van der Linde gang &middot; RDR2", "reg_role_fr": "Gang Van der Linde &middot; RDR2",
 "gender": "Male", "birth": "1880", "death": "1899", "nationality": "American",
 "portrait_alt": two("Lenny Summers in Red Dead Redemption 2", "Lenny Summers dans Red Dead Redemption 2"),
 "eyebrow": two("Character &middot; Van der Linde gang", "Personnage &middot; Gang Van der Linde"),
 "meta_desc": two("Lenny Summers: young gunman of the Van der Linde gang in Red Dead Redemption 2. His past, the Valentine bar night with Arthur, the Shady Belle raid, and his death in Saint Denis.",
                  "Lenny Summers : jeune tireur du gang Van der Linde dans Red Dead Redemption 2. Son passé, la soirée au saloon de Valentine avec Arthur, l'attaque de Shady Belle, et sa mort à Saint-Denis."),
 "og_desc": two("The gang's youngest gunman, Arthur's drinking partner in \"A Quiet Time\", killed during the Saint Denis bank job.",
                "Le plus jeune tireur du gang, compagnon de beuverie d'Arthur dans \"A Quiet Time\", tué lors du braquage de Saint-Denis."),
 "schema_desc": two("Young gunman of the Van der Linde gang in Red Dead Redemption 2.",
                    "Jeune tireur du gang Van der Linde dans Red Dead Redemption 2."),
 "chips": [two("1880&ndash;1899", "1880&ndash;1899"), two("Deceased", "Décédé"),
           two("Van der Linde gang", "Gang Van der Linde"), two("Gunman", "Tireur")],
 "facts": [
   {"label": two("Full name","Nom complet"), "value": two("Leonard Summers","Leonard Summers")},
   {"label": two("Born","Naissance"), "value": two("1880","1880")},
   {"label": two("Died","Mort"), "value": two("1899, Saint Denis","1899, Saint-Denis")},
   {"label": two("Status","Statut"), "value": two("Deceased","Décédé")},
   {"label": two("Affiliation","Affiliation"), "value": two("Van der Linde gang","Gang Van der Linde")},
   {"label": two("Voiced by","Voix"), "value": two("Harron Atkins","Harron Atkins")},
   {"label": two("Games","Jeux"), "value": two("Red Dead Redemption 2","Red Dead Redemption 2")},
 ],
 "intro": [
   two("Lenny Summers is the youngest gunman of the Van der Linde gang in Red Dead Redemption 2. Born in 1880 to former slaves, he is educated and close to [[arthur-morgan|Arthur Morgan]].",
       "Lenny Summers est le plus jeune tireur du gang Van der Linde dans Red Dead Redemption 2. Né en 1880 de parents anciens esclaves, il est instruit et proche d'[[arthur-morgan|Arthur Morgan]]."),
   two("He is killed in 1899 during the Saint Denis bank robbery.",
       "Il est tué en 1899 pendant le braquage de la banque de Saint-Denis."),
 ],
 "sections": [
   {"summary": two("Biography","Biographie"), "open": True, "blocks": [
     {"h3": two("Origins","Origines")},
     {"p": two("Lenny's father, an educated man, taught him to read and write. When Lenny was 15, his father was killed by drunken men; Lenny took a gun and shot them. He spent three years on the run before joining the gang.",
               "Le père de Lenny, un homme instruit, lui apprend à lire et à écrire. Quand Lenny a 15 ans, son père est tué par des hommes ivres ; Lenny prend une arme et les abat. Il passe trois ans en fuite avant de rejoindre le gang.")},
     {"h3": two("In the gang","Au sein du gang")},
     {"p": two(f"In {cl(1,'chapter 1','en')}, Lenny takes part in the raid on the O'Driscoll camp. In {cl(2,'chapter 2','en')}, he scouts Strawberry with [[micah-bell|Micah Bell]]; Micah is arrested and Lenny rides back to camp alone. In \"A Quiet Time\", he and Arthur spend a night drinking at a saloon in Valentine.",
               f"Au {cl(1,'chapitre 1','fr')}, Lenny participe à l'attaque du camp des O'Driscoll. Au {cl(2,'chapitre 2','fr')}, il part en reconnaissance à Strawberry avec [[micah-bell|Micah Bell]] ; Micah est arrêté et Lenny regagne seul le camp. Dans \"A Quiet Time\", Arthur et lui passent une nuit à boire dans un saloon de Valentine.")},
     {"p": two(f"In {cl(3,'chapter 3','en')}, in \"Preaching Forgiveness as He Went\", a tip from Black residents of Rhodes leads Lenny and Arthur to the Lemoyne Raiders hiding at Shady Belle, whom they kill before seizing their weapons. Lenny also robs the Valentine bank with Arthur, Bill and [[karen-jones|Karen]].",
               f"Au {cl(3,'chapitre 3','fr')}, dans \"Preaching Forgiveness as He Went\", un renseignement d'habitants noirs de Rhodes conduit Lenny et Arthur jusqu'aux Lemoyne Raiders retranchés à Shady Belle, qu'ils éliminent avant de s'emparer de leurs armes. Lenny braque aussi la banque de Valentine avec Arthur, Bill et [[karen-jones|Karen]].")},
     {"h3": two("Death","Mort")},
     {"p": two(f"In {cl(4,'chapter 4','en')}, during \"Banking, The Old American Art\", the robbery of the Saint Denis bank goes wrong. Lenny is shot by Pinkertons during the escape across the rooftops. [[hosea-matthews|Hosea Matthews]] is killed the same day.",
               f"Au {cl(4,'chapitre 4','fr')}, dans \"Banking, The Old American Art\", le braquage de la banque de Saint-Denis tourne mal. Lenny est abattu par les Pinkerton pendant la fuite sur les toits. [[hosea-matthews|Hosea Matthews]] est tué le même jour.")},
   ]},
   {"summary": two("Development and performance","Conception et interprétation"), "blocks": [
     {"p": two("Lenny is played by Harron Atkins, who provided the voice and the motion capture.",
               "Lenny est interprété par Harron Atkins, qui assure la voix et la capture de mouvement.")},
     {"p": two("Interviewed by Twinfinite in February 2019, Roger Clark, who plays Arthur, said the saloon scene was shot over \"two or three days\" and that by then he knew Atkins \"very well\". Rockstar told him the scene would use \"really frenetic editing\", unlike the rest of the game, to convey drunkenness.",
               "Interrogé par Twinfinite en février 2019, Roger Clark, l'interprète d'Arthur, explique que la scène du saloon a été tournée sur deux ou trois jours, à un moment où il connaissait déjà très bien Harron Atkins. Rockstar lui avait annoncé un montage volontairement frénétique, à l'opposé du reste du jeu, pour rendre l'ivresse.")},
   ]},
   {"summary": two("Reception","Accueil"), "blocks": [
     {"p": two("In February 2019, Game Informer's Jason Guisao described Lenny as \"a vocal reminder of the heightened racial tensions that plagued the wild frontier\" and called \"Preaching Forgiveness as He Went\" \"particularly striking\". The same month, Slate's Jonathan S. Jones cited Lenny, Arthur's \"protégé\", as part of the game's \"overt commentary about the brutality of life under slavery and Jim Crow\".",
               "En février 2019, Jason Guisao, dans Game Informer, voit en Lenny un rappel explicite des tensions raciales de la Frontière et juge la mission \"Preaching Forgiveness as He Went\" particulièrement marquante. Le même mois, Jonathan S. Jones, dans Slate, cite Lenny, le protégé d'Arthur, parmi les éléments par lesquels le jeu commente ouvertement la brutalité de l'esclavage et des lois Jim Crow.")},
   ]},
 ],
 "rel_after": 0,
 "relationships": [
   {"img": "arthur.jpeg", "slug": "arthur-morgan", "name": "Arthur Morgan", "text": two(
     "His closest friend in the gang, from the Valentine saloon to Shady Belle.",
     "Son ami le plus proche dans le gang, du saloon de Valentine à Shady Belle.")},
   {"img": "micah.jpeg", "slug": "micah-bell", "name": "Micah Bell", "text": two(
     "Scouts Strawberry with him before being arrested.",
     "Part en reconnaissance avec lui à Strawberry avant d'être arrêté.")},
   {"img": "hosea.jpeg", "slug": "hosea-matthews", "name": "Hosea Matthews", "text": two(
     "Killed on the same day, during the Saint Denis bank job.",
     "Tué le même jour, lors du braquage de Saint-Denis.")},
   {"img": "sean.jpeg", "slug": "sean-macguire", "name": "Sean MacGuire", "text": two(
     "A fellow young member of the gang.",
     "Autre jeune membre du gang.")},
   {"img": "dutch.jpeg", "slug": "dutch-van-der-linde", "name": "Dutch van der Linde", "text": two(
     "Leads the Saint Denis robbery that costs Lenny his life.",
     "Mène le braquage de Saint-Denis qui coûte la vie à Lenny.")},
 ],
 "gallery": [
   {"img": "gallery-1.jpeg", "alt": two("Lenny Summers","Lenny Summers"), "cap": two("Lenny Summers.","Lenny Summers.")},
 ],
 "related": ["arthur-morgan", "hosea-matthews", "micah-bell", "sean-macguire"],
},
# ============================ KIERAN DUFFY ============================
{
 "slug": "kieran-duffy", "name": "Kieran Duffy",
 "publishDate": "2026-07-01", "updated": "2026-10-06", "schema_game": "Red Dead Redemption 2",
 "reg_role_en": "Van der Linde gang &middot; RDR2", "reg_role_fr": "Gang Van der Linde &middot; RDR2",
 "gender": "Male", "death": "1899", "nationality": "American",
 "portrait_alt": two("Kieran Duffy in Red Dead Redemption 2", "Kieran Duffy dans Red Dead Redemption 2"),
 "eyebrow": two("Character &middot; Van der Linde gang", "Personnage &middot; Gang Van der Linde"),
 "meta_desc": two("Kieran Duffy: former O'Driscoll who joins the Van der Linde gang in Red Dead Redemption 2. His capture, how he earns his place, and his murder by the O'Driscolls at Shady Belle.",
                  "Kieran Duffy : ancien O'Driscoll qui rejoint le gang Van der Linde dans Red Dead Redemption 2. Sa capture, comment il gagne sa place, et son assassinat par les O'Driscoll à Shady Belle."),
 "og_desc": two("The captured O'Driscoll who changes sides, and whose murder opens the attack on Shady Belle.",
                "L'O'Driscoll capturé qui change de camp, et dont l'assassinat ouvre l'attaque de Shady Belle."),
 "schema_desc": two("Former O'Driscoll Boys member who joins the Van der Linde gang in Red Dead Redemption 2.",
                    "Ancien membre des O'Driscoll Boys devenu membre du gang Van der Linde dans Red Dead Redemption 2."),
 "chips": [two("Died <strong>1899</strong>", "Mort en <strong>1899</strong>"), two("Deceased", "Décédé"),
           two("Van der Linde gang", "Gang Van der Linde"), two("Former O'Driscoll", "Ancien O'Driscoll")],
 "facts": [
   {"label": two("Died","Mort"), "value": two("1899","1899")},
   {"label": two("Status","Statut"), "value": two("Deceased","Décédé")},
   {"label": two("Affiliation","Affiliation"), "value": two("O'Driscoll Boys (former), Van der Linde gang","O'Driscoll Boys (ancien), gang Van der Linde")},
   {"label": two("Role","Rôle"), "value": two("Stable hand","Palefrenier")},
   {"label": two("Voiced by","Voix"), "value": two("Pico Alexander","Pico Alexander")},
   {"label": two("Games","Jeux"), "value": two("Red Dead Redemption 2","Red Dead Redemption 2")},
 ],
 "intro": [
   two("Kieran Duffy is a former low-ranking member of the O'Driscoll Boys who joins the Van der Linde gang after being captured, in Red Dead Redemption 2.",
       "Kieran Duffy est un ancien sous-fifre des O'Driscoll Boys qui rejoint le gang Van der Linde après avoir été capturé, dans Red Dead Redemption 2."),
   two("He is murdered by the O'Driscolls in 1899, and his body is sent back to the gang's camp at Shady Belle.",
       "Il est assassiné par les O'Driscoll en 1899, et son corps est renvoyé au camp du gang à Shady Belle."),
 ],
 "sections": [
   {"summary": two("Biography","Biographie"), "open": True, "blocks": [
     {"h3": two("Prisoner","Prisonnier")},
     {"p": two(f"In {cl(1,'chapter 1','en')}, in \"Old Friends\", the gang raids an O'Driscoll camp. [[arthur-morgan|Arthur]] chases Kieran down, ropes him and brings him back to the Colter camp as a prisoner. At Horseshoe Overlook, he is kept tied to a tree.",
               f"Au {cl(1,'chapitre 1','fr')}, dans \"Old Friends\", le gang attaque un camp des O'Driscoll. [[arthur-morgan|Arthur]] rattrape Kieran, le prend au lasso et le ramène prisonnier au camp de Colter. À Horseshoe Overlook, il reste attaché à un arbre.")},
     {"p": two(f"In {cl(2,'chapter 2','en')}, in \"Paying a Social Call\", [[dutch-van-der-linde|Dutch]] orders [[bill-williamson|Bill]] to castrate him. Under the threat, Kieran reveals an O'Driscoll safehouse, Six Point Cabin, and leads Arthur, John and Bill there. [[colm-odriscoll|Colm O'Driscoll]] is not there. When an O'Driscoll jumps Arthur at the door, Kieran shoots him and saves Arthur's life. Arthur then lets him join the gang.",
               f"Au {cl(2,'chapitre 2','fr')}, dans \"Paying a Social Call\", [[dutch-van-der-linde|Dutch]] ordonne à [[bill-williamson|Bill]] de le castrer. Sous la menace, Kieran livre une planque des O'Driscoll, Six Point Cabin, et y conduit Arthur, John et Bill. [[colm-odriscoll|Colm O'Driscoll]] n'y est pas. Quand un O'Driscoll se jette sur Arthur à la porte, Kieran l'abat et lui sauve la vie. Arthur accepte alors qu'il rejoigne le gang.")},
     {"h3": two("In the gang","Au sein du gang")},
     {"p": two("Kieran works with the horses at camp. According to the official guide, several members of the gang never fully accept him.",
               "Kieran s'occupe des chevaux au camp. D'après le guide officiel, plusieurs membres du gang ne l'acceptent jamais vraiment.")},
     {"h3": two("Death","Mort")},
     {"p": two(f"In {cl(4,'chapter 4','en')}, Kieran disappears. In \"Horsemen, Apocalypses\", his body rides into the Shady Belle camp on his horse: he has been beheaded and his eyes gouged out. The O'Driscolls attack the camp immediately afterwards. Dutch has him buried by Charles, Pearson and Reverend Swanson.",
               f"Au {cl(4,'chapitre 4','fr')}, Kieran disparaît. Dans \"Horsemen, Apocalypses\", son corps arrive au camp de Shady Belle sur son cheval : il a été décapité et a les yeux crevés. Les O'Driscoll attaquent le camp dans la foulée. Dutch le fait enterrer par Charles, Pearson et le révérend Swanson.")},
   ]},
   {"summary": two("Development and performance","Conception et interprétation"), "blocks": [
     {"p": two("Kieran is played by Pico Alexander, an American actor born in New York in 1991, who provided the voice and the motion capture.",
               "Kieran est interprété par Pico Alexander, acteur américain né à New York en 1991, qui assure la voix et la capture de mouvement.")},
   ]},
   {"summary": two("Reception","Accueil"), "blocks": [
     {"p": two("In its December 2018 ranking of the gang's members, Game Informer placed Kieran 20th out of 24, noting \"a lot of pathos in his struggle for acceptance\", a journey \"cut short just as everyone starts to warm up to him\".",
               "Dans son classement des membres du gang publié en décembre 2018, Game Informer place Kieran 20e sur 24, en soulignant ce que sa quête d'acceptation a de poignant, et un parcours interrompu au moment même où le camp commence à l'adopter.")},
   ]},
 ],
 "rel_after": 0,
 "relationships": [
   {"img": "arthur.jpeg", "slug": "arthur-morgan", "name": "Arthur Morgan", "text": two(
     "Captures him, then owes him his life at Six Point Cabin.",
     "Le capture, puis lui doit la vie à Six Point Cabin.")},
   {"img": "bill.jpeg", "slug": "bill-williamson", "name": "Bill Williamson", "text": two(
     "Ordered by Dutch to castrate him, before Kieran talks.",
     "Chargé par Dutch de le castrer, avant que Kieran ne parle.")},
   {"img": "colm.jpeg", "slug": "colm-odriscoll", "name": "Colm O'Driscoll", "text": two(
     "The leader of the gang he leaves, and whose men kill him.",
     "Le chef du gang qu'il quitte, dont les hommes le tuent.")},
   {"img": "dutch.jpeg", "slug": "dutch-van-der-linde", "name": "Dutch van der Linde", "text": two(
     "Has him interrogated, then buried.",
     "Le fait interroger, puis enterrer.")},
 ],
 "gallery": [
   {"img": "gallery-1.jpeg", "alt": two("Kieran Duffy in the mountains","Kieran Duffy dans les montagnes"),
    "cap": two("Kieran during the gang's time in the mountains.","Kieran pendant le séjour du gang dans les montagnes.")},
 ],
 "related": ["colm-odriscoll", "bill-williamson", "arthur-morgan", "dutch-van-der-linde"],
},
# ============================ ORVILLE SWANSON ============================
{
 "slug": "orville-swanson", "name": "Orville Swanson",
 "publishDate": "2026-08-26", "updated": "2026-10-06", "schema_game": "Red Dead Redemption 2",
 "reg_role_en": "Gang chaplain &middot; RDR2", "reg_role_fr": "Aumônier du gang &middot; RDR2",
 "gender": "Male", "death": None, "nationality": "American",
 "portrait_alt": two("Reverend Orville Swanson in Red Dead Redemption 2", "Le révérend Orville Swanson dans Red Dead Redemption 2"),
 "eyebrow": two("Character &middot; Van der Linde gang", "Personnage &middot; Gang Van der Linde"),
 "meta_desc": two("Reverend Orville Swanson: the former clergyman of the Van der Linde gang in Red Dead Redemption 2. His addictions, his rescue by Arthur, his sobriety, and his New York church in 1907.",
                  "Le révérend Orville Swanson : l'ancien homme d'Église du gang Van der Linde dans Red Dead Redemption 2. Ses addictions, son sauvetage par Arthur, sa sobriété retrouvée, et son église new-yorkaise en 1907."),
 "og_desc": two("The gang's fallen reverend, who gets sober after Guarma and leads a New York church by 1907.",
                "Le révérend déchu du gang, qui retrouve la sobriété après Guarma et dirige une église new-yorkaise en 1907."),
 "schema_desc": two("Former clergyman and member of the Van der Linde gang in Red Dead Redemption 2.",
                    "Ancien homme d'Église, membre du gang Van der Linde dans Red Dead Redemption 2."),
 "chips": [two("Van der Linde gang", "Gang Van der Linde"), two("Alive in 1907", "Vivant en 1907"),
           two("Reverend", "Révérend"), two("RDR2", "RDR2")],
 "facts": [
   {"label": two("Affiliation","Affiliation"), "value": two("Van der Linde gang","Gang Van der Linde")},
   {"label": two("Role","Rôle"), "value": two("Former clergyman","Ancien homme d'Église")},
   {"label": two("In 1907","En 1907"), "value": two("Minister of the First Congregational Church of New York","Pasteur de la First Congregational Church de New York")},
   {"label": two("Status","Statut"), "value": two("Alive in 1907","Vivant en 1907")},
   {"label": two("Voiced by","Voix"), "value": two("Sean Haberle","Sean Haberle")},
   {"label": two("Games","Jeux"), "value": two("Red Dead Redemption 2","Red Dead Redemption 2")},
 ],
 "intro": [
   two("Reverend Orville Swanson is a former clergyman and a member of the Van der Linde gang in Red Dead Redemption 2. Rockstar's description notes that, had he not once saved Dutch's life, the gang would probably not have kept him around.",
       "Le révérend Orville Swanson est un ancien homme d'Église, membre du gang Van der Linde dans Red Dead Redemption 2. Selon la présentation de Rockstar, s'il n'avait pas jadis sauvé la vie de Dutch, le gang ne l'aurait sans doute pas gardé si longtemps."),
   two("He gets sober, leaves the gang before its collapse, and leads a church in New York by 1907.",
       "Il retrouve la sobriété, quitte le gang avant sa chute, et dirige une église à New York en 1907."),
 ],
 "sections": [
   {"summary": two("Biography","Biographie"), "open": True, "blocks": [
     {"h3": two("A fallen reverend","Un révérend déchu")},
     {"p": two("Swanson says he lost his vocation, his faith and his family. He is addicted to morphine and alcohol. He once saved [[dutch-van-der-linde|Dutch]]'s life, which is why the gang keeps him; the game never explains how.",
               "Swanson dit avoir perdu sa vocation, sa foi et sa famille. Il est dépendant à la morphine et à l'alcool. Il a autrefois sauvé la vie de [[dutch-van-der-linde|Dutch]], ce qui explique que le gang le garde ; le jeu ne dit jamais dans quelles circonstances.")},
     {"p": two("He speaks the game's first line, in the snowstorm of the opening mission, about the dying Davey Callahan: \"Abigail says he's dying, Dutch. We'll have to stop someplace.\"",
               "C'est lui qui prononce la toute première réplique du jeu, dans la tempête de neige de la mission d'ouverture, au sujet de Davey Callahan, mourant : Abigail dit qu'il va mourir et qu'il faut s'arrêter quelque part.")},
     {"h3": two("Who is Not Without Sin","Who is Not Without Sin")},
     {"p": two(f"In {cl(2,'chapter 2','en')}, in \"Who is Not Without Sin\", [[arthur-morgan|Arthur]] finds him drunk at Flatneck Station, playing poker. Arthur saves him from a beating, then pulls him off the Bard's Crossing railway bridge, where his foot is stuck in the tracks, just before a train passes, and brings him back to camp.",
               f"Au {cl(2,'chapitre 2','fr')}, dans \"Who is Not Without Sin\", [[arthur-morgan|Arthur]] le retrouve ivre à Flatneck Station, en pleine partie de poker. Il le tire d'une bagarre, puis le dégage du pont ferroviaire de Bard's Crossing, où son pied est coincé dans les rails, juste avant le passage d'un train, et le ramène au camp.")},
     {"h3": two("Sobriety and departure","Sobriété et départ")},
     {"p": two(f"In {cl(4,'chapter 4','en')}, after the O'Driscoll attack on Shady Belle, Dutch has him bury [[kieran-duffy|Kieran Duffy]] with [[charles-smith|Charles]] and [[simon-pearson|Pearson]]. After the gang's return from Guarma, Swanson is sober. He leaves the gang at {cl(6,'Beaver Hollow','en')}.",
               f"Au {cl(4,'chapitre 4','fr')}, après l'attaque des O'Driscoll sur Shady Belle, Dutch le charge d'enterrer [[kieran-duffy|Kieran Duffy]] avec [[charles-smith|Charles]] et [[simon-pearson|Pearson]]. Après le retour de Guarma, Swanson est sobre. Il quitte le gang à {cl(6,'Beaver Hollow','fr')}.")},
     {"p": two("At the end of \"The Fine Art of Conversation\", if Arthur's honor is low or he has not completed \"Of Men and Angels\", Swanson is the one Arthur meets at Emerald Station, boarding a train. Otherwise, Arthur meets Sister Calderón there.",
               "À la fin de \"The Fine Art of Conversation\", si l'honneur d'Arthur est bas ou s'il n'a pas fait \"Of Men and Angels\", c'est Swanson qu'Arthur croise à Emerald Station, sur le point de prendre un train. Sinon, il y rencontre sœur Calderón.")},
     {"h3": two("1907","1907")},
     {"p": two("An in-game newspaper article, \"Reverend Swanson Leads NY Church\", reports that he has become minister of the First Congregational Church of New York, after preaching on street corners and serving as an assistant pastor in Ohio.",
               "Un article de presse du jeu, \"Reverend Swanson Leads NY Church\", annonce qu'il est devenu pasteur de la First Congregational Church de New York, après avoir prêché au coin des rues puis servi comme pasteur adjoint dans l'Ohio.")},
   ]},
   {"summary": two("Development and performance","Conception et interprétation"), "blocks": [
     {"p": two("Swanson is played by Sean Haberle, an American actor who provided the voice and the motion capture.",
               "Swanson est interprété par Sean Haberle, acteur américain qui assure la voix et la capture de mouvement.")},
   ]},
   {"summary": two("Reception","Accueil"), "blocks": [
     {"p": two("Game Informer's December 2018 ranking of the gang placed Swanson 17th, describing a character who \"bounces back and forth between a wise man and fool\". Polygon's Colin Campbell called him \"the drunken, self-loathing padre\" in November 2018. In April 2019, GamesRadar cited Swanson and Uncle as addicts the camp protects and shelters.",
               "Le classement du gang publié par Game Informer en décembre 2018 place Swanson 17e, un personnage qui oscille selon le magazine entre le sage et le fou. Dans Polygon, en novembre 2018, Colin Campbell voit en lui le prêtre ivrogne qui se méprise. En avril 2019, GamesRadar cite Swanson et Uncle comme des dépendants que le camp protège et héberge.")},
   ]},
 ],
 "rel_after": 0,
 "relationships": [
   {"img": "dutch.jpeg", "slug": "dutch-van-der-linde", "name": "Dutch van der Linde", "text": two(
     "Owes him his life, which is why the gang keeps Swanson.",
     "Lui doit la vie, raison pour laquelle le gang garde Swanson.")},
   {"img": "arthur.jpeg", "slug": "arthur-morgan", "name": "Arthur Morgan", "text": two(
     "Rescues him at Flatneck Station and on the Bard's Crossing bridge.",
     "Le sauve à Flatneck Station et sur le pont de Bard's Crossing.")},
   {"img": "charles.jpeg", "slug": "charles-smith", "name": "Charles Smith", "text": two(
     "Buries Kieran Duffy with him.",
     "Enterre Kieran Duffy avec lui.")},
 ],
 "gallery": [
   {"img": "gallery-1.jpeg", "alt": two("Swanson's bible box","La bible de Swanson"),
    "cap": two("Swanson's \"bible\", a box in which he hides his addictions.","La \"bible\" de Swanson, une boîte où il cache ses addictions.")},
 ],
 "related": ["dutch-van-der-linde", "arthur-morgan", "charles-smith", "molly-oshea"],
},
]
ENRICHED += BATCH2

# ---- Batch 3 (6 Oct 2026): Strauss, Trelawny, Susan Grimshaw, Uncle ----
BATCH3 = [
# ============================ LEOPOLD STRAUSS ============================
{
 "slug": "leopold-strauss", "name": "Leopold Strauss",
 "publishDate": "2026-07-03", "updated": "2026-10-06", "schema_game": "Red Dead Redemption 2",
 "reg_role_en": "Van der Linde gang &middot; RDR2", "reg_role_fr": "Gang Van der Linde &middot; RDR2",
 "gender": "Male", "death": "1899", "nationality": "Austrian",
 "portrait_alt": two("Leopold Strauss in Red Dead Redemption 2", "Leopold Strauss dans Red Dead Redemption 2"),
 "eyebrow": two("Character &middot; Van der Linde gang", "Personnage &middot; Gang Van der Linde"),
 "meta_desc": two("Leopold Strauss: the Van der Linde gang's money lender in Red Dead Redemption 2. His past in Vienna, the debt collections, the Downes debt behind Arthur's tuberculosis, and his fate.",
                  "Leopold Strauss : l'usurier du gang Van der Linde dans Red Dead Redemption 2. Son passé à Vienne, les recouvrements de dettes, la dette Downes à l'origine de la tuberculose d'Arthur, et son sort."),
 "og_desc": two("The gang's loan shark, whose debt collections give Arthur tuberculosis.",
                "L'usurier du gang, dont les recouvrements de dettes valent à Arthur sa tuberculose."),
 "schema_desc": two("Austrian bookkeeper and money lender of the Van der Linde gang in Red Dead Redemption 2.",
                    "Comptable et usurier autrichien du gang Van der Linde dans Red Dead Redemption 2."),
 "chips": [two("Died <strong>1899</strong>", "Mort en <strong>1899</strong>"), two("Deceased", "Décédé"),
           two("Van der Linde gang", "Gang Van der Linde"), two("Money lender", "Usurier")],
 "facts": [
   {"label": two("Origin","Origine"), "value": two("Vienna, Austria","Vienne, Autriche")},
   {"label": two("Died","Mort"), "value": two("1899, in Pinkerton custody","1899, détenu par les Pinkerton")},
   {"label": two("Status","Statut"), "value": two("Deceased","Décédé")},
   {"label": two("Affiliation","Affiliation"), "value": two("Van der Linde gang","Gang Van der Linde")},
   {"label": two("Role","Rôle"), "value": two("Bookkeeper and money lender","Comptable et usurier")},
   {"label": two("Voiced by","Voix"), "value": two("Howard Pinhasik","Howard Pinhasik")},
   {"label": two("Games","Jeux"), "value": two("Red Dead Redemption 2","Red Dead Redemption 2")},
 ],
 "intro": [
   two("Leopold Strauss is the bookkeeper of the Van der Linde gang in Red Dead Redemption 2, and runs its money-lending business. He sends [[arthur-morgan|Arthur Morgan]] to collect the debts.",
       "Leopold Strauss est le comptable du gang Van der Linde dans Red Dead Redemption 2, et gère son activité de prêt d'argent. C'est lui qui envoie [[arthur-morgan|Arthur Morgan]] recouvrer les dettes."),
   two("One of those collections is how Arthur catches tuberculosis.",
       "C'est lors de l'un de ces recouvrements qu'Arthur contracte la tuberculose."),
 ],
 "sections": [
   {"summary": two("Biography","Biographie"), "open": True, "blocks": [
     {"h3": two("Origins","Origines")},
     {"p": two("According to the official guide, Strauss grew up poor in Vienna and was often ill as a child. He was sent to America by boat at 17, spent years as a swindler, and joined [[dutch-van-der-linde|Dutch]]'s gang for protection.",
               "D'après le guide officiel, Strauss grandit pauvre à Vienne et souffre de problèmes de santé dans l'enfance. Envoyé en Amérique par bateau à 17 ans, il vit plusieurs années d'escroqueries, puis rejoint le gang de [[dutch-van-der-linde|Dutch]] pour s'assurer une protection.")},
     {"h3": two("The debt collections","Les recouvrements")},
     {"p": two(f"From {cl(2,'chapter 2','en')} onwards, Strauss gives Arthur a series of missions titled \"Money Lending and Other Sins\", in which Arthur collects debts from borrowers across the map. In the third, Arthur beats a sick farmer, Thomas Downes, who coughs blood on him. This is where Arthur contracts tuberculosis. After Downes dies, Strauss passes the debt on to his widow, Edith.",
               f"À partir du {cl(2,'chapitre 2','fr')}, Strauss confie à Arthur une série de missions intitulées \"Money Lending and Other Sins\", où Arthur recouvre des dettes aux quatre coins de la carte. Dans la troisième, Arthur roue de coups un fermier malade, Thomas Downes, qui lui crache du sang au visage. C'est ainsi qu'Arthur contracte la tuberculose. À la mort de Downes, Strauss reporte la dette sur sa veuve, Edith.")},
     {"p": two(f"In {cl(4,'chapter 4','en')}, Strauss takes part in the gang's robbery aboard the riverboat Grand Korrigan, with Arthur, Javier and [[josiah-trelawny|Josiah Trelawny]].",
               f"Au {cl(4,'chapitre 4','fr')}, Strauss participe au braquage du bateau à aubes Grand Korrigan, avec Arthur, Javier et [[josiah-trelawny|Josiah Trelawny]].")},
     {"h3": two("Expulsion and fate","Exclusion et sort")},
     {"p": two(f"In {cl(6,'chapter 6','en')}, Arthur throws Strauss out of the camp for ruining lives with his loans, and gives him money as he leaves. In the 1907 epilogue, [[charles-smith|Charles Smith]] tells John Marston that Strauss was arrested by the Pinkertons, interrogated, and died in custody without giving up the gang. His death is reported, not shown.",
               f"Au {cl(6,'chapitre 6','fr')}, Arthur chasse Strauss du camp pour avoir brisé des vies avec ses prêts, et lui donne de l'argent avant son départ. Dans l'épilogue de 1907, [[charles-smith|Charles Smith]] apprend à John Marston que Strauss a été arrêté par les Pinkerton, interrogé, et qu'il est mort en détention sans livrer le gang. Sa mort est rapportée, pas montrée.")},
   ]},
   {"summary": two("Development and performance","Conception et interprétation"), "blocks": [
     {"p": two("Strauss is played by Howard Pinhasik.",
               "Strauss est interprété par Howard Pinhasik.")},
   ]},
   {"summary": two("Reception","Accueil"), "blocks": [
     {"p": two("Game Informer's December 2018 ranking of the gang placed Strauss 23rd, noting that \"it's his cruel business that results in Arthur getting infected with tuberculosis\". In Polygon, Colin Campbell described him as \"a slightly sinister money lender complete with a German accent and a taste for cruelty\".",
               "Le classement du gang publié par Game Informer en décembre 2018 place Strauss 23e, en rappelant que c'est son commerce cruel qui vaut à Arthur sa tuberculose. Dans Polygon, Colin Campbell voit en lui un usurier vaguement inquiétant, à l'accent germanique et au goût prononcé pour la cruauté.")},
   ]},
 ],
 "rel_after": 0,
 "relationships": [
   {"img": "arthur.jpeg", "slug": "arthur-morgan", "name": "Arthur Morgan", "text": two(
     "Collects his debts, catches tuberculosis doing it, then throws him out.",
     "Recouvre ses dettes, y contracte la tuberculose, puis le chasse du camp.")},
   {"img": "dutch.jpeg", "slug": "dutch-van-der-linde", "name": "Dutch van der Linde", "text": two(
     "Gives him the gang's protection and its books.",
     "Lui offre la protection du gang et lui confie ses comptes.")},
   {"img": "trelawny.jpeg", "slug": "josiah-trelawny", "name": "Josiah Trelawny", "text": two(
     "Plans the riverboat robbery he takes part in.",
     "Monte le braquage du bateau à aubes auquel il participe.")},
   {"img": "charles.jpeg", "slug": "charles-smith", "name": "Charles Smith", "text": two(
     "Tells John in 1907 that Strauss died in custody.",
     "Apprend à John, en 1907, que Strauss est mort en détention.")},
 ],
 "gallery": [
   {"img": "gallery-1.jpeg", "alt": two("Strauss at the Horseshoe Overlook camp","Strauss au camp de Horseshoe Overlook"),
    "cap": two("Strauss at the gang's Horseshoe Overlook camp.","Strauss au camp de Horseshoe Overlook.")},
 ],
 "related": ["arthur-morgan", "dutch-van-der-linde", "josiah-trelawny", "charles-smith"],
},
# ============================ JOSIAH TRELAWNY ============================
{
 "slug": "josiah-trelawny", "name": "Josiah Trelawny",
 "publishDate": "2026-07-12", "updated": "2026-10-06", "schema_game": "Red Dead Redemption 2",
 "reg_role_en": "Van der Linde gang &middot; RDR2", "reg_role_fr": "Gang Van der Linde &middot; RDR2",
 "gender": "Male", "death": None, "nationality": None,
 "portrait_alt": two("Josiah Trelawny in Red Dead Redemption 2", "Josiah Trelawny dans Red Dead Redemption 2"),
 "eyebrow": two("Character &middot; Van der Linde gang", "Personnage &middot; Gang Van der Linde"),
 "meta_desc": two("Josiah Trelawny: conman and magician associated with the Van der Linde gang in Red Dead Redemption 2 and Red Dead Online. His schemes, the riverboat heist, his family, and his departure.",
                  "Josiah Trelawny : escroc et magicien associé au gang Van der Linde dans Red Dead Redemption 2 et Red Dead Online. Ses combines, le braquage du bateau à aubes, sa famille, et son départ."),
 "og_desc": two("The gang's well-dressed conman and magician, who comes and goes as he pleases and leaves for good in chapter 6.",
                "L'escroc et magicien tiré à quatre épingles du gang, qui va et vient à sa guise et part pour de bon au chapitre 6."),
 "schema_desc": two("Conman and magician associated with the Van der Linde gang in Red Dead Redemption 2.",
                    "Escroc et magicien associé au gang Van der Linde dans Red Dead Redemption 2."),
 "chips": [two("Van der Linde gang", "Gang Van der Linde"), two("Con man", "Escroc"),
           two("Fate unknown", "Sort inconnu"), two("RDR2 &amp; Online", "RDR2 et Online")],
 "facts": [
   {"label": two("Affiliation","Affiliation"), "value": two("Van der Linde gang (associate)","Gang Van der Linde (associé)")},
   {"label": two("Role","Rôle"), "value": two("Conman and magician","Escroc et magicien")},
   {"label": two("Family","Famille"), "value": two("Wife and two sons, in Saint Denis","Une épouse et deux fils, à Saint-Denis")},
   {"label": two("Status","Statut"), "value": two("Leaves the gang in 1899","Quitte le gang en 1899")},
   {"label": two("Voiced by","Voix"), "value": two("Stephen Gevedon","Stephen Gevedon")},
   {"label": two("Games","Jeux"), "value": two("Red Dead Redemption 2, Red Dead Online","Red Dead Redemption 2, Red Dead Online")},
 ],
 "intro": [
   two("Josiah Trelawny is a conman and magician associated with the Van der Linde gang in Red Dead Redemption 2. According to the official guide, he is allowed to come and go from Dutch's gang as he pleases.",
       "Josiah Trelawny est un escroc et magicien associé au gang Van der Linde dans Red Dead Redemption 2. D'après le guide officiel, il est libre d'aller et venir dans le gang de Dutch à sa guise."),
   two("He leaves for good in chapter 6, and also appears in Red Dead Online.",
       "Il part pour de bon au chapitre 6, et apparaît aussi dans Red Dead Online."),
 ],
 "sections": [
   {"summary": two("Biography","Biographie"), "open": True, "blocks": [
     {"h3": two("The gang's fixer","L'homme des combines")},
     {"p": two(f"In {cl(2,'chapter 2','en')}, Trelawny brings Dutch word that bounty hunters are holding [[sean-macguire|Sean MacGuire]]. In \"The First Shall Be Last\", he fakes a fit to distract the guards while [[arthur-morgan|Arthur]] and Javier move in, and Sean is freed.",
               f"Au {cl(2,'chapitre 2','fr')}, Trelawny apprend à Dutch que des chasseurs de primes retiennent [[sean-macguire|Sean MacGuire]]. Dans \"The First Shall Be Last\", il simule un malaise pour distraire les gardes pendant qu'[[arthur-morgan|Arthur]] et Javier approchent, et Sean est libéré.")},
     {"p": two(f"In {cl(3,'chapter 3','en')}, he twice ends up in the hands of others: in a prison wagon in \"The New South\", then held by bounty hunters until Arthur and Charles free him in \"Magicians for Sport\". In \"Friends in Very Low Places\", he distracts an opera singer while Arthur opens a strongbox, on a tip from a Rhodes postal clerk.",
               f"Au {cl(3,'chapitre 3','fr')}, il tombe deux fois entre de mauvaises mains : dans un fourgon cellulaire dans \"The New South\", puis aux mains de chasseurs de primes jusqu'à ce qu'Arthur et Charles le libèrent dans \"Magicians for Sport\". Dans \"Friends in Very Low Places\", il distrait un chanteur d'opéra pendant qu'Arthur ouvre un coffre, sur un tuyau d'un employé des postes de Rhodes.")},
     {"p": two(f"In {cl(4,'chapter 4','en')}, in \"A Fine Night of Debauchery\", he plans the robbery of the riverboat Grand Korrigan. He has Arthur shaved and dressed for the occasion. The job, with Arthur, Javier and [[leopold-strauss|Strauss]], ends in a shootout and a swim to shore.",
               f"Au {cl(4,'chapitre 4','fr')}, dans \"A Fine Night of Debauchery\", il monte le braquage du bateau à aubes Grand Korrigan. Il fait raser et habiller Arthur pour l'occasion. Le coup, mené avec Arthur, Javier et [[leopold-strauss|Strauss]], finit en fusillade et en retour à la nage.")},
     {"h3": two("Family and departure","Famille et départ")},
     {"p": two(f"Trelawny has a wife and two sons in Saint Denis, who know nothing of his criminal life. At the start of \"The Fine Art of Conversation\", in {cl(6,'chapter 6','en')}, he leaves the gang for good, with Arthur's blessing. His fate afterwards is not shown.",
               f"Trelawny a une épouse et deux fils à Saint-Denis, qui ignorent tout de ses activités criminelles. Au début de \"The Fine Art of Conversation\", au {cl(6,'chapitre 6','fr')}, il quitte le gang pour de bon, avec la bénédiction d'Arthur. La suite de son histoire n'est pas montrée.")},
     {"h3": two("Red Dead Online","Red Dead Online")},
     {"p": two("In Red Dead Online, Trelawny lives in a caravan near Rhodes. He introduces himself by faking a suicide, the gun turning into a bird, then gives the player a series of jobs, starting with the theft of one of Catherine Braithwaite's horses.",
               "Dans Red Dead Online, Trelawny vit dans une roulotte près de Rhodes. Il se présente en simulant un suicide, son arme se changeant en oiseau, puis confie au joueur une série de missions, à commencer par le vol d'un cheval de Catherine Braithwaite.")},
   ]},
   {"summary": two("Development and performance","Conception et interprétation"), "blocks": [
     {"p": two("Trelawny is played by Stephen Gevedon, an American actor who co-wrote and starred in the film Session 9 (2001) and appeared in the series Oz and The Deuce.",
               "Trelawny est interprété par Stephen Gevedon, acteur américain, coscénariste et interprète du film Session 9 (2001), vu aussi dans les séries Oz et The Deuce.")},
     {"p": two("In an October 2019 podcast interview with ComiCulture, Gevedon said he did not know at casting that the project was a game, and expected about a week of recording. He described the character's accent as a \"bad Katharine Hepburn\", chosen in part to keep Trelawny mysterious. Rockstar later expanded the role, adding his wife and children in the final years of development.",
               "Dans un entretien en podcast avec ComiCulture, en octobre 2019, Gevedon raconte avoir ignoré au casting qu'il s'agissait d'un jeu, et s'attendre à une semaine d'enregistrement. Il compare l'accent du personnage à une \"mauvaise Katharine Hepburn\", un choix fait en partie pour garder Trelawny mystérieux. Rockstar a ensuite étoffé le rôle, en ajoutant sa femme et ses enfants dans les dernières années du développement.")},
   ]},
   {"summary": two("Reception","Accueil"), "blocks": [
     {"p": two("In Polygon, in November 2018, Colin Campbell described Trelawny as \"an affectatious dandy, a gentleman thief with swell togs and a crisp English accent\".",
               "Dans Polygon, en novembre 2018, Colin Campbell voit en Trelawny un dandy maniéré, un gentleman cambrioleur élégamment vêtu à l'accent anglais impeccable.")},
   ]},
 ],
 "rel_after": 0,
 "relationships": [
   {"img": "arthur.jpeg", "slug": "arthur-morgan", "name": "Arthur Morgan", "text": two(
     "His partner on most of his schemes, who lets him leave in peace.",
     "Son partenaire dans la plupart de ses combines, qui le laisse partir en paix.")},
   {"img": "sean.jpeg", "slug": "sean-macguire", "name": "Sean MacGuire", "text": two(
     "Rescued with his help in chapter 2.",
     "Libéré avec son aide au chapitre 2.")},
   {"img": "strauss.jpeg", "slug": "leopold-strauss", "name": "Leopold Strauss", "text": two(
     "Part of his riverboat robbery.",
     "Participe à son braquage du bateau à aubes.")},
   {"img": "dutch.jpeg", "slug": "dutch-van-der-linde", "name": "Dutch van der Linde", "text": two(
     "Lets him come and go from the gang as he pleases.",
     "Le laisse aller et venir dans le gang à sa guise.")},
 ],
 "gallery": [
   {"img": "gallery-1.jpeg", "alt": two("Josiah Trelawny","Josiah Trelawny"),
    "cap": two("Trelawny, the gang's conman and magician.","Trelawny, l'escroc et magicien du gang.")},
 ],
 "related": ["arthur-morgan", "sean-macguire", "leopold-strauss", "dutch-van-der-linde"],
},
# ============================ SUSAN GRIMSHAW ============================
{
 "slug": "susan-grimshaw", "name": "Susan Grimshaw",
 "publishDate": "2026-07-04", "updated": "2026-10-06", "schema_game": "Red Dead Redemption 2",
 "reg_role_en": "Van der Linde gang &middot; RDR2", "reg_role_fr": "Gang Van der Linde &middot; RDR2",
 "gender": "Female", "death": "1899", "nationality": "American",
 "portrait_alt": two("Susan Grimshaw in Red Dead Redemption 2", "Susan Grimshaw dans Red Dead Redemption 2"),
 "eyebrow": two("Character &middot; Van der Linde gang", "Personnage &middot; Gang Van der Linde"),
 "meta_desc": two("Susan Grimshaw: the camp's enforcer in the Van der Linde gang in Red Dead Redemption 2. Her past with Dutch, Tilly's rescue, Molly's death, her stand against Micah, and Kaili Vernoff's performance.",
                  "Susan Grimshaw : l'autorité du camp du gang Van der Linde dans Red Dead Redemption 2. Son passé avec Dutch, le sauvetage de Tilly, la mort de Molly, son face-à-face avec Micah, et l'interprétation de Kaili Vernoff."),
 "og_desc": two("The camp's iron-willed matriarch, who sides with Arthur against Micah and is killed for it.",
                "La matriarche intraitable du camp, qui se range du côté d'Arthur contre Micah et le paie de sa vie."),
 "schema_desc": two("Camp matriarch of the Van der Linde gang in Red Dead Redemption 2.",
                    "Matriarche du camp du gang Van der Linde dans Red Dead Redemption 2."),
 "chips": [two("Died <strong>1899</strong>", "Morte en <strong>1899</strong>"), two("Deceased", "Décédée"),
           two("Van der Linde gang", "Gang Van der Linde"), two("Camp matriarch", "Matriarche du camp")],
 "facts": [
   {"label": two("Died","Mort"), "value": two("1899","1899")},
   {"label": two("Status","Statut"), "value": two("Deceased","Décédée")},
   {"label": two("Nationality","Nationalité"), "value": two("American","Américaine")},
   {"label": two("Affiliation","Affiliation"), "value": two("Van der Linde gang","Gang Van der Linde")},
   {"label": two("Role","Rôle"), "value": two("Runs the camp","Dirige le camp")},
   {"label": two("Voiced by","Voix"), "value": two("Kaili Vernoff","Kaili Vernoff")},
   {"label": two("Games","Jeux"), "value": two("Red Dead Redemption 2","Red Dead Redemption 2")},
 ],
 "intro": [
   two("Susan Grimshaw runs the camp of the Van der Linde gang in Red Dead Redemption 2. Rockstar describes her as \"the undisputed boss and arbiter of justice in the camp\".",
       "Susan Grimshaw dirige le camp du gang Van der Linde dans Red Dead Redemption 2. Rockstar la présente comme la patronne incontestée du camp, celle qui y fait la loi."),
   two("She is killed by Micah Bell in 1899, after taking Arthur's side against him.",
       "Elle est tuée par Micah Bell en 1899, après avoir pris le parti d'Arthur contre lui."),
 ],
 "sections": [
   {"summary": two("Biography","Biographie"), "open": True, "blocks": [
     {"h3": two("The camp's authority","L'autorité du camp")},
     {"p": two("According to the official guide, Grimshaw was once in a relationship with [[dutch-van-der-linde|Dutch]]; after it ended, she remained his loyal partner. She has been in the gang as long as [[arthur-morgan|Arthur]]. With [[simon-pearson|Pearson]], she sets up each new camp, and she makes sure everyone does their share of the work, especially the younger women.",
               "D'après le guide officiel, Grimshaw a eu une liaison avec [[dutch-van-der-linde|Dutch]] ; une fois celle-ci terminée, elle est restée sa fidèle alliée. Elle fait partie du gang depuis aussi longtemps qu'[[arthur-morgan|Arthur]]. Avec [[simon-pearson|Pearson]], elle installe chaque nouveau camp, et veille à ce que chacun fasse sa part, à commencer par les plus jeunes femmes.")},
     {"h3": two("Tilly's rescue","Le sauvetage de Tilly")},
     {"p": two(f"In {cl(4,'chapter 4','en')}, in \"No, No and Thrice, No\", the Foreman Brothers kidnap [[tilly-jackson|Tilly Jackson]]. Grimshaw and Arthur free her at Radley's House; Grimshaw kills a guard with a knife. Whether to kill or spare the captured Anthony Foreman is left to Arthur.",
               f"Au {cl(4,'chapitre 4','fr')}, dans \"No, No and Thrice, No\", les frères Foreman enlèvent [[tilly-jackson|Tilly Jackson]]. Grimshaw et Arthur la libèrent à Radley's House ; Grimshaw poignarde un garde. Le sort d'Anthony Foreman, capturé, est laissé au choix d'Arthur.")},
     {"h3": two("Molly O'Shea","Molly O'Shea")},
     {"p": two(f"At the new camp at {cl(6,'Beaver Hollow','en')}, a drunk [[molly-oshea|Molly O'Shea]] claims she told the Pinkertons about the Saint Denis bank job. Grimshaw shoots her dead with a shotgun, saying Molly \"knew the rules\", and has the body burned. Molly's claim later turns out to be false.",
               f"Au nouveau camp de {cl(6,'Beaver Hollow','fr')}, une [[molly-oshea|Molly O'Shea]] ivre affirme avoir renseigné les Pinkerton sur le braquage de Saint-Denis. Grimshaw l'abat d'un coup de fusil, en expliquant que Molly connaissait les règles, et fait brûler le corps. L'aveu de Molly se révèle faux par la suite.")},
     {"h3": two("Death","Mort")},
     {"p": two("In the final mission of chapter 6, \"Red Dead Redemption\", Arthur names [[micah-bell|Micah Bell]] as the gang's traitor. Grimshaw is the only one to side openly with Arthur and John, and turns her shotgun on Micah. Distracted by the arrival of the Pinkertons, she is shot dead by Micah. [[charles-smith|Charles Smith]] later buries her.",
               "Dans la dernière mission du chapitre 6, \"Red Dead Redemption\", Arthur désigne [[micah-bell|Micah Bell]] comme le traître du gang. Grimshaw est la seule à se ranger ouvertement du côté d'Arthur et de John, et braque son fusil sur Micah. Distraite par l'arrivée des Pinkerton, elle est abattue par Micah. [[charles-smith|Charles Smith]] l'enterre plus tard.")},
   ]},
   {"summary": two("Development and performance","Conception et interprétation"), "blocks": [
     {"p": two("Grimshaw is played by Kaili Vernoff. Speaking to Forbes in February 2019, she said she worked on the game \"for about four and a half years, off and on\", and that it was both the first video game she had worked on and the first she had ever played. She had previously voiced a minor character in Grand Theft Auto V.",
               "Grimshaw est interprétée par Kaili Vernoff. Auprès de Forbes, en février 2019, elle explique avoir travaillé sur le jeu environ quatre ans et demi, par intermittence, et que c'était à la fois le premier jeu vidéo sur lequel elle travaillait et le premier auquel elle jouait. Elle avait auparavant prêté sa voix à un personnage secondaire de Grand Theft Auto V.")},
     {"p": two("In the same interview, she described Susan's code: \"Everyone must earn their keep; she cannot abide hangers on or laziness; and she values loyalty above all.\" Speaking to GameFragger the same month, she said she wanted Susan's vulnerability to come through as she came to understand the character, and that \"Susan dies defending her family and she wouldn't have it any other way.\"",
               "Dans le même entretien, elle résume le code de Susan : chacun doit mériter sa place, elle ne supporte ni les parasites ni la paresse, et place la loyauté au-dessus de tout. Auprès de GameFragger, le même mois, elle dit avoir voulu faire ressortir la vulnérabilité du personnage à mesure qu'elle le comprenait, et estime que Susan meurt en défendant sa famille, comme elle l'aurait voulu.")},
   ]},
   {"summary": two("Reception","Accueil"), "blocks": [
     {"p": two("In Polygon, in November 2018, Colin Campbell called Grimshaw \"literally a walking cliché\", comparing her to frontier matriarchs of classic westerns and television, such as Ma Ingalls in Little House on the Prairie.",
               "Dans Polygon, en novembre 2018, Colin Campbell voit en Grimshaw un cliché ambulant, et la rapproche des matriarches de la Frontière des westerns classiques et de la télévision, comme Ma Ingalls dans La Petite Maison dans la prairie.")},
   ]},
 ],
 "rel_after": 0,
 "relationships": [
   {"img": "dutch.jpeg", "slug": "dutch-van-der-linde", "name": "Dutch van der Linde", "text": two(
     "Her former partner, to whom she stays loyal until Micah's betrayal.",
     "Son ancien compagnon, à qui elle reste fidèle jusqu'à la trahison de Micah.")},
   {"img": "tilly.jpeg", "slug": "tilly-jackson", "name": "Tilly Jackson", "text": two(
     "Rescued by her and Arthur from the Foreman Brothers.",
     "Libérée par Arthur et elle des frères Foreman.")},
   {"img": "molly.jpeg", "slug": "molly-oshea", "name": "Molly O'Shea", "text": two(
     "Shot by Grimshaw after her false confession.",
     "Abattue par Grimshaw après son faux aveu.")},
   {"img": "micah.jpeg", "slug": "micah-bell", "name": "Micah Bell", "text": two(
     "The traitor she confronts, and who kills her.",
     "Le traître qu'elle affronte, et qui la tue.")},
   {"img": "arthur.jpeg", "slug": "arthur-morgan", "name": "Arthur Morgan", "text": two(
     "The one she sides with at the end.",
     "Celui dont elle prend le parti à la fin.")},
 ],
 "gallery": [
   {"img": "gallery-1.jpeg", "alt": two("Susan Grimshaw at the camp","Susan Grimshaw au camp"),
    "cap": two("Susan keeping the camp's younger members in line.","Susan tient les plus jeunes du camp.")},
 ],
 "related": ["tilly-jackson", "molly-oshea", "micah-bell", "dutch-van-der-linde"],
},
# ============================ UNCLE ============================
{
 "slug": "uncle", "name": "Uncle",
 "publishDate": "2026-07-14", "updated": "2026-10-06", "schema_game": "Red Dead Redemption 2",
 "reg_role_en": "Van der Linde gang &middot; RDR1 &amp; 2", "reg_role_fr": "Gang Van der Linde &middot; RDR1 &amp; 2",
 "gender": "Male", "death": "1911", "nationality": "American",
 "portrait_alt": two("Uncle in Red Dead Redemption 2", "Uncle dans Red Dead Redemption 2"),
 "eyebrow": two("Character &middot; Van der Linde gang", "Personnage &middot; Gang Van der Linde"),
 "meta_desc": two("Uncle: the oldest drinker of the Van der Linde gang in Red Dead Redemption 2 and the Marstons' companion at Beecher's Hope in Red Dead Redemption. Biography, his death in 1911, and his three actors.",
                  "Uncle : le vieux buveur du gang Van der Linde dans Red Dead Redemption 2 et le compagnon des Marston à Beecher's Hope dans Red Dead Redemption. Biographie, sa mort en 1911, et ses trois interprètes."),
 "og_desc": two("The gang's work-shy old drinker, who follows the Marstons to Beecher's Hope and dies defending it in 1911.",
                "Le vieux buveur fainéant du gang, qui suit les Marston à Beecher's Hope et meurt en le défendant en 1911."),
 "schema_desc": two("Aging member of the Van der Linde gang and companion of the Marston family in Red Dead Redemption and Red Dead Redemption 2.",
                    "Vieux membre du gang Van der Linde et compagnon de la famille Marston dans Red Dead Redemption et Red Dead Redemption 2."),
 "chips": [two("Died <strong>1911</strong>", "Mort en <strong>1911</strong>"), two("Deceased", "Décédé"),
           two("Van der Linde gang", "Gang Van der Linde"), two("RDR1 &amp; 2", "RDR1 et 2")],
 "facts": [
   {"label": two("Real name","Vrai nom"), "value": two("Never given","Jamais révélé")},
   {"label": two("Died","Mort"), "value": two("1911, Beecher's Hope","1911, Beecher's Hope")},
   {"label": two("Status","Statut"), "value": two("Deceased","Décédé")},
   {"label": two("Affiliation","Affiliation"), "value": two("Van der Linde gang, Marston ranch","Gang Van der Linde, ranch des Marston")},
   {"label": two("Voiced by","Voix"), "value": two("Spider Madison (RDR1); John O'Creagh and James McBride (RDR2)","Spider Madison (RDR1) ; John O'Creagh et James McBride (RDR2)")},
   {"label": two("Games","Jeux"), "value": two("Red Dead Redemption, Red Dead Redemption 2","Red Dead Redemption, Red Dead Redemption 2")},
 ],
 "intro": [
   two("Uncle is one of the oldest members of the Van der Linde gang. His real name is never given. Rockstar describes him as \"always around when the whiskey is open and never around when there's any work to be done\".",
       "Uncle est l'un des plus vieux membres du gang Van der Linde. Son vrai nom n'est jamais donné. Rockstar le décrit comme toujours là quand le whisky est ouvert, et jamais quand il y a du travail."),
   two("He appears in Red Dead Redemption 2 and in Red Dead Redemption, where he dies defending the Marston ranch in 1911.",
       "Il apparaît dans Red Dead Redemption 2 et dans Red Dead Redemption, où il meurt en défendant le ranch des Marston en 1911."),
 ],
 "sections": [
   {"summary": two("Biography","Biographie"), "open": True, "blocks": [
     {"h3": two("In the gang","Au sein du gang")},
     {"p": two("According to the official guide, Uncle is a heavy drinker who claims to have had several wives, travelled widely, and been a gifted gunslinger in his youth. He blames his reluctance to work on \"terminal lumbago\". He introduced [[abigail-marston|Abigail]] to the gang around 1894.",
               "D'après le guide officiel, Uncle est un gros buveur qui affirme avoir eu plusieurs épouses, beaucoup voyagé et été un pistolero doué dans sa jeunesse. Il met son peu d'empressement au travail sur le compte d'un \"lumbago en phase terminale\". C'est lui qui a fait entrer [[abigail-marston|Abigail]] dans le gang, vers 1894.")},
     {"p": two(f"In {cl(2,'chapter 2','en')}, he takes part in the outing to Valentine with [[arthur-morgan|Arthur]], Karen, Mary-Beth and Tilly. In {cl(3,'chapter 3','en')}, in \"An Honest Mistake\", his tip about an unguarded Cornwall coach leads Arthur, Bill, Charles and Uncle into a fight with Cornwall's men, which they escape from a barn.",
               f"Au {cl(2,'chapitre 2','fr')}, il participe à la sortie à Valentine avec [[arthur-morgan|Arthur]], Karen, Mary-Beth et Tilly. Au {cl(3,'chapitre 3','fr')}, dans \"An Honest Mistake\", son tuyau sur une diligence de Cornwall prétendument sans escorte entraîne Arthur, Bill, Charles et Uncle dans un affrontement avec les hommes de Cornwall, dont ils s'échappent depuis une grange.")},
     {"p": two(f"At {cl(6,'Beaver Hollow','en')}, he brings a drunk [[molly-oshea|Molly O'Shea]] back from Saint Denis, on the night she is killed. He leaves the gang shortly afterwards; Dutch announces that he, Pearson and Mary-Beth have run away.",
               f"À {cl(6,'Beaver Hollow','fr')}, il ramène de Saint-Denis une [[molly-oshea|Molly O'Shea]] ivre, le soir où elle est tuée. Il quitte le gang peu après ; Dutch annonce que Pearson, Mary-Beth et lui ont pris la fuite.")},
     {"h3": two("Beecher's Hope (1907)","Beecher's Hope (1907)")},
     {"p": two(f"In the {cl('E1','epilogue','en')}, Uncle meets [[john-marston|John Marston]] in Blackwater as John buys the land at Beecher's Hope, and insists on helping. He tells John that [[charles-smith|Charles]] is in Saint Denis, and the three build the ranch, Uncle mostly giving orders. After a celebration, the Skinner Brothers kidnap him and burn his back; John and Charles rescue him. He stays on the ranch with the Marstons.",
               f"Dans l'{cl('E1','épilogue','fr')}, Uncle retrouve [[john-marston|John Marston]] à Blackwater au moment où John achète le terrain de Beecher's Hope, et insiste pour l'aider. Il lui apprend que [[charles-smith|Charles]] est à Saint-Denis, et tous trois bâtissent le ranch, Uncle se contentant surtout de donner des ordres. Après une soirée de fête, les frères Skinner l'enlèvent et lui brûlent le dos ; John et Charles le délivrent. Il reste au ranch avec les Marston.")},
     {"h3": two("Death (1911)","Mort (1911)")},
     {"p": two(f"In Red Dead Redemption, Uncle looks after the ranch, badly, while John is away hunting his former gang. In {cl('A3','the third act','en')}, in \"The Last Enemy That Shall Be Destroyed\", soldiers and agents led by Edgar Ross attack Beecher's Hope. Uncle helps defend the ranch and is shot dead.",
               f"Dans Red Dead Redemption, Uncle veille sur le ranch, tant bien que mal, pendant que John traque son ancien gang. Dans {cl('A3','le troisième acte','fr')}, au cours de \"The Last Enemy That Shall Be Destroyed\", des soldats et des agents menés par Edgar Ross attaquent Beecher's Hope. Uncle participe à la défense du ranch et y est abattu.")},
   ]},
   {"summary": two("Development and performance","Conception et interprétation"), "blocks": [
     {"p": two("In Red Dead Redemption (2010), Uncle is played by Spider Madison. For Red Dead Redemption 2, the role first went to John O'Creagh, who died during production; James McBride took over, while O'Creagh's singing lines were kept in the game. A lake in Ambarino, O'Creagh's Run, is named after him.",
               "Dans Red Dead Redemption (2010), Uncle est interprété par Spider Madison. Pour Red Dead Redemption 2, le rôle revient d'abord à John O'Creagh, mort pendant la production ; James McBride lui succède, tandis que les passages chantés enregistrés par O'Creagh sont conservés dans le jeu. Un lac de l'Ambarino, O'Creagh's Run, porte son nom.")},
   ]},
 ],
 "rel_after": 0,
 "relationships": [
   {"img": "john.jpeg", "slug": "john-marston", "name": "John Marston", "text": two(
     "Builds Beecher's Hope with him, and loses him in 1911.",
     "Bâtit Beecher's Hope avec lui, et le perd en 1911.")},
   {"img": "charles.jpeg", "slug": "charles-smith", "name": "Charles Smith", "text": two(
     "Helps build the ranch and rescues him from the Skinner Brothers.",
     "Aide à bâtir le ranch et le tire des griffes des frères Skinner.")},
   {"img": "abigail.jpeg", "slug": "abigail-marston", "name": "Abigail Marston", "text": two(
     "Brought into the gang by Uncle around 1894.",
     "Entrée dans le gang par son intermédiaire, vers 1894.")},
   {"img": "molly.jpeg", "slug": "molly-oshea", "name": "Molly O'Shea", "text": two(
     "Brought back drunk by him on the night she dies.",
     "Ramenée ivre par lui le soir de sa mort.")},
   {"img": "arthur.jpeg", "slug": "arthur-morgan", "name": "Arthur Morgan", "text": two(
     "Rides with him to Valentine and on the Cornwall coach job.",
     "L'accompagne à Valentine et lors de l'attaque de la diligence de Cornwall.")},
 ],
 "gallery": [
   {"img": "gallery-1.jpeg", "alt": two("Uncle at the camp","Uncle au camp"),
    "cap": two("Uncle, the gang's work-shy old survivor.","Uncle, le vieux rescapé fainéant du gang.")},
 ],
 "related": ["john-marston", "charles-smith", "abigail-marston", "molly-oshea"],
},
]
ENRICHED += BATCH3

# ---- Main characters 1 (6 Oct 2026): Arthur, John, Dutch ----
VID_CLARK = {"id": "pl2ZPoevd0I",
  "title": two("Roger Clark wins Best Performance for Red Dead Redemption 2 at The Game Awards 2018",
               "Roger Clark reçoit le prix de la meilleure interprétation pour Red Dead Redemption 2 aux Game Awards 2018"),
  "cap": two("Roger Clark accepting Best Performance at The Game Awards 2018.",
             "Roger Clark reçoit le prix de la meilleure interprétation aux Game Awards 2018.")}
BH = "Beecher's Hope"
MAINS1 = [
# ============================ ARTHUR MORGAN ============================
{
 "slug": "arthur-morgan", "name": "Arthur Morgan",
 "publishDate": "2026-06-22", "updated": "2026-10-06", "schema_game": "Red Dead Redemption 2",
 "reg_role_en": "Van der Linde gang &middot; RDR2", "reg_role_fr": "Gang Van der Linde &middot; RDR2",
 "gender": "Male", "death": "1899", "nationality": "American",
 "portrait_alt": two("Arthur Morgan in Red Dead Redemption 2", "Arthur Morgan dans Red Dead Redemption 2"),
 "eyebrow": two("Character &middot; Van der Linde gang", "Personnage &middot; Gang Van der Linde"),
 "meta_desc": two("Arthur Morgan: protagonist of Red Dead Redemption 2. His story from Colter to the four endings, his tuberculosis, the break with Dutch, Roger Clark's performance and the character's awards.",
                  "Arthur Morgan : le héros de Red Dead Redemption 2. Son histoire de Colter aux quatre fins, sa tuberculose, la rupture avec Dutch, l'interprétation de Roger Clark et les récompenses du personnage."),
 "og_desc": two("Dutch's most trusted enforcer, whose illness and break with the gang drive Red Dead Redemption 2.",
                "Le plus fidèle homme de main de Dutch, dont la maladie et la rupture avec le gang portent Red Dead Redemption 2."),
 "schema_desc": two("Protagonist of Red Dead Redemption 2 and senior member of the Van der Linde gang.",
                    "Personnage principal de Red Dead Redemption 2 et pilier du gang Van der Linde."),
 "chips": [two("Died <strong>1899</strong>", "Mort en <strong>1899</strong>"), two("Deceased", "Décédé"),
           two("Van der Linde gang", "Gang Van der Linde"), two("Voiced by <strong>Roger Clark</strong>", "Voix de <strong>Roger Clark</strong>")],
 "facts": [
   {"label": two("Born","Naissance"), "value": two("Around 1863","Vers 1863")},
   {"label": two("Died","Mort"), "value": two("1899","1899")},
   {"label": two("Status","Statut"), "value": two("Deceased","Décédé")},
   {"label": two("Nationality","Nationalité"), "value": two("American","Américaine")},
   {"label": two("Affiliation","Affiliation"), "value": two("Van der Linde gang","Gang Van der Linde")},
   {"label": two("Role","Rôle"), "value": two("Senior enforcer, Dutch's right-hand man","Homme de main, bras droit de Dutch")},
   {"label": two("Family","Famille"), "value": two("Son Isaac, with Eliza (both killed)","Un fils, Isaac, avec Eliza (tous deux tués)")},
   {"label": two("Games","Jeux"), "value": two("Red Dead Redemption 2, Red Dead Online","Red Dead Redemption 2, Red Dead Online")},
   {"label": two("Voiced by","Voix"), "value": two("Roger Clark","Roger Clark")},
 ],
 "intro": [
   two("Arthur Morgan is the protagonist of Red Dead Redemption 2 (2018). Rockstar presents him as \"Dutch's most trusted enforcer\", a member of the Van der Linde gang since his teens.",
       "Arthur Morgan est le héros de Red Dead Redemption 2 (2018). Rockstar le présente comme l'homme de main le plus fidèle de Dutch, membre du gang Van der Linde depuis l'adolescence."),
   two("He is played by Roger Clark, whose performance won Best Performance at The Game Awards 2018.",
       "Il est interprété par Roger Clark, récompensé pour ce rôle par le prix de la meilleure interprétation aux Game Awards 2018."),
 ],
 "sections": [
   {"summary": two("Biography","Biographie"), "open": True, "blocks": [
     {"h3": two("Origins","Origines")},
     {"p": two("According to the official guide, Arthur lost his parents young and joined [[dutch-van-der-linde|Dutch van der Linde]]'s gang at 14, becoming Dutch's first protégé alongside [[hosea-matthews|Hosea Matthews]]. With a waitress named Eliza, he had a son, Isaac; he sent them money until both were killed in a robbery. He was once engaged to [[mary-linton|Mary Gillis]], now Mary Linton.",
               "D'après le guide officiel, Arthur perd ses parents jeune et entre à 14 ans dans le gang de [[dutch-van-der-linde|Dutch van der Linde]], dont il devient le premier protégé aux côtés d'[[hosea-matthews|Hosea Matthews]]. Avec une serveuse nommée Eliza, il a un fils, Isaac ; il leur envoie de l'argent jusqu'à ce que tous deux soient tués lors d'un vol. Il a autrefois été fiancé à [[mary-linton|Mary Gillis]], devenue Mary Linton.")},
     {"figure": {"img": "gang.jpeg", "alt": two("Dutch van der Linde addresses the Van der Linde gang in the forest","Dutch van der Linde s'adresse au gang Van der Linde dans la forêt"),
                 "cap": two("The Van der Linde gang, Arthur's family since his teens.","Le gang Van der Linde, la famille d'Arthur depuis l'adolescence.")}},
     {"h3": two("1899: the gang on the run","1899 : le gang en fuite")},
     {"p": two(f"After a failed ferry robbery in Blackwater, the gang flees into the snowbound mountains of {cl(1,'chapter 1','en')}, where Arthur and Javier rescue [[john-marston|John Marston]] from wolves. In {cl(2,'chapter 2','en')}, while collecting a debt for [[leopold-strauss|Leopold Strauss]], Arthur beats a sick farmer, Thomas Downes, who coughs blood on him: this is how Arthur contracts tuberculosis.",
               f"Après un braquage raté sur un ferry à Blackwater, le gang fuit dans les montagnes enneigées du {cl(1,'chapitre 1','fr')}, où Arthur et Javier tirent [[john-marston|John Marston]] des griffes des loups. Au {cl(2,'chapitre 2','fr')}, en recouvrant une dette pour [[leopold-strauss|Leopold Strauss]], Arthur roue de coups un fermier malade, Thomas Downes, qui lui crache du sang au visage : c'est ainsi qu'il contracte la tuberculose.")},
     {"p": two(f"In {cl(3,'chapter 3','en')}, the gang's double game between the Grays and the Braithwaites ends with [[jack-marston|Jack Marston]] kidnapped and handed to [[angelo-bronte|Angelo Bronte]]. In {cl(4,'chapter 4','en')}, Arthur brings Jack back; Dutch drowns Bronte, an act Arthur finds out of character. The Saint Denis bank robbery turns out to be a Pinkerton trap: Hosea and [[lenny-summers|Lenny]] are killed and John is arrested. The survivors are shipwrecked on {cl(5,'Guarma','en')}.",
               f"Au {cl(3,'chapitre 3','fr')}, le double jeu du gang entre les Gray et les Braithwaite aboutit à l'enlèvement de [[jack-marston|Jack Marston]], livré à [[angelo-bronte|Angelo Bronte]]. Au {cl(4,'chapitre 4','fr')}, Arthur ramène Jack ; Dutch noie Bronte, un geste qu'Arthur ne lui reconnaît pas. Le braquage de la banque de Saint-Denis se révèle un piège des Pinkerton : Hosea et [[lenny-summers|Lenny]] sont tués, John est arrêté. Les survivants font naufrage à {cl(5,'Guarma','fr')}.")},
     {"h3": two("Illness and the break with Dutch","La maladie et la rupture avec Dutch")},
     {"p": two(f"Back on the mainland, Arthur collapses in Saint Denis, and Dr. Joseph R. Barnes diagnoses tuberculosis. In {cl(6,'chapter 6','en')}, he and [[sadie-adler|Sadie Adler]] free John from Sisika Penitentiary against Dutch's wishes, in \"Visiting Hours\". Dutch then leaves Arthur behind at the oil fields in \"My Last Boy\", leaves John for dead after the army payroll robbery in \"Our Best Selves\", and refuses to rescue Abigail. Arthur breaks with him and learns that [[micah-bell|Micah Bell]] is the Pinkertons' informant.",
               f"De retour sur le continent, Arthur s'effondre à Saint-Denis, et le docteur Joseph R. Barnes lui diagnostique la tuberculose. Au {cl(6,'chapitre 6','fr')}, il libère John du pénitencier de Sisika avec [[sadie-adler|Sadie Adler]], contre l'avis de Dutch, dans \"Visiting Hours\". Dutch l'abandonne ensuite aux champs pétrolifères dans \"My Last Boy\", laisse John pour mort après l'attaque du convoi de la solde de l'armée dans \"Our Best Selves\", et refuse de secourir Abigail. Arthur rompt avec lui et découvre que [[micah-bell|Micah Bell]] est l'informateur des Pinkerton.")},
     {"h3": two("Death: the four endings","Mort : les quatre fins")},
     {"p": two("In the final mission, \"Red Dead Redemption\", Arthur chooses on the mountain either to help John escape or to go back for the gang's money. That choice, combined with Arthur's honor, produces four endings:",
               "Dans la dernière mission, \"Red Dead Redemption\", Arthur choisit sur la montagne d'aider John à fuir ou de retourner chercher l'argent du gang. Ce choix, combiné à son niveau d'honneur, donne quatre fins :")},
     {"ul": [
       two("Helping John, high honor: Arthur dies of his illness watching the sunrise.","Aider John, honneur élevé : Arthur meurt de sa maladie face au lever du soleil."),
       two("Helping John, low honor: Micah shoots him in the head.","Aider John, honneur bas : Micah l'abat d'une balle dans la tête."),
       two("Going back for the money, high honor: after a knife fight with Micah, Arthur dies at sunrise.","Retourner chercher l'argent, honneur élevé : après un combat au couteau contre Micah, Arthur meurt au lever du soleil."),
       two("Going back for the money, low honor: Micah stabs him to death.","Retourner chercher l'argent, honneur bas : Micah le poignarde à mort."),
     ]},
     {"p": two(f"In every version, Dutch walks away. In the 1907 {cl('E2','epilogue','en')}, John, Sadie and [[charles-smith|Charles]] track Micah down on Mount Hagen, where Dutch and John kill him.",
               f"Dans toutes les versions, Dutch s'en va. Dans l'{cl('E2','épilogue','fr')} de 1907, John, Sadie et [[charles-smith|Charles]] retrouvent Micah au mont Hagen, où Dutch et John le tuent.")},
     {"figure": {"img": "ending.jpeg", "alt": two("A lone figure against a still sunrise, echoing Arthur's final dawn","Une silhouette solitaire face à un lever de soleil, écho du dernier matin d'Arthur"),
                 "cap": two("The high-honor endings close on a sunrise.","Les fins à honneur élevé s'achèvent sur un lever de soleil.")}},
   ]},
   {"summary": two("As a playable character","Le personnage jouable"), "blocks": [
     {"ul": [
       two("The player controls Arthur for the six chapters of the main story; the epilogue switches to John Marston.",
           "Le joueur incarne Arthur pendant les six chapitres de l'histoire principale ; l'épilogue passe à John Marston."),
       two("An honor system tracks his actions. It changes some dialogue and scenes, and decides how his last scene plays out.",
           "Un système d'honneur suit ses actes. Il modifie certains dialogues et certaines scènes, et décide du déroulement de sa dernière scène."),
       two("Arthur keeps a journal of sketches and notes, updated as the story advances.",
           "Arthur tient un journal de croquis et de notes, enrichi au fil de l'histoire."),
       two("His weight changes with how much the player makes him eat, and his tuberculosis visibly marks his face and body in the later chapters.",
           "Son poids varie selon ce que le joueur lui fait manger, et sa tuberculose marque visiblement son visage et son corps dans les derniers chapitres."),
     ]},
   ]},
   {"summary": two("Development and performance","Conception et interprétation"), "blocks": [
     {"p": two("After the three protagonists of Grand Theft Auto V, Rockstar returned to a single lead. \"Sticking with a single character felt more appropriate for the structure and narrative of a Western\", Rockstar's Josh Bass told The Hollywood Reporter in September 2018.",
               "Après les trois héros de Grand Theft Auto V, Rockstar revient à un personnage principal unique. Un choix plus adapté à la structure et au récit d'un western, explique Josh Bass, de Rockstar, au Hollywood Reporter en septembre 2018.")},
     {"p": two("Writer Dan Houser told GQ that, instead of the usual arc of a hero who grows stronger, Arthur is strong from the outset and \"is going to be taken on a more intellectual roller coaster when his world view gets taken apart\". He told Vulture that a second love interest for Arthur was written and then cut, as part of about five hours removed from the game. In a 2025 podcast interview, Houser said an early opening in which Arthur's baby died was also cut, because \"it was too tough in some ways\".",
               "Le scénariste Dan Houser explique à GQ qu'au lieu de l'arc habituel d'un héros qui gagne en puissance, Arthur est fort d'emblée et voit plutôt sa vision du monde démontée pièce par pièce. Il confie à Vulture qu'une seconde histoire d'amour pour Arthur a été écrite puis coupée, parmi environ cinq heures retirées du jeu. Dans un podcast en 2025, Houser évoque aussi une ouverture abandonnée, où le bébé d'Arthur mourait, jugée trop dure.")},
     {"figure": {"img": "roger-clark.jpeg", "alt": two("Roger Clark, the actor behind Arthur Morgan","Roger Clark, l'interprète d'Arthur Morgan"),
                 "cap": two("Roger Clark, who played Arthur through performance capture.","Roger Clark, qui a joué Arthur en capture de performance.")}},
     {"p": two("Arthur is played by Roger Clark, an Irish-American actor born in 1978 who grew up near Sligo, in Ireland. His first day on the project was in August 2013, and he described the role as \"five years of work\", mostly in performance capture rather than in a voice booth. He told The Hollywood Reporter that he drew on Toshiro Mifune and John Wayne for the character.",
               "Arthur est interprété par Roger Clark, acteur irlando-américain né en 1978, qui a grandi près de Sligo, en Irlande. Son premier jour sur le projet date d'août 2013, et il parle de \"cinq ans de travail\", pour l'essentiel en capture de performance plutôt qu'en cabine. Il explique au Hollywood Reporter s'être inspiré de Toshiro Mifune et de John Wayne.")},
     {"video": VID_CLARK},
   ]},
   {"summary": two("Reception","Accueil"), "blocks": [
     {"p": two("Roger Clark won Best Performance at The Game Awards 2018. He was nominated for Performer at the 2019 BAFTA Games Awards, and Arthur was nominated for Outstanding Achievement in Character at the 2019 D.I.C.E. Awards; both awards went to God of War.",
               "Roger Clark remporte le prix de la meilleure interprétation aux Game Awards 2018. Il est nommé aux BAFTA Games Awards 2019 dans la catégorie interprète, et Arthur est nommé aux D.I.C.E. Awards 2019 pour le meilleur personnage ; les deux prix reviennent à God of War.")},
     {"p": two("Reviewing the game, IGN noted \"an infectious authenticity\" in Clark's voice, and Kotaku wrote that Clark \"brings Arthur to life with uncommon confidence and consistency\". In The New York Times, Peter Suderman described Arthur as \"a bad man with a good heart, because his choices are, in fact, your own\". In an April 2024 BAFTA public poll of more than 4,000 voters, Arthur was voted the 11th most iconic video game character.",
               "Dans sa critique, IGN salue l'authenticité contagieuse de la voix de Clark, et Kotaku estime que l'acteur donne vie à Arthur avec une assurance et une constance rares. Dans le New York Times, Peter Suderman voit en Arthur un homme mauvais au bon cœur, puisque ses choix sont ceux du joueur. En avril 2024, un sondage public de la BAFTA auprès de plus de 4 000 votants le classe 11e personnage de jeu vidéo le plus emblématique.")},
   ]},
 ],
 "rel_after": 0,
 "relationships": [
   {"img": "dutch.jpeg", "slug": "dutch-van-der-linde", "name": "Dutch van der Linde", "text": two(
     "His mentor since his teens, whom he turns against in 1899.",
     "Son mentor depuis l'adolescence, contre qui il se retourne en 1899.")},
   {"img": "hosea.jpeg", "slug": "hosea-matthews", "name": "Hosea Matthews", "text": two(
     "Raised him in the gang alongside Dutch.",
     "L'a élevé dans le gang aux côtés de Dutch.")},
   {"img": "john.jpeg", "slug": "john-marston", "name": "John Marston", "text": two(
     "The brother-like figure he helps escape at the end.",
     "Le quasi-frère qu'il aide à fuir à la fin.")},
   {"img": "mary.jpeg", "slug": "mary-linton", "name": "Mary Linton", "text": two(
     "His former fiancée.",
     "Son ancienne fiancée.")},
   {"img": "micah.jpeg", "slug": "micah-bell", "name": "Micah Bell", "text": two(
     "The informant he unmasks, and his final opponent.",
     "L'informateur qu'il démasque, et son dernier adversaire.")},
   {"img": "sadie.jpeg", "slug": "sadie-adler", "name": "Sadie Adler", "text": two(
     "Frees John from Sisika with him.",
     "Libère John de Sisika avec lui.")},
 ],
 "gallery": [
   {"img": "gallery-1.jpeg", "alt": two("Arthur Morgan in his coat and hat","Arthur Morgan, manteau et chapeau"),
    "cap": two("Arthur in 1899, Red Dead Redemption 2.","Arthur en 1899, Red Dead Redemption 2.")},
   {"img": "gallery-2.jpeg", "alt": two("Red Dead Redemption 2 cover artwork featuring Arthur Morgan","Jaquette de Red Dead Redemption 2 avec Arthur Morgan"),
    "cap": two("Arthur on the Red Dead Redemption 2 cover art.","Arthur sur la jaquette de Red Dead Redemption 2.")},
 ],
 "related": ["john-marston", "dutch-van-der-linde", "micah-bell", "sadie-adler"],
},
# ============================ JOHN MARSTON ============================
{
 "slug": "john-marston", "name": "John Marston",
 "publishDate": "2026-06-23", "updated": "2026-10-06", "schema_game": "Red Dead Redemption",
 "reg_role_en": "Van der Linde gang &middot; RDR1", "reg_role_fr": "Gang Van der Linde &middot; RDR1",
 "gender": "Male", "birth": "1873", "death": "1911", "nationality": "American",
 "portrait_alt": two("John Marston in Red Dead Redemption 2", "John Marston dans Red Dead Redemption 2"),
 "eyebrow": two("Character &middot; Van der Linde gang", "Personnage &middot; Gang Van der Linde"),
 "meta_desc": two("John Marston: protagonist of Red Dead Redemption and of the Red Dead Redemption 2 epilogue. His life from the gang to Beecher's Hope, his death in 1911, Rob Wiethoff's performance and awards.",
                  "John Marston : le héros de Red Dead Redemption et de l'épilogue de Red Dead Redemption 2. Sa vie du gang à Beecher's Hope, sa mort en 1911, l'interprétation de Rob Wiethoff et ses récompenses."),
 "og_desc": two("The former outlaw forced to hunt his old gang in 1911, and the hero of both Red Dead Redemption games.",
                "L'ancien hors-la-loi contraint de traquer son ancien gang en 1911, héros des deux Red Dead Redemption."),
 "schema_desc": two("Protagonist of Red Dead Redemption and of the epilogue of Red Dead Redemption 2.",
                    "Héros de Red Dead Redemption et de l'épilogue de Red Dead Redemption 2."),
 "chips": [two("<strong>1873&ndash;1911</strong>", "<strong>1873&ndash;1911</strong>"), two("Deceased", "Décédé"),
           two("Van der Linde gang", "Gang Van der Linde"), two("Voiced by <strong>Rob Wiethoff</strong>", "Voix de <strong>Rob Wiethoff</strong>")],
 "facts": [
   {"label": two("Born","Naissance"), "value": two("1873","1873")},
   {"label": two("Died","Mort"), "value": two("1911, Beecher's Hope","1911, Beecher's Hope")},
   {"label": two("Status","Statut"), "value": two("Deceased","Décédé")},
   {"label": two("Nationality","Nationalité"), "value": two("American","Américaine")},
   {"label": two("Affiliation","Affiliation"), "value": two("Van der Linde gang (former)","Gang Van der Linde (ancien)")},
   {"label": two("Family","Famille"), "value": two("[[abigail-marston|Abigail Marston]] (wife), [[jack-marston|Jack Marston]] (son)","[[abigail-marston|Abigail Marston]] (épouse), [[jack-marston|Jack Marston]] (fils)")},
   {"label": two("Alias","Alias"), "value": two("Jim Milton (1907)","Jim Milton (1907)")},
   {"label": two("Games","Jeux"), "value": two("Red Dead Redemption, Red Dead Redemption 2, Red Dead Online","Red Dead Redemption, Red Dead Redemption 2, Red Dead Online")},
   {"label": two("Voiced by","Voix"), "value": two("Rob Wiethoff","Rob Wiethoff")},
 ],
 "intro": [
   two("John Marston is the protagonist of Red Dead Redemption (2010), a major character of Red Dead Redemption 2 (2018) and the playable character of its epilogue. Rockstar describes him as an orphaned street kid taken under Dutch's wing at twelve.",
       "John Marston est le héros de Red Dead Redemption (2010), un personnage majeur de Red Dead Redemption 2 (2018) et le personnage jouable de son épilogue. Rockstar le présente comme un gamin des rues orphelin, recueilli par Dutch à 12 ans."),
   two("He is played by Rob Wiethoff, whose performance won Outstanding Character Performance at the 2011 D.I.C.E. Awards.",
       "Il est interprété par Rob Wiethoff, récompensé aux D.I.C.E. Awards 2011 pour la meilleure interprétation d'un personnage."),
 ],
 "sections": [
   {"summary": two("Biography","Biographie"), "open": True, "blocks": [
     {"h3": two("Origins","Origines")},
     {"p": two("John was born in 1873. According to the official guide, his mother died giving birth to him, and his father, a Scottish immigrant, died when John was eight. After a few years in an orphanage, he ran away. At twelve, he was about to be hanged for theft when [[dutch-van-der-linde|Dutch van der Linde]] saved him and took him into the gang. [[abigail-marston|Abigail Roberts]] joined the gang in 1894, and their son [[jack-marston|Jack]] was born the following year.",
               "John naît en 1873. D'après le guide officiel, sa mère meurt en le mettant au monde, et son père, un immigré écossais, meurt quand John a huit ans. Après quelques années en orphelinat, il s'enfuit. À douze ans, il est sur le point d'être pendu pour vol lorsque [[dutch-van-der-linde|Dutch van der Linde]] le sauve et le fait entrer dans le gang. [[abigail-marston|Abigail Roberts]] rejoint le gang en 1894, et leur fils [[jack-marston|Jack]] naît l'année suivante.")},
     {"h3": two("Red Dead Redemption 2 (1899)","Red Dead Redemption 2 (1899)")},
     {"p": two(f"In {cl(1,'chapter 1','en')}, lost in the snow after the Blackwater robbery, John is mauled by wolves, which scar his face; [[arthur-morgan|Arthur]] and [[javier-escuella|Javier]] rescue him in \"Enter, Pursued by a Memory\". In {cl(4,'chapter 4','en')}, he is arrested during the failed Saint Denis bank robbery and sent to Sisika Penitentiary.",
               f"Au {cl(1,'chapitre 1','fr')}, perdu dans la neige après le braquage de Blackwater, John est attaqué par des loups qui lui balafrent le visage ; [[arthur-morgan|Arthur]] et [[javier-escuella|Javier]] le secourent dans \"Enter, Pursued by a Memory\". Au {cl(4,'chapitre 4','fr')}, il est arrêté lors du braquage raté de la banque de Saint-Denis et envoyé au pénitencier de Sisika.")},
     {"p": two(f"In {cl(6,'chapter 6','en')}, Arthur and [[sadie-adler|Sadie]] break him out, against Dutch's wishes. Arthur urges him to leave the gang with his family. During the army payroll robbery in \"Our Best Selves\", John is shot and falls from the train, and Dutch leaves him for dead. He returns during the final mission and escapes with Arthur's help; Arthur gives him his hat and satchel.",
               f"Au {cl(6,'chapitre 6','fr')}, Arthur et [[sadie-adler|Sadie]] le font évader, contre l'avis de Dutch. Arthur le presse de quitter le gang avec sa famille. Lors de l'attaque du convoi de la solde de l'armée, dans \"Our Best Selves\", John est touché et tombe du train, et Dutch le laisse pour mort. Il réapparaît lors de la dernière mission et s'échappe grâce à Arthur, qui lui confie son chapeau et sa sacoche.")},
     {"h3": two("The epilogue (1907)","L'épilogue (1907)")},
     {"p": two(f"In 1907, John works at Pronghorn Ranch under the name Jim Milton. Abigail leaves with Jack, and John takes a bank loan to buy land at {cl('E2',BH,'en')}, where [[uncle|Uncle]] and [[charles-smith|Charles]] help him build a house. He proposes to Abigail. In \"American Venom\", he tracks [[micah-bell|Micah Bell]] to Mount Hagen: Dutch shoots Micah first and John finishes him. John takes the gang's money, pays off the loan and marries Abigail. The game ends with Edgar Ross and Archer Fordham watching the ranch.",
               f"En 1907, John travaille au Pronghorn Ranch sous le nom de Jim Milton. Abigail part avec Jack, et John emprunte à la banque pour acheter un terrain à {cl('E2',BH,'fr')}, où [[uncle|Uncle]] et [[charles-smith|Charles]] l'aident à bâtir la maison. Il demande Abigail en mariage. Dans \"American Venom\", il retrouve [[micah-bell|Micah Bell]] au mont Hagen : Dutch tire le premier et John l'achève. John récupère l'argent du gang, rembourse son emprunt et épouse Abigail. Le jeu se clôt sur Edgar Ross et Archer Fordham, qui observent le ranch.")},
     {"h3": two("Red Dead Redemption (1911)","Red Dead Redemption (1911)")},
     {"p": two(f"In 1911, the Bureau of Investigation holds Abigail and Jack to force John to hunt down his former gang. In {cl('A1','New Austin','en')}, he is shot by [[bill-williamson|Bill Williamson]]'s men and saved by [[bonnie-macfarlane|Bonnie MacFarlane]]. In {cl('A2','Mexico','en')}, he works for both [[agustin-allende|Colonel Allende]] and the rebel [[abraham-reyes|Abraham Reyes]] to reach Bill and [[javier-escuella|Javier]]. In {cl('A3','West Elizabeth','en')}, Dutch steps off a cliff rather than be taken.",
               f"En 1911, le Bureau of Investigation retient Abigail et Jack pour forcer John à traquer son ancien gang. Dans le {cl('A1','New Austin','fr')}, il est blessé par les hommes de [[bill-williamson|Bill Williamson]] et sauvé par [[bonnie-macfarlane|Bonnie MacFarlane]]. Au {cl('A2','Mexique','fr')}, il travaille à la fois pour [[agustin-allende|le colonel Allende]] et pour le rebelle [[abraham-reyes|Abraham Reyes]] afin d'atteindre Bill et [[javier-escuella|Javier]]. Dans le {cl('A3','West Elizabeth','fr')}, Dutch se jette d'une falaise plutôt que d'être pris.")},
     {"p": two("Back at Beecher's Hope, John is reunited with his family. In \"The Last Enemy That Shall Be Destroyed\", soldiers and agents led by [[edgar-ross|Edgar Ross]] attack the ranch. Uncle is killed; John sends Abigail and Jack away and is shot dead. In 1914, after Abigail's death, Jack kills Ross in a duel. John is also the protagonist of Undead Nightmare (2010), an expansion outside the series' canon.",
               "De retour à Beecher's Hope, John retrouve sa famille. Dans \"The Last Enemy That Shall Be Destroyed\", des soldats et des agents menés par [[edgar-ross|Edgar Ross]] attaquent le ranch. Uncle est tué ; John met Abigail et Jack à l'abri et tombe sous les balles. En 1914, après la mort d'Abigail, Jack tue Ross en duel. John est aussi le héros d'Undead Nightmare (2010), une extension hors de la continuité officielle.")},
   ]},
   {"summary": two("Development and performance","Conception et interprétation"), "blocks": [
     {"p": two("Rob Wiethoff was cast after a last-minute audition for an \"untitled video game project\", in which he was handed his lines and a basket of laundry: \"Say the lines and fold the laundry\", he recalled to Polygon in 2013. He had spent about ten years in Los Angeles with little acting work, tending bar, and moved back to Seymour, Indiana, after the game.",
               "Rob Wiethoff décroche le rôle après une audition de dernière minute pour un \"projet de jeu vidéo sans titre\", où on lui remet son texte et un panier de linge : il doit dire ses répliques en pliant le linge, raconte-t-il à Polygon en 2013. Il venait de passer une dizaine d'années à Los Angeles, avec peu de rôles, en travaillant comme barman, et repart à Seymour, dans l'Indiana, après le jeu.")},
     {"p": two("Rockstar called him back in 2014 for Red Dead Redemption 2. Told the role would take about a year, he used up his leave at a construction job, then quit, and ended up working on the game for nearly four years. For the sequel, producer Rob Nelson told Variety the team \"had to be careful not to John it up too much\".",
               "Rockstar le rappelle en 2014 pour Red Dead Redemption 2. Annoncé pour un an environ, le rôle l'oblige à épuiser ses congés sur un chantier, puis à démissionner ; il travaillera finalement près de quatre ans sur le jeu. Pour cette suite, le producteur Rob Nelson explique à Variety que l'équipe a pris garde à ne pas trop mettre John en avant.")},
   ]},
   {"summary": two("Reception","Accueil"), "blocks": [
     {"p": two("Rob Wiethoff won Outstanding Character Performance at the 2011 D.I.C.E. Awards. At the 2010 Spike Video Game Awards, he was nominated for Best Performance by a Human Male, and John for Character of the Year.",
               "Rob Wiethoff remporte le prix de la meilleure interprétation d'un personnage aux D.I.C.E. Awards 2011. Aux Spike Video Game Awards 2010, il est nommé pour la meilleure interprétation masculine, et John pour le personnage de l'année.")},
     {"p": two("In The New York Times in 2010, Seth Schiesel wrote that \"the leading edge of interactive media has a new face\", belonging to John Marston. GamesRadar ranked him 5th in its 2013 list of the best game characters of the generation, and Game Informer's Javy Gwaltney called him in 2018 \"the best of the best\" among Rockstar's protagonists.",
               "Dans le New York Times, en 2010, Seth Schiesel écrit que le jeu vidéo a un nouveau visage, celui de John Marston. GamesRadar le classe 5e de sa liste des meilleurs personnages de la génération en 2013, et Javy Gwaltney, dans Game Informer, le juge en 2018 le meilleur des héros de Rockstar.")},
   ]},
 ],
 "rel_after": 0,
 "relationships": [
   {"img": "abigail.jpeg", "slug": "abigail-marston", "name": "Abigail Marston", "text": two(
     "His partner, then his wife from 1907.",
     "Sa compagne, puis son épouse à partir de 1907.")},
   {"img": "jack.jpeg", "slug": "jack-marston", "name": "Jack Marston", "text": two(
     "His son, who avenges him in 1914.",
     "Son fils, qui le venge en 1914.")},
   {"img": "arthur.jpeg", "slug": "arthur-morgan", "name": "Arthur Morgan", "text": two(
     "Saves him twice and helps him escape in 1899.",
     "Le sauve deux fois et l'aide à fuir en 1899.")},
   {"img": "dutch.jpeg", "slug": "dutch-van-der-linde", "name": "Dutch van der Linde", "text": two(
     "Saves him from the gallows at twelve, then leaves him for dead.",
     "Le sauve de la potence à douze ans, puis le laisse pour mort.")},
   {"img": "uncle.jpeg", "slug": "uncle", "name": "Uncle", "text": two(
     "Helps him build Beecher's Hope.",
     "L'aide à bâtir Beecher's Hope.")},
   {"img": "sadie.jpeg", "slug": "sadie-adler", "name": "Sadie Adler", "text": two(
     "Frees him from Sisika, then hunts Micah with him.",
     "Le fait évader de Sisika, puis traque Micah avec lui.")},
   {"img": "ross.jpeg", "slug": "edgar-ross", "name": "Edgar Ross", "text": two(
     "Coerces him in 1911, then leads the attack that kills him.",
     "Le contraint en 1911, puis mène l'assaut qui le tue.")},
 ],
 "gallery": [
   {"img": "gallery-1.jpeg", "alt": two("Official Red Dead Redemption artwork of John Marston","Artwork officiel de Red Dead Redemption représentant John Marston"),
    "cap": two("Official Red Dead Redemption key art.","Artwork officiel de Red Dead Redemption.")},
   {"img": "gallery-2.jpeg", "alt": two("John Marston on horseback at dusk","John Marston à cheval au crépuscule"),
    "cap": two("John on the trail.","John sur les pistes.")},
 ],
 "related": ["arthur-morgan", "abigail-marston", "jack-marston", "dutch-van-der-linde"],
},
# ============================ DUTCH VAN DER LINDE ============================
{
 "slug": "dutch-van-der-linde", "name": "Dutch van der Linde",
 "publishDate": "2026-06-24", "updated": "2026-10-06", "schema_game": "Red Dead Redemption 2",
 "reg_role_en": "Gang leader &middot; RDR1 &amp; 2", "reg_role_fr": "Chef de gang &middot; RDR1 &amp; 2",
 "gender": "Male", "death": "1911", "nationality": "American",
 "portrait_alt": two("Dutch van der Linde in Red Dead Redemption 2", "Dutch van der Linde dans Red Dead Redemption 2"),
 "eyebrow": two("Character &middot; Van der Linde gang", "Personnage &middot; Gang Van der Linde"),
 "meta_desc": two("Dutch van der Linde: founder and leader of the Van der Linde gang in Red Dead Redemption 2 and Red Dead Redemption. His ideals, his fall in 1899, his death in 1911, and Benjamin Byron Davis's performance.",
                  "Dutch van der Linde : fondateur et chef du gang Van der Linde dans Red Dead Redemption 2 et Red Dead Redemption. Ses idéaux, sa chute en 1899, sa mort en 1911, et l'interprétation de Benjamin Byron Davis."),
 "og_desc": two("The charismatic leader whose plans hold the gang together, then tear it apart.",
                "Le chef charismatique dont les plans soudent le gang, puis le détruisent."),
 "schema_desc": two("Founder and leader of the Van der Linde gang in Red Dead Redemption 2 and Red Dead Redemption.",
                    "Fondateur et chef du gang Van der Linde dans Red Dead Redemption 2 et Red Dead Redemption."),
 "chips": [two("Died <strong>1911</strong>", "Mort en <strong>1911</strong>"), two("Deceased", "Décédé"),
           two("Gang leader", "Chef de gang"), two("Voiced by <strong>Benjamin Byron Davis</strong>", "Voix de <strong>Benjamin Byron Davis</strong>")],
 "facts": [
   {"label": two("Born","Naissance"), "value": two("Around 1855","Vers 1855")},
   {"label": two("Died","Mort"), "value": two("1911, Cochinay","1911, Cochinay")},
   {"label": two("Status","Statut"), "value": two("Deceased","Décédé")},
   {"label": two("Nationality","Nationalité"), "value": two("American","Américaine")},
   {"label": two("Affiliation","Affiliation"), "value": two("Van der Linde gang (founder and leader)","Gang Van der Linde (fondateur et chef)")},
   {"label": two("Games","Jeux"), "value": two("Red Dead Redemption, Red Dead Redemption 2, Red Dead Online","Red Dead Redemption, Red Dead Redemption 2, Red Dead Online")},
   {"label": two("Voiced by","Voix"), "value": two("Benjamin Byron Davis","Benjamin Byron Davis")},
 ],
 "intro": [
   two("Dutch van der Linde is the founder and leader of the Van der Linde gang, in Red Dead Redemption 2 (2018) and Red Dead Redemption (2010). The official guide describes him as radically opposed to government control and valuing individual liberty above all else.",
       "Dutch van der Linde est le fondateur et le chef du gang Van der Linde, dans Red Dead Redemption 2 (2018) et Red Dead Redemption (2010). Le guide officiel le décrit comme farouchement opposé au contrôle de l'État et attaché par-dessus tout à la liberté individuelle."),
   two("He is played by Benjamin Byron Davis in both games.",
       "Il est interprété par Benjamin Byron Davis dans les deux jeux."),
 ],
 "sections": [
   {"summary": two("Biography","Biographie"), "open": True, "blocks": [
     {"h3": two("Origins and the gang","Origines et fondation du gang")},
     {"p": two("Dutch was born around 1855. He says his father \"died in a field in Pennsylvania\", fighting in the Civil War. He founded the gang with [[hosea-matthews|Hosea Matthews]] and took in orphans and street children, teaching them to read: [[arthur-morgan|Arthur Morgan]] at fourteen, then [[john-marston|John Marston]] at twelve.",
               "Dutch naît vers 1855. Il raconte que son père est mort \"dans un champ de Pennsylvanie\", pendant la guerre de Sécession. Il fonde le gang avec [[hosea-matthews|Hosea Matthews]] et recueille des orphelins et des enfants des rues, à qui il apprend à lire : [[arthur-morgan|Arthur Morgan]] à quatorze ans, puis [[john-marston|John Marston]] à douze.")},
     {"p": two(f"In 1899, a ferry robbery in Blackwater, planned with [[micah-bell|Micah Bell]], goes wrong and forces the gang to flee into the mountains of {cl(1,'chapter 1','en')}. Several characters say Dutch shot an unarmed young woman during the robbery; the scene itself is never shown. Dutch speaks of buying land in Tahiti once he has enough money.",
               f"En 1899, un braquage sur un ferry à Blackwater, préparé avec [[micah-bell|Micah Bell]], tourne mal et contraint le gang à fuir dans les montagnes du {cl(1,'chapitre 1','fr')}. Plusieurs personnages affirment que Dutch y a abattu une jeune femme désarmée ; la scène n'est jamais montrée. Dutch parle d'acheter une terre à Tahiti une fois l'argent réuni.")},
     {"h3": two("The fall (1899)","La chute (1899)")},
     {"p": two(f"In {cl(4,'chapter 4','en')}, Dutch drowns [[angelo-bronte|Angelo Bronte]] in Saint Denis. The bank robbery he leads in the city is a Pinkerton trap: Hosea is killed by Agent Milton, [[lenny-summers|Lenny]] dies, John is arrested, and the survivors are shipwrecked on Guarma.",
               f"Au {cl(4,'chapitre 4','fr')}, Dutch noie [[angelo-bronte|Angelo Bronte]] à Saint-Denis. Le braquage de banque qu'il mène dans la ville est un piège des Pinkerton : Hosea est tué par l'agent Milton, [[lenny-summers|Lenny]] meurt, John est arrêté, et les survivants font naufrage à Guarma.")},
     {"p": two(f"In {cl(6,'chapter 6','en')}, Dutch refuses to rescue John from prison. He kills [[leviticus-cornwall|Leviticus Cornwall]] in Annesburg, leaves Arthur behind at the oil fields in \"My Last Boy\", then leaves John for dead and abandons Abigail on Micah's advice in \"Our Best Selves\". In the final mission, he sides with Micah against Arthur, then walks away in silence.",
               f"Au {cl(6,'chapitre 6','fr')}, Dutch refuse de faire évader John. Il tue [[leviticus-cornwall|Leviticus Cornwall]] à Annesburg, abandonne Arthur aux champs pétrolifères dans \"My Last Boy\", puis laisse John pour mort et abandonne Abigail sur les conseils de Micah dans \"Our Best Selves\". Lors de la dernière mission, il prend le parti de Micah contre Arthur, puis s'en va sans un mot.")},
     {"p": two(f"In the 1907 {cl('E2','epilogue','en')}, John finds Micah on Mount Hagen, with Dutch. Dutch shoots Micah, letting John finish him off, and leaves.",
               f"Dans l'{cl('E2','épilogue','fr')} de 1907, John retrouve Micah au mont Hagen, en compagnie de Dutch. Dutch tire sur Micah, laisse John l'achever, puis s'en va.")},
     {"h3": two("Death (1911)","Mort (1911)")},
     {"p": two(f"In Red Dead Redemption, Dutch leads a band of young Native Americans from a hideout at Cochinay, in {cl('A3','West Elizabeth','en')}, and robs the Blackwater bank. In \"And the Truth Will Set You Free\", John corners him on a cliff. Dutch tells him that the government will always need an enemy (\"they'll just find another monster\") and that \"our time is passed\", then lets himself fall.",
               f"Dans Red Dead Redemption, Dutch mène une bande de jeunes Amérindiens depuis un repaire à Cochinay, dans le {cl('A3','West Elizabeth','fr')}, et braque la banque de Blackwater. Dans \"And the Truth Will Set You Free\", John l'accule au bord d'une falaise. Dutch le prévient que le gouvernement aura toujours besoin d'un ennemi et que leur temps est révolu, puis se laisse tomber.")},
   ]},
   {"summary": two("Development and performance","Conception et interprétation"), "blocks": [
     {"p": two("Benjamin Byron Davis plays Dutch in both games. For Red Dead Redemption 2, he told GQ in April 2019 that scheduling began in the summer of 2013, that capture sessions ran in 2014, 2016 and 2017, and that playing Dutch \"in his prime\" for almost a year before his decline was \"entirely heartbreaking\". At six feet six inches tall, he needed his size adjusted by the animators.",
               "Benjamin Byron Davis interprète Dutch dans les deux jeux. Pour Red Dead Redemption 2, il raconte à GQ, en avril 2019, que le planning a démarré à l'été 2013, que les séances de capture se sont étalées sur 2014, 2016 et 2017, et que jouer Dutch au sommet de sa forme pendant près d'un an avant son déclin a été déchirant. Avec ses 1,98 m, sa taille a dû être ajustée par les animateurs.")},
     {"p": two("Senior creative writer Michael Unsworth told Variety that \"Dutch has always viewed himself less as a criminal, and more as someone fighting back against a corrupt system of power\". Davis told Twinfinite that he saw Dutch as \"a principled man\" and \"a dreamer\" for whom \"the journey was more important than any arrival\".",
               "Le scénariste Michael Unsworth explique à Variety que Dutch se voit moins comme un criminel que comme un homme qui résiste à un système de pouvoir corrompu. Davis confie à Twinfinite voir en lui un homme de principes et un rêveur, pour qui le voyage comptait plus que l'arrivée.")},
   ]},
   {"summary": two("Reception","Accueil"), "blocks": [
     {"p": two("Twinfinite named Dutch its best character of 2018 and Davis its best voice actor of the year. In Polygon's list of the 70 best video game characters of the decade (2019), Cass Marshall wrote that Dutch \"started his career as a folk hero and revolutionary and ended it as a sad, broken man\". Polygon's Colin Campbell was more critical, calling him \"a manipulative blowhard\".",
               "Twinfinite désigne Dutch meilleur personnage de 2018 et Davis meilleur comédien de doublage de l'année. Dans la liste de Polygon des 70 meilleurs personnages de jeu vidéo de la décennie (2019), Cass Marshall écrit que Dutch a commencé en héros populaire et révolutionnaire, et fini en homme triste et brisé. Colin Campbell, dans Polygon également, se montre plus sévère et le qualifie de fanfaron manipulateur.")},
   ]},
 ],
 "rel_after": 0,
 "relationships": [
   {"img": "hosea.jpeg", "slug": "hosea-matthews", "name": "Hosea Matthews", "text": two(
     "Co-founder of the gang and his oldest partner.",
     "Cofondateur du gang et son plus vieux complice.")},
   {"img": "arthur.jpeg", "slug": "arthur-morgan", "name": "Arthur Morgan", "text": two(
     "His first protégé, who turns against him in 1899.",
     "Son premier protégé, qui se retourne contre lui en 1899.")},
   {"img": "john.jpeg", "slug": "john-marston", "name": "John Marston", "text": two(
     "Saved by him at twelve; corners him on the cliff in 1911.",
     "Sauvé par lui à douze ans ; l'accule au bord de la falaise en 1911.")},
   {"img": "micah.jpeg", "slug": "micah-bell", "name": "Micah Bell", "text": two(
     "The adviser whose influence grows as the gang falls apart.",
     "Le conseiller dont l'influence grandit à mesure que le gang se délite.")},
   {"img": "molly.jpeg", "slug": "molly-oshea", "name": "Molly O'Shea", "text": two(
     "His companion, whom he grows to neglect.",
     "Sa compagne, qu'il finit par délaisser.")},
   {"img": "bill.jpeg", "slug": "bill-williamson", "name": "Bill Williamson", "text": two(
     "A loyal gunman, who follows him to the end of 1899.",
     "Un homme de main fidèle, qui le suit jusqu'au bout de 1899.")},
 ],
 "gallery": [
   {"img": "gallery-1.jpeg", "alt": two("Dutch van der Linde portrait in Red Dead Redemption 2","Portrait de Dutch van der Linde dans Red Dead Redemption 2"),
    "cap": two("The leader of the Van der Linde gang.","Le chef du gang Van der Linde.")},
   {"img": "gallery-2.jpeg", "alt": two("Dutch van der Linde mid-speech","Dutch van der Linde en plein discours"),
    "cap": two("Dutch in full flow.","Dutch dans son élément.")},
 ],
 "related": ["arthur-morgan", "john-marston", "hosea-matthews", "micah-bell"],
},
]
ENRICHED += MAINS1


if __name__ == "__main__":
    from characters_registry import CHARACTERS as REG
    for s, n, en, fr, _g in REG:
        reg(s, n, en, fr)
    only = set(sys.argv[1:])
    for c in ENRICHED:
        if only and c["slug"] not in only:
            continue
        print("rebuilt", build_live(c))
