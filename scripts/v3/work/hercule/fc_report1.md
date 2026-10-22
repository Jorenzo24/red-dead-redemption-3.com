# Fact-check report 1: Hercule Fontaine, chunk half1.txt (intro, Key facts, facts grid, Biography, Personality, In his own words, Names, Appearance)

## Sources used
- Fan transcript, Game Scripts Wiki (fc/gsw.txt), lines 10480-11010: "Welcome to the New World", "Savagery Unleashed", "A Kind and Benevolent Despot", "Hell Hath No Fury", "Paradise Mercifully Departed".
- Red Dead Wiki EN character page (en.txt); mission pages in scripts/v3/work/_m/ (Welcome_to_the_New_World, Hell_Hath_No_Fury, Paradise_Mercifully_Departed); wiki pages Guarma_Rebels, Baptiste, Captain_C, La_Capilla, Cinco_Torres, El_Nido; newspaper pages Leader_of_Guarma_Assassinated and Unrest_in_the_Tropics (+ Bureau_of_Investigation_Founded, to confirm that Ledger No. 74 is a 1907 issue); scripts/v3/sources/Camp_Events.txt (Guarma section); scripts/v3/sources/thr_descriptions.txt (no Hercule entry).
- fc/wp_list_rdr2_hercule_line.txt (Guyviaud Joseph); live portrait assets/characters/hercule-fontaine/portrait.jpeg (Appearance).
- FIX_RULES.md, HOUSE_FACTS.md, OWNERSHIP.md, the docstrings of hercule_A..D, and fussar_A for consistency. Full fiche (hercule_full_en.txt) for duplicates.

