# Architectuur | centrale regels, projectcode lokaal

## Eén bron van waarheid

- `AGENTS.md`: projectoverschrijdende ontwerp- en codeerregels.
- `.agents/skills/*/SKILL.md`: gespecialiseerde workflows; activeer ze alleen bij de taak die ze nodig heeft.
- `CHATGPT.md`: compacte verwijzing voor ChatGPT-projectinstructies.
- `SOURCES.md`: herkomst en beperkingen van de verzamelde principes.

## Werkstroom

1. Haal waar mogelijk de nieuwste centrale instructies op.
2. Lees de relevante *eigen* projectrepo inclusief bestaand `AGENTS.md`, architectuur en workflows.
3. Kies passende skills, maak de kleinste correcte wijziging en test de hoofdgebruikersroute.
4. Maak een leesbare Git-commit of PR; verifieer deployment alleen wanneer gepubliceerd.

## Scheiding van verantwoordelijkheden

Deze repo bevat **geen** specifieke projectimplementaties, API-keys, builds, APK's, HTML-sites, grote datasets of automatische hooks. De daadwerkelijke website/Android/Python-code en haar feitelijke `ARCHITECTURE.md` blijven bij het betreffende project.

## Voorrangsregels

Expliciete opdracht en veiligheid > aantoonbare projectconstraints > centrale adviezen. Bij verschil tussen centrale skills en bestaande werkende projectstack: onderzoek en kies bewust in plaats van alles te herschrijven.

## Designcontract en risicocontrole

- `templates/DESIGN.template.md` is alleen een **optioneel** sjabloon voor een productgebonden `DESIGN.md`, geen centrale branding. Bestaand werkend design behouden tenzij redesign is gevraagd.
- UI: test werkelijke states en screenshots wanneer browser beschikbaar is; hoogstens drie betekenisvolle verfijningsrondes. Zonder screenshot geen claim van visuele verificatie.
- Docs/typo: gerichte check. Codegedrag: regressietest. Upload/auth/financiën: input-, negatieve en securitytests. Release: exact artefact, CI, rechten en doelomgeving.
- Veiligheid, privacy en toestemming prevaleren boven bondige code en optionele designpolish; toets specifieke skill-regels aan dit principe.
