"""
lab-oefening: temperaturen inlezen uit een bestand en
basisinformatie van de temperaturen tonen.

In deze opdracht ga je temperaturen inlezen uit een bestand
en de volgende basisinformatie op het console tonen:
* de hoogste en laagste temperatuur,
* de gemiddelde temperatuur,
* en de mediane temperatuur.

De temperaturen zijn de maandelijks hoogste temperaturen op
Heathrow Airport van 1948 tot en met 2016.
Vervolgens haal je wat basisinformatie uit de temperaturen:

De mediane temperatuur is 'de temperatuur in het midden van
de lijst' als alle temperaturen zijn gesorteerd.

Gegevens en tips:
Bestand: 'lab_temp.txt'
Maak gebruik van data-type list voor de temperaturen.
Maak gebruik van de string functie 'strip()'.
"""
temperatures = []
lab_file = 'lab_temp.txt'  # list of temperature data
with open(lab_file) as infile:
    for row in infile:
        temperatures.append(float(row.strip()))
print('Aantal ingelezen temperaturen:', len(temperatures))  # 828

# uitwerking:
# bepaal minimum, maximum, gemiddelde en mediane temperaturen
# en toon op scherm/console
