# PWM: pulsing LED
# firmware 1.20.2.rc6
# 2020-03 PP Smart City semester 2
# 2018-09 PP new

from machine import Pin, PWM
import math
import time


# LED configuration
def setup(gpio, freq=1000):
    pwm = PWM(0, frequency=freq)
    led = pwm.channel(0, pin=gpio, duty_cycle=0)
    return led


# pulse function
def pulse(led, t):
    """pulse led l with time interval t in ms"""
    for i in range(17):
        led.duty_cycle(math.sin(i / 10 * math.pi))
        time.sleep_ms(t)


def main():
    print('Demo pulsing LED...')

    # ''' - remove # for yellow led
    # pulsing blue led
    led = setup(Pin.exp_board.G22)  # blue, P11
    '''
    # pulsing yellow led
    led = setup(Pin.exp_board.G12)  # yellow, P5
    # '''

    for i in range(50):
        # ''' pulse LED with differend duty-cycles
        duty_cycles = [10*i for i in range(10)]
        # slower
        print('\tslowing down...')
        for duty_cycle in duty_cycles:
            pulse(led, duty_cycle)
        # faster
        print('\tgoing faster...')
        duty_cycles.reverse()
        for duty_cycle in duty_cycles:
            pulse(led, duty_cycle)


if __name__ == '__main__':
    main()
