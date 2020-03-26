"""
application which detects an object via infrared (PIR sensor)

2020-0324 PP new WORK_IN_PROGRESS
"""
from machine import Pin
from utime import sleep_ms
import time

from pir import PIR
from lopy4board import USR_BUTTON

# Device configuration
pirPin = Pin.exp_board.G9


class App():
    def __init__(self, display=None):
        self._pir = PIR(pirPin, self.pirTriggered)
        self._pir_triggered = False
        self.setUSRButton()  # use USR-button on expansion board
        self._display = display

    # callback for PIR sensor: object detected
    def pirTriggered(self, pin):
        # DEBUG: print('pirTriggered() pin: {}'.format(pin))
        self._pir_triggered = True

    # callback for USR button: stop detecting objects with PIR sensor
    def buttonPressed(self, pin):
        # DEBUG: print('buttonPressed() pin: {}'.format(pin))
        self._button_pressed = True

    def setUSRButton(self):
        self._button = Pin(USR_BUTTON, mode=Pin.IN, pull=Pin.PULL_UP)
        self._button.callback(trigger=Pin.IRQ_RISING, handler=self.buttonPressed)
        self._button_pressed = False

    def stopUSRButton(self):
        self._button_pressed = False
        self._button.callback()  # remove callback
        self._button = None  # remove button

    def run(self, display=None):
        try:
            # DEBUG: print("Starting run loop")
            # flags
            running = True
            while running:
                time.sleep_ms(500)
                if self._pir_triggered is True:
                    self._pir_triggered = False
                    print('Object detected!')
                    # do something usefull
                elif self._button_pressed:
                    self._button_pressed = False
                    running = False
            # DEBUG: print("Exited run loop")
            print('PIR done!')

        except KeyboardInterrupt:
            self._pir.stop()  # stop PIR sensing
            self.stopUSRButton()  # stop detecting button presses
            print('PIR done!')

    def show(self, message):
        if self._display is None:
            print(message)
        # else:
        #     self._display.print(message)

    @property
    def display(self):
        return self._display

    @display.setter
    def display(self, display):
        self._display = display


if __name__ == '__main__':
    print('main - doing nothing')
    pass
