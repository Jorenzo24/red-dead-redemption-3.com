# Fact-check report 1: Eagle Flies, chunk half1.txt (intro, key facts, facts grid, Biography, Personality, In his own words, Names, Appearance)

## Sources used
- Fan transcript fc/gsw.txt: Eastward Bound (l. 3455-3500), The Gilded Cage (l. 9070-9110, 9300-9320), American Fathers I+II (l. 9536-9660), That's Murfree Country (l. 11232), A Rage Unleashed (l. 12195-12300), Archeology for Beginners (l. 12305-12400), The Fine Art of Conversation (l. 12500-12540), Favored Sons (l. 12838-12965), The King's Son (l. 12965-13095), My Last Boy (l. 13095-13305), Red Dead Redemption mission (l. 13457-13489).
- Mission pages in _m/: Eastward_Bound, The_Gilded_Cage, American_Fathers_I, American_Fathers_II, A_Rage_Unleashed, Archeology_for_Beginners, The_Fine_Art_of_Conversation, Favored_Sons, The_King_s_Son, My_Last_Boy, Ending_Credits, Newspapers_Red_Dead_Redemption_2.
- Wiki pages: eagle/en.txt, eagle/fr.txt, rains/en.txt; fetched via API: Paytah, Paying Respects, Donner Falls.
- fc/Tensions_High.txt, fc/Pump_Jacks_Sit_Silent.txt; sources/Camp_Events.txt; rules/HOUSE_FACTS.md, rules/OWNERSHIP.md, FIX_RULES.md; eagle_D.py docstring (Bitsui).

