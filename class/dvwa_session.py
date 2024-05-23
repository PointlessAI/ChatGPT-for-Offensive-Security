from bs4 import BeautifulSoup

class DVWA_Session:
    base_url = "http://127.0.0.1"
    login_url = base_url + "/login.php"
    sql_injection = f"{base_url}/vulnerabilities/sqli/"

    proxies = {"http": "http://127.0.0.1:"}
    headers = {
        "Host": "127.0.0.1",
        "Cache-Control": "max-age=0",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate",
        "Connection": "keep-alive"
    }

    def __init__(self):
        pass

    def get_constants(self):
        return self.login_url

    def get_dvwa(self, s, page_url):
        # Fetch the DVWA page within the established session.
        response = s.get(page_url, proxies=self.proxies, headers=self.headers)
        return response

    def post_dvwa(self, s, url, payload):
        # Post to DVWA
        response = s.post(url, data={'input': payload}, proxies=self.proxies, headers=self.headers)
        return response

    def get_csrf_token_and_cookie(self, s, url):
        # Retrieve CSRF token and cookie required for DVWA login.
        response = s.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        user_token = soup.find("input", {"name": "user_token"})
        if user_token:
            return user_token.get("value"), response.cookies

    def login_to_dvwa(self, s, url, username, password, user_token):
        # Log in to the DVWA.
        data = {
            "username": username,
            "password": password,
            "user_token": user_token,
            "Login": "Login"
        }
        response = s.post(url, data=data)
        return response
    
    def setup_database(self, s, setup_url, user_token, cookies):
        # Set up database
        data = {
            'create_db': 'Create / Reset Database',
            'user_token': user_token
        }
        headers = {'Referer': setup_url}
        response = s.post(setup_url, data=data, cookies=cookies, headers=headers)
        return response