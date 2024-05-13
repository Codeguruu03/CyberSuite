import hashlib
import pyfiglet as fig
from colorama import Fore
import os


def generate_hash(data, hash_type):
    if hash_type == 1:
        hasher = hashlib.md5()
    elif hash_type == 2:
        hasher = hashlib.sha1()
    elif hash_type == 3:
        hasher = hashlib.sha256()
    else:
        raise ValueError("Invalid hash type")

    hasher.update(data.encode('utf-8'))
    return hasher.hexdigest()

def hash_file(file_path, hash_type):
    try:
        with open(file_path, 'rb') as file:
            data = file.read()
            print(Fore.LIGHTCYAN_EX + "Hashing The file ......")

    except FileNotFoundError:
        print("File not found.")
        return
    
    if hash_type == 1:
        hasher = hashlib.md5()
    elif hash_type == 2:
        hasher = hashlib.sha1()
    elif hash_type == 3:
        hasher = hashlib.sha256()
    else:
        raise ValueError("Invalid hash type")

    hasher.update(data)
    hash_value = hasher.hexdigest()

    file_name, file_extension = os.path.splitext(file_path)
    hashed_file_path = f"{file_name}_hash{file_extension}"

    with open(hashed_file_path, 'w') as hashed_file:
        hashed_file.write(hash_value)
    

    return hashed_file_path


def main():
    for i in fig.figlet_format('                    HashGenie    ', font='big', width=200).split('\n\n'):
        print(Fore.LIGHTMAGENTA_EX + i.center(120) + Fore.RESET)

    print(Fore.LIGHTBLUE_EX + "HashGenie is a Python tool that generates hash values for input data using different hash algorithms. Users can input data and select a hash algorithm (e.g., MD5, SHA-1, SHA-256) to generate the corresponding hash value. HashGenie provides secure and efficient hashing functionalities for data integrity verification and password storage." + Fore.RESET)

    print(Fore.CYAN + "Choose an option:")
    print("1. Hash a message")
    print("2. Hash a file (Upcoming feature)")
    option = input("Enter your choice (1/2): ").strip()

    if option == '1':
        data = input("Enter the message to hash: ")
        print(Fore.LIGHTYELLOW_EX + "Choose a hash algorithm:")
        print("1. MD5")
        print("2. SHA-1")
        print("3. SHA-256")
        hash_type = input("Enter your choice (1/2/3): "+ Fore.RESET).strip()

        if hash_type not in {'1', '2', '3'}:
            print("Invalid hash algorithm choice.")
            return

        hash_value = generate_hash(data, int(hash_type))
        print(Fore.LIGHTGREEN_EX + f"Hash value: {hash_value}" + Fore.RESET)

    elif option == '2':
        file_path = input("Enter the path to the file: ")
        print(Fore.LIGHTYELLOW_EX + "Choose a hash algorithm:")
        print("1. MD5")
        print("2. SHA-1")
        print("3. SHA-256")
        hash_type = input("Enter your choice (1/2/3): "+ Fore.RESET).strip()

        if hash_type not in {'1', '2', '3'}:
            print("Invalid hash algorithm choice.")
            return

        hashed_file_path = hash_file(file_path, int(hash_type))
        if hashed_file_path:
            print(Fore.LIGHTCYAN_EX + f"Hashed file saved successfully: {hashed_file_path}" + Fore.RESET )

    else:
        print("Invalid option.")
        return

    while True:
        choice = input(Fore.LIGHTBLUE_EX + "\nDo you want to rerun this tool? (Y/N): " + Fore.RESET).lower()
        if choice in {'y', 'n'}:
            if choice == 'n':
                print("Returning to main page...")
                os.system('cls' if os.name == 'nt' else 'clear')
                os.system('python main.py')
                return
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                main()
        else:
            print(Fore.RED + "Invalid choice. Please enter 'y' or 'n'." + Fore.RESET)


if __name__ == "__main__":
    main()
