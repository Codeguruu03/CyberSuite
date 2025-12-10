import os
import hashlib
import pyfiglet as fig
from colorama import Fore
import time
from tabulate import tabulate
from utils import validate_file_path, print_error, print_success, print_warning, print_info, clear_screen, return_to_main

def crack_hash(hash_to_crack, hash_type, dictionary):
    """
    Attempt to crack a hash using a dictionary.
    Returns (cracked_password, attempts) or (None, attempts).
    """
    print(Fore.CYAN + f"Attempting to crack {hash_type} hash..." + Fore.RESET)
    print(Fore.YELLOW + f"Dictionary size: {len(dictionary)} passwords\n" + Fore.RESET)
    
    start_time = time.time()
    
    for idx, password in enumerate(dictionary, 1):
        # Progress indicator
        if idx % 1000 == 0:
            elapsed = time.time() - start_time
            rate = idx / elapsed if elapsed > 0 else 0
            print(Fore.YELLOW + f"Progress: {idx}/{len(dictionary)} | Rate: {rate:.0f} hashes/sec" + Fore.RESET, end='\r')
        
        # Hash the password based on type
        if hash_type.lower() == 'md5':
            hashed = hashlib.md5(password.encode()).hexdigest()
        elif hash_type.lower() == 'sha1':
            hashed = hashlib.sha1(password.encode()).hexdigest()
        elif hash_type.lower() == 'sha256':
            hashed = hashlib.sha256(password.encode()).hexdigest()
        elif hash_type.lower() == 'sha512':
            hashed = hashlib.sha512(password.encode()).hexdigest()
        elif hash_type.lower() == 'blake2b':
            hashed = hashlib.blake2b(password.encode()).hexdigest()
        else:
            return None, idx
        
        if hashed == hash_to_crack.lower():
            elapsed = time.time() - start_time
            print("\n")
            return password, idx, elapsed
    
    elapsed = time.time() - start_time
    print("\n")
    return None, len(dictionary), elapsed

def generate_common_passwords():
    """
    Generate a list of common passwords.
    """
    common = [
        "password", "123456", "12345678", "1234", "qwerty",
        "12345", "dragon", "pussy", "baseball", "football",
        "letmein", "monkey", "696969", "abc123", "mustang",
        "michael", "shadow", "master", "jennifer", "111111",
        "2000", "jordan", "superman", "harley", "1234567",
        "fuckme", "hunter", "fuckyou", "trustno1", "ranger",
        "buster", "thomas", "tigger", "robert", "soccer",
        "fuck", "batman", "test", "pass", "killer",
        "hockey", "george", "charlie", "andrew", "michelle",
        "jessica", "pepper", "daniel", "1111", "admin",
        "administrator", "root", "toor", "pass123", "password123",
        "welcome", "Welcome123", "passw0rd", "p@ssw0rd", "P@ssw0rd"
    ]
    
    # Add common variations
    variations = []
    for pwd in common[:20]:  # Top 20
        variations.append(pwd + "123")
        variations.append(pwd + "!")
        variations.append(pwd.capitalize())
        variations.append(pwd.upper())
    
    return common + variations

