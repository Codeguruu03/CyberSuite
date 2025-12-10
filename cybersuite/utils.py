import re
import os
import socket
import json
import logging
from datetime import datetime
from colorama import Fore

def validate_ip(ip_address):
    """
    Validate IP address format.
    Returns True if valid, False otherwise.
    """
    # IPv4 pattern
    ipv4_pattern = r'^(\d{1,3}\.){3}\d{1,3}$'
    
    if re.match(ipv4_pattern, ip_address):
        # Check if each octet is valid (0-255)
        octets = ip_address.split('.')
        for octet in octets:
            if int(octet) > 255:
                return False
        return True
    return False

def validate_hostname(hostname):
    """
    Validate hostname/domain format.
    Returns True if valid, False otherwise.
    """
    try:
        socket.gethostbyname(hostname)
        return True
    except socket.gaierror:
        return False

def validate_ip_or_hostname(target):
    """
    Validate if input is either a valid IP address or hostname.
    Returns (True, "") if valid, (False, error_message) if invalid.
    """
    if not target or not target.strip():
        return False, "Target cannot be empty."
    
    target = target.strip()
    
    # Try IP validation first
    if validate_ip(target):
        return True, ""
    
    # Try hostname validation
    if validate_hostname(target):
        return True, ""
    
    return False, f"'{target}' is not a valid IP address or hostname."

def validate_file_path(file_path, must_exist=True):
    """
    Validate file path.
    Returns (True, "") if valid, (False, error_message) if invalid.
    """
    if not file_path or not file_path.strip():
        return False, "File path cannot be empty."
    
    file_path = file_path.strip()
    
    if must_exist and not os.path.exists(file_path):
        return False, f"File '{file_path}' does not exist."
    
    if must_exist and not os.path.isfile(file_path):
        return False, f"'{file_path}' is not a valid file."
    
    return True, ""

def validate_image_file(file_path):
    """
    Validate image file path and extension.
    Returns (True, "") if valid, (False, error_message) if invalid.
    """
    valid, error = validate_file_path(file_path, must_exist=True)
    if not valid:
        return False, error
    
    # Check image extensions
    valid_extensions = ['.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff']
    _, ext = os.path.splitext(file_path.lower())
    
    if ext not in valid_extensions:
        return False, f"File must be an image ({', '.join(valid_extensions)}). Got: {ext}"
    
    return True, ""

def validate_url(url):
    """
    Validate URL format.
    Returns (True, "") if valid, (False, error_message) if invalid.
    """
    if not url or not url.strip():
        return False, "URL cannot be empty."
    
    url = url.strip()
    
    # Basic URL pattern
    url_pattern = r'^https?://.+'
    
    if not re.match(url_pattern, url):
        return False, "URL must start with http:// or https://"
    
    return True, ""

def print_error(message):
    """Print error message in red."""
    print(Fore.RED + f"❌ {message}" + Fore.RESET)

def print_success(message):
    """Print success message in green."""
    print(Fore.GREEN + f"✓ {message}" + Fore.RESET)

def print_warning(message):
    """Print warning message in yellow."""
    print(Fore.YELLOW + f"⚠️  {message}" + Fore.RESET)

def print_info(message):
    """Print info message in cyan."""
    print(Fore.CYAN + f"ℹ️  {message}" + Fore.RESET)

def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def return_to_main():
    """Return to main menu."""
    print("Returning to main page...")
    clear_screen()
    os.system('python main.py')

def export_results(data, filename_prefix, format='txt'):
    """
    Export results to a file.
    Returns (True, filepath) on success, (False, error_message) on failure.
    """
    try:
        # Create results directory if it doesn't exist
        results_dir = 'results'
        if not os.path.exists(results_dir):
            os.makedirs(results_dir)
        
        # Generate filename with timestamp
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f"{filename_prefix}_{timestamp}.{format}"
        filepath = os.path.join(results_dir, filename)
        
        # Write data based on format
        if format == 'txt':
            with open(filepath, 'w', encoding='utf-8') as f:
                if isinstance(data, str):
                    f.write(data)
                elif isinstance(data, list):
                    for item in data:
                        f.write(str(item) + '\n')
                else:
                    f.write(str(data))
        
        elif format == 'json':
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2)
        
        else:
            return False, f"Unsupported format: {format}"
        
        return True, filepath
    
    except Exception as e:
        return False, str(e)

def setup_logging(tool_name):
    """
    Setup logging for a tool.
    Returns logger object.
    """
    # Create logs directory if it doesn't exist
    logs_dir = 'logs'
    if not os.path.exists(logs_dir):
        os.makedirs(logs_dir)
    
    # Setup logger
    logger = logging.getLogger(tool_name)
    logger.setLevel(logging.DEBUG)
    
    # Create file handler
    timestamp = datetime.now().strftime('%Y%m%d')
    log_file = os.path.join(logs_dir, f"{tool_name}_{timestamp}.log")
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.DEBUG)
    
    # Create formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    
    # Add handler to logger
    if not logger.handlers:
        logger.addHandler(file_handler)
    
    return logger
