import pywifi
from pywifi import const

wifi = pywifi.PyWiFi()

iface = wifi.interfaces()[0]

iface.scan()

networks = iface.scan_results()
for network in networks:
    print("SSID:", network.ssid)
    print("BSSID:", network.bssid)
    print("Signal Strength:", network.signal)
    print("Encryption:", network.akm[0])
    print("------")
