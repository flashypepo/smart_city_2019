"""
lorasettings.py
   contains the credentials for connecting to TTN via LoRa gateway.

TODO: app_eui en app_key van Console TTN provision of device and application
zie workshop LoRa

History
2020-03 PP template for smart-city 2020-02
"""
import binascii

# app_eui = TTN - application EUI (and NOT device EUI)
#   !! Each application can handle only one kind of payload format !!
app_eui = binascii.unhexlify('<zie getdevieeui.py>')

# device application key: zie TTN Console device
app_key = binascii.unhexlify('<zie TTN - console>')
