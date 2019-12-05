# boot.py -- run on boot-up
# 2019-0915 disabe wifi and wdt
# bron: https://docs.pycom.io/firmwareapi/pycom/pycom/
import micropython
import pycom
from machine import I2C

# allocate memory for exceptions...
# Pycom: https://docs.pycom.io/chapter/firmwareapi/micropython/micropython.html
micropython.alloc_emergency_exception_buf(100)

# disable WiFi on boot, i.e. no AP-netwerk on Wifi
pycom.wifi_on_boot(False)
print('Wifi AP-mode enabled: ', pycom.wifi_on_boot())

# If this flag is set, the application needs to reconfigure the WDT with a
# new timeout and feed it regularly to avoid a reset.
pycom.wdt_on_boot(False)  # no Watch Dog
print('WDT enabled: ', pycom.wdt_on_boot())

# setup i2c, use default PIN assignments (P10=SDA, P11=SCL)
# Expansion board 3.0: SCL=GPO17 ('P10'), SDA=GPO16 ('P9')
i2c = I2C(0, I2C.MASTER)
print('i2c scan:', i2c.scan())
