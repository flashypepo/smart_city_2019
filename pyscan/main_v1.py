#!/usr/bin/env python
#
# Copyright (c) 2019, Pycom Limited.
#
# This software is licensed under the GNU GPL version 3 or any
# later version, with permitted additional terms. For more information
# see the Pycom Licence v1.0 document supplied with this file, or
# available at https://www.pycom.io/opensource/licensing
#

# See https://docs.pycom.io for more information regarding library specifics
from lopy4_board import *
import pyscan_board as board

import binascii
import time
import pycom
import _thread

DEBUG = False  # change to True to see debug messages

# 2019-0910 added my valid card ID's
VALID_CARDS = [[0x43, 0x95, 0xDD, 0xF8],
               [0x43, 0x95, 0xDD, 0xF9],
               [0xD3, 0x8B, 0x8E, 0x01],   # 2019-0715 card added
               [0xC6, 0x35, 0xC1, 0x32]]   # 2019-0715 tag added

# shortcuts to avoid editing
py = board.py
nfc = board.nfc
lt = board.lt
li = board.li


RGB_BRIGHTNESS = 0x8
RGB_RED = (RGB_BRIGHTNESS << 16)
RGB_GREEN = (RGB_BRIGHTNESS << 8)
RGB_BLUE = (RGB_BRIGHTNESS)

# Make sure heartbeat is disabled before setting RGB LED
pycom.heartbeat(False)

# Initialise the MFRC630 with some settings
nfc.mfrc630_cmd_init()


def check_uid(uid, len):
    return VALID_CARDS.count(uid[:len])


def print_debug(msg):
    if DEBUG:
        print(msg)


# 2019-0910 added some useful text to print
def send_sensor_data(name, timeout):
    while(True):
        print('Lightsensor: {}'.format(lt.light()))  # 2019-0715 changed
        print('Accelerometer: {}'.format(li.acceleration()))  # 2019-0715 changd
        time.sleep(timeout)


def discovery_loop(nfc, id):
    while True:
        # Send REQA for ISO14443A card type
        print_debug('Sending REQA for ISO14443A card type...')
        atqa = nfc.mfrc630_iso14443a_WUPA_REQA(nfc.MFRC630_ISO14443_CMD_REQA)
        print_debug('Response: {}'.format(atqa))
        if (atqa != 0):
            # A card has been detected, read UID
            print_debug('A card has been detected, read UID...')
            uid = bytearray(10)
            uid_len = nfc.mfrc630_iso14443a_select(uid)
            print_debug('UID has length: {}'.format(uid_len))
            if (uid_len > 0):
                print_debug('Checking if card with UID: [{:s}] is listed in VALID_CARDS...'.format(binascii.hexlify(uid[:uid_len],' ').upper()))
                if (check_uid(list(uid), uid_len)) > 0:
                    print_debug('Card is listed, turn LED green')
                    print('Detected card with UID: [{:s}]'.format(binascii.hexlify(uid[:uid_len], ' ').upper()))
                    pycom.rgbled(RGB_GREEN)
                else:
                    print_debug('Card is not listed, turn LED red')
                    pycom.rgbled(RGB_RED)
        else:
            # No card detected
            print_debug('Did not detect any card...')
            pycom.rgbled(RGB_BLUE)
        nfc.mfrc630_cmd_reset()
        time.sleep(.5)
        nfc.mfrc630_cmd_init()


print('RFID demo started...')
# This is the start of our main execution... start the thread
_thread.start_new_thread(discovery_loop, (nfc, 0))
# _thread.start_new_thread(send_sensor_data, ('Thread 2', 10))
