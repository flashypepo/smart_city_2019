#!/usr/bin/env python
#
# Copyright (c) 2019, Pycom Limited.
#
# This software is licensed under the GNU GPL version 3 or any
# later version, with permitted additional terms. For more information
# see the Pycom Licence v1.0 document supplied with this file, or
# available at https://www.pycom.io/opensource/licensing
#

"""
main.py - main entry RFID demo program
scans key/card tags and when valid card, turns RGBLed green, else red.

@History:
2019-0910 OOP version, using pyscan_board specification

See https://docs.pycom.io for more information regarding library specifics
"""
from lopy4_board import *
import pyscan_board as board

import binascii
import time
import pycom
import _thread

DEBUG = False  # 2019-0910 changed, True to see debug messages

RGB_BRIGHTNESS = 0x8
RGB_RED = (RGB_BRIGHTNESS << 16)
RGB_GREEN = (RGB_BRIGHTNESS << 8)
RGB_BLUE = (RGB_BRIGHTNESS)


class App:

    def __init__(self):
        # shortcuts to avoid much editing
        self.py = board.py
        self.nfc = board.nfc
        self.lt = board.lt
        self.li = board.li
        # Make sure heartbeat is disabled before setting RGB LED
        pycom.heartbeat(False)
        # Initialise the MFRC630 with some settings
        self.nfc.mfrc630_cmd_init()

    @property
    def VALID_CARDS(self):
        # 2019-0910 added my valid card ID's
        return [[0x43, 0x95, 0xDD, 0xF8],
                [0x43, 0x95, 0xDD, 0xF9],
                [0xD3, 0x8B, 0x8E, 0x01],   # 2019-0715 card added
                [0xC6, 0x35, 0xC1, 0x32]]   # 2019-0715 tag added

    def check_uid(self, uid, len):
        return self.VALID_CARDS.count(uid[:len])

    def print_debug(self, msg):
        if DEBUG:
            print(msg)

    # 2019-0910 added some useful text to print
    def send_sensor_data(self, name, timeout):
        while(True):
            print('Lightsensor: {}'.format(self.lt.light()))  # 2019-0715 changed
            print('Accelerometer: {}'.format(self.li.acceleration()))  # 2019-0715 changd
            time.sleep(timeout)

    def discovery_loop(self, nfc, id):
        while True:
            # Send REQA for ISO14443A card type
            self.print_debug('Sending REQA for ISO14443A card type...')
            atqa = nfc.mfrc630_iso14443a_WUPA_REQA(nfc.MFRC630_ISO14443_CMD_REQA)
            self.print_debug('Response: {}'.format(atqa))

            if (atqa != 0):
                # A card has been detected, read UID
                self.print_debug('A card has been detected, read UID...')
                uid = bytearray(10)
                uid_len = nfc.mfrc630_iso14443a_select(uid)
                self.print_debug('UID has length: {}'.format(uid_len))
                if (uid_len > 0):
                    self.print_debug('Checking if card with UID: [{:s}] is listed in VALID_CARDS...'.format(binascii.hexlify(uid[:uid_len],' ').upper()))
                    if (self.check_uid(list(uid), uid_len)) > 0:
                        self.print_debug('Card is listed, turn LED green')
                        print('Authorized access detected [{:s}]'.format(binascii.hexlify(uid[:uid_len], ' ').upper()))
                        pycom.rgbled(RGB_GREEN)
                    else:
                        self.print_debug('Card is not listed, turn LED red')
                        print('Alarm!! No authorized access detected')
                        pycom.rgbled(RGB_RED)
            else:
                # No card detected
                self.print_debug('Did not detect any card...')
                pycom.rgbled(RGB_BLUE)

            nfc.mfrc630_cmd_reset()
            time.sleep(.5)
            nfc.mfrc630_cmd_init()


if __name__ == '__main__':
    print('RFID demo started...')
    app = App()
    # This is the start of our main execution... start the thread
    _thread.start_new_thread(app.discovery_loop, (app.nfc, 0))
    # _thread.start_new_thread(send_sensor_data, ('Thread 2', 10))
