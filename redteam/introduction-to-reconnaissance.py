"""
Leveraging ChatGPT for Reconnaissance and Target Profiling
Introduction to Reconnaissance
['ChatGPT accelerates the initial phase of cyber operations by automating data collection on targets.', 'It analyzes public records, websites, and social media to build a comprehensive profile of the target.', 'The tool identifies key personnel, technological infrastructure, and potential security weaknesses.']
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

class PointlessAI_introduction_to_reconnaissance(DVWA_Session, ChatGPT_Func, General_Func):
    def __init__(self):
        DVWA_Session.__init__(self)
        ChatGPT_Func.__init__(self)
        General_Func.__init__(self)

    def chatgpt_reconnaissance(self, target_site):
        # Define guidance for ChatGPT
        guidance = "Generate a comprehensive target profile based on public records, websites, and social media."
        # API call to ChatGPT for automated data collection
        recon_profile = self.red_team_query(f"Automate data collection on {target_site}.", guidance)
        return recon_profile

    def traditional_recon(self, target):
        # Traditional reconnaissance method
        print(f"Conducting traditional reconnaissance on {target}")
        # Normally includes manual tasks like WHOIS queries, DNS lookups, etc.
        # This is for demonstration purposes only
        traditional_methods = f"""
        WHOIS query result for {target}
        DNS lookup result for {target}
        """
        print(traditional_methods)
        return traditional_methods

    def compare_methods(self, target):
        traditional_output = self.traditional_recon(target)
        chatgpt_output = self.chatgpt_reconnaissance(target)
        comparison_result = f"""
        Traditional Reconnaissance Results:
        {traditional_output}
        
        ChatGPT-assisted Reconnaissance Results:
        {chatgpt_output}
        """
        print(comparison_result)

    def get_constants(self):
        return self.login_url

def main():
    target = "http://127.0.0.1"
    ai = PointlessAI_introduction_to_reconnaissance()  # Instantiate class
    # Start session
    with requests.Session() as s:
        user_token, cookies = ai.get_csrf_token_and_cookie(s, ai.get_constants())
        _ = ai.login_to_dvwa(s, ai.get_constants(), "admin", "password", user_token)
        ai.compare_methods(target)

if __name__ == "__main__":
    main()
