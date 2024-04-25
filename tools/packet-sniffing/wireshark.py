import requests
    
class SessionHijack:
    # Packet Sniffing: Capturing and analyzing data packets being sent over a network
    # Wireshark: A popular network protocol analyzer tool for packet sniffing
    
    def __init__(self):
        self.target_url = "http://127.0.0.1:81/vulnerabilities/xss_d/"

    def method_1(self):
        response = s.get(self.target_url)
        print("Method 1: Successfully hijacked session")

    def method_2(self):
        payload = {'user': 'admin', 'password': 'hijack123'}
        response = s.post(self.target_url, data=payload)
        print("Method 2: Successfully hijacked session")

    def method_3(self):
        response = s.get(self.target_url, headers={'Cookie': 'session=hacked123'})
        print("Method 3: Successfully hijacked session")

def main():
    with requests.Session() as s:
        hijacker = SessionHijack()
        hijacker.method_1()
        hijacker.method_2()
        hijacker.method_3()

if __name__ == "__main__":
    main()
