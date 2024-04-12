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
    print(Fore.LIGHTYELLOW_EX + "Please select an option:" + Fore.RESET)
    print(Fore.LIGHTYELLOW_EX + "1. GuardGenie" + Fore.RESET)
    print(Fore.LIGHTYELLOW_EX + "2. StegGenie" + Fore.RESET)
    print(Fore.LIGHTYELLOW_EX + "3. ScanGenie" + Fore.RESET)
    print(Fore.LIGHTYELLOW_EX + "4. HashGenie" + Fore.RESET)    
    print(Fore.LIGHTYELLOW_EX + "5. Quit" + Fore.RESET)

    choice = input(Fore.LIGHTCYAN_EX + "Enter your choice (1/2/3/4): " + Fore.RESET)
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
        print(Fore.LIGHTRED_EX + "Exiting...")
        print("Thank you for using Cyber-Suite! \U0001F91D")
        print("Developed by Naman Goyal")
        print(Fore.RESET)
        time.sleep(3)
        sys.exit()
         

if __name__ == "__main__":
    main()