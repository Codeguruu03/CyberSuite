from tabulate import tabulate
import os
import math
import pyfiglet as fig
from colorama import Fore

def calculate_password_strength(password):
    length = len(password)
    uppercase_chars = sum(1 for char in password if char.isupper())
    lowercase_chars = sum(1 for char in password if char.islower())
    digits = sum(1 for char in password if char.isdigit())
    special_chars = length - (uppercase_chars + lowercase_chars + digits)
    
    # Calculate password complexity score
    complexity_score = (uppercase_chars > 0) + (lowercase_chars > 0) + (digits > 0) + (special_chars > 0)

    #calculation of the entropy on the basis of the complexity score and length of the password
    entropy = math.log2(complexity_score ** length)

    #strengths of the password on the basis of the entropy
    if entropy < 8:
        strength = "Very Weak"
    elif 8 <= entropy < 14:
        strength =  "Weak"
    elif 14 <= entropy < 21:
        strength =  "Moderate"
    elif 21 <= entropy < 26:
        strength =  "Strong"
    else:
        strength =  "Very Strong"
    
    return strength

def generate_passwords(details):
    passwords = set()
    # Generate passwords based on user details
    for detail in details:
        passwords.add(detail)
        passwords.add(detail[::-1])  # Reverse of detail
        passwords.add(detail.lower())  # Lowercase detail
        passwords.add(detail.upper())  # Uppercase detail
        passwords.add(detail.replace(' ', ''))  # Remove spaces
        passwords.add(''.join(char.swapcase() if i % 2 == 0 else char for i, char in enumerate(detail)))  # Swapcase every other character
        passwords.add(''.join(char + char if i % 2 == 0 else char for i, char in enumerate(detail)))  # Double every other character
        passwords.add(detail + '123')  # Append '123' to the end
        passwords.add(detail[::-1] + '456')  # Reverse detail and append '456' to the end
    
    
    # Add some common passwords
    common_passwords = {'password', '123456', 'qwerty', 'letmein', 'abc123'}
    passwords.update(common_passwords)
    
    return passwords

def main():
    while True:

        for i in fig.figlet_format('                    GuardGenie    ', font='big', width=200).split('\n\n'):
                print(Fore.LIGHTMAGENTA_EX + i.center(120) + Fore.RESET)

        
        print(Fore.GREEN + "The Common User Password Generator (CUPG) is a versatile tool designed to enhance security by creating strong and unique passwords for everyday use. With its intuitive interface and customizable options, CUPG empowers users to fortify their online accounts against unauthorized access, ensuring peace of mind in the digital realm" + Fore.RESET)

        print(Fore.LIGHTGREEN_EX + "You can skip any question by pressing Enter." + Fore.RESET)
        print("")
        
        details = []
        questions = [
            "First name: ",
            "Last name: ",
            "Nickname: ",
            "Birthdate (YYYY-MM-DD): ",
            "Partner's name: ",
            "Partner's nickname: ",
            "Partner's birthdate (YYYY-MM-DD): ",
            "Child's name: ",
            "Child's nickname: ",
            "Child's birthdate (YYYY-MM-DD): ",
            "Pet's name: ",
            "Company name: ",
            "Special words (separated by spaces): ",
            "Key words (separated by spaces): ",
            "Random words (separated by spaces): "
        ]
        
        for question in questions:
            detail = input(Fore.LIGHTBLUE_EX + question + Fore.RESET)
            if detail:
                details.append(detail)
        
        if not details:
            print(Fore.RED + "No details provided. Exiting." + Fore.RESET)
            return
        
        passwords = generate_passwords(details)
        
        password_data = []
        for password in passwords:
            strength = calculate_password_strength(password)
            password_data.append([password, strength])
        
        print(Fore.LIGHTYELLOW_EX + "\nGenerated Passwords:")
        print(tabulate(password_data, headers=['Password', 'Strength']))


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
