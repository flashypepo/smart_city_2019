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
# uncomment als je TFT-display aangesloten hebt...
# from spibus import SPIBUS

# TFT-display - LoPy4 connections
# uncomment als je TFT-display aangesloten hebt...
# from ST7735 import TFT, TFTColor
# from examples.displays.config_tft import TFT_SPEED

USE_PIR_SENSOR = True

# uncomment als je TFT-display aangesloten hebt...
# create SPI-object
# spibus = SPIBUS(baudrate=TFT_SPEED)  # default SPI-pins
# spi = spibus.spi
# DEBUG: spibus.debug_printSPI()

print("Demo PIR sensor ...", USE_PIR_SENSOR)
if USE_PIR_SENSOR is True:
    # uncomment als je TFT-display aangesloten hebt...
    # from examples.displays.displaytft import DisplayTFT as Display
    from examples.proximitysensors.test_pir_pycom import run

    try:
        # uncomment als je TFT-display aangesloten hebt...
        # assert(spi is not None)  # check pre-condition
        # display = Display(spi)  # use my default TFT-lopy4 connections
        # display.blank()
        # # DEBUG: display.printPins()  # print used default Pins for display
        # run(display)
        run()  # display is console

    except KeyboardInterrupt:
        print("User interrupt!")
        # uncomment als je TFT-display aangesloten hebt...
        # display.blank()
        # display.text("Done!", x=5, y=30, color=TFT.GREEN, size=3)
