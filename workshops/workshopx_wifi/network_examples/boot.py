# boot.py -- run on boot-up

# recommended: https://docs.pycom.io/firmwareapi/micropython/micropython/
import micropython
micropython.alloc_emergency_exception_buf(100)

USE_WIFI = False  # connect to Wifi (True) or not (False)
# Voordat je USE_WIFI op 'True' zet, doe eerst de volgende stappen:
# 1. Copieer file 'config/wificonfig_template.json naar file 'config/wificonfig.json'.
# 2. Vul in file 'config/wificonfig.json' het jouw gegeven IP-adres in.
#    De andere gegevens staan al goed voor Wifi netwerk 'devices' op Windesheim (Almere).
# 3. Optioneel: vul in een naam van jouw device.

if USE_WIFI:
    from wifimanager import WifiManager
    try:
        wificonfig_file = 'config/wificonfig.json'
        print('Start to connect to Wifi...({})'.format(wificonfig_file))
        wifi = WifiManager(wificonfig_file)
        ip = wifi.connect()  # connect device to wifi, returns IP
        print('Device is connected to Wifi: {}'.format(wifi.isconnected))
        print('\tIP = {}'.format(ip))
    except OSError as err:
        print('OSError: file not found...{}'.format(err))
    except Exception as ex:
        print('Exception...')
        print(ex)
        pass
