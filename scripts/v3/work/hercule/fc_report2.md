# Fact-check report: Hercule Fontaine, chunk half2.txt (Relationships, Smuggling and fighting, Missions, Quotes, Development and performance, Reception, Other media, Trivia)

## Sources used
- Fan transcript, Game Scripts Wiki (fc/gsw.txt), lines 10470-11027: "Welcome to the New World", "Savagery Unleashed", "A Kind and Benevolent Despot", "Hell Hath No Fury", "Paradise Mercifully Departed".
- Red Dead Wiki: en.txt / fr.txt (Hercule), _m/Welcome_to_the_New_World.txt, _m/Hell_Hath_No_Fury.txt, _m/Paradise_Mercifully_Departed.txt, _m/Baptiste.txt, _m/Leon_Fuentes.txt, _m/Captain_C.txt, _m/Guarma_Rebels.txt, _m/Guarma.txt, _m/Red_Dead_Redemption_2_Cut_Content.txt.
- Wikipedia "List of Red Dead Redemption 2 characters", fetched live via the API on 22 Oct 2026 (and fc/wp_list_rdr2_hercule_line.txt).
- WhatCulture, Dustin Crawford, June 16, 2020, fetched live on 22 Oct 2026 (and fc/whatculture_2020-06-16.txt).
- scripts/v3/sources/thr_descriptions.txt (no "Hercule" in it), FIX_RULES.md, hercule_A..D docstrings, hercule_full_en.txt (for DUPLICATE checks).

## Verified OK
**Voice credit:** confirmed. The live Wikipedia list reads "Guarman rebellion leader Hercule Fontaine (Guyviaud Joseph)". The reference `<ref name="Credits">` is a `{{cite video game}}` of Red Dead Redemption 2 (Rockstar Games, October 26, 2018), so "which cites the game's credits" is accurate. The Red Dead Wiki gives the same credit in English (`voice = [[Guyviaud Joseph]]`) and in French (`acteur = [[Guyviaud Joseph]]`). The wiki also credits Babs Olusanmokun for Baptiste and Andhy Méndez for Leon.

**WhatCulture item:** confirmed live. The author is Dustin Crawford and the date is June 16, 2020. Both quotes are verbatim: "an interesting character" and "Haitian-born freedom fighter leading a revolt" (the source sentence goes on "against the Leopold-esque Colonel Fussar"). "After the fall of Fussar's regime" is a fair paraphrase of "after the collapse of Fussar's regime". Note for the lead: "Haitian-born" is WhatCulture's own wording, in quotation marks and attributed to the article. It does not state a nationality as fact, so it does not break FIX_RULES 3.

**Other checks:**
- Every quotation in the Quotes block matches the transcript word for word (curly apostrophes and the ellipsis character normalized). This covers the "Almost certainly..." line (gsw 10706) and Arthur's "this Hercule feller" line (10705).
- Relationship quotes match: the Bill/Hercule exchange, the Micah exchange, "Nice island"/"It's not my island", "Hercule, we follow you.", "great pleasure".
- Mission givers match the mission pages: Dutch for Welcome to the New World, Hercule for Hell Hath No Fury, Bill for Paradise Mercifully Departed.
- The mission-fail condition matches the Welcome to the New World page, as do the kill lists of all three missions.
- These items all check out: the score track (Part II), the magazine trivia, the fast run, Captain C. among Hercule's followers, the random encounter, Red Dead Online (inaccessible; rank 59 of the third Outlaw Pass), the rifles in the infobox, Baptiste's $450 and missing arm, and Leon as "a member of the rebel faction led by Hercule Fontaine" (Leon page).
- Every cut-content item matches the Cut Content page: the unused coat, the horse fail text, the wagon records for PMD, "smg1"/"Smuggler1" with Leon's niece (cut dialogue: Arthur and Bill help her off the island), and Senor Andreas Colon's trousers.
- The THR article has no entry for Hercule.
- "En allez" and "connards" are verbatim.
- Micah and Bill guarding the cannon matches the HHNF page and "We'll guard this thing!".
- The cannon (not a machine gun) follows the mission page, per the A/B docstrings.
- Arthur killing Fussar with the cannon follows HOUSE_FACTS.

## Problems

