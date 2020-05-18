"""
loadcell application
source: https://github.com/robert-hh/hx711-lopy

TODO:
1. use other Pins
2. add TFT-display
3. calibrate !!!
2020-0516 PP use other pins, add TFT-display (h/w)
2020-0515 PP first version, hx711 in lib

"""
import time

from ST7735 import TFT, TFTColor
# TFT-display orientation parameter
from examples.displays.config_tft import orientation

# from sysfont import sysfont
# Lelijk font: from seriffont import seriffont as sysfont
from terminalfont import terminalfont as sysfont

# loadcell sensor HX711
# HX711 configuration and connection
# DATA_PIN, CLOCK_PIN, orientation
from examples.loadcell.config_hx711 import *
from hx711 import HX711

# HX711 sensor object
hx711 = HX711(DATA_PIN, CLOCK_PIN)


# helper function: display value with a header
def showOn(display, header, value, color=TFT.WHITE,
           h=5, v=20, font_scale=1, orient=0, refresh=False):
    """ showOn(display, message, h, v, refresh):
        show on display value with a header at position (h,v),
            @param display - screen on which message is drawn
            @param header - header-text to be displayed
            @param value - value to be displayed, float
            @param h = 5  - horizontal-position of header
            @param v = 20  - vertical-position of header
            @param font_scale = 1 - size factor for font
            @param orient = 0 -tio n of display (0,1,2,3)
            @param refresh  - blank screen if True
        @returns tuple (hn, vn) - position for next header and value
    """
    if refresh is True:
        display.blank()
    # fixed: display.rotation(orientation["PORTRAIT_FLIP"])
    display.rotation(orient)

    bias = 3  # bias offset betwee header and value in pixels

    # display header
    display.text(header, h, v, color=color,
                 size=font_scale, font=sysfont)

    # display value
    v += bias + font_scale * sysfont["Height"]  # distance to next text line
    message = "{:2.2f}".format(value)
    display.text(message, h, v, color=color,
                 size=font_scale, font=sysfont)

    # calculate vertical position of next textline
    v += 2 * font_scale * sysfont["Height"]  # distance to next text line
    # and returns positon of possible next text line
    return (h, v)


# test weight values
# https://github.com/tatobari/hx711py/blob/master/example.py
# def test_weight(wait=0.1):
def test_weight(display=None, times=3, wait=1):
    # print("test HX711 - weight...")
    # my trial: w0 = 97440
    hx711.tare()
    print("Tare done!. Add weight now...")

    while True:
        # value = hx711.read()
        # my raw calibration: value = (value - w0) // 1000  # calibration
        # print("raw values: read():\t{:2.1f}".format(value), end=", ")
        # average_value = hx711.read_average(times=3) / 10000  # gram
        average_value = hx711.read_average(times=times)
        print("gemiddeld gewicht ({0}):\t{1:2.2f}".format(times, average_value),
              end=", ")
        value = hx711.get_value()
        print("get_value(): {}".format(value))
        if display is not None:
            # show weight
            h = 5
            v = 20
            orient = orientation["PORTRAIT_FLIP"]
            h, v = showOn(display, "Gewicht:", average_value,
                          color=TFT.YELLOW, h=h, v=v, font_scale=2,
                          orient=orient, refresh=True)
            # show get_value -- reference unit????
            h, v = showOn(display, "Value:", value,
                          color=TFT.GREEN, h=h, v=v, font_scale=2,
                          orient=orient, refresh=False)
        # print("---")
        # hx711.power_down()
        # hx711.power_up()
        time.sleep(wait)


# test scale
def test_scale(scale_value=48.36, units_value=5):
    print("test HX711 - scale...{}".format(scale_value))
    hx711.set_scale(scale_value)
    hx711.tare()
    val = hx711.get_units(units_value)
    print("value get_units: ", val)


if __name__ == '__main__':
    # '''
    test_weight(wait=1)
    '''
    test_scale()
    # '''
