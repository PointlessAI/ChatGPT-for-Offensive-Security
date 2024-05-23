import requests
from bs4 import BeautifulSoup

def check_2fa_for_admin_access(url):
    try:
        session = requests.Session()
        response = session.get(url)
        if response.status_code != 200:
            raise Exception(f"Failed to reach {url}")
        soup = BeautifulSoup(response.text, 'html.parser')
        login_form = soup.find("form")
        if not login_form:
            raise Exception("Login form not found")
        username_field = login_form.find("input", {"name": "username"})
        password_field = login_form.find("input", {"name": "password"})
        submit_button = login_form.find("button", {"type": "submit"})
        if not (username_field and password_field and submit_button):
            raise Exception("Necessary login fields not found in the form")
        login_payload = {
            username_field["name"]: "admin",
            password_field["name"]: "password"
        }
        action = login_form.get("action", url)
        post_url = action if 'http' in action else f"{url}/{action}"
        post_response = session.post(post_url, data=login_payload)
        if post_response.status_code == 200:
            subsequent_page = BeautifulSoup(post_response.text, 'html.parser')
            possible_2fa_fields = ["otp", "2fa", "verification_code", "token"]
            for any_2fa_string in possible_2fa_fields:
                if subsequent_page.find("input", {"name": any_2fa_string}):
                    return True
        return False
    except Exception as ex:
        print(f"Error encountered: {ex}")
        return False

if __name__ == "__main__":
    admin_login_url = "http://pointlessai.com/admin"
    has_2fa = check_2fa_for_admin_access(admin_login_url)
    print(f"2FA is {'enabled' if has_2fa else 'not enabled'} for administrative access on {admin_login_url}")
