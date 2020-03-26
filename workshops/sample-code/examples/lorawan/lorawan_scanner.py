"""
lorawan scanner - test to connect device to TTN via nearest LoRa Gateway.

To connect a Pycom LoRa device (LoPy4) to TTN you’ll need to provision it.
This requires three pieces of information
1. Device EUI (DevEUI)
2. Application EUI (AppEUI)
3. Application Key (AppKey)

See information how to register a device on TTN:
https://docs.pycom.io/chapter/gettingstarted/registration/lora/objenious.html

Device EUI
This comes from the device itself and can be obtained from lora.mac().
See helper: examples/lorawan/getdeviceeui.py

Application EUI and Application Key
See TTN Console - registering device

Application EUI and Key are two LoRaWAN parameters that should ideally
by generated by you, if supplying devices to end customers.

The Application EUI is a EUI-64 (8 bytes) identifier which should be
universally unique.

The Application Key is generated by the TTN and should be a randomly
generated, secure, 128 bit (16 byte) token.

Protocol LoraWan: Over-the-Air Activation (OTAA)

History
2020-0326:  test lorawan_scanner with firmware 1.20.2.rc6 (pybytes)
            PyBytes not active. Connects to Lora-gateway, after ±6 secs.
2018-0511:  test at home/Naarden with device on TheThingsNetwork
2018-0424:  registration a device on TTN:
device eui:
https://docs.pycom.io/chapter/gettingstarted/registration/lora/objenious.html
DevEUI: 70b3d549936a3db0
* bytes, bytes, bytes:
https://www.thethingsnetwork.org/docs/devices/bytes.html
"""
from network import LoRa
import socket
import time
import binascii

import pycom
from lorasettings import app_eui, app_key


def main(delay=5):
    print('LoRaWan scanner entered...')
    # 2018-05 status LoRaWan via rgbled
    # LED=RED - no LoRaWan connection
    # LED=GREEN - LoRAWAN connection
    # hearbeat off
    pycom.heartbeat(False)

    # Initialize LoRa in LORAWAN mode.
    # Please pick the region that matches where you are using the device:
    # Asia = LoRa.AS923
    # Australia = LoRa.AU915
    # Europe = LoRa.EU868
    # United States = LoRa.US915
    lora = LoRa(mode=LoRa.LORAWAN, region=LoRa.EU868)

    # create an OTAA authentication parameters
    loramodem_mac = binascii.hexlify(lora.mac(), ':').decode()
    print("Lora modem MAC is {}".format(loramodem_mac.upper()))

    # join a network using OTAA (Over the Air Activation)
    lora.join(activation=LoRa.OTAA, auth=(app_eui, app_key), timeout=0)

    # wait until the module has joined the network
    pycom.rgbled(0x7f0000)  # red

    while not lora.has_joined():
        time.sleep(delay)  # delay=5 seconds - some trial-and-error
        # ORG: time.sleep_ms(10)
        print('LoraWan: not yet joined...')

    # yes, connected...
    pycom.rgbled(0x007f00)  # green
    print('LoraWan joined...')  # console message

    # create a LoRa socket
    s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)

    # set the LoRaWAN data rate
    s.setsockopt(socket.SOL_LORA, socket.SO_DR, 5)

    # make the socket blocking
    # (waits for the data to be sent and for the 2 receive windows to expire)
    s.setblocking(True)

    # send some data
    # 2018-0424 after connecting to lora/TTN,
    # you only have to use next line to send data
    s.send(bytes([0x50, 0x65, 0x74, 0x65, 0x72]))  # 'Peter'
    # s.sendData(version, sensor.temperature, sensor.humidity, sensor.pressure)

    # make the socket non-blocking
    # (because if there's no data received it will block forever...)
    s.setblocking(False)

    # get any data received (if any...)
    data = s.recv(64)
    print('Received data:', data)

    # 2018-0518 - set on hearbeat
    pycom.heartbeat(True)


if __name__ == '__main__':
    main(delay=2)
