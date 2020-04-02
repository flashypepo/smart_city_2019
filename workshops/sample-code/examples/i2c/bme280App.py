'''
  BE280/BMP280 temperature sensor application
  pin sensor  LoPy4
  SCL         P8 / G15
  SDA         P9 / G16
  VIN         3.3V
  GND         GND

2020-0402 PP new class BME280DemoApp, smart city 2020 semester 2
#'''
from micropython import const
import machine
import time
import json
import bme280   # required in lib-folder
from bme280 import BME280


class BME280DemoApp():
    # create a bme280 object
    def __init__(self, i2c):
        self._bme = bme280.BME280(i2c=i2c)

    # helper function: Celsius to Fahrenheit
    # Exercise 2018: requires temperature as raw value from bme20 module. Change library.
    def fahrenheit(self, temperature):
        """ temperatue in Celsius"""
        return (temperature * 9/5) + 32

    def bme2json(self, values):
        """ returns sensor values as JSON"""
        dict = {}  # store data in dict
        dict['temp'] = values[0]
        # print(dict['temp'])
        dict['pressure'] = values[1]
        # print(dict['pressure'])
        dict['humidity'] = values[2]
        # print(dict['humidity'])
        # dict['internal'] = machine.internal_temp()[1] #ESP32 temperature sensor
        return json.dumps(dict)  # JSON format

    # run sensor reading, Ctrl-C to abort
    def run(self, display=None, delay=2):
        print("Demo: BME280 values on display of cnsole")

        while True:
            values = self._bme.values
            # splits values into temperature, pressure and humidity
            t, p, h = values
            if display is not None:
                display.fill(0)
                display.text('Temp: {:}'.format(t), 0, 0)
                display.text('Pres: {:}'.format(p), 0, 13)
                display.text('Hum: {:}'.format(h), 0, 23)
                display.show()
            else:
                print('BME280 values: ', values)
                print('JSON:', self.bme2json(values))

            # wait > 2 sec, see datasheet
            delay = 2 if delay < 2 else delay
            time.sleep(delay)


if __name__ == '__main__':
    # i2c must be created
    app = BME280DemoApp(i2c)
    app.run(display=None, delay=3)
