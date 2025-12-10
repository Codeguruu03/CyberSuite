import pyfiglet as fig
from colorama import Fore
import os
import sys
import time

def main():
    for i in fig.figlet_format('                    CyberSuite    ', font='big', width=200).split('\n\n'):
            print(Fore.LIGHTMAGENTA_EX + i.center(120) + Fore.RESET)
    
    print(Fore.LIGHTBLUE_EX + "Welcome to Cyber-Suite!  \U0001F64F" + Fore.RESET)
    print(Fore.LIGHTGREEN_EX + "Cyber Suite is a Python application offering Linux tool functionalities within a user-friendly interface. With Cyber Suite, users can access and utilize various cybersecurity tools directly from Python, simplifying the process of security testing, network analysis, and other related tasks, all within one comprehensive suite." + Fore.RESET)
    print(Fore.LIGHTYELLOW_EX + "\nPlease select an option:" + Fore.RESET)
    print(Fore.LIGHTYELLOW_EX + "1. GuardGenie - Password Generator & Analyzer" + Fore.RESET)
    print(Fore.LIGHTYELLOW_EX + "2. StegGenie - Steganography Tool" + Fore.RESET)
    print(Fore.LIGHTYELLOW_EX + "3. ScanGenie - Network Scanner (Nmap)" + Fore.RESET)
    print(Fore.LIGHTYELLOW_EX + "4. HashGenie - Hash Generator" + Fore.RESET)    
    print(Fore.LIGHTCYAN_EX + "5. SQLGenie - SQL Injection Tester" + Fore.RESET)
    print(Fore.LIGHTCYAN_EX + "6. WiFiGenie - WiFi Network Scanner" + Fore.RESET)
    print(Fore.LIGHTCYAN_EX + "7. WebGenie - Web Directory Scanner" + Fore.RESET)
    print(Fore.LIGHTCYAN_EX + "8. CrackGenie - Password Hash Cracker" + Fore.RESET)
    print(Fore.LIGHTCYAN_EX + "9. NetGenie - Network Utility (Netcat)" + Fore.RESET)
    print(Fore.LIGHTRED_EX + "10. Quit" + Fore.RESET)

    choice = input(Fore.LIGHTCYAN_EX + "\nEnter your choice (1-10): " + Fore.RESET)
    
    if choice == '1':
        os.system('cls' if os.name == 'nt' else 'clear')
        os.system('python GuardGenie.py')
    elif choice == '2':
        os.system('cls' if os.name == 'nt' else 'clear')
        os.system('python StegGenie.py')
    elif choice == '3':
        os.system('cls' if os.name == 'nt' else 'clear')
        os.system('python ScanGenie.py')
    elif choice == '4':
        os.system('cls' if os.name == 'nt' else 'clear')
        os.system('python HashGenie.py')
    elif choice == '5':
        os.system('cls' if os.name == 'nt' else 'clear')
        os.system('python SQLGenie.py')
    elif choice == '6':
        os.system('cls' if os.name == 'nt' else 'clear')
        os.system('python WiFiGenie.py')
    elif choice == '7':
        os.system('cls' if os.name == 'nt' else 'clear')
        os.system('python WebGenie.py')
    elif choice == '8':
        os.system('cls' if os.name == 'nt' else 'clear')
        os.system('python CrackGenie.py')
    elif choice == '9':
        os.system('cls' if os.name == 'nt' else 'clear')
        os.system('python NetGenie.py')
    elif choice == '10':
        print(Fore.LIGHTRED_EX + "Exiting...")
        print("Thank you for using Cyber-Suite! \U0001F91D")
        print("Developed by Naman Goyal")
        print(Fore.RESET)
        time.sleep(3)
        sys.exit()
    else:
        print(Fore.RED + "Invalid choice. Please enter a number between 1 and 10." + Fore.RESET)
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
         

if __name__ == "__main__":
    main()