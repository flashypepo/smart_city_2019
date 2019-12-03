"""
Examples of networking.
Pre-conditie: device is connected to web (see boot.py)

1. DNS lookup
2. HTTP request with sockets
3. HTTP request with custom library urequest
4. HTTP request which returns JSON data
5. HTTP webserver (data, handler)
    Let op: inschakelen webserver kan alleen
    onderbroken worden met een harde-reset en
    onderbreken main programma met Ctrl-C.

2019-1203 Demos work for Pycom version 1.18.2.* - 1.19.0.b4. 
          Demos do not work with Pycom v1.20.*

2019-1103 examples from Micropython Cookbook, packtpub publishing, 2018
          https://www.packtpub.com/application-development/micropython-cookbook
          adopted by Peter for Pycom Micropython
"""

USE_DEBUG = False  # controls DEBUG messages in console


# helper for printing DEBUG messages on console
def print_debug(msg):
    if USE_DEBUG:
        print(msg)


"""
Performing a DNS lookup
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
"""
# when succesful, put code in main.py:
import socket
import time

# sleep for five seconds to allow the board to
# establish a connection to the Wi-Fi network on
# boot-up before performing the DNS lookups.
# The value of 5 seconds depends on the network!
# Any time you use hardcoded sleep values in your code,
# you should dig deep and try to find better solutions.

BOOTUP_WIFI_DELAY = 5


def get_ip(host, port=80):
    addr_info = socket.getaddrinfo(host, port)
    return addr_info[0][-1][0]


def dns_lookup_demo():
    print('dns_lookup_demo: applying wifi delay...')
    time.sleep(BOOTUP_WIFI_DELAY)
    print('dns_lookup_demo: performing DNS lookup...')
    hosts = ['python.org', 'micropython.org', 'pypi.org']
    for host in hosts:
        print(host, get_ip(host))


"""
Creating a function to wait for internet connectivity
If your script starts immediately, connecting to the
internet before the network connection has come up,
it will raise exceptions and fail to continue.

 Once our created function 'wait_for_networking' has
 detected that a connection has been successfully
 established, and an IP address has been assigned,
 then the function will return.

First, experiment in REPL (prototyping)
>>> import network
>>> import time
>>>
>>> # following code detects if wifi is connected or not
>>> station = network.WLAN(mode=network.WLAN.STA)
>>> station.isconnected()
# --> True or False, dependend if connected or not
>>>
>>> # following code retrieves IP, once devices is connected
>>> ip = station.ifconfig()[0]
>>> ip
'145.44.186.5'    # IP depends on your static IP
>>>
>>> # combined in an function wait_for_networking()
>>> def wait_for_networking():
...     station = network.WLAN(mode=network.WLAN.STA)
...     while not station.isconnected():
...         print('waiting for network...')
...         time.sleep(1)
...     ip = station.ifconfig()[0]
...     print('address on network:', ip)
...     return ip
>>>
>>> # IP depends on your given static IP!
>>> ip = wait_for_networking()
address on network: 145.44.186.5
>>> ip
'145.44.186.5'
>>>
"""
# when succesful, put code in main.py:
import network
import time

#''' 2019-1203 see wifi in boot.py -----
def wait_for_networking():
    print('checking network connection...')
    station = network.WLAN()
    while not station.isconnected():
        print('waiting for connection...')
        time.sleep(1)
    ip = station.ifconfig()[0]
    print('Device IP address on network:', ip)
    return ip
#'''

""" Performing an HTTP request using raw sockets
We will create a function that receives a URL as its
input and returns the response from the requested
web server after performing the HTTP request.
We will also create a function that can parse a URL
and return the hostname and path components of the URL.
These pieces will be needed to perform the HTTP request.

First, experiment in REPL (prototyping)
>>> import socket, time
>>> # function, which takes a URL and returns
>>> # the host and path components:
>>> def parse_url(url):
...     return url.replace('http://', '').split('/', 1)
>>>
>>> url = 'http://micropython.org/ks/test.html'
>>> host, path = parse_url(url)
>>> host
'micropython.org'
>>> path
'ks/test.html'
>>> # define the fetch function, which receives a
>>> # URL as its input and retrieves its content
>>> # from a web server:
>>> HTTP_REQUEST = 'GET /{path} HTTP/1.0\r\nHost: {host}\r\n\r\n'
>>> BUFFER_SIZE = 1024
>>>
>>> def fetch(url):
...     host, path = parse_url(url)
...     ip = get_ip(host)
...     sock = socket.socket()
...     sock.connect((ip, 80))
...     request = HTTP_REQUEST.format(host=host, path=path)
...     sock.send(bytes(request, 'utf8'))
...     response = b''
...     while True:
...         chunk = sock.recv(BUFFER_SIZE)
...         if not chunk:
...             break
...         response += chunk
...     sock.close()
...     body = response.split(b'\r\n\r\n', 1)[1]
...     return str(body, 'utf8')
>>>
>>> html = fetch('http://micropython.org/ks/test.html')
>>> html
'<!DOCTYPE html>\n<html lang="en">\n    <head>\n        <title>Test</title>\n    </head>\n    <body>\n        <h1>Test</h1>\n        It\'s working if you can read this!\n    </body>\n</html>\n'
>>>
>>> print(html)
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Test</title>
    </head>
    <body>
        <h1>Test</h1>
        It's working if you can read this!
    </body>
</html>

"""
# when succesful, put code in main.py:
import socket
# requires function get_ip()
HTTP_REQUEST = 'GET /{path} HTTP/1.0\r\nHost: {host}\r\n\r\n'
HTTP_PORT = 80
BUFFER_SIZE = 1024

