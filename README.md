# FaceDetect

Lokale AI fotoselector die gezichten in een gekozen map detecteert, vergelijkbare gezichten groepeert en foto's naar gekozen uitvoermappen kopieert.

## Functies

- Kies een bronmap via een Windows mapvenster
- Scan JPG, JPEG, PNG en WEBP bestanden
- Preview van automatisch gevonden unieke personen
- Geef iedere persoon een naam
- Bekijk alle foto's waarin een gekozen persoon voorkomt
- Sorteer foto's waarop alleen die persoon staat
- Sorteer foto's waarop die persoon staat, ook wanneer anderen aanwezig zijn
- Plaats foto's met meerdere gezichten apart
- Bestanden worden standaard gekopieerd, nooit uit de bronmap verwijderd
- Volledig lokaal, zonder cloud API

## Installeren

Python 3.11 wordt aanbevolen.

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
streamlit run app.py
```

Of start na installatie met `start.bat`.

## Werkwijze

1. Klik op **Kies fotomap**.
2. Klik op **Scan gezichten**.
3. Controleer de automatisch aangemaakte persoonsgroepen.
4. Geef groepen herkenbare namen.
5. Kies een persoon en een sorteerregel.
6. Bekijk eerst de preview.
7. Kopieer daarna de geselecteerde foto's naar een uitvoermap.

## Sorteerregels

| Regel | Resultaat |
|---|---|
| Alleen deze persoon | Foto bevat precies één gezicht en dat gezicht hoort bij de gekozen persoon |
| Deze persoon, ook met anderen | Iedere foto waarop de gekozen persoon voorkomt |
| Meerdere personen | Iedere foto met twee of meer gedetecteerde gezichten |
| Geen gezicht | Foto's waarop geen gezicht is gevonden |

## Privacy

De foto's en gezichtskenmerken blijven lokaal op de computer. De cache staat in `.facedetect/cache.pkl` binnen de geselecteerde fotomap en kan altijd worden verwijderd.

## Opmerking

Gezichtsherkenning blijft probabilistisch. Controleer de preview voordat je grote hoeveelheden foto's kopieert. De gevoeligheid van het groeperen is in de zijbalk aanpasbaar.
