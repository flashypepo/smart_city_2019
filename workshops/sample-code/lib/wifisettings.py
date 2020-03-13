"""
wifisettings - collection of known wifi networks

URL: https://docs.pycom.io/tutorials/all/wlan/
section: 'Multiple Networks using a Static IP Address'

Specify for each ssid (wifi netwerk):
1. passwrd
2. for STATIC IP: provide values for 'wlan_config'
3. for DYNAMIC IP, such as your home Wifi: remove 'wlan_config' values.

Format known_nets (Python dictionary):
known_nets = {
  'ssid_name': {'pwd': 'passwrd',
                'wlan_config': (ip, subnet_mask, gateway, DNS_server),
                },
     .....
}

2020-03 PP Smart City -semester 2
"""
known_nets = {
    'devices': {'pwd': 'devices2',
                       'wlan_config': ('145.44.186.xxx', '255.255.255.128', '145.44.186.1', '8.8.8.8')
                },
    'SSID-THUISNETWERK': {'pwd': 'WACHTWOORD',
                         'wlan_config': ('STATIC-IP', '255.255.255.0', 'GATEWAY', '8.8.8.8')
                  }
}
