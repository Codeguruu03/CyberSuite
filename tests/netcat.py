import socket

def netcat(host, port):
    try:
        # Create a socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Connect to the target host and port
        s.connect((host, port))
        
        # Receive data from the server
        data = s.recv(1024)
        
        # Print received data
        print(data.decode())

        # Send data to the server
        s.send(b'Hello from client!\n')

        # Receive data from the server
        data = s.recv(1024)
        
        # Print received data
        print(data.decode())

    except Exception as e:
        print("Error:", e)

    finally:
        # Close the socket
        s.close()

# Example usage
netcat("google.com", 80)
