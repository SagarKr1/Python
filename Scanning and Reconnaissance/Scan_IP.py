import subprocess

def scan_network(network):
    active_hosts = []  # List to store active IPs

    for i in range(1, 255):  # Scan 192.168.31.1 to 192.168.31.254
        ip = f"{network}.{i}"
        print("Scanning Ip Address : ",ip)
        result = subprocess.run(["ping", "-n", "1", "-w", "500", ip], capture_output=True, text=True)

        if "Reply from" in result.stdout:  # Windows response
            active_hosts.append(ip)

    return active_hosts

# Example usage
network_prefix = "192.168.31"  # Extracted from 192.168.31.195/24
active_ips = scan_network(network_prefix)

print("Active IP Addresses:", active_ips)
