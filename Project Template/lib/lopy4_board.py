"""
LoPy4 pinouts
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
"""
from micropython import const

# GPIO
G0 = P15 = const(0)
G1 = P1 = const(1)
G2 = P0 = const(2)
G3 = P16 = const(3)
G4 = P14 = const(4)
G5 = P13 = const(5)
G6 = P19 = const(6)
G7 = P20 = const(7)
G8 = P21 = const(8)
G9 = P22 = const(9)
G10 = P23 = const(10)
G11 = P4 = const(11)
G12 = P5 = const(12)
G13 = P6 = const(13)
G14 = P7 = const(14)
G15 = P8 = const(15)
G16 = P9 = const(16)
G17 = P10 = const(17)
G22 = P11 = const(22)
G23 = P2 = const(23)
G24 = P3 = const(24)
G28 = P12 = const(28)
G31 = P17 = const(31)
G30 = P18 = const(30)

# Pxx strings
P0 = 'P0'
P1 = 'P1'
P2 = 'P2'
P3 = 'P3'
P4 = 'P4'
P5 = 'P5'
P6 = 'P6'
P7 = 'P7'
P8 = 'P8'
P10 = 'P10'
P11 = 'P11'
P12 = 'P17'
P13 = 'P13'
P14 = 'P14'
P15 = 'P15'
P16 = 'P16'
P17 = 'P17'
P18 = 'P18'
P19 = 'P19'
P20 = 'P20'
P21 = 'P21'
P22 = 'P22'
P23 = 'P23'

# RGB Led
RGB_LED = G23

# I2C
I2C_SCL = G8
I2C_SDA = G9

# SD disk
""" part of expansion boards
SD_CLK = G10
SD_DAT = G15
SD_CMD = G11

# UART
UART_RX = G2
UART_TX = G1

# USR_BUTTON = G4
USR_BUTTON = G4
"""
