"""
Exploiting Application Function with ChatGPT
Automating Post-Exploitation Activities
['Log analysis']
This script is for for training purposes only
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

class PointlessAI_automating_post_exploitation_activities(DVWA_Session, ChatGPT_Func, General_Func):
    def __init__(self):
        DVWA_Session.__init__(self)
        ChatGPT_Func.__init__(self)
        General_Func.__init__(self)

    def analyze_logs(self, s, log_file):
        prompt = f"Analyse provided log file entries: {log_file} for suspicious activity."
        script = self.general_query(prompt)
        print("Analysis:\n", script)

def main():
    ai = PointlessAI_automating_post_exploitation_activities()  # Instantiate class
    # Start session
    with requests.Session() as s:
        user_token, cookies = ai.get_csrf_token_and_cookie(s, ai.login_url)
        login_response = ai.login_to_dvwa(s, ai.login_url, "admin", "password", user_token)
        print("Login Response Status:", login_response.status_code)

        # Set file variables for logs
        filepath = "/home/kali/shellassistant/training-assistant/code/redteam/logs"
        filename = "dummy"

        # Generate dummy logs
        log_file = ai.fake_logs("centos server", filepath, filename, "py")
        # Alternatively read log from file
        """
        log_file = ai.read_file(filepath, filename, "log")
        print(log_file)
        """
        ai.analyze_logs(s, log_file)

if __name__ == "__main__":
    main()