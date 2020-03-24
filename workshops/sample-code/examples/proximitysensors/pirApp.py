"""
application which detects an object via infrared (PIR sensor)

2020-0324 PP new WORK_IN_PROGRESS
"""
from machine import Pin
from utime import sleep_ms
# TODO: from pir import PIR

# Device configuration
pirPin = Pin.exp_board.G9


class App():

    def __init__(self, display=None):
        pass
        # self._sensor = PIR(pirPin)
        self._display = display

    def show(self, message):
        if self._display is None:
            print(message)
        # else:
        #     self._display.print(message)

    def run(self, display=None, delay=20):
        pass
        # try:
        #     self.show("Detecting object...")
        #     while True:
        #         isdetected = self._sensor.detect()
        #         if isDetected is True:
        #             self.show("Detection: {}".format(isdetected))
        #         sleep_ms(delay)
        # except KeyboardInterrupt:
        #     self.show('done!')

    @property
    def display(self):
        return self._display

    @display.setter
    def display(self, display):
        self._display = display


if __name__ == '__main__':
    app = App(display=None)
    app.run()
