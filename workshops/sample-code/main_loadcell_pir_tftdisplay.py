"""
Demo program demonstrating
1. the capabities of the MicroPython display module
2. Loadcell HX711
3. PIR-sensor (3V3 / G7)
TODO: OOP versions of the code

Micropython v1.1.2 - 22 april 2020

2020-0516 PP added SPIBUS, added TFT-display to show values HX711
2020-0515 PP setup loadcell HX711
2020-0426 PP 2nd test: TFT ST7735S + Lolin D32-Pro + mp v1.12 (22 april)

Sources:
[robert-hh] https://github.com/robert-hh/hx711-lopy
[hackaday.io] https://hackaday.io/project/1741-honeybee-hive-monitoring/log/9780-modifying-the-hx711-breakout-board-for-33v-operation

[boochow] https://github.com/boochow/MicroPython-ST7735
[cavers]  https://github.com/GuyCarver/MicroPython/tree/master/lib
          https://github.com/GuyCarver/MicroPython
[wemos.cc] https://docs.wemos.cc/en/latest/d32/d32_pro.html

To create correct BMP images, use ImageMagick (Terminal):
$ magick tiger.bmp -resize 128x160
         -background Black -gravity center
         -extent 128x160
         tiger128x160.bmp
result: a centered and resized image on a black canvas of 128x160 pixels.
"""
import time
import os
from spibus import SPIBUS
import lopy4board as board

# TFT-display - LoPy4 connections
from ST7735 import TFT, TFTColor
from examples.displays.config_tft import TFT_SPEED

USE_GRAPHICS_TEST = False
USE_SLIDESHOW = False
USE_LOADCELL_HXK711 = False  # True
USE_PIR_SENSOR = True

# create SPI-object
spibus = SPIBUS(baudrate=TFT_SPEED)  # default SPI-pins
spi = spibus.spi
# DEBUG: spibus.debug_printSPI()

print("Demo TFT-display ST7735...", USE_SLIDESHOW or USE_GRAPHICS_TEST)
if USE_GRAPHICS_TEST is True:
    print("Demo TFT-display ST7735...GRAPHICS_TEST")
    # from examples.displays.graphicstest import test_main
    from examples.displays.testdisplaytft import TestDisplayTFT

    assert(spi is not None)  # check pre-condition
    display = TestDisplayTFT(spi)  # use my default TFT-lopy4 connections

    # helper function
    def tft_simpletest(display):
        orient_text = ["PORTRAIT", "LANDSCAPE",
                       "PORTRAIT_FLIP", "LANDSCAPE_FLIP"]
        # do the graphics test in all orientations
        for orient in range(0, 4):
            display._tft.rotation(orient)
            print("Orientation: {}".format(orient_text[orient]))
            display.test_main()
            time.sleep(1)

    # do the graphic tests...
    tft_simpletest(display)
    display.blank()

if USE_SLIDESHOW is True:
    print("Demo TFT-display ST7735...SLIDESHOW")
    from examples.displays.displaytft import DisplayTFT as Display

    assert(spi is not None)  # check pre-condition
    display = Display(spi)  # use my default TFT-lopy4 connections
    # display.displayOn()
    display.printPins()  # print used default Pins for display

    # function to show all images in path
    def slideshow(display, path="images/",
                  orient=0, wait=5, clearDisplay=False):
        # generate list of images...
        # 2020-0427 PP: LoPy4 - path should not end with '/',
        # else os.listdir(path) will give
        #        OSError: [Errno 22] EINVAL
        # not seen on ESP32.
        pathname = path.split("/")
        # files = os.listdir(path[:-1])  # remove '/'
        files = os.listdir(pathname[0])
        # DEBUG: print("#files: {}".format(len(files)))
        for file in files:
            if clearDisplay is True:
                display.blank()
            filename = path + file
            display.displayBMP(filename, orient)
            time.sleep(wait)

    try:
        while True:
            slideshow(display, path="images/",
                      orient=2, wait=5, clearDisplay=False)
            # optional: time.sleep(10)
    except OSError as ex:
        print("OSError: {}".format(ex))
    except KeyboardInterrupt:
        print("Slideshow done")


print("Demo weight sensor HX711...", USE_LOADCELL_HXK711)
if USE_LOADCELL_HXK711 is True:
    from examples.displays.displaytft import DisplayTFT as Display
    from examples.loadcell.hx711DemoApp import test_weight, test_scale

    assert(spi is not None)  # check pre-condition
    display = Display(spi)  # use my default TFT-lopy4 connections
    # display.displayOn()
    display.blank()
    # DEBUG: display.printPins()  # print used default Pins for display

    try:
        # test_weight(wait=1)  # print on console
        test_weight(display, times=5, wait=5)  # print on TFT-display
        # test_scale()  # wat doet dit?
        # import test_hx711_spi  # wat doet dit?
    except KeyboardInterrupt:
        print("User interrupt!")
        display.blank()
        display.text("Done!", x=5, y=30, color=TFT.RED, size=3)

print("Demo PIR sensor ...", USE_PIR_SENSOR)
if USE_PIR_SENSOR is True:
    from examples.displays.displaytft import DisplayTFT as Display
    from examples.proximitysensors.test_pir_pycom import run

    assert(spi is not None)  # check pre-condition
    display = Display(spi)  # use my default TFT-lopy4 connections
    display.blank()
    # DEBUG: display.printPins()  # print used default Pins for display
    try:
        run(display)

    except KeyboardInterrupt:
        print("User interrupt!")
        display.blank()
        display.text("Done!", x=5, y=30, color=TFT.GREEN, size=3)
