"""
boot.py - connect to Wifi before application code in main

2020-0303 PP removed outdated comments
2019-1203 code from https://docs.pycom.io/tutorials/all/wlan/
     Aanleiding: foutmelding in wlan=WLAN() sinds v1.20.0.rc13[legacy]
     Works for Pycom version 1.18.2.r2 - 1.19.0.b4
"""
import os
import machine
import pycom
import time
# recommended: https://docs.pycom.io/firmwareapi/micropython/micropython/
import micropython
micropython.alloc_emergency_exception_buf(100)

uart = machine.UART(0, 115200)
os.dupterm(uart)


# 2020-03 PP bug in firmware v1.20.2.rc6 prevents
#   'cntrl-d' (=soft reboot) does not work!
#   Temporary fix according to
# https://github.com/pycom/pycom-micropython-sigfox/releases/tag/v1.20.2.rc6
# pycom.pybytes_on_boot(False)
# However, pytbytes is not starting.
# Reset: pycom.pybytes_on_boot(True)
# 2020-03 PP: recomendation
#   type <pycom.pybytes_on_boot(False)> (without <>) on the REPL.

# PP: specifiy is device should be connected to Wifi
# 2020-03 when PyBytes is used and configered for Wifi,
# USE_WIFI=False, because device is connected with Wifi thru PyBytes!
USE_WIFI = False  # connect to Wifi (True) or not (False)

if USE_WIFI:
    from wifisettings import known_nets
    from wifimanager import WifiManager
    from lopy4board import RED, GREEN
    try:
        print("Device is about to connect to Wifi...")
        wifi = WifiManager(known_nets)

        pycom.heartbeat(False)  # turn off heartbeat

        pycom.rgbled(RED)
        wifi.connect()  # connect device to wifi
        pycom.rgbled(GREEN)
        time.sleep(1)

        print(".. connected to '{}' with IP '{}'".format(wifi.ssid, wifi.ip))
        print('.. MAC-adres: {}'.format(wifi.mac))

    except OSError as err:
        print('OSError: file not found...{}'.format(err))

    except KeyboardInterrupt:
        print('User interrupted.')

    except Exception as ex:
        print('Exception...')
        print(ex)

    finally:
        pycom.heartbeat(True)  # turn on heartbeat
