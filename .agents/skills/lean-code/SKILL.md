---
name: lean-code
description: Use the least complicated maintainable solution for HTML, Python, Power BI, Windows and Android; reduce code, dependencies, duplicated logic and manual steps.
---

# Lean Code

## Beslisladder

1. Is het nodig voor de expliciete taak? Niet nodig betekent niet bouwen.
2. Heeft de bestaande codebase al een functie, component of patroon? Hergebruik.
3. Voldoet de taal-standaardbibliotheek?
4. Voldoet de native browser/Windows/Android-functie?
5. Is een dependency al aanwezig en passend?
6. Schrijf anders de kleinste **leesbare, robuuste** oplossing.

Lees **eerst** de echte dataflow en relevante callsites. Minder regels in de verkeerde functie is geen verbetering.

- Geen premature cache, state manager, framework, factory, wrappers of extra configlagen.
- Eén source of truth voor berekeningen en gedeelde contracten; geen copy/paste tussen HTML en APK.
- In Python: standaardbibliotheek voor paden, streams, hashing, ZIP en CLI als dat volstaat.
- Code moet debugbaar blijven: geen cryptische one-liners of shortcuts die veiligheid aantasten.
- Maak één kleine test van niet-triviale logica, liefst zonder extra testframework.
- Optimaliseer security, goede fouten, dataintegriteit en accessibility nooit weg.

Bronideeën: Ponytail.
