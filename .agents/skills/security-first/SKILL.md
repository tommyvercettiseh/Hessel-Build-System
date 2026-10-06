---
name: security-first
description: Risk-based security for DOM, uploads, file operations, APIs, credentials, dependency chains, CI releases, finance data and Android apps.
---

# Security First

1. Inventariseer trust boundaries: URL, user-input, browser, API, files, shell, opslag, auth, Actions en release.
2. Zoek concrete manieren waarop onbetrouwbare data naar DOM/shell/files of credentials stroomt.
3. Valideer risico's met onschuldige gerichte negatieve tests; onderscheid bewezen kwetsbaarheid, verdenking en niet geteste scenario's.
4. Repareer bij de bron en bevestig met dezelfde test; beschrijf rest-risico.

## Web

- Gebruik `textContent` en veilige DOM APIs voor externe tekst; geen `innerHTML` op ongecontroleerde content en nooit `eval`.
- Controleer origins bij cross-origin messaging, gebruik veilige links/redirects; serverauth niet vervangen door alleen UI-controles.
- Geen tokens of API keys in client-HTML, bundels, repo of logs. Stel CSP/headers in als hosting dit ondersteunt.

## Bestanden en Windows

- Bulkbestanden: standaard preview/dry-run waar zinvol; destructieve taken alleen na expliciete toestemming, met herstelpad of back-up.
- Vermijd path traversal, symlinks, ZIP-bombs, shell-injection en grote geheugenpieken; stream grote bestanden.
- Exacte duplicaten vereisen contenthash/verificatie, niet alleen naam, grootte of datum.

## Android, GitHub en geld

- Least-privilege `permissions` voor Actions, geen secrets in logs, release vanaf vertrouwde refs en verifieer artefact-integriteit.
- Android APK-updates: controleer signatuur/integriteit en respecteer expliciete OS-goedkeuring.
- Financiële berekeningen: test valutanotatie, precisie, lege input, grenswaarden en afronding.

**Rapporteer:** risico, concreet bewijs, ernst, minimale fix en teststatus. Nooit '100% veilig' claimen.

Bronideeën: Cloudflare security-audit-skill en Addy Osmani security-and-hardening.

## Platformgerichte controles

**Windows / PowerShell / Python**
- Voer processen standaard zonder administratorrechten uit, verhoog alleen een expliciete noodzakelijke bewerking.
- Geen `Invoke-Expression` met gebruikersinput of ongecontroleerde `shell=True`. Geef paden letterlijk en argumenten als een lijst door.
- Valideer netwerk-/UNC-paden, symlinks, DLL- en registrywaarden; blokkeer legitieme netwerkschijven niet blind, voorkom onverwachte netwerk-authenticatie en onbedoelde schrijfacties.
- Bescherm API-tokens via geschikte OS-credentialopslag; geen credentials in configbestanden, commando-logs of Git. Schakel PowerShell execution policy niet systeemwijd uit als generieke oplossing.

**Android**
- Controleer exported components, Intents, WebView-URL's, JS-bruggen, opslag en permissies op onbetrouwbare input.
- Keystore of gelijkwaardige beveiligde opslag voor secrets; signing-keys buiten Git en controleer release-APK-signatuur.
- Productieconfiguratie op `debuggable`, cleartext en HTTPS controleren. Bepaal back-upbeleid en eventuele certificate-pinning *risicogebaseerd*, niet automatisch uitschakelen of opleggen.
- Updates alleen met passende handtekening/verificatie en de door Android vereiste toestemming.

Bronidee: Claude Vibe Skills `SECURITY_WINDOWS.md`, `SECURITY_ANDROID.md`, `SECURITY_GATE.md`.
