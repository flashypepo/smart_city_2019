"""
boot.py - connect to Wifi before application code in main

2019-1203 code from https://docs.pycom.io/tutorials/all/wlan/
     Aanleiding: foutmelding in wlan=WLAN() sinds v1.20.0.rc13[legacy]
     Works for Pycom version 1.18.2.r2 - 1.19.0.b4
     Demos accessing the web do have problems and do not work as expected.
"""
import os
import machine
import pycom
import time

from wifisettings import known_nets

# recommended: https://docs.pycom.io/firmwareapi/micropython/micropython/
import micropython
micropython.alloc_emergency_exception_buf(100)

uart = machine.UART(0, 115200)
os.dupterm(uart)

USE_WIFI = True  # connect to Wifi (True) or not (False)
RED = 0xff0000
BLUE = 0x0000ff
GREEN = 0x00ff00

if USE_WIFI:
    from wifimanager import WifiManager
    try:
        print("Device about to connect to Wifi...")
        pycom.heartbeat(False)  # turn off heartbeat
        wifi = WifiManager(known_nets)

        pycom.rgbled(RED)
        wifi.connect()  # connect device to wifi
        pycom.rgbled(GREEN)
        time.sleep(1)

        print("Device is connected to '{}' with IP address '{}'".format(wifi.ssid, wifi.ip))
        #print('Device MAC-adres: {}'.format(wifi.mac))

    except OSError as err:
        print('OSError: file not found...{}'.format(err))

    except KeyboardInterrupt:
        print('User interrupted.')

    except Exception as ex:
        print('Exception...')
        print(ex)

    finally:
        print('Finally .. heartbeat back')
        pycom.heartbeat(True)  # turn on heartbeat

'''
if machine.reset_cause() != machine.SOFT_RESET:
    from network import WLAN
    wl = WLAN()
    wl.mode(WLAN.STA)
    original_ssid = wl.ssid()
    original_auth = wl.auth()

    print("Scanning for known wifi nets...")
    available_nets = wl.scan()
    nets = frozenset([e.ssid for e in available_nets])

    known_nets_names = frozenset([key for key in known_nets])
    net_to_use = list(nets & known_nets_names)
    try:
        net_to_use = net_to_use[0]
        net_properties = known_nets[net_to_use]
        pwd = net_properties['pwd']
        sec = [e.sec for e in available_nets if e.ssid == net_to_use][0]
        if 'wlan_config' in net_properties:
            wl.ifconfig(config=net_properties['wlan_config'])
        wl.connect(net_to_use, (sec, pwd), timeout=10000)
        while not wl.isconnected():
            machine.idle() # save power while waiting
        print("Connected to "+net_to_use+" with IP address:" + wl.ifconfig()[0])

    except Exception as e:
        print("Failed to connect to any known network, going into AP mode")
        wl.init(mode=WLAN.AP, ssid=original_ssid, auth=original_auth, channel=6, antenna=WLAN.INT_ANT)

'''
