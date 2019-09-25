'''
toggleLeds - LED animaties
2019-0917 Peter - add toggleLeds
'''
from machine import Pin
import _thread
import time

USE_DEBUG = False  # 2019-0917 changed


class BlinkLedsApp:

    def __init__(self, pins):
        """ create LED objects on pins.
        If no pins -> raise exception"""
        if len(pins) == 0:
            raise Exception('No leds??')
        self._pins = pins
        self._leds = []  # collection of leds
        for pin in pins:
            led = Pin(pin, Pin.OUT)
            self._leds.append(led)
        if USE_DEBUG:
            print('{} LED-objects created...'.format(len(self._leds)))

    def blink(self, dt=1):
        """ blink(dt): blink all leds in frequency of dt seconds """
        while True:
            if len(self._leds) == 0:
                raise Exception('No leds??')
            for led in self._leds:
                led.toggle()
                time.sleep(dt)

    def run(self, dt=0.5):
        """ blink all leds in a thread """
        _thread.start_new_thread(self.blink, (dt, ))


if __name__ == '__main__':
    from ledsApp import BlinkLedsApp
    from lopy4_board import G28, G22
    pins = [G28, G22]  # [] is test for exception!
    try:
        leds = BlinkLedsApp(pins)
        leds.run(dt=0.5)
    except Exception as ex:
        print(ex)
        print('Blinking leds is stopped')
