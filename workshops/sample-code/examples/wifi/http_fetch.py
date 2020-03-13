"""
http_fetch: Performing an HTTP request using raw sockets

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

# when succesful, put code in Python file:
"""
import socket
# requires function get_ip()
from examples.dns_lookup import get_ip

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


def http_fetch(url):
    print("get HTML-page '{}'".format(url))
    # fetch and print the HTML-page...
    html = fetch(url)
    print(html)


def main():
    print('DEMO HTTP request using raw sockets...')
    url = 'http://micropython.org/ks/test.html'
    http_fetch(url)
    print('-----')


if __name__ == '__main__':
    main()
