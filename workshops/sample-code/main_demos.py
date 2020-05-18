"""
main.py - collection of GPIO examples.

main.py is splitup in various modules,
Each module can be found in folder examples

History
2020-0326 PP added Lorawan scanner, PIR sensor app
2020-03 PP new, main calls applications, nothing less, nothing more
firmware v1.20.2.rc6 (pybytes)
"""

# execution of the various demos
if __name__ == '__main__':
    print('\nEntering main.py...')

    ###############################################
    # Configuration of the various demo's / samples
    ###############################################
    DEMO_BLINKING_RGB = False  # blink RGBLed of the LoPy4
    DEMO_EXTERNAL_LED = False  # external LED
    DEMO_BUTTON = False        # external button (polling)
    DEMO_BUTTON_LED = False    # button clicked -> LED on
    DEMO_ADC = False           # ADC input - potentiometer
    DEMO_LED_DIMMER = False    # TODO: Led dimmer (requires PWM)
    DEMO_BINAIRE_COUNTER = False  # binaire counter (multiple leds)
    DEMO_PULSING_LED = False   # TODO pulse external led
    DEMO_OLED_DISPLAY = False  # TODO: I2C - OLED display
    DEMO_TFT_DISPLAY = False   # TODO: SPI - TFT 1.8' 160*128 ST7735S
    DEMO_NEOPIXELS = True     # neopixels chain (via level-shifter, good power supply)
    DEMO_HSR04 = True         # HSR04 ultrasonic proximity sensor (digital)
    DEMO_PIR = True            # PIR, IR proximity sensor
    DEMO_CSS811 = False        # TODO: Air quality sensor (I2C)
    DEMO_SGP30 = False         # TODO: another air quality sensor (I2C)
    DEMO_LORAWAN_TTN = False   # 2020-0326 joined TTN via LorawWan succesfully

    #########################################
    # Projects i.e. combination of sensors
    #########################################
    # distance controls color of neopixel chain
    PROJECT_HSR04_NEOPIXELS = False  # TODO: work in progress

    #########################################
    # execute the DEMO examples when selected
    #########################################
    # TFT display
    if DEMO_TFT_DISPLAY is True:
        print("TFT display (spi)... TODO")
        from examples.display import tftApp
        tftApp.main()

    # OLED display
    if DEMO_OLED_DISPLAY is True:
        print("OLED display (i2c)...")
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
        print("Internal RGBLed...")
        from examples.gpio import HelloWorldRGBled
        HelloWorldRGBled.main()

    # external LED - digital IO
    if DEMO_EXTERNAL_LED is True:
        print("External LED...")
        from machine import Pin
        from examples.gpio import external_gpio
        led = external_gpio.Led(pin=Pin.exp_board.G28)
        led.demo(5)

    # external button - digital IO - polling button
    if DEMO_BUTTON is True:
        print("button pressed...")
        from machine import Pin
        from examples.gpio import external_gpio
        button = external_gpio.Button(pin=Pin.exp_board.G22)
        button.demo(5)

    # button + LED - digital IO
    if DEMO_BUTTON_LED is True:
        print("Button lits LED...")
        from machine import Pin
        from examples.gpio import external_gpio
        led = external_gpio.Led(pin=Pin.exp_board.G28)
        buttonled = external_gpio.ButtonLed(led=led, pin=Pin.exp_board.G22)
        buttonled.demo(5)

    # ADC input - potentiometer
    if DEMO_ADC is True:
        print("Potentiometer: ADC...")
        from machine import Pin
        from examples.gpio import external_gpio
        adc = external_gpio.AnalogDigital(Pin.exp_board.G5)
        adc.demo()
        pass

    # ADC input - Led output
    if DEMO_LED_DIMMER is True:
        print("LED dimmer...")
        from machine import Pin
        from examples.gpio import external_gpio
        led = external_gpio.Led(pin=Pin.exp_board.G28)
        adc = external_gpio.ADCLed(led=led, pin=Pin.exp_board.G5)
        pass

    # Neopixels demo
    if DEMO_NEOPIXELS is True:
        print("Neopixels - light show...")
        from examples.display import neopixelsApp
        app = neopixelsApp.App()
        app.run(delay=5)

    # distance sensor HSR04
    if DEMO_HSR04 is True:
        print("HSR04 sensor: distance measurement...")
        from examples.proximitysensors import hsr04App
        app = hsr04App.App()
        app.run()

    # PIR sensor: object detection (IR)
    if DEMO_PIR is True:
        print("PIR sensor: object detection (IR)...")
        from examples.proximitysensors import pirApp
        app = pirApp.App()
        app.run()

    # more advanced demos or
    # exercise solution samples
    if DEMO_PULSING_LED is True:
        from examples.gpio import pulsing_led
        pulsing_led.main()

    if DEMO_BINAIRE_COUNTER is True:
        from examples.gpio import binaire_counter
        binaire_counter.main(maximum=256, dt=0.1)

    # PROJECTS
    if PROJECT_HSR04_NEOPIXELS is True:
        from examples.projects import colorNeopixelsApp
        app = colorNeopixelsApp.App()
        app.run()
        # # distance controls color of neopixels
        # from machine import Pin
        # from hsr04 import HSR04
        # echoPin = Pin.exp_board.G7
        # triggerPin = Pin.exp_board.G8
        # app = coloredNeopixelsApp.App(Din, echoPin, triggerPin)
        # app.run()

    # LoRaWan connection
    if DEMO_LORAWAN_TTN is True:
        from examples.lorawan import lorawan_scanner
        lorawan_scanner.main(delay=2)

    # cleanup
    import gc
    gc.collect()
    print('main(): free memory {} Kb'.format(gc.mem_free() // 1024))
    print('main done')
