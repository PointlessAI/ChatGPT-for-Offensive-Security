# Session Fixation using bWAPP (demo environment)
# This code provides an example of session hijacking using the bWAPP (demo environment)
# targetting vulnerabilities at http://127.0.0.1/vulnerabilities/xss_d/.

import requests

class SessionFixation:
    def __init__(self):
        # Initialize the session object
        self.s = requests.Session()

    def get_csrf_token(self):
        # Function to extract CSRF token from the main page
        target_url = "http://127.0.0.1/vulnerabilities/xss_d/"
        response = self.s.get(target_url)
        token = self.extract_from_response(response.text, 'input name="user_token" value="', '"')
        return token

    def extract_from_response(self, response_text, start_str, end_str):
        # Helper function to extract the required part from response
        start_index = response_text.find(start_str)
        if start_index == -1:
            return None
        start_index += len(start_str)
        end_index = response_text.find(end_str, start_index)
        if end_index == -1:
            return None
        return response_text[start_index:end_index]

    def authenticate_session(self, user_token, username='bee', password='bug'):
        # Function to authenticate the stolen session using CSRF token
        login_url = "http://127.0.0.1/login.php"
        post_data = {
            'login': username,
            'password': password,
            'form': 'submit',
            'user_token': user_token
        }
        self.s.post(login_url, data=post_data)

    def show_authenticated_page(self):
        # Function to display the content of an authenticated page
        profile_url = "http://127.0.0.1/profile.php"
        response = self.s.get(profile_url)
        return response.text

def main():
    session_fixation = SessionFixation()

    # Demonstrate token extraction
    csrf_token = session_fixation.get_csrf_token()
    print(f"CSRF Token: {csrf_token}")  # Verify token value manually

    # Authenticate session using valid credentials
    if csrf_token:
        session_fixation.authenticate_session(csrf_token)
        
        # Show authenticated page content
        authenticated_contents = session_fixation.show_authenticated_page()
        print(authenticated_contents)

if __name__ == "__main__":
    main()
