"""
main.py - main startup of workshop 4  analog and digital IO,
sensors and actuators
2019-0926 Peter - added USE_GFX eand BME280 sample code
2019-0917 Peter - split up in modules
2019-0912 Peter - workshop 4 sample code

System configuration:
sensor/actuator       | GPIO-pin        | Application/driver
                      | (exp.board)     |
------------------------------------------------------------
CCS811, i2c           | G16 / I2C_SCL   | lib/CCS811.py
                      | G17 / I2C_SDA   |
OLED i2c              | G16 / I2C_SCL   | SSD1306_I2C
                      | G17 / I2C_SDA   |
Vcc (3V3), GND

"""
import time
import gc

# device configuration:
USE_CCS811 = True          # I2C: gas sensor

if __name__ == '__main__':
    gc.collect()  # cleanup memory / garbage collect

    # CCS811 gas sensor
    # pre-condition: i2c is not None - see boot.py
    print('DEMO gas sensor...{}'.format(USE_CCS811))
    if USE_CCS811:
        from CCS811 import CCS811
        import time
        from oledApp import OLEDApp
        # gc.collect()  # trial-and-error garbage collect

        app = OLEDApp(i2c=i2c, width=128, height=32)
        msg = {
            'Gas sensor': (0, 0),
            ' ': (30, 10),
            ' ': (60, 20),
        }
        app.showText(msg)

        # create gas sensor, and reset it
        try:
            # gs = CCS811.CCS811(i2c)
            gs = CCS811(i2c)
            gs.reset()
            time.sleep(0.5)  # trial-and-error waittime

            # test: read sensor values, sleep 10 secs
            while True:
                # console print...
                print('VOC reading...{}'.format(gs.readtVOC()))
                time.sleep(0.5)  # trial-and-error waittime
                print('CO2 reading...{}'.format(gs.readeCO2()))
                # OLED print...
                msg = {
                    'Gas sensor...': (20, 0),
                    'VOC: {}'.format(gs.readtVOC()): (5, 10),
                    'CO2: {}'.format(gs.readeCO2()): (5, 20),
                }
                app.clearDisplay()
                app.showText(msg)
                time.sleep(10)

        except ValueError as ex:
            print(ex)
            pass
