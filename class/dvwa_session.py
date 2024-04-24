from bs4 import BeautifulSoup

class DVWA_Session:
    base_url = "http://127.0.0.1"
    login_url = base_url + "/login.php"
    sql_injection = f"{base_url}/vulnerabilities/sqli/"#?id=test&Submit=Submit"

    def __init__(self):
        pass

    def get_constants(self):
        return self.login_url

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