def main():
    while True:
        for i in fig.figlet_format('                    CrackGenie    ', font='big', width=200).split('\n\n'):
            print(Fore.LIGHTMAGENTA_EX + i.center(120) + Fore.RESET)
        
        print(Fore.GREEN + "CrackGenie is a password hash cracking tool using dictionary attacks. Supports MD5, SHA-1, and SHA-256 hashes. Use ONLY for authorized security testing and password recovery.".center(120) + Fore.RESET)
        print("")
        
        print(Fore.RED + "⚠️  WARNING: Only crack hashes you have permission to test!" + Fore.RESET)
        print("")
        
        # Get hash to crack
        hash_input = input(Fore.LIGHTCYAN_EX + "Enter the hash to crack: " + Fore.RESET).strip()
        
        if not hash_input:
            print_error("Hash cannot be empty.")
            continue
        
        # Determine hash type by length
        hash_len = len(hash_input)
        if hash_len == 32:
            detected_type = "MD5"
            print_info(f"Detected hash type: MD5 (32 characters)")
        elif hash_len == 40:
            detected_type = "SHA1"
            print_info(f"Detected hash type: SHA-1 (40 characters)")
        elif hash_len == 64:
            detected_type = "SHA256"
            print_info(f"Detected hash type: SHA-256 (64 characters)")
        elif hash_len == 128:
            print_warning(f"Hash length is 128 characters - could be SHA-512 or BLAKE2b")
            print(Fore.YELLOW + "Please specify hash type:" + Fore.RESET)
            print("1. SHA-512")
            print("2. BLAKE2b")
            type_choice = input("Enter choice (1/2): ")
            if type_choice == '1':
                detected_type = "SHA512"
            elif type_choice == '2':
                detected_type = "BLAKE2B"
            else:
                print_error("Invalid choice.")
                continue
        else:
            print_warning(f"Unknown hash length ({hash_len} characters)")
            print(Fore.YELLOW + "Please specify hash type manually." + Fore.RESET)
            print("1. MD5")
            print("2. SHA-1")
            print("3. SHA-256")
            print("4. SHA-512")
            print("5. BLAKE2b")
            type_choice = input("Enter choice (1/2/3/4/5): ")
            if type_choice == '1':
                detected_type = "MD5"
            elif type_choice == '2':
                detected_type = "SHA1"
            elif type_choice == '3':
                detected_type = "SHA256"
            elif type_choice == '4':
                detected_type = "SHA512"
            elif type_choice == '5':
                detected_type = "BLAKE2B"
            else:
                print_error("Invalid choice.")
                continue
        
        print(Fore.LIGHTYELLOW_EX + "\nChoose dictionary:")
        print("1. Built-in common passwords (~200 passwords)")
        print("2. Custom wordlist file")
        print("3. Back to main menu")
        choice = input("Enter your choice (1/2/3): " + Fore.RESET)
        
        dictionary = []
        
        if choice == '1':
            dictionary = generate_common_passwords()
            print_success(f"Loaded {len(dictionary)} common passwords")
        
        elif choice == '2':
            file_path = input(Fore.LIGHTCYAN_EX + "Enter path to wordlist file: " + Fore.RESET)
            valid, error_msg = validate_file_path(file_path)
            if not valid:
                print_error(error_msg)
                continue
            
            try:
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    dictionary = [line.strip() for line in f if line.strip()]
                print_success(f"Loaded {len(dictionary)} passwords from wordlist")
            except Exception as e:
                print_error(f"Error reading file: {e}")
                continue
        
        elif choice == '3':
            return_to_main()
            return
        
        else:
            print_error("Invalid choice.")
            continue
        
        # Perform cracking
        print(Fore.LIGHTYELLOW_EX + f"\nStarting crack attempt...\n" + Fore.RESET)
        
        result, attempts, elapsed = crack_hash(hash_input, detected_type, dictionary)
        
        if result:
            print(Fore.GREEN + "╔═══════════════════════════════════════╗" + Fore.RESET)
            print(Fore.GREEN + "║     🎉 PASSWORD CRACKED! 🎉         ║" + Fore.RESET)
            print(Fore.GREEN + "╚═══════════════════════════════════════╝" + Fore.RESET)
            print(Fore.LIGHTGREEN_EX + f"\nPassword: {result}" + Fore.RESET)
            print(Fore.CYAN + f"Attempts: {attempts:,}" + Fore.RESET)
            print(Fore.CYAN + f"Time elapsed: {elapsed:.2f} seconds" + Fore.RESET)
            print(Fore.CYAN + f"Rate: {attempts/elapsed:.0f} hashes/second\n" + Fore.RESET)
        else:
            print(Fore.RED + "✗ Password not found in dictionary" + Fore.RESET)
            print(Fore.CYAN + f"Attempts: {attempts:,}" + Fore.RESET)
            print(Fore.CYAN + f"Time elapsed: {elapsed:.2f} seconds\n" + Fore.RESET)
            print_warning("Try a larger dictionary or different wordlist.")
        
        # Ask to rerun
        while True:
            rerun = input(Fore.LIGHTBLUE_EX + "\nDo you want to crack another hash? (Y/N): " + Fore.RESET).lower()
            if rerun in {'y', 'n'}:
                if rerun == 'n':
                    return_to_main()
                    return
                else:
                    clear_screen()
                    break
            else:
                print_error("Invalid choice. Please enter 'y' or 'n'.")

if __name__ == "__main__":
    main()
