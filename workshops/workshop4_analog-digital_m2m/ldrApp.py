"""
ldrApp - lightsensor example
- reading values from lightsensor LDR

LDR - analog IO sensor
for example LDR connected to GPIO-pin G5 (G3)

"""
from machine import ADC
import _thread
import time

USE_DEBUG = True  # 2019-0924 changed


class LDRApp():

    def __init__(self, pin, attn):
        self._adc = ADC(0)  # create ADC
        # create a LDR channel with attn
        self._ldr = self._adc.channel(pin=pin, attn=attn)
        self._pin = pin
        self._display = None

    @property
    def ldr(self):
        return self._ldr

    @property
    def setDisplay(self):
        return self._display

    # 2019-0917 is setter is defined, you must also define a getter
    @setDisplay.setter
    def setDisplay(self, display=None):
        """ setter for display attribute.
            Example: app.setDisplay = oled """
        self._display = display

    # print data on console
    def showOnConsole(self, value, isVoltage):
        """ show LDR-value on console,
            value is voltage (isVoltage=True)
            or raw value otherwise."""
        msg = 'LDR value: {}'.format(value)
        if isVoltage:
            msg = 'LDR: {} mV'.format(value)
        print(msg)

    # print data on attached display
    def showOnDisplay(self, value, isVoltage=False):
        """ show LDR-value on display,
            value is voltage (isVoltage=True)
            or raw value otherwise."""
        header = 'LDR value:'
        valueStr = '  {:04d}'.format(value)
        if isVoltage:
            header = 'LDR voltage:'
            valueStr = '  {:3.2f} V'.format(value / 1000)
        self._display.fill(0)
        self._display.text(header, 0, 0)
        self._display.text(valueStr, 0, 10)
        self._display.show()

    # ADC - get readings from LDR and display data
    def showLDRvalues(self, isVoltage=False, dt=1):
        while True:
            value = self._ldr.value()
            if isVoltage:
                value = self._ldr.value_to_voltage(value)
            if self._display is not None:
                self.showOnDisplay(value, isVoltage)
            elif USE_DEBUG:
                self.showOnConsole(value, isVoltage)
            time.sleep(dt)

    def run(self, dt=10):
        _thread.start_new_thread(self.showLDRvalues, (True, dt))


if __name__ == '__main__':
    from lopy4_board import G3
    attn = [ADC.ATTN_0DB,
            ADC.ATTN_2_5DB,
            ADC.ATTN_6DB,
            ADC.ATTN_11DB]
    app = LDRApp(G3, attn[3])
    app.run()  # default 10 seconds, faster -> OLED problem
    ldr = app.ldr  # get LDR-sensor
    print('LDR sensor: {}'.format(ldr))
    # app.setDisplay = oled   # inject OLED display
