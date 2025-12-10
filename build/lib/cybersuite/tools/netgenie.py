import os
import socket
import pyfiglet as fig
from colorama import Fore
import time
from utils import print_error, print_success, print_warning, print_info, clear_screen, return_to_main

def netcat_connect(host, port):
    """
    Connect to a host and port (like netcat).
    """
    try:
        # Create socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(10)
        
        print_info(f"Connecting to {host}:{port}...")
        s.connect((host, int(port)))
        print_success(f"Connected to {host}:{port}")
        
        # Receive banner/initial data
        try:
            s.settimeout(2)
            data = s.recv(4096)
            if data:
                print(Fore.LIGHTWHITE_EX + "\n--- Received Data ---" + Fore.RESET)
                print(data.decode('utf-8', errors='ignore'))
                print(Fore.LIGHTWHITE_EX + "--- End Data ---\n" + Fore.RESET)
        except socket.timeout:
            print_warning("No initial data received")
        
        # Interactive mode
        print(Fore.CYAN + "\nEntering interactive mode. Type 'exit' to close connection." + Fore.RESET)
        s.settimeout(None)
        
        while True:
            message = input(Fore.LIGHTGREEN_EX + "> " + Fore.RESET)
            
            if message.lower() == 'exit':
                break
            
            # Send message
            s.send((message + '\n').encode())
            
            # Receive response
            try:
                s.settimeout(5)
                response = s.recv(4096)
                if response:
                    print(response.decode('utf-8', errors='ignore'))
                else:
                    print_warning("No response received")
            except socket.timeout:
                print_warning("Response timeout")
            except Exception as e:
                print_error(f"Error receiving data: {e}")
        
        s.close()
        print_success("Connection closed")
        
    except socket.timeout:
        print_error("Connection timeout")
    except ConnectionRefusedError:
        print_error(f"Connection refused by {host}:{port}")
    except socket.gaierror:
        print_error(f"Could not resolve hostname: {host}")
    except Exception as e:
        print_error(f"Connection error: {e}")

def netcat_listen(port):
    """
    Listen on a port for incoming connections (like netcat -l).
    """
    try:
        # Create socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(('0.0.0.0', int(port)))
        s.listen(1)
        
        print_info(f"Listening on port {port}...")
        print(Fore.YELLOW + "Waiting for incoming connection..." + Fore.RESET)
        
        conn, addr = s.accept()
        print_success(f"Connection received from {addr[0]}:{addr[1]}")
        
        # Interactive mode
        print(Fore.CYAN + "\nEntering interactive mode. Type 'exit' to close connection." + Fore.RESET)
        
        while True:
            # Receive data
            try:
                conn.settimeout(5)
                data = conn.recv(4096)
                if data:
                    print(Fore.LIGHTWHITE_EX + f"\n[{addr[0]}]: " + data.decode('utf-8', errors='ignore') + Fore.RESET)
                else:
                    print_warning("Client disconnected")
                    break
            except socket.timeout:
                pass
            except Exception as e:
                print_error(f"Error receiving data: {e}")
                break
            
            # Send data
            message = input(Fore.LIGHTGREEN_EX + "> " + Fore.RESET)
            
            if message.lower() == 'exit':
                break
            
            try:
                conn.send((message + '\n').encode())
            except Exception as e:
                print_error(f"Error sending data: {e}")
                break
        
        conn.close()
        s.close()
        print_success("Connection closed")
        
    except OSError as e:
        if "address already in use" in str(e).lower():
            print_error(f"Port {port} is already in use")
        else:
            print_error(f"Socket error: {e}")
    except Exception as e:
        print_error(f"Listen error: {e}")

