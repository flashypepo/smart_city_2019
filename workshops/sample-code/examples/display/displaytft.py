"""
class DisplayTFT based upon TFT-display

Adafruit: To make new bitmaps, make sure they are less
than 240 by 320 pixels and save them in 24-bit BMP format!

2020-0516 PP TODO: add adafruit_gfx for drawing graphics
2020-0516 PP new/basic, based upon tftbmp.py
"""
import time
import math
from machine import SPI, Pin
# LoPy4 board specifications
import lopy4board as board
# TFT ST7735 type of TFT-display
from ST7735 import TFT, TFTColor
# from sysfont import sysfont
# Lelijk font: from seriffont import seriffont as sysfont
from terminalfont import terminalfont as sysfont

# TFT-display configuration
# TFT_DC, TFT_RST, TFT_CS, TFT_BLK, TFT_SPEED
from examples.displays.config_tft import *

USE_DEBUG = False


class DisplayTFT():

    def __init__(self, spi,
                 dc_pin=TFT_DC, rst_pin=TFT_RST,
                 cs_pin=TFT_CS, blk_pin=TFT_BLK):
        self._tft = TFT(spi, dc_pin, rst_pin, cs_pin)
        self._blkPin = blk_pin
        self._dcPin = dc_pin  # ?: necessary?
        self._rstPin = rst_pin  # ?: necessary?
        self._csPin = cs_pin  # ?: necessary?
        self.init()

    def init(self):
        # DEBUG: print("DisplayTFT::init() entered...")
        self._tft.initr()
        # alternative: self._tft.initb2()
        self._tft.rgb(True)

    # Backlight on or off
    def displayOn(self, isOnOff=True):
        self._blkPin.value(1 if isOnOff else 0)

    # erase TFT-display
    def blank(self):
        self._tft.fill(TFT.BLACK)

    def rotation(self, orient=0):
        assert (orient >= 0 and orient <= 4)
        self._tft.rotation(orient)

    def printPins(self):
        dcPin, rstPin, csPin, blkPin = self.pins
        print("DC={0}\nRST={1}\nCS={2}\nBLK={3}".format(
            dcPin, rstPin, csPin, blkPin)
        )

    @property
    def pins(self):
        return (
            self._dcPin,
            self._rstPin,
            self._csPin,
            self._blkPin,
        )

    # display BMP-image on display
    def displayBMP(self, filename, orient=0, font=sysfont):
        tft = self._tft
        if USE_DEBUG:
            print("File: {}".format(filename), end=", ")
        tft.rotation(orient)  # PP added
        with open(filename, 'rb') as f:
            if f.read(2) == b'BM':  # header
                dummy = f.read(8)  # file size(4), creator bytes(4)
                offset = int.from_bytes(f.read(4), 'little')
                hdrsize = int.from_bytes(f.read(4), 'little')
                width = int.from_bytes(f.read(4), 'little')
                height = int.from_bytes(f.read(4), 'little')
                if int.from_bytes(f.read(2), 'little') == 1:  # planes must be 1
                    depth = int.from_bytes(f.read(2), 'little')
                    if depth == 24 and int.from_bytes(f.read(4), 'little') == 0:#compress method == uncompressed
                        if USE_DEBUG:
                            print("image size:", width, "x", height)
                        rowsize = (width * 3 + 3) & ~3
                        if height < 0:
                            height = -height
                            flip = False
                        else:
                            flip = True
                        w, h = width, height
                        if w > 128: w = 128
                        if h > 160: h = 160
                        tft._setwindowloc((0,0),(w - 1,h - 1))
                        for row in range(h):
                            if flip:
                                pos = offset + (height - 1 - row) * rowsize
                            else:
                                pos = offset + row * rowsize
                            if f.tell() != pos:
                                dummy = f.seek(pos)
                            for col in range(w):
                                bgr = f.read(3)
                                tft._pushcolor(TFTColor(bgr[2],bgr[1],bgr[0]))
            fname = filename.split("/")
            tft.text((10, h-font["Height"]-3),
                     fname[1][:-4].upper(), TFT.YELLOW, font, 1,
                     nowrap=True)

    # display text on screenpostion x,y in color and font
    def text(self, message, x, y, color=TFT.YELLOW, size=1, font=sysfont):
        self._tft.text((x, y), message,
                       color, font, size,
                       nowrap=True
                       )


if __name__ == '__main__':
    from machine import SPI
    # from machine import Pin
    # LoPy4 board specifications
    import lopy4board as board
    try:
        # create SPI-object
        spi = SPI(0, mode=SPI.MASTER, baudrate=TFT_SPEED)  # defaults
        # __init__( self, spi, aDC, aReset, aCS)

        # TFT_DC = Pin('P22')  # Pin.exp_board.G9
        # TFT_RST = Pin('P23')  # Pin.exp_board.G10
        # TFT_CS = Pin('P12')  # Pin.exp_board.G28
        # TFT_BLK = Pin('P21')  # Pin.exp_board.G8
        # different Pins: display = DisplayTFT(spi, TFT_DC, TFT_RST, TFT_CS, TFT_BLK)
        display = DisplayTFT(spi)  # use my default lopy4-pins
        display.displayOn()
        print(display.pins)  # print my used default Pins for display
        # # Backlight on or off
        # display.displayOn(isOnOff=True)
        path = "images/"
        display.displayBMP(filename=path + 'woman.bmp')

    except OSError:
        print("File problem.")

    except KeyboardInterrupt:
        print("User interrupt.")
    # finally:
    #     spi.deinit()
    #     print("Done.")
