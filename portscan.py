import socket

def port_scan(host = "localhost"):
    try:
        # Resolve IP address
        ip_addr = socket.gethostbyname(host)

    except socket.gaierror:
        # Stop the program if it doesn't work
        print("Unable to resolve hostname", host)
        exit()

    # Actual port scan

    print("Scanning IP address", ip_addr)

    try:
        for port in range(1, 1025):

            # Create socket (default: IPV4)
            sock = socket.socket()

            result = sock.connect_ex((ip_addr, port))
            if result == 0:
                print(ip_addr + "/" + str(port) + ": Open")

            sock.close()

    except socket.error:
        print("Could not connect")
        exit()

def main():
    # Port scan in Python
    # Get either a hostname or an IP address
    hostname = input("Hi, what is the host you want to scan?")
    port_scan(hostname)

# Call 
if __name__ == "__main__":
    main()
    if __name__ == "__main__":
