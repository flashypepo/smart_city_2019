"""
class PIR - device driver for a generic PIR sensor

2020-0326 PP new
"""
import time
from machine import Pin


class PIR():
    def __init__(self, pin, pirTriggered=None):
        # DEBUG: print('PIR entered... pin:{}'.format(pin))
        self._pir = Pin(pin, mode=Pin.IN, pull=Pin.PULL_UP)
        if pirTriggered is not None:
            # specify callback when pir detect object
            # DEPRECATED: self._pir.irq(trigger=Pin.IRQ_RISING, handler=pirTriggered)
            self._pir.callback(trigger=Pin.IRQ_RISING, handler=pirTriggered)

    def stop(self):
        """ stop() - remove callback, i.e. stop sensing objects """
        self._pir.callback()  # remove callback
        self._pir = None


if __name__ == '__main__':
    import time
    from machine import Pin

    # flags
    running = True
    pir_triggered = False
    button_pressed = False

    # PIR sensor
    pirPin = Pin.exp_board.G7

    # callback
    def pirTriggered(pin):
        global pir_triggered
        print('pirTriggered() pin: {}'.format(pin))
        pir_triggered = True

    pir = PIR(pirPin, pirTriggered)

    # Expansion board: USR button
    from lopy4board import USR_BUTTON
    usr_button = Pin(USR_BUTTON, mode=Pin.IN, pull=Pin.PULL_UP)

    # callback
    def buttonPressed(pin):
        global button_pressed
        print('buttonPressed() pin: {}'.format(pin))
        button_pressed = True

    usr_button.callback(trigger=Pin.IRQ_FALLING, handler=buttonPressed)

    # main loop
    print("Starting main loop")
    while running:
        time.sleep_ms(500)
        if pir_triggered:
            pir_triggered = False
            print('Presence detected')
        elif button_pressed:
            button_pressed = False
            running = False
    pir.stop()  # stop PIR sensing
    usr_button.callback()  # stop button
    print("Exited main loop")
