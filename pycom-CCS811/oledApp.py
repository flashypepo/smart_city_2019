'''
oledApp - creates an OLED display
OLED, I2C, ssd1306

History
2019-1205 PP: renamed method welcome() to showText()

'''
from ssd1306 import SSD1306_I2C


# OLED
class OLEDApp():
    def __init__(self, i2c, width, height):
        self._i2c = i2c
        self._width = width
        self._height = height
        self._oled = SSD1306_I2C(width, height, i2c)
        # optional: I'd to flip and mirror my oled display
        # oled.flip(180)   # flip display 180
        # oled.mirror(90)  # mirror display 90 degree
        # oled.show()    # update display
        # effectively: turn display 180 degrees counter-clockwise

    # 2019-1205 PP: renamed method to showText()
    def showText(self, msgs):
        """ welcome(msg): shows msgs on OLED.
        each element of msgs is a dictionary {'tekst':(x,y), ...}
        Example:
        msgs = {
            'Welkom':(0, 0),
            'Smart':(30, 10),
            'citizens!':(60, 20)
        }
        showText(msgs)
        """
        self._oled.fill(0)  # clear canvas
        for key, value in msgs.items():
            self._oled.text(key, value[0], value[1])  # text, x, y in pixels
        # self._oled.contrast(constrast)
        self._oled.show()

    def clearDisplay(self, refresh=True):
        """ clear(): clear display immediately (refresh=True),
            else postpone to next update."""
        self._oled.fill(0)  # clear canvas
        if refresh:
            self._oled.show()

    @property
    def oled(self):
        """ returns oled object"""
        return self._oled


if __name__ == '__main__':
    app = OLEDApp(i2c=i2c, width=128, height=32)
    '''msg = {
        'Welkom': (0, 0),
        'Smart': (30, 10),
        'citizens!': (60, 20),
    }'''
    msg = {
        'Hello': (0, 0),
        'Peter': (30, 10),
        'TEST!': (60, 20),
    }
    app.welcome(msg)
