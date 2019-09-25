'''
servoApp - servo application
2019-0917 added sweep demo
'''
from machine import PWM
import time
import _thread

USE_DEBUG = False  # 2019-0917 changed


class ServoSweepApp:
    def __init__(self, servoPin, servoRange):
        self._pwm = PWM(0, frequency=50)
        self.servo = self._pwm.channel(0,
                                       pin=servoPin,
                                       duty_cycle=servoRange[0] / 1000.0
                                       )
        self._pin = servoPin
        self._range = servoRange
        time.sleep(4)
        if USE_DEBUG:
            print('servoRange: {} - {}'.format(self._range[0],
                                               self._range[-1] + 1))
        self._display = None  # no display attached

    @property
    def setDisplay(self):
        return self._display

    # 2019-0917 is setter is defined, you must also define a getter
    @setDisplay.setter
    def setDisplay(self, display=None):
        """ setter for display attribute.
            Example: app.setDisplay = oled """
        self._display = display

    def start(self):
        """start() - put servo at _range[0] position"""
        self.servo.duty_cycle(self._range[0] / 1000.0)
        time.sleep(1)

    # 2019-0917 an improvement will be to do display in a thread
    # only when dt > 10 seconds, else too fast and I2C-errors
    def showOnDisplay(self, smin, smax, step):
        self._display.fill(0)
        self._display.text('- Sweep servo -', 10, 0)
        self._display.text('min: {}'.format(smin), 0, 10)
        self._display.text('max: {}'.format(smax), 0, 20)
        self._display.show()

    def sweep(self, min, max, step):
        """ sweeps servo from min to max in steps"""
        if USE_DEBUG:
            print('sweep({}, {}, {})'.format(min, max, step))
        if self._display is not None:
            self.showOnDisplay(min, max, step)
        for i in range(min, max, step):
            self.servo.duty_cycle(i / 1000.0)
            time.sleep(0.1)

    # def backAndForth(servo, min=40, max=120, dt=4):
    def backAndForth(self, dt=4):
        """sweeps servo in servoRange and back..."""
        while True:
            smin = self._range[0]
            smax = self._range[-1] + 1
            self.sweep(smin, smax, 1)
            time.sleep(dt//2)
            self.sweep(smax, smin, -1)
            time.sleep(dt)

    def run(self):
        """ run: do your thing"""
        self.start()   # put servo at start position
        _thread.start_new_thread(self.backAndForth, (4, ))


if __name__ == '__main__':
    from lopy4_board import G12
    # servo is attached to GPIO-pin G12
    servoPin = G12
    # servo range hobby-sevo SG90: 0.127 .. 0.040
    # servo range Tower Pro MG90S: 0.120 .. 0.040
    # servoRange = range(40, 128)  # servo Hobby servo SG90
    servoRange = range(30, 120)  # servo: Tower pro MG90S
    servo = ServoSweepApp(servoPin, servoRange)
    servo.run()
