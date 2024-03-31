import nmap

# Create a new instance of the PortScanner class
nm = nmap.PortScanner()

# Scan localhost for common ports
nm.scan('localhost', '1-1024')

# Iterate over each scanned host
for host in nm.all_hosts():
    print('----------------------------------------------------')
    print('Host : %s (%s)' % (host, nm[host].hostname()))
    print('State : %s' % nm[host].state())

    # Iterate over each scanned port
    for proto in nm[host].all_protocols():
        print('----------')
        print('Protocol : %s' % proto)

        # Get a list of all ports for the current protocol
        ports = nm[host][proto].keys()
        # Sort the ports numerically
        sorted_ports = sorted(ports)

        # Iterate over each port and its state
        for port in sorted_ports:
            print('Port : %s\tState : %s' % (port, nm[host][proto][port]['state']))
