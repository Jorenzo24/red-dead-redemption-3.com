#!/usr/bin/env python3
"""Wave 3 content -> _queue/. Run: python scripts/_wave3.py
Not deployed (scripts/ is excluded from .cpanel.yml).

Six fiches: Angelo Bronte, Leviticus Cornwall, Andrew Milton, Josiah Trelawny,
Molly O'Shea, Uncle. Factual register (no mood-prose). Images already staged in
assets/characters/<slug>/.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_fiche import build_to_queue

def two(en, fr): return {"en": en, "fr": fr}

CHARS = [
# ============================ 12. ANGELO BRONTE ============================
{
 "order": 12, "slug": "angelo-bronte", "name": "Angelo Bronte",
 "publishDate": "2026-07-09", "schema_game": "Red Dead Redemption 2",
 "reg_role_en": "Antagonist &middot; RDR2", "reg_role_fr": "Antagoniste &middot; RDR2",
 "gender": "Male", "death": "1899", "nationality": "Italian",
 "portrait_alt": two("Angelo Bronte in Red Dead Redemption 2", "Angelo Bronte dans Red Dead Redemption 2"),
 "eyebrow": two("Character &middot; Saint Denis", "Personnage &middot; Saint-Denis"),
 "meta_desc": two("Angelo Bronte: the crime lord who rules Saint Denis in Red Dead Redemption 2, buyer of the kidnapped Jack Marston. Biography, alliance and death.",
                  "Angelo Bronte : le chef de la pègre qui règne sur Saint-Denis dans Red Dead Redemption 2, acheteur du jeune Jack Marston enlevé. Biographie, alliance et mort."),
 "og_desc": two("The crime lord of Saint Denis who buys and returns Jack Marston, then dies at Dutch's hands.",
                "Le chef de la pègre de Saint-Denis qui achète puis rend Jack Marston, avant de mourir de la main de Dutch."),
 "schema_desc": two("Crime lord who controls the city of Saint Denis in Red Dead Redemption 2.",
                    "Chef de la pègre qui contrôle la ville de Saint-Denis dans Red Dead Redemption 2."),
 "chips": [two("Died <strong>1899</strong>", "Mort en <strong>1899</strong>"), two("Deceased", "Décédé"),
           two("Crime lord", "Chef de la pègre"), two("Saint Denis", "Saint-Denis")],
 "facts": [
   {"label": two("Died","Mort"), "value": two("1899","1899")},
   {"label": two("Status","Statut"), "value": two("Deceased","Décédé")},
   {"label": two("Nationality","Nationalité"), "value": two("Italian","Italienne")},
   {"label": two("Role","Rôle"), "value": two("Crime lord of Saint Denis","Chef de la pègre de Saint-Denis")},
   {"label": two("Games","Jeux"), "value": two("Red Dead Redemption 2","Red Dead Redemption 2")},
 ],
 "intro": [
   two("Angelo Bronte is the crime lord who controls the city of Saint Denis in Red Dead Redemption 2. An Italian-born gangster who styles himself a man of honour, he becomes first a reluctant ally and then an enemy of the Van der Linde gang.",
       "Angelo Bronte est le chef de la pègre qui contrôle la ville de Saint-Denis dans Red Dead Redemption 2. Gangster d'origine italienne qui se pose en homme d'honneur, il devient d'abord un allié réticent, puis un ennemi du gang Van der Linde."),
   two("Bronte is the man who buys the kidnapped [[jack-marston|Jack Marston]] and returns him to the gang, before [[dutch-van-der-linde|Dutch]] turns on him and kills him.",
       "Bronte est l'homme qui achète [[jack-marston|Jack Marston]], enlevé, puis le rend au gang, avant que [[dutch-van-der-linde|Dutch]] ne se retourne contre lui et le tue."),
 ],
 "sections": [
   {"summary": two("Biography","Biographie"), "open": True, "blocks": [
     {"h3": two("The boss of Saint Denis","Le patron de Saint-Denis")},
     {"p": two("Bronte rules Saint Denis through bribery, intimidation and political connections. When the Braithwaites sell him [[jack-marston|Jack Marston]], the gang comes to his mansion to get the boy back, and Bronte returns Jack in exchange for a job.",
               "Bronte règne sur Saint-Denis par la corruption, l'intimidation et ses appuis politiques. Quand les Braithwaite lui vendent [[jack-marston|Jack Marston]], le gang se rend à son manoir pour récupérer l'enfant, et Bronte rend Jack en échange d'un service.")},
     {"h3": two("Alliance and betrayal","Alliance et trahison")},
     {"p": two("Bronte and the gang work together briefly, but neither side trusts the other. In \"Revenge is a Dish Best Eaten\", the gang abducts him from his mansion, and [[dutch-van-der-linde|Dutch]] drowns him and feeds his body to an alligator.",
               "Bronte et le gang collaborent brièvement, mais aucun des deux camps ne fait confiance à l'autre. Dans « Revenge is a Dish Best Eaten », le gang l'enlève de son manoir, et [[dutch-van-der-linde|Dutch]] le noie avant de livrer son corps à un alligator.")},
   ]},
   {"summary": two("Personality","Personnalité"), "blocks": [
     {"p": two("Charming, theatrical and cruel, Bronte plays the part of a refined aristocrat of crime. Beneath the manners he is a brutal operator who treats violence as ordinary business.",
               "Charmeur, théâtral et cruel, Bronte joue le rôle d'un aristocrate raffiné du crime. Sous les manières se cache un homme brutal, pour qui la violence est une affaire ordinaire.")},
   ]},
   {"summary": two("Death and fate","Mort et destin"), "blocks": [
     {"p": two("Bronte is killed by [[dutch-van-der-linde|Dutch]] in 1899. His murder removes a major power in Saint Denis and is one of the clearest early signs of Dutch's growing instability.",
               "Bronte est tué par [[dutch-van-der-linde|Dutch]] en 1899. Son meurtre élimine une grande puissance de Saint-Denis et constitue l'un des signes les plus nets, très tôt, de l'instabilité grandissante de Dutch.")},
   ]},
   {"summary": two("Behind the scenes","Coulisses"), "blocks": [
     {"p": two("Bronte appears in Red Dead Redemption 2 (2018), mainly across Chapter 4. Though present for only one chapter, he is one of the game's most memorable antagonists.",
               "Bronte apparaît dans Red Dead Redemption 2 (2018), surtout au long du Chapitre 4. Bien que présent sur un seul chapitre, il est l'un des antagonistes les plus marquants du jeu.")},
   ]},
   {"summary": two("Trivia","Anecdotes"), "blocks": [
     {"ul": [
       two("He buys the kidnapped Jack Marston from the Braithwaites.","Il achète Jack Marston, enlevé, aux Braithwaite."),
       two("He calls himself a man of honour.","Il se présente comme un homme d'honneur."),
       two("He is drowned and killed by Dutch.","Il est noyé et tué par Dutch."),
     ]},
   ]},
 ],
 "relationships": [
   {"img": "dutch.jpeg", "slug": "dutch-van-der-linde", "name": "Dutch van der Linde", "text": two(
     "The gang leader he briefly allies with and who ultimately murders him.",
     "Le chef de gang avec qui il s'allie brièvement et qui finit par l'assassiner.")},
   {"img": "arthur.jpeg", "slug": "arthur-morgan", "name": "Arthur Morgan", "text": two(
     "Dutch's right hand, who deals with Bronte to recover Jack and takes part in his abduction.",
     "Le bras droit de Dutch, qui traite avec Bronte pour récupérer Jack et participe à son enlèvement.")},
   {"img": "jack.jpeg", "slug": "jack-marston", "name": "Jack Marston", "text": two(
     "The kidnapped boy Bronte holds and then returns to the gang.",
     "L'enfant enlevé que Bronte détient puis rend au gang.")},
   {"img": "john.jpeg", "slug": "john-marston", "name": "John Marston", "text": two(
     "Jack's father, desperate to get his son back from the Saint Denis crime lord.",
     "Le père de Jack, prêt à tout pour récupérer son fils des mains du chef de la pègre de Saint-Denis.")},
 ],
 "gallery": [
   {"img": "gallery-1.jpeg", "alt": two("Dutch confronting Angelo Bronte","Dutch face à Angelo Bronte"),
    "cap": two("Bronte's end at the hands of Dutch van der Linde.","La fin de Bronte, de la main de Dutch van der Linde.")},
 ],
 "related": ["dutch-van-der-linde", "micah-bell", "arthur-morgan", "john-marston"],
},
# ============================ 13. LEVITICUS CORNWALL ============================
{
 "order": 13, "slug": "leviticus-cornwall", "name": "Leviticus Cornwall",
 "publishDate": "2026-07-10", "schema_game": "Red Dead Redemption 2",
 "reg_role_en": "Antagonist &middot; RDR2", "reg_role_fr": "Antagoniste &middot; RDR2",
 "gender": "Male", "death": "1899",
 "portrait_alt": two("Leviticus Cornwall in Red Dead Redemption 2", "Leviticus Cornwall dans Red Dead Redemption 2"),
 "eyebrow": two("Character &middot; Red Dead Redemption 2", "Personnage &middot; Red Dead Redemption 2"),
 "meta_desc": two("Leviticus Cornwall: the industrialist whose railroad and oil empire makes him a major antagonist of Red Dead Redemption 2, and who funds the Pinkertons.",
                  "Leviticus Cornwall : l'industriel dont l'empire du rail et du pétrole en fait un antagoniste majeur de Red Dead Redemption 2, et qui finance les Pinkerton."),
 "og_desc": two("The railroad and oil magnate the gang robs, who hires the Pinkertons that hunt them.",
                "Le magnat du rail et du pétrole que le gang détrousse, et qui engage les Pinkerton lancés à leurs trousses."),
 "schema_desc": two("Wealthy industrialist and antagonist of Red Dead Redemption 2.",
                    "Riche industriel et antagoniste de Red Dead Redemption 2."),
 "chips": [two("Died <strong>1899</strong>", "Mort en <strong>1899</strong>"), two("Deceased", "Décédé"),
           two("Industrialist", "Industriel"), two("Red Dead Redemption 2", "Red Dead Redemption 2")],
 "facts": [
   {"label": two("Died","Mort"), "value": two("1899","1899")},
   {"label": two("Status","Statut"), "value": two("Deceased","Décédé")},
   {"label": two("Nationality","Nationalité"), "value": two("American","Américaine")},
   {"label": two("Role","Rôle"), "value": two("Railroad & oil magnate","Magnat du rail et du pétrole")},
   {"label": two("Games","Jeux"), "value": two("Red Dead Redemption 2","Red Dead Redemption 2")},
 ],
 "intro": [
   two("Leviticus Cornwall is one of the most powerful industrialists in the country and a major antagonist of Red Dead Redemption 2. His railroad, oil and shipping empire makes him a symbol of the industrial age closing in on the outlaw way of life.",
       "Leviticus Cornwall est l'un des industriels les plus puissants du pays et un antagoniste majeur de Red Dead Redemption 2. Son empire du rail, du pétrole et du transport maritime en fait un symbole de l'ère industrielle qui referme son étau sur la vie de hors-la-loi."),
   two("After the Van der Linde gang robs his train and attacks his oil interests, Cornwall uses his wealth to hire the Pinkertons who hunt them for the rest of the story.",
       "Après que le gang Van der Linde a braqué son train et s'en est pris à ses intérêts pétroliers, Cornwall met sa fortune au service des Pinkerton qu'il engage pour les traquer tout le reste de l'histoire."),
 ],
 "sections": [
   {"summary": two("Biography","Biographie"), "open": True, "blocks": [
     {"h3": two("An industrial empire","Un empire industriel")},
     {"p": two("Cornwall owns railroads, oil fields and shipping across the region. The gang first crosses him by robbing his private train in the mountains during [[dutch-van-der-linde|Dutch]]'s early plans.",
               "Cornwall possède des chemins de fer, des champs pétroliers et des lignes maritimes dans toute la région. Le gang le contrarie une première fois en braquant son train privé dans les montagnes, au tout début des plans de [[dutch-van-der-linde|Dutch]].")},
     {"h3": two("The vendetta","La vendetta")},
     {"p": two("The gang later strikes his oil business, deepening the feud. Cornwall's money buys the Pinkerton agents, led by [[andrew-milton|Agent Milton]], who pursue the gang relentlessly. He is killed during a confrontation with the gang at Annesburg.",
               "Le gang s'attaque ensuite à son commerce pétrolier, ce qui aggrave la vendetta. L'argent de Cornwall paie les agents Pinkerton, menés par [[andrew-milton|l'agent Milton]], qui traquent le gang sans relâche. Il est tué lors d'une confrontation avec le gang à Annesburg.")},
   ]},
   {"summary": two("Personality","Personnalité"), "blocks": [
     {"p": two("Cornwall is ruthless, arrogant and used to getting his way. He regards the gang as vermin to be exterminated and treats his fortune as a licence to command men and the law alike.",
               "Cornwall est impitoyable, arrogant et habitué à ce qu'on lui obéisse. Il considère le gang comme de la vermine à exterminer et voit sa fortune comme un droit de commander aux hommes comme à la loi.")},
   ]},
   {"summary": two("Death and fate","Mort et destin"), "blocks": [
     {"p": two("Cornwall is killed in 1899 during a standoff with the Van der Linde gang at the Annesburg docks. His death does nothing to call off the Pinkertons his money had already set loose.",
               "Cornwall est tué en 1899 lors d'un face-à-face avec le gang Van der Linde sur les quais d'Annesburg. Sa mort ne suffit pas à rappeler les Pinkerton que son argent avait déjà lâchés.")},
   ]},
   {"summary": two("Behind the scenes","Coulisses"), "blocks": [
     {"p": two("Cornwall appears in Red Dead Redemption 2 (2018). His company and its rolling stock, Cornwall Kerosene & Tar, recur throughout the game as a backdrop to the gang's crimes.",
               "Cornwall apparaît dans Red Dead Redemption 2 (2018). Sa société et ses wagons, la Cornwall Kerosene & Tar, reviennent tout au long du jeu en toile de fond des crimes du gang.")},
   ]},
   {"summary": two("Trivia","Anecdotes"), "blocks": [
     {"ul": [
       two("His company is Cornwall Kerosene & Tar.","Sa société est la Cornwall Kerosene & Tar."),
       two("Robbing his train early on starts the feud with the gang.","Le braquage de son train, au début, déclenche la vendetta avec le gang."),
       two("He funds the Pinkertons who hunt the Van der Lindes.","Il finance les Pinkerton qui traquent les Van der Linde."),
     ]},
   ]},
 ],
 "relationships": [
   {"img": "dutch.jpeg", "slug": "dutch-van-der-linde", "name": "Dutch van der Linde", "text": two(
     "The outlaw leader whose gang robs him and defies him, and whom Cornwall spends a fortune to destroy.",
     "Le chef hors-la-loi dont le gang le détrousse et le défie, et que Cornwall dépense une fortune à vouloir détruire.")},
   {"img": "milton.jpeg", "slug": "andrew-milton", "name": "Andrew Milton", "text": two(
     "The Pinkerton agent Cornwall's money puts on the gang's trail.",
     "L'agent Pinkerton que l'argent de Cornwall lance sur la piste du gang.")},
   {"img": "arthur.jpeg", "slug": "arthur-morgan", "name": "Arthur Morgan", "text": two(
     "The gang enforcer at the sharp end of the robberies that make Cornwall an enemy.",
     "L'homme de main du gang en première ligne des braquages qui font de Cornwall un ennemi.")},
   {"img": "john.jpeg", "slug": "john-marston", "name": "John Marston", "text": two(
     "Another Van der Linde gunman caught up in the war Cornwall's wealth unleashes on them.",
     "Un autre fusil des Van der Linde pris dans la guerre que la fortune de Cornwall déchaîne sur eux.")},
 ],
 "gallery": [
   {"img": "gallery-1.jpeg", "alt": two("A portrait of Leviticus Cornwall","Un portrait de Leviticus Cornwall"),
    "cap": two("Leviticus Cornwall, magnate of the new industrial age.","Leviticus Cornwall, magnat de la nouvelle ère industrielle.")},
 ],
 "related": ["dutch-van-der-linde", "micah-bell", "arthur-morgan", "bill-williamson"],
},
# ============================ 14. ANDREW MILTON ============================
{
 "order": 14, "slug": "andrew-milton", "name": "Andrew Milton",
 "publishDate": "2026-07-11", "schema_game": "Red Dead Redemption 2",
 "reg_role_en": "Pinkerton agent &middot; RDR2", "reg_role_fr": "Agent Pinkerton &middot; RDR2",
 "gender": "Male", "death": "1899",
 "portrait_alt": two("Agent Andrew Milton in Red Dead Redemption 2", "L'agent Andrew Milton dans Red Dead Redemption 2"),
 "eyebrow": two("Character &middot; Pinkerton Agency", "Personnage &middot; Agence Pinkerton"),
 "meta_desc": two("Andrew Milton: the lead Pinkerton agent hunting the Van der Linde gang in Red Dead Redemption 2, and the man who kills Hosea Matthews. Biography and death.",
                  "Andrew Milton : l'agent Pinkerton en chef qui traque le gang Van der Linde dans Red Dead Redemption 2, et l'homme qui tue Hosea Matthews. Biographie et mort."),
 "og_desc": two("The relentless Pinkerton agent who hunts the gang and executes Hosea Matthews.",
                "L'agent Pinkerton implacable qui traque le gang et exécute Hosea Matthews."),
 "schema_desc": two("Lead Pinkerton agent pursuing the Van der Linde gang in Red Dead Redemption 2.",
                    "Agent Pinkerton en chef lancé aux trousses du gang Van der Linde dans Red Dead Redemption 2."),
 "chips": [two("Died <strong>1899</strong>", "Mort en <strong>1899</strong>"), two("Deceased", "Décédé"),
           two("Pinkerton Agency", "Agence Pinkerton"), two("Red Dead Redemption 2", "Red Dead Redemption 2")],
 "facts": [
   {"label": two("Died","Mort"), "value": two("1899","1899")},
   {"label": two("Status","Statut"), "value": two("Deceased","Décédé")},
   {"label": two("Nationality","Nationalité"), "value": two("American","Américaine")},
   {"label": two("Affiliation","Affiliation"), "value": two("Pinkerton National Detective Agency","Agence de détectives Pinkerton")},
   {"label": two("Role","Rôle"), "value": two("Detective","Détective")},
   {"label": two("Games","Jeux"), "value": two("Red Dead Redemption 2","Red Dead Redemption 2")},
 ],
 "intro": [
   two("Agent Andrew Milton is the lead Pinkerton detective hunting the Van der Linde gang in Red Dead Redemption 2. Calm, relentless and self-righteous, he is the human face of the law closing in on [[dutch-van-der-linde|Dutch]]'s gang.",
       "L'agent Andrew Milton est le détective Pinkerton en chef qui traque le gang Van der Linde dans Red Dead Redemption 2. Posé, implacable et sûr de son bon droit, il est le visage humain de la loi qui se referme sur le gang de [[dutch-van-der-linde|Dutch]]."),
   two("Milton personally kills [[hosea-matthews|Hosea Matthews]] during the Saint Denis bank robbery and pursues the gang all the way to its final days.",
       "Milton tue de sa main [[hosea-matthews|Hosea Matthews]] pendant le braquage de la banque de Saint-Denis et poursuit le gang jusqu'à ses tout derniers jours."),
 ],
 "sections": [
   {"summary": two("Biography","Biographie"), "open": True, "blocks": [
     {"h3": two("The hunt","La traque")},
     {"p": two("Backed by [[leviticus-cornwall|Leviticus Cornwall]] and the state, Milton and his partner Agent Ross track the gang across the country, confronting [[arthur-morgan|Arthur]] and Dutch several times and slowly tightening the net.",
               "Soutenus par [[leviticus-cornwall|Leviticus Cornwall]] et l'État, Milton et son coéquipier, l'agent Ross, traquent le gang à travers le pays, confrontant plusieurs fois [[arthur-morgan|Arthur]] et Dutch et resserrant peu à peu l'étau.")},
     {"h3": two("Killing Hosea, and the end","La mort de Hosea, et la fin")},
     {"p": two("During the botched Saint Denis bank robbery, Milton executes [[hosea-matthews|Hosea]] in the street. He keeps up the pursuit to Beaver Hollow, where he is shot dead by [[abigail-marston|Abigail Marston]].",
               "Pendant le braquage raté de la banque de Saint-Denis, Milton exécute [[hosea-matthews|Hosea]] en pleine rue. Il poursuit sa traque jusqu'à Beaver Hollow, où il est abattu par [[abigail-marston|Abigail Marston]].")},
   ]},
   {"summary": two("Personality","Personnalité"), "blocks": [
     {"p": two("Milton is composed and moralizing, convinced he stands for civilization against savagery. His calm certainty makes him more chilling than any hot-headed lawman.",
               "Milton est posé et moralisateur, convaincu d'incarner la civilisation face à la sauvagerie. Sa certitude tranquille le rend plus glaçant que n'importe quel représentant de la loi au sang chaud.")},
   ]},
   {"summary": two("Death and fate","Mort et destin"), "blocks": [
     {"p": two("Milton is killed at Beaver Hollow in 1899. Cornered by the gang, he is shot by [[abigail-marston|Abigail Marston]], but not before his words help expose the traitor within the gang.",
               "Milton est tué à Beaver Hollow en 1899. Acculé par le gang, il est abattu par [[abigail-marston|Abigail Marston]], mais pas avant que ses paroles n'aident à démasquer le traître au sein du gang.")},
   ]},
   {"summary": two("Behind the scenes","Coulisses"), "blocks": [
     {"p": two("Milton appears throughout Red Dead Redemption 2 (2018) as the gang's chief pursuer. He is the recurring, patient antagonist who represents the law itself rather than a personal vendetta.",
               "Milton apparaît tout au long de Red Dead Redemption 2 (2018) comme le principal poursuivant du gang. C'est l'antagoniste récurrent et patient qui incarne la loi elle-même plutôt qu'une vengeance personnelle.")},
   ]},
   {"summary": two("Trivia","Anecdotes"), "blocks": [
     {"ul": [
       two("He works for the Pinkerton National Detective Agency.","Il travaille pour l'agence de détectives Pinkerton."),
       two("He kills Hosea Matthews during the Saint Denis bank robbery.","Il tue Hosea Matthews pendant le braquage de Saint-Denis."),
       two("He is killed by Abigail Marston at Beaver Hollow.","Il est tué par Abigail Marston à Beaver Hollow."),
     ]},
   ]},
 ],
 "relationships": [
   {"img": "dutch.jpeg", "slug": "dutch-van-der-linde", "name": "Dutch van der Linde", "text": two(
     "The gang leader Milton is determined to bring in, and whose downfall he patiently engineers.",
     "Le chef de gang que Milton est déterminé à faire tomber, et dont il orchestre patiemment la chute.")},
   {"img": "arthur.jpeg", "slug": "arthur-morgan", "name": "Arthur Morgan", "text": two(
     "Dutch's enforcer, whom Milton confronts and taunts repeatedly across the hunt.",
     "L'homme de main de Dutch, que Milton confronte et provoque à plusieurs reprises au fil de la traque.")},
   {"img": "hosea.jpeg", "slug": "hosea-matthews", "name": "Hosea Matthews", "text": two(
     "The gang elder Milton executes in the street during the Saint Denis bank robbery.",
     "L'ancien du gang que Milton exécute en pleine rue lors du braquage de Saint-Denis.")},
   {"img": "abigail.jpeg", "slug": "abigail-marston", "name": "Abigail Marston", "text": two(
     "The woman who finally kills Milton at Beaver Hollow.",
     "La femme qui finit par tuer Milton à Beaver Hollow.")},
 ],
 "gallery": [
   {"img": "gallery-1.jpeg", "alt": two("Agent Milton confronting the gang","L'agent Milton face au gang"),
    "cap": two("Milton, the Pinkerton who never stops hunting the gang.","Milton, le Pinkerton qui ne cesse jamais de traquer le gang.")},
 ],
 "related": ["dutch-van-der-linde", "arthur-morgan", "hosea-matthews", "micah-bell"],
},
# ============================ 15. JOSIAH TRELAWNY ============================
{
 "order": 15, "slug": "josiah-trelawny", "name": "Josiah Trelawny",
 "publishDate": "2026-07-12", "schema_game": "Red Dead Redemption 2",
 "reg_role_en": "Van der Linde gang &middot; RDR2", "reg_role_fr": "Gang Van der Linde &middot; RDR2",
 "gender": "Male",
 "portrait_alt": two("Josiah Trelawny in Red Dead Redemption 2", "Josiah Trelawny dans Red Dead Redemption 2"),
 "eyebrow": two("Character &middot; Van der Linde gang", "Personnage &middot; Gang Van der Linde"),
 "meta_desc": two("Josiah Trelawny: the con man, magician and fixer of the Van der Linde gang in Red Dead Redemption 2. Biography, role, and how he survives the story.",
                  "Josiah Trelawny : l'escroc, magicien et intermédiaire du gang Van der Linde dans Red Dead Redemption 2. Biographie, rôle, et comment il survit à l'histoire."),
 "og_desc": two("The gang's charming con man and fixer, who keeps a secret family and survives the story.",
                "L'escroc charmeur et intermédiaire du gang, qui cache une famille et survit à l'histoire."),
 "schema_desc": two("Con man and fixer loosely attached to the Van der Linde gang.",
                    "Escroc et intermédiaire vaguement rattaché au gang Van der Linde."),
 "chips": [two("Red Dead Redemption 2", "Red Dead Redemption 2"), two("Con man &amp; fixer", "Escroc et intermédiaire"),
           two("Van der Linde gang", "Gang Van der Linde"), two("Survivor", "Survivant")],
 "facts": [
   {"label": two("Status","Statut"), "value": two("Alive (survives)","En vie (survit)")},
   {"label": two("Nationality","Nationalité"), "value": two("British","Britannique")},
   {"label": two("Affiliation","Affiliation"), "value": two("Van der Linde gang (associate)","Gang Van der Linde (associé)")},
   {"label": two("Role","Rôle"), "value": two("Con man, magician, fixer","Escroc, magicien, intermédiaire")},
   {"label": two("Games","Jeux"), "value": two("Red Dead Redemption 2","Red Dead Redemption 2")},
 ],
 "intro": [
   two("Josiah Trelawny is a con man, magician and fixer loosely attached to the Van der Linde gang in Red Dead Redemption 2. Charming and theatrical, he sets up scores and solves problems but keeps the outlaw life at arm's length.",
       "Josiah Trelawny est un escroc, magicien et intermédiaire vaguement rattaché au gang Van der Linde dans Red Dead Redemption 2. Charmeur et théâtral, il monte des coups et règle les problèmes tout en tenant la vie de hors-la-loi à distance."),
   two("Unlike the others, Trelawny keeps a secret family he protects, and he drifts in and out of the gang rather than living in the camp full time.",
       "Contrairement aux autres, Trelawny protège une famille tenue secrète, et il va et vient dans le gang plutôt que de vivre au camp à plein temps."),
 ],
 "sections": [
   {"summary": two("Biography","Biographie"), "open": True, "blocks": [
     {"h3": two("The gang's fixer","L'intermédiaire du gang")},
     {"p": two("Trelawny arranges opportunities for the gang, from confidence schemes to freeing captured members. [[arthur-morgan|Arthur]] works several jobs at his side, especially around Saint Denis.",
               "Trelawny déniche des occasions pour le gang, de l'arnaque à la libération de membres capturés. [[arthur-morgan|Arthur]] mène plusieurs coups à ses côtés, notamment autour de Saint-Denis.")},
     {"h3": two("A man apart","Un homme à part")},
     {"p": two("Trelawny is careful never to be fully swallowed by the gang. He has a wife and sons he keeps hidden from the outlaw world, and that caution is part of why he lives to see the other side of the story.",
               "Trelawny veille à ne jamais se laisser happer entièrement par le gang. Il a une épouse et des fils qu'il tient à l'écart du monde des hors-la-loi, et cette prudence explique en partie pourquoi il survit jusqu'à l'autre bout de l'histoire.")},
   ]},
   {"summary": two("Personality","Personnalité"), "blocks": [
     {"p": two("Witty, elegant and self-preserving, Trelawny is a performer who talks his way into and out of trouble. His loyalty is real but always weighed against his own survival and his family.",
               "Spirituel, élégant et soucieux de sa peau, Trelawny est un bonimenteur qui s'attire les ennuis et s'en sort par le verbe. Sa loyauté est réelle, mais toujours mise en balance avec sa survie et sa famille.")},
   ]},
   {"summary": two("Fate","Destin"), "blocks": [
     {"p": two("Trelawny is one of the gang members who survives the events of Red Dead Redemption 2, slipping away before the collapse to return to the family he kept hidden.",
               "Trelawny fait partie des membres du gang qui survivent aux événements de Red Dead Redemption 2, s'éclipsant avant l'effondrement pour retrouver la famille qu'il tenait cachée.")},
   ]},
   {"summary": two("Behind the scenes","Coulisses"), "blocks": [
     {"p": two("Trelawny appears in Red Dead Redemption 2 (2018) as a recurring associate rather than a full camp member, a role that suits his careful distance from the gang's fate.",
               "Trelawny apparaît dans Red Dead Redemption 2 (2018) comme un associé récurrent plutôt qu'un membre à part entière du camp, un rôle en accord avec la distance prudente qu'il garde vis-à-vis du sort du gang.")},
   ]},
   {"summary": two("Trivia","Anecdotes"), "blocks": [
     {"ul": [
       two("He is a magician and con artist.","C'est un magicien et un escroc."),
       two("He keeps a secret wife and sons.","Il cache une épouse et des fils."),
       two("He survives the events of the game.","Il survit aux événements du jeu."),
     ]},
   ]},
 ],
 "relationships": [
   {"img": "arthur.jpeg", "slug": "arthur-morgan", "name": "Arthur Morgan", "text": two(
     "His most frequent partner in schemes, especially the cons around Saint Denis.",
     "Son partenaire le plus fréquent dans les combines, notamment les arnaques autour de Saint-Denis.")},
   {"img": "dutch.jpeg", "slug": "dutch-van-der-linde", "name": "Dutch van der Linde", "text": two(
     "The gang leader Trelawny works for at a deliberate distance, never fully one of the camp.",
     "Le chef de gang pour qui Trelawny travaille à distance choisie, sans jamais être tout à fait du camp.")},
   {"img": "hosea.jpeg", "slug": "hosea-matthews", "name": "Hosea Matthews", "text": two(
     "A fellow schemer whose taste for the con Trelawny shares.",
     "Un autre manœuvrier, avec qui Trelawny partage le goût de l'arnaque.")},
   {"img": "john.jpeg", "slug": "john-marston", "name": "John Marston", "text": two(
     "A gang member alongside whom Trelawny occasionally works when his plans need extra hands.",
     "Un membre du gang aux côtés duquel Trelawny travaille à l'occasion, quand ses plans réclament des bras.")},
 ],
 "gallery": [
   {"img": "gallery-1.jpeg", "alt": two("Josiah Trelawny with the gang","Josiah Trelawny avec le gang"),
    "cap": two("Trelawny, the gang's smooth-talking fixer.","Trelawny, l'intermédiaire beau parleur du gang.")},
 ],
 "related": ["dutch-van-der-linde", "arthur-morgan", "hosea-matthews", "john-marston"],
},
# ============================ 16. MOLLY O'SHEA ============================
{
 "order": 16, "slug": "molly-oshea", "name": "Molly O'Shea",
 "publishDate": "2026-07-13", "schema_game": "Red Dead Redemption 2",
 "reg_role_en": "Van der Linde gang &middot; RDR2", "reg_role_fr": "Gang Van der Linde &middot; RDR2",
 "gender": "Female", "death": "1899", "nationality": "Irish",
 "portrait_alt": two("Molly O'Shea in Red Dead Redemption 2", "Molly O'Shea dans Red Dead Redemption 2"),
 "eyebrow": two("Character &middot; Van der Linde gang", "Personnage &middot; Gang Van der Linde"),
 "meta_desc": two("Molly O'Shea: Dutch van der Linde's lover in Red Dead Redemption 2, an Irishwoman whose story ends in tragedy at Shady Belle. Biography, relationships, death.",
                  "Molly O'Shea : la compagne de Dutch van der Linde dans Red Dead Redemption 2, une Irlandaise dont l'histoire s'achève en tragédie à Shady Belle. Biographie, relations, mort."),
 "og_desc": two("Dutch's neglected Irish lover, whose story ends in a tragic death at Shady Belle.",
                "La compagne irlandaise délaissée de Dutch, dont l'histoire s'achève par une mort tragique à Shady Belle."),
 "schema_desc": two("Irish lover of Dutch van der Linde and member of his gang's camp.",
                    "Compagne irlandaise de Dutch van der Linde et membre du camp de son gang."),
 "chips": [two("Died <strong>1899</strong>", "Morte en <strong>1899</strong>"), two("Deceased", "Décédée"),
           two("Van der Linde gang", "Gang Van der Linde"), two("Dutch's lover", "Compagne de Dutch")],
 "facts": [
   {"label": two("Died","Mort"), "value": two("1899","1899")},
   {"label": two("Status","Statut"), "value": two("Deceased","Décédée")},
   {"label": two("Nationality","Nationalité"), "value": two("Irish","Irlandaise")},
   {"label": two("Affiliation","Affiliation"), "value": two("Van der Linde gang","Gang Van der Linde")},
   {"label": two("Relationship","Relation"), "value": two("[[dutch-van-der-linde|Dutch van der Linde]] (lover)","[[dutch-van-der-linde|Dutch van der Linde]] (compagne)")},
   {"label": two("Games","Jeux"), "value": two("Red Dead Redemption 2","Red Dead Redemption 2")},
 ],
 "intro": [
   two("Molly O'Shea is [[dutch-van-der-linde|Dutch van der Linde]]'s lover in Red Dead Redemption 2, an Irishwoman who left a comfortable life to be with the gang's leader. As Dutch grows colder and more distant, Molly becomes increasingly isolated in the camp.",
       "Molly O'Shea est la compagne de [[dutch-van-der-linde|Dutch van der Linde]] dans Red Dead Redemption 2, une Irlandaise qui a quitté une vie confortable pour le chef du gang. À mesure que Dutch devient plus froid et plus distant, Molly s'isole de plus en plus au sein du camp."),
   two("Looked down on by some members and neglected by Dutch, her story ends in tragedy during the gang's time at Shady Belle.",
       "Méprisée par certains membres et délaissée par Dutch, son histoire s'achève en tragédie durant le séjour du gang à Shady Belle."),
 ],
 "sections": [
   {"summary": two("Biography","Biographie"), "open": True, "blocks": [
     {"h3": two("Dutch's companion","La compagne de Dutch")},
     {"p": two("Molly joined the gang for [[dutch-van-der-linde|Dutch]] and struggles with camp life. She does little of the daily work, is resented by some of the other women, and is increasingly ignored by Dutch as his schemes consume him.",
               "Molly a rejoint le gang pour [[dutch-van-der-linde|Dutch]] et s'accommode mal de la vie de camp. Elle participe peu aux tâches quotidiennes, s'attire le ressentiment de certaines autres femmes, et se voit de plus en plus ignorée par Dutch, que ses plans dévorent.")},
     {"h3": two("A fatal outburst","Un éclat fatal")},
     {"p": two("Drunk and heartbroken at Shady Belle, Molly claims she told the Pinkertons about the Saint Denis bank job. [[susan-grimshaw|Susan Grimshaw]] shoots her, and it later emerges that Molly had not actually betrayed the gang.",
               "Ivre et le cœur brisé à Shady Belle, Molly prétend avoir parlé du braquage de Saint-Denis aux Pinkerton. [[susan-grimshaw|Susan Grimshaw]] l'abat, et il apparaît plus tard que Molly n'avait en réalité pas trahi le gang.")},
   ]},
   {"summary": two("Personality","Personnalité"), "blocks": [
     {"p": two("Molly is proud, passionate and lonely. She craves Dutch's attention and resents the camp's disdain, a combination that leaves her dangerously isolated as the gang's troubles mount.",
               "Molly est fière, passionnée et seule. Elle réclame l'attention de Dutch et supporte mal le dédain du camp, un mélange qui la laisse dangereusement isolée à mesure que les ennuis du gang s'accumulent.")},
   ]},
   {"summary": two("Death and fate","Mort et destin"), "blocks": [
     {"p": two("Molly is killed at Shady Belle in 1899, shot by [[susan-grimshaw|Susan Grimshaw]] after a false confession born of jealousy and despair rather than any real betrayal.",
               "Molly est tuée à Shady Belle en 1899, abattue par [[susan-grimshaw|Susan Grimshaw]] après un faux aveu né de la jalousie et du désespoir, et non d'une véritable trahison.")},
   ]},
   {"summary": two("Behind the scenes","Coulisses"), "blocks": [
     {"p": two("Molly appears in Red Dead Redemption 2 (2018). Her arc is one of the game's clearest portraits of how Dutch's growing coldness destroys the people closest to him.",
               "Molly apparaît dans Red Dead Redemption 2 (2018). Son parcours est l'un des portraits les plus nets, dans le jeu, de la façon dont la froideur grandissante de Dutch détruit ses proches.")},
   ]},
   {"summary": two("Trivia","Anecdotes"), "blocks": [
     {"ul": [
       two("She is Dutch van der Linde's lover.","Elle est la compagne de Dutch van der Linde."),
       two("She is Irish and left a comfortable life for the gang.","Elle est irlandaise et a quitté une vie confortable pour le gang."),
       two("She is killed after falsely claiming to have informed on the gang.","Elle est tuée après avoir faussement prétendu avoir dénoncé le gang."),
     ]},
   ]},
 ],
 "relationships": [
   {"img": "dutch.jpeg", "slug": "dutch-van-der-linde", "name": "Dutch van der Linde", "text": two(
     "Her lover, whose growing neglect and coldness drive her isolation and, indirectly, her death.",
     "Son compagnon, dont l'indifférence et la froideur croissantes nourrissent son isolement et, indirectement, sa mort.")},
   {"img": "susan.jpeg", "slug": "susan-grimshaw", "name": "Susan Grimshaw", "text": two(
     "The camp matriarch who shoots Molly after her false confession.",
     "La matriarche du camp qui abat Molly après son faux aveu.")},
   {"img": "arthur.jpeg", "slug": "arthur-morgan", "name": "Arthur Morgan", "text": two(
     "A gang member who witnesses Molly's unravelling in the camp's final months.",
     "Un membre du gang qui assiste à la déchéance de Molly dans les derniers mois du camp.")},
   {"img": "hosea.jpeg", "slug": "hosea-matthews", "name": "Hosea Matthews", "text": two(
     "A gang elder who sees, like Arthur, how Dutch's choices are poisoning the camp around him.",
     "Un ancien du gang qui voit, comme Arthur, combien les choix de Dutch empoisonnent le camp autour de lui.")},
 ],
 "gallery": [
   {"img": "gallery-1.jpeg", "alt": two("Molly O'Shea at the camp","Molly O'Shea au camp"),
    "cap": two("Molly O'Shea at the gang's camp.","Molly O'Shea au camp du gang.")},
 ],
 "related": ["dutch-van-der-linde", "hosea-matthews", "sadie-adler", "arthur-morgan"],
},
# ============================ 17. UNCLE ============================
{
 "order": 17, "slug": "uncle", "name": "Uncle",
 "publishDate": "2026-07-14", "schema_game": "Red Dead Redemption 2",
 "reg_role_en": "Van der Linde gang &middot; RDR1 &amp; 2", "reg_role_fr": "Gang Van der Linde &middot; RDR1 &amp; 2",
 "gender": "Male", "death": "1911",
 "portrait_alt": two("Uncle in Red Dead Redemption 2", "Uncle dans Red Dead Redemption 2"),
 "eyebrow": two("Character &middot; Van der Linde gang", "Personnage &middot; Gang Van der Linde"),
 "meta_desc": two("Uncle: the lazy, hard-drinking old outlaw of the Van der Linde gang and the Marston ranch, a comic figure across both Red Dead Redemption games. Biography and death.",
                  "Uncle : le vieux hors-la-loi fainéant et porté sur la bouteille du gang Van der Linde et du ranch Marston, figure comique des deux Red Dead Redemption. Biographie et mort."),
 "og_desc": two("The gang's work-shy old freeloader who dies defending the Marston ranch in 1911.",
                "Le vieux parasite fainéant du gang, qui meurt en défendant le ranch des Marston en 1911."),
 "schema_desc": two("Aging outlaw of the Van der Linde gang and later the Marston household.",
                    "Vieux hors-la-loi du gang Van der Linde, puis du foyer Marston."),
 "chips": [two("Died <strong>1911</strong>", "Mort en <strong>1911</strong>"), two("Deceased", "Décédé"),
           two("Van der Linde gang", "Gang Van der Linde"), two("RDR1 &amp; 2", "RDR1 &amp; 2")],
 "facts": [
   {"label": two("Died","Mort"), "value": two("1911","1911")},
   {"label": two("Status","Statut"), "value": two("Deceased","Décédé")},
   {"label": two("Nationality","Nationalité"), "value": two("American","Américaine")},
   {"label": two("Affiliation","Affiliation"), "value": two("Van der Linde gang, Marston ranch","Gang Van der Linde, ranch Marston")},
   {"label": two("Games","Jeux"), "value": two("Red Dead Redemption, Red Dead Redemption 2","Red Dead Redemption, Red Dead Redemption 2")},
 ],
 "intro": [
   two("Uncle is a lazy, hard-drinking old outlaw attached to the Van der Linde gang and later to the Marston household, a comic-relief fixture across both Red Dead Redemption games.",
       "Uncle est un vieux hors-la-loi fainéant et porté sur la bouteille, rattaché au gang Van der Linde puis au foyer Marston, une figure comique récurrente des deux Red Dead Redemption."),
   two("Famous for dodging work by blaming his \"lumbago\", Uncle is loyal to the family in his own way, and he dies defending it.",
       "Célèbre pour esquiver le travail en invoquant son « lumbago », Uncle est loyal à la famille à sa façon, et il meurt en la défendant."),
 ],
 "sections": [
   {"summary": two("Biography","Biographie"), "open": True, "blocks": [
     {"h3": two("The gang's freeloader","Le parasite du gang")},
     {"p": two("Uncle does as little as possible around camp, forever nursing a bottle and a bad back. Despite this, he is part of the gang's extended family and takes part in a handful of its schemes.",
               "Uncle en fait le moins possible au camp, toujours à soigner une bouteille et un mal de dos. Il n'en fait pas moins partie de la famille élargie du gang et prend part à quelques-uns de ses coups.")},
     {"h3": two("Beecher's Hope","Beecher's Hope")},
     {"p": two("After the gang falls, Uncle attaches himself to [[john-marston|John]] and [[abigail-marston|Abigail Marston]]'s ranch at Beecher's Hope, helping, a little, to run it in the years that follow.",
               "Après la chute du gang, Uncle s'attache au ranch de [[john-marston|John]] et [[abigail-marston|Abigail Marston]] à Beecher's Hope, aidant, un peu, à le faire tourner dans les années qui suivent.")},
   ]},
   {"summary": two("Personality","Personnalité"), "blocks": [
     {"p": two("Idle, witty and self-serving, Uncle is the source of much of the gang's humour. For all his laziness, his loyalty to the family is real, and in the end he proves it.",
               "Oisif, spirituel et intéressé, Uncle est à l'origine d'une grande part de l'humour du gang. Malgré toute sa paresse, sa loyauté envers la famille est réelle, et il finit par le prouver.")},
   ]},
   {"summary": two("Death and fate","Mort et destin"), "blocks": [
     {"p": two("Uncle is killed in 1911 during the government's raid on Beecher's Hope, gunned down helping [[john-marston|John]] and the Marstons defend the ranch.",
               "Uncle est tué en 1911 lors du raid du gouvernement sur Beecher's Hope, abattu alors qu'il aide [[john-marston|John]] et les Marston à défendre le ranch.")},
   ]},
   {"summary": two("Behind the scenes","Coulisses"), "blocks": [
     {"p": two("Uncle appears in both Red Dead Redemption (2010) and Red Dead Redemption 2 (2018), one of the few characters present across the whole saga.",
               "Uncle apparaît dans Red Dead Redemption (2010) comme dans Red Dead Redemption 2 (2018), l'un des rares personnages présents sur toute la saga.")},
   ]},
   {"summary": two("Trivia","Anecdotes"), "blocks": [
     {"ul": [
       two("He blames his laziness on \"lumbago\".","Il met sa paresse sur le compte de son « lumbago »."),
       two("He appears in both main Red Dead Redemption games.","Il apparaît dans les deux jeux principaux Red Dead Redemption."),
       two("He dies defending Beecher's Hope in 1911.","Il meurt en défendant Beecher's Hope en 1911."),
     ]},
   ]},
 ],
 "relationships": [
   {"img": "john.jpeg", "slug": "john-marston", "name": "John Marston", "text": two(
     "The former gang member whose ranch Uncle joins, and beside whom he makes his last stand.",
     "L'ancien membre du gang dont Uncle rejoint le ranch, et aux côtés de qui il livre son dernier combat.")},
   {"img": "abigail.jpeg", "slug": "abigail-marston", "name": "Abigail Marston", "text": two(
     "The woman of the Beecher's Hope household, who tolerates Uncle's idleness as part of the family.",
     "La maîtresse de maison de Beecher's Hope, qui tolère l'oisiveté d'Uncle comme un membre de la famille.")},
   {"img": "arthur.jpeg", "slug": "arthur-morgan", "name": "Arthur Morgan", "text": two(
     "A gang brother from the old days, often the target and the source of Uncle's jokes.",
     "Un frère de gang du temps jadis, souvent cible et source des plaisanteries d'Uncle.")},
   {"img": "dutch.jpeg", "slug": "dutch-van-der-linde", "name": "Dutch van der Linde", "text": two(
     "The leader whose gang Uncle rode with for years before the family scattered.",
     "Le chef dont Uncle a suivi le gang pendant des années, avant la dispersion de la famille.")},
 ],
 "gallery": [
   {"img": "gallery-1.jpeg", "alt": two("Uncle in Red Dead Redemption 2","Uncle dans Red Dead Redemption 2"),
    "cap": two("Uncle, the gang's work-shy old survivor.","Uncle, le vieux survivant fainéant du gang.")},
 ],
 "related": ["john-marston", "arthur-morgan", "dutch-van-der-linde", "sadie-adler"],
},
]

if __name__ == "__main__":
    for c in CHARS:
        print("built", build_to_queue(c))
