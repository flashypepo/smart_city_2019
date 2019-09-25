"""
RGLed aansturen
workshop 2: lab-oefening 3 en 4
2019-0912 nieuw
"""
import pycom

pycom.heartbeat(False)

# oefening 3
RED = const(0xFF0000)
ORANGE = const(0xFFA500)
GREEN = const(0x00FF00)
# eventueel meerdere kleuren

colors = [RED, ORANGE, GREEN]  # order of traffic lights

# dictionary om kleur en tijd aan elkaar te koppelen
traffic_lights = {
    RED: 3,
    ORANGE: 1,
    GREEN: 5,
}


# cycle through {color:time} dictionary
def traffic_cycle():
    for color, dt in traffic_lights.items():
        pycom.rgbled(color)
        time.sleep(dt)
    pycom.rgbled(0)  # RGBLed off


# oefening 4
# gegeven helper functie
def rgb_to_hex(red, green, blue):
    """Return color as #rrggbb for the given color values."""
    return '0x{:02X}{:02X}{:02X}'.format(red, green, blue)


# fade() - oplossing 1
def fade(min, max, step):
    """fade(min, max. step): helderheid RGBLed
       van min naar max met step"""
    for i in range(min, max, step):
        color = rgb_to_hex(i, i, i)
        # print('color:', color)
        pycom.rgbled(256-int(color, 16))
        time.sleep(0.005)


def fadeIn():
    min, max, step = 0, 256, 1
    fade(min, max, step)


def fadeOut():
    min, max, step = 255, 0, -1
    fade(min, max, step)


# oefening 4 - oplossing 2
# Dit vervaagt van wit naar uit (isUp=True),
# anders vervaagt led van uit naar wit (isUp=False)
# functie range(min, max, step):
#     step = +1 -> optellen
#     step = -1 -> aftellen
# let op grenzen min en max.
def fadeInOut(isUp=True):
    if isUp:
        min, max, step = 0, 256, 1
    else:
        min, max, step = 255, 0, -1
    # for i in range(255, 0, -1):
    for i in range(min, max, step):
        color = rgb_to_hex(i, i, i)
        # print('color:', color)
        pycom.rgbled(256-int(color, 16))
        time.sleep(0.005)


def demo():
    """ demo() - RGBLed fade-in en fade-out met exception handling"""
    try:
        while True:
            # """ oplossing 1, bij weghalen '#'-teken -> oplossing 2
            # oplossing 1
            fadeIn()   # fade in
            fadeOut()  # fade out
            """
            # oplossing 2:
            fadeInOut(isUp=True)   # fade in
            fadeInOut(isUp=False)  # fade out
            # """
    except KeyboardInterrupt:
        pycom.rgbled(0)  # RGBled off
        print('done')


# main entry - (TDD)
if __name__ == '__main__':
    # oefening 3:
    #traffic_cycle()
    # oefening 4:
    demo()
