"""
Pyscan board pinouts

On-board sensors:
3 axis 12-bit accelerometer (ST LIS2HH12), I2C
Ambient light sensor (Lite-on LTR-329ALS-01), I2C
RFID-NFC Chip + NFC / RFID Antenna (NXP MFRC63002HN), I2C

2019-0910 Peter new
"""
from lopy4_board import *

# import of sensors classes
from pyscan import Pyscan
from MFRC630 import MFRC630
from LIS2HH12 import LIS2HH12
from LTR329ALS01 import LTR329ALS01

# Micro-SD card reader
SD_CLK = G10
SD_DAT = G15
SD_CMD = G11

# UART
UART_RX = G2
UART_TX = G1

# USR_BUTTON = G4
USR_BUTTON = G4

# TODO ????
# Camera connector
# Bar code scanner connector
# Fingerprint sensor connector
# LCD/infrared sensor connector


# create the sensors
py = Pyscan()
nfc = MFRC630(py)  # RFID reader
lt = LTR329ALS01(py)  # Ambient lightsensor
li = LIS2HH12(py)  # Accelerometer
