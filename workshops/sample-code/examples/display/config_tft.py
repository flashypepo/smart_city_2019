"""
TFT-display configuration parameters
2020-0516 PP new, for connections with LoPy4
"""
from machine import Pin

TFT_DC = Pin('P22')  # exp_board.G9
TFT_RST = Pin('P23')  # exp_board.G10
TFT_CS = Pin('P12')  # exp_board.G28
TFT_BLK = Pin('P21')  # exp_board.G8

# SPI baudrate, fast and it works!
TFT_SPEED = 4000000

# vlaues for TFT-display rotation
orientation = {
    "PORTRAIT": 0,
    "LANDSCAPE": 1,
    "PORTRAIT_FLIP": 2,
    "LANDSCAPE_FLIP": 3,
}
