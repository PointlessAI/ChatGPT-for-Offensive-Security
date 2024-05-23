import requests
from scapy.all import *
import logging

logging.basicConfig(filename='firewall_analysis.log', level=logging.INFO, format='%(asctime)s %(message)s')

def analyze_firewalls(target_url):
    try:
        headers = requests.get(target_url).headers
        logging.info("HTTP Headers: %s", headers)

        possible_wafa = ["X-Squid-Error", "Nel", "X-CDN", "X-Backside-Transport", "X-Sucuri-ID", "Server"]
        waf_detected = any(header for header in possible_wafa if header in headers)
        logging.info("WAF Detection: %s", waf_detected)

        def port_scan(target):
            logging.info("Starting port scan on %s", target)
            open_ports = []
            ans, unans = sr(IP(dst=target)/TCP(sport=RandShort(), dport=[80, 443, 8080], flags="S"), timeout=5)
            for sent, received in ans:
                if received.haslayer(TCP) and received.getlayer(TCP).flags & 0x12:
                    open_ports.append(received.sport)
                    logging.info("Open Port Found: %s", received.sport)
                if received.haslayer(ICMP):
                    icmp_type = received.getlayer(ICMP).type
                    logging.info("ICMP Response Type: %s", icmp_type)
            return open_ports

        target_ip = socket.gethostbyname(target_url.replace("http://", "").replace("https://", "").split('/')[0])
        open_ports = port_scan(target_ip)

        logging.info("Open Ports: %s", open_ports)
    except Exception as e:
        logging.error("An error occurred: %s", e)

analyze_firewalls('http://pointlessai.com')

