#!/usr/bin/env python3
"""Wave 2 content -> _queue/. Run: python scripts/_wave2.py
Not deployed (scripts/ is excluded from .cpanel.yml).

Six fiches: Kieran Duffy, Mary Linton, Leopold Strauss, Susan Grimshaw,
Colm O'Driscoll, Edgar Ross. Factual register (no mood-prose); see the
no-AI-poetry rule. Images already staged in assets/characters/<slug>/.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_fiche import build_to_queue

def two(en, fr): return {"en": en, "fr": fr}

CHARS = [
# ============================ 6. KIERAN DUFFY ============================
{
 "order": 6, "slug": "kieran-duffy", "name": "Kieran Duffy",
 "publishDate": "2026-07-01", "schema_game": "Red Dead Redemption 2",
 "reg_role_en": "Van der Linde gang &middot; RDR2", "reg_role_fr": "Gang Van der Linde &middot; RDR2",
 "gender": "Male", "death": "1899",
 "portrait_alt": two("Kieran Duffy in Red Dead Redemption 2", "Kieran Duffy dans Red Dead Redemption 2"),
 "eyebrow": two("Character &middot; Van der Linde gang", "Personnage &middot; Gang Van der Linde"),
 "meta_desc": two("Kieran Duffy: the captured O'Driscoll who becomes the Van der Linde gang's stable hand in Red Dead Redemption 2. Biography, relationships and death.",
                  "Kieran Duffy : l'O'Driscoll capturé qui devient le palefrenier du gang Van der Linde dans Red Dead Redemption 2. Biographie, relations et mort."),
 "og_desc": two("The captured O'Driscoll who earns a place in the Van der Linde gang: biography, relationships and brutal end.",
                "L'O'Driscoll capturé qui gagne sa place dans le gang Van der Linde : biographie, relations et fin brutale."),
 "schema_desc": two("Former O'Driscoll Boy captured by and absorbed into the Van der Linde gang.",
                    "Ancien O'Driscoll capturé puis intégré au gang Van der Linde."),
 "chips": [two("Died <strong>1899</strong>", "Mort en <strong>1899</strong>"), two("Deceased", "Décédé"),
           two("Van der Linde gang", "Gang Van der Linde"), two("Former O'Driscoll", "Ancien O'Driscoll")],
 "facts": [
   {"label": two("Died","Mort"), "value": two("1899","1899")},
   {"label": two("Status","Statut"), "value": two("Deceased","Décédé")},
   {"label": two("Nationality","Nationalité"), "value": two("American","Américaine")},
   {"label": two("Affiliation","Affiliation"), "value": two("O'Driscoll Boys (former), Van der Linde gang","Gang O'Driscoll (ancien), gang Van der Linde")},
   {"label": two("Role","Rôle"), "value": two("Stable hand","Palefrenier")},
   {"label": two("Games","Jeux"), "value": two("Red Dead Redemption 2","Red Dead Redemption 2")},
 ],
 "intro": [
   two("Kieran Duffy is a former member of the O'Driscoll Boys who is captured by the Van der Linde gang and slowly becomes one of their own. Timid and eager to please, he is less an outlaw than a frightened young man trying to survive between two gangs that have spent years killing each other.",
       "Kieran Duffy est un ancien membre du gang O'Driscoll, capturé par le gang Van der Linde, dont il finit par faire partie. Timide et soucieux de bien faire, il est moins un hors-la-loi qu'un jeune homme apeuré qui tente de survivre entre deux gangs qui s'entretuent depuis des années."),
   two("Caught by [[arthur-morgan|Arthur Morgan]] in the mountains around Colter, Kieran spends much of Red Dead Redemption 2 earning the gang's trust as their stable hand before meeting a brutal end.",
       "Capturé par [[arthur-morgan|Arthur Morgan]] dans les montagnes de Colter, Kieran passe une grande partie de Red Dead Redemption 2 à gagner la confiance du gang comme palefrenier, avant une fin brutale."),
 ],
 "sections": [
   {"summary": two("Biography","Biographie"), "open": True, "blocks": [
     {"h3": two("From O'Driscoll to prisoner","D'O'Driscoll à prisonnier")},
     {"p": two("Kieran is captured after the gang raids an O'Driscoll camp during their escape into the mountains, lassoed by [[arthur-morgan|Arthur]] in the mission \"Old Friends\". Held prisoner at Colter and then at Horseshoe Overlook, he is distrusted and threatened, but eventually warns the gang of an O'Driscoll ambush, proving he is not a spy.",
               "Kieran est capturé après l'assaut du gang sur un camp O'Driscoll, lors de leur fuite dans les montagnes : [[arthur-morgan|Arthur]] l'attrape au lasso dans la mission « Old Friends ». Retenu prisonnier à Colter puis à Horseshoe Overlook, il est méprisé et menacé, mais finit par révéler une embuscade O'Driscoll, prouvant qu'il n'est pas un espion.")},
     {"h3": two("A place in the camp","Une place dans le camp")},
     {"p": two("Allowed to stay, Kieran makes himself useful tending the gang's horses and slowly wins a cautious acceptance. He develops a shy attachment to camp member Mary-Beth Gaskill, though [[dutch-van-der-linde|Dutch]] and others never fully trust his O'Driscoll past.",
               "Autorisé à rester, Kieran se rend utile en s'occupant des chevaux du gang et gagne peu à peu une acceptation prudente. Il noue un attachement timide avec Mary-Beth Gaskill, une autre membre du camp, même si [[dutch-van-der-linde|Dutch]] et les autres ne lui pardonnent jamais tout à fait son passé O'Driscoll.")},
   ]},
   {"summary": two("Personality","Personnalité"), "blocks": [
     {"p": two("Kieran is gentle, nervous and desperate to belong. He joined the O'Driscolls for protection rather than out of cruelty, and among the Van der Lindes he is hard-working and harmless, the least violent man in a camp full of killers.",
               "Kieran est doux, nerveux et désespérément en quête d'appartenance. Il avait rejoint les O'Driscoll par besoin de protection, pas par cruauté, et chez les Van der Linde il est travailleur et inoffensif : l'homme le moins violent d'un camp peuplé de tueurs.")},
   ]},
   {"summary": two("Death and fate","Mort et destin"), "blocks": [
     {"p": two("Kieran is killed in 1899 during the gang's feud with [[colm-odriscoll|Colm O'Driscoll]]. While the gang is camped at Shady Belle, O'Driscolls behead him and send his body riding into camp to open an ambush. It is one of the most shocking deaths in the game.",
               "Kieran est tué en 1899 pendant la guerre du gang contre [[colm-odriscoll|Colm O'Driscoll]]. Alors que le gang campe à Shady Belle, des O'Driscoll le décapitent et renvoient son corps à cheval dans le camp pour déclencher une embuscade. C'est l'une des morts les plus choquantes du jeu.")},
   ]},
   {"summary": two("Behind the scenes","Coulisses"), "blocks": [
     {"p": two("Kieran appears only in Red Dead Redemption 2 (2018). His arc, from enemy prisoner to trusted hand, is often cited as an example of the game's willingness to kill off sympathetic characters without warning.",
               "Kieran n'apparaît que dans Red Dead Redemption 2 (2018). Son parcours, de prisonnier ennemi à homme de confiance, est souvent cité comme un exemple de la façon dont le jeu n'hésite pas à tuer des personnages attachants, sans prévenir.")},
   ]},
   {"summary": two("Trivia","Anecdotes"), "blocks": [
     {"ul": [
       two("He is captured in the mission \"Old Friends\".","Il est capturé dans la mission « Old Friends »."),
       two("He has feelings for fellow camp member Mary-Beth Gaskill.","Il a des sentiments pour Mary-Beth Gaskill, une autre membre du camp."),
       two("He proves his loyalty by revealing an O'Driscoll ambush.","Il prouve sa loyauté en révélant une embuscade O'Driscoll."),
     ]},
   ]},
 ],
 "relationships": [
   {"img": "arthur.jpeg", "slug": "arthur-morgan", "name": "Arthur Morgan", "text": two(
     "The man who captures him and, over time, one of the few who treats him with a measure of fairness.",
     "L'homme qui le capture et, avec le temps, l'un des rares à le traiter avec une certaine équité.")},
   {"img": "dutch.jpeg", "slug": "dutch-van-der-linde", "name": "Dutch van der Linde", "text": two(
     "The gang's leader, who tolerates Kieran but never lets go of his suspicion of a former O'Driscoll.",
     "Le chef du gang, qui tolère Kieran sans jamais renoncer à sa méfiance envers un ancien O'Driscoll.")},
   {"img": "colm.jpeg", "slug": "colm-odriscoll", "name": "Colm O'Driscoll", "text": two(
     "His former gang leader, whose war with the Van der Lindes ultimately gets Kieran killed.",
     "Son ancien chef de gang, dont la guerre avec les Van der Linde finit par coûter la vie à Kieran.")},
   {"img": "john.jpeg", "slug": "john-marston", "name": "John Marston", "text": two(
     "A gang member alongside whom Kieran works in the camp's day-to-day life.",
     "Un membre du gang aux côtés duquel Kieran travaille dans la vie quotidienne du camp.")},
 ],
 "gallery": [
   {"img": "gallery-1.jpeg", "alt": two("Kieran Duffy in the snow at Colter","Kieran Duffy dans la neige à Colter"),
    "cap": two("Kieran during the gang's time in the mountains.","Kieran pendant le séjour du gang dans les montagnes.")},
 ],
 "related": ["dutch-van-der-linde", "arthur-morgan", "john-marston", "micah-bell"],
},
# ============================ 7. MARY LINTON ============================
{
 "order": 7, "slug": "mary-linton", "name": "Mary Linton",
 "publishDate": "2026-07-02", "schema_game": "Red Dead Redemption 2",
 "reg_role_en": "Arthur's former love &middot; RDR2", "reg_role_fr": "Ancien amour d'Arthur &middot; RDR2",
 "gender": "Female",
 "portrait_alt": two("Mary Linton in Red Dead Redemption 2", "Mary Linton dans Red Dead Redemption 2"),
 "eyebrow": two("Character &middot; Red Dead Redemption 2", "Personnage &middot; Red Dead Redemption 2"),
 "meta_desc": two("Mary Linton (née Gillis): the former fiancee and great love of Arthur Morgan in Red Dead Redemption 2. Biography, relationship with Arthur, fate.",
                  "Mary Linton (née Gillis) : l'ancienne fiancée et le grand amour d'Arthur Morgan dans Red Dead Redemption 2. Biographie, relation avec Arthur, destin."),
 "og_desc": two("The former fiancee and great love of Arthur Morgan: her story, her family, and the life Arthur left behind.",
                "L'ancienne fiancée et le grand amour d'Arthur Morgan : son histoire, sa famille, et la vie qu'Arthur a laissée derrière lui."),
 "schema_desc": two("Former fiancee of Arthur Morgan and a recurring figure in Red Dead Redemption 2.",
                    "Ancienne fiancée d'Arthur Morgan et figure récurrente de Red Dead Redemption 2."),
 "chips": [two("Red Dead Redemption 2", "Red Dead Redemption 2"), two("Arthur's former love", "Ancien amour d'Arthur"),
           two("Widow", "Veuve"), two("Alive", "En vie")],
 "facts": [
   {"label": two("Status","Statut"), "value": two("Alive","En vie")},
   {"label": two("Nationality","Nationalité"), "value": two("American","Américaine")},
   {"label": two("Maiden name","Nom de jeune fille"), "value": two("Gillis","Gillis")},
   {"label": two("Married name","Nom d'épouse"), "value": two("Linton","Linton")},
   {"label": two("Relationship","Relation"), "value": two("[[arthur-morgan|Arthur Morgan]] (former fiance)","[[arthur-morgan|Arthur Morgan]] (ancien fiancé)")},
   {"label": two("Games","Jeux"), "value": two("Red Dead Redemption 2","Red Dead Redemption 2")},
 ],
 "intro": [
   two("Mary Linton, born Mary Gillis, is the former fiancee and great love of [[arthur-morgan|Arthur Morgan]]. Their engagement ended years before the events of Red Dead Redemption 2, broken by Arthur's outlaw life and her family's disapproval, and she later married a man named Barry Linton, who has since died.",
       "Mary Linton, née Mary Gillis, est l'ancienne fiancée et le grand amour d'[[arthur-morgan|Arthur Morgan]]. Leurs fiançailles ont pris fin des années avant les événements de Red Dead Redemption 2, brisées par la vie de hors-la-loi d'Arthur et la désapprobation de sa famille ; elle a ensuite épousé un certain Barry Linton, aujourd'hui décédé."),
   two("Widowed and still drawn to Arthur, Mary reappears through the story asking for his help with her troubled family. She represents the ordinary, settled life Arthur gave up for the gang.",
       "Veuve et toujours attachée à Arthur, Mary réapparaît au fil de l'histoire pour lui demander de l'aide avec sa famille en difficulté. Elle incarne la vie rangée et ordinaire à laquelle Arthur a renoncé pour le gang."),
 ],
 "sections": [
   {"summary": two("Biography","Biographie"), "open": True, "blocks": [
     {"h3": two("Engaged to an outlaw","Fiancée à un hors-la-loi")},
     {"p": two("Mary and [[arthur-morgan|Arthur]] were engaged in their youth, but his loyalty to the Van der Linde gang and her father's contempt for him ended the relationship. Mary went on to marry Barry Linton; by 1899 she is a widow.",
               "Mary et [[arthur-morgan|Arthur]] se sont fiancés dans leur jeunesse, mais la loyauté de ce dernier envers le gang Van der Linde et le mépris du père de Mary ont mis fin à leur relation. Mary a fini par épouser Barry Linton ; en 1899, elle est veuve.")},
     {"h3": two("The Gillis family","La famille Gillis")},
     {"p": two("In Red Dead Redemption 2, Mary contacts Arthur for help: first to pull her brother Jamie away from a cult, and later to deal with her ailing, demanding father. Their reunions are warm but painful, and a future together never quite becomes possible.",
               "Dans Red Dead Redemption 2, Mary recontacte Arthur pour qu'il l'aide : d'abord à arracher son frère Jamie à une secte, puis à gérer son père malade et exigeant. Leurs retrouvailles sont tendres mais douloureuses, et un avenir commun ne devient jamais vraiment possible.")},
   ]},
   {"summary": two("Personality","Personnalité"), "blocks": [
     {"p": two("Mary is kind and quietly sad, torn between her feelings for Arthur and her knowledge of what loving an outlaw costs. She is one of the few people who sees Arthur as more than a gunman.",
               "Mary est douce et empreinte d'une tristesse discrète, tiraillée entre ses sentiments pour Arthur et sa conscience de ce que coûte le fait d'aimer un hors-la-loi. Elle est l'une des rares personnes à voir en Arthur autre chose qu'un homme de main.")},
   ]},
   {"summary": two("Fate","Destin"), "blocks": [
     {"p": two("Mary survives the events of the game. In the epilogue, she is seen visiting [[arthur-morgan|Arthur]]'s grave, a quiet acknowledgement of what he meant to her.",
               "Mary survit aux événements du jeu. Dans l'épilogue, on la voit se recueillir sur la tombe d'[[arthur-morgan|Arthur]], hommage silencieux à ce qu'il a représenté pour elle.")},
   ]},
   {"summary": two("Behind the scenes","Coulisses"), "blocks": [
     {"p": two("Mary appears in Red Dead Redemption 2 (2018) through a series of optional companion missions. Whether the player pursues them is left open, making her one of the game's most personal and easily missed threads.",
               "Mary apparaît dans Red Dead Redemption 2 (2018) à travers une série de missions de compagnon facultatives. Le jeu laisse au joueur le choix de les suivre ou non, ce qui en fait l'un des fils les plus intimes et les plus faciles à manquer.")},
   ]},
   {"summary": two("Trivia","Anecdotes"), "blocks": [
     {"ul": [
       two("Her maiden name is Gillis.","Son nom de jeune fille est Gillis."),
       two("She was once engaged to Arthur Morgan.","Elle a été fiancée à Arthur Morgan."),
       two("She visits Arthur's grave in the epilogue.","Elle se recueille sur la tombe d'Arthur dans l'épilogue."),
     ]},
   ]},
 ],
 "relationships": [
   {"img": "arthur.jpeg", "slug": "arthur-morgan", "name": "Arthur Morgan", "text": two(
     "Her former fiance and the love of her life. Their bond is the heart of Mary's story, and a window into the man Arthur might have been.",
     "Son ancien fiancé et l'amour de sa vie. Leur lien est le cœur de l'histoire de Mary, et une fenêtre sur l'homme qu'Arthur aurait pu être.")},
   {"img": "dutch.jpeg", "slug": "dutch-van-der-linde", "name": "Dutch van der Linde", "text": two(
     "The gang leader whose hold on Arthur is, in large part, why Mary and Arthur never built a life together.",
     "Le chef de gang dont l'emprise sur Arthur explique en grande partie pourquoi Mary et Arthur n'ont jamais construit de vie commune.")},
   {"img": "john.jpeg", "slug": "john-marston", "name": "John Marston", "text": two(
     "A fellow gang member who, unlike Arthur, eventually does leave the outlaw life for a family.",
     "Un autre membre du gang qui, contrairement à Arthur, finit par quitter la vie de hors-la-loi pour fonder une famille.")},
 ],
 "gallery": [
   {"img": "gallery-1.jpeg", "alt": two("Arthur Morgan and Mary in an old photograph","Arthur Morgan et Mary sur une vieille photographie"),
    "cap": two("Arthur and Mary in happier days.","Arthur et Mary, à une époque plus heureuse.")},
 ],
 "related": ["arthur-morgan", "john-marston", "sadie-adler", "hosea-matthews"],
},
# ============================ 8. LEOPOLD STRAUSS ============================
{
 "order": 8, "slug": "leopold-strauss", "name": "Leopold Strauss",
 "publishDate": "2026-07-03", "schema_game": "Red Dead Redemption 2",
 "reg_role_en": "Van der Linde gang &middot; RDR2", "reg_role_fr": "Gang Van der Linde &middot; RDR2",
 "gender": "Male", "death": "1899", "nationality": "Austrian",
 "portrait_alt": two("Leopold Strauss in Red Dead Redemption 2", "Leopold Strauss dans Red Dead Redemption 2"),
 "eyebrow": two("Character &middot; Van der Linde gang", "Personnage &middot; Gang Van der Linde"),
 "meta_desc": two("Leopold Strauss: the Van der Linde gang's Austrian moneylender and bookkeeper in Red Dead Redemption 2, and the man behind Arthur's tuberculosis.",
                  "Leopold Strauss : l'usurier et comptable autrichien du gang Van der Linde dans Red Dead Redemption 2, et l'homme à l'origine de la tuberculose d'Arthur."),
 "og_desc": two("The gang's cold moneylender and bookkeeper, whose debt list gives Arthur Morgan tuberculosis.",
                "L'usurier et comptable au sang froid du gang, dont la liste de débiteurs vaut à Arthur Morgan la tuberculose."),
 "schema_desc": two("Austrian moneylender and bookkeeper of the Van der Linde gang.",
                    "Usurier et comptable autrichien du gang Van der Linde."),
 "chips": [two("Died <strong>1899</strong>", "Mort en <strong>1899</strong>"), two("Deceased", "Décédé"),
           two("Van der Linde gang", "Gang Van der Linde"), two("Money lender", "Usurier")],
 "facts": [
   {"label": two("Died","Mort"), "value": two("1899","1899")},
   {"label": two("Status","Statut"), "value": two("Deceased","Décédé")},
   {"label": two("Nationality","Nationalité"), "value": two("Austrian","Autrichienne")},
   {"label": two("Affiliation","Affiliation"), "value": two("Van der Linde gang","Gang Van der Linde")},
   {"label": two("Role","Rôle"), "value": two("Money lender & bookkeeper","Usurier et comptable")},
   {"label": two("Games","Jeux"), "value": two("Red Dead Redemption 2","Red Dead Redemption 2")},
 ],
 "intro": [
   two("Leopold Strauss is the Van der Linde gang's moneylender and bookkeeper, an Austrian immigrant who manages the gang's finances and runs a loan-sharking operation on the side. Cold and businesslike, he is behind some of the gang's least honourable work.",
       "Leopold Strauss est l'usurier et le comptable du gang Van der Linde, un immigré autrichien qui gère les finances du groupe et tient en parallèle un commerce de prêts à la petite semaine. Froid et calculateur, il est à l'origine de certaines des besognes les moins reluisantes du gang."),
   two("It is Strauss who sends [[arthur-morgan|Arthur Morgan]] to collect debts from people who cannot pay, including the encounter that infects Arthur with the tuberculosis that eventually kills him.",
       "C'est Strauss qui envoie [[arthur-morgan|Arthur Morgan]] recouvrer des dettes auprès de gens incapables de payer, dont la rencontre qui contamine Arthur par la tuberculose qui finira par l'emporter."),
 ],
 "sections": [
   {"summary": two("Biography","Biographie"), "open": True, "blocks": [
     {"h3": two("The gang's bookkeeper","Le comptable du gang")},
     {"p": two("Born in Austria and arriving in America by way of Vienna, Strauss handles the gang's money and lends it at interest to desperate locals. In \"Money Lending and Other Sins\" he hands [[arthur-morgan|Arthur]] a list of debtors to shake down.",
               "Né en Autriche et arrivé en Amérique en passant par Vienne, Strauss gère l'argent du gang et le prête à intérêt à des habitants aux abois. Dans « Money Lending and Other Sins », il remet à [[arthur-morgan|Arthur]] une liste de débiteurs à racketter.")},
     {"h3": two("The Downes debt","La dette Downes")},
     {"p": two("One of those debtors is a sick, broke farmer named Thomas Downes, who coughs blood on Arthur during the collection. That moment, set up by Strauss's ledger, is the source of the tuberculosis that defines the rest of [[arthur-morgan|Arthur]]'s story.",
               "L'un de ces débiteurs est un fermier malade et fauché, Thomas Downes, qui crache du sang sur Arthur pendant le recouvrement. Ce moment, provoqué par le grand livre de Strauss, est à l'origine de la tuberculose qui marque toute la fin de l'histoire d'[[arthur-morgan|Arthur]].")},
   ]},
   {"summary": two("Personality","Personnalité"), "blocks": [
     {"p": two("Strauss is calculating, mercenary and indifferent to the suffering his loans cause. He sees people as accounts to be settled, a coldness that eventually disgusts even Arthur.",
               "Strauss est calculateur, vénal et indifférent à la souffrance qu'engendrent ses prêts. Il voit les gens comme des comptes à solder, une froideur qui finit par dégoûter Arthur lui-même.")},
   ]},
   {"summary": two("Death and fate","Mort et destin"), "blocks": [
     {"p": two("As his health fails, [[arthur-morgan|Arthur]] turns on Strauss and throws him out of the gang for the misery his work has caused. Strauss is later captured by the Pinkertons and, according to [[dutch-van-der-linde|Dutch]], dies in custody without giving the gang up.",
               "Tandis que sa santé décline, [[arthur-morgan|Arthur]] se retourne contre Strauss et le chasse du gang pour le malheur que son travail a semé. Strauss est ensuite capturé par les Pinkerton et, selon [[dutch-van-der-linde|Dutch]], meurt en détention sans livrer le gang.")},
   ]},
   {"summary": two("Behind the scenes","Coulisses"), "blocks": [
     {"p": two("Strauss appears in Red Dead Redemption 2 (2018). His quiet, paperwork-driven cruelty is one of the game's clearest illustrations of how the gang harms ordinary people.",
               "Strauss apparaît dans Red Dead Redemption 2 (2018). Sa cruauté discrète, à coups de paperasse, est l'une des illustrations les plus nettes de la façon dont le gang fait du mal aux gens ordinaires.")},
   ]},
   {"summary": two("Trivia","Anecdotes"), "blocks": [
     {"ul": [
       two("He is Austrian, originally from Vienna.","Il est autrichien, originaire de Vienne."),
       two("His debt list leads directly to Arthur's tuberculosis.","Sa liste de débiteurs mène directement à la tuberculose d'Arthur."),
       two("Arthur banishes him from the camp near the end.","Arthur le bannit du camp vers la fin."),
     ]},
   ]},
 ],
 "relationships": [
   {"img": "dutch.jpeg", "slug": "dutch-van-der-linde", "name": "Dutch van der Linde", "text": two(
     "The leader Strauss serves as financier, funding the gang's plans with interest squeezed from the poor.",
     "Le chef que Strauss sert comme financier, alimentant les plans du gang avec les intérêts arrachés aux pauvres.")},
   {"img": "arthur.jpeg", "slug": "arthur-morgan", "name": "Arthur Morgan", "text": two(
     "The enforcer he sends to collect his debts, and the man who finally turns on him over the harm it causes.",
     "L'homme de main qu'il envoie recouvrer ses dettes, et celui qui finit par se retourner contre lui à cause du mal que cela provoque.")},
   {"img": "hosea.jpeg", "slug": "hosea-matthews", "name": "Hosea Matthews", "text": two(
     "A gang elder who, like Arthur, has little taste for the predatory side of Strauss's money lending.",
     "Un ancien du gang qui, comme Arthur, goûte peu le versant prédateur des prêts de Strauss.")},
   {"img": "john.jpeg", "slug": "john-marston", "name": "John Marston", "text": two(
     "A fellow gang member who shares in the proceeds of, and the unease around, the money Strauss brings in.",
     "Un autre membre du gang qui partage les profits, et le malaise, liés à l'argent que Strauss fait rentrer.")},
 ],
 "gallery": [
   {"img": "gallery-1.jpeg", "alt": two("Leopold Strauss at the camp","Leopold Strauss au camp"),
    "cap": two("Strauss at the gang's Horseshoe Overlook camp.","Strauss au camp du gang, à Horseshoe Overlook.")},
 ],
 "related": ["dutch-van-der-linde", "hosea-matthews", "arthur-morgan", "john-marston"],
},
# ============================ 9. SUSAN GRIMSHAW ============================
{
 "order": 9, "slug": "susan-grimshaw", "name": "Susan Grimshaw",
 "publishDate": "2026-07-04", "schema_game": "Red Dead Redemption 2",
 "reg_role_en": "Van der Linde gang &middot; RDR2", "reg_role_fr": "Gang Van der Linde &middot; RDR2",
 "gender": "Female", "death": "1899",
 "portrait_alt": two("Susan Grimshaw in Red Dead Redemption 2", "Susan Grimshaw dans Red Dead Redemption 2"),
 "eyebrow": two("Character &middot; Van der Linde gang", "Personnage &middot; Gang Van der Linde"),
 "meta_desc": two("Susan Grimshaw: the matriarch who runs the Van der Linde gang's camp in Red Dead Redemption 2. Biography, role, relationships and death.",
                  "Susan Grimshaw : la matriarche qui fait tourner le camp du gang Van der Linde dans Red Dead Redemption 2. Biographie, rôle, relations et mort."),
 "og_desc": two("The iron matriarch who keeps the Van der Linde camp running: her role, her loyalty to Dutch, and her death.",
                "La matriarche de fer qui fait tourner le camp Van der Linde : son rôle, sa loyauté envers Dutch, et sa mort."),
 "schema_desc": two("Matriarch and camp manager of the Van der Linde gang.",
                    "Matriarche et intendante du camp du gang Van der Linde."),
 "chips": [two("Died <strong>1899</strong>", "Morte en <strong>1899</strong>"), two("Deceased", "Décédée"),
           two("Van der Linde gang", "Gang Van der Linde"), two("Camp matriarch", "Matriarche du camp")],
 "facts": [
   {"label": two("Died","Mort"), "value": two("1899","1899")},
   {"label": two("Status","Statut"), "value": two("Deceased","Décédée")},
   {"label": two("Nationality","Nationalité"), "value": two("American","Américaine")},
   {"label": two("Affiliation","Affiliation"), "value": two("Van der Linde gang","Gang Van der Linde")},
   {"label": two("Role","Rôle"), "value": two("Camp matriarch","Matriarche du camp")},
   {"label": two("Games","Jeux"), "value": two("Red Dead Redemption 2","Red Dead Redemption 2")},
 ],
 "intro": [
   two("Susan Grimshaw is the matriarch and de facto manager of the Van der Linde gang's camp. She keeps the household running, disciplines its members and enforces order with a sharp tongue and, when needed, a shotgun.",
       "Susan Grimshaw est la matriarche et l'intendante de fait du camp du gang Van der Linde. Elle fait tourner la maisonnée, recadre ses membres et impose l'ordre à la langue bien pendue et, au besoin, au fusil."),
   two("One of the gang's longest-serving members and fiercely loyal to [[dutch-van-der-linde|Dutch van der Linde]], Susan holds the camp together long after its discipline begins to fray.",
       "Membre parmi les plus anciennes du gang et farouchement loyale à [[dutch-van-der-linde|Dutch van der Linde]], Susan tient le camp debout bien après que sa discipline a commencé à se déliter."),
 ],
 "sections": [
   {"summary": two("Biography","Biographie"), "open": True, "blocks": [
     {"h3": two("Running the camp","Faire tourner le camp")},
     {"p": two("Susan oversees the daily life of the camp: cooking, supplies, chores and the wellbeing, and the behaviour, of its members. She is especially firm with the younger women, Karen, Tilly and Mary-Beth, whom she both bosses and protects.",
               "Susan supervise la vie quotidienne du camp : la cuisine, les provisions, les corvées, et le bien-être, comme la conduite, de ses membres. Elle est particulièrement ferme avec les plus jeunes femmes, Karen, Tilly et Mary-Beth, qu'elle commande autant qu'elle protège.")},
     {"h3": two("Loyal to Dutch","Loyale à Dutch")},
     {"p": two("One of the gang's longest-serving members, Susan has a history with [[dutch-van-der-linde|Dutch]] going back to its early days, and she remains devoted to him even as his leadership unravels.",
               "Parmi les plus anciennes du gang, Susan a un passé avec [[dutch-van-der-linde|Dutch]] qui remonte aux débuts du groupe, et elle lui reste dévouée alors même que son autorité se défait.")},
   ]},
   {"summary": two("Personality","Personnalité"), "blocks": [
     {"p": two("Hard, blunt and tireless, Susan has no patience for idleness or self-pity. Beneath the severity is real care for the gang she treats as family.",
               "Dure, directe et infatigable, Susan n'a aucune patience pour l'oisiveté ou l'apitoiement. Sous la sévérité se cache une véritable affection pour le gang qu'elle traite comme une famille.")},
   ]},
   {"summary": two("Death and fate","Mort et destin"), "blocks": [
     {"p": two("Susan dies in 1899 at Beaver Hollow during the gang's collapse. When she confronts [[micah-bell|Micah Bell]] over his betrayal, shotgun in hand, he shoots her dead.",
               "Susan meurt en 1899 à Beaver Hollow, pendant l'effondrement du gang. Lorsqu'elle affronte [[micah-bell|Micah Bell]] au sujet de sa trahison, fusil au poing, il l'abat.")},
   ]},
   {"summary": two("Behind the scenes","Coulisses"), "blocks": [
     {"p": two("Susan appears in Red Dead Redemption 2 (2018). She is remembered as the person who, more than anyone, keeps the gang functioning day to day, and for her blunt warnings about what the camp would become without her.",
               "Susan apparaît dans Red Dead Redemption 2 (2018). On se souvient d'elle comme de la personne qui, plus que toute autre, fait tenir le gang au jour le jour, et pour ses avertissements sans détour sur ce que deviendrait le camp sans elle.")},
   ]},
   {"summary": two("Trivia","Anecdotes"), "blocks": [
     {"ul": [
       two("She manages the camp's daily life and chores.","Elle gère la vie quotidienne et les corvées du camp."),
       two("She has a past with Dutch from the gang's early years.","Elle a un passé avec Dutch, du temps des débuts du gang."),
       two("She is killed by Micah Bell at Beaver Hollow.","Elle est tuée par Micah Bell à Beaver Hollow."),
     ]},
   ]},
 ],
 "relationships": [
   {"img": "dutch.jpeg", "slug": "dutch-van-der-linde", "name": "Dutch van der Linde", "text": two(
     "The leader she has followed since the gang's earliest days, and to whom she stays loyal to the end.",
     "Le chef qu'elle suit depuis les tout débuts du gang, et à qui elle reste fidèle jusqu'au bout.")},
   {"img": "hosea.jpeg", "slug": "hosea-matthews", "name": "Hosea Matthews", "text": two(
     "A fellow gang elder; together they form the steadying older generation at the heart of the camp.",
     "Un autre ancien du gang ; ensemble, ils forment la génération plus âgée et stabilisatrice au cœur du camp.")},
   {"img": "sadie.jpeg", "slug": "sadie-adler", "name": "Sadie Adler", "text": two(
     "A widow taken in by the gang, whom Susan helps settle into camp life after the loss of her husband.",
     "Une veuve recueillie par le gang, que Susan aide à trouver sa place au camp après la perte de son mari.")},
   {"img": "arthur.jpeg", "slug": "arthur-morgan", "name": "Arthur Morgan", "text": two(
     "A gang mainstay Susan has known for years and treats, like the rest, as part of her extended family.",
     "Un pilier du gang que Susan connaît depuis des années et traite, comme les autres, comme un membre de sa famille élargie.")},
 ],
 "gallery": [
   {"img": "gallery-1.jpeg", "alt": two("Susan Grimshaw at the camp","Susan Grimshaw au camp"),
    "cap": two("Susan keeping the camp's younger members in line.","Susan tenant les plus jeunes du camp à la baguette.")},
 ],
 "related": ["dutch-van-der-linde", "hosea-matthews", "sadie-adler", "arthur-morgan"],
},
# ============================ 10. COLM O'DRISCOLL ============================
{
 "order": 10, "slug": "colm-odriscoll", "name": "Colm O'Driscoll",
 "publishDate": "2026-07-05", "schema_game": "Red Dead Redemption 2",
 "reg_role_en": "O'Driscoll Boys &middot; RDR2", "reg_role_fr": "Gang O'Driscoll &middot; RDR2",
 "gender": "Male", "death": "1899",
 "portrait_alt": two("Colm O'Driscoll in Red Dead Redemption 2", "Colm O'Driscoll dans Red Dead Redemption 2"),
 "eyebrow": two("Character &middot; O'Driscoll Boys", "Personnage &middot; Gang O'Driscoll"),
 "meta_desc": two("Colm O'Driscoll: leader of the O'Driscoll Boys and Dutch van der Linde's sworn enemy in Red Dead Redemption 2. Biography, the feud, and his hanging.",
                  "Colm O'Driscoll : chef du gang O'Driscoll et ennemi juré de Dutch van der Linde dans Red Dead Redemption 2. Biographie, la vendetta, et sa pendaison."),
 "og_desc": two("Leader of the O'Driscoll Boys and Dutch van der Linde's oldest enemy: the feud that drives the gangs to war.",
                "Chef du gang O'Driscoll et plus vieil ennemi de Dutch van der Linde : la vendetta qui pousse les gangs à la guerre."),
 "schema_desc": two("Leader of the O'Driscoll Boys and rival of the Van der Linde gang.",
                    "Chef du gang O'Driscoll et rival du gang Van der Linde."),
 "chips": [two("Died <strong>1899</strong>", "Mort en <strong>1899</strong>"), two("Deceased", "Décédé"),
           two("O'Driscoll Boys", "Gang O'Driscoll"), two("Dutch's rival", "Rival de Dutch")],
 "facts": [
   {"label": two("Died","Mort"), "value": two("1899 (hanged)","1899 (pendu)")},
   {"label": two("Status","Statut"), "value": two("Deceased","Décédé")},
   {"label": two("Nationality","Nationalité"), "value": two("American","Américaine")},
   {"label": two("Affiliation","Affiliation"), "value": two("O'Driscoll Boys (leader)","Gang O'Driscoll (chef)")},
   {"label": two("Rival","Rival"), "value": two("[[dutch-van-der-linde|Dutch van der Linde]]","[[dutch-van-der-linde|Dutch van der Linde]]")},
   {"label": two("Games","Jeux"), "value": two("Red Dead Redemption 2","Red Dead Redemption 2")},
 ],
 "intro": [
   two("Colm O'Driscoll is the leader of the O'Driscoll Boys, the rival outlaw gang and sworn enemies of the Van der Linde gang. The hatred between Colm and [[dutch-van-der-linde|Dutch van der Linde]] is the oldest and deepest feud in Red Dead Redemption 2.",
       "Colm O'Driscoll est le chef du gang O'Driscoll, la bande rivale et l'ennemie jurée du gang Van der Linde. La haine entre Colm et [[dutch-van-der-linde|Dutch van der Linde]] est la vendetta la plus ancienne et la plus profonde de Red Dead Redemption 2."),
   two("Ruthless and patient, Colm spends the game trading ambushes and reprisals with Dutch's gang until the rivalry ends at the gallows.",
       "Impitoyable et patient, Colm passe le jeu à échanger embuscades et représailles avec le gang de Dutch, jusqu'à ce que la rivalité s'achève au bout d'une corde."),
 ],
 "sections": [
   {"summary": two("Biography","Biographie"), "open": True, "blocks": [
     {"h3": two("The feud with Dutch","La vendetta avec Dutch")},
     {"p": two("The war between Colm and [[dutch-van-der-linde|Dutch]] goes back years and has cost both men dearly: Colm's people killed Dutch's lover, Annabelle, and Dutch killed Colm's brother. By 1899 the two gangs ambush and rob one another at every opportunity.",
               "La guerre entre Colm et [[dutch-van-der-linde|Dutch]] remonte à des années et a coûté cher aux deux hommes : les gens de Colm ont tué la compagne de Dutch, Annabelle, et Dutch a tué le frère de Colm. En 1899, les deux gangs s'embusquent et se détroussent à la moindre occasion.")},
     {"h3": two("Capture and hanging","Capture et pendaison")},
     {"p": two("After a failed parley and a string of clashes, including Colm's men capturing and torturing [[arthur-morgan|Arthur Morgan]], Colm is eventually taken and hanged in Saint Denis. His public execution doubles as a trap, drawing O'Driscolls and lawmen alike.",
               "Après un pourparler raté et une série d'affrontements, dont la capture et la torture d'[[arthur-morgan|Arthur Morgan]] par les hommes de Colm, ce dernier est finalement pris et pendu à Saint-Denis. Son exécution publique sert aussi de piège, attirant aussi bien les O'Driscoll que les forces de l'ordre.")},
   ]},
   {"summary": two("Personality","Personnalité"), "blocks": [
     {"p": two("Colm is cold, vengeful and calculating, a darker mirror of [[dutch-van-der-linde|Dutch]] without the charm or the talk of loyalty. He treats his own men as expendable.",
               "Colm est froid, vindicatif et calculateur, un reflet plus sombre de [[dutch-van-der-linde|Dutch]] sans le charme ni les discours sur la loyauté. Il traite ses propres hommes comme de la chair à canon.")},
   ]},
   {"summary": two("Death and fate","Mort et destin"), "blocks": [
     {"p": two("Colm O'Driscoll is hanged in Saint Denis in 1899. With his death the O'Driscoll Boys lose their leader, though the feud has already done lasting damage to the Van der Linde gang.",
               "Colm O'Driscoll est pendu à Saint-Denis en 1899. Sa mort prive le gang O'Driscoll de son chef, même si la vendetta a déjà infligé des dégâts durables au gang Van der Linde.")},
   ]},
   {"summary": two("Behind the scenes","Coulisses"), "blocks": [
     {"p": two("Colm appears in Red Dead Redemption 2 (2018), and the O'Driscoll Boys are referenced across the series. He is the external rival that pushes Dutch's gang toward open war early in the story.",
               "Colm apparaît dans Red Dead Redemption 2 (2018), et le gang O'Driscoll est évoqué dans toute la série. Il est le rival extérieur qui pousse le gang de Dutch vers la guerre ouverte dès le début de l'histoire.")},
   ]},
   {"summary": two("Trivia","Anecdotes"), "blocks": [
     {"ul": [
       two("His gang, the O'Driscoll Boys, are the Van der Lindes' chief rivals.","Son gang, les O'Driscoll, sont les principaux rivaux des Van der Linde."),
       two("His feud with Dutch involves the deaths of Annabelle and Colm's brother.","Sa vendetta avec Dutch implique les morts d'Annabelle et du frère de Colm."),
       two("He is hanged in Saint Denis.","Il est pendu à Saint-Denis."),
     ]},
   ]},
 ],
 "relationships": [
   {"img": "dutch.jpeg", "slug": "dutch-van-der-linde", "name": "Dutch van der Linde", "text": two(
     "His oldest enemy. The blood feud between them, paid in dead loved ones, shapes both gangs.",
     "Son plus vieil ennemi. La vendetta sanglante qui les oppose, payée en proches morts, façonne les deux gangs.")},
   {"img": "arthur.jpeg", "slug": "arthur-morgan", "name": "Arthur Morgan", "text": two(
     "Dutch's enforcer, whom Colm's men capture and torture during the feud.",
     "L'homme de main de Dutch, que les hommes de Colm capturent et torturent au cours de la vendetta.")},
   {"img": "kieran.jpeg", "slug": "kieran-duffy", "name": "Kieran Duffy", "text": two(
     "A former O'Driscoll who defects to the Van der Lindes, and whom Colm's men later kill.",
     "Un ancien O'Driscoll qui passe chez les Van der Linde, et que les hommes de Colm finiront par tuer.")},
   {"img": "john.jpeg", "slug": "john-marston", "name": "John Marston", "text": two(
     "A Van der Linde gunman on the other side of the war Colm wages against Dutch.",
     "Un fusil des Van der Linde, de l'autre côté de la guerre que Colm livre à Dutch.")},
 ],
 "gallery": [
   {"img": "gallery-1.jpeg", "alt": two("Colm O'Driscoll held captive","Colm O'Driscoll retenu captif"),
    "cap": two("Colm O'Driscoll held by the Van der Linde gang.","Colm O'Driscoll retenu par le gang Van der Linde.")},
 ],
 "related": ["dutch-van-der-linde", "micah-bell", "arthur-morgan", "bill-williamson"],
},
# ============================ 11. EDGAR ROSS ============================
{
 "order": 11, "slug": "edgar-ross", "name": "Edgar Ross",
 "publishDate": "2026-07-06", "schema_game": "Red Dead Redemption",
 "reg_role_en": "Antagonist &middot; RDR1", "reg_role_fr": "Antagoniste &middot; RDR1",
 "gender": "Male", "death": "1914",
 "portrait_alt": two("Edgar Ross in Red Dead Redemption", "Edgar Ross dans Red Dead Redemption"),
 "eyebrow": two("Character &middot; Red Dead Redemption", "Personnage &middot; Red Dead Redemption"),
 "meta_desc": two("Edgar Ross: the Bureau of Investigation agent and main antagonist of Red Dead Redemption who forces John Marston to hunt his old gang. Biography and death.",
                  "Edgar Ross : l'agent du Bureau of Investigation et antagoniste principal de Red Dead Redemption qui force John Marston à traquer son ancien gang. Biographie et mort."),
 "og_desc": two("The federal agent who blackmails John Marston into hunting his old gang, and the man Jack Marston later kills.",
                "L'agent fédéral qui force John Marston à traquer son ancien gang, et l'homme que Jack Marston finira par tuer."),
 "schema_desc": two("Bureau of Investigation agent and main antagonist of Red Dead Redemption.",
                    "Agent du Bureau of Investigation et antagoniste principal de Red Dead Redemption."),
 "chips": [two("Died <strong>1914</strong>", "Mort en <strong>1914</strong>"), two("Deceased", "Décédé"),
           two("Bureau of Investigation", "Bureau of Investigation"), two("Main antagonist (RDR1)", "Antagoniste principal (RDR1)")],
 "facts": [
   {"label": two("Died","Mort"), "value": two("1914","1914")},
   {"label": two("Status","Statut"), "value": two("Deceased","Décédé")},
   {"label": two("Nationality","Nationalité"), "value": two("American","Américaine")},
   {"label": two("Affiliation","Affiliation"), "value": two("Bureau of Investigation","Bureau of Investigation")},
   {"label": two("Role","Rôle"), "value": two("Federal agent","Agent fédéral")},
   {"label": two("Games","Jeux"), "value": two("Red Dead Redemption, Red Dead Redemption 2","Red Dead Redemption, Red Dead Redemption 2")},
 ],
 "intro": [
   two("Edgar Ross is a federal agent of the Bureau of Investigation and the main antagonist of the original Red Dead Redemption. In 1911 he forces [[john-marston|John Marston]] to hunt down his former gang by holding John's wife and son hostage.",
       "Edgar Ross est un agent fédéral du Bureau of Investigation et l'antagoniste principal du premier Red Dead Redemption. En 1911, il force [[john-marston|John Marston]] à traquer son ancien gang en retenant en otage la femme et le fils de ce dernier."),
   two("After John does everything asked of him, the government betrays him: Ross leads the raid in which John is killed. Three years later, John's son avenges him.",
       "Une fois que John a accompli tout ce qu'on lui demandait, le gouvernement le trahit : Ross mène le raid au cours duquel John est tué. Trois ans plus tard, le fils de John le venge."),
 ],
 "sections": [
   {"summary": two("Biography","Biographie"), "open": True, "blocks": [
     {"h3": two("Blackmailing John Marston","Le chantage sur John Marston")},
     {"p": two("In 1911 Ross and the Bureau take [[abigail-marston|Abigail]] and [[jack-marston|Jack Marston]] into custody to coerce [[john-marston|John]] into tracking down his old associates, Bill Williamson, Javier Escuella and [[dutch-van-der-linde|Dutch van der Linde]]. John completes the grim list in exchange for his family's freedom.",
               "En 1911, Ross et le Bureau placent [[abigail-marston|Abigail]] et [[jack-marston|Jack Marston]] en détention pour contraindre [[john-marston|John]] à traquer ses anciens complices : Bill Williamson, Javier Escuella et [[dutch-van-der-linde|Dutch van der Linde]]. John mène à bien cette sinistre liste en échange de la liberté de sa famille.")},
     {"h3": two("Betrayal and revenge","Trahison et vengeance")},
     {"p": two("Rather than leaving John in peace, Ross leads an army raid on the Marston ranch at Beecher's Hope, where [[john-marston|John]] is gunned down. In 1914 a grown [[jack-marston|Jack Marston]] tracks the retired Ross down and kills him, closing the story.",
               "Plutôt que de laisser John en paix, Ross mène un raid de l'armée sur le ranch des Marston, à Beecher's Hope, où [[john-marston|John]] est abattu. En 1914, un [[jack-marston|Jack Marston]] devenu adulte retrouve Ross, désormais à la retraite, et le tue, refermant l'histoire.")},
   ]},
   {"summary": two("Personality","Personnalité"), "blocks": [
     {"p": two("Ross is pragmatic, manipulative and without remorse, a man who frames cruelty as the price of progress and order. He embodies the new century's faith in government power.",
               "Ross est pragmatique, manipulateur et sans remords, un homme qui présente la cruauté comme le prix du progrès et de l'ordre. Il incarne la foi du nouveau siècle dans la puissance de l'État.")},
   ]},
   {"summary": two("Death and fate","Mort et destin"), "blocks": [
     {"p": two("Edgar Ross is killed by [[jack-marston|Jack Marston]] in 1914, shot in a duel by a river. His death is the final act of the original Red Dead Redemption.",
               "Edgar Ross est tué par [[jack-marston|Jack Marston]] en 1914, abattu en duel au bord d'une rivière. Sa mort est l'acte final du premier Red Dead Redemption.")},
   ]},
   {"summary": two("Behind the scenes","Coulisses"), "blocks": [
     {"p": two("Ross is the central antagonist of Red Dead Redemption (2010) and appears briefly in Red Dead Redemption 2 (2018) as a younger Bureau agent. He is, by design, one of the series' most hated figures.",
               "Ross est l'antagoniste central de Red Dead Redemption (2010) et apparaît brièvement dans Red Dead Redemption 2 (2018) en jeune agent du Bureau. Il est, à dessein, l'une des figures les plus détestées de la série.")},
   ]},
   {"summary": two("Trivia","Anecdotes"), "blocks": [
     {"ul": [
       two("He works for the Bureau of Investigation, a forerunner of the FBI.","Il travaille pour le Bureau of Investigation, ancêtre du FBI."),
       two("He forces John Marston to hunt Bill Williamson, Javier Escuella and Dutch.","Il force John Marston à traquer Bill Williamson, Javier Escuella et Dutch."),
       two("He is killed by Jack Marston in 1914.","Il est tué par Jack Marston en 1914."),
     ]},
   ]},
 ],
 "relationships": [
   {"img": "john.jpeg", "slug": "john-marston", "name": "John Marston", "text": two(
     "The reformed outlaw he blackmails and then betrays, the central victim of Ross's pursuit of order.",
     "Le hors-la-loi repenti qu'il fait chanter puis trahit, la victime centrale de la quête d'ordre de Ross.")},
   {"img": "jack.jpeg", "slug": "jack-marston", "name": "Jack Marston", "text": two(
     "John's son, who grows up to hunt Ross down and kill him in 1914.",
     "Le fils de John, qui, devenu adulte, retrouve Ross et le tue en 1914.")},
   {"img": "dutch.jpeg", "slug": "dutch-van-der-linde", "name": "Dutch van der Linde", "text": two(
     "The old gang leader and one of the targets Ross sends John to hunt down.",
     "L'ancien chef de gang et l'une des cibles que Ross envoie John traquer.")},
 ],
 "gallery": [
   {"img": "gallery-1.jpeg", "alt": two("Edgar Ross during the hunt for the gang","Edgar Ross pendant la traque du gang"),
    "cap": two("Ross closing in during the hunt for the Van der Linde gang's remnants.","Ross resserrant l'étau lors de la traque des derniers membres du gang Van der Linde.")},
 ],
 "related": ["john-marston", "dutch-van-der-linde", "bill-williamson", "micah-bell"],
},
]

if __name__ == "__main__":
    for c in CHARS:
        folder = build_to_queue(c)
        print("built", folder)
