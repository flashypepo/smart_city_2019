"""
demo program for a servo DG90
* includes assert ad subclassing

SG90 servo:
Vcc = 5V, signal=3V3 (Gxx/Pyy).
   Level-shifter to connect 5V line with 3V3 line.

PWM Pycom documentatie
https://docs.pycom.io/firmwareapi/pycom/machine/pwm

ELO documentation:
M2M 2019-2020.pdf

GitHub code:
https://github.com/flashypepo/smart_city_2019/tree/master/workshops/sample-code

2020-0402 PP new, SG90 hobby servo
"""

from machine import Pin
from time import sleep

from servo90 import Servo90

# device configuration
DEFAULT_SERVOPIN = Pin.exp_board.G15  # 'P8'
# servo SG90: minimm ad maxum duty-cycle values
# to calibrate a servo. Trial-and error values
DEFAULT_MAX_RIGHT = 0.025  # servo max right (0 degree)
DEFAULT_MAX_LEFT = 0.116   # servo max left (180 degree)


class ServoSG90Demo():

    def __init__(self):
        self._servo = Servo90()  # servo connected to Expansionboard G15/P8
        # servo = Servo90(servoPin='P8')  # servo connected to customized pin

        self._servo.calibrate()  # use default values
        # using customized calibration values:
        # servo.calibrate(DEFAULT_MAX_RIGHT, DEFAULT_MAX_LEFT)

    def run(self, angle=90, n=5, delay=1):
        print('servo turns {} degrees'.format(angle))
        self._servo.rotate(angle)

        sleep(4)  # demo time: wait before the sweep

        try:
            # sweep servo a number of times
            print('servo sweeps back and forth {} times...'.format(n))
            self._servo.sweep(n, delay)
            self._servo.stop()
            self._servo.rotate(angle)
            print("Servo demo done")
        except KeyboardInterrupt:
            self._servo.stop()
            print("Servo demo interrupted")


if __name__ == '__main__':
    # servo SG90 - a regular hobby servo
    # It rotatation range 0 .. 180 graden (in principe)
    app = ServoSG90Demo()  # use default servo pin
    app.run()  # default values
    app.run(n=10)
    print("Servo testdemo done")
