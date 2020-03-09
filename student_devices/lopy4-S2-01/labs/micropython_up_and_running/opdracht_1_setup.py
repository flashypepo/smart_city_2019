"""
Opdracht 1a: HARDWARE SETUP
URL: https://docs.pycom.io/gettingstarted/connection/lopy4/

Assembleer de microcontroller, Expansionboard en LoRa antenna.

Verbind ten alle tijde de LoRa-antenna met de LoPy4,
voordat je de micro-usb kabel/power verbindt met de laptop.
* Europa: je mag alleen de 868 MHz LoRa/Sigfox gebruiken.
  Verbind de antenna met de juiste conector.
* Wifi/BLE: er is geen antenna bijgeleverd voor Wifi en/of Bluetooth.
  Dat is ook niet nodig.

=========================
Opdracht 1b: SOFTWARE SETUP
URL's:
https://docs.pycom.io/gettingstarted/installation/
https://docs.pycom.io/gettingstarted/installation/pymakr/

Drivers: mgelijk niet nodig.
Pycom firmware update: sla dit over.
    De Lopy4 heeft Micropython firmware (v1.20.2.rc6).
Development IDE: volg de beschrijving,
    kies ofwel Atom ofwel Visual Studio Code.
    Installeer Pymakr plugin.
    Optioneel: installeer lint en git plugins - zie ELO.

=========================
Opdracht 1c: VERBIND DEVICE MET SERIELE POORT (USB) van LAPTOP
Gebruik een goede micro-USB datakabel.
Open Atom/VSC met een *lege* folder op jouw laptop.
PyMakr Console:
    - Settings >> Project Setting >> pymakr.conf file
        * als je slechts een device heb, kan je ook Global Settings
          aanpassen met Seriele poort address, zoals in documentatie staat,
          en sla je deze stap over.
    - More >> Set Serial Port
        - paste Serial Port -> address in pymakr.conf
    - Connect >> resultaat REPL (>>>) in PyMakr-console.
!!  - Download >> *alle* files van device naar projectfolder op laptop
        - vul pymakr.conf aan met voorbeeld pymakr.conf regels
          onderaan dit bestand.
    - Open Git tab in Atom/VSC, stage en commit alle bestanden.
        - voor backup en versie control.

RESULTAAT:
Wanneer je de REPL (>>>) in PyMakr-console ziet (device is verbonden),
tik dan in

print ("hello world")

en als je dan, na enter gegeven te hebben, de tekst

hello world

ziet staan als reactie, dan pas heb je de setup voltooid.

=========================
Opdracht 1d: Ga verder met andere opdrachten, of, bekijk de documentatie
op URL: https://docs.pycom.io/gettingstarted/programming/

* Introductie to Micropython
De code kan je in de REPL uitvoeren.

* Your first Pymakr project
met Controlling the on-board LED

NB. Beste manier is dat je een *lege* folder op je laptop als
project folder opent in VSC of Atom. Bij upload (PyMakr-knop)
worden *alle* bestanden en folders in de geopended folder naar
het device gekopieerd (probeer niet je disk te kopieren naar het device).

=========================
Tip: wil je alle bestanden en folders op het device verwijderen,
omdat het grandioos in de knoop zit, kan het device filesysteem formatteren.
Gebruik de volgende commando's op de REPL (je werkt dan op het device,
niet op je laptop):

import os
os.fsformat('/flash')

LET OP: Alle bestanden en folders op je device zijn dan wel weg !!!
Met een upload kan je jouw projectfolder weer op device zetten.
Zorg dat je een goede backup heb van projectfolder op jouw laptop
    (git, github, etc).


=========================
Voorbeeld pymakr.conf instellingen:
Volgende regels werken heel handig als je ze in pymakr.conf plaatst
(vervang de bestaande regels, zorg wel voor correcte json-syntax):

    "sync_file_types": [
        "py", "mpy",
        "txt", "log",
        "json", "xml",
        "html", "js", "css",
        "pem", "cet", "crt", "key"
    ],

    "py_ignore": [
    "pymakr.conf",
    "LoPy4-S2-01 240AC4C76AD0.pdf",
    ".gitignore"
    ],

Een voorbeeld pymakr.conf staat op ELO (pas wel 'address' aan).

"""
