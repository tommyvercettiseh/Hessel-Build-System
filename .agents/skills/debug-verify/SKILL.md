---
name: debug-verify
description: Reproduce a bug, find root cause, implement minimal safe fix, add a targeted regression test and verify related flows.
---

# Debug & Verify

1. Definieer het werkelijk gemelde defect en de gebruikersroute die stukgaat.
2. Maak een kleine herhaalbare check die vóór de fix faalt op exact het defect.
3. Volg alle relevante callsites, grenzen, mogelijke aannames en bestaande testuitvoer.
4. Repareer het gedeelde probleem waar het ontstaat, niet alleen het zichtbare symptoom.
5. Herhaal dezelfde check en controleer naburige routes; onderscheid uitgevoerd van niet getest.

## Gerichte checks

- HTML/media: file-open, drop, metadata, `play()`, audio, IN/OUT-positie, export, foutmeldingen, mobiel en console.
- Windows/PowerShell: quoting, encodings, newline, paden met spaties, ontbrekende directories en rechten.
- Python: leeg bestand, grote bestanden, onverwacht formaat, kopie versus delete, correcte paden.
- Excel/Power BI: typen, locale, percentages, nulls, duplicaten en referentieformules.
- CI: syntax, bouwartefact, testlog en werkelijke deploy.

Geen zware testharness wanneer één assert of kleine browsertest volstaat.

Bronideeën: Matt Pocock diagnosing-bugs en Superpowers.

## Aanvullende kwaliteitschecks

- Visuele wijzigingen: controleer indien mogelijk screenshots van het echte scherm, devicebreedtes en states; zonder uitvoeromgeving geen geslaagde screenshottest claimen.
- Securitytests: aantonen dat het nieuwe regressiescenario zonder fix daadwerkelijk kan falen; groene maar verkeerd geformuleerde tests tellen niet als bewijs.
- Houd onderzoek, implementatie en validatie minimaal maar voldoende en schaal op bij grotere risico's.

Bronidee: Claude Vibe Skills `QUALITY_REFERENCE.md`.
