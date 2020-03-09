"""
blinkingled_direct.py - 'hello world' for microcontrollers

History
2020-03 Smart City semester 2
2020-03 PP direct execution of code - Arduino style
firmware v1.20.2.rc6
"""
import pycom
import time

pycom.heartbeat(False)

while True:
    pycom.rgbled(0xFF0000)  # Red
    time.sleep(1)
    pycom.rgbled(0x00FF00)  # Green
    time.sleep(1)
    pycom.rgbled(0x0000FF)  # Blue
    time.sleep(1)
    pycom.rgbled(0x000000)  # Black = off
    time.sleep(1)

# Note: next statement does not get executed when user interrupts
pycom.heartbeat(True)