## Verified OK
Intro and key facts match the transcripts and mission pages (courthouse, Leland Oil report, 125-dollar reward, Van Horn boat, Cumberland Forest ambush, Fort Wallace rescue on Taima, Favours's shot, death in the tent). Origins (father's speech verbatim in gsw l. 13111; wiki "second son", "by the U.S. Army", FR "peu de temps avant 1899") is correctly attributed. Eastward Bound, Gilded Cage (Bronte's mockery, letter to the mayor, Dutch on Miller the next day), American Fathers I/II dialogue, the oil-well blast attributed to the mission page, That's Murfree Country, the Rage Unleashed raid (Charles's "I will not fight over some horses", Dutch "made no such promise", night boarding, four horses, "Father need not know"), Fine Art (mission page trivia), Favored Sons and The King's Son (cell, keys, hole repaired, cannon/dynamite breach, Taima, canoes, "heal fast", "Where would we go?", soldier's horse per mission page), My Last Boy (war paint, Micah/Cleet/Joe stay, wounded brave, walkway, Sadie, Paytah, steam, abdomen, "as it should be", "You ran away"), "Red Dead Redemption" mission line to Sadie, wiki attributions (in his father's arms, burial, west/east of Donner Falls, gallery 1907, Annesburg encounter, credits in the Grizzlies East), "Pump Jacks Sit Silent" (No. 72, available after "The Wheel" = epilogue). All quotations in Personality, In his own words and Names are verbatim in gsw. Names (impetuous Prince, my last son, My only boy, son, this boy, my friend, brother, Aigle-Qui-Vole) all attested. No em or en dashes.

## Problems

1. **IMPRECISE** (FIX_RULES 2) - "In "A Rage Unleashed", Eagle Flies rides into Beaver Hollow escorted by Karen Jones and Javier Escuella. Arthur introduces him to Dutch". Source: gsw l. 12211 "Charles Smith: Pardon me for interrupting. I've brought a friend, Arthur." then Arthur: "Dutch, this is Eagle Flies..." (l. 12213); mission page: escorted by Karen and Javier. Charles's role is missing. Fix: "...escorted by Karen Jones and Javier Escuella. Charles brings him to Arthur, who introduces him to Dutch; Eagle Flies explains..."

2. **IMPRECISE** (wrong chapter) - "The press covers the conflict the same year. "Tensions High", an article of the Blackwater Ledger (No. 69)..." placed at the end of Chapter 4. Source: _m/Newspapers_Red_Dead_Redemption_2.txt: issue 8 (Blackwater Ledger No. 69) becomes available after "Visiting Hours" (chapter 6); No. 71 after "The King's Son". Fix: move the paragraph into Chapter 6 (e.g. before "A Rage Unleashed": "After John's rescue from Sisika, "Tensions High" (Blackwater Ledger No. 69) says..."), drop "the same year" or keep it there.

3. **IMPRECISE** - "On the way Eagle Flies asks to go back for the bodies of his men, and Paytah tells him to save his breath." Source: gsw l. 13270-13271: "Our men... we must go back for the bodies..." / Paytah: "We will. Save your strength."; "save your breath" comes later (l. 13294) when the dying Eagle Flies calls Paytah's name. Fix: "...and Paytah promises they will and tells him to save his strength. Near the reservation, when Eagle Flies calls his name, Paytah tells him to save his breath."

4. **IMPRECISE / SPECULATION** - "Rains Fall later confirms the sighting to Arthur in Saint Denis: he says he saw him with the wagon train crossing the river at Cumberland Falls." Source: gsw l. 9554 "We saw you on the wagon train... crossing the river at Cumberland Falls... and at the party, you were upstairs." It is "we", and nothing ties this crossing to the cliff scene of "Eastward Bound" (mission page: "After crossing a stream"; no place named). Fix: "In Saint Denis, Rains Fall tells Arthur that they saw him with the wagon train crossing the river at Cumberland Falls, and upstairs at the party."

5. **IMPRECISE** - "As the group heads to an appointment with officials, Eagle Flies calls it a waste of time". Source: gsw l. 9577 Miller: "that appointment with the senator". Fix: "an appointment with a senator" (as Personality already says).

6. **IMPRECISE** - "Arthur warns him that Dutch does not have Eagle Flies's interests at heart, and afterwards writes in his journal..." Source: Archeology_for_Beginners mission page: on the ride "Arthur can discuss Eagle Flies, or Dutch" (optional ride conversation; gsw l. 12360-12368). Fix: "On the ride, Arthur can tell him that he does not trust Dutch to have his son's best interests at heart".

7. **IMPRECISE** - "The English wiki places his grave on the western side of Donner Falls and says it can be found from the epilogue onward". The Red Dead Wiki pages disagree on timing: "Donner Falls" says "once the player has reached the epilogue"; "Paying Respects" (trophy page) lists "Eagle Flies - After "My Last Boy"". Eagle Flies's own page gives no timing. Fix: drop the timing, or "the wiki's pages differ on whether it is available after "My Last Boy" or only in the epilogue".

8. **IMPRECISE** - Personality: "and in captivity and in battle his concern is for his men". In captivity (gsw l. 13050-13083) he jokes, asks for the keys and a gun; no concern for his men is shown. Fix: "and in battle his concern is for his men: in Cumberland Forest he looks for Paytah, and at the oil fields..."

9. **STYLE** - "His father sees him differently from himself:" Awkward and empty. Fix: "His father describes him: ..." or start directly with the quote.

10. **STYLE** - Two consecutive paragraphs: "...In "The King's Son", Rains Fall tells Arthur that the Army holds his son..." / next paragraph "In "The King's Son", Arthur decides to free him..." Fix: merge: "In "The King's Son", Rains Fall tells Arthur that the Army will hang his son for treason. Arthur decides to free him despite the chief's refusal."

11. **STYLE** - Key facts: "He is played by Jeremiah Bitsui, known for the role of Victor in Breaking Bad, who provided his voice and motion capture." The relative clause attaches to Victor/Breaking Bad. Fix: "He is played by Jeremiah Bitsui (Victor in Breaking Bad), who provided both his voice and his motion capture."

12. **STYLE** (FIX_RULES 7) - Personality block (Personality + In his own words + Names + Appearance) is about 600 words; "He's a vile man..." is still there. Fix: cut "He's a vile man..." first (see 13), then trim the second Personality paragraph (see 18-20).

13. **DUPLICATE** (FIX_RULES 7) - In his own words: "On the ride, about Favours: "He's a vile man. He and his regiment take pleasure in persecuting us..."" Same content is in Biography ("Eagle Flies describes Colonel Henry Favours as a vile man whose regiment enjoys persecuting...") and in the Favours relationship ("...removal of the young to reform schools (see In his own words)"). Keep the Biography paraphrase; cut from In his own words; change the Favours relationship pointer to "(see Biography)".

14. **DUPLICATE** - Personality: "Rockstar's character descriptions of September 6, 2018 cover the Van der Linde gang and do not include Eagle Flies". Same sentence in Other media (full text l. 174). OWNERSHIP: official descriptions live in Personality. Keep in Personality, cut from Other media.

15. **DUPLICATE** (FIX_RULES 6) - In his own words lines repeated verbatim in Quotes: "Colonel Favours is a liar and a murderer..." (Quotes l. 131), "Sure... I enjoy being tortured... clears the mind." (l. 139), "They'll pay for this. They'll wish they killed me..." (l. 141), "Where would we go?" (l. 143), "Any men we see... we must save them." (l. 149), "Our men... we must go back for the bodies..." (l. 153). Keep in B, cut all six from Quotes (the Quotes intro even claims no repetition).

16. **DUPLICATE** (FIX_RULES 6) - Personality quotes "Told you, they're all mercenaries." and Arthur's "He's very brave... very angry. He's me."; Quotes repeats them (l. 120 and l. 156 "I know your son, a little. He's very brave... very angry."). Keep in B, cut both from Quotes.

17. **DUPLICATE** - In his own words quotes "Father has confused wisdom with weakness..."; the Rains Fall relationship quotes it too ("his father "has confused wisdom with weakness""). Keep in In his own words (FIX_RULES 6); paraphrase in the relationship.

18. **DUPLICATE** - Biography ch. 4: "according to the wiki's Camp Events page, Charles tells Arthur that Eagle Flies has asked him to rescue some Native children from a reform school; Charles turns down Arthur's offer of help." Same camp scene in the Charles relationship (l. 70), where it is "free members of the tribe being sent to a reform school". OWNERSHIP: camp scenes belong to Relationships. Keep in Charles relationship (and align its wording to Camp_Events.txt l. 350: "rescue some Native children from a reform school"); cut from Biography or reduce to a pointer.

19. **DUPLICATE** - Personality: "at the oil fields he will not leave until he has found them all". Told in Biography ("Eagle Flies refuses to leave until he has found all his men") and quoted in the Dutch relationship ("Until I find all my men, I'm not leaving."). Keep Biography; cut from Personality.

20. **DUPLICATE** - Personality: "when Arthur introduces him to Dutch, he says that Arthur and Charles did him a great favor" and "At the courthouse in Saint Denis he predicts that a new removal will lead to war, and he calls the family's appointment with a senator a waste of time". Both told in Biography; the first also quoted in the Arthur relationship, the second quoted in the Evelyn Miller relationship AND in Quotes (l. 122: "It's a waste of our time and his." appears twice). Keep in Biography; cut from Personality; keep the "waste of our time" quote in only one place (Quotes), paraphrase in Miller.

21. **DUPLICATE** - Biography Archeology passage (impetuous prince, "great disappointment to his son", "easily led") and Origins (brother killed by a drunken soldier, mother's throat slit) are retold in the Rains Fall relationship (l. 64-65). Keep in Biography; the relationship should point to it in one clause.

22. **COPIED** - My Last Boy paragraphs track the mission page wording. Draft: "Arthur agrees, followed by Charles, then Dutch and most of the gang" / wiki: "Arthur agrees, followed by Charles, then Dutch and eventually the rest of the gang". Draft: "Charles spots Eagle Flies fighting on a walkway. Arthur, Charles and Sadie Adler ride down with a few Wapiti to reach him while Dutch attacks from another side." / wiki: "Arthur and Charles soon spot Eagle Flies on the walkway, fighting. Arthur, Charles and Sadie ride with a small group of Wapiti Indians to rescue him, while the rest of the gang go with Dutch to attack the Army from a different angle." Draft: "a pipe bursts and sprays steam into Arthur's face" / wiki: "a pipe bursts and blasts steam into Arthur's face". Draft: "Eagle Flies bursts in and kills the soldiers" / wiki: "Eagle Flies bursts in and kills the soldiers in quick succession". Draft: "where he dies after a last moment with Rains Fall" / wiki: "Rains Fall has one last moment with his son". Fix: rephrase from the transcript (e.g. "Charles points him out crossing a walkway"; "a burst pipe knocks Arthur down and blinds him"; "Eagle Flies arrives and shoots the soldiers").

23. **COPIED** - "In "Favored Sons", Eagle Flies, Dutch, Paytah and a group of Wapiti warriors wait on a clifftop in Cumberland Forest." / wiki Favored Sons: "Arthur speaks with Dutch, Eagle Flies and a group of Wapiti warriors on a clifftop in Cumberland Forest." Fix: e.g. "Arthur finds Dutch, Eagle Flies and Paytah with armed Wapiti above a pass in Cumberland Forest."

### Cross-part errors noticed (half2, not counted)
- Arthur relationship: "On the way to rescue Abigail in "Our Best Selves", Arthur names him to Sadie..." WRONG: the line is in "Red Dead Redemption" (gsw l. 13457 heading, line at l. 13489), as the Biography and the Missions table say.
- Rains Fall relationship: "In the canoe after Fort Wallace, Eagle Flies says that there will be more trouble and that even his father may have to fight." It is on the shore after leaving the canoes (gsw l. 13086-13090), as the Biography says.

## Count per category
- WRONG: 0
- IMPRECISE: 8 (items 1-8; item 4 also SPECULATION)
- UNSUPPORTED: 0
- MISQUOTE: 0
- SPECULATION: 0 (see item 4)
- COPIED: 2
- DUPLICATE: 9
- STYLE: 4
