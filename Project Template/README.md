Description: Sample files to setup a new Project.

## Must-Have:
boot.py - startup code - connects device with Wifi, using lib/wifisettings.py
main.py - main startup applications on device

main_wifi_samples.py - main example with Wifi-networking. 
                     - Works with firmware "1.19.0.b4 (legacy)"
pymakr.conf  - configuration file for PyMakr plugin. 
             - DO: change 'address' value to com-port where device is connected.

Readme for Github:
README.md - this textfile

## Could-Have:
main_pyscan_oop.py  - OOP versie van main_pyscan.py for a PyScan board
main_pyscan.py      - main example for PyScan board
main_pysense.py     - main example for PySense board
main_pytrack.py     - main example for PyTrack board

## Must-Have:
folder lib
- lopy4board.py  -- specifications of board pins.
- urequests.py  -- helper to do a GET/POST HTTP-requests
- wifimanager.py  -- class WifiManager to connect devices to Wifi WPA2-networks (ssid & password)
- wifisettings.py   -- settings/credentials for Wifi networks. DO NOT DISTRIBUTE

## Could-Have: folder lib/sensors
- several drivers for sensors. Most are present on PySense, PyScan or PyTrack boards.
- DO: copy Python files to folder 'lib'.

## Could-Have: folder lib/boards
- board classes for PySense, PyScan or PyTrack boards.
- DO: copy Python files to folder 'lib'.

## Recommendation Smart City as startup for your Smart Device:
semester 1: copy/clone Must-Have files and select files for your bundle/board.
semester 2: copy/clone Must-Have files.

Firmware LoPy4: version 1.19.0.b4 (legacy). This works with the Wifi-code.

updated 2020-0229 by PP