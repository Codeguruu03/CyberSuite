import os
import pyfiglet as fig
from colorama import Fore
import requests
from tabulate import tabulate
import time
from utils import validate_url, print_error, print_success, print_warning, print_info, clear_screen, return_to_main

def check_url(url):
    """
    Check if URL is accessible.
    Returns True if status 200, False otherwise.
    """
    try:
        response = requests.get(url, timeout=5)
        return response.status_code == 200, response.status_code
    except requests.exceptions.RequestException:
        return False, None

def brute_force_directories(base_url, wordlist):
    """
    Brute force directories/paths on target URL.
    """
    results = []
    total = len(wordlist)
    
    print(Fore.CYAN + f"Testing {total} paths...\n" + Fore.RESET)
    
    for idx, path in enumerate(wordlist, 1):
        url = base_url.rstrip('/') + '/' + path.strip()
        
        # Progress indicator
        if idx % 10 == 0 or idx == total:
            print(Fore.YELLOW + f"Progress: {idx}/{total} ({int(idx/total*100)}%)" + Fore.RESET, end='\r')
        
        exists, status_code = check_url(url)
        
        if exists or status_code in [301, 302, 403]:  # Include redirects and forbidden
            status_str = ""
            if status_code == 200:
                status_str = Fore.GREEN + f"[200 OK]" + Fore.RESET
            elif status_code == 301:
                status_str = Fore.YELLOW + f"[301 Moved]" + Fore.RESET
            elif status_code == 302:
                status_str = Fore.YELLOW + f"[302 Found]" + Fore.RESET
            elif status_code == 403:
                status_str = Fore.RED + f"[403 Forbidden]" + Fore.RESET
            
            results.append([url, status_str])
            print(Fore.GREEN + f"\n[+] Found: {url} {status_str}" + Fore.RESET)
    
    print("\n")  # Clear progress line
    return results

def main():
    while True:
        for i in fig.figlet_format('                    WebGenie    ', font='big', width=200).split('\n\n'):
            print(Fore.LIGHTMAGENTA_EX + i.center(120) + Fore.RESET)
        
        print(Fore.GREEN + "WebGenie is a web directory and file brute-forcing tool for discovering hidden paths on web servers. Use ONLY on systems you own or have permission to test.".center(120) + Fore.RESET)
        print("")
        
        print(Fore.RED + "⚠️  WARNING: Unauthorized testing is illegal!" + Fore.RESET)
        print("")
        
        # Get target URL
        base_url = input(Fore.LIGHTCYAN_EX + "Enter the base URL (e.g., http://example.com): " + Fore.RESET)
        
        # Validate URL
        valid, error_msg = validate_url(base_url)
        if not valid:
            print_error(error_msg)
            continue
        
        print(Fore.LIGHTYELLOW_EX + "\nChoose wordlist:")
        print("1. Built-in common paths (20 paths)")
        print("2. Built-in extended paths (50 paths)")
        print("3. Custom wordlist file")
        print("4. Back to main menu")
        choice = input("Enter your choice (1/2/3/4): " + Fore.RESET)
        
        wordlist = []
        
        if choice == '1':
            wordlist = [
                "admin", "administrator", "login", "dashboard",
                "wp-admin", "phpmyadmin", "cpanel", "webmail",
                "backup", "backups", "db", "database",
                "config", "install", "setup", "test",
                "temp", "tmp", "uploads", "files"
            ]
        
        elif choice == '2':
            wordlist = [
                "admin", "administrator", "login", "dashboard", "panel",
                "wp-admin", "wp-login", "wordpress", "wp-content",
                "phpmyadmin", "pma", "mysql", "cpanel", "webmail",
                "backup", "backups", "old", "backup.zip", "backup.sql",
                "db", "database", "sql", "mysql", "data",
                "config", "configuration", "settings", "install", "setup",
                "test", "dev", "development", "staging", "beta",
                "temp", "tmp", "temporary", "cache",
                "uploads", "upload", "files", "images", "img",
                "assets", "static", "public", "private",
                "api", "rest", "json", "xml",
                "docs", "documentation", "help", "support",
                "download", "downloads"
            ]
        
        elif choice == '3':
            file_path = input(Fore.LIGHTCYAN_EX + "Enter path to wordlist file: " + Fore.RESET)
            try:
                with open(file_path, 'r') as f:
                    wordlist = [line.strip() for line in f if line.strip()]
                print_success(f"Loaded {len(wordlist)} paths from wordlist")
            except FileNotFoundError:
                print_error(f"File '{file_path}' not found.")
                continue
            except Exception as e:
                print_error(f"Error reading file: {e}")
                continue
        
        elif choice == '4':
            return_to_main()
            return
        
        else:
            print_error("Invalid choice.")
            continue
        
        # Perform brute force
        print(Fore.LIGHTYELLOW_EX + f"\nStarting directory brute force on {base_url}...\n" + Fore.RESET)
        results = brute_force_directories(base_url, wordlist)
        
        if results:
            print(Fore.LIGHTWHITE_EX + f"\n✓ Found {len(results)} accessible path(s):\n" + Fore.RESET)
            print(tabulate(results, headers=['URL', 'Status'], tablefmt='grid'))
        else:
            print_warning("No accessible paths found.")
        
        # Ask to rerun
        while True:
            rerun = input(Fore.LIGHTBLUE_EX + "\nDo you want to scan another URL? (Y/N): " + Fore.RESET).lower()
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
