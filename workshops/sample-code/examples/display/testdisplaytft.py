"""
class TestDisplayTFT based upon TFT-display

Adafruit: To make new bitmaps, make sure they are less
than 240 by 320 pixels and save them in 24-bit BMP format!

2020-0516 PPP based upon class DisplayTFT
"""
import time
import math
from machine import SPI, Pin

# baseclass DisplayTFT
from examples.displays.displaytft import DisplayTFT

# LoPy4 board specifications
import lopy4board as board
# TFT ST7735 type of TFT-display
from ST7735 import TFT
# from ST7735 import TFTColor
# from sysfont import sysfont
# Lelijk font: from seriffont import seriffont as sysfont
from terminalfont import terminalfont as sysfont

# TFT-display configuration
# TFT_DC, TFT_RST, TFT_CS, TFT_BLK, TFT_SPEED
from examples.displays.config_tft import *

USE_DEBUG = False


class TestDisplayTFT(DisplayTFT):
    def __init__(self, spi,
                 dc_pin=TFT_DC, rst_pin=TFT_RST,
                 cs_pin=TFT_CS, blk_pin=TFT_BLK):
        super().__init__(spi, dc_pin, rst_pin, cs_pin, blk_pin)
        # DEBUG: print("self._tft: ", type(self._tft))

    def init(self, verbose=False):
        # Note: is called from superclass in super() !!
        # DEBUG: print("TestDisplayTFT::init() entered...")
        super().init()  # call superclass init()
        self.blank()
        if verbose is True:
            self.printPins()

    """
    Test methods for lines, and some graphics...
    main test entry: test_main()
    """
    def testlines(self, color):
        tft = self._tft

        tft.fill(TFT.BLACK)
        for x in range(0, tft.size()[0], 6):
            tft.line((0, 0), (x, tft.size()[1] - 1), color)
        for y in range(0, tft.size()[1], 6):
            tft.line((0, 0), (tft.size()[0] - 1, y), color)

        tft.fill(TFT.BLACK)
        for x in range(0, tft.size()[0], 6):
            tft.line((tft.size()[0] - 1, 0), (x, tft.size()[1] - 1), color)
        for y in range(0, tft.size()[1], 6):
            tft.line((tft.size()[0] - 1, 0), (0, y), color)

        tft.fill(TFT.BLACK)
        for x in range(0, tft.size()[0], 6):
            tft.line((0, tft.size()[1] - 1), (x, 0), color)
        for y in range(0, tft.size()[1], 6):
            tft.line((0, tft.size()[1] - 1), (tft.size()[0] - 1,y), color)

        tft.fill(TFT.BLACK)
        for x in range(0, tft.size()[0], 6):
            tft.line((tft.size()[0] - 1, tft.size()[1] - 1), (x, 0), color)
        for y in range(0, tft.size()[1], 6):
            tft.line((tft.size()[0] - 1, tft.size()[1] - 1), (0, y), color)

    def testfastlines(self, color1, color2):
        tft = self._tft
        tft.fill(TFT.BLACK)
        for y in range(0, tft.size()[1], 5):
            tft.hline((0,y), tft.size()[0], color1)
        for x in range(0, tft.size()[0], 5):
            tft.vline((x,0), tft.size()[1], color2)

    def testdrawrects(self, color):
        tft = self._tft
        tft.fill(TFT.BLACK);
        for x in range(0,tft.size()[0],6):
            tft.rect((tft.size()[0]//2 - x//2, tft.size()[1]//2 - x/2), (x, x), color)

    def testfillrects(self, color1, color2):
        tft = self._tft
        tft.fill(TFT.BLACK);
        for x in range(tft.size()[0],0,-6):
            tft.fillrect((tft.size()[0]//2 - x//2, tft.size()[1]//2 - x/2), (x, x), color1)
            tft.rect((tft.size()[0]//2 - x//2, tft.size()[1]//2 - x/2), (x, x), color2)

    def testfillcircles(self, radius, color):
        tft = self._tft
        for x in range(radius, tft.size()[0], radius * 2):
            for y in range(radius, tft.size()[1], radius * 2):
                tft.fillcircle((x, y), radius, color)

    def testdrawcircles(self, radius, color):
        tft = self._tft
        for x in range(0, tft.size()[0] + radius, radius * 2):
            for y in range(0, tft.size()[1] + radius, radius * 2):
                tft.circle((x, y), radius, color)

    def testtriangles(self):
        tft = self._tft
        tft.fill(TFT.BLACK)
        color = 0xF800
        w = tft.size()[0] // 2
        x = tft.size()[1] - 1
        y = 0
        z = tft.size()[0]
        for t in range(0, 15):
            tft.line((w, y), (y, x), color)
            tft.line((y, x), (z, x), color)
            tft.line((z, x), (w, y), color)
            x -= 4
            y += 4
            z -= 4
            color += 100

    def testroundrects(self):
        tft = self._tft
        tft.fill(TFT.BLACK)
        color = 100
        for t in range(5):
            x = 0
            y = 0
            w = tft.size()[0] - 2
            h = tft.size()[1] - 2
            for i in range(17):
                tft.rect((x, y), (w, h), color)
                x += 2
                y += 3
                w -= 4
                h -= 6
                color += 1100
            color += 100

    # 2020-0426 PP add parameter font
    def tftprinttest(self, font=sysfont):
        tft = self._tft
        tft.fill(TFT.BLACK)
        v = 30
        tft.text((0, v), "Hello World!", TFT.RED, font, 1, nowrap=True)
        v += font["Height"]
        tft.text((0, v), "Hello World!", TFT.YELLOW, font, 2, nowrap=True)
        v += font["Height"] * 2
        tft.text((0, v), "Hello World!", TFT.GREEN, font, 3, nowrap=True)
        v += font["Height"] * 3
        tft.text((0, v), str(1234.567), TFT.BLUE, font, 4, nowrap=True)
        time.sleep_ms(1500)
        tft.fill(TFT.BLACK)
        v = 0
        tft.text((0, v), "Hello World!", TFT.RED, font)
        v += font["Height"]
        tft.text((0, v), str(math.pi), TFT.GREEN, font)
        v += font["Height"]
        tft.text((0, v), " Want pi?", TFT.GREEN, font)
        v += font["Height"] * 2
        tft.text((0, v), hex(8675309), TFT.GREEN, font)
        v += font["Height"]
        tft.text((0, v), " Print HEX!", TFT.GREEN, font)
        v += font["Height"] * 2
        tft.text((0, v), "Sketch has been", TFT.WHITE, font)
        v += font["Height"]
        tft.text((0, v), "running for: ", TFT.WHITE, font)
        v += font["Height"]
        tft.text((0, v), str(time.ticks_ms() / 1000), TFT.PURPLE, font)
        v += font["Height"]
        tft.text((0, v), " seconds.", TFT.WHITE, font)

    def test_main(self, font=sysfont):
        tft = self._tft
        tft.fill(TFT.BLACK)
        tft.text((0, 0), "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur adipiscing ante sed nibh tincidunt feugiat. Maecenas enim massa, fringilla sed malesuada et, malesuada sit amet turpis. Sed porttitor neque ut ante pretium vitae malesuada nunc bibendum. Nullam aliquet ultrices massa eu hendrerit. Ut sed nisi lorem. In vestibulum purus a tortor imperdiet posuere. ", TFT.WHITE, font, 1)
        time.sleep_ms(1000)

        self.tftprinttest(font)
        time.sleep_ms(4000)

        self.testlines(TFT.YELLOW)
        time.sleep_ms(500)

        self.testfastlines(TFT.RED, TFT.BLUE)
        time.sleep_ms(500)

        self.testdrawrects(TFT.GREEN)
        time.sleep_ms(500)

        self.testfillrects(TFT.YELLOW, TFT.PURPLE)
        time.sleep_ms(500)

        tft.fill(TFT.BLACK)
        self.testfillcircles(10, TFT.BLUE)
        self.testdrawcircles(10, TFT.WHITE)
        time.sleep_ms(500)

        self.testroundrects()
        time.sleep_ms(500)

        self.testtriangles()
        time.sleep_ms(500)


if __name__ == '__main__':
    from machine import SPI
    # from machine import Pin
    # LoPy4 board specifications
    import lopy4board as board
    try:
        # create SPI-object
        TFT_SPEED = 4000000  # baudrate for SPI
        spi = SPI(0, mode=SPI.MASTER, baudrate=TFT_SPEED)  # defaults
        # __init__( self, spi, aDC, aReset, aCS)

        # TFT_DC = Pin('P22')  # Pin.exp_board.G9
        # TFT_RST = Pin('P23')  # Pin.exp_board.G10
        # TFT_CS = Pin('P12')  # Pin.exp_board.G28
        # TFT_BLK = Pin('P21')  # Pin.exp_board.G8
        # different Pins: display = DisplayTFT(spi, TFT_DC, TFT_RST, TFT_CS, TFT_BLK)
        display = TestDisplayTFT(spi)  # use my default lopy4-pins
        # display.displayOn()
        display.test_main()

    except OSError:
        print("File problem.")

    except KeyboardInterrupt:
        print("User interrupt.")
    # finally:
    #     spi.deinit()
    #     print("Done.")
