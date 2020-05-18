"""
spibus.py - creates SPI bus object to be used globally

SPI documentation Pycom:
https://docs.pycom.io/firmwareapi/pycom/machine/spi/

Usage:
see __main__ code

Default SPI:
* baudrate=1000000, bits=8, polarity=0, phase=0, firstbit=SPI.MSB
* default SPI-pins - see lopy4board.py:
    * SPI_SCL = Pin.exp_board.G17   # 'P10'
    * SPI_MOSI = Pin.exp_board.G22  # 'P11'
    * SPI_MISO = Pin.exp_board.G4   # 'P14'

2020-0427 PP new
"""
from machine import Pin, SPI
import lopy4board as board

SPI_CLK = board.SPI_SCL  # G17/'P10'
SPI_MOSI = board.SPI_MOSI  # G22/'P11'
SPI_MISO = board.SPI_MISO  # G4/'P14'
SPI_BAUDRATE = board.SPI_DEFAULT_BAUDRATE


class SPIBUS(object):
    # def __init__(self, clk='P10', mosi='P11', miso='P14',
    def __init__(self, clk=SPI_CLK, mosi=SPI_MOSI, miso=SPI_MISO,
                 baudrate=SPI_BAUDRATE):
        # default: configure the SPI master @ 2MHz
        # this uses the SPI default pins for CLK, MOSI and MISO
        # (``P10``, ``P11`` and ``P14``)
        self._spi = SPI(0, mode=SPI.MASTER, baudrate=baudrate)
        self._pins = None  # default SPI pins
        # 2020-0417 PP do not specify non-default pins here,
        #              but use self.init() for non-default pins
        # 2020-0427 PP: non-default pins: not tested

    def init(self, mode=SPI.MASTER,
             baudrate=SPI_BAUDRATE,
             polarity=0, phase=0, bits=8, firstbit=SPI.MSB,
             pins=None):
        """init(arg): initialise the SPI bus with the given parameters:
            - mode must be SPI.MASTER.
            - baudrate is the SCK clock rate.
            - polarity can be 0 or 1, and is the level the idle clock line
              sits at.
            - phase can be 0 or 1 to sample data on the first or second clock
              edge respectively.
            - bits is the width of each transfer,
              accepted values are 8, 16 and 32.
            - firstbit can be SPI.MSB or SPI.LSB.
            - pins is an optional tuple with the pins to assign
              to the SPI bus.
              If the pins argument is not given the default pins
              will be selected (P10 as CLK, P11 as MOSI and P14 as MISO).
              If pins is passed as None then no pin assignment will be made.
        """
        if pins is None:  # default SPI pins
            self._pins = None
            self._spi.init(mode,
                           baudrate=baudrate,
                           polarity=polarity,
                           phase=phase,
                           bits=bits,
                           firstbit=firstbit
                           )
        else:
            self._pins = pins  # save pins
            self._spi.init(mode,
                           baudrate=baudrate,
                           polarity=polarity,
                           phase=phase,
                           bits=bits,
                           firstbit=firstbit,
                           pins=pins
                           )

    def close(self):
        """close(): close the SPI bus.
            post-condition: spi=None"""
        self._spi.deinit()
        self._spi = None

    @property
    def baudrate(self):
        """ baudrate() returns baudrate of SPI"""
        return SPI_BAUDRATE

    @property
    def spi(self):
        """ spi() returns SPI object."""
        return self._spi

    @property
    def pins(self):
        """ pins() returns SPI pins in a tuple (clk, mosi, miso)"""
        # DEPRECATED: return ("P10", "P11", "P14")
        if self._pins is None:
            return (SPI_CLK, SPI_MOSI, SPI_MISO)
        else:
            return self._pins

    def debug_printSPI(self):
        print("SPI information...")
        print("spi={}".format(self._spi))  # including baudrate
        clk, mosi, miso = self.pins
        print("CLK={0}\nMOSI={1}\nMISO={2}".format(clk, mosi, miso))
        print("---")


if __name__ == '__main__':
    from spibus import SPIBUS
    spibus = SPIBUS()  # default SPI-pins
    print(spibus)
    spi = spibus.spi
    print("spi={}".format(spi))
    clk, mosi, miso = spibus.pins
    print("CLK={0}\nMOSI={1}\nMISO={2}".format(clk, mosi, miso))
