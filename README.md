# Hessel Build System

**Centrale bron van waarheid** voor Hessel's AI-ontwikkelwerk: prachtige, snelle HTML-tools; veilige Python/Windows-automatisering; Android; GitHub-deployment en zo min mogelijk handmatige input.

## Gebruik

1. Lees bij iedere code- of ontwerpwijziging eerst de actuele [AGENTS.md](AGENTS.md).
2. Kies **alleen** de skills die bij de taak passen in [.agents/skills](.agents/skills).
3. Inspecteer vervolgens de daadwerkelijke projectrepo, hergebruik de bestaande stack en voer gerichte tests uit.
4. Publiceer uitsluitend wanneer gevraagd. Controleer het uiteindelijke resultaat, niet alleen of de build slaagt.

De bronbestanden in **deze repo** zijn leidend. Maak geen extra kopieën die onafhankelijk aangepast worden. Projectspecifieke feiten horen in de eigen projectrepo.

## Inhoud

| Bestand | Verantwoordelijkheid |
|---|---|
| [AGENTS.md](AGENTS.md) | Altijd geldende ontwikkelregels |
| [CHATGPT.md](CHATGPT.md) | Projectinstructies om in ChatGPT te gebruiken |
| [ARCHITECTURE.md](ARCHITECTURE.md) | Hoe de centrale instructies en projectcode samenwerken |
| [SOURCES.md](SOURCES.md) | Geselecteerde upstream-projecten |
| [beautiful-html](.agents/skills/beautiful-html/SKILL.md) | Premium HTML, CSS, UX en motion |
| [lean-code](.agents/skills/lean-code/SKILL.md) | Minimale begrijpelijke code |
| [security-first](.agents/skills/security-first/SKILL.md) | Browser-, data-, Windows- en APK-beveiliging |
| [debug-verify](.agents/skills/debug-verify/SKILL.md) | Oorzaak vinden en echte tests draaien |
| [clean-deployment](.agents/skills/clean-deployment/SKILL.md) | GitHub Actions en releases |
| [visual-diagrams](.agents/skills/visual-diagrams/SKILL.md) | Interactieve en statische HTML/SVG-schema's |
| [dashboard-storytelling](.agents/skills/dashboard-storytelling/SKILL.md) | KPI-hiërarchie, correcte groeicijfers, grafiekselectie, interactie en data-QA |

## ChatGPT (aanbevolen)

Plaats de korte instructie uit [CHATGPT.md](CHATGPT.md) in je ChatGPT-projectinstructies. Hierdoor weet ChatGPT **welke GitHub-bron eerst te openen**; een link alleen wordt niet automatisch bij iedere nieuwe chat gelezen.

## Andere AI-codeeragents

Voor Codex-compatibele agent-skills is `.agents/skills/` de canonieke locatie. Een andere tool kan de skills via een eigen pad of expliciete verwijzing laden. Kopieer niet blind naar alle agents; kies één centraal beheerde bron en controleer wat de gebruikte agent ondersteunt.

## Principes

- **Design hoort bijzonder te zijn; code hoeft niet ingewikkeld te zijn.**
- Native HTML/CSS/JS en Python-stdlib eerst, frameworks alleen met reden.
- Echte werking vóór mooie mockups, security nooit wegoptimaliseren.
- Eén werkende, gecontroleerde implementatie in plaats van tien onafgemaakte opties.
- Bij destructieve wijzigingen eerst herstelbaarheid vastleggen.

Dit zijn eigen, compacte richtlijnen geïnspireerd op externe repos, geen installaties van die plugins. Zie [SOURCES.md](SOURCES.md).
