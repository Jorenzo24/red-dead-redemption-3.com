#!/usr/bin/env python3
"""Wave 1 content -> _queue/. Run: python scripts/_wave1.py
Not deployed (scripts/ is excluded from .cpanel.yml)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_fiche import build_to_queue

def two(en, fr): return {"en": en, "fr": fr}

CHARS = [
# ============================ 1. ABIGAIL MARSTON ============================
{
 "order": 1, "slug": "abigail-marston", "name": "Abigail Marston",
 "publishDate": "2026-06-24", "schema_game": "Red Dead Redemption 2",
 "reg_role_en": "Marston family &middot; RDR1 &amp; 2", "reg_role_fr": "Famille Marston &middot; RDR1 &amp; 2",
 "gender": "Female", "death": "1914",
 "portrait_alt": two("Abigail Marston in Red Dead Redemption 2", "Abigail Marston dans Red Dead Redemption 2"),
 "eyebrow": two("Character &middot; Van der Linde gang", "Personnage &middot; Gang Van der Linde"),
 "meta_desc": two("Abigail Marston (Roberts): wife of John, mother of Jack, former Van der Linde gang member. Biography, relationships and fate.",
                  "Abigail Marston (Roberts) : épouse de John, mère de Jack, ancienne du gang Van der Linde. Biographie, relations et destin."),
 "og_desc": two("Wife of John, mother of Jack: the biography, relationships and fate of one of Red Dead's most important women.",
                "Épouse de John, mère de Jack : biographie, relations et destin de l'une des femmes les plus importantes de Red Dead."),
 "schema_desc": two("Wife of John Marston and former member of the Van der Linde gang.",
                    "Épouse de John Marston et ancienne membre du gang Van der Linde."),
 "chips": [two("Died <strong>1914</strong>", "Morte en <strong>1914</strong>"), two("Deceased", "Décédée"),
           two("Marston family", "Famille Marston"), two("Van der Linde gang", "Gang Van der Linde")],
 "facts": [
   {"label": two("Died","Mort"), "value": two("1914","1914")},
   {"label": two("Status","Statut"), "value": two("Deceased","Décédée")},
   {"label": two("Nationality","Nationalité"), "value": two("American","Américaine")},
   {"label": two("Affiliation","Affiliation"), "value": two("Van der Linde gang (former)","Gang Van der Linde (ancienne)")},
   {"label": two("Family","Famille"), "value": two("[[john-marston|John Marston]] (husband), [[jack-marston|Jack Marston]] (son)","[[john-marston|John Marston]] (époux), [[jack-marston|Jack Marston]] (fils)")},
   {"label": two("Games","Jeux"), "value": two("Red Dead Redemption, Red Dead Redemption 2","Red Dead Redemption, Red Dead Redemption 2")},
 ],
 "intro": [
   two("Abigail Marston, born Abigail Roberts, is the wife of [[john-marston|John Marston]], the mother of [[jack-marston|Jack Marston]], and one of the most important figures in the Red Dead Redemption story. A former prostitute who joined the Van der Linde gang, she gave up that life to raise a family and spends years pushing John to do the same.",
       "Abigail Marston, née Abigail Roberts, est l'épouse de [[john-marston|John Marston]], la mère de [[jack-marston|Jack Marston]] et l'une des figures les plus importantes de l'histoire de Red Dead Redemption. Ancienne prostituée ayant rejoint le gang Van der Linde, elle a quitté cette vie pour élever une famille et passe des années à pousser John à en faire autant."),
   two("Fierce, loyal and pragmatic, Abigail is the emotional anchor of the Marston family across both games. Her love for John and Jack, and her refusal to give up on either, drive much of the series' heart.",
       "Farouche, loyale et pragmatique, Abigail est l'ancrage émotionnel de la famille Marston dans les deux jeux. Son amour pour John et Jack, et son refus de renoncer à l'un comme à l'autre, portent une grande part du cœur de la série."),
 ],
 "sections": [
   {"summary": two("Biography","Biographie"), "open": True, "blocks": [
     {"h3": two("From the gang to a family","Du gang à une famille")},
     {"p": two("Abigail joined the Van der Linde gang as a young woman and, around 1895, gave birth to a son, Jack, with [[john-marston|John Marston]]. When John briefly abandoned them, it was the women of the gang and a reluctant John who eventually came back that shaped Jack's early years.",
               "Abigail a rejoint le gang Van der Linde jeune femme et, vers 1895, a eu un fils, Jack, avec [[john-marston|John Marston]]. Quand John les a brièvement abandonnés, ce sont les femmes du gang, et un John revenu à contrecœur, qui ont façonné les premières années de Jack.")},
     {"figure": {"img": "gallery-1.jpeg", "alt": two("Abigail Marston at the ranch","Abigail Marston au ranch"),
                 "cap": two("Abigail built the honest life she always wanted at Beecher's Hope.","Abigail a bâti la vie honnête qu'elle a toujours voulue à Beecher's Hope.")}},
     {"h3": two("Beecher's Hope and after","Beecher's Hope et après")},
     {"p": two("After the gang's fall, Abigail, John and Jack finally build an honest life on a ranch at Beecher's Hope. That peace is shattered in 1911 when government agents take Abigail and Jack to force John to hunt his old friends. She is widowed when John is killed, and dies a few years later, in 1914.",
               "Après la chute du gang, Abigail, John et Jack bâtissent enfin une vie honnête dans un ranch à Beecher's Hope. Cette paix vole en éclats en 1911 quand des agents du gouvernement enlèvent Abigail et Jack pour forcer John à traquer ses anciens amis. Veuve à la mort de John, elle meurt quelques années plus tard, en 1914.")},
   ]},
   {"summary": two("Personality","Personnalité"), "blocks": [
     {"p": two("Abigail is tough, sharp-tongued and deeply devoted to her family. Years in a hard world left her with no patience for self-pity, and she is often the most clear-eyed person in any room, especially about the cost of the outlaw life.",
               "Abigail est dure, à la langue bien pendue et profondément dévouée à sa famille. Des années dans un monde rude lui ont ôté toute patience pour l'apitoiement, et elle est souvent la personne la plus lucide d'une pièce, surtout sur le prix de la vie de hors-la-loi.")},
     {"p": two("Her great strength is constancy: she never stops believing John can be a better man, and never stops fighting for Jack's future.",
               "Sa grande force est la constance : elle ne cesse jamais de croire que John peut devenir meilleur, ni de se battre pour l'avenir de Jack.")},
   ]},
   {"summary": two("Death and fate","Mort et destin"), "blocks": [
     {"p": two("Abigail survives the fall of the gang and the loss of [[john-marston|John]] in 1911, only to die in 1914. Her son [[jack-marston|Jack]], now grown, buries her beside his father at Beecher's Hope before setting out to avenge them both.",
               "Abigail survit à la chute du gang et à la perte de [[john-marston|John]] en 1911, pour mourir en 1914. Son fils [[jack-marston|Jack]], désormais adulte, l'enterre auprès de son père à Beecher's Hope avant de partir les venger tous les deux.")},
   ]},
   {"summary": two("Behind the scenes","Coulisses"), "blocks": [
     {"p": two("Abigail appears in both Red Dead Redemption (2010) and Red Dead Redemption 2 (2018), one of the few characters present across the whole saga. Red Dead Redemption 2 expands her from a supporting role into a fully realised woman with her own grief, humour and resolve.",
               "Abigail apparaît dans Red Dead Redemption (2010) comme dans Red Dead Redemption 2 (2018), l'un des rares personnages présents sur toute la saga. Red Dead Redemption 2 la fait passer d'un second rôle à une femme pleinement incarnée, avec son chagrin, son humour et sa détermination.")},
   ]},
   {"summary": two("Reception and legacy","Accueil et héritage"), "blocks": [
     {"p": two("Abigail is widely seen as one of the series' strongest characters, the moral and emotional centre of the Marston family. Her insistence on a better life is, in many ways, the engine of the entire Red Dead Redemption story.",
               "Abigail est largement considérée comme l'un des personnages les plus forts de la série, le centre moral et émotionnel de la famille Marston. Son exigence d'une vie meilleure est, à bien des égards, le moteur de toute l'histoire de Red Dead Redemption.")},
   ]},
   {"summary": two("Trivia","Anecdotes"), "blocks": [
     {"ul": [
       two("Her maiden name is Roberts; she becomes Abigail Marston after marrying John.","Son nom de jeune fille est Roberts ; elle devient Abigail Marston après avoir épousé John."),
       two("She appears in both main Red Dead Redemption games.","Elle apparaît dans les deux jeux principaux Red Dead Redemption."),
       two("Her kidnapping in 1911 is what forces John into the events of the original game.","Son enlèvement en 1911 est ce qui force John à entrer dans les événements du premier jeu."),
     ]},
   ]},
 ],
 "relationships": [
   {"img": "john.jpeg", "slug": "john-marston", "name": "John Marston", "text": two(
     "Her husband and the father of her son. Abigail spends years trying to pull John out of the outlaw life and into the family he keeps almost choosing.",
     "Son époux et le père de son fils. Abigail passe des années à tenter d'arracher John à la vie de hors-la-loi pour le ramener à la famille qu'il manque sans cesse de choisir.")},
   {"img": "jack.jpeg", "slug": "jack-marston", "name": "Jack Marston", "text": two(
     "Her son, whom she fights to give a future away from guns and gangs. Everything Abigail does is, in the end, for Jack.",
     "Son fils, à qui elle se bat pour offrir un avenir loin des armes et des gangs. Tout ce que fait Abigail, c'est, au fond, pour Jack.")},
   {"img": "arthur.jpeg", "slug": "arthur-morgan", "name": "Arthur Morgan", "text": two(
     "A gang brother who helps protect her and Jack in the gang's final days, and whose sacrifice helps the Marstons escape.",
     "Un frère de gang qui aide à la protéger, elle et Jack, dans les derniers jours du gang, et dont le sacrifice permet aux Marston de s'échapper.")},
   {"img": "sadie.jpeg", "slug": "sadie-adler", "name": "Sadie Adler", "text": two(
     "A fellow survivor and friend who stands with the Marstons long after the gang is gone.",
     "Une autre survivante et amie qui se tient aux côtés des Marston bien après la fin du gang.")},
   {"img": "uncle.jpeg", "slug": None, "name": "Uncle", "text": two(
     "The work-shy old outlaw who attaches himself to the Marston household and helps run Beecher's Hope.",
     "Le vieux hors-la-loi fainéant qui s'attache au foyer Marston et aide à faire tourner Beecher's Hope.")},
 ],
 "gallery": [
   {"img": "gallery-1.jpeg", "alt": two("Abigail Marston at the ranch","Abigail Marston au ranch"),
    "cap": two("Abigail Marston at Beecher's Hope.","Abigail Marston à Beecher's Hope.")},
 ],
 "related": ["john-marston", "arthur-morgan", "sadie-adler", "dutch-van-der-linde"],
},
# ============================ 2. JACK MARSTON ============================
{
 "order": 2, "slug": "jack-marston", "name": "Jack Marston",
 "publishDate": "2026-06-25", "schema_game": "Red Dead Redemption",
 "reg_role_en": "Marston family &middot; RDR1 &amp; 2", "reg_role_fr": "Famille Marston &middot; RDR1 &amp; 2",
 "gender": "Male", "birth": "1895",
 "portrait_alt": two("Jack Marston in Red Dead Redemption 2", "Jack Marston dans Red Dead Redemption 2"),
 "eyebrow": two("Character &middot; Marston family", "Personnage &middot; Famille Marston"),
 "meta_desc": two("Jack Marston: son of John and Abigail, the final playable character of Red Dead Redemption. Biography, the 1914 revenge, relationships.",
                  "Jack Marston : fils de John et Abigail, dernier personnage jouable de Red Dead Redemption. Biographie, la vengeance de 1914, relations."),
 "og_desc": two("Son of John and Abigail and the final playable character of Red Dead Redemption: biography, the 1914 revenge and relationships.",
                "Fils de John et Abigail et dernier personnage jouable de Red Dead Redemption : biographie, la vengeance de 1914 et relations."),
 "schema_desc": two("Son of John and Abigail Marston and the final playable character of Red Dead Redemption.",
                    "Fils de John et Abigail Marston et dernier personnage jouable de Red Dead Redemption."),
 "chips": [two("Born <strong>1895</strong>", "Né en <strong>1895</strong>"), two("Survivor", "Survivant"),
           two("Marston family", "Famille Marston"), two("Playable in RDR1", "Jouable dans RDR1")],
 "facts": [
   {"label": two("Born","Naissance"), "value": two("1895","1895")},
   {"label": two("Status","Statut"), "value": two("Alive (last known)","En vie (dernières nouvelles)")},
   {"label": two("Nationality","Nationalité"), "value": two("American","Américaine")},
   {"label": two("Parents","Parents"), "value": two("[[john-marston|John Marston]], [[abigail-marston|Abigail Marston]]","[[john-marston|John Marston]], [[abigail-marston|Abigail Marston]]")},
   {"label": two("Role","Rôle"), "value": two("Final playable character of RDR1","Dernier personnage jouable de RDR1")},
   {"label": two("Games","Jeux"), "value": two("Red Dead Redemption, Red Dead Redemption 2","Red Dead Redemption, Red Dead Redemption 2")},
 ],
 "intro": [
   two("Jack Marston is the son of [[john-marston|John Marston]] and [[abigail-marston|Abigail Marston]], born around 1895 and raised inside the Van der Linde gang before his family sought an honest life. Bookish and gentle where his father was hard, Jack is the boy the whole Marston tragedy is meant to protect.",
       "Jack Marston est le fils de [[john-marston|John Marston]] et [[abigail-marston|Abigail Marston]], né vers 1895 et élevé au sein du gang Van der Linde avant que sa famille ne cherche une vie honnête. Porté sur les livres et doux là où son père était dur, Jack est l'enfant que toute la tragédie des Marston cherche à protéger."),
   two("After losing both parents, Jack becomes the final playable character of Red Dead Redemption, and in 1914 closes the saga's long cycle of revenge.",
       "Après avoir perdu ses deux parents, Jack devient le dernier personnage jouable de Red Dead Redemption et, en 1914, referme le long cycle de vengeance de la saga."),
 ],
 "sections": [
   {"summary": two("Biography","Biographie"), "open": True, "blocks": [
     {"h3": two("A child of the gang","Un enfant du gang")},
     {"p": two("Jack grew up among the outlaws of the Van der Linde gang, doted on by the camp and especially close to his mother. Unlike the gunmen around him, he loved reading and dreamed of a quieter life, a sensibility his father [[john-marston|John]] never quite understood but fought to give him.",
               "Jack a grandi parmi les hors-la-loi du gang Van der Linde, choyé par le camp et particulièrement proche de sa mère. Contrairement aux tireurs qui l'entouraient, il aimait lire et rêvait d'une vie plus paisible, une sensibilité que son père [[john-marston|John]] n'a jamais vraiment comprise mais s'est battu pour lui offrir.")},
     {"figure": {"img": "gallery-1.jpeg", "alt": two("Jack Marston in Red Dead Redemption 2","Jack Marston dans Red Dead Redemption 2"),
                 "cap": two("Jack Marston, the future of a family of outlaws.","Jack Marston, l'avenir d'une famille de hors-la-loi.")}},
     {"h3": two("Revenge, 1914","La vengeance, 1914")},
     {"p": two("After his father is killed in 1911 and his mother dies in 1914, a grown Jack takes up the gun he never wanted. He tracks down Edgar Ross, the former agent who destroyed his family, and kills him on a riverbank, ending Red Dead Redemption as its last playable character.",
               "Après la mort de son père en 1911 et celle de sa mère en 1914, un Jack devenu adulte reprend l'arme qu'il n'a jamais voulue. Il retrouve Edgar Ross, l'ancien agent qui a détruit sa famille, et le tue au bord d'une rivière, terminant Red Dead Redemption comme son dernier personnage jouable.")},
   ]},
   {"summary": two("Personality","Personnalité"), "blocks": [
     {"p": two("As a boy, Jack is sensitive, curious and bookish, the gentlest soul in a family of hard people. The tragedy of his arc is watching that gentleness give way to the same violence that defined his father.",
               "Enfant, Jack est sensible, curieux et porté sur les livres, l'âme la plus douce d'une famille de durs. La tragédie de son arc est de voir cette douceur céder à la même violence qui a défini son père.")},
   ]},
   {"summary": two("Fate and legacy","Destin et héritage"), "blocks": [
     {"p": two("Jack survives the saga, but at a cost: by avenging his parents he becomes the very thing they died trying to keep him from. His story closes the original Red Dead Redemption and asks whether the cycle of violence can ever truly end.",
               "Jack survit à la saga, mais à un prix : en vengeant ses parents, il devient ce qu'ils sont morts en essayant de lui épargner. Son histoire clôt le premier Red Dead Redemption et demande si le cycle de la violence peut vraiment prendre fin un jour.")},
   ]},
   {"summary": two("Behind the scenes","Coulisses"), "blocks": [
     {"p": two("Jack appears as a child in Red Dead Redemption 2 and as the final playable adult protagonist in Red Dead Redemption. Letting players end the original game in his shoes was a bold, melancholy choice that has stayed with fans ever since.",
               "Jack apparaît enfant dans Red Dead Redemption 2 et en protagoniste adulte jouable à la toute fin de Red Dead Redemption. Laisser les joueurs terminer le jeu d'origine dans sa peau fut un choix audacieux et mélancolique qui a marqué les fans depuis.")},
   ]},
   {"summary": two("Reception and legacy","Accueil et héritage"), "blocks": [
     {"p": two("Jack divides players: some resent leaving Arthur and John behind for him, others find his grim transformation the perfect, tragic full stop to the saga. Either way, he embodies its central question about violence and inheritance.",
               "Jack divise les joueurs : certains regrettent de quitter Arthur et John pour lui, d'autres trouvent sa sombre transformation comme le point final, tragique et parfait, de la saga. Quoi qu'il en soit, il incarne sa question centrale sur la violence et l'héritage.")},
   ]},
   {"summary": two("Trivia","Anecdotes"), "blocks": [
     {"ul": [
       two("Jack is the final playable character of the original Red Dead Redemption.","Jack est le dernier personnage jouable du premier Red Dead Redemption."),
       two("He is far more interested in books than in guns as a child.","Enfant, il s'intéresse bien plus aux livres qu'aux armes."),
       two("He kills Edgar Ross in 1914 to avenge his father.","Il tue Edgar Ross en 1914 pour venger son père."),
     ]},
   ]},
 ],
 "relationships": [
   {"img": "john.jpeg", "slug": "john-marston", "name": "John Marston", "text": two(
     "His father, who dies in 1911 trying to give Jack the honest life he never had. Jack later avenges him.",
     "Son père, qui meurt en 1911 en tentant d'offrir à Jack la vie honnête qu'il n'a jamais eue. Jack le vengera.")},
   {"img": "abigail.jpeg", "slug": "abigail-marston", "name": "Abigail Marston", "text": two(
     "His mother and fiercest protector, who dies in 1914. Her death sets Jack on the path of revenge.",
     "Sa mère et sa plus farouche protectrice, qui meurt en 1914. Sa mort lance Jack sur le chemin de la vengeance.")},
   {"img": "arthur.jpeg", "slug": "arthur-morgan", "name": "Arthur Morgan", "text": two(
     "A gang elder who helped protect Jack as a boy, part of the family that bought the Marstons their chance at freedom.",
     "Un aîné du gang qui a aidé à protéger Jack enfant, membre de la famille qui a offert aux Marston leur chance de liberté.")},
   {"img": "uncle.jpeg", "slug": None, "name": "Uncle", "text": two(
     "The old outlaw who lives with the Marstons and is, in his lazy way, a kind of grandfather figure to Jack.",
     "Le vieux hors-la-loi qui vit avec les Marston et fait, à sa manière paresseuse, office de grand-père pour Jack.")},
   {"img": "ross.jpeg", "slug": None, "name": "Edgar Ross", "text": two(
     "The agent who destroyed the Marston family. In 1914, Jack hunts him down and kills him.",
     "L'agent qui a détruit la famille Marston. En 1914, Jack le traque et le tue.")},
 ],
 "gallery": [
   {"img": "gallery-1.jpeg", "alt": two("Jack Marston in Red Dead Redemption 2","Jack Marston dans Red Dead Redemption 2"),
    "cap": two("Jack Marston.","Jack Marston.")},
 ],
 "related": ["john-marston", "abigail-marston", "arthur-morgan", "sadie-adler"],
},
# ============================ 3. SEAN MACGUIRE ============================
{
 "order": 3, "slug": "sean-macguire", "name": "Sean MacGuire",
 "publishDate": "2026-06-26", "schema_game": "Red Dead Redemption 2",
 "reg_role_en": "Van der Linde gang &middot; RDR2", "reg_role_fr": "Gang Van der Linde &middot; RDR2",
 "gender": "Male", "death": "1899",
 "portrait_alt": two("Sean MacGuire in Red Dead Redemption 2", "Sean MacGuire dans Red Dead Redemption 2"),
 "eyebrow": two("Character &middot; Van der Linde gang", "Personnage &middot; Gang Van der Linde"),
 "meta_desc": two("Sean MacGuire: the brash young Irishman of the Van der Linde gang. Biography, his shocking 1899 death, relationships and legacy.",
                  "Sean MacGuire : le jeune Irlandais effronté du gang Van der Linde. Biographie, sa mort brutale en 1899, relations et héritage."),
 "og_desc": two("The brash young Irishman of the Van der Linde gang: biography, his shocking 1899 death and relationships.",
                "Le jeune Irlandais effronté du gang Van der Linde : biographie, sa mort brutale en 1899 et relations."),
 "schema_desc": two("Young Irish gunman of the Van der Linde gang in Red Dead Redemption 2.",
                    "Jeune tireur irlandais du gang Van der Linde dans Red Dead Redemption 2."),
 "chips": [two("Died <strong>1899</strong>", "Mort en <strong>1899</strong>"), two("Deceased", "Décédé"),
           two("Van der Linde gang", "Gang Van der Linde"), two("Irish gunman", "Tireur irlandais")],
 "facts": [
   {"label": two("Died","Mort"), "value": two("1899","1899")},
   {"label": two("Status","Statut"), "value": two("Deceased","Décédé")},
   {"label": two("Origin","Origine"), "value": two("Irish","Irlandaise")},
   {"label": two("Affiliation","Affiliation"), "value": two("Van der Linde gang","Gang Van der Linde")},
   {"label": two("Role","Rôle"), "value": two("Young gunman","Jeune tireur")},
   {"label": two("Games","Jeux"), "value": two("Red Dead Redemption 2","Red Dead Redemption 2")},
 ],
 "intro": [
   two("Sean MacGuire is the loud, cocky young Irishman of the Van der Linde gang in Red Dead Redemption 2, the son of an Irish revolutionary and the camp's most reliable source of bravado and bad jokes. Beneath the swagger is a fierce loyalty to the only family he has.",
       "Sean MacGuire est le jeune Irlandais bruyant et fanfaron du gang Van der Linde dans Red Dead Redemption 2, fils d'un révolutionnaire irlandais et meilleure source de bravade et de mauvaises blagues du camp. Sous l'arrogance se cache une loyauté farouche envers la seule famille qu'il ait."),
   two("Captured early in the story and rescued by the gang, Sean's joy at being home is cut brutally short, making him one of the game's most sudden and memorable losses.",
       "Capturé tôt dans l'histoire puis sauvé par le gang, le bonheur de Sean d'être de retour est brutalement écourté, ce qui en fait l'une des pertes les plus soudaines et marquantes du jeu."),
 ],
 "sections": [
   {"summary": two("Biography","Biographie"), "open": True, "blocks": [
     {"h3": two("The gang's loudest son","Le fils le plus bruyant du gang")},
     {"p": two("Sean is young, brash and endlessly talkative, forever boasting and picking fun. Early in 1899 he is captured by bounty hunters, and a major mission sees [[arthur-morgan|Arthur]] and the gang rescue him, a reunion the whole camp celebrates.",
               "Sean est jeune, effronté et intarissable, toujours à se vanter et à charrier. Au début de 1899, il est capturé par des chasseurs de primes, et une mission importante voit [[arthur-morgan|Arthur]] et le gang le secourir, des retrouvailles que tout le camp célèbre.")},
     {"figure": {"img": "gallery-1.jpeg", "alt": two("Sean MacGuire in Red Dead Redemption 2","Sean MacGuire dans Red Dead Redemption 2"),
                 "cap": two("Sean MacGuire, all bravado and bad jokes.","Sean MacGuire, tout en bravade et mauvaises blagues.")}},
   ]},
   {"summary": two("Personality","Personnalité"), "blocks": [
     {"p": two("Sean hides his insecurity behind nonstop talk and swagger. He wants desperately to be taken seriously as a gunman, and for all his noise he is brave and loyal when it counts.",
               "Sean cache son manque d'assurance derrière un bavardage et une arrogance sans fin. Il veut désespérément être pris au sérieux comme tireur et, malgré tout son tapage, il est courageux et loyal quand ça compte.")},
   ]},
   {"summary": two("Death and fate","Mort et destin"), "blocks": [
     {"p": two("Not long after his rescue, during a deal in the town of Rhodes, Sean is shot in the head mid-sentence by an ambushing bounty hunter. His sudden death stuns the gang and is one of the first signs that their world is collapsing.",
               "Peu après son sauvetage, lors d'une transaction dans la ville de Rhodes, Sean est abattu d'une balle dans la tête en pleine phrase par un chasseur de primes embusqué. Sa mort soudaine sidère le gang et constitue l'un des premiers signes que leur monde s'effondre.")},
   ]},
   {"summary": two("Behind the scenes","Coulisses"), "blocks": [
     {"p": two("Sean's death is deliberately abrupt and without ceremony, the game using his loss to puncture the camp's early optimism. It is often cited as one of Red Dead Redemption 2's most shocking moments.",
               "La mort de Sean est délibérément abrupte et sans cérémonie, le jeu utilisant sa perte pour crever l'optimisme initial du camp. Elle est souvent citée parmi les moments les plus choquants de Red Dead Redemption 2.")},
   ]},
   {"summary": two("Reception and legacy","Accueil et héritage"), "blocks": [
     {"p": two("Despite limited screen time, Sean is a fan favourite, remembered for his humour and the gut-punch of his exit. He is proof of how quickly Red Dead Redemption 2 can make players care, and then grieve.",
               "Malgré un temps d'écran limité, Sean est un favori des fans, retenu pour son humour et le coup au ventre de sa sortie. Il prouve à quelle vitesse Red Dead Redemption 2 sait faire s'attacher les joueurs, puis les endeuiller.")},
   ]},
   {"summary": two("Trivia","Anecdotes"), "blocks": [
     {"ul": [
       two("Sean is the son of an Irish revolutionary and often invokes his father.","Sean est le fils d'un révolutionnaire irlandais et invoque souvent son père."),
       two("A whole mission is devoted to rescuing him from bounty hunters.","Une mission entière est consacrée à le sauver des chasseurs de primes."),
       two("His death comes mid-sentence, with no warning.","Sa mort survient en pleine phrase, sans aucun avertissement."),
     ]},
   ]},
 ],
 "relationships": [
   {"img": "arthur.jpeg", "slug": "arthur-morgan", "name": "Arthur Morgan", "text": two(
     "The gang enforcer who leads the mission to rescue Sean and is present for his sudden death.",
     "L'homme de main du gang qui mène la mission pour sauver Sean et assiste à sa mort soudaine.")},
   {"img": "hosea.jpeg", "slug": "hosea-matthews", "name": "Hosea Matthews", "text": two(
     "A gang elder and planner whose schemes Sean is eager to be part of.",
     "Un aîné et planificateur du gang dont Sean est avide de faire partie des combines.")},
   {"img": "lenny.jpeg", "slug": None, "name": "Lenny Summers", "text": two(
     "A fellow young gang member and one of Sean's closest friends in camp.",
     "Un autre jeune membre du gang et l'un des plus proches amis de Sean au camp.")},
   {"img": "dutch.jpeg", "slug": "dutch-van-der-linde", "name": "Dutch van der Linde", "text": two(
     "The leader Sean is desperate to impress and prove himself to.",
     "Le chef que Sean est désespéré d'impressionner et auprès de qui il veut faire ses preuves.")},
   {"img": "john.jpeg", "slug": "john-marston", "name": "John Marston", "text": two(
     "A fellow gunman in the 1899 gang, part of the family that mourns Sean's loss.",
     "Un autre tireur du gang de 1899, membre de la famille qui pleure la perte de Sean.")},
 ],
 "gallery": [
   {"img": "gallery-1.jpeg", "alt": two("Sean MacGuire in Red Dead Redemption 2","Sean MacGuire dans Red Dead Redemption 2"),
    "cap": two("Sean MacGuire.","Sean MacGuire.")},
 ],
 "related": ["arthur-morgan", "hosea-matthews", "dutch-van-der-linde", "john-marston"],
},
# ============================ 4. LENNY SUMMERS ============================
{
 "order": 4, "slug": "lenny-summers", "name": "Lenny Summers",
 "publishDate": "2026-06-27", "schema_game": "Red Dead Redemption 2",
 "reg_role_en": "Van der Linde gang &middot; RDR2", "reg_role_fr": "Gang Van der Linde &middot; RDR2",
 "gender": "Male", "death": "1899",
 "portrait_alt": two("Lenny Summers in Red Dead Redemption 2", "Lenny Summers dans Red Dead Redemption 2"),
 "eyebrow": two("Character &middot; Van der Linde gang", "Personnage &middot; Gang Van der Linde"),
 "meta_desc": two("Lenny Summers: the sharp, level-headed young gunman of the Van der Linde gang. Biography, his 1899 death, relationships and legacy.",
                  "Lenny Summers : le jeune tireur vif et posé du gang Van der Linde. Biographie, sa mort en 1899, relations et héritage."),
 "og_desc": two("The sharp, level-headed young gunman of the Van der Linde gang: biography, his 1899 death and relationships.",
                "Le jeune tireur vif et posé du gang Van der Linde : biographie, sa mort en 1899 et relations."),
 "schema_desc": two("Young, educated gunman of the Van der Linde gang in Red Dead Redemption 2.",
                    "Jeune tireur instruit du gang Van der Linde dans Red Dead Redemption 2."),
 "chips": [two("Died <strong>1899</strong>", "Mort en <strong>1899</strong>"), two("Deceased", "Décédé"),
           two("Van der Linde gang", "Gang Van der Linde"), two("Young gunman", "Jeune tireur")],
 "facts": [
   {"label": two("Died","Mort"), "value": two("1899","1899")},
   {"label": two("Status","Statut"), "value": two("Deceased","Décédé")},
   {"label": two("Nationality","Nationalité"), "value": two("American","Américaine")},
   {"label": two("Affiliation","Affiliation"), "value": two("Van der Linde gang","Gang Van der Linde")},
   {"label": two("Role","Rôle"), "value": two("Young gunman","Jeune tireur")},
   {"label": two("Games","Jeux"), "value": two("Red Dead Redemption 2","Red Dead Redemption 2")},
 ],
 "intro": [
   two("Lenny Summers is one of the youngest and most likeable members of the Van der Linde gang in Red Dead Redemption 2: sharp, educated and level-headed, the son of a man who had escaped slavery. He is among [[arthur-morgan|Arthur Morgan]]'s most trusted and easy companions.",
       "Lenny Summers est l'un des membres les plus jeunes et les plus attachants du gang Van der Linde dans Red Dead Redemption 2 : vif, instruit et posé, fils d'un homme qui avait fui l'esclavage. Il fait partie des compagnons les plus fiables et les plus faciles d'[[arthur-morgan|Arthur Morgan]]."),
   two("Brave and genuinely competent in a fight, Lenny is the gang's promise of a better future, which makes his death one of the story's cruellest blows.",
       "Courageux et réellement compétent au combat, Lenny est la promesse d'un avenir meilleur pour le gang, ce qui fait de sa mort l'un des coups les plus cruels de l'histoire."),
 ],
 "sections": [
   {"summary": two("Biography","Biographie"), "open": True, "blocks": [
     {"h3": two("The gang's bright young hope","Le jeune espoir du gang")},
     {"p": two("Lenny is clever, well-read and quick on his feet, a stark contrast to the gang's blunter gunmen. He shares one of Red Dead Redemption 2's most beloved scenes with [[arthur-morgan|Arthur]]: a riotous drunken night in a Valentine saloon.",
               "Lenny est intelligent, cultivé et vif d'esprit, en net contraste avec les tireurs plus frustes du gang. Il partage avec [[arthur-morgan|Arthur]] l'une des scènes les plus aimées de Red Dead Redemption 2 : une soirée d'ivresse mémorable dans un saloon de Valentine.")},
     {"figure": {"img": "gallery-1.jpeg", "alt": two("Lenny Summers with Arthur Morgan","Lenny Summers avec Arthur Morgan"),
                 "cap": two("Lenny and Arthur shared one of the game's most beloved scenes.","Lenny et Arthur partagent l'une des scènes les plus aimées du jeu.")}},
   ]},
   {"summary": two("Personality","Personnalité"), "blocks": [
     {"p": two("Thoughtful, principled and brave, Lenny is wise beyond his years. He is acutely aware of the dangers he faces as a young Black man on the frontier, and carries himself with a quiet dignity the gang respects.",
               "Réfléchi, intègre et courageux, Lenny est sage pour son âge. Il a une conscience aiguë des dangers qu'il affronte en tant que jeune homme noir sur la frontière, et se tient avec une dignité tranquille que le gang respecte.")},
   ]},
   {"summary": two("Death and fate","Mort et destin"), "blocks": [
     {"p": two("Lenny is killed during the gang's disastrous bank robbery in Saint Denis, shot down by lawmen as the heist falls apart, the same catastrophe that claims [[hosea-matthews|Hosea Matthews]]. He is buried beside Hosea, the gang's bright future cut down alongside its wise old heart.",
               "Lenny est tué lors du braquage désastreux de la banque de Saint Denis, abattu par les forces de l'ordre tandis que le casse vire au chaos, la même catastrophe qui emporte [[hosea-matthews|Hosea Matthews]]. Il est enterré auprès d'Hosea, le bel avenir du gang fauché aux côtés de son vieux cœur sage.")},
   ]},
   {"summary": two("Behind the scenes","Coulisses"), "blocks": [
     {"p": two("Losing Lenny and Hosea in the same sequence is a deliberate gut-punch: the gang loses its conscience and its future at once. Many players rank the Saint Denis robbery among the story's darkest turning points.",
               "Perdre Lenny et Hosea dans la même séquence est un coup au ventre délibéré : le gang perd à la fois sa conscience et son avenir. Beaucoup de joueurs classent le braquage de Saint Denis parmi les tournants les plus sombres de l'histoire.")},
   ]},
   {"summary": two("Reception and legacy","Accueil et héritage"), "blocks": [
     {"p": two("Lenny is one of the most universally liked characters in Red Dead Redemption 2, and his death is among the most mourned. He represents the kinder, smarter world the gang might have built and never will.",
               "Lenny est l'un des personnages les plus unanimement appréciés de Red Dead Redemption 2, et sa mort l'une des plus pleurées. Il représente le monde plus doux et plus intelligent que le gang aurait pu bâtir et ne bâtira jamais.")},
   ]},
   {"summary": two("Trivia","Anecdotes"), "blocks": [
     {"ul": [
       two("His drunken night out with Arthur in Valentine is a fan-favourite scene.","Sa soirée d'ivresse avec Arthur à Valentine est une scène culte des fans."),
       two("He is the son of a man who escaped slavery.","Il est le fils d'un homme qui a fui l'esclavage."),
       two("He is buried next to Hosea Matthews.","Il est enterré à côté d'Hosea Matthews."),
     ]},
   ]},
 ],
 "relationships": [
   {"img": "arthur.jpeg", "slug": "arthur-morgan", "name": "Arthur Morgan", "text": two(
     "His closest friend among the gang's elders; their drunken night in Valentine is one of the game's warmest moments.",
     "Son plus proche ami parmi les aînés du gang ; leur soirée d'ivresse à Valentine est l'un des moments les plus chaleureux du jeu.")},
   {"img": "hosea.jpeg", "slug": "hosea-matthews", "name": "Hosea Matthews", "text": two(
     "A mentor figure who dies in the same Saint Denis catastrophe; the two are buried side by side.",
     "Une figure de mentor qui meurt dans la même catastrophe de Saint Denis ; les deux sont enterrés côte à côte.")},
   {"img": "dutch.jpeg", "slug": "dutch-van-der-linde", "name": "Dutch van der Linde", "text": two(
     "The leader Lenny follows loyally, part of the gang Dutch's choices ultimately doom.",
     "Le chef que Lenny suit loyalement, membre du gang que les choix de Dutch finissent par condamner.")},
   {"img": "sean.jpeg", "slug": "sean-macguire", "name": "Sean MacGuire", "text": two(
     "A fellow young gang member and friend; the two represent the gang's next generation.",
     "Un autre jeune membre du gang et ami ; les deux incarnent la génération suivante du gang.")},
   {"img": "micah.jpeg", "slug": "micah-bell", "name": "Micah Bell", "text": two(
     "A gang newcomer Lenny has little reason to trust, part of the toxic turn the camp takes.",
     "Un nouveau venu du gang à qui Lenny a peu de raisons de se fier, symptôme du tournant toxique que prend le camp.")},
 ],
 "gallery": [
   {"img": "gallery-1.jpeg", "alt": two("Lenny Summers and Arthur Morgan","Lenny Summers et Arthur Morgan"),
    "cap": two("Lenny Summers.","Lenny Summers.")},
 ],
 "related": ["arthur-morgan", "hosea-matthews", "dutch-van-der-linde", "john-marston"],
},
# ============================ 5. JAVIER ESCUELLA ============================
{
 "order": 5, "slug": "javier-escuella", "name": "Javier Escuella",
 "publishDate": "2026-06-28", "schema_game": "Red Dead Redemption 2",
 "reg_role_en": "Van der Linde gang &middot; RDR1 &amp; 2", "reg_role_fr": "Gang Van der Linde &middot; RDR1 &amp; 2",
 "gender": "Male", "death": "1911",
 "portrait_alt": two("Javier Escuella in Red Dead Redemption 2", "Javier Escuella dans Red Dead Redemption 2"),
 "eyebrow": two("Character &middot; Van der Linde gang", "Personnage &middot; Gang Van der Linde"),
 "meta_desc": two("Javier Escuella: the loyal Mexican gunman of the Van der Linde gang and a Red Dead Redemption target. Biography, his 1911 fate, relationships.",
                  "Javier Escuella : le fidèle tireur mexicain du gang Van der Linde et une cible de Red Dead Redemption. Biographie, son destin en 1911, relations."),
 "og_desc": two("The loyal Mexican gunman of the Van der Linde gang and a Red Dead Redemption target: biography, his 1911 fate and relationships.",
                "Le fidèle tireur mexicain du gang Van der Linde et une cible de Red Dead Redemption : biographie, son destin en 1911 et relations."),
 "schema_desc": two("Mexican gunman of the Van der Linde gang and an antagonist of Red Dead Redemption.",
                    "Tireur mexicain du gang Van der Linde et antagoniste de Red Dead Redemption."),
 "chips": [two("Died <strong>1911</strong>", "Mort en <strong>1911</strong>"), two("Deceased", "Décédé"),
           two("Van der Linde gang", "Gang Van der Linde"), two("Mexican gunman", "Tireur mexicain")],
 "facts": [
   {"label": two("Died","Mort"), "value": two("1911","1911")},
   {"label": two("Status","Statut"), "value": two("Deceased","Décédé")},
   {"label": two("Origin","Origine"), "value": two("Mexican","Mexicaine")},
   {"label": two("Affiliation","Affiliation"), "value": two("Van der Linde gang","Gang Van der Linde")},
   {"label": two("Role","Rôle"), "value": two("Gunman","Tireur")},
   {"label": two("Games","Jeux"), "value": two("Red Dead Redemption, Red Dead Redemption 2","Red Dead Redemption, Red Dead Redemption 2")},
 ],
 "intro": [
   two("Javier Escuella is a loyal, talented Mexican gunman of the Van der Linde gang and, years later, one of the outlaws a coerced [[john-marston|John Marston]] must hunt in the original Red Dead Redemption. A fugitive from Mexico who found a home with [[dutch-van-der-linde|Dutch]], Javier prizes loyalty above almost everything.",
       "Javier Escuella est un fidèle et talentueux tireur mexicain du gang Van der Linde et, des années plus tard, l'un des hors-la-loi qu'un [[john-marston|John Marston]] sous contrainte doit traquer dans le premier Red Dead Redemption. Fugitif du Mexique ayant trouvé un foyer auprès de [[dutch-van-der-linde|Dutch]], Javier place la loyauté au-dessus de presque tout."),
   two("In Red Dead Redemption 2 he stands among Dutch's most devoted followers; by 1911 that loyalty has carried him back to Mexico and into John's sights.",
       "Dans Red Dead Redemption 2, il compte parmi les plus dévoués des fidèles de Dutch ; en 1911, cette loyauté l'a ramené au Mexique et placé dans le viseur de John."),
 ],
 "sections": [
   {"summary": two("Biography","Biographie"), "open": True, "blocks": [
     {"h3": two("A fugitive finds a family","Un fugitif trouve une famille")},
     {"p": two("Javier fled Mexico after turning on a corrupt official, and found belonging in the Van der Linde gang, where his skill with a gun and his loyalty quickly made him valued. He is a true believer in [[dutch-van-der-linde|Dutch]]'s vision of freedom.",
               "Javier a fui le Mexique après s'être retourné contre un officiel corrompu, et a trouvé sa place dans le gang Van der Linde, où son habileté au tir et sa loyauté l'ont vite rendu précieux. Il croit sincèrement à la vision de liberté de [[dutch-van-der-linde|Dutch]].")},
     {"figure": {"img": "gallery-1.jpeg", "alt": two("Javier Escuella in Red Dead Redemption 2","Javier Escuella dans Red Dead Redemption 2"),
                 "cap": two("Javier Escuella, loyal to Dutch to the very end.","Javier Escuella, fidèle à Dutch jusqu'au bout.")}},
     {"h3": two("Back to Mexico, 1911","Retour au Mexique, 1911")},
     {"p": two("When the gang falls, Javier stays loyal to Dutch and eventually returns to Mexico. There, in 1911, [[john-marston|John Marston]], forced by government agents, tracks down his former gang brother, and Javier's long run finally ends.",
               "Quand le gang s'effondre, Javier reste fidèle à Dutch et finit par regagner le Mexique. Là, en 1911, [[john-marston|John Marston]], contraint par des agents du gouvernement, retrouve son ancien frère de gang, et la longue cavale de Javier prend fin.")},
   ]},
   {"summary": two("Personality","Personnalité"), "blocks": [
     {"p": two("Javier is proud, passionate and intensely loyal, a romantic who loves music as much as he respects a good gun. That same loyalty becomes his weakness: he follows Dutch even as Dutch loses his way.",
               "Javier est fier, passionné et intensément loyal, un romantique qui aime la musique autant qu'il respecte une bonne arme. Cette loyauté devient sa faiblesse : il suit Dutch alors même que Dutch s'égare.")},
   ]},
   {"summary": two("Death and fate","Mort et destin"), "blocks": [
     {"p": two("By 1911, Javier is hiding in the Mexican territory of Nuevo Paraíso, like [[bill-williamson|Bill Williamson]] before him. John Marston, sent to bring in his old associates, catches up with him there, and Javier's story ends far from the gang that gave him a home.",
               "En 1911, Javier se cache dans le territoire mexicain de Nuevo Paraíso, comme [[bill-williamson|Bill Williamson]] avant lui. John Marston, envoyé livrer ses anciens compagnons, le rattrape là-bas, et l'histoire de Javier s'achève loin du gang qui lui avait offert un foyer.")},
   ]},
   {"summary": two("Behind the scenes","Coulisses"), "blocks": [
     {"p": two("Like [[bill-williamson|Bill]] and [[dutch-van-der-linde|Dutch]], Javier bridges both games: an antagonist in the 2010 original whose younger, fuller self is revealed in the 2018 prequel. Red Dead Redemption 2 turns a henchman into a sympathetic, tragic figure.",
               "Comme [[bill-williamson|Bill]] et [[dutch-van-der-linde|Dutch]], Javier relie les deux jeux : antagoniste dans l'original de 2010 dont le moi plus jeune et plus complet est révélé dans le préquel de 2018. Red Dead Redemption 2 transforme un homme de main en une figure attachante et tragique.")},
   ]},
   {"summary": two("Reception and legacy","Accueil et héritage"), "blocks": [
     {"p": two("Javier is a memorable example of the series' bridging of its two eras, his loyalty making his eventual fate genuinely sad. Fans value him as one of the gang members whose RDR2 portrayal recoloured the original game.",
               "Javier est un exemple marquant du pont entre les deux époques de la série, sa loyauté rendant son destin véritablement triste. Les fans l'apprécient comme l'un des membres du gang dont le portrait dans RDR2 a recoloré le jeu d'origine.")},
   ]},
   {"summary": two("Trivia","Anecdotes"), "blocks": [
     {"ul": [
       two("Javier appears in both Red Dead Redemption and Red Dead Redemption 2.","Javier apparaît dans Red Dead Redemption et Red Dead Redemption 2."),
       two("He fled Mexico after turning against a corrupt official.","Il a fui le Mexique après s'être retourné contre un officiel corrompu."),
       two("He loves music and is often associated with the guitar.","Il aime la musique et est souvent associé à la guitare."),
     ]},
   ]},
 ],
 "relationships": [
   {"img": "dutch.jpeg", "slug": "dutch-van-der-linde", "name": "Dutch van der Linde", "text": two(
     "The leader Javier follows with near-total devotion, staying loyal long after others have run.",
     "Le chef que Javier suit avec une dévotion presque totale, restant fidèle bien après que d'autres ont fui.")},
   {"img": "john.jpeg", "slug": "john-marston", "name": "John Marston", "text": two(
     "A former gang brother who, in 1911, is forced to hunt Javier down in Mexico.",
     "Un ancien frère de gang qui, en 1911, est forcé de traquer Javier au Mexique.")},
   {"img": "bill.jpeg", "slug": "bill-williamson", "name": "Bill Williamson", "text": two(
     "A fellow loyalist and another of John's Mexican targets; the two outlaws share a similar fate.",
     "Un autre fidèle et une autre cible mexicaine de John ; les deux hors-la-loi partagent un destin semblable.")},
   {"img": "arthur.jpeg", "slug": "arthur-morgan", "name": "Arthur Morgan", "text": two(
     "A fellow gunman in the 1899 gang, working alongside Javier through its final year.",
     "Un autre tireur du gang de 1899, travaillant aux côtés de Javier durant sa dernière année.")},
   {"img": "micah.jpeg", "slug": "micah-bell", "name": "Micah Bell", "text": two(
     "A late arrival Javier ends up siding with among Dutch's loyalists as the gang splinters.",
     "Un venu tardif dont Javier finit par prendre le parti parmi les fidèles de Dutch tandis que le gang se fracture.")},
 ],
 "gallery": [
   {"img": "gallery-1.jpeg", "alt": two("Javier Escuella in Red Dead Redemption 2","Javier Escuella dans Red Dead Redemption 2"),
    "cap": two("Javier Escuella.","Javier Escuella.")},
 ],
 "related": ["dutch-van-der-linde", "john-marston", "bill-williamson", "arthur-morgan"],
},
]

if __name__ == "__main__":
    for c in CHARS:
        print("queued:", build_to_queue(c))
