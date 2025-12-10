import os
import pyfiglet as fig
from colorama import Fore
from tabulate import tabulate
import time

try:
    import pywifi
    PYWIFI_AVAILABLE = True
except ImportError:
    PYWIFI_AVAILABLE = False

from utils import print_error, print_success, print_warning, print_info, clear_screen, return_to_main

def scan_wifi_networks():
    """
    Scan for available WiFi networks.
    Returns list of network dictionaries.
    """
    if not PYWIFI_AVAILABLE:
        print_error("pywifi module is not available. Please install it: pip install pywifi")
        return []
    
    try:
        wifi = pywifi.PyWiFi()
        if len(wifi.interfaces()) == 0:
            print_error("No WiFi adapter found!")
            return []
        
        iface = wifi.interfaces()[0]
        print_info(f"Using WiFi adapter: {iface.name()}")
        
        print(Fore.CYAN + "Scanning for networks..." + Fore.RESET)
        iface.scan()
        time.sleep(3)  # Wait for scan to complete
        
        networks = iface.scan_results()
        
        network_list = []
        for network in networks:
            ssid = network.ssid
            bssid = network.bssid
            signal = network.signal
            
            # Get channel if available
            channel = network.freq if hasattr(network, 'freq') else "N/A"
            
            # Get security type
            try:
                if len(network.akm) > 0:
                    security = str(network.akm[0])
                else:
                    security = "Open"
            except:
                security = "Unknown"
            
            network_list.append({
                'SSID': ssid,
                'BSSID': bssid,
                'Signal': signal,
                'Channel': channel,
                'Security': security
            })
        
        return network_list
    
    except Exception as e:
        print_error(f"Error during WiFi scan: {e}")
        return []

def main():
    while True:
        for i in fig.figlet_format('                    WiFiGenie    ', font='big', width=200).split('\n\n'):
            print(Fore.LIGHTMAGENTA_EX + i.center(120) + Fore.RESET)
        
        print(Fore.GREEN + "WiFiGenie is a WiFi network scanner that displays nearby wireless networks with signal strength, security type, and channel information. Perfect for network analysis and troubleshooting.".center(120) + Fore.RESET)
        print("")
        
        if not PYWIFI_AVAILABLE:
            print_error("pywifi module is not installed!")
            print(Fore.YELLOW + "Install it with: pip install pywifi" + Fore.RESET)
            time.sleep(3)
            return_to_main()
            return
        
        print(Fore.LIGHTYELLOW_EX + "Choose an option:")
        print("1. Scan WiFi networks")
        print("2. Refresh scan")
        print("3. Back to main menu")
        choice = input("Enter your choice (1/2/3): " + Fore.RESET)
        
        if choice in ['1', '2']:
            networks = scan_wifi_networks()
            
            if networks:
                print(Fore.LIGHTWHITE_EX + f"\nFound {len(networks)} network(s):\n" + Fore.RESET)
                
                # Prepare table data
                table_data = []
                for net in networks:
                    # Color code by signal strength
                    signal = net['Signal']
                    if signal > -50:
                        signal_str = Fore.GREEN + str(signal) + " (Excellent)" + Fore.RESET
                    elif signal > -60:
                        signal_str = Fore.LIGHTGREEN_EX + str(signal) + " (Good)" + Fore.RESET
                    elif signal > -70:
                        signal_str = Fore.YELLOW + str(signal) + " (Fair)" + Fore.RESET
                    else:
                        signal_str = Fore.RED + str(signal) + " (Weak)" + Fore.RESET
                    
                    # Color code security
                    security = net['Security']
                    if "Open" in security.upper():
                        security_str = Fore.RED + security + " ⚠️" + Fore.RESET
                    else:
                        security_str = Fore.GREEN + security + Fore.RESET
                    
                    table_data.append([
                        net['SSID'],
                        net['BSSID'],
                        signal_str,
                        net['Channel'],
                        security_str
                    ])
                
                print(tabulate(table_data, headers=['SSID', 'BSSID', 'Signal Strength (dBm)', 'Channel/Freq', 'Security'], tablefmt='grid'))
            else:
                print_warning("No networks found or scan failed.")
        
        elif choice == '3':
            return_to_main()
            return
        
        else:
            print_error("Invalid choice. Please enter 1, 2, or 3.")
            continue
        
        # Ask to rerun
        while True:
            rerun = input(Fore.LIGHTBLUE_EX + "\nDo you want to run another scan? (Y/N): " + Fore.RESET).lower()
            if rerun in {'y', 'n'}:
                if rerun == 'n':
                    return_to_main()
                    return
                else:
                    clear_screen()
                    break
            else:
                print_error("Invalid choice. Please enter 'y' or 'n'.")

if __name__ == "__main__":
    main()
