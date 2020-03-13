"""
 external_gpio
- class Led  - external Led connected to a GPIO
- class Button  - external Button connected to a GPIO
- class ButtonLed - Button controls a Led
# firmware 1.20.2.rc6
# 2020-03 PP Smart City semester 2 - new
#  software engineering: encapsulate code in OOP classes
"""
from machine import Pin, ADC
import time


# external LED attached to a GPIO-pin
class Led():
    def __init__(self, pin):
        self._ledPin = Pin(pin, Pin.OUT)

    def on(self):
        # DEBUG: print('led on...')
        self._ledPin.value(1)
        pass

    def off(self):
        # DEBUG: print('led off...')
        self._ledPin.value(0)
        pass

    def toggle(self, cycle=5, dt=1):
        print('Toggel led on/off {} times'.format(cycle))
        for i in range(cycle):
            self.on()
            time.sleep(dt)
            self.off()
            time.sleep(dt)

    @property
    def pin(self):
        return self._ledPin

    def demo(self, cycle=5):
        print('Demo Led at GPIO {}...'.format(self._ledPin.id()))
        self.on()
        time.sleep(1)
        self.off()
        time.sleep(1)
        self.toggle(cycle, 0.5)
        time.sleep(1)
        print('Demo done')


# external button attached to a GPIO-pin
class Button():
    def __init__(self, pin):
        self._buttonPin = Pin(pin, Pin.IN)

    def value(self):
        return self._buttonPin.value()

    def demo(self, cycle=5):
        print("Demo Button at GPIO '{}'...".format(self._buttonPin.id()))
        count = 0
        while count < 6:
            if self.value() == 1:
                print('button pressed {} times'.format(count))
                count += 1
            time.sleep(0.1)
        print('Demo done')


class ButtonLed():
    def __init__(self, pin, led=None):
        self._buttonPin = Pin(pin, Pin.IN)
        self._led = led

    # Wrapper
    @property
    def value(self):
        """ value() - returns 1 if button pressed,
                      otherwise returns 0."""
        return self._buttonPin.value()

    @property
    def led(self):
        return self._led

    @property
    def pin(self):
        return self._buttonPin

    def demo(self, cycle=5):
        print("Demo Button (GPIO '{}')".format(self.pin.id()))
        if self._led is not None:
            print("\tcontrols Led (GPIO '{}')".format(self.led.pin.id()))
        count = 0
        while count < 6:
            if self.value == 1:   # button pressed?
                print('button pressed {} times'.format(count))
                if self._led is not None:
                    self._led.on()
                count += 1
            else:
                if self._led is not None:
                    self._led.off()

            time.sleep(0.1)
            if self._led is not None:
                # always exit with led off
                self._led.off()
        print('Demo done')
# TODO: ButtonLed inherits from Button


class AnalogDigital():
    def __init__(self, pin):
        self._adc = ADC(0)
        self._adc_c = self._adc.channel(pin=pin, attn=ADC.ATTN_11DB)
        self.calibrate(reference=1100)  # a default reference value

    def calibrate(self, reference=1100):
        """ Set calibration of ADC channel"""
        # Output Vref of P22
        self._adc.vref_to_pin('P22')
        self._adc.vref(reference)

    @property
    def voltage(self):
        """ voltage() - returns voltage in mV from ADC-pin."""
        return self._adc_c.voltage()

    @property
    def value(self):
        """ value() - returns raw value from ADC-pin."""
        return self._adc_c.value()

    def demo(self, dt=1):
        print("Demo ADC: {}".format(self._adc_c))
        try:
            adc_fmt = 'ADC: voltage={0:4.2f}V, value={1}'
            while True:
                print(adc_fmt.format(self.voltage / 1000, self.value))
                time.sleep(dt)
        except KeyboardInterrupt:
            print('Demo done')


# TODO: Led dimmer, requires PWM
# TODO: LedDimmer inherits from Led and uses AnalogDigital
class LedDimmer(Led):
    def __init__(self, pin, led=None):
        self._adc = AnalogDigital(pin=pin)
        #self._adc = ADC(0)
        #self._adc_c = self._adc.channel(pin=pin, attn=ADC.ATTN_11DB)
        #self.calibrate(reference=1100)  # a default reference value
        self._led = led

    # Wrappers
    @property
    def voltage(self):
        """ voltage() - returns voltage in mV from ADC-pin."""
        return self._adc.voltage

    @property
    def value(self):
        """ value() - returns raw value from ADC-pin."""
        return self._adc.value

    def demo(self, dt=1):
        print("Demo led dimmer: {}".format(self._adc))
        if self._led is not None:
            print("\tcontrols Led (GPIO '{}')".format(self._led.pin.id()))
        try:
            adc_fmt = 'dimmer: voltage={0:4.2f}V, value={1}'
            while True:
                print(adc_fmt.format(self.voltage / 1000, self.value))
                time.sleep(dt)
        except KeyboardInterrupt:
            print('Demo done')


if __name__ == '__main__':
    import time

    '''
    # only a button
    button = Button(pin=Pin.exp_board.G22)
    button.demo(5)
    '''
    # demo: button presed -> Led on
    #led = Led(pin=Pin.exp_board.G28)
    #button = ButtonLed(led=led, pin=Pin.exp_board.G22)
    #button.demo(5)

    # '''

    '''  Analog input -> digital
    # using a potentiometer
    # also applicable for LDR, TMP36, ...
    adc = AnalogDigital(pin=Pin.exp_board.G5)
    adc.demo(0.5)  # seconds delay between readings
    '''
    # demo: Led dimmer
    # A potentiometer controls brigtness of LED
    # requires PWM.   TODO
    led = Led(pin=Pin.exp_board.G28)
    dimmer = LedDimmer(led=None, pin=Pin.exp_board.G5)
    dimmer.demo(0.5)  # seconds delay between readings
    # '''

# opdracht: bouw "button debounce" in.
