"""
class Servo90 for a SG90 servo (smart city)

OPDRACHT:
Maak de methode get_duty(), waarin een angle wordt omgezet
in een valide duty-cycle waarde.
Valide: de berekende duty_cycle waarde ligt tussen
        DEFAULT_MAX_RIGHT en DEFAULT_MAX_LEFT.

2020-04 PP smart city - semester 2
"""
import machine
import time

DEFAULT_SERVOPIN = machine.Pin.exp_board.G15  # 'P8'
# servo SG90: trial-and-error for default values
DEFAULT_MAX_RIGHT = 0.025  # servo max right (0 degree)
DEFAULT_MAX_LEFT = 0.116   # servo max left (180 degree)


class Servo90(object):
    def __init__(self, servoPin=DEFAULT_SERVOPIN, duty_c=0):
        self.pwm = machine.PWM(0, frequency=50)
        self.pwm_c = self.pwm.channel(0, pin=servoPin, duty_cycle=duty_c)
        self.calibrate()  # calibrate servo with default values

    def calibrate(self, max_right=DEFAULT_MAX_RIGHT,
                  max_left=DEFAULT_MAX_LEFT):
        self._max_range = (max_right, max_left)
        assert(self._max_range[0] < self._max_range[1])  # check valide values

    def get_duty(self, angle):
        """ get_duty(angle): calculates and returns a valid
            duty_cycle value ('duty') for the 'angle'.
        """
        # bereken de duty-waarde waarbij je de angle interpoleert
        # tussen max_right (0 degrees) en max_left (180 degrees)
        # aanname: linear interpolation

        # ... jouw code

        # check met 'assert(conditie)'' dat berekende duty
        # een valide waarde is
        # ... jouw code

        return duty

    def rotate(self, angle):
        # map angle to a valid duty_cycle value
        duty = self.get_duty(angle)
        max_right = self._max_range[0]
        max_left = self._max_range[1]
        # DEBUG: print("duty={0} in range(0={1}, 180={2})".format(duty, max_right, max_left))
        self.pwm_c.duty_cycle(duty)

    def stop(self):
        self.pwm_c.duty_cycle(0)

    # demo servo: sweep from left to right and back
    def sweep(self, n=5, delay=5):
        counter = 1
        while counter <= n:
            # go from 0 to 180 degree:
            print("{}: servo from 0 -> 180".format(counter))
            for angle in range(0, 180, 10):
                self.rotate(angle)
                # time.sleep(0.1)
            time.sleep(delay)
            # go from 180 to 0 degree:
            print("{}: servo from 180 -> 0".format(counter))
            for angle in range(180, 0, -10):
                self.rotate(angle)
                # time.sleep(0.5)
            time.sleep(delay)
            counter += 1


if __name__ == '__main__':
    # servo SG90 - rotation range 0 .. 180 graden (in principe)
    servo = Servo90()
    servo.calibrate()  # use default calibration values
    # servo.calibrate(0.034, 0.11)  # use customized calibration values
    rotation = 45
    print('rotate servo...{} graden'.format(rotation))
    servo.rotate(rotation)

    # sweep servo n times
    servo.sweep(delay=1)
