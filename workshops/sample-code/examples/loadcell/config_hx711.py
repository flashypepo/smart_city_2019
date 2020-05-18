"""
HX711 configuration parameters
Connection HX711 -- LoPy4/Expansion board

# Example for Expansionboard / Lopy4 device.
# Connections:
# Exp.board  | HX711    | Lopy4 | used for
# -----------|----------|-------|---------
# G13        | data_pin | P6    | --
# G14        | clock_pin| P7    | --
#

2020-0516 PP new
"""
# HX711 constants
CHANNEL_A = const(128)  # gain and channel A
CHANNEL_B = const(32)   # gain and channel B
# CHANNEL_A = const(64)  # gain and channel A

# OK: DATA_PIN = 'P9'  # G16
# OK: CLOCK_PIN = 'P8'  # G15
DATA_PIN = 'P6'  # G13
CLOCK_PIN = 'P7'  # G14
