import socket

hostname = "example.com"
# hostname = "emazon.com"
# hostname = "techstarter.de"
ip_adress = socket.gethostbyname(hostname)
print(f"the IP-Adress of {hostname} is {ip_adress}")