1. **DUPLICATE (Quotes block vs Relationships / "In his own words")**: FIX_RULES 5 says lines quoted in part B must not be quoted again in part C. Seven Quotes entries repeat lines already quoted:
   - "It's not my island." (also in Relationships, Arthur)
   - "I don't see you have any choice..." (also in In his own words)
   - "I am! What do you want me to do? We are trapped up here!" (also in Relationships, Bill)
   - "We'll be like you... long gone by morning." (also in In his own words)
   - "Almost certainly, but he's the best chance..." (Relationships, Dutch, quotes "Almost certainly")
   - "He's using us!" (also in Relationships, Micah)
   - "Hercule... it was a great pleasure to make your acquaintance." (also in Relationships, Dutch)

   Fix: delete these 7 entries from Quotes and keep them in part B. To refill the block, use the C-owned lines listed in hercule_B's docstring, all verbatim in gsw:
   - "Okay. Well, Fussar will be desperate to find you. We must be very careful."
   - "Leon wants the people to stand up to Fussar... but most are too afraid."
   - "But, if we can silence him... then I can help you escape before anyone has time... to get here from America. That way, we all get what we want."
   - "So now we have a real problem. This must be the boat he called in from Cuba."
   - "Oh, they'll be back... but, I found a boat for you... and he should be arriving on the dock anytime now."
   - "Gentlemen, goodbye."

2. **DUPLICATE (Trivia)**: "In 'Welcome to the New World', the mission fails if the player attacks or kills Hercule or Leon Fuentes." The same fact is in Smuggling and fighting ("In 'Welcome to the New World', the mission fails if the player attacks or kills Hercule or Leon."). Fix: OWNERSHIP says trivia only holds what is nowhere else, but this is not a skill, so keep it in Trivia and delete the sentence from Smuggling and fighting.

3. **DUPLICATE + COPIED (Trivia / Fighting)**: the fast run back to the roof appears twice.
   - Fighting: "The Red Dead Wiki notes that in 'Hell Hath No Fury' he runs very fast on the way back up to the roof, along a path with sharp turns and drops, and advises players to follow him on the mini-map."
   - Trivia: "The Red Dead Wiki notes that Hercule runs very fast on the way back up to the roof of Cinco Torres, along a path with sharp turns and drops, and that the player can easily lose sight of him."
   - The wiki (HHNF Trivia) says: "Hercule runs very fast when he and Arthur are sprinting back up to the roof to use the cannon, as the path he takes involves several sharp turns and drops and it is very easy to lose track of him in the bushes."

   Fix: keep one occurrence (Trivia) and delete the Fighting one. Reword away from the wiki's wording, e.g. "According to the Red Dead Wiki, Hercule is hard to keep up with on the climb back to the roof of Cinco Torres, because his route twists and drops through the undergrowth."

4. **DUPLICATE (Trivia)**: "He switches to French several times during the fighting: a few exclamations, an order to move on and an insult aimed at the soldiers." This repeats the Languages paragraph item by item ("swears in French", "En allez", "connards"). Fix: delete it from Trivia.

5. **DUPLICATE (Other media)**: "Hercule appears only in Red Dead Redemption 2." The same is said in Development ("Hercule Fontaine appears only in Red Dead Redemption 2 (2018), in chapter 5."), and the intro says it implicitly. Fix: keep it in Development and start Other media with the THR sentence.

6. **DUPLICATE (Smuggling paragraph vs Biography, Origins + Key facts)**: "Hercule describes himself as a smuggler who moves goods on and off the islands without Fussar's knowledge... He and his men use the old fort of Cinco Torres as a hideout whenever they are on Guarma... he leads the group to an old building where he says he has guns stashed... he tells Dutch about the cave below the cliffs." Every one of these facts is already in the Biography Origins paragraph and the Key facts, and the cave is also in the Biography and in Relationships (Javier). Fix: cut Smuggling down to what is not told elsewhere: the wiki occupations "revolutionary and smuggler", and his being the only one who can arrange a boat. Point to Biography for the rest.

7. **DUPLICATE (Fighting vs Biography and Relationships, Arthur)**: "At Cinco Torres he readies the fort's cannon, tells Arthur to take the shotgun before going down to the beach, shoots a soldier who is running at Dutch, and keeps the cannon supplied with shot while Arthur aims at the warship." All four facts are in the Biography (HHNF paragraphs), and the cannon/shot is also in Relationships (Arthur). Fix: shorten to "He fights at Cinco Torres and at the gun positions (see Biography)", or keep only the shotgun line if a fighting example is wanted.

