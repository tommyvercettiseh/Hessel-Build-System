# DESIGN.md | optioneel projectsjabloon

Voor blijvende UI-projecten: leid deze informatie eerst af uit bestaande schermen, styles en componenten. Vervang de onderstaande **placeholders** voordat je dit kopieert als `DESIGN.md`. Voor kleine losse HTML-tools is dit bestand niet nodig.

Gebaseerd op [Google Labs DESIGN.md](https://github.com/google-labs-code/design.md/blob/main/docs/spec.md), waarvan de specificatie momenteel alpha is.

```markdown
---
version: alpha
name: REPLACE_PRODUCT_NAME
colors:
  primary: "REPLACE_WITH_VALID_COLOR"
  surface: "REPLACE_WITH_VALID_COLOR"
  on-primary: "REPLACE_WITH_VALID_COLOR"
typography:
  heading:
    fontFamily: REPLACE_WITH_PRODUCT_FONT
    fontSize: 30px
    fontWeight: 600
    lineHeight: 1.2
  body:
    fontFamily: REPLACE_WITH_PRODUCT_FONT
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.5
spacing:
  sm: 8px
  md: 16px
  lg: 24px
rounded:
  sm: 6px
  md: 10px
---
## Overview
Productdoel, doelgroep en bestaande merkidentiteit.

## Colors
Semantische kleuren en contrast voor elke benodigde state.

## Typography
Concreet font, omvang en hiërarchie van koppen, tekst, labels en data.

## Layout
Grid, breakpoints, dichtheid, navigatie en hoofdactie.

## Elevation & Depth
Borders, oppervlakteverschillen en eventueel schaduwgebruik.

## Shapes
Radii en componentvormen.

## Components
Button, input, modal, tabel en grafiek met hover, focus, disabled, loading, empty en error states.

## Do's and Don'ts
Meetbare productregels, geen loze stijltermen of willekeurige verboden.
```

Het formaat is pas valide na invullen van alle placeholders. Gebruik bestaande design tokens als bron. Lint of screenshotcontrole is alleen geslaagd wanneer werkelijk gedraaid. Niets uit deze template wordt automatisch uitgerold naar andere repositories.
