"""
LoPy4 pinouts
2019-0924 Peter updated: numbering according to pins.csv on GitHub PyCom
 https://raw.githubusercontent.com/pycom/pycom-micropython-sigfox/master/esp32/boards/LOPY4/pins.csv
2019-0915 Peter updated: GPIO returns 'Pxx', add Pin.module for Pin(Pxx)
# these definitions fits better with the example code
2019-0910 Peter new

>>> from machine import Pin
>>> help(Pin.exp_board)
G2 -- Pin('P0', mode=Pin.IN, pull=Pin.PULL_UP, alt=14)
G1 -- Pin('P1', mode=Pin.OUT, pull=Pin.PULL_UP, alt=14)
G23 -- Pin('P2', mode=Pin.OUT, pull=None, alt=-1)
G24 -- Pin('P3', mode=Pin.IN, pull=Pin.PULL_DOWN, alt=-1)
G11 -- Pin('P4', mode=Pin.IN, pull=Pin.PULL_DOWN, alt=-1)
G12 -- Pin('P5', mode=Pin.IN, pull=Pin.PULL_DOWN, alt=-1)
G13 -- Pin('P6', mode=Pin.IN, pull=Pin.PULL_DOWN, alt=-1)
G14 -- Pin('P7', mode=Pin.IN, pull=Pin.PULL_DOWN, alt=-1)
G15 -- Pin('P8', mode=Pin.IN, pull=Pin.PULL_DOWN, alt=-1)
G16 -- Pin('P9', mode=Pin.IN, pull=Pin.PULL_DOWN, alt=-1)
G17 -- Pin('P10', mode=Pin.IN, pull=Pin.PULL_DOWN, alt=-1)
G22 -- Pin('P11', mode=Pin.IN, pull=Pin.PULL_DOWN, alt=-1)
G28 -- Pin('P12', mode=Pin.IN, pull=None, alt=-1)
G5 -- Pin('P13', mode=Pin.IN, pull=Pin.PULL_DOWN, alt=-1)
G4 -- Pin('P14', mode=Pin.IN, pull=Pin.PULL_DOWN, alt=-1)
G0 -- Pin('P15', mode=Pin.IN, pull=Pin.PULL_DOWN, alt=-1)
G3 -- Pin('P16', mode=Pin.IN, pull=Pin.PULL_DOWN, alt=-1)
G31 -- Pin('P17', mode=Pin.IN, pull=Pin.PULL_DOWN, alt=-1)
G30 -- Pin('P18', mode=Pin.IN, pull=Pin.PULL_DOWN, alt=-1)
G6 -- Pin('P19', mode=Pin.IN, pull=Pin.PULL_DOWN, alt=-1)
G7 -- Pin('P20', mode=Pin.IN, pull=Pin.PULL_DOWN, alt=-1)
G8 -- Pin('P21', mode=Pin.IN, pull=Pin.PULL_DOWN, alt=-1)
G9 -- Pin('P22', mode=Pin.IN, pull=Pin.PULL_DOWN, alt=-1)
G10 -- Pin('P23', mode=Pin.IN, pull=None, alt=-1)

>>> from machine import Pin
>>> P12 = Pin.module.P12
>>> P12
Pin('P12', mode=Pin.IN, pull=None, alt=-1)
"""
# from micropython import const
from machine import Pin

# GPIO -> Pxx
# 2019-0924 added GPIOxx from pins.csv,
# so you can look it up from the labels
# on the expansions boards and from lopy4 pinlayout
#   GPIO = Input/Output pin
#   GPI = only Input pin
# Note: G** vind je terug op de expansion boards (exp):
# exp = lopy4 = P
G0 = GPIO38 = 'P15'
G1 = GPIO1 = 'P1'
G2 = GPIO3 = 'P0'
G3 = GPI39 = 'P16'
G4 = GPI37 = 'P14'
G5 = GPI36 = 'P13'
G6 = GPIO32 = 'P19'
G7 = GPIO33 = 'P20'
G8 = GPIO26 = 'P21'
G9 = GPIO25 = 'P22'
G10 = GPIO14 = 'P23'
G11 = GPIO15 = 'P4'
G12 = GPIO5 = 'P5'
G13 = GPIO27 = 'P6'
G14 = GPIO19 = 'P7'
G15 = GPIO2 = 'P8'
G16 = GPIO12 = 'P9'
G17 = GPIO13 = 'P10'
G22 = GPIO22 = 'P11'
G23 = GPIO0 = 'P2'
G24 = GPIO4 = 'P3'
G28 = GPIO21 = 'P12'
G31 = GPI35 = 'P17'
G30 = GPI34 = 'P18'

# default I2C-pins
# Note: values returns Pin-object
# https://docs.pycom.io/firmwareapi/pycom/machine/i2c/
I2C_SDA = Pin.module.P9   # G16
I2C_SCL = Pin.module.P10  # G17, same as default SPI_CLK

# default SPI-pins
# Note: values returns Pin-object
# https://docs.pycom.io/firmwareapi/pycom/machine/spi/
SPI_CLK = Pin.module.P10   # G17, same as default I2C_SCL
SPI_MOSI = Pin.module.P11  # G22
SPI_MISO = Pin.module.P14  # G4

# default SD cardreader pins
# Note: values returns Pin-object
# SD card is formatted either as FAT16 or FAT32.
SD_CLK = Pin.module.P23  # G10
SD_DAT = Pin.module.P8   # G15
SD_CMD = Pin.module.P4   # G11


# default UART pins
# Note: values returns Pin-object
UART_TX = Pin.module.P3  # G24
UART_RX = Pin.module.P4  # G11

# USR_BUTTON = G4
# Note: values returns Pin-object
USR_BUTTON = Pin.module.P14
