"""
LoPy4 pinouts and colors for RGB-led

2002-0516 PP default SPI baudrate increased to 2MHz
2020-0427 PP added SPI
2020-03xx PP add color definitions
2020-0228 PP redefined known pins with Pin.exp_board


>>> from machine import Pin
>>> help(Pin.exp_board)
  G2 -- Pin('P0', mode=Pin.IN, pull=Pin.PULL_UP, alt=14)
  G1 -- Pin('P1', mode=Pin.OUT, pull=Pin.PULL_UP, alt=14)
  G23 -- Pin('P2', mode=Pin.OUT, pull=None, alt=-1)
  G24 -- Pin('P3', mode=Pin.IN, pull=Pin.PULL_DOWN, alt=-1)
  G11 -- Pin('P4', mode=Pin.IN, pull=Pin.PULL_DOWN, alt=-1)
  G12 -- Pin('P5', mode=Pin.OUT, pull=None, alt=63)
  G13 -- Pin('P6', mode=Pin.OUT, pull=None, alt=65)
  G14 -- Pin('P7', mode=Pin.IN, pull=None, alt=64)
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

Usage:

from machine import Pin
ledPin = Pin.exp_board.G7
# etc. Pin.exp_board.Gxx levert Pin op horende bij Gxx
P-numbers: LoPy4 pinsnumbering
G-numbers: Expansion board 3.0 pin labelling
Note: 2020-03: exp.board labelling are also P-numbers

"""
from micropython import const
from machine import Pin

# RGB Led
RGB_LED = Pin.exp_board.G23
# PP: some color specifications for RGB-led of LoPy4
RED = 0xff0000
BLUE = 0x0000ff
GREEN = 0x00ff00
BLACK = 0x000000

# I2C
I2C_SCL = Pin.exp_board.G15  # 'P8'
I2C_SDA = Pin.exp_board.G16  # 'P9'

# SPI
SPI_SCL = Pin.exp_board.G17   # 'P10'
SPI_MOSI = Pin.exp_board.G22  # 'P11'
SPI_MISO = Pin.exp_board.G4   # 'P14'
SPI_DEFAULT_BAUDRATE = const(2000000)

# SD disk
SD_CLK = Pin.exp_board.G10
SD_DAT = Pin.exp_board.G15
SD_CMD = Pin.exp_board.G11

# UART
UART_RX = Pin.exp_board.G2
UART_TX = Pin.exp_board.G1

# USR_BUTTON = G4
USR_BUTTON = Pin.exp_board.G4
