"""
get deviceui.py - extracts the Device EUI for TTN from device
Device EUI

DeviceEUI comes from the device itself and can be obtained from lora.mac().

2020-0326 PP new
"""
from network import LoRa
import ubinascii


def getDeviceEUI():
    lora = LoRa()
    return (ubinascii.hexlify(lora.mac()).decode('ascii'))
    # returns: DevEUI - 8-byte characterstring


if __name__ == '__main__':
    print("DevEUI: %s" % getDeviceEUI())