## Verified OK
The intro, the Key facts and the facts grid match the transcript and FIX_RULES (the offer, the cannon on the tower, the hedged nationality, no fate after Guarma, Guyviaud Joseph via the Wikipedia credits). The biography follows the transcript closely, line by line: the ambush, the guns stashed at the old building (El Nido, wiki), the introductions, Leon and Hercule on Fussar, the Aguasdulces lookout, the deal, the cave, "Gentlemen, goodbye", Baptiste's boat message and the $450 (Baptiste page), the "using us" exchange in the cave, the whole of "Hell Hath No Fury" (argument, offer, navy from Cuba, French call, fight or run, shotgun, the shell that hits their own men, "following you", the soldier heading for Dutch, the waterline, the boat and captain due at the dock, Dutch's farewell), and the whole of "Paradise Mercifully Departed" (Micah's report, "every day I can", the batteries, the roof soldier, the fields, the blue building, the rifle kicked to the captain, "I didn't see him", the tower cannon, the second cannon, the attributed fire-drawing claim, the Haiti answer). Captain engaged in return for the workers: Captain C. page. The newspaper titles, issue numbers and content match the wiki article pages, and No. 74 is an epilogue issue. The "status unclear by 1907" claim comes from the Guarma Rebels page. All five "In his own words" lines and the two Names quotes are verbatim in the transcript. Leaders Hercule and Leon: Guarma Rebels infobox. "Supplied the uprising": Baptiste page. "Capital of his rebel movement": Cinco Torres page. No em or en dashes.

## Problems

1. **IMPRECISE**: "On the island, he works with the rebel Leon Fuentes and with Baptiste, who tells Arthur Morgan that he works for Hercule."
   Source: the transcript, "Savagery Unleashed": Baptiste says "I work with Hercule." (Leon calls him "One of Hercule's men"). Relationships quotes "I work with Hercule" correctly.
   Fix: "...and with Baptiste, who tells Arthur Morgan that he works with Hercule; Leon calls him one of Hercule's men."

2. **SPECULATION**: "Levi Simon, Fussar's overseer, dismisses the island's insurgents as Haitian pirates"
   Source: the transcript, "Welcome to the New World": "Bunch of Haitian pirates won't frighten him. They'll be strung up in the streets soon enough." Simon does not say whom he means. Part B (Relationships, Levi Simon) says so explicitly: "the game does not say whom he means." The draft names the target, which contradicts B.
   Fix: "Levi Simon, Fussar's overseer, speaks of Haitian pirates who will not frighten Fussar, without saying whom he means (see Relationships)." Better still, drop the sentence here and keep the point only in Relationships (see item 13).

3. **IMPRECISE**: "On the march, the column picks up a group of captured local rebels, among them Leon Fuentes, whom a guard accuses of insurrection."
   Source: the transcript: Dutch asks what crime "they" (the whole group) committed. The guard answers "Criminals." / "Insurrection." about all of them. Leon (labelled "Stranger") mocks the word ("Insurrection? That's quite a word."), and the guard replies "Be quiet, Mr. Fuentes."
   Fix: "...a group of captured local rebels, among them Leon Fuentes. A guard tells Dutch that they are guilty of insurrection, and orders Leon to be quiet when he mocks the word."

4. **IMPRECISE (order)**: "They take rifles from the crates and drive off the soldiers who followed them. Arthur thanks him for getting them out; when Arthur comments on the island, Hercule replies that it is not his."
   Source: the transcript: "Thanks for getting us out of there" and the "Nice island" / "It's not my island" exchange both come during the fight at the old building, before Dutch's "They're running away!".
   Fix: "During the fight, Arthur thanks him for getting them out and comments on the island; Hercule replies that it is not his. The soldiers finally retreat."

5. **IMPRECISE**: "Leon describes Fussar as a tyrant who works the islanders to death"
   Source: the transcript: "A tyrant, driven by nothing but power and greed. Our only purpose is to work ourselves to death... to make him rich." Leon adds that the workers are "little more than slaves shipped in from other islands", so not "islanders".
   Fix: "Leon describes Fussar as a tyrant driven by power and greed, for whom the workers exist only to work themselves to death and make him rich."

6. **IMPRECISE (violates FIX_RULES 6)**: "He takes the four men to a place where they can rest, near La Capilla, which the mission page describes as the rebels' camp"
   Source: the mission page "Welcome to the New World" says "La Capilla, the rebels' camp". The La Capilla page says "an enemy outpost... an outpost for Fussar's soldiers", and Arthur is held prisoner there in "Savagery Unleashed" (Guarma Rebels, La Capilla pages). Camp Events: "a small run down fort by La Capilla". FIX_RULES 6: do not label it, or give both versions, attributed, in one place.
   Fix: "He takes the four men to a place where they can rest, near La Capilla, then says goodbye and leaves with Leon." Drop the label.

7. **IMPRECISE (order)**: "Micah complains that this is not their fight and that Hercule is using them; Hercule asks him whether he wants to leave the island or not."
   Source: the transcript: Micah says "This ain't our fight!", Hercule answers "Do you want to get off this island or not?", and only then does Micah shout "He's using us!". Relationships (Micah) gives the right order.
   Fix: "Micah complains that this is not their fight; Hercule asks him whether he wants to leave the island or not, and Micah shouts that Hercule is using them."

8. **COPIED**: three biography sentences reuse the mission pages' wording.
   - "Arthur takes a gun from a dead guard and kills the soldiers while the others free themselves." Mission page "Welcome to the New World": "Arthur is able to steal one of their guns and kill the guards while the others free themselves."
   - "Arthur helps Hercule push the cannon into position." Mission page "Hell Hath No Fury": "Arthur helps Hercule push the cannon into position" (identical; the same sentence also appears in Relationships, Arthur).
   - "Micah and Bill stay on the roof to guard the cannon" / "Dutch stays below to hold off the soldiers". Mission page: "Micah and Bill remain on the roof to guard the cannon" / "Dutch stays behind to hold off the reinforcements".
   Fix: reword, e.g. "Arthur grabs the revolver of a guard who has been shot and kills the escort, while the others get out of their chains." / "Arthur and Hercule drag the heavy cannon to the edge of the roof." / "Micah and Bill keep watch over the cannon from the roof" / "Dutch holds the beach alone".

9. **IMPRECISE**: "Oh, I'll fight Alberto Fussar every day I can." (when Dutch asks if he is in, "Paradise Mercifully Departed")
   Source: the transcript: Dutch only says "Hercule?" after Micah's report.
   Fix: context "(when Dutch turns to him after Micah's report, 'Paradise Mercifully Departed')".

10. **SPECULATION / STYLE**: Personality, second paragraph: "Under fire at Cinco Torres he answers Bill's and Micah's complaints sharply, then follows Arthur's lead in the fighting on the beach. He knows that killing soldiers will not end Fussar's hold on the island. Once Fussar is dead, he does not claim the island for the rebels: he says they will disappear, like the gang, before morning."
    Source: "sharply" is a reading of tone, and "Fussar's hold on the island" extrapolates his line ("He will have the money to get more"). "Does not claim the island for the rebels" is analysis of something he does not say. All three are also duplicates (see item 11).
    Fix: delete the paragraph. The quotes just below already carry these lines.

11. **DUPLICATE**: Personality, first paragraph after the official-description sentence ("He asks the castaways what they are doing on the island before he gives his own name. He says plainly that he is not from Guarma and that he works behind Fussar's back. He sets the terms of his help at once...") plus the second paragraph (item 10).
    Each fact is already in the Biography ("Welcome to the New World" paragraphs), in Origins, in Key facts, in Smuggling, in Relationships (Arthur, Bill, Micah), and in the "In his own words" lines directly below ("I am not from here...", "I don't see you have any choice...", "It doesn't matter how many we kill...", "We'll be like you..."). OWNERSHIP: the biography owns events, and Personality must not be a second biography.
    Fix: reduce Personality to the official-description sentence plus one sentence pointing to his own words, e.g. "What is known of his character comes from what he says in his three missions." Keep the events in the Biography.

12. **DUPLICATE (quotes)**: "In his own words" quotes "I don't see you have any choice. I am the only one who can arrange a boat for you. But... I need something in return." and "We'll be like you. We'll disappear probably... back to Haiti. Believe me, we'll be long gone by morning.". Both lines are quoted again in part C's Quotes block.
    FIX_RULES 5 / the hercule_B docstring: lines quoted in B are not quoted again in C.
    Fix: keep both in "In his own words" (B) and remove them from C's Quotes.

13. **DUPLICATE**: the Haiti line and Levi Simon's "Haitian pirates" appear in Key facts, the facts grid (Nationality), Origins (second paragraph), the end of the biography, Personality, In his own words, C Quotes and Relationships (Levi Simon).
    Fix: keep the nationality point in the facts grid (D). Keep the event at the end of the biography (A), with the verbatim line in B "In his own words". Keep Simon's line in Relationships (Levi Simon). In Origins, cut it to one clause: "The game never states his nationality (see the facts grid); the Red Dead Wiki describes him as Haitian." Drop Simon's sentence there (item 2).

14. **DUPLICATE**: Origins "He also keeps a supply of guns in an old building in the jungle, which the Red Dead Wiki names El Nido" and "He and his men use the old Spanish fort of Cinco Torres as a hideout". The same facts are retold in B "Smuggling" ("He has weapons hidden on the island... old building where he says he has guns stashed", "use the old fort of Cinco Torres as a hideout whenever they are on Guarma") and in Key facts.
    OWNERSHIP: A owns these; Skills should point to the Biography.
    Fix: keep them in A Origins (Key facts may keep the one-line summary); reduce Smuggling to a pointer.

15. **DUPLICATE (quote)**: Names: "Arthur refers to him as 'this Hercule feller' (see Relationships)". The same line is quoted verbatim in Relationships (Arthur).
    OWNERSHIP: each line is quoted in exactly one place.
    Fix: keep the quote in Names (it is a name use) and paraphrase it in Relationships (Arthur), e.g. "Arthur asks Dutch whether Hercule is just using them." Or the reverse: drop it from Names.

16. **IMPRECISE (wrong section)**: Names: "Leon Fuentes describes Baptiste as 'One of Hercule's men'." This line is about Baptiste, not about a name for Hercule.
    Fix: move it to Origins as the support for item 1 (paraphrased, without quotation marks, since A always paraphrases) or to Relationships (Baptiste), and remove it from Names.

17. **DUPLICATE**: Personality: "Rockstar's character descriptions of September 2018 cover the Van der Linde gang and do not include him". The same point is repeated in "Other media and legacy" ("He was not among the characters described in the details Rockstar gave The Hollywood Reporter in September 2018...").
    OWNERSHIP: official descriptions belong to Personality (B).
    Fix: keep it in Personality; delete it from Other media.

18. **IMPRECISE**: Appearance: "He wears several strings of colored beads around his neck."
    Source: the live portrait shows one string of colored beads plus a thin dark cord or chain with a pendant. He also has a scar on his left cheek, which is correct as written.
    Fix: "He wears a necklace of colored beads and a thin cord with a pendant around his neck."

## Cross-chunk note (half2, for the other checker or the fixer)
Several lines are quoted twice in half2: "It's not my island" (Relationships Arthur + Quotes), "I am! What do you want me to do?..." (Relationships Bill + Quotes), "He's using us!" (Relationships Micah + Quotes), "Hercule... it was a great pleasure..." (Relationships Dutch + Quotes). The B docstring assigns all four to Relationships, so they should come out of C Quotes. Leon is described as one of "the two leaders" in Origins (Guarma Rebels page) but as "a member of the rebel faction led by Hercule" in Relationships (Leon page). The wikis differ: state it once, attributed.

## Count per category
- WRONG: 0
- IMPRECISE: 9 (items 1, 3, 4, 5, 6, 7, 9, 16, 18)
- UNSUPPORTED: 0
- MISQUOTE: 0
- SPECULATION: 2 (items 2, 10)
- COPIED: 1 (item 8, three sentences)
- DUPLICATE: 6 (items 11, 12, 13, 14, 15, 17)
- STYLE: 0 (the style issues of item 10 are counted under SPECULATION)

Total: 18 items.
