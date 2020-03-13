"""
blinkingled.py - 'hello world' for microcontrollers

Component level
- functional style
- OOP style

2020-03 PP , added lopy4board for RGB-colors
firmware v1.20.2.rc6
2019-09 PP new
"""
import pycom
import time
from lopy4board import RED, GREEN, BLUE, BLACK
# define literals as constants: best practices SE


# functional paradigm style: function blink
def blink():
    pycom.heartbeat(False)

    while True:
        pycom.rgbled(RED)  # 0xFF0000
        time.sleep(1)
        pycom.rgbled(GREEN)  # 0x00FF00
        time.sleep(1)
        pycom.rgbled(BLUE)  # 0x0000FF
        time.sleep(1)
        pycom.rgbled(BLACK)  # 0x000000 = off
        time.sleep(1)

    pycom.heartbeat(True)


print('blink() defined')


# OOP style: class RGBLed
class RGBLed():
    def __init__(self):
        pycom.heartbeat(False)

    def blink(self):
        while True:
            pycom.rgbled(RED)
            time.sleep(1)
            pycom.rgbled(GREEN)
            time.sleep(1)
            pycom.rgbled(BLUE)
            time.sleep(1)
            pycom.rgbled(BLACK)
            time.sleep(1)

    def off(self):
        pycom.rgbled(BLACK)  # Black = off
        pycom.heartbeat(True)


print('class RGBLed defined')

if __name__ == '__main__':
    '''
    # functional paradigm style
    blink()
    '''
    # OOP style:
    rgb = RGBled()
    try:
        rgb.blink()
    except KeyboardInterrupt:
        rgb.off()
        pycom.heartbeat(True)
        print("done!")
    # '''
