"""
PIR proximity sensor: test program

2020-0326 PP new based upon
https://forum.pycom.io/topic/240/example-project-pir-sensor-and-domoticz-api
"""
import time
from machine import Pin


# flags
running = True
pir_triggered = False
button_pressed = False


# callback PIR sensor
def pirTriggered(pin):
    global pir_triggered
    print('pirTriggered - pin: {}'.format(pin))
    pir_triggered = True


# callback button press on expansion board
def buttonPressed(pin):
    global button_pressed
    button_pressed = True


pir = Pin(Pin.exp_board.G9, mode=Pin.IN, pull=Pin.PULL_UP)
pir.callback(trigger=Pin.IRQ_RISING, handler=pirTriggered)

# button = Pin('GP17',mode=Pin.IN,pull=Pin.PULL_UP)
button = Pin(Pin.exp_board.G17, mode=Pin.IN, pull=Pin.PULL_UP)
button.callback(trigger=Pin.IRQ_FALLING, handler=buttonPressed)


# main loop
def main():
    print("Starting main loop")
    while running is True:
        time.sleep_ms(500)
        if pir_triggered:
            pir_triggered = False
            print("Presence detected... ")
        elif button_pressed is True:
            button_pressed = False
            running = False
    print("Exited main loop")


if __name__ == '__main__':
    main()
