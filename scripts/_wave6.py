#!/usr/bin/env python3
"""Wave 6 content -> _queue/. Run: python scripts/_wave6.py
Not deployed (scripts/ is excluded from .cpanel.yml).

The RDR1 supporting cast the story guide (/story/, published 9 Sept 2026) names
in plain text for want of a fiche: Colonel Agustin Allende, Captain Vincente de
Santa, Luisa Fortuna, Nastas, Professor Harold MacDougal, Irish and Archer
Fordham. Publishing these turns those mentions into internal links.

Factual register, FR written natively. Deliberately narrow where the wiki is
loose: no claim about who lands the killing blow on Allende, nothing on
MacDougal's fate after Yale, no cause of death invented for Irish.
Images already staged in assets/characters/<slug>/.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_fiche import build_to_queue

def two(en, fr): return {"en": en, "fr": fr}

CHARS = [
# ======================== 32. AGUSTIN ALLENDE ========================
{
 "order": 32, "slug": "agustin-allende", "name": "Agustin Allende",
 "publishDate": "2026-09-15", "schema_game": "Red Dead Redemption",
 "reg_role_en": "Provincial governor &middot; RDR1", "reg_role_fr": "Gouverneur de province &middot; RDR1",
 "gender": "Male", "death": "1911", "nationality": "Mexican",
 "portrait_alt": two("Colonel Agustin Allende in uniform at Escalera in Red Dead Redemption",
                     "Le colonel Agustin Allende en uniforme à Escalera dans Red Dead Redemption"),
 "eyebrow": two("Character &middot; Nuevo Paraiso", "Personnage &middot; Nuevo Paraíso"),
 "meta_desc": two("Agustin Allende: the colonel who governs Nuevo Paraiso in Red Dead Redemption. Biography, his grip on the province, and how he shelters Bill Williamson and Javier Escuella.",
                  "Agustin Allende : le colonel qui gouverne le Nuevo Paraíso dans Red Dead Redemption. Biographie, sa mainmise sur la province, et comment il protège Bill Williamson et Javier Escuella."),
 "og_desc": two("The colonel who rules Nuevo Paraiso, and the reason John Marston has to deal with the Mexican army at all.",
                "Le colonel qui règne sur le Nuevo Paraíso, et la raison pour laquelle John Marston doit traiter avec l'armée mexicaine."),
 "schema_desc": two("Colonel and provincial governor of Nuevo Paraiso in Red Dead Redemption.",
                    "Colonel et gouverneur de la province de Nuevo Paraíso dans Red Dead Redemption."),
 "chips": [two("Mexican Army", "Armée mexicaine"), two("Governor", "Gouverneur"),
           two("Died 1911", "Mort en 1911"), two("RDR1", "RDR1")],
 "facts": [
   {"label": two("Affiliation","Affiliation"), "value": two("Mexican Army","Armée mexicaine")},
   {"label": two("Role","Rôle"), "value": two("Colonel, governor of Nuevo Paraiso","Colonel, gouverneur du Nuevo Paraíso")},
   {"label": two("Based at","Résidence"), "value": two("Escalera","Escalera")},
   {"label": two("Status","Statut"), "value": two("Killed in 1911","Tué en 1911")},
   {"label": two("Nationality","Nationalité"), "value": two("Mexican","Mexicain")},
   {"label": two("Games","Jeux"), "value": two("Red Dead Redemption","Red Dead Redemption")},
 ],
 "intro": [
   two("Agustin Allende is a colonel in the Mexican Army and the governor of Nuevo Paraiso in Red Dead Redemption. He runs the province from his residence at Escalera and puts down the rebellion led by [[abraham-reyes|Abraham Reyes]].",
       "Agustin Allende est colonel de l'armée mexicaine et gouverneur du Nuevo Paraíso dans Red Dead Redemption. Il administre la province depuis sa résidence d'Escalera et réprime la rébellion menée par [[abraham-reyes|Abraham Reyes]]."),
   two("He is also the man sheltering [[bill-williamson|Bill Williamson]] and [[javier-escuella|Javier Escuella]], which is what obliges [[john-marston|John Marston]] to work for him.",
       "C'est aussi lui qui abrite [[bill-williamson|Bill Williamson]] et [[javier-escuella|Javier Escuella]], ce qui contraint [[john-marston|John Marston]] à travailler pour lui."),
 ],
 "sections": [
   {"summary": two("Biography","Biographie"), "open": True, "blocks": [
     {"h3": two("Governor of Nuevo Paraiso","Gouverneur du Nuevo Paraíso")},
     {"p": two("Allende governs the province under military rule. His soldiers conscript villagers, seize property and execute suspected rebels. He holds court at Escalera, where his officers report to him, and his authority over Nuevo Paraiso is effectively absolute.",
               "Allende administre la province sous régime militaire. Ses soldats enrôlent de force les villageois, saisissent les biens et exécutent les rebelles présumés. Il tient sa cour à Escalera, où ses officiers viennent lui rendre compte, et son autorité sur le Nuevo Paraíso est de fait sans partage.")},
     {"h3": two("Sheltering the two outlaws","Les deux hors-la-loi qu'il protège")},
     {"p": two("Bill Williamson and Javier Escuella cross into Mexico and are taken under Allende's protection, working as hired guns for his regime. When John Marston arrives looking for them, Allende neither hands them over nor admits they are there. Instead he sets John to work against the rebels, through his officer Captain Vincente de Santa.",
               "Bill Williamson et Javier Escuella passent au Mexique et se placent sous la protection d'Allende, dont ils deviennent les hommes de main. Quand John Marston arrive à leur recherche, Allende ne les livre pas et ne reconnaît pas leur présence. Il met plutôt John au travail contre les rebelles, par l'intermédiaire de son officier, le capitaine Vincente de Santa.")},
   ]},
   {"summary": two("Reputation","Réputation"), "blocks": [
     {"p": two("Allende is shown as vain and self-indulgent. He presents the repression as a service to the country, keeps young women at his residence, and treats the war as an inconvenience to his comfort. His soldiers fear him, and the villages he taxes have nothing good to say about him.",
               "Allende est présenté comme vaniteux et jouisseur. Il présente la répression comme un service rendu au pays, retient des jeunes femmes dans sa résidence et traite la guerre comme une gêne à son confort. Ses soldats le craignent, et les villages qu'il pressure n'en disent rien de bon.")},
   ]},
   {"summary": two("Fate","Destin"), "blocks": [
     {"p": two("John eventually breaks with the army and joins the rebels. Escalera falls to the uprising in 1911, and Allende is killed during the collapse, in the same sequence that leaves Bill Williamson dead. Abraham Reyes takes the province immediately afterwards.",
               "John finit par rompre avec l'armée et rejoint les rebelles. Escalera tombe aux mains de l'insurrection en 1911, et Allende est tué pendant la débâcle, dans la même séquence qui coûte la vie à Bill Williamson. Abraham Reyes s'empare de la province dans la foulée.")},
   ]},
   {"summary": two("Behind the scenes","Coulisses"), "blocks": [
     {"p": two("Agustin Allende appears in Red Dead Redemption (2010), in the Nuevo Paraiso chapter of the story.",
               "Agustin Allende apparaît dans Red Dead Redemption (2010), dans la partie de l'histoire consacrée au Nuevo Paraíso.")},
   ]},
 ],
 "relationships": [
   {"name": "Vincente de Santa", "slug": None, "img": "desanta.jpeg",
    "text": two("His captain, and the officer who handles the army's dealings with John Marston.",
                "Son capitaine, l'officier qui gère les rapports de l'armée avec John Marston.")},
   {"name": "Bill Williamson", "slug": "bill-williamson", "img": "bill.jpeg",
    "text": two("The outlaw he shelters in exchange for service to the regime.",
                "Le hors-la-loi qu'il protège en échange de services rendus au régime.")},
   {"name": "Abraham Reyes", "slug": "abraham-reyes", "img": "reyes.jpeg",
    "text": two("The revolutionary whose uprising ends his rule over the province.",
                "Le révolutionnaire dont le soulèvement met fin à son pouvoir sur la province.")},
   {"name": "John Marston", "slug": "john-marston", "img": "john.jpeg",
    "text": two("Works for him under false pretences, then turns on him.",
                "Travaille pour lui sous un faux prétexte, puis se retourne contre lui.")},
 ],
 "gallery": [
   {"img": "gallery-1.jpeg", "alt": two("Colonel Allende at his residence in Escalera","Le colonel Allende dans sa résidence d'Escalera"),
    "cap": two("Allende at Escalera, the seat of the provincial government.","Allende à Escalera, siège du gouvernement provincial.")},
 ],
},
# ======================== 33. VINCENTE DE SANTA ========================
{
 "order": 33, "slug": "vincente-de-santa", "name": "Vincente de Santa",
 "publishDate": "2026-09-18", "schema_game": "Red Dead Redemption",
 "reg_role_en": "Mexican Army captain &middot; RDR1", "reg_role_fr": "Capitaine de l'armée mexicaine &middot; RDR1",
 "gender": "Male", "death": "1911", "nationality": "Mexican",
 "portrait_alt": two("Captain Vincente de Santa in Red Dead Redemption",
                     "Le capitaine Vincente de Santa dans Red Dead Redemption"),
 "eyebrow": two("Character &middot; Nuevo Paraiso", "Personnage &middot; Nuevo Paraíso"),
 "meta_desc": two("Vincente de Santa: the Mexican Army captain who strings John Marston along in Red Dead Redemption. Biography, his false promises, and the betrayal that gets him killed.",
                  "Vincente de Santa : le capitaine de l'armée mexicaine qui mène John Marston en bateau dans Red Dead Redemption. Biographie, ses fausses promesses, et la trahison qui lui coûte la vie."),
 "og_desc": two("Allende's captain, the officer who promises John Marston two outlaws and delivers nothing.",
                "Le capitaine d'Allende, l'officier qui promet deux hors-la-loi à John Marston et ne livre rien."),
 "schema_desc": two("Captain in the Mexican Army under Colonel Allende in Red Dead Redemption.",
                    "Capitaine de l'armée mexicaine sous les ordres du colonel Allende dans Red Dead Redemption."),
 "chips": [two("Mexican Army", "Armée mexicaine"), two("Captain", "Capitaine"),
           two("Died 1911", "Mort en 1911"), two("RDR1", "RDR1")],
 "facts": [
   {"label": two("Affiliation","Affiliation"), "value": two("Mexican Army","Armée mexicaine")},
   {"label": two("Role","Rôle"), "value": two("Captain under Colonel Allende","Capitaine sous les ordres du colonel Allende")},
   {"label": two("Status","Statut"), "value": two("Killed by John Marston in 1911","Tué par John Marston en 1911")},
   {"label": two("Nationality","Nationalité"), "value": two("Mexican","Mexicain")},
   {"label": two("Games","Jeux"), "value": two("Red Dead Redemption","Red Dead Redemption")},
 ],
 "intro": [
   two("Vincente de Santa is a captain in the Mexican Army in Red Dead Redemption, and the officer [[agustin-allende|Colonel Allende]] puts between himself and [[john-marston|John Marston]].",
       "Vincente de Santa est capitaine de l'armée mexicaine dans Red Dead Redemption, et l'officier que [[agustin-allende|le colonel Allende]] place entre lui et [[john-marston|John Marston]]."),
   two("He repeatedly promises to hand over [[bill-williamson|Bill Williamson]] and [[javier-escuella|Javier Escuella]], and repeatedly finds another errand for John to run instead.",
       "Il promet à plusieurs reprises de livrer [[bill-williamson|Bill Williamson]] et [[javier-escuella|Javier Escuella]], et trouve chaque fois une nouvelle course à confier à John."),
 ],
 "sections": [
   {"summary": two("Biography","Biographie"), "open": True, "blocks": [
     {"h3": two("The army's middleman","L'intermédiaire de l'armée")},
     {"p": two("De Santa is John's first contact with the government side in Nuevo Paraiso. He takes John on as a hired gun against the rebels, and each job comes with the assurance that the two outlaws will be produced once the work is done. They never are. The pattern runs for most of the Mexican chapter.",
               "De Santa est le premier contact de John du côté du gouvernement, au Nuevo Paraíso. Il l'engage comme homme de main contre les rebelles, et chaque mission s'accompagne de l'assurance que les deux hors-la-loi lui seront remis une fois le travail fini. Ils ne le sont jamais. Le manège dure presque toute la partie mexicaine.")},
     {"h3": two("Repression","La répression")},
     {"p": two("The work De Santa hands out is the day-to-day business of the occupation: raids on villages, executions of suspected rebels, and the hunt for [[abraham-reyes|Abraham Reyes]]. He carries it out without hesitation and expects the same from the men under him.",
               "Les missions que confie De Santa relèvent du quotidien de l'occupation : razzias dans les villages, exécutions de rebelles présumés, traque d'[[abraham-reyes|Abraham Reyes]]. Il les mène sans état d'âme et attend la même chose de ses hommes.")},
   ]},
   {"summary": two("The betrayal","La trahison"), "blocks": [
     {"p": two("De Santa eventually turns John over to be executed. John escapes the firing squad, hunts him down and kills him. De Santa begs for his life first. The break ends John's arrangement with the army for good, and he commits to the rebel side for the assault on Escalera.",
               "De Santa finit par livrer John pour qu'il soit exécuté. John échappe au peloton, le retrouve et le tue. De Santa commence par implorer qu'on l'épargne. La rupture met définitivement fin à l'arrangement de John avec l'armée, et il s'engage aux côtés des rebelles pour l'assaut d'Escalera.")},
   ]},
   {"summary": two("Behind the scenes","Coulisses"), "blocks": [
     {"p": two("Vincente de Santa appears in Red Dead Redemption (2010). His name is also written Vicente in some materials.",
               "Vincente de Santa apparaît dans Red Dead Redemption (2010). Son prénom est parfois orthographié Vicente selon les supports.")},
   ]},
 ],
 "relationships": [
   {"name": "Agustin Allende", "slug": "agustin-allende", "img": "allende.jpeg",
    "text": two("The colonel he serves, and whose orders he carries out in the province.",
                "Le colonel qu'il sert, et dont il applique les ordres dans la province.")},
   {"name": "John Marston", "slug": "john-marston", "img": "john.jpeg",
    "text": two("The gunman he strings along, then betrays, and who kills him for it.",
                "L'homme de main qu'il fait patienter, puis trahit, et qui le tue pour cela.")},
   {"name": "Abraham Reyes", "slug": "abraham-reyes", "img": "reyes.jpeg",
    "text": two("The rebel leader he is tasked with hunting down.",
                "Le chef rebelle qu'il est chargé de traquer.")},
 ],
 "gallery": [
   {"img": "gallery-1.jpeg", "alt": two("John Marston confronting Captain de Santa","John Marston face au capitaine de Santa"),
    "cap": two("John catches up with de Santa after escaping the firing squad.","John rattrape de Santa après avoir échappé au peloton d'exécution.")},
 ],
},
# ======================== 34. LUISA FORTUNA ========================
{
 "order": 34, "slug": "luisa-fortuna", "name": "Luisa Fortuna",
 "publishDate": "2026-09-21", "schema_game": "Red Dead Redemption",
 "reg_role_en": "Revolutionary &middot; RDR1", "reg_role_fr": "Révolutionnaire &middot; RDR1",
 "gender": "Female", "death": "1911", "nationality": "Mexican",
 "portrait_alt": two("Luisa Fortuna and John Marston in Red Dead Redemption",
                     "Luisa Fortuna et John Marston dans Red Dead Redemption"),
 "eyebrow": two("Character &middot; Nuevo Paraiso", "Personnage &middot; Nuevo Paraíso"),
 "meta_desc": two("Luisa Fortuna: the young revolutionary devoted to Abraham Reyes in Red Dead Redemption. Biography, her family, and her death at El Presidio.",
                  "Luisa Fortuna : la jeune révolutionnaire dévouée à Abraham Reyes dans Red Dead Redemption. Biographie, sa famille, et sa mort à El Presidio."),
 "og_desc": two("A farm girl who joins the revolution for Abraham Reyes, and does not live to see it win.",
                "Une paysanne qui rejoint la révolution par amour pour Abraham Reyes, et ne vit pas assez pour la voir gagner."),
 "schema_desc": two("Young Mexican revolutionary and follower of Abraham Reyes in Red Dead Redemption.",
                    "Jeune révolutionnaire mexicaine et partisane d'Abraham Reyes dans Red Dead Redemption."),
 "chips": [two("Rebels", "Rebelles"), two("Revolutionary", "Révolutionnaire"),
           two("Died 1911", "Morte en 1911"), two("RDR1", "RDR1")],
 "facts": [
   {"label": two("Affiliation","Affiliation"), "value": two("Mexican rebels","Rebelles mexicains")},
   {"label": two("Family","Famille"), "value": two("The Fortuna family, Nuevo Paraiso","La famille Fortuna, Nuevo Paraíso")},
   {"label": two("Status","Statut"), "value": two("Killed at El Presidio in 1911","Tuée à El Presidio en 1911")},
   {"label": two("Nationality","Nationalité"), "value": two("Mexican","Mexicaine")},
   {"label": two("Games","Jeux"), "value": two("Red Dead Redemption","Red Dead Redemption")},
 ],
 "intro": [
   two("Luisa Fortuna is a young Mexican woman who joins the rebellion in Red Dead Redemption. She comes from a farming family in Nuevo Paraiso and believes completely in [[abraham-reyes|Abraham Reyes]], whom she describes as her fiance.",
       "Luisa Fortuna est une jeune Mexicaine qui rejoint la rébellion dans Red Dead Redemption. Issue d'une famille de paysans du Nuevo Paraíso, elle croit sans réserve en [[abraham-reyes|Abraham Reyes]], qu'elle présente comme son fiancé."),
   two("She becomes one of [[john-marston|John Marston]]'s contacts on the rebel side, and asks him for help with her own family as well as the cause.",
       "Elle devient l'un des contacts de [[john-marston|John Marston]] du côté rebelle, et lui demande de l'aide pour sa famille autant que pour la cause."),
 ],
 "sections": [
   {"summary": two("Biography","Biographie"), "open": True, "blocks": [
     {"h3": two("Devotion to Reyes","Son dévouement à Reyes")},
     {"p": two("Luisa tells everyone who will listen that she and Reyes are to be married. Reyes does not treat the attachment as she does, and the gap between what she believes and how he behaves is left plain to see. She keeps working for the rebellion regardless.",
               "Luisa répète à qui veut l'entendre qu'elle et Reyes doivent se marier. Reyes n'accorde pas à cet attachement la même valeur qu'elle, et l'écart entre ce qu'elle croit et la façon dont il se comporte est montré sans détour. Elle n'en continue pas moins à servir la rébellion.")},
     {"h3": two("Her family","Sa famille")},
     {"p": two("Luisa's family are ordinary farmers caught between the army and the rebels. She asks John to intervene on their behalf, and her sister's situation is one of the errands he takes on in Nuevo Paraiso.",
               "La famille de Luisa, de simples paysans, se retrouve prise entre l'armée et les rebelles. Elle demande à John d'intervenir en leur faveur, et le sort de sa sœur fait partie des missions qu'il accepte au Nuevo Paraíso.")},
   ]},
   {"summary": two("Death at El Presidio","Sa mort à El Presidio"), "blocks": [
     {"p": two("Reyes is captured and held at El Presidio. Luisa takes part in the attack to free him and is shot during the assault. She dies there, before the revolution she believed in takes the province. Reyes goes on to win and to govern.",
               "Reyes est capturé et détenu à El Presidio. Luisa participe à l'attaque menée pour le libérer et y est touchée. Elle meurt sur place, avant que la révolution en laquelle elle croyait ne s'empare de la province. Reyes, lui, l'emporte et gouverne.")},
   ]},
   {"summary": two("Behind the scenes","Coulisses"), "blocks": [
     {"p": two("Luisa Fortuna appears in Red Dead Redemption (2010), in the Nuevo Paraiso chapter of the story.",
               "Luisa Fortuna apparaît dans Red Dead Redemption (2010), dans la partie de l'histoire consacrée au Nuevo Paraíso.")},
   ]},
 ],
 "relationships": [
   {"name": "Abraham Reyes", "slug": "abraham-reyes", "img": "reyes.jpeg",
    "text": two("The rebel leader she is devoted to, and calls her fiance.",
                "Le chef rebelle auquel elle se dévoue, et qu'elle présente comme son fiancé.")},
   {"name": "John Marston", "slug": "john-marston", "img": "john.jpeg",
    "text": two("The American she brings into the rebellion's errands, and who helps her family.",
                "L'Américain qu'elle entraîne dans les missions de la rébellion, et qui aide sa famille.")},
   {"name": "Agustin Allende", "slug": "agustin-allende", "img": "allende.jpeg",
    "text": two("The governor whose forces hold Reyes at El Presidio.",
                "Le gouverneur dont les forces détiennent Reyes à El Presidio.")},
 ],
 "gallery": [
   {"img": "gallery-1.jpeg", "alt": two("A rebel wagon on the roads of Nuevo Paraiso","Un chariot rebelle sur les routes du Nuevo Paraíso"),
    "cap": two("The rebel supply runs Luisa helps organise across Nuevo Paraiso.","Les convois de ravitaillement rebelles que Luisa aide à organiser à travers le Nuevo Paraíso.")},
 ],
},
# ======================== 35. NASTAS ========================
{
 "order": 35, "slug": "nastas", "name": "Nastas",
 "publishDate": "2026-09-24", "schema_game": "Red Dead Redemption",
 "reg_role_en": "Guide &middot; RDR1", "reg_role_fr": "Guide &middot; RDR1",
 "gender": "Male", "death": "1911", "nationality": "American",
 "portrait_alt": two("Nastas and John Marston held at gunpoint in Red Dead Redemption",
                     "Nastas et John Marston tenus en joue dans Red Dead Redemption"),
 "eyebrow": two("Character &middot; West Elizabeth", "Personnage &middot; West Elizabeth"),
 "meta_desc": two("Nastas: the Native American guide who helps John Marston find Dutch van der Linde in Red Dead Redemption. Biography, his work with Professor MacDougal, and his death.",
                  "Nastas : le guide amérindien qui aide John Marston à retrouver Dutch van der Linde dans Red Dead Redemption. Biographie, son travail avec le professeur MacDougal, et sa mort."),
 "og_desc": two("The guide who leads John Marston through Tall Trees on the hunt for Dutch van der Linde.",
                "Le guide qui conduit John Marston à travers Tall Trees sur la piste de Dutch van der Linde."),
 "schema_desc": two("Native American guide in West Elizabeth in Red Dead Redemption.",
                    "Guide amérindien de West Elizabeth dans Red Dead Redemption."),
 "chips": [two("West Elizabeth", "West Elizabeth"), two("Guide", "Guide"),
           two("Died 1911", "Mort en 1911"), two("RDR1", "RDR1")],
 "facts": [
   {"label": two("Role","Rôle"), "value": two("Guide and informant","Guide et informateur")},
   {"label": two("Region","Région"), "value": two("West Elizabeth, Tall Trees","West Elizabeth, Tall Trees")},
   {"label": two("Works with","Travaille avec"), "value": two("Professor Harold MacDougal","Le professeur Harold MacDougal")},
   {"label": two("Status","Statut"), "value": two("Killed in 1911","Tué en 1911")},
   {"label": two("Games","Jeux"), "value": two("Red Dead Redemption","Red Dead Redemption")},
 ],
 "intro": [
   two("Nastas is a Native American guide in Red Dead Redemption, and one of the two men [[edgar-ross|Edgar Ross]] assigns to help [[john-marston|John Marston]] locate [[dutch-van-der-linde|Dutch van der Linde]] in West Elizabeth.",
       "Nastas est un guide amérindien de Red Dead Redemption, et l'un des deux hommes que [[edgar-ross|Edgar Ross]] adjoint à [[john-marston|John Marston]] pour localiser [[dutch-van-der-linde|Dutch van der Linde]] dans West Elizabeth."),
   two("He knows Tall Trees and the men Dutch has recruited there, which makes him the only practical way into the forest.",
       "Il connaît Tall Trees et les hommes que Dutch y a recrutés, ce qui fait de lui le seul moyen réaliste d'entrer dans la forêt."),
 ],
 "sections": [
   {"summary": two("Biography","Biographie"), "open": True, "blocks": [
     {"h3": two("Working for MacDougal","Au service de MacDougal")},
     {"p": two("Nastas works as guide and informant for Professor Harold MacDougal, an anthropologist based in Blackwater. MacDougal treats him as a research subject as much as an employee, and Nastas takes the work anyway. The arrangement is what puts him in John Marston's path.",
               "Nastas travaille comme guide et informateur pour le professeur Harold MacDougal, anthropologue installé à Blackwater. MacDougal le traite autant comme un sujet d'étude que comme un employé, et Nastas accepte malgré tout ce travail. C'est cet arrangement qui le met sur la route de John Marston.")},
     {"h3": two("The hunt through Tall Trees","La traque dans Tall Trees")},
     {"p": two("Dutch has gathered a new gang in Tall Trees, made up largely of displaced Native men, and raids banks and coaches from a hideout at Cochinay. Nastas leads John through the forest, identifies Dutch's people and narrows down the location of the camp.",
               "Dutch a réuni un nouveau gang à Tall Trees, composé pour l'essentiel d'Amérindiens chassés de leurs terres, et attaque banques et diligences depuis un repaire établi à Cochinay. Nastas guide John à travers la forêt, identifie les hommes de Dutch et resserre peu à peu la localisation du camp.")},
   ]},
   {"summary": two("Death","Mort"), "blocks": [
     {"p": two("Nastas is killed during the search, before John reaches Cochinay. His death removes the one person able to move freely between the two sides in Tall Trees, and the hunt continues without him.",
               "Nastas est tué au cours des recherches, avant que John n'atteigne Cochinay. Sa mort prive la traque du seul homme capable de circuler librement entre les deux camps à Tall Trees, et elle se poursuit sans lui.")},
   ]},
   {"summary": two("Behind the scenes","Coulisses"), "blocks": [
     {"p": two("Nastas appears in Red Dead Redemption (2010), in the West Elizabeth chapter of the story.",
               "Nastas apparaît dans Red Dead Redemption (2010), dans la partie de l'histoire consacrée à West Elizabeth.")},
   ]},
 ],
 "relationships": [
   {"name": "John Marston", "slug": "john-marston", "img": "john.jpeg",
    "text": two("The man he guides through Tall Trees on the hunt for Dutch.",
                "L'homme qu'il guide dans Tall Trees sur la piste de Dutch.")},
   {"name": "Dutch van der Linde", "slug": "dutch-van-der-linde", "img": "dutch.jpeg",
    "text": two("The outlaw whose new gang holds Cochinay, and whom the search is aimed at.",
                "Le hors-la-loi dont le nouveau gang tient Cochinay, et que vise la traque.")},
   {"name": "Edgar Ross", "slug": "edgar-ross", "img": "ross.jpeg",
    "text": two("The Bureau agent directing the operation out of Blackwater.",
                "L'agent du Bureau qui dirige l'opération depuis Blackwater.")},
 ],
 "gallery": [
   {"img": "gallery-1.jpeg", "alt": two("Federal agents and their motor car in West Elizabeth","Des agents fédéraux et leur automobile dans West Elizabeth"),
    "cap": two("The Bureau's operation in West Elizabeth, which Nastas is attached to.","L'opération du Bureau dans West Elizabeth, à laquelle Nastas est rattaché.")},
 ],
},
# ======================== 36. HAROLD MACDOUGAL ========================
{
 "order": 36, "slug": "harold-macdougal", "name": "Harold MacDougal",
 "publishDate": "2026-09-27", "schema_game": "Red Dead Redemption",
 "reg_role_en": "Anthropologist &middot; RDR1", "reg_role_fr": "Anthropologue &middot; RDR1",
 "gender": "Male", "death": None, "nationality": "American",
 "portrait_alt": two("Professor Harold MacDougal in the streets of Blackwater in Red Dead Redemption",
                     "Le professeur Harold MacDougal dans les rues de Blackwater dans Red Dead Redemption"),
 "eyebrow": two("Character &middot; West Elizabeth", "Personnage &middot; West Elizabeth"),
 "meta_desc": two("Harold MacDougal: the Yale anthropologist in Blackwater in Red Dead Redemption. Biography, his theories, his addictions, and his part in the hunt for Dutch van der Linde.",
                  "Harold MacDougal : l'anthropologue de Yale installé à Blackwater dans Red Dead Redemption. Biographie, ses théories, ses addictions, et son rôle dans la traque de Dutch van der Linde."),
 "og_desc": two("The Blackwater academic whose research, and whose guide, put John Marston on the trail of Dutch van der Linde.",
                "L'universitaire de Blackwater dont les travaux, et le guide, mettent John Marston sur la piste de Dutch van der Linde."),
 "schema_desc": two("Anthropologist based in Blackwater in Red Dead Redemption.",
                    "Anthropologue installé à Blackwater dans Red Dead Redemption."),
 "chips": [two("West Elizabeth", "West Elizabeth"), two("Anthropologist", "Anthropologue"),
           two("Yale", "Yale"), two("RDR1", "RDR1")],
 "facts": [
   {"label": two("Role","Rôle"), "value": two("Professor of anthropology","Professeur d'anthropologie")},
   {"label": two("Institution","Institution"), "value": two("Yale University","Université de Yale")},
   {"label": two("Based at","Installé à"), "value": two("Blackwater, West Elizabeth","Blackwater, West Elizabeth")},
   {"label": two("Works with","Travaille avec"), "value": two("Nastas","Nastas")},
   {"label": two("Games","Jeux"), "value": two("Red Dead Redemption","Red Dead Redemption")},
 ],
 "intro": [
   two("Harold MacDougal is a professor of anthropology from Yale, living in Blackwater in Red Dead Redemption. [[edgar-ross|Edgar Ross]] sends [[john-marston|John Marston]] to him because his research has brought him closer to [[dutch-van-der-linde|Dutch van der Linde]]'s new gang than the Bureau has managed.",
       "Harold MacDougal est professeur d'anthropologie à Yale, installé à Blackwater dans Red Dead Redemption. [[edgar-ross|Edgar Ross]] envoie [[john-marston|John Marston]] le voir parce que ses travaux l'ont rapproché du nouveau gang de [[dutch-van-der-linde|Dutch van der Linde]] plus sûrement que le Bureau n'y est parvenu."),
   two("He employs [[nastas|Nastas]] as a guide, and his study of the region's Native population is what makes the hunt through Tall Trees possible.",
       "Il emploie [[nastas|Nastas]] comme guide, et son étude des populations amérindiennes de la région est ce qui rend possible la traque dans Tall Trees."),
 ],
 "sections": [
   {"summary": two("Biography","Biographie"), "open": True, "blocks": [
     {"h3": two("The Blackwater research","Ses travaux à Blackwater")},
     {"p": two("MacDougal has come west to study the Native peoples of West Elizabeth. His theories are the racial pseudo-science of the period, and he states them plainly and often. He funds and directs the work himself, with Nastas doing the fieldwork that MacDougal will not do.",
               "MacDougal est venu dans l'Ouest étudier les peuples amérindiens de West Elizabeth. Ses théories relèvent de la pseudo-science raciale de l'époque, qu'il expose sans détour et à longueur de temps. Il finance et dirige lui-même ses recherches, Nastas se chargeant du travail de terrain que MacDougal n'assume pas.")},
     {"h3": two("Addictions","Addictions")},
     {"p": two("MacDougal is a heavy user of cocaine and alcohol, and his condition worsens over the course of the story. His judgement is unreliable throughout, and several of the missions he sends John on go wrong because of it.",
               "MacDougal consomme cocaïne et alcool en quantité, et son état se dégrade au fil de l'histoire. Son jugement n'est jamais fiable, et plusieurs des missions qu'il confie à John tournent mal pour cette raison.")},
   ]},
   {"summary": two("The hunt for Dutch","La traque de Dutch"), "blocks": [
     {"p": two("MacDougal, Nastas and John work together to find Dutch's hideout at Cochinay. The three are captured at one point and held at gunpoint before they get clear. Nastas is killed during the search, and the operation continues without him.",
               "MacDougal, Nastas et John travaillent ensemble pour localiser le repaire de Dutch, à Cochinay. Les trois hommes sont capturés à un moment et tenus en joue avant de pouvoir s'échapper. Nastas est tué au cours des recherches, et l'opération se poursuit sans lui.")},
   ]},
   {"summary": two("Leaving the West","Le départ de l'Ouest"), "blocks": [
     {"p": two("Once his part in the hunt is done, MacDougal packs up his research and leaves Blackwater for Yale. John sees him off at the train.",
               "Une fois son rôle dans la traque terminé, MacDougal remballe ses travaux et quitte Blackwater pour Yale. John l'accompagne jusqu'au train.")},
   ]},
   {"summary": two("Behind the scenes","Coulisses"), "blocks": [
     {"p": two("Harold MacDougal appears in Red Dead Redemption (2010), in the West Elizabeth chapter of the story.",
               "Harold MacDougal apparaît dans Red Dead Redemption (2010), dans la partie de l'histoire consacrée à West Elizabeth.")},
   ]},
 ],
 "relationships": [
   {"name": "Nastas", "slug": "nastas", "img": "nastas.jpeg",
    "text": two("His guide and informant, and the man who does the fieldwork for him.",
                "Son guide et informateur, celui qui fait le travail de terrain à sa place.")},
   {"name": "John Marston", "slug": "john-marston", "img": "john.jpeg",
    "text": two("Sent to him by the Bureau, and works his missions in Tall Trees.",
                "Envoyé vers lui par le Bureau, et exécute ses missions dans Tall Trees.")},
   {"name": "Edgar Ross", "slug": "edgar-ross", "img": "ross.jpeg",
    "text": two("The Bureau agent who puts John and the professor together.",
                "L'agent du Bureau qui met John et le professeur en relation.")},
 ],
 "gallery": [
   {"img": "gallery-1.jpeg", "alt": two("Nastas, John Marston and Harold MacDougal held at gunpoint","Nastas, John Marston et Harold MacDougal tenus en joue"),
    "cap": two("Nastas, John and MacDougal taken during the search through Tall Trees.","Nastas, John et MacDougal capturés pendant les recherches dans Tall Trees.")},
 ],
},
# ======================== 37. IRISH ========================
{
 "order": 37, "slug": "irish", "name": "Irish",
 "publishDate": "2026-09-30", "schema_game": "Red Dead Redemption",
 "reg_role_en": "Gunrunner &middot; RDR1", "reg_role_fr": "Trafiquant d'armes &middot; RDR1",
 "gender": "Male", "death": None, "nationality": "Irish",
 "portrait_alt": two("Irish, the drunken gunrunner, in Red Dead Redemption",
                     "Irish, le trafiquant d'armes alcoolique, dans Red Dead Redemption"),
 "eyebrow": two("Character &middot; New Austin", "Personnage &middot; New Austin"),
 "meta_desc": two("Irish: the drunken gunrunner who helps John Marston take Fort Mercer in Red Dead Redemption. Biography, the Gatling gun, and his run of broken promises.",
                  "Irish : le trafiquant d'armes alcoolique qui aide John Marston à prendre Fort Mercer dans Red Dead Redemption. Biographie, la mitrailleuse Gatling, et sa série de promesses non tenues."),
 "og_desc": two("The gunrunner who claims connections he does not have, and who still produces the Gatling gun that takes Fort Mercer.",
                "Le trafiquant d'armes qui se vante de relations qu'il n'a pas, et qui fournit malgré tout la Gatling qui fait tomber Fort Mercer."),
 "schema_desc": two("Irish immigrant and gunrunner in New Austin in Red Dead Redemption.",
                    "Immigré irlandais et trafiquant d'armes de New Austin dans Red Dead Redemption."),
 "chips": [two("New Austin", "New Austin"), two("Gunrunner", "Trafiquant d'armes"),
           two("Irish immigrant", "Immigré irlandais"), two("RDR1", "RDR1")],
 "facts": [
   {"label": two("Role","Rôle"), "value": two("Gunrunner","Trafiquant d'armes")},
   {"label": two("Region","Région"), "value": two("New Austin, later Nuevo Paraiso","New Austin, puis Nuevo Paraíso")},
   {"label": two("Known for","Connu pour"), "value": two("Supplying the Gatling gun for Fort Mercer","Avoir fourni la Gatling de Fort Mercer")},
   {"label": two("Nationality","Nationalité"), "value": two("Irish","Irlandaise")},
   {"label": two("Games","Jeux"), "value": two("Red Dead Redemption","Red Dead Redemption")},
 ],
 "intro": [
   two("Irish is an Irish immigrant and gunrunner in Red Dead Redemption, and one of the three men [[john-marston|John Marston]] recruits in New Austin to take Fort Mercer.",
       "Irish est un immigré irlandais et trafiquant d'armes dans Red Dead Redemption, l'un des trois hommes que [[john-marston|John Marston]] recrute à New Austin pour prendre Fort Mercer."),
   two("He is drunk in most of his appearances and claims contacts and abilities he does not have, but he is the one who produces the Gatling gun the assault depends on.",
       "Il est ivre dans la plupart de ses apparitions et se vante de relations et de talents qu'il n'a pas, mais c'est lui qui fournit la mitrailleuse Gatling dont dépend l'assaut."),
 ],
 "sections": [
   {"summary": two("Biography","Biographie"), "open": True, "blocks": [
     {"h3": two("The Fort Mercer job","Le coup de Fort Mercer")},
     {"p": two("John needs firepower to get through the walls of Fort Mercer. Irish claims he can get a Gatling gun, and, after a detour that nearly gets both of them killed, he does. The weapon is hidden in [[nigel-west-dickens|Nigel West Dickens]]'s stagecoach and fired from inside the fort once the gate opens.",
               "John a besoin d'une puissance de feu suffisante pour franchir les murs de Fort Mercer. Irish affirme pouvoir se procurer une Gatling et, au terme d'un détour qui manque de les faire tuer tous les deux, il y parvient. L'arme est dissimulée dans la diligence de [[nigel-west-dickens|Nigel West Dickens]] et mise en action à l'intérieur du fort dès l'ouverture des portes.")},
     {"h3": two("Promises and excuses","Promesses et excuses")},
     {"p": two("Irish's dealings with John follow a pattern: a confident claim, a job that goes wrong, and an excuse. He takes John to contacts who turn out to be hostile, and to places that turn out to be ambushes. John keeps working with him because the alternative is doing it alone.",
               "Les affaires d'Irish avec John suivent toujours le même schéma : une promesse assurée, une mission qui tourne mal, une excuse. Il emmène John chez des contacts qui se révèlent hostiles, dans des lieux qui se révèlent être des embuscades. John continue de traiter avec lui parce que la seule autre option est de se débrouiller seul.")},
   ]},
   {"summary": two("Across the border","De l'autre côté de la frontière"), "blocks": [
     {"p": two("Irish turns up again in Nuevo Paraiso, where he helps John cross the border and keeps trading in weapons. His drinking is worse, and his usefulness has not improved.",
               "Irish réapparaît au Nuevo Paraíso, où il aide John à franchir la frontière et poursuit son trafic d'armes. Il boit davantage, et son utilité ne s'est pas améliorée.")},
   ]},
   {"summary": two("Behind the scenes","Coulisses"), "blocks": [
     {"p": two("Irish appears in Red Dead Redemption (2010). He is known only by that nickname; no other name is given for him in the game.",
               "Irish apparaît dans Red Dead Redemption (2010). Il n'est désigné que par ce surnom, et le jeu ne lui donne aucun autre nom.")},
   ]},
 ],
 "relationships": [
   {"name": "John Marston", "slug": "john-marston", "img": "john.jpeg",
    "text": two("The man he supplies, misleads, and eventually comes through for.",
                "L'homme qu'il fournit, mène en bateau, et finit par dépanner.")},
   {"name": "Nigel West Dickens", "slug": "nigel-west-dickens", "img": "nigel.jpeg",
    "text": two("Fellow recruit for Fort Mercer, whose stagecoach hides the Gatling gun.",
                "Autre recrue pour Fort Mercer, dont la diligence dissimule la Gatling.")},
   {"name": "Seth Briars", "slug": "seth-briars", "img": "seth.jpeg",
    "text": two("The third man in the Fort Mercer plan, who plays the corpse at the gate.",
                "Le troisième homme du plan de Fort Mercer, celui qui joue le mort devant les portes.")},
 ],
 "gallery": [
   {"img": "gallery-1.jpeg", "alt": two("Irish drinking while talking to John Marston","Irish en train de boire tout en parlant à John Marston"),
    "cap": two("Irish, drunk, explaining the latest plan to John.","Irish, ivre, exposant son dernier plan à John.")},
 ],
},
# ======================== 38. ARCHER FORDHAM ========================
{
 "order": 38, "slug": "archer-fordham", "name": "Archer Fordham",
 "publishDate": "2026-10-03", "schema_game": "Red Dead Redemption",
 "reg_role_en": "Bureau agent &middot; RDR1 &amp; 2", "reg_role_fr": "Agent du Bureau &middot; RDR1 &amp; 2",
 "gender": "Male", "death": None, "nationality": "American",
 "portrait_alt": two("Agent Archer Fordham with John Marston in the Bureau office in Red Dead Redemption",
                     "L'agent Archer Fordham avec John Marston dans le bureau du Bureau of Investigation dans Red Dead Redemption"),
 "eyebrow": two("Character &middot; Bureau of Investigation", "Personnage &middot; Bureau of Investigation"),
 "meta_desc": two("Archer Fordham: Edgar Ross's fellow Bureau of Investigation agent in Red Dead Redemption. Biography, his role in the blackmail of John Marston, and his RDR2 appearance.",
                  "Archer Fordham : l'agent du Bureau of Investigation qui seconde Edgar Ross dans Red Dead Redemption. Biographie, son rôle dans le chantage exercé sur John Marston, et son apparition dans RDR2."),
 "og_desc": two("The second federal agent on John Marston's case, present at every step from the blackmail to Beecher's Hope.",
                "Le second agent fédéral chargé du dossier Marston, présent à chaque étape, du chantage jusqu'à Beecher's Hope."),
 "schema_desc": two("Agent of the Bureau of Investigation in Red Dead Redemption.",
                    "Agent du Bureau of Investigation dans Red Dead Redemption."),
 "chips": [two("Bureau of Investigation", "Bureau of Investigation"), two("Federal agent", "Agent fédéral"),
           two("Alive", "Vivant"), two("RDR1 &amp; 2", "RDR1 &amp; 2")],
 "facts": [
   {"label": two("Affiliation","Affiliation"), "value": two("Bureau of Investigation","Bureau of Investigation")},
   {"label": two("Role","Rôle"), "value": two("Federal agent","Agent fédéral")},
   {"label": two("Works with","Travaille avec"), "value": two("Edgar Ross","Edgar Ross")},
   {"label": two("Status","Statut"), "value": two("Alive at the end of RDR1","Vivant à la fin de RDR1")},
   {"label": two("Games","Jeux"), "value": two("Red Dead Redemption, Red Dead Redemption 2","Red Dead Redemption, Red Dead Redemption 2")},
 ],
 "intro": [
   two("Archer Fordham is an agent of the Bureau of Investigation in Red Dead Redemption, and [[edgar-ross|Edgar Ross]]'s partner on the case against the Van der Linde gang.",
       "Archer Fordham est agent du Bureau of Investigation dans Red Dead Redemption, et le coéquipier d'[[edgar-ross|Edgar Ross]] sur le dossier du gang Van der Linde."),
   two("He is present at nearly every step of [[john-marston|John Marston]]'s coerced hunt, from the initial blackmail to the attack on Beecher's Hope.",
       "Il est présent à presque chaque étape de la traque imposée à [[john-marston|John Marston]], du chantage initial jusqu'à l'attaque de Beecher's Hope."),
 ],
 "sections": [
   {"summary": two("Biography","Biographie"), "open": True, "blocks": [
     {"h3": two("The case against Marston","Le dossier Marston")},
     {"p": two("Fordham and Ross take John's wife and son into government custody and send him west to bring in his former associates. Fordham handles much of the practical side of the operation: the paperwork, the transport, the coordination with the army and the local law.",
               "Fordham et Ross placent la femme et le fils de John sous la garde du gouvernement et l'envoient dans l'Ouest livrer ses anciens complices. Fordham assure une bonne part du côté pratique de l'opération : les dossiers, les transports, la coordination avec l'armée et les forces de l'ordre locales.")},
     {"h3": two("Alongside Ross","Aux côtés de Ross")},
     {"p": two("Fordham is the more measured of the two agents. He raises objections to Ross's methods and questions how far the operation should go, but he carries out the orders. He is with Ross in West Elizabeth for the hunt through Tall Trees, and at Beecher's Hope when the army moves on the ranch.",
               "Fordham est le plus mesuré des deux agents. Il émet des objections sur les méthodes de Ross et s'interroge sur les limites à donner à l'opération, mais il exécute les ordres. Il accompagne Ross dans West Elizabeth pour la traque dans Tall Trees, et se trouve à Beecher's Hope quand l'armée fond sur le ranch.")},
   ]},
   {"summary": two("In Red Dead Redemption 2","Dans Red Dead Redemption 2"), "blocks": [
     {"p": two("Fordham appears in the epilogue of Red Dead Redemption 2, alongside Ross, in the sequence where the two agents take an interest in [[micah-bell|Micah Bell]]. The appearance places both men on the gang's trail years before the events of the first game.",
               "Fordham apparaît dans l'épilogue de Red Dead Redemption 2, aux côtés de Ross, dans la séquence où les deux agents s'intéressent à [[micah-bell|Micah Bell]]. Cette apparition les place tous deux sur la piste du gang des années avant les événements du premier jeu.")},
   ]},
   {"summary": two("Behind the scenes","Coulisses"), "blocks": [
     {"p": two("Archer Fordham appears in Red Dead Redemption (2010) and in the epilogue of Red Dead Redemption 2 (2018).",
               "Archer Fordham apparaît dans Red Dead Redemption (2010) et dans l'épilogue de Red Dead Redemption 2 (2018).")},
   ]},
 ],
 "relationships": [
   {"name": "Edgar Ross", "slug": "edgar-ross", "img": "ross.jpeg",
    "text": two("His fellow Bureau agent, and the one who sets the terms for John.",
                "Son collègue du Bureau, celui qui fixe les conditions imposées à John.")},
   {"name": "John Marston", "slug": "john-marston", "img": "john.jpeg",
    "text": two("The man the Bureau coerces into hunting his former gang.",
                "L'homme que le Bureau contraint à traquer son ancien gang.")},
   {"name": "Andrew Milton", "slug": "andrew-milton", "img": "milton.jpeg",
    "text": two("The Pinkerton agent who pursued the same gang a decade earlier.",
                "L'agent Pinkerton qui poursuivait le même gang dix ans plus tôt.")},
 ],
 "gallery": [
   {"img": "gallery-1.jpeg", "alt": two("Agents Fordham and Ross at Beecher's Hope","Les agents Fordham et Ross à Beecher's Hope"),
    "cap": two("Fordham and Ross at Beecher's Hope in 1911.","Fordham et Ross à Beecher's Hope en 1911.")},
 ],
},
]

# "More characters" ccards. Only characters already live on each fiche's publishDate.
RELATED = {
 "agustin-allende":   ["john-marston", "abraham-reyes", "bill-williamson", "javier-escuella"],
 "vincente-de-santa": ["agustin-allende", "john-marston", "abraham-reyes", "landon-ricketts"],
 "luisa-fortuna":     ["abraham-reyes", "agustin-allende", "john-marston", "landon-ricketts"],
 "nastas":            ["john-marston", "edgar-ross", "dutch-van-der-linde", "jack-marston"],
 "harold-macdougal":  ["nastas", "john-marston", "edgar-ross", "dutch-van-der-linde"],
 "irish":             ["john-marston", "nigel-west-dickens", "seth-briars", "bonnie-macfarlane"],
 "archer-fordham":    ["edgar-ross", "john-marston", "andrew-milton", "jack-marston"],
}

# Characters this wave links to that gen_fiche's base REGISTRY does not carry.
EXTRA_REG = [
 ("abraham-reyes",     "Abraham Reyes",     "Revolutionary &middot; RDR1",   "Révolutionnaire &middot; RDR1"),
 ("javier-escuella",   "Javier Escuella",   "Van der Linde gang &middot; RDR1 &amp; 2", "Gang Van der Linde &middot; RDR1 &amp; 2"),
 ("edgar-ross",        "Edgar Ross",        "Antagonist &middot; RDR1",      "Antagoniste &middot; RDR1"),
 ("jack-marston",      "Jack Marston",      "Marston family &middot; RDR1 &amp; 2", "Famille Marston &middot; RDR1 &amp; 2"),
 ("landon-ricketts",   "Landon Ricketts",   "Gunslinger &middot; RDR1",      "Pistolero &middot; RDR1"),
 ("nigel-west-dickens","Nigel West Dickens","Con-artist &middot; RDR1",      "Escroc &middot; RDR1"),
 ("seth-briars",       "Seth Briars",       "Grave-robber &middot; RDR1",    "Pilleur de tombes &middot; RDR1"),
 ("bonnie-macfarlane", "Bonnie MacFarlane", "Rancher &middot; RDR1",         "Ranchère &middot; RDR1"),
 ("andrew-milton",     "Andrew Milton",     "Pinkerton agent &middot; RDR2", "Agent Pinkerton &middot; RDR2"),
]

if __name__ == "__main__":
    from gen_fiche import reg
    for slug, name, en, fr in EXTRA_REG:
        reg(slug, name, en, fr)
    for c in CHARS:
        reg(c["slug"], c["name"], c["reg_role_en"], c["reg_role_fr"])
    for c in CHARS:
        c["related"] = RELATED[c["slug"]]
        folder = build_to_queue(c)
        print("wrote", folder)
