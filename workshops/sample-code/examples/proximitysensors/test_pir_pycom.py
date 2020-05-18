"""
PIR proximity sensor: test program
2020-0517 PP PIR -> G7/P20, sample code from:
          https://docs.pycom.io/tutorials/all/pir/
"""
import time
from machine import Pin

# set False when NO TFT-display is connected
TFT_DISPLAY = True
# TFT-support
if TFT_DISPLAY is True:
    from ST7735 import TFT

pir_triggered = False


# callback PIR sensor
def pirTriggered(pin):
    global pir_triggered
    # print Pin-info of PIR
    print('pirTriggered - pin:{} -> value={}'.format(pin, pin.value()))
    pir_triggered = True


# PIR sensor, connected to G7/P20 expansion board
PIR_PIN = Pin.exp_board.G7
pir = Pin(PIR_PIN, mode=Pin.IN, pull=Pin.PULL_UP)
# trigger callback when line is going up
pir.callback(trigger=Pin.IRQ_RISING, handler=pirTriggered)


# alarm message
def setAlert(display, refresh=False):
    print("Alert! persoon gedetecteerd, doe iets...")
    if display is not None:
        if refresh is True:
            display.blank()
        display.text("Alert!", 5, 20,
                     color=TFT.RED, size=3)
    last_trigger = time.time()
    return_code = ('Presence:LivingRoom', '1')
    print("Send request: "+str(return_code))
    time.sleep(3)  # simulate transmission
    return last_trigger


# no alert messages
def noAlert(display, refresh=False):
    print("Niemand aanwezig...")
    if display is not None:
        if refresh is True:
            display.blank()
        display.text("OKAY!", 5, 20,
                     color=TFT.GREEN, size=3)
    return 0


# main loop
def run(display=None):
    global pir_triggered

    print("Starting main loop")
    # config
    hold_time_sec = 10
    # flags
    last_trigger = -10


    try:
        if display is not None:
            # orientation TFT-display
            display.rotation(2)

        while True:
            # polling: if pir() == 1:
            if pir_triggered is True:
                # set alarm if more then 10 seconds ago
                if time.time() - last_trigger > hold_time_sec:
                    last_trigger = setAlert(display=display, refresh=True)
                    pir_triggered = False
            else:
                if last_trigger != 0:
                    # clear Alert-text
                    last_trigger = noAlert(display=display, refresh=True)
                else:
                    last_trigger = noAlert(display=display, refresh=False)
            time.sleep_ms(500)

    except KeyboardInterrupt:
        print("User interrupt - exited main loop")
        if display is not None:
            display.blank()
        pir.callback(trigger=Pin.IRQ_RISING, handler=None)


if __name__ == '__main__':
    run(display=None)
