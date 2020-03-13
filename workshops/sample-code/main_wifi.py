"""
Examples of networking.
Pre-conditie: device is connected to web
    either via pybytes provisioning (pybytes_config.)
    or DIY in boot.py (USE_WIFI=True)

main.py is splitup in various modules,
Each module can be found in folder examples/wifi.

1. dns_lookup.py: DNS lookup
2. http_fetch.py: HTTP request with sockets
3. http_fetch_urequests.py: HTTP request with custom library urequest
4. fetch_iss_station.py: HTTP request which returns JSON data (RESTfull webservice)
5. simple_webserver.py: simple HTTP webserver (data, handler)
    Let op: inschakelen webserver kan alleen
    onderbroken worden met een harde-reset en
    onderbreken main programma met Ctrl-C.

History
2020-0303 PP main splitup in modules.
          Adding device and wifi in pytbytes (provisioning), and
          gets the code working in Pycom firmware 1.20.2.rc6 (pytbytes)!
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


# execution of the various demos
if __name__ == '__main__':
    print('\nEntering main.py...')

    # activate/deactivate various demo's
    USE_DNS_DEMO = False  # 2020-0303 okay
    USE_HTTP_REQUEST_SOCKET_DEMO = False  # 2020-0303 okay
    USE_HTTP_REQUEST_UREQUETSTS_DEMO = False  # 2020-0303 okay
    USE_WEBSERVICE_JSON = True   # 2020-0303 okay

    # ********************************************
    # Let op: inschakelen webserver kan alleen
    # onderbroken worden met een harde-reset en
    # na restart onderbreken programma met Ctrl-C.
    # ********************************************
    USE_WEBSERVER = False  # 2020-0303 okay
    USE_WEBSERVER_HANDLER = False  # 2020-0303 okay

    """ Note: When you run Python on a typical computer,
    the operating system takes care of the process
    of ensuring all network connections are up before
    starting other services for you.

    In the case of MicroPython, there is no operating
    system—it's just your script running on bare metal.
    You have to take these things into account so that
    your code can run correctly."""

    from netcheck import wait_for_networking
    ip = wait_for_networking()
    print_debug("IP of device is {}".format(ip))
    if ip is None:
        print("\tdevice not connected to Wifi")
    print('-----')

    #################################
    # execute the networking examples
    #################################

    # perform dns lookup...
    if USE_DNS_DEMO and ip is not None:
        from examples.wifi import dns_lookup
        dns_lookup.main()

    # Performing an HTTP request using raw sockets
    if USE_HTTP_REQUEST_SOCKET_DEMO and ip is not None:
        from examples.wifi import http_fetch
        http_fetch.main()

    # Performing an HTTP request using custom library urequests
    if USE_HTTP_REQUEST_UREQUETSTS_DEMO and ip is not None:
        from examples.wifi import http_fetch_urequests
        http_fetch_urequests.main()

    # Fetching JSON data from a RESTful web service
    if USE_WEBSERVICE_JSON and ip is not None:
        from examples.wifi import fetch_iss_station
        fetch_iss_station.main()

    # Creating an HTTP server
    if USE_WEBSERVER and ip is not None:
        # inschakelen webserver kan alleen onderbroken worden
        # met een harde-reset en onderbreken huidige
        # programma in main (Ctrl-c).
        from examples.wifi import simple_webserver
        print('Creating an HTTP server...')
        simple_webserver.webserver()
        print('-----')

    if USE_WEBSERVER_HANDLER and ip is not None:
        # inschakelen webserver kan alleen onderbroken worden
        # met een harde-reset en onderbreken huidige
        # programma in main (Ctrl-c).
        from examples.wifi import simple_webserver
        # example 2 - webserver which shows a random number
        simple_webserver.webserver_handler()
        print('-----')

    # cleanup and closing...
    import gc
    gc.collect()
    print('main(): free memory {} Kb'.format(gc.mem_free() // 1024))
    print('main done')
