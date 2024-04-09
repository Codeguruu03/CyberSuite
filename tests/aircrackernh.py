from tabulate import tabulate

import pywifi

wifi = pywifi.PyWiFi()
iface = wifi.interfaces()[0]
iface.scan()

networks = iface.scan_results()

# Initialize lists to store network information
ssid_list = []
bssid_list = []
signal_strength_list = []
channel_list = []  # Removed from here since it's causing the error
security_list = []

# Extract network information
for network in networks:
    ssid_list.append(network.ssid)
    bssid_list.append(network.bssid)
    signal_strength_list.append(network.signal)
    # Check if 'channel' attribute exists before appending
    if hasattr(network, 'channel'):
        channel_list.append(network.channel)
    else:
        channel_list.append("N/A")  # Or handle it accordingly
    security_list.append(network.akm[0])

# Create tabular representation
table_data = []
for ssid, bssid, signal_strength, channel, security in zip(ssid_list, bssid_list, signal_strength_list, channel_list, security_list):
    table_data.append([ssid, bssid, signal_strength, channel, security])

# Print tabular representation
print(tabulate(table_data, headers=['SSID', 'BSSID', 'Signal Strength', 'Channel', 'Security']))
