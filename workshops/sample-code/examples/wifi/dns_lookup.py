"""
dns_lookup.py - performing a DNS lookup

Whenever our applications try and connect to the host,
one of the first steps is to look up the hostname using
the DNS protocol and get the host's IP address so that
you can open a connection to that IP address.

First, experiment in REPL (prototyping)

>>> import socket
>>> addr_info = socket.getaddrinfo('python.org', 80)
>>> addr_info
[(2, 1, 0, '', ('45.55.99.72', 80))]
>>>
>>> ip = addr_info[0][-1][0]
>>> ip
'45.55.99.72'
>>> def get_ip(host, port=80):
...    addr_info = socket.getaddrinfo(host, port)
...    return addr_info[0][-1][0]
>>>
>>> hosts = ['python.org', 'micropython.org', 'pypi.org']
>>> for host in hosts:
...    print('IP van {0}: {1}'.format(host, get_ip(host, port=80)))
IP van python.org: 45.55.99.72
IP van micropython.org: 176.58.119.26
IP van pypi.org: 151.101.192.223
>>>
# when succesful, put code in Python file, such as dns_lookup.py

2020-0303 PP first version for SmartCity-S2
             using firmware: 1.20.2.rc6 (pytbytes)
"""
import time
import socket

HTTP_PORT = 80
BOOTUP_WIFI_DELAY = 5
# sleep for five seconds to allow the board to
# establish a connection to the Wi-Fi network on
# boot-up before performing the DNS lookups.
# The value of 5 seconds depends on the network!
# Any time you use hardcoded sleep values in your code,
# you should dig deep and try to find better solutions.


def get_ip(host, port=HTTP_PORT):
    addr_info = socket.getaddrinfo(host, port)
    return addr_info[0][-1][0]


def dns_lookup(hosts):
    print('dns_lookup: applying wifi delay...')
    time.sleep(BOOTUP_WIFI_DELAY)
    print('dns_lookup: performing DNS lookup...')
    for host in hosts:
        print(host, get_ip(host))


def main():
    print('DEMO DNS lookup...')
    hosts = ['python.org', 'micropython.org', 'pypi.org']
    dns_lookup(hosts)
    print('-----')


if __name__ == '__main__':
    main()
