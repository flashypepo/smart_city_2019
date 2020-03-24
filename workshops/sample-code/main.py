"""
main.py - collection of GPIO examples.

main.py is splitup in various modules,
Each module can be found in folder examples/gpio.

1. blinking RGB-led
2. pulserende LED
3. binaire LED counter
4. OLED-display

History
2020-03 PP new, main calls applications, nothing less, nothing more
firmware v1.20.2.rc6 (pybytes)
"""

# execution of the various demos
if __name__ == '__main__':
    print('\nEntering main.py...')

    # activate/deactivate various demo's

    # workshop: demo - 'Hello World'
    # blink RGBLed of the LoPy4
    DEMO_BLINKING_RGB = False

    # GPIO-demos
    # workshop: demo's
    # =============================
    # Setting: PCB led, button, potentiometer
    # =============================
    # === digital output: - external led ON / OFF
    DEMO_EXTERNAL_LED = False  # external LED
    DEMO_BUTTON = False        # external button

    # ==== digital input and output: button + led
    DEMO_BUTTON_LED = False    # button clicked -> LED on

    # Analoge input and output: ADC
    DEMO_ADC = False  # ADC input - potentiometer

    # LATER demo
    DEMO_LED_DIMMER = False  # Led dimmer (requires PWM)

    # =============================
    # Setting: breadboard multiple leds
    # EXERCISE DEMO - show no code
    # =============================
    # binaire counter (multiple leds)
    DEMO_BINAIRE_COUNTER = False  # binaire counter

    # =============================
    # Setting: PCB multiple sensors,
    #              actuators, battery-feeded
    # =============================
    # LATER demos
    DEMO_PULSING_LED = False  # pulse external led

    # i2c - display/actuator
    DEMO_OLED_DISPLAY = False  # OLED display

    # SPI - TFT-display/actuator
    # TFT 1.8' 160*128 ST7735S
    DEMO_TFT_DISPLAY = False

    # neopixels, 8-stick, level-shifter
    DEMO_NEOPIXELS = True

    # Various sensors
    DEMO_HSR04 = True    # HSR04 ultrasonic proximity sensor (digital)
    DEMO_PIR = False     # PIR, IR proximity sensor (analog)
    DEMO_CSS811 = False  # Air quality sensor (I2C)
    DEMO_SGP30 = False   # another air quality sensor (I2C)

    #################################
    # execute the GPIO examples
    #################################
    # 2020-0321 TFT display
    if DEMO_TFT_DISPLAY is True:
        from examples.display import tftApp
        tftApp.main()

    # 2020-03 PP: OLED first, then other applications can be executed too.
    if DEMO_OLED_DISPLAY is True:
        from time import sleep
        from machine import I2C
        # from ssd1306 import SSD1306_I2C as ssd
        from lopy4board import I2C_SCL, I2C_SDA
        from examples.i2c import oledApp

        # TODO: move i2c to boot.py
        i2c = I2C(0, I2C.MASTER, baudrate=100000, pins=(I2C_SDA, I2C_SCL))
        print('i2c scan:', i2c.scan())

        app = oledApp.OLEDApp(i2c=i2c, width=128, height=32)
        app.whiteScreen(refresh=True)
        sleep(3)
        msg = {
            'Welkom': (0, 0),
            'Smart': (30, 10),
            'citizens!': (60, 20),
        }
        app.showText(msg)
        # get OLED-object to use as display in other applications
        display = app.oled

    # built-in RGB led - digital IO
    if DEMO_BLINKING_RGB is True:
        from examples.gpio import HelloWorldRGBled
        HelloWorldRGBled.main()

    # external LED - digital IO
    if DEMO_EXTERNAL_LED is True:
        from machine import Pin
        from examples.gpio import external_gpio
        led = external_gpio.Led(pin=Pin.exp_board.G28)
        led.demo(5)

    # external button - digital IO
    if DEMO_BUTTON is True:
        from machine import Pin
        from examples.gpio import external_gpio
        button = external_gpio.Button(pin=Pin.exp_board.G22)
        button.demo(5)

    # button + LED - digital IO
    if DEMO_BUTTON_LED is True:
        from machine import Pin
        from examples.gpio import external_gpio
        led = external_gpio.Led(pin=Pin.exp_board.G28)
        buttonled = external_gpio.ButtonLed(led=led, pin=Pin.exp_board.G22)
        buttonled.demo(5)

    # ADC input - potentiometer
    if DEMO_ADC is True:
        from machine import Pin
        from examples.gpio import external_gpio
        adc = external_gpio.AnalogDigital(Pin.exp_board.G5)
        adc.demo()
        pass

    # ADC input - Led output
    if DEMO_LED_DIMMER is True:
        from machine import Pin
        from examples.gpio import external_gpio
        led = external_gpio.Led(pin=Pin.exp_board.G28)
        adc = external_gpio.ADCLed(led=led, pin=Pin.exp_board.G5)
        pass

    # Neopixels demo
    if DEMO_NEOPIXELS is True:
        from examples.display import neopixelsApp
        neopixelsApp.main()

    if DEMO_HSR04 is True:
        # TODO: from examples.proximitysensors import hsr04App
        # TODO: hsr04App.main()
        from machine import Pin
        from hsr04 import HSR04
        echoPin = Pin.exp_board.G7
        triggerPin = Pin.exp_board.G8
        sensor = HSR04(echoPin, triggerPin)
        try:
            while True:
                distance = sensor.distance_median()
                print("Distance: {:00.1f} cm".format(distance))
        except KeyboardInterrupt:
            print('done!')

    # more advanced demos or
    # exercise solution samples
    if DEMO_PULSING_LED is True:
        from examples.gpio import pulsing_led
        pulsing_led.main()

    if DEMO_BINAIRE_COUNTER is True:
        from examples.gpio import binaire_counter
        binaire_counter.main(maximum=256, dt=0.1)

    # cleanup
    import gc
    gc.collect()
    print('main(): free memory {} Kb'.format(gc.mem_free() // 1024))
    print('main done')