def port_scan(host, start_port, end_port):
    """
    Simple port scanner.
    """
    print_info(f"Scanning ports {start_port}-{end_port} on {host}...")
    print("")
    
    open_ports = []
    
    for port in range(int(start_port), int(end_port) + 1):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)
            result = s.connect_ex((host, port))
            
            if result == 0:
                # Try to get banner
                try:
                    s.send(b'\n')
                    banner = s.recv(1024).decode('utf-8', errors='ignore').strip()
                except:
                    banner = ""
                
                open_ports.append((port, banner))
                print(Fore.GREEN + f"[+] Port {port} - OPEN" + (f" | {banner}" if banner else "") + Fore.RESET)
            
            s.close()
            
            # Progress
            if port % 10 == 0:
                progress = int((port - start_port + 1) / (end_port - start_port + 1) * 100)
                print(Fore.YELLOW + f"Progress: {progress}%" + Fore.RESET, end='\r')
        
        except socket.gaierror:
            print_error(f"Could not resolve hostname: {host}")
            return []
        except socket.error:
            pass
    
    print("\n")
    return open_ports

def main():
    while True:
        for i in fig.figlet_format('                    NetGenie    ', font='big', width=200).split('\n\n'):
            print(Fore.LIGHTMAGENTA_EX + i.center(120) + Fore.RESET)
        
        print(Fore.GREEN + "NetGenie is a network utility tool inspired by netcat. Features include connecting to remote hosts, listening for connections, port scanning, and banner grabbing. Perfect for network debugging and testing.".center(120) + Fore.RESET)
        print("")
        
        print(Fore.LIGHTYELLOW_EX + "Choose an option:")
        print("1. Connect to host (like nc <host> <port>)")
        print("2. Listen on port (like nc -l <port>)")
        print("3. Port scan")
        print("4. Back to main menu")
        choice = input("Enter your choice (1/2/3/4): " + Fore.RESET)
        
        if choice == '1':
            host = input(Fore.LIGHTCYAN_EX + "Enter host to connect to: " + Fore.RESET)
            port = input(Fore.LIGHTCYAN_EX + "Enter port: " + Fore.RESET)
            
            if not host or not port:
                print_error("Host and port are required.")
                continue
            
            try:
                port = int(port)
                if port < 1 or port > 65535:
                    print_error("Port must be between 1 and 65535.")
                    continue
            except ValueError:
                print_error("Port must be a number.")
                continue
            
            netcat_connect(host, port)
        
        elif choice == '2':
            port = input(Fore.LIGHTCYAN_EX + "Enter port to listen on: " + Fore.RESET)
            
            if not port:
                print_error("Port is required.")
                continue
            
            try:
                port = int(port)
                if port < 1 or port > 65535:
                    print_error("Port must be between 1 and 65535.")
                    continue
                if port < 1024:
                    print_warning("Ports below 1024 may require administrator privileges.")
            except ValueError:
                print_error("Port must be a number.")
                continue
            
            netcat_listen(port)
        
        elif choice == '3':
            host = input(Fore.LIGHTCYAN_EX + "Enter host to scan: " + Fore.RESET)
            start_port = input(Fore.LIGHTCYAN_EX + "Enter start port (default 1): " + Fore.RESET) or "1"
            end_port = input(Fore.LIGHTCYAN_EX + "Enter end port (default 1000): " + Fore.RESET) or "1000"
            
            if not host:
                print_error("Host is required.")
                continue
            
            try:
                start_port = int(start_port)
                end_port = int(end_port)
                
                if start_port < 1 or end_port > 65535 or start_port > end_port:
                    print_error("Invalid port range (1-65535, start <= end).")
                    continue
            except ValueError:
                print_error("Ports must be numbers.")
                continue
            
            open_ports = port_scan(host, start_port, end_port)
            
            if open_ports:
                print_success(f"Found {len(open_ports)} open port(s)")
            else:
                print_warning("No open ports found in range")
        
        elif choice == '4':
            return_to_main()
            return
        
        else:
            print_error("Invalid choice. Please enter 1, 2, 3, or 4.")
            continue
        
        # Ask to rerun
        while True:
            rerun = input(Fore.LIGHTBLUE_EX + "\nDo you want to use NetGenie again? (Y/N): " + Fore.RESET).lower()
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