def parse_url(url):
    """ split url in host in path"""
    return url.replace('http://', '').split('/', 1)

"""
# returns IP for host
# in case function is not yet defined.
def get_ip(host, port=HTTP_PORT):
    addr_info = socket.getaddrinfo(host, port)
    return addr_info[0][-1][0]
"""

def fetch(url):
    host, path = parse_url(url)
    ip = get_ip(host)
    sock = socket.socket()
    sock.connect((ip, 80))
    request = HTTP_REQUEST.format(host=host, path=path)
    sock.send(bytes(request, 'utf8'))
    response = b''
    while True:
        chunk = sock.recv(BUFFER_SIZE)
        if not chunk:
            break
        response += chunk
    sock.close()
    body = response.split(b'\r\n\r\n', 1)[1]
    return str(body, 'utf8')

def http_fetch_demo():
    print("get HTML-page 'http://micropython.org/ks/test.html'...")
    # check connection to network...
    #2019-1203 removed: wait_for_networking()
    # fetch and print the HTML-page...
    html = fetch('http://micropython.org/ks/test.html')
    print(html)

"""
Performing an HTTP request using the urequests library.

The library 'urequest' provides an object that you can use to
perform your HTTP interactions. After the request
is completed, you can access different attributes
of this object to get a variety of information
on the completed request.

Note: The library 'urequest' is not part of the Micropython distribution.
See supplied lib/urequest.py

First, experiment in REPL:
>>> import urequests
>>> url = 'http://micropython.org/ks/test.html'
>>> req = urequests.get(url)
>>> req.text
'<!DOCTYPE html>\n<html lang="en">\n    <head>\n        <title>Test</title>\n    </head>\n    <body>\n        <h1>Test</h1>\n        It\'s working if you can read this!\n    </body>\n</html>\n'
>>> print(req.text)
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Test</title>
    </head>
    <body>
        <h1>Test</h1>
        It's working if you can read this!
    </body>
</html>

>>> # HTTP status code
>>> req.status_code
200
>>>
>>> # get a non-existing page:
>>> url = 'http://micropython.org/no_such_page_exists'
>>> req = urequests.get(url)
>>> req.status_code
404
>>>
>>> req.reason
b'Not Found'
>>>

"""
# when succesful, put code in main.py:
import urequests

def urequest_demo():
    #2019-1203 removed: wait_for_networking()
    url = 'http://micropython.org/ks/test.html'
    response = urequests.get(url)  # response object
    print('HTTP status code:{}'.format(response.status_code))
    html = response.text
    print(html)


