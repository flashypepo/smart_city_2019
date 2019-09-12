"""
RGLed aansturen
workshop 2: lab-oefening 3 en 4
2019-0912 nieuw
"""
import pycom

pycom.heartbeat(False)

# ---------------
# Workshop - oefening 3
# ---------------
# maak de functie traffic_cycle
# en bijbehoredne variabelen en data-types
def traffic_cycle():
    pass


# ---------------
# Workshop - oefening 4
# ---------------
# maak de functie fade() en demo()
# met bijbehoredne variabelen en data-types

# Gegeven helper functie:
def rgb_to_hex(red, green, blue):
    """Return color as #rrggbb for the given color values."""
    return '0x{:02X}{:02X}{:02X}'.format(red, green, blue)


def fade():
    pass
    # verwijder 'pass' en maak code
    # waarin RGBLed oplicht (fade in) OF uitvaagt (fade out).
    # Je mag ook twee functies maken (fadeIn(), fadeOut())


def demo():
    # verwijder 'pass' en maak een oneindige loop
    # waarin RGBLed oplicht (fade in),
    # en vervolgens uitvaagt (fade out).
    pass


# verander nets aan onderstaande code
# Het is de test voor de uitwerking (TDD-programming)
if __name__ == '__main__':
    # oefening 3:
    traffic_cycle()
    # oefening 4:
    demo(0.5)
