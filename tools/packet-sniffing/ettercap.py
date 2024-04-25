```python
# Packet Sniffing using Ettercap
import requests

class SessionHijacking:
  
    def __init__(self):
        self.target_url = "http://127.0.0.1:81/vulnerabilities/xss_d/"

    def packet_sniffing(self):
        with requests.Session() as s:
            response = s.get(self.target_url)
            return response.text

    def arp_spoofing(self):
        with requests.Session() as s:
            response = s.get(self.target_url)
            # Implement ARP Spoofing using Ettercap here
            return response.text

    def dns_spoofing(self):
        with requests.Session() as s:
            response = s.get(self.target_url)
            # Implement DNS Spoofing using Ettercap here
            return response.text

def main():
    session_hijack = SessionHijacking()
    packet_sniffing_result = session_hijack.packet_sniffing()
    print("Packet Sniffing Result: ", packet_sniffing_result)

    arp_spoofing_result = session_hijack.arp_spoofing()
    print("ARP Spoofing Result: ", arp_spoofing_result)

    dns_spoofing_result = session_hijack.dns_spoofing()
    print("DNS Spoofing Result: ", dns_spoofing_result)

if __name__ == "__main__":
    main()
```
