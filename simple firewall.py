import os

blocked_ips = ["192.168.1.100", "10.0.0.5"]

for ip in blocked_ips:
    os.system(f"sudo iptables -A INPUT -s {ip} -j DROP")
    print(f"Blocked IP: {ip}")