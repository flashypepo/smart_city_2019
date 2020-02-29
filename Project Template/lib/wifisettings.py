"""
wifisettings - collection of known wifi networks

URL: https://docs.pycom.io/tutorials/all/wlan/
section: 'Multiple Networks using a Static IP Address'

2019-1203 Reason: problems with connecting to wifi due to
following (Exception) message:
"
WifiManager::WLAN mode: 1
Exception...
object with buffer protocol required
"
Specify for each ssid (wifi netwerk):
1. passwrd
2. for STATIC IP: provide values for 'wlan_config'
3. for DYNAMIC IP, such as your home Wifi: remove 'wlan_config' values.

Format:
known_nets = {
  'ssid_name': {'pwd': 'passwrd',
                'wlan_config': (ip, subnet_mask, gateway, DNS_server),
                },
     .....
}
"""
known_nets = {
    'devices': {'pwd': 'devices2',
                       'wlan_config': ('145.44.186.xxx', '255.255.255.128', '145.44.186.1', '8.8.8.8')
                },
    'ZiggoPePo': {'pwd': 'hGsnbaY2yfrw',
                         'wlan_config': ('192.168.178.103', '255.255.255.0', '192.168.178.1', '8.8.8.8')
                  }
}
