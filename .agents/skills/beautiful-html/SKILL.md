---
name: beautiful-html
description: Design and build visually exceptional, fully functional responsive HTML/CSS/JS apps, dashboards, media tools and landing pages with accessible motion and real interactions.
---

# Beautiful HTML

**Doel:** visueel onderscheidend en direct bruikbaar, nooit alleen een mockup.

1. Analyseer huidige branding, bestaande HTML/CSS/JS, assets, interfaces en relevante devicebeperkingen.
2. Kies sterke compositie, typografie, schaal, kleur en visuele hiërarchie. Eén duidelijke hoofdactie, geen standaard-SaaS-vibe of kaartepidemie.
3. Maak de functionaliteit eerst werkelijk werkend: drag & drop, uploads, sliders, scrubbers, audio/video, export, errors, loading, empty states en responsive knoppen waar gevraagd.
4. Begin voor standalone tools met één lichte HTML-file en native Web APIs wanneer dat volstaat. Voeg geen framework toe om simpele state of datumvelden te beheren.
5. Werk motion af als feedback en navigatie: vooral `transform`/`opacity`, beperkte duur, `prefers-reduced-motion`, soepele 60fps-interactie.
6. Test waar mogelijk met een echte browser op 360/768/1440 px, touch, toetsenbord, tab-order, contrast, console en falende invoer.

## Media en performance

- Gebruik voor grote video's `preload=metadata`, posters en thumbnails; decodeer niet onnodig volledige 4K-media in RAM.
- Toon originele media en bewerkt resultaat apart als de gebruiker om een vergelijking of IN/OUT-editor vraagt.
- Native download, Canvas, Media APIs of ffmpeg.wasm alleen als de gevraagde functie daarmee echt kan werken; geen servertranscoding beloven op pure GitHub Pages.
- Vermijd afhankelijkheid van grote externe fonts/scripts als er een nette lichte oplossing is.
- Respecteer toegankelijkheid: semantische controls, keyboard, aria waar zinvol, zichtbare focus, voldoende contrast.

Bronideeën: Impeccable en Addy Osmani frontend-ui-engineering.

## Designcontract en visuele controle (selectief)

1. Controleer bestaande kleuren, spacing, fonts, tokens en bestaande `DESIGN.md`; de huidige merkidentiteit is leidend tenzij herontwerp gevraagd is.
2. Bij langdurige projecten met meerdere schermen kan `templates/DESIGN.template.md` dienen voor een **eigen** `DESIGN.md` met meetbare tokens (kleur, typografie, radius, spacing), navigatie en states (hover, focus, disabled, loading, empty, error). Gebruik geen centrale standaardkleuren in alle projecten.
3. Bij losse HTML-tools zijn CSS-variabelen genoeg; geen design-document, npm-linter of plugin verplicht.
4. Vermijd onbedoelde AI-templatepatronen zoals overbodige kaarten, zware schaduwen en decoratieve gradients. Bewust gekozen merkpatronen zijn toegestaan.
5. Na UI-wijziging: wanneer een browser beschikbaar is screenshot op de relevante viewport en interactiestates, grootste afwijking herstellen, maximaal drie iteraties. Test keyboard, focus en leescontrast (WCAG AA, normale tekst 4,5:1 en grote tekst 3:1). Zonder browser niet beweren dat deze controle uitgevoerd is.

Bronidee: Claude Vibe Skills `DESIGN_REFERENCE.md` en Google Labs `DESIGN.md`.
