import pyfiglet as fig
from colorama import Fore

def main():
    for i in fig.figlet_format('                    Cyber - Suite    ', font='big', width=200).split('\n\n'):
            print(Fore.LIGHTMAGENTA_EX + i.center(120) + Fore.RESET)

if __name__ == "__main__":
    main()