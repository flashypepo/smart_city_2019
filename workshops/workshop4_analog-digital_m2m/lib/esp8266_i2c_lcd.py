"""Implements a HD44780 character LCD connected via PCF8574 on I2C.
   This was tested with: https://www.wemos.cc/product/d1-mini.html

2019-0917 Peter tested with Lopy4 and Expansion board 3.0
          add _thread, USE_DEBUG
"""
from lcd_api import LcdApi
from machine import I2C
from time import sleep_ms, ticks_ms
import _thread
USE_DEBUG = False  # 2019-0917 added for internal test_main

# The PCF8574 has a jumper selectable address: 0x20 - 0x27
DEFAULT_I2C_ADDR = 0x27

# Defines shifts or masks for the various LCD line attached to the PCF8574

MASK_RS = 0x01
MASK_RW = 0x02
MASK_E = 0x04
SHIFT_BACKLIGHT = 3
SHIFT_DATA = 4


class I2cLcd(LcdApi):
    """Implements a HD44780 character LCD connected via PCF8574 on I2C."""

    def __init__(self, i2c, i2c_addr, num_lines, num_columns):
        self.i2c = i2c
        self.i2c_addr = i2c_addr
        self.i2c.writeto(self.i2c_addr, bytearray([0]))
        sleep_ms(20)   # Allow LCD time to powerup
        # Send reset 3 times
        self.hal_write_init_nibble(self.LCD_FUNCTION_RESET)
        sleep_ms(5)    # need to delay at least 4.1 msec
        self.hal_write_init_nibble(self.LCD_FUNCTION_RESET)
        sleep_ms(1)
        self.hal_write_init_nibble(self.LCD_FUNCTION_RESET)
        sleep_ms(1)
        # Put LCD into 4 bit mode
        self.hal_write_init_nibble(self.LCD_FUNCTION)
        sleep_ms(1)
        LcdApi.__init__(self, num_lines, num_columns)
        cmd = self.LCD_FUNCTION
        if num_lines > 1:
            cmd |= self.LCD_FUNCTION_2LINES
        self.hal_write_command(cmd)

    def hal_write_init_nibble(self, nibble):
        """Writes an initialization nibble to the LCD.

        This particular function is only used during initialization.
        """
        byte = ((nibble >> 4) & 0x0f) << SHIFT_DATA
        self.i2c.writeto(self.i2c_addr, bytearray([byte | MASK_E]))
        self.i2c.writeto(self.i2c_addr, bytearray([byte]))

    def hal_backlight_on(self):
        """Allows the hal layer to turn the backlight on."""
        self.i2c.writeto(self.i2c_addr, bytearray([1 << SHIFT_BACKLIGHT]))

    def hal_backlight_off(self):
        """Allows the hal layer to turn the backlight off."""
        self.i2c.writeto(self.i2c_addr, bytearray([0]))

    def hal_write_command(self, cmd):
        """Writes a command to the LCD.

        Data is latched on the falling edge of E.
        """
        byte = ((self.backlight << SHIFT_BACKLIGHT) | (((cmd >> 4) & 0x0f) << SHIFT_DATA))
        self.i2c.writeto(self.i2c_addr, bytearray([byte | MASK_E]))
        self.i2c.writeto(self.i2c_addr, bytearray([byte]))
        byte = ((self.backlight << SHIFT_BACKLIGHT) | ((cmd & 0x0f) << SHIFT_DATA))
        self.i2c.writeto(self.i2c_addr, bytearray([byte | MASK_E]))
        self.i2c.writeto(self.i2c_addr, bytearray([byte]))
        if cmd <= 3:
            # The home and clear commands require a worst case delay of 4.1 msec
            sleep_ms(5)

    def hal_write_data(self, data):
        """Write data to the LCD."""
        byte = (MASK_RS | (self.backlight << SHIFT_BACKLIGHT) | (((data >> 4) & 0x0f) << SHIFT_DATA))
        self.i2c.writeto(self.i2c_addr, bytearray([byte | MASK_E]))
        self.i2c.writeto(self.i2c_addr, bytearray([byte]))
        byte = (MASK_RS | (self.backlight << SHIFT_BACKLIGHT) | ((data & 0x0f) << SHIFT_DATA))
        self.i2c.writeto(self.i2c_addr, bytearray([byte | MASK_E]))
        self.i2c.writeto(self.i2c_addr, bytearray([byte]))

    def test_main(self, dt=1):
        """Test function for verifying basic functionality.
           2019-0917 dt is dummy for _thread."""
        if USE_DEBUG:
            print("Running test_main...")
        self.putstr("It Works!\nSecond Line")
        sleep_ms(3000)
        self.clear()
        count = 0
        while True:
            self.move_to(0, 0)
            self.putstr("%7d\nIt Works" % (ticks_ms() // 1000))
            sleep_ms(1000)
            count += 1
            if count % 10 == 3:
                if USE_DEBUG:
                    print("Turning backlight off")
                self.backlight_off()
            if count % 10 == 4:
                if USE_DEBUG:
                    print("Turning backlight on")
                self.backlight_on()
            if count % 10 == 5:
                if USE_DEBUG:
                    print("Turning display off")
                self.display_off()
            if count % 10 == 6:
                if USE_DEBUG:
                    print("Turning display on")
                self.display_on()
            if count % 10 == 7:
                if USE_DEBUG:
                    print("Turning display & backlight off")
                self.backlight_off()
                self.display_off()
            if count % 10 == 8:
                if USE_DEBUG:
                    print("Turning display & backlight on")
                self.backlight_on()
                self.display_on()

    # 2019-0917 startup test-main in a thread...
    def run(self, dt=0):
        _thread.start_new_thread(self.test_main, (dt, ))


if __name__ == '__main__':
    """Implements a HD44780 character LCD connected via PCF8574 on I2C.
   This was tested with: https://www.wemos.cc/product/d1-mini.html"""
    from esp8266_i2c_lcd import I2cLcd
    # from lopy4_board import I2C_SCL, I2C_SDA
    # ?? i2c = I2C(scl=I2C_SCL, sda=I2C_SDA, freq=400000)
    # DEFAULT_I2C_ADDR = 0x27
    lcd = I2cLcd(i2c, DEFAULT_I2C_ADDR, 2, 16)
    lcd.show_cursor()
    lcd.blink_cursor_on()
    lcd.putstr("Hello Smart\nWorld! It works!")
    lcd.hide_cursor()
    time.sleep(5)
    lcd.clear()
    # run internal LCD test in a thread
    lcd.run()
