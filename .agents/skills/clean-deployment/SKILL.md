---
name: clean-deployment
description: Minimal safe CI and release workflow for GitHub Actions, website hosting, Python apps and Android artifacts with true build and live verification.
---

# Clean Deployment

1. Inspecteer eerst huidige repo, default branch, tests, build, Actions, tokens/secrets, DNS, hosting en publicatiewijze.
2. Hergebruik een bewezen werkende workflow. Kies de kleinste wijziging, niet automatisch migreren of volledig herstructureren.
3. Test syntax, code, inputvalidatie en build. Controleer bij HTML ook assetpaden, netwerk en console; bij APK signatuur en artefact.
4. Beperk workflowpermissies, scherm secrets af en zorg dat release vanaf vertrouwde commits komt.
5. Commit of push alleen als expliciet gevraagd en geautoriseerd; test daarna de echte URL/release wanneer bereikbaar.

- Een groene GitHub Actions-run betekent **niet** automatisch dat de website live is.
- Houd herstelfuncties via commit/backup-ref, en verifieer dat releases terug te draaien zijn.
- Android kent platformbeperkingen en toestemming voor installaties: beloof geen stille updates.
- Nieuwe dependencies of workflows zijn alleen gerechtvaardigd als ze aantoonbaar fouten of handwerk verminderen.

**Verslag:** Gewijzigd, Getest, Build, Gepubliceerd, Live geverifieerd/niet getest.

Bronideeën: Addy Osmani ci-cd-and-automation.
