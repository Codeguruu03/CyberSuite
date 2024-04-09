
import os
import math
import random
import string
import pyfiglet as fig
from colorama import Fore
from tabulate import tabulate
 
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
    if entropy < 5:
        strength = "Very Weak"
    elif 5 <= entropy < 8:
        strength =  "Weak"
    elif 8 <= entropy < 15:
        strength =  "Moderate"
    elif 15 <= entropy < 18:
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
        passwords.add(detail.replace(' ', '_'))  # Replace spaces with underscores
        passwords.add(''.join(char.swapcase() if i % 2 == 0 else char for i, char in enumerate(detail)))  # Swapcase every other character
        passwords.add(''.join(char + char if i % 2 == 0 else char for i, char in enumerate(detail)))  # Double every other character
        passwords.add(detail + '123')  # Append '123' to the end
        passwords.add(detail[::-1] + '456')  # Reverse detail and append '456' to the end
         # Add detail with random digits appended
        for _ in range(5):  # Generate 5 variations with random digits appended
            random_digits = ''.join(random.choice(string.digits) for _ in range(random.randint(1, 5)))
            passwords.add(detail + random_digits)

        # Add detail with random special characters appended
        special_chars = string.punctuation.replace('_', '').replace('-', '')  # Remove underscore and hyphen
        for _ in range(5):  # Generate 5 variations with random special characters appended
            random_special = ''.join(random.choice(special_chars) for _ in range(random.randint(1, 3)))
            passwords.add(detail + random_special)

        # Add detail with repeated characters
        passwords.add(''.join(char * 2 if random.random() < 0.5 else char for char in detail))

        # Add detail with common substitutions
        substitution_mapping = {'i': '1', 'e': '3', 'a': '@', 'o': '0', 's': '$'}
        substituted_detail = ''.join(substitution_mapping.get(char, char) for char in detail)
        passwords.add(substituted_detail)

        # Add detail with common leetspeak substitutions
        for _ in range(5):
            prefix = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(random.randint(1, 3)))
            suffix = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(random.randint(1, 3)))
            passwords.add(prefix + detail + suffix)

    # Add some common passwords
    common_passwords = {'password', '123456', 'qwerty', 'letmein', 'abc123'}
    passwords.update(common_passwords)
    
    return passwords

def main():
    while True:

        for i in fig.figlet_format('                    GuardGenie    ', font='big', width=200).split('\n\n'):
                print(Fore.LIGHTMAGENTA_EX + i.center(120) + Fore.RESET)

        
        print(Fore.GREEN + "GuardGenie is a password generation tool designed to enhance security by creating strong and unique passwords. It utilizes user-provided details like names, birthdates, and keywords to generate passwords with varying degrees of strength, ensuring robust protection for online accounts." + Fore.RESET)

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
            if strength == "Very Weak":
                password_data.append([password, Fore.RED + strength + Fore.RESET])
            elif strength == "Weak":
                password_data.append([password, Fore.LIGHTRED_EX + strength + Fore.RESET])
            elif strength == "Moderate":
                password_data.append([password, Fore.YELLOW + strength + Fore.RESET])
            elif strength == "Strong":
                password_data.append([password, Fore.GREEN + strength + Fore.RESET])
            else:
                password_data.append([password, Fore.LIGHTGREEN_EX + strength + Fore.RESET])
        
        
        print(Fore.LIGHTYELLOW_EX + "\nGenerated Passwords:")
        print(tabulate(password_data, headers=['Password', 'Strength']))
        print(Fore.RESET)


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
