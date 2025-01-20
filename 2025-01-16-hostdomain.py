# import socket

# hostname = "example.com"
# ip_address = socket.gethostbyname(hostname)
# print(f"Die IP-Adresse von {hostname} ist {ip_address}")

import os
import platform


# def ping(host):
### param = "-n" if platform.system().lower() == "windows" else "-c"
# command = f"ping {param} 4 {host}"
# return os.system(command)


# host = "google.com"
# ost = input("enter a domain")
# ping(host)

import ipaddress

network = ipaddress.ip_network("192.168.10.0/24")
print(f"Netzwerk: {network}")
print(f"Erste IP: {network[0]}")
print(f"Letzte IP: {network[-1]}")
print(f"Anzahl nutzbarer Hosts: {network.num_addresses - 2}")
print(f"the range is: {network.num_addresses - [0]}-{network.num_addresses - [-2]}")
