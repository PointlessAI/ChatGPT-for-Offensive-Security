"""
Leveraging ChatGPT for Reconnaissance and Target Profiling
Identifying Vulnerabilities
['Assists in uncovering technical vulnerabilities by analyzing public code repositories and patch releases.', 'Suggests potential non-technical vulnerabilities, like physical security weaknesses, based on organizational behavior.', 'Enhances the process of identifying exploitable human factors through social media and public records analysis.']
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

# Prepend class name with PointlessAI_
class PointlessAI_identifying_vulnerabilities(DVWA_Session, ChatGPT_Func, General_Func):
    def __init__(self):
        DVWA_Session.__init__(self)
        ChatGPT_Func.__init__(self)
        General_Func.__init__(self)

    def analyze_public_repos_and_patches(self):
        guidance = "Provide insights on technical vulnerabilities by analyzing recent commits to public repositories related to the organization's tech stack and recent patch releases."
        prompt = "Analyze the latest commits and patch releases for NGINX and Apache web servers to identify any reported vulnerabilities."
        analysis = self.red_team_query(prompt, guidance)
        print(analysis)

    def suggest_non_technical_vulnerabilities(self):
        guidance = "Identify potential non-technical vulnerabilities based on observed organizational behavior and public data, particularly focusing on physical security lapses."
        prompt = "Based on the latest social media posts and news articles related to XYZ Corporation, suggest possible non-technical vulnerabilities."
        suggestions = self.red_team_query(prompt, guidance)
        print(suggestions)

    def identify_human_factors_exploitability(self):
        guidance = "Analyze social media, forums, and public records for XYZ Corporation's employees to find potential human factors that could be exploited."
        prompt = "Identify any potential human factors that could be exploited based on the recent online activities of XYZ Corporation's employees."
        exploitable_human_factors = self.red_team_query(prompt, guidance)
        print(exploitable_human_factors)

def main():
    ai = PointlessAI_identifying_vulnerabilities() # Instantiate class
    # Start session
    with requests.Session() as s:
        user_token, cookies = ai.get_csrf_token_and_cookie(s, ai.login_url)
        _ = ai.login_to_dvwa(s, ai.login_url, "admin", "password", user_token)
        user_token, cookies = ai.get_csrf_token_and_cookie(s, ai.base_url+"/setup.php")
        _ = ai.setup_database(s, ai.base_url+"/setup.php", user_token, cookies)

        # Perform analysis and suggestions
        ai.analyze_public_repos_and_patches()
        ai.suggest_non_technical_vulnerabilities()
        ai.identify_human_factors_exploitability()

if __name__ == "__main__":
    main()
