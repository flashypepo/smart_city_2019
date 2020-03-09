"""

Opdracht 3: binaire counter met externe LED's.

Circuit/hardware:
Plaats 6-8 LED's op breadboard en verbind elke LED met een weerstand
(220-330 Ohm) met een GPIO op de Exapansionboard.
Bijvoorbeeld, bruikbare GPIOs op Expansionboard zijn:
    G28, G22, G17, G16, G15, G14 (en G12, G24).

Software:
Maak een micropython programma waarmee de leds een binaire optelling
laten zien, bijv.  00000001, 00000010, 00000011, 00000100, etc.
0=led uit, 1=led aan.
NB. 8 leds = simulatie  van een 8-bits Program Counter.

Keuzen:
* High-bit is LED aan linkerkant van de rij LED's, low-bit aan de rechterkant
* Low-bit is LED aan linkerkant van de rij LED's, high-bit aan de rechterkant

Tip: een getal heeft een waarde, bij. 3, en een representatie,
bijvoorbeeld 0x3 in hex, zo ook 000010 binair met 6-digits.

"""
