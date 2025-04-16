from scapy.all import sniff

def packet_callback(packet):
    print(packet.summary())

print("Starting Packet Sniffer...")
sniff(prn=packet_callback, count=10)