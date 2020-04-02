"""
LCD 1602 character display demonstration

2020-0330 PP added show_time, used in a thread
2020-0329 PP new
"""
__version__ = "0.0.02"

from esp8266_i2c_lcd import I2cLcd
import time
from time_helpers import timerecord
import _thread

# The PCF8574 has a jumper selectable address: 0x20 - 0x27
DEFAULT_I2C_ADDR = 0x27  # 2020-0329 PP: decimal=39, check with i2c.scan()


class LCDDemo():
    def __init__(self, i2c, i2c_addr=DEFAULT_I2C_ADDR, lines=2, columns=16):
        self._i2c = i2c
        # __init__(self, i2c, i2c_addr, num_lines, num_columns):
        self._lcd = I2cLcd(i2c, i2c_addr, lines, columns)
        self.init("It Works!\nSecond Line")

    def init(self, msg):
        self._lcd.blink_cursor_on()
        self._lcd.clear()
        self._lcd.putstr(msg)
        time.sleep(3)
        self._lcd.clear()

    def setbatteryicons(self):
        # custom characters: battery icons - 5 wide, 8 tall
        self._lcd.custom_char(0, bytearray([0x0E,0x1B,0x11,0x11,0x11,0x11,0x11,0x1F]))  # 0% Empty
        self._lcd.custom_char(1, bytearray([0x0E,0x1B,0x11,0x11,0x11,0x11,0x1F,0x1F]))  # 16%
        self._lcd.custom_char(2, bytearray([0x0E,0x1B,0x11,0x11,0x11,0x1F,0x1F,0x1F]))  # 33%
        self._lcd.custom_char(3, bytearray([0x0E,0x1B,0x11,0x11,0x1F,0x1F,0x1F,0x1F]))  # 50%
        self._lcd.custom_char(4, bytearray([0x0E,0x1B,0x11,0x1F,0x1F,0x1F,0x1F,0x1F]))  # 66%
        self._lcd.custom_char(5, bytearray([0x0E,0x1B,0x1F,0x1F,0x1F,0x1F,0x1F,0x1F]))  # 83%
        self._lcd.custom_char(6, bytearray([0x0E,0x1F,0x1F,0x1F,0x1F,0x1F,0x1F,0x1F]))  # 100% Full
        self._lcd.custom_char(7, bytearray([0x0E,0x1F,0x1B,0x1B,0x1B,0x1F,0x1B,0x1F]))  # ! Error

    def run(self):
        """Test function for verifying basic functionality."""
        print("LCDDemo run... i2c.scan:{}".format(self._i2c.scan()))

        try:
            self.setbatteryicons()
            for i in range(8):
                self._lcd.putchar(chr(i))
            time.sleep(3)
            self._lcd.clear()
            self._lcd.blink_cursor_off()
            count = 0
            while True:
                self._lcd.move_to(0, 0)
                # commented: strftime is not implemented in micropython
                #   lcd.putstr(time.strftime('%b %d %Y\n%H:%M:%S', time.localtime()))
                # self._lcd.putstr(time.strftime('%b %d %Y\n%H:%M:%S', time.localtime()))
                now = timerecord()  # 2020-0329 PP added
                self._lcd.putstr("{0}\n{1}".format(now[:10], now[11:]))
                time.sleep(1)
                count += 1
                if count % 10 == 3:
                    print("Turning backlight off")
                    self._lcd.backlight_off()
                if count % 10 == 4:
                    print("Turning backlight on")
                    self._lcd.backlight_on()
                if count % 10 == 5:
                    print("Turning display off")
                    self._lcd.display_off()
                if count % 10 == 6:
                    print("Turning display on")
                    self._lcd.display_on()
                if count % 10 == 7:
                    print("Turning display & backlight off")
                    self._lcd.backlight_off()
                    self._lcd.display_off()
                if count % 10 == 8:
                    print("Turning display & backlight on")
                    self._lcd.backlight_on()
                    self._lcd.display_on()
                if count % 10 == 9:    # 2020-0329 PP added
                    print("Show battery icons")
                    for i in range(8):
                        self._lcd.putchar(chr(i))
                    time.sleep(3)
                    self._lcd.clear()
        except KeyboardInterrupt:
            print("LCD demo exit...")
            pass

    def show_time(self):
        """show_time() - shows date and time on LCD.
           Intendend to be used in a _thread"""
        try:
            self._lcd.clear()
            self._lcd.blink_cursor_off()
            while True:
                self._lcd.move_to(0, 0)
                now = timerecord()  # 2020-0329 PP added
                self._lcd.putstr("{0}\n{1}".format(now[:10], now[11:]))
                time.sleep(1)
        except KeyboardInterrupt:
            print("time and date done!")
            _thread.exit()
            pass


if __name__ == '__main__':
    from machine import I2C
    import lopy4board as board

    print('LCDDemo... main()')
    i2c = I2C(0, I2C.MASTER, pins=(board.I2C_SDA, board.I2C_SCL))
    app = LCDDemo(i2c)
    ''' demo or date/time
    app.run()
    '''
    app.show_time()
    # '''
