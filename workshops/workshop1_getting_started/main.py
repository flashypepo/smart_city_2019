"""
main.py - main startup
2019-0906 Peter - 'hello world' - blinking LED
"""
import micropython
import pycom
import time

# allocate memory for exceptions...
# Pycom: https://docs.pycom.io/chapter/firmwareapi/micropython/micropython.html
micropython.alloc_emergency_exception_buf(100)

pycom.heartbeat(False)

# """ w/o exception
while True:
    pycom.rgbled(0xFF0000)  # Red
    time.sleep(1)
    pycom.rgbled(0x00FF00)  # Green
    time.sleep(1)
    pycom.rgbled(0x0000FF)  # Blue
    time.sleep(1)


"""

# add exception for a gracefully end
try:
    while True:
        pycom.rgbled(0xFF0000)  # Red
        time.sleep(1)
        pycom.rgbled(0x00FF00)  # Green
        time.sleep(1)
        pycom.rgbled(0x0000FF)  # Blue
        time.sleep(1)
except KeyboardInterrupt:
    pycom.heartbeat(True)
    print("done!")
# """
