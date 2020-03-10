# This is a demo of the NMAP interface for Python
import nmap

# Create a port scan object and scan the whole subnet
scanner = nmap.PortScanner()
scanner.scan('172.16.43.1/24')

# Loop trough all hosts scanned
for host in scanner.all_hosts():

    print(30*"=")

    # Recover the status
    curr_host = scanner[host]
    status = curr_host["status"]
    print(host, "has status", status["state"])

    print()

    if "tcp" in curr_host.keys():
        # Recover the ports scanned in TCP
        tcp_ports = curr_host["tcp"]


        ports = list(tcp_ports.keys())

        for port in ports:
            port_results = tcp_ports[port]
            print("Port",port,"state:",port_results["state"],"name",port_results["name"])
    





