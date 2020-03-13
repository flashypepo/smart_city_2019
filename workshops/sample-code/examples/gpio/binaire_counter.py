"""
binaire counter

based upon tutorial of Muharrem Demiray:
URL: https://github.com/mdemiray/MicroPython-BinaryCounterLED

2020-03 PP adopted for an 8-LED array
Pycom firmware 1.20.2.rc6

"""
from machine import Pin
from time import sleep

# states of LED
ON = const(0)   # led = off
OFF = const(1)  # led = on


def setup(on_off=OFF):
    """setup(on_off) - setup LED array
        state=on or off, default OFF.
        returns list of leds. """
    leds = []
    leds.append(Pin.exp_board.G28)
    leds.append(Pin.exp_board.G22)
    leds.append(Pin.exp_board.G17)
    leds.append(Pin.exp_board.G16)

    leds.append(Pin.exp_board.G15)
    leds.append(Pin.exp_board.G14)
    leds.append(Pin.exp_board.G11)
    leds.append(Pin.exp_board.G24)

    for pin in leds:
        pin.mode(Pin.OUT)
        pin.pull(Pin.PULL_DOWN)
        pin.value(on_off)
        # print(pin)

    return leds


def displayBinary(leds, decimalNumber):
    # format given decimal...convert to binary..
    # Total number of bits is 8...zero padding....
    binaryString = '{0:08b}'.format(decimalNumber)
    # i = len(pins) - 1  # count from left to right on LED array
    i = 0  # count from right to left on LED array
    for led in leds:
        # not is necessary because LED array has reversed polarity
        # i.e '0' is on, '1' is off
        led.value(not int(binaryString[i]))
        # i -= 1   # LED order: from left to right
        i += 1  # LED order: from right to left


def main(maximum, dt=0.5):
    leds = setup(OFF)
    while True:  # include for restart binaire counter
        print('Start binaire counter', end='... ')
        for i in range(0, maximum):
            displayBinary(leds, i)
            sleep(dt)
        print("{}".format(i+1))
        sleep(10*dt)


if __name__ == '__main__':
    # test()
    main(32, 0.1)  # 2**5
    # main(64, 0.2)  # 2**6
    # main(256, 0.1)  # 2**8
