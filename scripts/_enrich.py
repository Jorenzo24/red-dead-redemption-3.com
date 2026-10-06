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
     {"p": two("Tilly is played by Meeya Davis, an actress from Detroit who moved to New Jersey in 2012 to study acting. She provided the voice and the motion capture. Speaking to Fuzzable in March 2019, she said she was first called in for what was presented as a commercial audition, and only learned about the character on her shooting days. She also said she went to high school with Harron Alexander, who plays Lenny Summers.",
               "Tilly est interprétée par Meeya Davis, actrice originaire de Detroit, installée dans le New Jersey en 2012 pour étudier le jeu. Elle assure la voix et la capture de mouvement. Auprès de Fuzzable, en mars 2019, elle raconte avoir été convoquée pour ce qu'on lui présentait comme une audition pour une publicité, et n'avoir découvert le personnage qu'aux jours de tournage. Elle y précise aussi avoir fréquenté le même lycée que Harron Alexander, l'interprète de Lenny Summers.")},
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


if __name__ == "__main__":
    from characters_registry import CHARACTERS as REG
    for s, n, en, fr, _g in REG:
        reg(s, n, en, fr)
    only = set(sys.argv[1:])
    for c in ENRICHED:
        if only and c["slug"] not in only:
            continue
        print("rebuilt", build_live(c))
