'''
oledApp - creates an OLED display
OLED, I2C, ssd1306

History
2020-03 PP: Smart City semester 2
2019-12 PP: renamed method welcome() to showText()

'''
from time import sleep
from ssd1306 import SSD1306_I2C

# device configuration
DISPLAY_WIDTH = const(128)
DISPLAY_HEIGHT = const(64)


# OLED application
class OLEDApp():
    def __init__(self, i2c, width=DISPLAY_WIDTH, height=DISPLAY_HEIGHT):
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
        """ showText(msg): shows msgs on OLED.
        msg is a dictionary, each element of msgs a messageline
        {'tekst':(x,y), ...}
        Example:
        msgs = {
            'Welkom':(0, 0),
            'Smart':(30, 10),
            'citizens!':(60, 20)
        }
        """
        self._oled.fill(0)  # clear canvas
        for key, value in msgs.items():
            self._oled.text(key, value[0], value[1])  # text, x, y in pixels
        # self._oled.contrast(constrast)
        self._oled.show()

    def clearScreen(self, refresh=True):
        """ clearScreen(): clear display immediately (refresh=True),
            else postpone to next update."""
        self._oled.fill(0)  # clear canvas
        if refresh:
            self._oled.show()

    def whiteScreen(self, refresh=True):
        self._oled.fill(1)
        if refresh:
            self._oled.show()

    def flipScreen(self, angle=180, refresh=True):
        ''' flipScreen() - flip the screen over angle vertical & horizontal
            angle=180: mirror and flip topside
            angle=0: mirror and flip again  '''
        self._oled.flip(angle)  # val=degrees
        self._oled.mirror(angle)

    @property
    def oled(self):
        """ returns oled object"""
        return self._oled

    def run(self, msg=None):
        # blank screen
        self.whiteScreen()
        sleep(3)

        # show message
        # if none is given, use default message
        if msg is None:
            msg = {
                'Welkom': (0, 0),
                'Smart': (30, 10),
                'citizens!': (60, 20),
            }
        self.showText(msg)
        sleep(3)

        # demo: flipscreen a couple of times
        print("Flip OLED screen 180 degrees...")
        self.flipScreen(angle=180, refresh=True)
        sleep(3)
        print("Reset OLED screen...")
        self.flipScreen(angle=0, refresh=True)


if __name__ == '__main__':
    print('i2c scan:', i2c.scan())

    app = OLEDApp(i2c=i2c)
    app.whiteScreen(refresh=True)

    msg = {
        'Welkom': (0, 0),
        'Smart': (30, 10),
        'citizens!': (60, 20),
    }
    app.showText(msg)
    sleep(3)
    app.flipScreen()
