'''
2018-0818 Peter doesnot work!
chain = WS2812( ledNumber=16, dataPin='P12' )
 # dataPin is for LoPy board only
ERROR: AttributeError - Pin doesnot have 'ALT'
'''
from machine import Pin
import time
# from utime import sleep_ms
from ws2812 import WS2812


def test(pinLed, numLed=8, color=(0, 25, 0), delay=5):
    print('test chain of {0} neopixels on pin {1}'.format(numLed, pinLed))
    chain = WS2812(ledNumber=numLed,
                   brightness=10,
                   dataPin=pinLed)
    # clear leds
    print('clearing {} neopixels...'.format(numLed))
    data = [(0, 0, 0)] * numLed
    chain.show(data)
    time.sleep(delay / 2)
    # set chain on color
    print('set neopixels on color {}...'.format(color))
    data = [color] * numLed
    chain.show(data)
    time.sleep(delay * 2)
    # clear leds
    print('clearing {} neopixels...'.format(numLed))
    data = [(0, 0, 0)] * numLed
    chain.show(data)


if __name__ == '__main__':
    # n = 8
    pin = Pin.exp_board.G22
    test(pin)