8. **DUPLICATE (Relationships, Dutch, para 1)**: "Dutch gives his name and the names of Micah, Bill and Arthur after the escape, and asks whether Hercule can be trusted; Hercule answers that they have no choice. Dutch accepts the deal, a boat in return for their help." This repeats Biography paragraphs 3-4 almost line for line, and "In his own words" quotes the same answer. OWNERSHIP gives events to the Biography. Fix: reduce it to one pointer clause (e.g. "Dutch makes the deal with him after the escape (see Biography)") and keep the relationship-specific "Almost certainly" judgment.

9. **DUPLICATE (Relationships, Arthur, para 2)**: "Arthur helps Hercule push the cannon into position; on the beach, when Arthur sends Dutch to cover the left, Hercule says he will follow Arthur. Back on the roof, Arthur fires the cannon while Hercule brings the shot, and the warship sinks." This restates the Biography HHNF paragraphs (and item 7). Fix: keep "Hercule says he will follow Arthur" (relationship-specific) and point to Biography for the cannon.

10. **DUPLICATE (Relationships, Javier)**: "Hercule tells Dutch that if he is still alive, he will be held at Fussar's compound, and points him to the cave that leads there". This is a third telling of the cave (Biography para 4; Smuggling). Fix: keep it in the Biography and leave only the "(see Biography)" pointer here.

11. **DUPLICATE (Relationships, Baptiste / Leon / ship's captain / Fussar)**: these entries restate Biography facts almost verbatim:
    - Baptiste: "Hercule is lining up a boat... gives him money... 450 dollars", which is Biography para 5.
    - Leon: "explains Fussar's rule... Hercule adds that Leon wants the people to rise", which is Biography para 3.
    - Captain: "he has found a boat... captain should reach the dock... Micah goes to meet him... Fussar's men seize the captain", which is Biography HHNF/PMD.
    - Fussar: "Fussar knows who the gang are and has called in the navy from Cuba", which is Biography HHNF.

    Fix: trim each to its identity line plus the relationship-specific detail (Baptiste: "I work with Hercule" and the wiki's "smuggler working with Hercule"; Leon: the wiki's faction line; Captain: the Red Dead Wiki says Hercule engaged him; Fussar: they never speak on screen), each with "(see Biography)".

12. **IMPRECISE (Relationships, Javier)**: "Javier is shot in the leg and captured as the group flees the ambush led by Hercule." Per the transcript (gsw 10541-10545), the ambush succeeds. The group is fleeing the soldiers' reinforcements when Javier is shot ("Damn... reinforcements", then Javier falls). Fix: "Javier is shot in the leg and captured as the group, led by Hercule, flees the soldiers' reinforcements after the ambush."

13. **IMPRECISE (Languages)**: "He speaks English with the gang and French with his men." The transcript shows only one rebel addressing him in French ("Rebel in French: Hercule, Hercule, please... quick, quick."). Hercule's own French lines are exclamations and calls to everyone: "My God", "Run, run" in WttNW; "Take that, asshole", "Shit" in HHNF; "En allez" said to the gang. Nothing shows him speaking French to his men. Fix: "He speaks English with the gang; a rebel calls to him in French, and he lapses into French in exclamations during the fighting."

14. **IMPRECISE (Reception)**: "noting that the Cuban Navy's involvement left room for international conflict." The source (WhatCulture, live) says: "The fact that the Cuban Navy got involved with the conflict means that there's potential for international involvement." Fix: "noting that the Cuban Navy's involvement opened the door to foreign involvement on the island."

15. **IMPRECISE (Development)**: "According to the Red Dead Wiki, the two other named rebels are voiced by Babs Olusanmokun (Baptiste) and Andhy Méndez (Leon Fuentes)." "The two other named rebels" claims these are the only named rebels, which no source states (the cut-content page names other Guarma characters, e.g. Emanuel). The voice credits themselves are correct (Baptiste.txt `voice = [[Babs Olusanmokun]]`; Leon_Fuentes.txt `voice = Andhy Méndez`). Fix: "According to the Red Dead Wiki, Baptiste is voiced by Babs Olusanmokun and Leon Fuentes by Andhy Méndez."

16. **STYLE (Reception)**: "Hercule has drawn little press attention." This is an evaluative opener based on an absence of search results (hercule_D docstring: "Searched without result"). Fix: delete it and start with "In a WhatCulture list of single-player expansions published on June 16, 2020, ...".

## Count per category
- WRONG: 0
- IMPRECISE: 4 (items 12, 13, 14, 15)
- UNSUPPORTED: 0
- MISQUOTE: 0
- SPECULATION: 0
- COPIED: 1 (item 3)
- DUPLICATE: 11 items (1-11; item 1 covers 7 quote lines)
- STYLE: 1 (item 16)