"""
Fetching JSON data from a RESTful web service.

This example will show connecting to a server
on the web in order to consume its RESTful web service.
The web service will provide data in JSON format,
which will then be parsed so that we can access
different parts of the returned dataset.

The example web service provides the current location of
the International Space Station (ISS).
Since the ISS moves at an incredible speed of
28,000 km/h, we can watch its position, which is
expressed in terms of longitude and latitude,
change as we repeatedly call this web service.

Whenever you want to create a MicroPython project
that connects to the internet-based web services,
you can use the techniques covered in this example
as a starting point to build these connections.

First, experiment in REPL
>>> import urequests
>>> import time
>>> ISS_API_URL = 'http://api.open-notify.org/iss-now.json'
>>> req = urequests.get(ISS_API_URL)
>>> req.text
'{"iss_position": {"longitude": "119.8205", "latitude": "-27.6808"}, "timestamp": 1572787994, "message": "success"}'
>>> data = req.json()
>>> data
{'message': 'success', 'iss_position': {'longitude': '45.0667', 'latitude': '-33.1779'}, 'timestamp': 1555012195}
>>> data['iss_position']['latitude']
'-27.6808'
>>> data['iss_position']['longitude']
'119.8205'
>>> # function track_space_station() every second
>>> # over periode of 10 seconds
>>> def track_space_station():
...     for i in range(10):
...         data = urequests.get(ISS_API_URL).json()
...         position = data['iss_position']
...         print(i, 'lat: {latitude} long: {longitude}'.format(**position))
...         time.sleep(1)
...
...
...
>>>
>>> track_space_station()
0 lat: -11.7137 long: 133.5172
1 lat: -11.6386 long: 133.5737
2 lat: -11.5635 long: 133.6301
3 lat: -11.4633 long: 133.7054
4 lat: -11.3882 long: 133.7618
5 lat: -11.3130 long: 133.8181
6 lat: -11.2378 long: 133.8744
7 lat: -11.1627 long: 133.9307
8 lat: -11.0624 long: 134.0057
9 lat: -10.9872 long: 134.0619
>>>
"""
"""
>>> print('lat: {latitude} long: {longitude}'.format(**position))
Example format(**position) is Named placeholders.
Setup: data = {'first': 'Hodor', 'last': 'Hodor!'}
Code:  '{first} {last}'.format(**data)
Output: Hodor Hodor!
"""
# when succesful, put code in main.py:
import urequests
import time

ISS_API_URL = 'http://api.open-notify.org/iss-now.json'

def track_space_station():
    for i in range(10):
        data = urequests.get(ISS_API_URL).json()
        position = data['iss_position']
        print(i, 'lat: {latitude} long: {longitude}'.format(**position))
        time.sleep(1)

def track_iss_demo():
    #2019-1203 removed: wait_for_networking()
    track_space_station()


"""
Create a web server in MicroPython that will serve
web pages with dynamic content on the LoPy4.

In this example, each time a browser visits the
web server, it will display the current uptime
of the board in seconds.

We'll ensure that the web page that's generated will
render well on computer web browsers, as well as
phone browsers. It can be a very powerful tool
for the projects you create, as that you have
the ability to interact with them from any phone
or computer on your network using a web browser.

This example shows you how to create projects like this,
where you can submit any live sensor data or information
straight to people's browsers, regardless of whether
they connect from their phone or desktop computer.

First, experiment in REPL:
>>> import socket
>>> import time
>>>
>>> HTTP_PORT = 80
>>> TCP_BACKLOG = 0
>>> # define an HTML template that we will use to
>>> # generate pages before submitting them to the
>>> # connecting browsers.
# copy and paste the next lines in REPL with Ctrl-E and Ctrl-D
"""
TEMPLATE = """\
<!DOCTYPE HTML>
<html lang="en">
<head>
    <title>PyCom - LoPy4</title>
    <meta charset="UTF-8">
    <link rel="icon" href="data:,">
    <meta name="viewport" content="width=device-width">
</head>
<body>
    <h1>LoPy4:</h1>
    uptime: {uptime}s
</body>
</html>
"""
""" continue with REPL...
>>> def socket_listen():
...     sock = socket.socket()
...     sock.bind(('0.0.0.0', HTTP_PORT))
...     sock.listen(TCP_BACKLOG)
...     return sock
...
...
...
>>> ip = wait_for_networking()
address on network: 145.44.186.5
>>> sock = socket_listen()
>>> # copy and past function serve_request(sock, ip)
>>>  # with help of Ctrl-C and Ctrl-D
>>> # serve_requests() which will be in charge of serving any requests that are made to the web server.
"""
# when succesful, put code in main.py:
import socket
import time

HTTP_PORT = 80
TCP_BACKLOG = 0
TEMPLATE = """\
<!DOCTYPE HTML>
<html lang="en">
<head>
    <title>PyCom - LoPy4</title>
    <meta charset="UTF-8">
    <link rel="icon" href="data:,">
    <meta name="viewport" content="width=device-width">
</head>
<body>
    <h1>LoPy4:</h1>
    uptime: {uptime} seconds
</body>
</html>
"""

def socket_listen():
    sock = socket.socket()
    sock.bind(('0.0.0.0', HTTP_PORT))
    sock.listen(TCP_BACKLOG)
    return sock

def serve_requests(sock, ip):
    """
    The following block of code defines and calls the
    serve_requests function, which will be in charge
    of serving any requests that are made to the web
    server. The function is called, and then the web
    server is visited by a browser three separate times.
    Each time a request is served, its details are
    printed out
    """
    print('webserver started on http://%s/' % ip)
    print('\t hard-reset device when done')
    start = time.ticks_us()
    while True:
        conn, address = sock.accept()
        print('request:', address)
        request = conn.makefile()
        while True:
            line = request.readline()
            if not line or line == b'\r\n':
                break
        uptime = time.ticks_us() - start  # time.monotonic() - start
        html = TEMPLATE.format(uptime=uptime / 1E06)  # microseconds -> seconds
        conn.send(html)
        conn.close()

