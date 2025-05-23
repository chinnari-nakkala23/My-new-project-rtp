from scapy.all import sniff, ARP

def detect_arp_spoof(packet):
    if packet.haslayer(ARP) and packet[ARP].op == 2:  # ARP Reply
        real_mac = packet[ARP].hwsrc
        print(f"Possible ARP Spoofing: {packet[ARP].psrc} has MAC {real_mac}")

print("Monitoring ARP packets...")
sniff(filter="arp", prn=detect_arp_spoof, store=False)