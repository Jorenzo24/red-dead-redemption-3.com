# Fact-check report: Tavish Gray, chunk half2.txt (Relationships, Caliga Hall, Missions, Quotes, Development and performance, Other media, Trivia)

## Sources used
- Fan transcript scripts/v3/work/tavish/fc/gsw.txt: "Horse Flesh for Dinner" (l. 7426-7560), "The Course of True Love I + II" (l. 6220-6256), "The New South" (l. 5784-5839), "American Distillation" (l. 6094-6110), "Advertising, The New American Art" (l. 6530-6548), "Sodom? Back To Gomorrah" (l. 7106), "The Fine Joys of Tobacco" (l. 7561-7711), "A Short Walk in a Pretty Town" (l. 7852-7937).
- scripts/v3/sources/Camp_Events.txt l. 326 (Dutch "make the Grays bleed"); scripts/v3/rules/HOUSE_FACTS.md, OWNERSHIP.md.
- Red Dead Wiki: en.txt / fr.txt (Tavish Gray), _m/Horse_Flesh_for_Dinner.txt, _m/Advertising_The_New_American_Art.txt, _m/Madison_Arnold.txt, _m/Red_Dead_Redemption_2_Cut_Content.txt; fetched 22 Oct 2026: "Gray's Secret", "Caliga Hall", "Leigh Gray", "Beau Gray", "Gray Family", "The Course of True Love V".
- fc/wp_GTA_IV.txt (Wikipedia GTA IV), fc/gtawiki_Jon_Gravelli.txt; GTABase "Tavish Gray" (fetched: "He is portrayed by Madison Arnold."); Wikipedia "Geraldine Moffat" (API, fetched 22 Oct 2026); GTA Wiki "The Sharmoota Job" (API, fetched 22 Oct 2026); catherine/fc/wp_list_rdr2.txt.
- Full fiche text tavish_full_en.txt for duplicates.

