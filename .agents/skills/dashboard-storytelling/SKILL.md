---
name: dashboard-storytelling
description: Maak minimalistische, interactieve en analytisch kloppende HTML-, Excel- en Power BI-dashboards met zinvolle KPI's, grafiekkeuze, dataconsistentie, vergelijkingen en drill-down.
---

# Dashboard Storytelling | van data naar beslissing

## Wanneer activeren
Gebruik bij dashboards, KPI-overzichten, voorraad- en klantleveringsanalyses, verkoop- en forecastoverzichten, interactieve grafieken en tabellen. Combineer bij een HTML-implementatie met `beautiful-html`; voor businesslogica met `lean-code`, `security-first` en zo nodig `debug-verify`. Dupliceer hun implementatieregels niet.

## Eerst bepalen: welke vraag beantwoordt het scherm?
1. Benoem **één beslissing** die de gebruiker wil nemen, bijvoorbeeld: welk artikel loopt achter, welke klant heeft voorraadtekort, wat groeit ten opzichte van vorig jaar?
2. Kies maximaal **vijf belangrijke inzichten**. Laat irrelevant beschikbare velden weg.
3. Bepaal de korrel van de data: orderdatum, leverdatum of factuurdatum; artikel, klant, land, week of maand; stuks, dozen of pallets; bruto/netto; tijdzone en boekjaar.
4. Toon een **eerste overzicht in één blik** (richtlijn: binnen drie seconden te scannen); ontsluit verdieping via selectie of drill-down, niet door elke metriek in het eerste scherm te proppen.
5. Maak expliciet of cijfers demo, schattingen, forecast of echte brongegevens zijn. Verzin nooit aantallen, percentages of correlaties.

## Visuele hiërarchie en layout
- Gebruik de natuurlijke leesrichting: belangrijkste informatie linksboven, dan trend, vergelijking en uitzondering. F- en Z-scanpatroon zijn hulpmiddelen, geen rigide raster.
- Boven: klant/periode/meettype en hoogstens 3-5 relevante KPI's (bijv. geleverd YTD, groei versus vergelijkbare periode, afwijking op forecast, risicovoorraad).
- Midden: **één dominante analyse**. Daaronder of ernaast een ranglijst met exacte waarden en compacte sparklines.
- Onder: context, verklaringen en drill-down. Geef filters en kaarten veel witruimte; geen sierkaarten om ruimte op te vullen.
- Verhoudingen: één hoofdkleur, rustige achtergrond, spaarzaam accent; consistente typografie, dimensies en decimalen. Geen 3D-grafieken of dual-axis om cijfers mooier te maken.

## Grafiekselectie: betekenis boven variatie
| Vraag | Voorkeursvisual | Vermijd |
|---|---|---|
| Hoeveel per artikel? | Gesorteerde horizontale staaf | Taartdiagram met 7+ segmenten |
| Wat verandert per maand? | Lijn voor enkele series, kolommen voor totaal | 7 kruiselings overlappende lijnen zonder focus |
| Vergelijk 7 artikelen door het jaar | Kleine veelvouden of selecteerbare series | Spaghetti-grafiek zonder selectie |
| Welke maand/artikel is opvallend? | Heatmap maand × artikel, met aantallen in tooltip/tabel | Kleur zonder legenda en eenheid |
| Welk aandeel levert een artikel? | 100% gestapelde balk bij aandeel; absolute stapeling voor volume | Procentmix presenteren als aantal |
| Wat wijkt af van target/forecast? | Bullet chart, staaf met targetmarker of variantie | Snelheidsmeter zonder informatiewaarde |
| Welke artikelen stijgen versus vorig jaar? | Gesorteerde groeibalk of slopegraph; altijd met absolute aantallen | Enkel groen/rood percentage zonder context |
| Details en controles | Sorteerbare tabel met echte waarden | Kleine cijfers verbergen in uitsluitend hover |

- Label grafieken direct waar dat leesbaar is; gebruik stabiele artikelkleuren over alle schermen. Kleur nooit als enige onderscheid.
- Vergelijkingen beginnen bij nul voor kwantitatieve bars; snijd assen niet om groei te overdrijven. Bij line charts kan een niet-nul-as soms verdedigbaar zijn, mits duidelijk.
- Voor seizoenartikelen Kerst/Sint: laat echte seizoenspatronen zien en vermijd gemiddelden die nulmaanden ten onrechte als slechte prestaties framen.

