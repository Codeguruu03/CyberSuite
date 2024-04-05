import pyfiglet as fig
from colorama import Fore

def main():
    for i in fig.figlet_format('                    Cyber - Suite    ', font='big', width=200).split('\n\n'):
            print(Fore.LIGHTMAGENTA_EX + i.center(120) + Fore.RESET)
    
    print(Fore.LIGHTBLUE_EX + "Welcome to Cyber-Suite!" + Fore.RESET)

    print(Fore.LIGHTYELLOW_EX + "Please select an option:" + Fore.RESET)
    print(Fore.LIGHTYELLOW_EX + "1. GuardGenie" + Fore.RESET)
    print(Fore.LIGHTYELLOW_EX + "2. Steganografy" + Fore.RESET)
    print(Fore.LIGHTYELLOW_EX + "3. Quit" + Fore.RESET)

if __name__ == "__main__":
    main()