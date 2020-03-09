"""
Voorwaarde: assemblage is gereed en je hebt print "hello world" uit kunnen voeren.
(zie opdracht_setup)

=============
Opdracht 2a: blinking built-in RGB-LED

Circuit/hardware: geen, maak alleen gebruik van RGB-led van Lopy4
Basis code: https://docs.pycom.io/gettingstarted/programming/first-project/
Maak een OOP-versie van de basis code.
Daarna kijk je eventueel op de ELO voor mijn vorbeelden.

Hanteer Software Engineering principes, zoals structureer
jouw code in niveau's (levels).

Voorbeeld - blinking RGBled:
1. main.py - code waarmee een applicatie, HelloWorldRGBled, wordt *opgestart*.
2. HelloWorldRGBled.py - Python bestand waarin de applicatie-logica instaat
        (class, functies,... i.e. *application-level code*).
        File kan staan in root-level, naast main.py, of in subfolders.
3. lib/blinkled.py  - Python bestand waarin code staat, waarmee een led wordt
               aangestuurd (*library/driver-level*).

boot.py: is niet nodig, bestaande boot.py laten staan.
Voorbeelden van een goede code structuur: zie ELO.

NB. Vergeet niet de code te uploaden, anders blijft het op jouw laptop
staan en 'doet het device niets'.


=============
Opdracht 2b: blinking externe LED.

Circuit/hardware: Plaats op breadboard een LED en verbind dat met een
weerstand (220-330 Ohm).
Maak verbindingen met device middels draadjes: een kant met GND (ground,
zwarte draad) en andere kant met een GPIO-pin (gele draad),
bijvoorbeeld G28 op Expansionboard.

NB. GPIO = General Purpose Input/Output

Maak een blinking LED, op basis van de Quick Usage Example code op
URL: https://docs.pycom.io/firmwareapi/pycom/machine/pin/

* Gebruik alleen de OUTPUT mode, om triviale reden.
* Maak ook gebruik van attribute pin.exp_board - is ook vermeld op gegeven URL.
* Maar gebruik van module time met de functie sleep()
* Speel met de led blinking effect:
    Realiseer bijvoorbeeld volgende scenario/cyclus:
        1. zet led aan gedurende 0.5 seconde
        2. zet led uit voor 0,.5 seconde
        3. zet led weer aan gedurende 0.5 seconde
        4. zet led weer uit gedurende 0.5 seconde

   Herhaal bovenstaand led-gedrag tot je als gebruiker
   een KeyboardInterrupt geeft (=Cntrl C).

   Zorg dat de led uit staat, na een keyboardinterrupt.
   Zorg dat er een melding komt en niet een tracetrack.


=============
Lastige opdracht 2c: fading RGB-led of externe LED.

Zoek op het web naar pycom/micropython code waarmee een oplichtende led
te maken is. Dit is een fading effect. Zo kan je ook proberen een
'heartbeat' led-effect te maken. Heel uitdagend.

"""
