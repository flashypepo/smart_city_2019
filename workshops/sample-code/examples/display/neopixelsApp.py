"""
Neopixel demo

TODO:
1.  move/add animations to class Animations
2.  add 'oldskool plasmascreens' from Tony DiCola
    especially for 8*8 neopixel matrix.
    Use good power source > 1.5A

Source lib/ws2812 driver:
https://core-electronics.com.au/tutorials/WS2812_and_NeoPixel_with_Pycom.html
"""
from machine import Pin
from time import sleep_ms, sleep
import os

from ws2812 import WS2812
# from animations import rainbow


class NeopixelsApp():
    def __init__(self, pinLed, numLed=8, brightness=10):
        print('NeopixelsApp contructor entered...')
        self._chain = WS2812(ledNumber=numLed,
                             brightness=brightness,
                             dataPin=pinLed)
        self._numLed = numLed
        self._data = [(0, 0, 0)] * numLed
        self.clear()

    def clear(self):
        print('clearing {} neopixels...'.format(self._numLed))
        self._data = [(0, 0, 0)] * self._numLed
        self._chain.show(self._data)
        sleep_ms(500)  # trial-and-error

    def Wheel(self, WheelPos):
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
    # TODO: move to class Animations
    # #################################
    # Cycles all the lights through the same rainbow colors
    def rainbow(self, wait):
        for j in range(0, 256, 1):
            for i in range(0, self._numLed, 1):
                self._data[i] = self.Wheel((i+j & 255))
                self._chain.show(self._data)
                sleep_ms(wait)

    # sparkle the LEDs to the set color
    def sparkle(self, c, wait):
        pixel = int.from_bytes(os.urandom(1), "big") % self._numLed
        pixel2 = int.from_bytes(os.urandom(1), "big") % self._numLed
        self._data[pixel] = c
        self._data[pixel2] = c
        self._chain.show(self._data)
        sleep_ms(wait)
        self._data[pixel] = (0, 0, 0)
        self._data[pixel2] = (0, 0, 0)

    def color(self, color=(0, 25, 0)):
        print('set neopixels on color {}...'.format(color))
        self._data = [color] * self._numLed
        self._chain.show(self._data)
        sleep_ms(100)

    def run(self, wait=5):
        print('NeopixelsApp::run() ... entered')
        c = (127, 127, 127)
        try:
            self.clear()
            while True:
                self.sparkle(c, 50)
                # self.rainbow(20)
        except KeyboardInterrupt:
            self.clear()


def main():
    numLed = 37  # Neopixels HEX of M5Stack
    # numLed = 64  # 8*8 neopixel matrix
    app = NeopixelsApp(Pin.exp_board.G22, numLed=numLed)
    wait = 5  # delay in secs
    app.run(wait)


if __name__ == '__main__':
    main()
