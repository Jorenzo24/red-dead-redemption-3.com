# Drafting spec: full reference character fiche (red-dead-redemption-3.com)

You draft ONE PART of a character profile (EN + FR). Goal: our site must be the most exhaustive AND reliable reference on Red Dead Redemption characters. Use the Red Dead Wiki page as the structural and factual base and cover EVERYTHING it says in your assigned part that is not speculation, then ADD verified facts from other sources if you have them. Your part must be AT LEAST as long as the matching wiki sections (word count targets are given).

## Facts
- Game content (what happens in a mission, what a character says or does, outfits, items, mechanics) described by the wiki is ALLOWED, provided nothing contradicts it. Cross-check with the wiki's mission transcripts (`<Mission>/dialogues` pages) when in doubt. Mission pages beat the character page when they disagree.
- EXCLUDE interpretation, speculation, fan theories, "it is implied that", "possibly", rumours. If two sources contradict each other, give both versions explicitly or leave it out.
- Keep consistent with the fact-checked fiches (scripts/fiches/parts/john_*.py, arthur_*.py): their corrections are authoritative.
- Real-world facts (interviews, reviews) need the outlet/date named in the text.
- Quotation marks only around words checked against a transcript or the wiki's quote pages; otherwise paraphrase.

## Writing rules (strict)
- NEVER copy or closely paraphrase the wiki's sentences. Rewrite from the facts in your own words and structure. The wiki is CC BY-SA; copied text is forbidden.
- Neutral, factual media tone. One fact per sentence where possible. No mood-setting, no "poetic" prose, no cheap analysis, no rhetorical flourishes.
- No em dashes or en dashes anywhere. Use commas, colons, parentheses.
- Mission titles stay in English exactly as Rockstar titles them, in straight double quotes inside text: \"Mission Title\" (escaped inside Python strings).
- FR is WRITTEN natively in French (not a literal translation): natural phrasing, French typography (espace avant : ; ? !), "Saint-Denis" in French, "Saint Denis" in English. No « » inside headings (h3/h4).
- Character links: write [[slug|Visible name]] ONLY for slugs in the live slugs list given. Other characters: plain text.
- Links to story guides: only through h4 blocks with a "chapter" key.

## Output format
A Python file containing:

```python
def two(en, fr): return {"en": en, "fr": fr}
BLOCKS = [
    {"h3": two("Heading EN", "Titre FR"), "year": "1899"},      # "year" on biography period h3 ("" hides the year strip)
    {"h4": two("Chapter 1: Colter", "Chapitre 1 : Colter"), "chapter": 1},   # keys: 1-6, "E1", "E2", "A1", "A2", "A3"
    {"p": two("Paragraph EN.", "Paragraphe FR.")},
    {"ul": [two("item EN", "item FR"), ...]},
    {"table": {"head": [two("Col","Col"), ...], "rows": [[two("cell","cellule") or "plain string", ...], ...]}},
    {"quotes": [{"q": two("original English quote", "same original English quote"), "src": two("Mission (RDR2, chapter 6)", "Mission (RDR2, chapitre 6). Traduction : « traduction française »")}]},
]
```
- Valid Python (check with `python3 -c "import ast;ast.parse(open(PATH).read())"`). Escape inner double quotes as \".
- Paragraphs: 60-180 words each. h3 for sub-sections, h4 for chapters/periods.
- Reply with EN/FR word counts and the facts you deliberately excluded, with a one-line reason each.
