"""
Demo program demonstrating
1. the capabities of the MicroPython display module
2. Loadcell HX711

TODO: OOP versions of the code

Micropython v1.1.2 - 22 april 2020

2020-0516 PP added SPIBUS, added TFT-display to show values HX711
2020-0515 PP setup loadcell HX711

Sources:
[robert-hh] https://github.com/robert-hh/hx711-lopy
[hackaday.io] https://hackaday.io/project/1741-honeybee-hive-monitoring/log/9780-modifying-the-hx711-breakout-board-for-33v-operation
"""
import time
import os
from spibus import SPIBUS

from ST7735 import TFT, TFTColor
import lopy4board as board

# TFT-display - LoPy4 connections
from examples.displays.config_tft import TFT_SPEED

USE_LOADCELL_HXK711 = True

# create SPI-object
spibus = SPIBUS(baudrate=TFT_SPEED)  # default SPI-pins
spi = spibus.spi
# DEBUG: spibus.debug_printSPI()


print("Demo weight sensor HX711...", USE_LOADCELL_HXK711)
if USE_LOADCELL_HXK711 is True:
    from examples.displays.displaytft import DisplayTFT as Display
    from examples.loadcell.hx711DemoApp import test_weight, test_scale

    assert(spi is not None)  # check pre-condition
    display = Display(spi)  # use my default TFT-lopy4 connections
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
