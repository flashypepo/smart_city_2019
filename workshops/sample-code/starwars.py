"""
Star Wars Asciimation
shows an animation of star wars in ASCII, telnet connection
should also work on computer with Python3.

Source:
URL: http://docs.micropython.org/en/latest/esp8266/esp8266/tutorial/network_tcp.html#star-wars-asciimation
"""
import socket
from netcheck import wait_for_networking

USE_DEBUG = False

# check network is connected
wait_for_networking()


# for debugging...
def print_debug(msg):
    if USE_DEBUG:
        print(msg)

# """
# NB. De 'losse' code werkt beter en sneller dan
#     als de functie wordt aangeroepen.
#     Reden: onbekend.
#  2019-1103 Peter

# get addres information of site
url = "towel.blinkenlights.nl"
addr_info = socket.getaddrinfo(url, 23)
print_debug(addr_info)


# get the IP and port
addr = addr_info[0][-1]
print_debug(addr)

# connect to it via socket
s = socket.socket()
s.connect(addr)

# print content/animation in console
# use cntrl-C to interrupt
while True:
    data = s.recv(500)
    print(str(data, 'utf8'), end='')

"""

def starwars_demo():
    # get addres information of site
    url = "towel.blinkenlights.nl"
    addr_info = socket.getaddrinfo(url, 23)
    print_debug(addr_info)

    # get the IP and port
    addr = addr_info[0][-1]
    print_debug(addr)

    # connect to it via socket
    s = socket.socket()
    s.connect(addr)

    # print content/animation in console
    # use cntrl-C to interrupt
    while True:
        data = s.recv(500)
        print(str(data, 'utf8'), end='')


if __name__ == '__main__':
    starwars_demo()

# """
