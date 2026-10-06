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
