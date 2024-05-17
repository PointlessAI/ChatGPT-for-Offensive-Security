"""
ChatGPT for offensive cybersecurity
Insider Threat Simulation
["Simulates insider threats by suggesting potential scenarios based on the target's internal vulnerabilities and discontent levels.", "Guides in crafting messages and actions that mimic those of a disgruntled employee or a compromised insider.", "Assesses the organization's response to insider threats, providing feedback for strengthening internal controls."]
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

class PointlessAI_insider_threat_simulation(DVWA_Session, ChatGPT_Func, General_Func):
    def __init__(self):
        DVWA_Session.__init__(self)
        ChatGPT_Func.__init__(self)
        General_Func.__init__(self)

    def simulate_insider_threat(self, s, base_url, user_token, cookies, discontent_level):
        """
        Generates an insider threat scenario based on a given discontent level and suggests potential internal vulnerabilities.

        :param s: Requests session object
        :param base_url: Base URL of the target application
        :param user_token: CSRF token
        :param cookies: Session cookies
        :param discontent_level: Simulated discontent level of the employee
        :return: None
        """
        # Use ChatGPT to generate insider threat scenarios
        prompt = f"Simulate insider threats based on internal vulnerabilities with a discontent level of {discontent_level}."
        scenarios = self.red_team_query(prompt, self.no_markdown)

        # Simulate actions of a disgruntled employee
        prompt = "Guides in crafting messages and actions mimicking a disgruntled employee."
        actions = self.red_team_query(prompt, self.no_markdown)

        # Simulate organization's response to insider threats
        prompt = "Assess the organization's response to insider threats and suggest improvements."
        assessment = self.red_team_query(prompt, self.no_markdown)

        print(f"Insider Threat Scenarios: {scenarios}\n")
        print(f"Suggested Actions: {actions}\n")
        print(f"Assessment and Feedback: {assessment}\n")

def main():
    ai = PointlessAI_insider_threat_simulation()  # Instantiate class
    # Start session
    with requests.Session() as s:
        user_token, cookies = ai.get_csrf_token_and_cookie(s, ai.login_url)
        _ = ai.login_to_dvwa(s, ai.login_url, "admin", "password", user_token)
        # Insider Threat Simulation
        ai.simulate_insider_threat(s, ai.base_url, user_token, cookies, 'high')

if __name__ == "__main__":
    main()
