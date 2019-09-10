# boot.py -- run on boot-up

USE_WIFI = False  # 2019-0910 changed

if USE_WIFI:
    from wifimanager import WifiManager
    try:
        wificonfig_file = 'config/wificonfig_home.json'
        print('Start to connect to Wifi...({})'.format(wificonfig_file))
        wifi = WifiManager(wificonfig_file)
        wifi.connect()  # connect device to wifi
        if wifi.isconnected:
            print('Device connected to Wifi, IP = {}'.format(wifi._wlan.ifconfig()[0]))
    except OSError as err:
        print('OSError: file not found...{}'.format(err))
    except Exception as ex:
        print('Exception...')
        print(ex)
