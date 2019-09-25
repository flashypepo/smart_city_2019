"""
main.py - main startup of workshop 4  analog and digital IO,
sensors and actuators
2019-0917 Peter - split up in modules
2019-0912 Peter - workshop 4 sample code

System configuration:
sensor/actuator       | GPIO-pin        | class
----------------------------------------------
digitalIO - leds      | G15, G28        | ledsApp
analogIO - TMP36      | G3              | tmp36App
OLED i2c              | I2C_SCL / G16   | SSD1306_I2C
                      | I2C_SDA / G17   |
actuator - servo      | G12             | servoApp
I2C-LCD display       | I2C_SCL/I2C_SDA | I2cLcd(LcdApi)
   2 * 16 chars       |                 |
digitalIO - neopixels | Gxx             | neopixelsApp
analogIO - LDR        | G5              | ldrApp

"""
import micropython
import pycom
import time
import _thread
import gc

from machine import Pin, ADC
from lopy4_board import G3, G12, G22, G28, G15, G31
from lopy4_board import I2C_SCL, I2C_SDA


DEBUG = False  # to DEBUG or not

# device configuration:
# analog/digital IO, sensors/actuator, I2C/SPI
USE_LEDS = True           # digital IO: actuator - using leds
USE_TMP36 = True         # analog IO: (ambient)temperature sensor
USE_OLED_I2C = True       # I2C: using OLED-I2C display
USE_SERVO = True         # PWM: actuator - servo
USE_NEOPIXELS = True     # digital IO: actuator - using neopixels (5V)
USE_LCD_I2C = True       # I2C: 2*16 chars LCD display - 5V/level-shifter

USE_LDR = False            # analog IO, sensor - using lightsensor
USE_DISPLAY_SPI = False   # SPI: using TFT-SPI display


if __name__ == '__main__':
    print('workshop 4 sample code...')
    gc.collect()  # trial-and-error garbage collect

    # DIGITAL IO: LEDS
    print('DIGITAL IO - blinking LEDS...{}'.format(USE_LEDS))
    if USE_LEDS:
        from ledsApp import BlinkLedsApp
        gc.collect()  # trial-and-error garbage collect
        pins = [G28, G15]  # lege lijst,[], is test for exception!
        try:
            leds = BlinkLedsApp(pins)
            leds.run(dt=0.5)
        except Exception as ex:
            print(ex)
            print('Led blinking stopped')
            pass  # continue

    # 2. OLED-I2C display
    print('OLED-I2C display...{}'.format(USE_OLED_I2C))
    if USE_OLED_I2C:
        from oledApp import OLEDApp
        gc.collect()  # trial-and-error garbage collect
        app = OLEDApp(i2c=i2c, width=128, height=32)
        msg = {
            'Welkom': (0, 0),
            'Smart': (30, 10),
            'citizens!': (60, 20),
        }
        app.welcome(msg)
        oled = app.oled
        print('\tOLED:', oled)

    # LCD_I2C display
    print('LCD-I2C display...{}'.format(USE_LCD_I2C))
    if USE_LCD_I2C:
        from esp8266_i2c_lcd import I2cLcd
        gc.collect()  # trial-and-error garbage collect
        DEFAULT_I2C_ADDR = 0x27
        lcd = I2cLcd(i2c, DEFAULT_I2C_ADDR, 2, 16)
        lcd.show_cursor()
        lcd.blink_cursor_on()
        lcd.putstr("Hello Smart\nWorld! It works!")
        lcd.hide_cursor()
        time.sleep(5)
        lcd.clear()
        lcd.run()  # internal LCD demo in thread!

    # Servo motor on pin G12 / P5, PWM
    # https://development.pycom.io/firmwareapi/pycom/machine/pwm/
    print('Servo ...{}'.format(USE_SERVO))
    if USE_SERVO:
        from servoApp import ServoSweepApp
        gc.collect()  # trial-and-error garbage collect
        # servo is attached to GPIO-pin G12
        servoPin = G12
        # servo range hobby-servo SG90: 0.127 .. 0.040
        # servo range Tower Pro MG90S: 0.120 .. 0.040
        # servoRange = range(40, 128)  # servo Hobby servo SG90
        servoRange = range(30, 120)  # servo: Tower pro MG90S
        servo = ServoSweepApp(servoPin, servoRange)
        servo.run()

    print('Neopixels ...{}'.format(USE_NEOPIXELS))
    # neopixels hebben 5V nodig -> level-shifter
    # source: https://core-electronics.com.au/tutorials/WS2812_and_NeoPixel_with_Pycom.html
    if USE_NEOPIXELS:
        from ws2812 import WS2812
        gc.collect()  # trial-and-error garbage collect
        numLed = 37
        chain = WS2812(ledNumber=numLed, brightness=10, dataPin=G22)
        data = [(0, 125, 0)] * numLed  # demo green pixels
        chain.show(data)
        time.sleep(5)
        # run the animations from sample code - see source
        from neopixelsApp import npDemo
        _thread.start_new_thread(npDemo, (0, ))

    # Analog IO, sensor: TMP36 on pin G3/P16
    # https://core-electronics.com.au/tutorials/temperature-sensing-pycom-tmp36-tutorial.html
    # Hardware: Vcc = 3.3V
    print('Temperature sensor TMP36 ...{}'.format(USE_TMP36))
    if USE_TMP36:
        from tmp36App import TMP36App
        tmpApp = TMP36App(G3)
        tmpApp.run(dt=1)
        sensor = tmpApp.tmp36  # get sensor-object
        print('\tTMP36 sensor: {}'.format(sensor))
        tmpApp.setDisplay = oled   # inject OLED display

    # Analog IO, sensor: ADC - LDR on pin G31/P17
    # https://core-electronics.com.au/tutorials/sensing-light-with-ldr-and-pycom-lopy4.html
    # Hardware: voltage divider required with 10K resistor.
    print('Analog lightsensor ...{}'.format(USE_LDR))
    if USE_LDR:
        from ldrApp import LDRApp
        """ not required:
        attn = [ADC.ATTN_0DB,
                ADC.ATTN_2_5DB,
                ADC.ATTN_6DB,
                ADC.ATTN_11DB]"""
        ldrApp = LDRApp(G31)
        ldrApp.run(dt=1)
        ldr = ldrApp.ldr  # get LDR-sensor
        print('\tLDR sensor: {}'.format(ldr))
        # ldrApp.setDisplay = oled   # inject OLED display

    # sensor -> actuator:
    # lightsensor value -> servo, kind of analog meter
    # opdracht
    print('Analog meter ... Opdracht!')
