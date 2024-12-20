from scapy.all import sniff, IP, TCP

# packets = sniff(timeout=10)
# print(packets.show())

response = IP(dst = "google.com")/TCP()
print(response.show())