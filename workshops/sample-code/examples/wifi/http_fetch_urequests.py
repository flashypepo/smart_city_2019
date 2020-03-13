"""
http_fetch_urequets
  - Performing an HTTP request using the urequests library.

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


def http_fetch_urequest(url):
    response = urequests.get(url)  # response object
    print('HTTP status code:{}'.format(response.status_code))
    html = response.text
    print(html)


def main():
    print("DEMO HTTP request using 'urequests'...")
    url = 'http://micropython.org/ks/test.html'
    http_fetch_urequest(url)
    print('-----')


if __name__ == '__main__':
    main()
