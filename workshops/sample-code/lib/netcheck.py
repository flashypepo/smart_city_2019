"""
netcheck.py - utility functions to check network

wait_for_networking() - a function to wait for internet connectivity

If your script starts immediately, connecting to the
internet before the network connection has come up,
it will raise exceptions and fail to continue.

Once the function 'wait_for_networking' has
detected that a connection has been successfully
established, and an IP address has been assigned,
then the function will return.

2020-0306 PP added idl and Timer for timeout.
2019-1103 from Micropyton Cookbook, PacktPublishing,
          Peter: adopted for Pycom micropython
"""
import network
import time
import machine


def wait_for_networking(dt=5):
    """ wait_for_networking(dt=5):
             wait for wifi connection within dt seconds
    """
    print('checking network connection...')
    chrono = machine.Timer.Chrono()
    chrono.start()
    station = network.WLAN(mode=network.WLAN.STA)
    start = chrono.read()  # read first time
    while not station.isconnected():
        print('waiting for network...')
        machine.idle()  # save power while waiting
        time.sleep(1)
        if chrono.read() - start > dt:
            print('timeout...')
            chrono.stop()
            return None  # there is no IP
    ip = station.ifconfig()[0]
    print('Device IP address on network:', ip)
    return ip


"""
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
# when succesful, add code to detect timeout (Timer),
# and put code in Python file.
"""
