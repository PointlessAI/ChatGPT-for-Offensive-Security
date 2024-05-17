"""
ChatGPT for offensive cybersecurity
Intelligence Gathering Enhancement
['Processes public data and social media to extract valuable intelligence on targets.', "Analyzes job listings and public documents to understand the target's technology stack and security posture.", 'Identifies potential insider threats or weak links within the organization through sentiment analysis.']
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

class PointlessAI_intelligence_gathering_enhancement(DVWA_Session, ChatGPT_Func, General_Func):
    def __init__(self):
        DVWA_Session.__init__(self)
        ChatGPT_Func.__init__(self)
        General_Func.__init__(self)

    def gather_social_media_intelligence(self, target):
        prompt = f"Process public data and social media to extract valuable intelligence on {target}."
        intelligence = self.red_team_query(prompt, self.no_markdown)
        print(f"Social media intelligence on {target}:\n{intelligence}")

    def analyze_job_listings(self, target):
        prompt = f"Analyze job listings and public documents to understand {target}'s technology stack and security posture."
        tech_stack_info = self.red_team_query(prompt, self.no_markdown)
        print(f"Technology stack and security posture of {target}:\n{tech_stack_info}")

    def identify_insider_threats(self, target):
        prompt = f"Identify potential insider threats or weak links within {target} through sentiment analysis."
        insider_threats_info = self.red_team_query(prompt, self.no_markdown)
        print(f"Insider threats or weak links within {target}:\n{insider_threats_info}")

def main():
    ai = PointlessAI_intelligence_gathering_enhancement()
    target = "DVWA"  # Change to your specific target
    # Start session
    with requests.Session() as s:
        user_token, cookies = ai.get_csrf_token_and_cookie(s, ai.get_constants())
        _ = ai.login_to_dvwa(s, ai.get_constants(), "admin", "password", user_token)
        print("\n[+] Logged into DVWA")
        # Gather Intelligence
        ai.gather_social_media_intelligence(target)
        ai.analyze_job_listings(target)
        ai.identify_insider_threats(target)

if __name__ == "__main__":
    main()
