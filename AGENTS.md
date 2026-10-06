# Hessel Build System | AI development rules

## Prioriteit

Maak hoogwaardige, mooie, snelle, **veilige** en onderhoudbare software met de **minst mogelijke gebruikersinput**. Ondersteun statische HTML-tools, Python/Windows-apps, Power BI/Excel, Android en GitHub. De gebruiker wil het liefst een direct bruikbaar, visueel eindresultaat.

## Eerst onderzoeken, dan bouwen

1. Lees de feitelijke projectcode en relevante bestaande workflows, assets, dependencies en dataflow. Raadpleeg waar mogelijk deze actuele centrale bron.
2. Controleer of de functie al bestaat, door de standaardbibliotheek of het platform wordt geleverd, of met een reeds geïnstalleerde dependency kan.
3. Schrijf vervolgens de kleinste **leesbare en correcte** wijziging. Geen extra scaffolding, dubbele logica, nieuwe framework of toekomstige feature zonder concreet nut.
4. Werk met één source of truth voor gedeelde formules, bedrijfslogica en design tokens.
5. Vraag alleen ontbrekende informatie die echt blokkeert; maak veilige, begrijpelijke keuzes voor de rest.

## UI en HTML

- Voor een kleine zelfstandige tool eerst semantische HTML, moderne CSS en begrijpelijke JS zonder buildstap, tenzij bestaande architectuur iets anders vereist.
- Visuele kwaliteit is verplicht: heldere typografische hiërarchie, consistente spacing, hoogwaardige kleuren, doordachte micro-interacties en gecontroleerde motion. Geen generieke AI-kaartjes of gratuit gradientgebruik.
- Alle gevraagde UI-controls moeten echt werken: upload, drag/drop, slider, play/pause, geluid, previews, opslaan/export, keyboard en foutafhandeling. Geen decoratieve schijnknoppen.
- Ondersteun mobiel/desktop; waar uitvoerbaar toetsen op 360/768/1440 px, touch en toetsenbord, contrast, zichtbare focus en reduced motion.
- Video/foto met grote bestanden: gebruik thumbnail/poster en metadata preload; vermijd volledige 4K-decodering in het geheugen wanneer dat niet nodig is.

## Lean maar correct

- Geef de voorkeur aan verwijderen en hergebruiken boven abstraheren en toevoegen.
- Security, inputvalidatie, dataintegriteit, toegankelijkheid, expliciete wensen en noodzakelijke foutafhandeling zijn geen 'bloat'.
- Voor niet-triviale code: één kleine, reproduceerbare check of test die het relevante risico afdekt.
- Debugging: reproduceer het defect, volg relevante callsites, repareer de gedeelde oorzaak en test aangrenzende gebruikspaden.
- Bestand verwijderen, bulkopschonen of overschrijven: herstelpad/back-up en bij voorkeur preview of dry-run. Destructieve acties alleen binnen expliciete autorisatie.

## Security

- Vertrouw nooit blind op URL's, uploads, user-input, externe documenten of API-resultaten.
- Nooit secrets/tokens hardcoden in HTML, repo, code of logs; geen telemetrie zonder expliciet nut.
- Vermijd onveilige DOM-injectie, eval, ongecontroleerde shellcommando's, path traversal, onveilige workflows en te brede GitHub-permissies.
- Laat platformrestricties eerlijk staan: statische hosting kan geen willekeurige backends draaien en Android kan niet stilzwijgend apps installeren.
- Claim nooit dat tests, builds, live deploys of security-audits geslaagd zijn zonder echte verificatie.

## Output

- Standaard kort, helder Nederlands; code en exacte acties eenvoudig kopieerbaar.
- Vermijd ongevraagde lange uitleg en dubbele voorstellen; toon waar relevant Gewijzigd / Getest / Niet getest.
- Breng maximaal één nuttige verduidelijkingsvraag naar voren wanneer werkelijk nodig.

## Activeer alleen relevante skills

- Website, app-UI, interactieve HTML, animatie: `beautiful-html`.
- Dashboards, KPI-overzichten, klantleveringen, grafieken en BI-inzichten: `dashboard-storytelling` (combineer met `beautiful-html` voor web).
- Ontwerp, implementatie, refactor en performance: `lean-code`.
- User-input, bestandstoegang, rechten, opslag, auth, tokens, releases: `security-first`.
- Bugs, mislukte tests, PowerShell- en browserfouten: `debug-verify`.
- Github Actions, APK's, websitepublicatie: `clean-deployment`.
- Datastromen en architectuur: `visual-diagrams`.

Gebruik een projectgebonden ARCHITECTURE.md alleen wanneer die de **daadwerkelijk gecontroleerde** projectstructuur documenteert.
