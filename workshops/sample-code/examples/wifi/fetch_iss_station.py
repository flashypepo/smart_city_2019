"""
fetch_json - fetching JSON data from a RESTful web service.

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

# when succesful, put code in Python file:
"""
import urequests
import time

# URL webservices
# ISS Space station position:
#     http://open-notify.org/Open-Notify-API/ISS-Location-Now/
# Map: http://open-notify.org/Open-Notify-API/
# People in Space:
#     http://open-notify.org/Open-Notify-API/People-In-Space/
ISS_API_URL = 'http://api.open-notify.org/iss-now.json'
ISS_ASTRO_URL = 'http://api.open-notify.org/astros.json'


def parse_iss_json(data):
    """parse_iss_json() - parse ISS Json data
        arg: data, a valid Json-string
        returns: tuple (timestamp, position)"""
    timestamp = data['timestamp']
    position = data['iss_position']
    return timestamp, position


def track_space_station():
    """track_space_station() - tracks position of ISS Space Station"""
    print_str = '{0}-{1:02}-{2:02} {3:02}:{4:02}:{5:02} lat: {latitude} long: {longitude}'
    for i in range(10):
        data = urequests.get(ISS_API_URL).json()
        timestamp, position = parse_iss_json(data)
        year, month, day, hr, min, sec, _, _ = time.localtime(timestamp)
        print(print_str.format(year, month, day, hr, min, sec, **position))
        time.sleep(1)


def parse_astro_json(data):
    """parse_astro_json() - parse inhabitant ISS JSON data
        arg: data, a valid JSON-string, returns: tuple (n, names)
        n = number of astronauts onboard
        names = list of names"""
    n = data['number']
    people = data['people']
    names = []  # list of names
    for men in people:
        names.append(men['name'])
    return (n, names)


def iss_inhabitants():
    """iss_inhabitants() - prints current inhabitants of ISS Space Station """
    data = urequests.get(ISS_ASTRO_URL).json()
    n, names = parse_astro_json(data)
    print('ISS Space Station has {0} astronauts: {1}'.format(n, names))


# Fetching JSON data from a RESTful web service
def main(dt=10):
    print('Fetching JSON data from a RESTful web service...')
    print('Inhabitants of the ISS station:')
    iss_inhabitants()
    print('Tracking position of the ISS-station...')
    # example: follow position of the ISS-station
    while True:
        track_space_station()  # prints position of ISS space station
        print('---')
        iss_inhabitants()  # also prints inhabitants of ISS space station
        time.sleep(dt)


if __name__ == '__main__':
    main()