def webserver_demo():
    #2019-1203 removed: ip = wait_for_networking()
    ip = wifi.ip
    sock = socket_listen()
    serve_requests(sock, ip)


"""
Creating a web handler module.

This example will show you how we can take a lot of
the code and logic involved in handling sockets,
parsing HTTP request headers, and generating HTML,
and bundle it all into a single Python module.
Once we have it in one module, we can import this
module and pass it our web handler, which will do
all the heavy lifting for us.

You will find this example useful when you are creating
projects that create a web-based application on your
microcontroller and you want to get productive fast,
without getting bogged down in all the low-level details
of sockets and parsing HTTP headers.

First, experiment in REPL:
>>> from netcheck import wait_for_networking
>>> import socket
>>>
>>> HTTP_PORT = 80
>>> TCP_BACKLOG = 0
"""
# create a generic HTML template.
# Copy and Paste next lines using Ctrl-E and Ctrl-D
# on the REPL:
BASE_TEMPLATE = """\
 <!DOCTYPE HTML>
 <html lang="en">
 <head>
     <title>MicroPython</title>
     <meta charset="UTF-8">
     <link rel="icon" href="data:,">
     <meta name="viewport" content="width=device-width">
 </head>
 <body>
 %s
 </body>
 </html>
 """

"""
.... remaining code is put in lib/web.py
Usage in main: see execution statements below
"""


# execution of the various demos
if __name__ == '__main__':
    print('\nEntering main.py...')

    # activate/deactivate various demo's
    USE_DNS_DEMO = True
    USE_HTTP_REQUEST_SOCKET_DEMO = False
    USE_HTTP_REQUEST_UREQUETSTS_DEMO = False
    USE_WEBSERVICE_JSON = False

    # Let op: inschakelen webserver kan alleen
    # onderbroken worden met een harde-reset en
    # onderbreken main programma met Ctrl-C.
    USE_WEBSERVER = False
    USE_WEBSERVER_HANDLER = False

    # demo fo wait-for-network connected...
    # see implementation of lib/wifimanager.py
    print('DEMO wait_for_networking...')
    ip = wait_for_networking()
    print('device ip:', ip)
    print('-----')

    """ Note: When you run Python on a typical computer,
    the operating system takes care of the process
    of ensuring all network connections are up before
    starting other services for you.
    In the case of MicroPython, there is no operating
    system—it's just your script running on bare metal.
    You have to take these things into account so that
    your code can run correctly."""

    #################################
    # execute the networking examples
    #################################

    # perform dns lookup...
    if USE_DNS_DEMO:
        print('DEMO DNS lookup...')
        dns_lookup_demo()
        print('-----')

    # Performing an HTTP request using raw sockets
    if USE_HTTP_REQUEST_SOCKET_DEMO:
        print('DEMO HTTP request using raw sockets...')
        http_fetch_demo()
        print('-----')

    # Performing an HTTP request using custom library urequests
    if USE_HTTP_REQUEST_UREQUETSTS_DEMO:
        print('DEMO HTTP request using custom library urequests...')
        urequest_demo()
        print('-----')

    # Fetching JSON data from a RESTful web service
    if USE_WEBSERVICE_JSON:
        print('Fetching JSON data from a RESTful web service...')
        print('Position of the ISS-station...')
        # example: follow the possition of the ISS-station
        while True:
            track_iss_demo()
            print('-----')
            time.sleep(1)

    # Creating an HTTP server
    if USE_WEBSERVER:
        print('Creating an HTTP server...')
        # inschakelen webserver kan alleen onderbroken worden
        # met een harde-reset en onderbreken huidige
        # programma in main (Ctrl-c).
        webserver_demo()
        print('-----')

    if USE_WEBSERVER_HANDLER:
        from web import BASE_TEMPLATE, run_server
        # import random    # Pycom: no module 'random'
        from os import urandom

        # Source:
        #  https://forum.pycom.io/topic/3841/lopy4-random-number-method-solved/3
        def random():
            return (int.from_bytes(urandom(1), "big"))

        print('Creating an HTTP server with handler...')
        print('Example: start a web server that generates random numbers whenever you visit it.')

        def handler(request, method, path):
            # body = 'random: %s' % random.random()
            body = 'random: %s' % random()
            return BASE_TEMPLATE % body

        def webserver_handler_demo():
            run_server(handler)

        # execute
        webserver_handler_demo()

    # cleanup and closing...
    import gc
    gc.collect()
    print('main(): free memory {} Kb'.format(gc.mem_free() // 1024))
    print('main done')