## Verified OK
All quoted lines in the Quotes block match the transcript verbatim (Tavish's two job lines, John's "Five thousand dollars for horses?...", Clay Davies, Arthur's journal, Dutch's "Sheriff Gray kindly put in a word with his father.", Beau's introduction) and the two journal lines match the Gray's Secret gallery captions word for word. Madison Arnold as Tavish's voice: Red Dead Wiki EN (infobox + actor page), Red Dead Wiki FR ("acteur = Madison Arnold") and GTABase ("He is portrayed by Madison Arnold") all agree. Jon Gravelli credit: Wikipedia GTA IV ("Jon Gravelli (Madison Arnold), the aging head of the city's most powerful crime family") and GTA Wiki ("He is voiced by Madison Arnold"). Geraldine Moffat: Wikipedia "Geraldine Houser (née Moffat; born 1939) is a British actress", children Sam and Dan Houser: confirmed. Cut content items (vest, Adam, free roam, unique stallions grays2_01-03, "Grey" spelling): all on the Cut Content page. Dutch's rare "make the Grays bleed" line (Camp Events), Bill's "cooking up... some deals with them Gray boys" (Sodom? Back To Gomorrah), Sean's "Old Man Gray's doubled security" and the supply/payroll wagons, the Caliga Hall guard ("This is private property"), Archibald's lines (generations, all the businesses, Rhodes Parlor House owned by the Grays), Beau and Penelope leaving Rhodes by train in "The Course of True Love V", Leigh Gray selling the bounty hunter license in Red Dead Online, Shirley Plantation and the 1907 state of the estate (Caliga Hall wiki page), the Callahan alias in "American Distillation", the mission-failure condition, and the "only point of interest tied to a mission" item (Gray's Secret page): all supported. House decisions respected: no shooter named for Sean, no cause of death, no "wiped out".

## Problems

1. **WRONG** (Relationships, Catherine Braithwaite): "He calls her a hag, calls her sons inbred and accuses them of killing his uncle (see Quotes)."
   Source: the "That hag and her inbred sons..." line is NOT in the Quotes block (tavish_full_en.txt: Quotes holds only the horse-job lines and lines about the Grays). Part B's docstring leaves it to C, part C's docstring leaves it to B: it ended up in neither. The pointer leads nowhere.
   Fix: either add the transcript line to Quotes (gsw.txt l. 7446: "That hag and her inbred sons… they've ruined this county. They killed my uncle, you know.", context: to John and Arthur, Horse Flesh for Dinner) and keep the pointer, or change the pointer to "(see Biography)", where the accusation is already paraphrased.

2. **WRONG** (Relationships, Catherine Braithwaite): "She pays the gang to burn his tobacco fields, while he pays it to steal her horses (see Biography)."
   Source: gsw.txt l. 7448-7460: Tavish never pays the gang. He says "We've got gold" but the gang's money comes from selling the horses to a fence ("give you fifty cents on the dollar"); the gang gets 700 dollars from Clay Davies, nothing from Tavish. For Catherine, Hosea raises "the question of money" and she answers "Oh, we've got money" (l. 7573-7574); no payment is shown on screen in "The Fine Joys of Tobacco".
   Fix: "She hires the gang to burn his tobacco fields, while he sends it to steal her horses and sell them to a fence (see Biography)."

3. **WRONG** (Relationships, Javier Escuella): "Tavish does not speak to him."
   Source: Horse Flesh for Dinner mission page (trivia): if "The Fine Joys of Tobacco" was played first, "Tavish Gray can be overheard ... telling Javier and John that he is suspicious"; the Biography (tavish_full_en.txt l. 33) says the same. His directions to the south-side stables are addressed to all three (gsw.txt l. 7465).
   Fix: "Javier never speaks with Tavish in the main scene." or drop the sentence.

4. **IMPRECISE** (Relationships, Micah Bell): "Micah rides into Rhodes with Arthur, Bill and Sean for the security job".
   Source: gsw.txt l. 7853-7854: Arthur rides to a butcher in Rhodes to meet Micah, Sean and Bill, who are already waiting ("We been waiting for you, Arthur").
   Fix: "Micah waits in Rhodes with Bill and Sean for Arthur before the security job, and fights the Grays' gunmen with Arthur (see Biography)."

5. **IMPRECISE** (Trivia, last item): "...a heist cut from Grand Theft Auto V, in which the crew poses as buyers interested in a rival's property in order to steal his horses."
   Source: GTA Wiki "The Sharmoota Job": Michael and Trevor view Martin Madrazo's house "as prospective buyers"; the targets were "a safe, Madrazo's prized horse and kidnap his wife". Madrazo is a cartel boss and antagonist, not a "rival"; the Red Dead Wiki mission page says "an antagonist's property" and "Madrazo's valuable horse or horses".
   Fix: "...a heist cut from Grand Theft Auto V (the 'Nice House Heist'), in which Michael and Trevor pose as buyers visiting Martin Madrazo's house in order to steal, among other things, his prized horse."

6. **IMPRECISE** (Development and performance): "Wikipedia's list of the game's characters, based on the credits, does not include him."
   Source: catherine/fc/wp_list_rdr2.txt: the list cites many sources (credits, booklet, press); "based on the credits" suggests the game's credits omit him, which nobody checked (part D docstring: "No Rockstar credits text could be read").
   Fix: "Wikipedia's list of the game's characters does not include him."

7. **COPIED** (Development and performance): "the aging head of the most powerful crime family of Liberty City".
   Wikipedia GTA IV (fc/wp_GTA_IV.txt): "Jon Gravelli (Madison Arnold), the aging head of the city's most powerful crime family".
   Fix: "who voices Jon Gravelli, the elderly don of the Gambetti family, in Grand Theft Auto IV (2008)" (Gambetti: GTA Wiki), or put the Wikipedia phrase in quotation marks.

8. **DUPLICATE** (Relationships, Leigh Gray): the whole son/brother inconsistency (Beau calls him uncle; both wikis; Dutch's "word with his father"; Arthur's "your son, the sheriff"; nobody corrects him) is told in full here AND in Biography/Origins para. 2 (tavish_full_en.txt l. 26), plus Key facts, facts grid and Names ("Dutch and Arthur speak of him as the sheriff's father").
   Fix: keep the full telling in ONE place. Part B's docstring assigns it to the Leigh entry: keep it there and cut Origins para. 2 to one clause with "(see Relationships, Leigh Gray)", as Names already does.

9. **DUPLICATE** (Relationships, Beau Gray): "Beau introduces himself to Arthur as the son of Tavish Gray, the nephew of Sheriff Leigh Gray and the grandson of Murdo Gray."
   Already in Biography/Origins (l. 25), in Names ("introduces himself as the son of Tavish Gray"), and quoted verbatim in Quotes. The same Murdo point is repeated in the Murdo entry.
   Fix: in the Beau entry, keep "His son" + the Penelope clause; refer to Quotes for the introduction.

10. **DUPLICATE** (Relationships, John Marston): "He tells Tavish the newcomers lost money in the west on a failed railway speculation, and claims a father who came over from Scotland. He accepts the deal and later takes the 700 dollars ... He calls Tavish a crazy old fool as they ride off (see Names)."
    All told in Biography (l. 31-32: railway, Scottish father, John accepts, "crazy old fool", 700) and "Crazy old fool" quoted again in Names. Ownership: relationship entries refer to events in one clause.
    Fix: "John does most of the talking at the stables, accepts the deal and takes the fence's 700 dollars (see Biography). He calls Tavish a crazy old fool (see Names)." (or drop the last sentence).

11. **DUPLICATE** (Relationships, Arthur Morgan): "In his journal he writes after the sale that they felt like prize idiots."
    The journal entry is quoted in Quotes and paraphrased in Biography (l. 32); here it reuses the quoted words ("prize idiots") without quotation marks.
    Fix: cut the sentence (or "see Quotes").

12. **DUPLICATE** (Caliga Hall, para. 1): Archibald's tour ("Grays have lived there for generations", "own all the businesses in Rhodes, including the Rhodes Parlor House") is already in Origins (l. 27: "lived at Caliga Hall for generations and own all the businesses in Rhodes, including the saloon") and in Key facts; the Bayou Nwa location is also in Origins.
    Fix: keep Archibald's description in the Caliga Hall paragraph (its natural home, per part B docstring) and cut Origins to "The Rhodes deputy Archibald MacGregor says the family owns all the businesses in town (see Caliga Hall)", or the reverse; one telling only.

13. **DUPLICATE** (Caliga Hall, para. 2): "In 'The Fine Joys of Tobacco', Sean reports that security has been doubled since the saloon incident..."
    Told in Biography (l. 34: "Sean says he has heard that security at the estate was doubled after the trouble at the Rhodes saloon") and in Names ("Sean says that 'Old Man Gray' has doubled security").
    Fix: keep it here (the supply/payroll wagons detail belongs with the estate), cut the doubled-security clause from the Biography; Names keeps only the nickname without the security detail.

14. **DUPLICATE** (Caliga Hall, para. 2): "According to the Red Dead Wiki, the family still owns the estate in 1907, the fields are still worked and guards patrol at night."
    Same three facts, same attribution, in Biography "the epilogue (1907)" (l. 41).
    Fix: keep in the Biography 1907 section (the epilogue is narrative chronology), cut from Caliga Hall; or, if the lead follows the part B docstring ("1907 state of the estate HERE"), cut from the Biography and leave only the body-unchanged sentence there.

## Count per category
- WRONG: 3
- IMPRECISE: 3
- UNSUPPORTED: 0
- MISQUOTE: 0
- SPECULATION: 0
- COPIED: 1
- DUPLICATE: 7
- STYLE: 0
Total: 14
