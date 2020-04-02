"""
application which demonstrates animation on neopixel chain.

TODO:
1.  make a class Animations from which animations can be used.
2.  add 'oldskool plasmascreens' from Tony DiCola
    especially for 8*8 neopixel matrix.
    Use good power source > 1.5A

2020-0329 PP added __version__, changed dinPin:G22->G28, NUMPIXEL
2020-0324 PP new, based upon source lib/ws2812 driver:
https://core-electronics.com.au/tutorials/WS2812_and_NeoPixel_with_Pycom.html
"""
__version__ = "0.0.2"

from machine import Pin
from time import sleep_ms, sleep
import os

from ws2812 import WS2812
# TODO: from animations import rainbow

# device configuration
dinPin = Pin.exp_board.G15  # G28
# NUMLED = const(8)  # neopixel stick
# NUMLED = const(37)  # Neopixels HEX of M5Stack
NUMLED = const(45)  # stick + HEX
# NUMLED = const(64)  # 8*8 neopixel matrix
wait = 5  # delay in ms
BRIGHTNESS = 30  # brightness %


class NeopixelsDemo():

    def __init__(self):
        # print('NeopixelsApp contructor entered...')
        self._chain = WS2812(ledNumber=NUMLED,
                             brightness=BRIGHTNESS,
                             dataPin=dinPin)
        self._data = [(0, 0, 0)] * NUMLED
        self.clear()

    def clear(self):
        self._data = [(0, 0, 0)] * NUMLED
        self._chain.show(self._data)
        sleep_ms(100)  # trial-and-error

    def wheel(self, WheelPos):
        WheelPos = 255 - WheelPos
        if WheelPos < 85:
            return (255 - WheelPos * 3, 0, WheelPos * 3)
        if WheelPos < 170:
            WheelPos -= 85
            return (0, WheelPos * 3, 255 - WheelPos * 3)
        WheelPos -= 170
        return (WheelPos * 3, 255 - WheelPos * 3, 0)

    # #################################
    # animations
    # TODO: class Animations
    # #################################

    # sparkle the LEDs to the set color
    def sparkle(self, c, wait):
        pixel = int.from_bytes(os.urandom(1), "big") % NUMLED
        pixel2 = int.from_bytes(os.urandom(1), "big") % NUMLED
        self._data[pixel] = c
        self._data[pixel2] = c
        self._chain.show(self._data)
        sleep_ms(wait)
        self._data[pixel] = (0, 0, 0)
        self._data[pixel2] = (0, 0, 0)

    def getRandomBrightness(self, isWheelColor=False):
        """ returns random color (isWheelColor is True), or,
            random white brightness (isWheelColor is False)
            Default: random white brightness
        """
        c = int.from_bytes(os.urandom(1), "big") % 255
        if isWheelColor is True:
            c = self.wheel(c)
            return c
        else:
            return (c, c, c)

    def color(self, color=(0, 25, 0)):
        print('set neopixels on color {}...'.format(color))
        self._data = [color] * NUMLED
        self._chain.show(self._data)
        sleep_ms(100)

    def run(self, delay=5):
        # print('NeopixelsApp::run({}) ... entered'.format(delay))
        try:
            # print('clearing {} neopixels...'.format(NUMLED))
            self.clear()
            # print('sparkle in a color...')
            while True:
                c = self.getRandomBrightness(isWheelColor=False)
                # print('sparkle in color {}'.format(c))
                self.sparkle(c, delay)
                # self.rainbow(20)
        except KeyboardInterrupt:
            self.clear()


if __name__ == '__main__':
    app = NeopixelsDemo()
    app.run()
