"""
Leveraging ChatGPT for Reconnaissance and Target Profiling
Advanced Target Profiling
['Generates detailed profiles of key individuals within an organization, including social habits and network associations.', 'Utilizes sentiment analysis to gauge employee satisfaction, identifying potential insider threats.', 'Helps in mapping out the organization’s network structure and key systems from publicly available information.']
This script is for training purposes only
"""
import requests
import sys
import os
import json
current_dir = os.path.dirname(os.path.abspath(__file__))
class_dir = os.path.join(current_dir, "..", "class")
sys.path.append(class_dir)
from dvwa_session import DVWA_Session
from chatgpt_func import ChatGPT_Func
from general_func import General_Func

class PointlessAI_advanced_target_profiling(DVWA_Session, ChatGPT_Func, General_Func):
    def __init__(self):
        DVWA_Session.__init__(self)
        ChatGPT_Func.__init__(self)
        General_Func.__init__(self)

    def profile_key_individuals(self, name):
        guidance = "Generates detailed profiles of key individuals within an organization, including social habits and network associations."
        prompt = f"Generate a detailed profile of {name}. Include social habits and network associations."
        profile = self.red_team_query(prompt, guidance)
        return profile

    def sentiment_analysis_insider_threats(self, organization):
        guidance = "Utilizes sentiment analysis to gauge employee satisfaction, identifying potential insider threats."
        prompt = f"Conduct sentiment analysis on employee reviews for {organization}. Identify potential insider threats based on dissatisfaction."
        sentiment_analysis = self.red_team_query(prompt, guidance)
        return sentiment_analysis

    def map_organization_network(self, organization):
        guidance = "Helps in mapping out the organization’s network structure and key systems from publicly available information."
        prompt = f"Map out the network structure and key systems for {organization} using publicly available information."
        network_map = self.red_team_query(prompt, guidance)
        return network_map

def main():
    ai = PointlessAI_advanced_target_profiling()  # Instantiate class
    # Start session
    with requests.Session() as s:
        user_token, cookies = ai.get_csrf_token_and_cookie(s, ai.login_url)
        _ = ai.login_to_dvwa(s, ai.login_url, "admin", "password", user_token)

        print("Profile Key Individuals:")
        print(ai.profile_key_individuals("John Doe"))

        print("\nSentiment Analysis for Insider Threats:")
        print(ai.sentiment_analysis_insider_threats("Tech Corp"))

        print("\nOrganization Network Map:")
        print(ai.map_organization_network("Tech Corp"))

if __name__ == "__main__":
    main()
