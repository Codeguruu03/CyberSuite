import nmap
import os
import time
from colorama import Fore
from tabulate import tabulate
import pyfiglet as fig
from utils import validate_ip_or_hostname, print_error

def perform_scan(target, scan_type):
    # Create a new instance of the PortScanner class
    try:
        nm = nmap.PortScanner()
    except nmap.PortScannerError:
        print(Fore.RED + "Error: Nmap is not installed or not found in PATH. Please install nmap first." + Fore.RESET)
        return []

    # Scan the target for the specified scan type
    try:
        if scan_type == '1':
            nm.scan(target, arguments='-sS')  # SYN scan
        elif scan_type == '2':
            nm.scan(target, arguments='-sT')  # TCP connect scan
        elif scan_type == '3':
            nm.scan(target, arguments='-sU')  # UDP scan
        elif scan_type == '4':
            nm.scan(target, arguments='-sV')  # Version detection
        elif scan_type == '5':
            nm.scan(target, arguments='-A')   # Aggressive scan
        elif scan_type == '6':
            nm.scan(target, arguments='-sA')  # ACK scan
        elif scan_type == '7':
            nm.scan(target, arguments='-sF')  # FIN scan
        elif scan_type == '8':
            nm.scan(target, arguments='-sN')  # NULL scan
        elif scan_type == '9':
            nm.scan(target, arguments='-sI')  # Idle scan
    except Exception as e:
        print(Fore.RED + f"Error during scan: {e}" + Fore.RESET)
        return []

    # Print scan results
    results = []
    for host in nm.all_hosts():
        row = {'Host': host, 'State': nm[host].state()}
        protocols = nm[host].all_protocols()
        for proto in protocols:
            ports = sorted(nm[host][proto].keys())
            for port in ports:
                service = nm[host][proto][port]['name']
                version = nm[host][proto][port]['version']
                row.update({'Protocol': proto, 'Port': port, 'Service': service, 'Version': version})
                results.append(row.copy())
    return results

def main():
    while True:
        for i in fig.figlet_format('                    ScanGenie    ', font='big', width=200).split('\n\n'):
            print(Fore.LIGHTMAGENTA_EX + i.center(120) + Fore.RESET)
        
        print(Fore.GREEN+ "ScanGenie is a Python tool utilizing Nmap for network scanning. Users input a target IP or hostname and select a scan type (e.g., SYN, TCP, UDP). It provides detailed results including host state, protocols, ports, services, and versions, displayed in a tabular format. It offers user-friendly rerun options." + Fore.RESET)

        target = input( Fore.CYAN + "Enter the target IP address or hostname: " + Fore.RESET)
        
        # Validate IP/hostname
        valid, error_msg = validate_ip_or_hostname(target)
        if not valid:
            print_error(error_msg)
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            continue
        
        print(Fore.LIGHTYELLOW_EX + "Note: Some scan types require root privileges." + Fore.RESET)
        print(Fore.LIGHTYELLOW_EX)
        print("Choose a scan type:")
        print("1. SYN scan")
        print("2. TCP connect scan")
        print("3. UDP scan")
        print("4. Version detection")
        print("5. Aggressive scan")
        print("6. ACK scan")
        print("7. FIN scan")
        print("8. NULL scan")
        print("9. Idle scan")
        print(Fore.RESET)
        print(Fore.YELLOW)
        scan_type = input("Enter the option number: ")

        if scan_type not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            print("Invalid option. Please choose a number between 1 and 9.")
            continue

        print(Fore.RESET)

        print(Fore.LIGHTWHITE_EX)
        results = perform_scan(target, scan_type)
        if results:
            print(tabulate(results, headers="keys"))
        else:
            print(Fore.YELLOW + "No results found or scan failed." + Fore.RESET)
        print(Fore.RESET)

        print(Fore.LIGHTCYAN_EX + "\nScan complete." + Fore.RESET)
        while True:
            choice = input(Fore.LIGHTBLUE_EX + "\nDo you want to rerun this tool? (Y/N): " + Fore.RESET).lower()
            if choice in {'y', 'n'}:
                if choice == 'n':
                    print("Returning to main page...")
                    os.system('cls' if os.name == 'nt' else 'clear')
                    os.system('python main.py')
                    return
                else:
                    break
            else:
                print(Fore.RED + "Invalid choice. Please enter 'y' or 'n'." + Fore.RESET)

if __name__ == "__main__":
    main()
