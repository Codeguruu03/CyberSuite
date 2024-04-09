import pyfiglet as fig
from colorama import Fore

def main():
    for i in fig.figlet_format('                    Cyber - Suite    ', font='big', width=200).split('\n\n'):
            print(Fore.LIGHTMAGENTA_EX + i.center(120) + Fore.RESET)
    
    print(Fore.LIGHTBLUE_EX + "Welcome to Cyber-Suite!" + Fore.RESET)
    print(Fore.LIGHTGREEN_EX + "Cyber Suite is a Python application offering Linux tool functionalities within a user-friendly interface. With Cyber Suite, users can access and utilize various cybersecurity tools directly from Python, simplifying the process of security testing, network analysis, and other related tasks, all within one comprehensive suite." + Fore.RESET)
    print(Fore.LIGHTYELLOW_EX + "Please select an option:" + Fore.RESET)
    print(Fore.LIGHTYELLOW_EX + "1. GuardGenie" + Fore.RESET)
    print(Fore.LIGHTYELLOW_EX + "2. StegGenie" + Fore.RESET)
    print(Fore.LIGHTYELLOW_EX + "3. ScanGenie" + Fore.RESET)    
    print(Fore.LIGHTYELLOW_EX + "4. Quit" + Fore.RESET)

if __name__ == "__main__":
    main()