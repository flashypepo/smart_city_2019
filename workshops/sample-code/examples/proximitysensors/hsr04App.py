"""
application which displays distance with an HSR04 ultrsonic distance sensors

2020-0324 PP new
"""
from machine import Pin
from utime import sleep_ms
from hsr04 import HSR04

# Device configuration
echoPin = Pin.exp_board.G7
triggerPin = Pin.exp_board.G8


class App():

    def __init__(self, display=None):
        self._sensor = HSR04(echoPin, triggerPin)
        self._display = display

    def show(self, message):
        if self._display is None:
            print(message)

    def run(self, display=None, delay=20):
        try:
            self.show("Distance Sensor...")
            while True:
                distance = self._sensor.distance_median()
                self.show("Distance: {:00.1f} cm".format(distance))
                sleep_ms(delay)
        except KeyboardInterrupt:
            self.show('done!')

    @property
    def display(self):
        return self._display

    @display.setter
    def display(self, display):
        self._display = display


if __name__ == '__main__':
    app = App(display=None)
    app.run()
