"""
wifimanager.py - connects to Wifi networks
* Micropython: Pycom uP
* static or dynamic IP
* JSON-based
2019-0910 checked if still working - minor code changes
2018-0528 PePo adopted to pycom. add mac-address

"""

# pycom:
from network import WLAN, Server
import machine
import time
from ubinascii import hexlify

# configurations
USE_DEBUG = False   # DEBUG or not debug


def print_debug(msg):
    """print_debug() - for debugging """
    if USE_DEBUG:
        print(msg)


class WifiManager:

    def __init__(self, known_nets):
        self._known_nets = known_nets
        # create network in STAtion mode
        # pycom: device always starts up in AP-mode
        #self._wl = WLAN()
        #self._wl.mode(WLAN.STA)

    '''def print_debug(self, message):
        """print_debug() - for debugging """
        if USE_DEBUG:
            print(msg)
    '''

    # 2019-1203 new, due to Exception error in legacy WifiManager
    # pre-condition: self._known_nets is not None
    # post-condition: self._wl is created
    # returns: IP
    # URL: https://docs.pycom.io/tutorials/all/wlan/
    def connect(self):
        """connect() - connects device according to network parameters in JSON-file."""
        if machine.reset_cause() != machine.SOFT_RESET:
            # from network import WLAN
            self._wl = WLAN()
            self._wl.mode(WLAN.STA)
            original_ssid = self._wl.ssid()
            original_auth = self._wl.auth()

            print_debug("Wifimanager - scanning for known wifi nets...")
            available_nets = self._wl.scan()
            nets = frozenset([e.ssid for e in available_nets])

            known_nets_names = frozenset([key for key in self._known_nets])
            net_to_use = list(nets & known_nets_names)
            print_debug("Wifimanager - SSID to use...{}".format(net_to_use))
            try:
                net_to_use = net_to_use[0]
                print_debug("Wifimanager - net to use...{}".format(net_to_use))
                net_properties = self._known_nets[net_to_use]
                pwd = net_properties['pwd']
                sec = [e.sec for e in available_nets if e.ssid == net_to_use][0]
                print_debug("Wifimanager - net_properties...{}".format(net_properties))
                if 'wlan_config' in net_properties:
                    print_debug("Wifimanager - wlan_config...{}".format(net_properties['wlan_config']))
                    self._wl.ifconfig(config=net_properties['wlan_config'])
                self._wl.connect(net_to_use, (sec, pwd), timeout=10000)
                ip = self.wait_for_networking(1)
                self._ssid = net_to_use
                print_debug("Connected to "+net_to_use+" with IP address:" + ip)

            except Exception as e:
                print("Failed to connect to any known network, going into AP mode")
                self._wl.init(mode=WLAN.AP, ssid=original_ssid, auth=original_auth, channel=6, antenna=WLAN.INT_ANT)
                self._ssid = None

        else:
            print_debug("Already connected to "+net_to_use+" with IP address:" + self._wl.ifconfig()[0])

        return self._wl.ifconfig()[0]

    def wait_for_networking(self, dt=1):
        """ wait unitil network is connected and returns IP"""
        station = self._wl  # network.WLAN(mode=network.WLAN.STA)
        while not station.isconnected():
            time.sleep(dt)
            machine.idle()
        ip = station.ifconfig()[0]
        return ip

    # wrapper for disconnecting network
    def disconnect(self):
        """disconnect() - de-activate network interface, but leaves Wifi radio on"""
        self._wl.disconnect()  # pycom - disconnect from Wifi, but leave Wif radio on.
        print_debug('WifiManager::Wifi disconnected')

    # wrapper for disabling Wifi radio
    def deinit(self):
        """deinit() - disable Wifi radio"""
        self._wl.deint()  # pycom
        print_debug('WifiManager::Wifi radio off')

    # wrapper for network scan
    def scan(self):
        """scan() - Performs a network scan and returns a list
        of named tuples with (ssid, bssid, sec, channel, rssi)
        """
        return self._wl.scan()

    def change_access(self, user=None, passwrd=None):
        """change_access - change password for telnet and ftp access"""
        if (user is None) or (passwrd is None):
            print('WifiManager:: username and password must be specified')
            return

        server = Server()  # from network
        # disable the server
        server.deinit()
        # enable the server again with new credentials
        # for ftp and telnet, not USB
        server.init(login=(user, passwrd), timeout=600)
        print_debug('WifiManager::password {} is changed...'.format(user))

    # wrappers for wlan settings.
    @property
    def ssid(self):
        """ ssid() - returns SSID of connected Wifi network"""
        return self._ssid

    @property
    def isconnected(self):
        """isconnected() - returns if connected to Wifi (True)
        or not (False)"""
        return self._wl.isconnected()

    @property
    def ip(self):
        """ip() - returns IP of device on connected Wifi network"""
        return self._wl.ifconfig()[0]

    @property
    def mac(self):
        """returns MAC-address of device"""
        mac = hexlify(self._wl.mac(), ':').decode()  # pycom
        # return (mac) # lower case
        return mac.upper()

    # ================================================
    # legacy methods
    # ================================================
    import json

    def __readjson(self, jsonfile):
        """readjson(file) - returns the contents of file in JSON-format"""
        with open(jsonfile, 'r') as infile:
            config = json.load(infile)
        if USE_DEBUG:
            print('WifiManager::JSON settings: {}'.format(config))
        return config


# test/usage
if __name__ == "__main__":
    # from wifimanager import WifiManager
    try:
        from wifisettings import known_nets
        # legacy: wifi = WifiManager('/config/wificonfig_home.json')
        wifi = WifiManager(known_nets)
        wifi.connect()  # connect device to wifi
        print('Device IP: {0}'.format(wifi.ip))  # device IP
    except OSError as err:
        print('OSError: file not found...{}'.format(err))
    except Exception as ex:
        print('Exception...')
        print(ex)
