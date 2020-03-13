"""
Create a web server in MicroPython that will serve
web pages with dynamic content on the LoPy4.

In example 1 (webserver), each time a browser visits the
web server, it will display the current uptime
of the board in seconds.

We'll ensure that the web page that's generated will
render well on computer web browsers, as well as
phone browsers. It can be a very powerful tool
for the projects you create, as that you have
the ability to interact with them from any phone
or computer on your network using a web browser.

This example 1 shows you how to create projects like this,
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

# when succesful, put code in Python file:

"""
import socket
import time
# import random    # Pycom: no module 'random'
from os import urandom
from netcheck import wait_for_networking

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


# inschakelen webserver kan alleen onderbroken worden
# met een harde-reset en onderbreken huidige
# programma in main (Ctrl-c).
def webserver():
    print('Creating an HTTP server...')
    ip = wait_for_networking()  # get IP from netcheck
    sock = socket_listen()
    serve_requests(sock, ip)
    print('-----')


"""
Example 2: Creating a web handler module.

This 2nd example will show you how we can take a lot of
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

from web import BASE_TEMPLATE, run_server


# Source:
#  https://forum.pycom.io/topic/3841/lopy4-random-number-method-solved/3
def random():
    return (int.from_bytes(urandom(1), "big"))


def handler(request, method, path):
    # body = 'random: %s' % random.random()
    body = 'random: %s' % random()
    return BASE_TEMPLATE % body


# inschakelen webserver kan alleen onderbroken worden
# met een harde-reset en onderbreken huidige
# programma in main (Ctrl-c).
def webserver_handler():
    print('Creating an HTTP server with handler...')
    print('Example: start a web server that generates random numbers whenever you visit it.')
    run_server(handler)


if __name__ == '__main__':
    ''' execute either example 1 or 2

    # example 1: simple webserver
    webserver()
    '''

    # example 2:  webserver that generates random numbers
    webserver_handler()
    # '''