## Interactie (echt werkend)
- Filters voor jaar, klant, artikel, meettype; zet actief filter zichtbaar neer en bied reset.
- Een keuze in grafiek beïnvloedt **alle gekoppelde KPI's, tabellen en grafieken** vanuit dezelfde gefilterde dataset, tenzij expliciet 'globaal totaal' staat.
- Ondersteun toetsenbord, touch, niet-hover drill-down, zoeken, sorteren, toegankelijke legenda en zichtbare selectie.
- Tooltips geven exacte waarde, maand, eenheid en vergelijkingsbasis; tooltips zijn geen enige bron van essentiële informatie.
- Exports (CSV/Excel) weerspiegelen de huidige filters en gebruiken brongetrouwe waarden, niet afgeronde schermteksten.
- Laat bron, bijwerkdatum, datadekking en berekeningsdefinities eenvoudig terugvinden.

## Datacontrole: **harde kwaliteitsgate**
1. **Reconciliatie:** som van 7 artikeltotalen = KPI totaallevering = som van alle 12 maanden (voor dezelfde filters, meeteenheden en periode). Hanteer geen handmatig getypte KPI's naast grafiekdata.
2. **Groei:** YoY = (huidige periode / vergelijkbare vorige periode - 1) × 100%; bij 0/ontbrekende basis: 'n.v.t.' met context, niet 0%, 100% of oneindig.
3. **Vergelijk vergelijkbaar:** YTD met vorige YTD tot dezelfde afsluitdatum, boekjaar met boekjaar; onderscheid complete maanden van onvolledige lopende maanden.
4. **Gemiddelde groei:** vermeld of deze gewogen is. Totale groei uit som volumes is iets anders dan ongewogen gemiddelde van artikelgroeipercentages.
5. **Definities:** bestellingen, uitleveringen, verkopen, omzet, voorspelling en voorraad zijn verschillende metrieken. Gebruik nooit onzichtbaar door elkaar.
6. **Transformaties:** sorteren/filteren, lege maanden, dubbele artikelcodes, ontbrekende weken, retouren/correcties, eenheidsconversie (dozen → stuks), negatieve hoeveelheden en nulls testen.
7. **Claims:** 'best lopend', 'meest stabiel', 'piekmaand' en 'grootste groeier' uitsluitend berekenen uit brondata en de bijbehorende definitie (bijv. variatiecoëfficiënt bij stabiliteit).
8. Voeg ten minste één geautomatiseerde check toe die **zichtbare KPI's versus onderliggende aggregaties** vergelijkt. Voor demo-afbeeldingen: label fictieve data en verifieer intern alle getoonde cijfers.

## Specifiek voorbeeld: 7 klantartikelen over 12 maanden
Een bruikbare eerste weergave voor jaarleveringen:
- Filterbalk: klant, boekjaar, artikel, aantallen/dozen/pallets.
- Vier KPI's: Totaal geleverd YTD; YoY % op vergelijkbare periode; grootste volumeverandering; afwijking op forecast (alleen als forecast bestaat).
- Hoofdgrafiek: maandelijks totaal (kolom) met vorig jaar als subtiele vergelijkingslijn, óf heatmap voor 7 artikelen × 12 maanden.
- Rechterpaneel: 7 gesorteerde artikeltotalen met YoY, absolute verandering, sparkline en selectiemogelijkheid.
- Selecteer één artikel voor detail: maandprofiel, seizoenseffect, levering versus forecast, voorraaddekking in weken indien beschikbaar.
- Voor klanten met seizoenspieken of zes weken voorraadvereiste: markeer werkelijke risico's en geplande DC-start uitsluitend als de bron die informatie bevat.

## Acceptatiecheck vóór oplevering
- Kan iemand in 3 seconden zeggen 'wat gaat goed, wat valt op en waar moet ik kijken'?
- Hebben alle grafieken een periode, correcte eenheid en betrouwbare basis voor vergelijking?
- Werken de filters, hover/tap, keyboard, selectie, export en reset die getoond worden?
- Kloppen KPI's, tabellen en grafieken exact met dezelfde gefilterde brongegevens?
- Ziet het er premium en rustig uit op 360, 768 en 1440 px, inclusief lege en grote datasets?
- Geen onbewezen claim over performance, toegankelijkheid, live data of succesvolle tests.

## Referenties
- [Justinmind dashboard design best practices](https://www.justinmind.com/ui-design/dashboard-design-best-practices-ux): doelgroep, dashboardtype, leesvolgorde, terughoudendheid en interactiviteit.
- [Nielsen Norman Group: Choosing chart types, consider context](https://www.nngroup.com/articles/choosing-chart-types/): context, contrast en cluttervrije visualisatie.
- [Nielsen Norman Group: Data Tables, four major user tasks](https://www.nngroup.com/articles/data-tables/): relevante kolommen naast elkaar, filters en vergelijkingen.

Deze skill is een eigen praktische synthese en geen gekopieerde tekst of pluginimplementatie.
