#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
CyberSuite Command Line Interface

Main entry point for the cybersuite command.
"""

import pyfiglet as fig
from colorama import Fore, init
import os
import sys

# Initialize colorama for Windows compatibility
init(autoreset=True)

def show_banner():
    """Display CyberSuite banner."""
    for i in fig.figlet_format('                    CyberSuite    ', font='big', width=200).split('\n\n'):
        print(Fore.LIGHTMAGENTA_EX + i.center(120))

def show_menu():
    """Display main menu."""
    print(Fore.LIGHTBLUE_EX + "Welcome to Cyber-Suite!  \U0001F64F")
    print(Fore.LIGHTGREEN_EX + "Cyber Suite is a Python application offering Linux tool functionalities within a user-friendly interface. With Cyber Suite, users can access and utilize various cybersecurity tools directly from Python, simplifying the process of security testing, network analysis, and other related tasks, all within one comprehensive suite.")
    print(Fore.LIGHTYELLOW_EX + "\nPlease select an option:")
    print(Fore.LIGHTYELLOW_EX + "1. GuardGenie - Password Generator & Analyzer")
    print(Fore.LIGHTYELLOW_EX + "2. StegGenie - Steganography Tool")
    print(Fore.LIGHTYELLOW_EX + "3. ScanGenie - Network Scanner (Nmap)")
    print(Fore.LIGHTYELLOW_EX + "4. HashGenie - Hash Generator")    
    print(Fore.LIGHTCYAN_EX + "5. SQLGenie - SQL Injection Tester")
    print(Fore.LIGHTCYAN_EX + "6. WiFiGenie - WiFi Network Scanner")
    print(Fore.LIGHTCYAN_EX + "7. WebGenie - Web Directory Scanner")
    print(Fore.LIGHTCYAN_EX + "8. CrackGenie - Password Hash Cracker")
    print(Fore.LIGHTCYAN_EX + "9. NetGenie - Network Utility (Netcat)")
    print(Fore.LIGHTRED_EX + "10. Quit")

def run_tool(tool_name):
    """Run a specific tool by importing and executing its main function."""
    try:
        if tool_name == 'guardgenie':
            from cybersuite.tools.guardgenie import main
        elif tool_name == 'steggenie':
            from cybersuite.tools.steggenie import main
        elif tool_name == 'scangenie':
            from cybersuite.tools.scangenie import main
        elif tool_name == 'hashgenie':
            from cybersuite.tools.hashgenie import main
        elif tool_name == 'sqlgenie':
            from cybersuite.tools.sqlgenie import main
        elif tool_name == 'wifigenie':
            from cybersuite.tools.wifigenie import main
        elif tool_name == 'webgenie':
            from cybersuite.tools.webgenie import main
        elif tool_name == 'crackgenie':
            from cybersuite.tools.crackgenie import main
        elif tool_name == 'netgenie':
            from cybersuite.tools.netgenie import main
        else:
            print(Fore.RED + f"Unknown tool: {tool_name}")
            return
        
        # Clear screen and run the tool
        os.system('cls' if os.name == 'nt' else 'clear')
        main()
    except ImportError as e:
        print(Fore.RED + f"Error importing tool '{tool_name}': {e}")
    except Exception as e:
        print(Fore.RED + f"Error running tool '{tool_name}': {e}")

def main():
    """Main entry point for CyberSuite CLI."""
    import time
    
    while True:
        show_banner()
        show_menu()
        
        choice = input(Fore.LIGHTCYAN_EX + "\nEnter your choice (1-10): " + Fore.RESET)
        
        if choice == '1':
            run_tool('guardgenie')
        elif choice == '2':
            run_tool('steggenie')
        elif choice == '3':
            run_tool('scangenie')
        elif choice == '4':
            run_tool('hashgenie')
        elif choice == '5':
            run_tool('sqlgenie')
        elif choice == '6':
            run_tool('wifigenie')
        elif choice == '7':
            run_tool('webgenie')
        elif choice == '8':
            run_tool('crackgenie')
        elif choice == '9':
            run_tool('netgenie')
        elif choice == '10':
            print(Fore.LIGHTRED_EX + "Exiting...")
            print("Thank you for using Cyber-Suite! \U0001F91D")
            print("Developed by Naman Goyal")
            time.sleep(2)
            sys.exit(0)
        else:
            print(Fore.RED + "Invalid choice. Please enter a number between 1 and 10.")
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    main()
