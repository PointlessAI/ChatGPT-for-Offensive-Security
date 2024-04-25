```python
import sys
import requests

class SessionHijacking:
    """
    Man-in-the-Middle (MitM) Attacks: 
    Man-in-the-Middle attacks involve intercepting communication between two parties without their knowledge.
    Bettercap:
    Bettercap is a powerful network manipulation tool that can be utilized for performing Man-in-the-Middle attacks.
    Description:
    This Python class implements session hijacking using Bettercap tool on the target website http://127.0.0.1:81/vulnerabilities/xss_d/
    """

    def redirect_traffic(self):
        headers = {
            'User-Agent': 'Bettercap/1.0',
        }
        response = s.get('http://127.0.0.1:81/vulnerabilities/xss_d/', headers=headers)
        print(response.text)

    def modify_response(self):
        data = {'username': 'hacker', 'password': 'password123'}
        response = s.post('http://127.0.0.1:81/vulnerabilities/xss_d/', data=data)
        print(response.text)

    def tamper_with_requests(self):
        params = {'id': '1'}
        response = s.get('http://127.0.0.1:81/vulnerabilities/xss_d/', params=params)
        print(response.text)

def main():
    sh = SessionHijacking()
    sh.redirect_traffic()
    sh.modify_response()
    sh.tamper_with_requests()

if __name__ == '__main__':
    with requests.Session() as s:
        main()
```
