"""
HSR04 proximity sensor: test program

TODO:
1. make a class UltrasonicSensor, such as (2017):
   https://github.com/mithru/MicroPython-Examples/tree/master/08.Sensors/HC-SR04
2. Send distacne to TTN - dont forget to multiply (float)distance with 10.

2020-0324 PP changes: use raw (float)values instead of integers for distance.
2020-0324 PP new, based upon code from
https://core-electronics.com.au/tutorials/hc-sr04-ultrasonic-sensor-with-pycom-tutorial.html
"""
import utime
import pycom
import machine
from machine import Pin

# initialise Ultrasonic Sensor pins

echo = Pin(Pin.exp_board.G7, mode=Pin.IN)  # 'P20'
trigger = Pin(Pin.exp_board.G8, mode=Pin.OUT)  # 'P21'
trigger(0)


# Ultrasonic distance measurment
def distance_measure():
    # trigger pulse LOW for 2us (just in case)
    trigger(0)
    utime.sleep_us(2)
    # trigger HIGH for a 10us pulse
    trigger(1)
    utime.sleep_us(10)
    trigger(0)
    # wait for the rising edge of the echo then start timer
    while echo() == 0:
        pass
    start = utime.ticks_us()
    # wait for end of echo pulse then stop timer
    while echo() == 1:
        pass
    finish = utime.ticks_us()
    # pause for 20ms to prevent overlapping echos
    utime.sleep_ms(20)
    # calculate distance by using time difference between start and stop
    # speed of sound 340m/s or .034cm/us. Time * .034cm/us = Distance sound travelled there and back
    # divide by two for distance to object detected.
    distance = ((utime.ticks_diff(start, finish)) * .034)/2
    # DEBUG: print('distance={}'.format(distance))
    return -distance  # 202-03 PP changed sign


# to reduce errors we take ten readings and use the median
# 2020-0324 PP use the raw (float)values instead of integers
# TODO: when using TTN/LoRa: dont forget to multiply distance with 10.
def distance_median():
    # initialise the list
    distance_samples = []
    # take 10 samples and append them into the list
    for count in range(10):
        # 2020-0324 PP changed: distance_samples.append(int(distance_measure()))
        distance_samples.append(distance_measure())
    # sort the list
    distance_samples = sorted(distance_samples)
    # take the center list row value (median average)
    distance_median = distance_samples[int(len(distance_samples)/2)]
    # apply the function to scale to volts
    # DEBUG: print(distance_samples)
    # 2020-0324 PP changed: return int(distance_median)
    return distance_median


def main():
    while True:
        # print(distance_measure())
        distance = distance_median()
        print("Distance: {:00.1f}".format(distance))


if __name__ == '__main__':
    main()
