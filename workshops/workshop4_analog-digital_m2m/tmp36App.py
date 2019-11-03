"""
tmp36App - reading and showing temperature
           from analog temperature sensor TMP36

TMP36 - analog IO sensor for example
        connected to pin G3/P16

Sample from:
https://core-electronics.com.au/tutorials/temperature-sensing-pycom-tmp36-tutorial.html

"""
from machine import ADC
import _thread
import time

USE_DEBUG = False  # 2019-0927 changed


class TMP36App():

    def __init__(self, pin):
        self._adc = ADC()  # create ADC object
        # create an analog pin on 'pin' & connect TMP36
        self._adc_c = self._adc.channel(pin=pin)
        self._pin = pin
        self._display = None

    @property
    def tmp36(self):
        """ return sensor/channel object"""
        return self._adc_c

    @property
    def setDisplay(self):
        return self._display

    # 2019-0917 if setter is defined, you must also define a getter
    @setDisplay.setter
    def setDisplay(self, display=None):
        """ setter for display attribute.
            Example: app.setDisplay = oled """
        self._display = display

    def calculate_temperature(self, value):
        """calculate_temperature(value): return temperature from value."""
        # LoPy  has 1.1 V input range for ADC
        # datasheet TMP36
        # TODO: use adc_c.vRef instead of hard-coded "1100"?
        return ((value*1100)/4096-500)/10

    # print data on console
    def showOnConsole(self, temperature):
        """ show temperature from TMP36 on console."""
        msg = 'Temperature = {:5.1f}'.format(temperature)
        print(msg)

    # print data on attached display
    def showOnDisplay(self, temperature):
        """ show value from TMP36 as temperature on console."""
        header = 'Temperature'
        msg = '{:5.1f}'.format(temperature)
        self._display.fill(0)
        self._display.text(header, 0, 0)
        self._display.text(msg, 0, 10)
        self._display.show()

    # ADC - get readings from TMP36 and display data
    def showValues(self, dt=1):
        while True:
            value = self._adc_c()  # read ADC count
            temperature = self.calculate_temperature(value)
            if self._display is not None:
                self.showOnDisplay(temperature)
            if USE_DEBUG:
                self.showOnConsole(temperature)
            time.sleep(dt)

    def run(self, dt=10):
        _thread.start_new_thread(self.showValues, (dt,))


if __name__ == '__main__':
    '''
    from lopy4_board import G3
    from machine import ADC
    import time
    # Measuring temperature by TMP36
    adc = ADC()               # create an ADC object
    apin = adc.channel(pin=G3)   # create an analog pin on P16 & connect TMP36
    while True:
        print("")
        print("Reading TMP36 Sensor...")
        value = apin()
        print("ADC count = %d" %(value))
        # LoPy  has 1.1 V input range for ADC
        temp = ((value * 1100 ) / 4096 - 500) / 10
        print("Temperature = %5.1f C" % (temp))
        time.sleep(2)
    '''
    """ attenuation factor is not needed...
    attn = [ADC.ATTN_0DB,
            ADC.ATTN_2_5DB,
            ADC.ATTN_6DB,
            ADC.ATTN_11DB] """
    print("Reading and displaying TMP36 Sensor values...")
    app = TMP36App(G3)
    app.run(2)  # default 10 seconds, faster -> OLED problem
    pin, sensor = app.tmp36  # get LDR-sensor
    print('Sensor pin: {}\n Sensor: {}'.format(pin, sensor))
    # app.setDisplay = oled   # inject OLED display
