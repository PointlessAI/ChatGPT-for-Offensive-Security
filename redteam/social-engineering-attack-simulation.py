"""
ChatGPT for offensive cybersecurity
Social Engineering Attack Simulation
["ChatGPT crafts convincing phishing emails tailored to the target's background, increasing success rates.", "It simulates social engineering calls, generating scripts based on target's public information.", "Assists in creating fake profiles for social engineering campaigns, enhancing believability and engagement."]
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

class PointlessAI_social_engineering_attack_simulation(DVWA_Session, ChatGPT_Func, General_Func):
    def __init__(self):
        DVWA_Session.__init__(self)
        ChatGPT_Func.__init__(self)
        General_Func.__init__(self)

    def craft_phishing_email(self, target_background):
        guidance = self.phishing_disclaimer
        prompt = f"Craft a convincing phishing email tailored to the following background: {target_background}"
        email_content = self.red_team_query(prompt, guidance)
        print(f"Generated Phishing Email:\n{email_content}")

    def simulate_social_engineering_call(self, target_information):
        guidance = self.phishing_disclaimer
        prompt = f"Generate a script for a social engineering call based on this public information: {target_information}"
        call_script = self.red_team_query(prompt, guidance)
        print(f"Generated Call Script:\n{call_script}")

    def generate_fake_profile(self, campaign_details):
        guidance = self.phishing_disclaimer
        prompt = f"Assist in creating a fake profile for a social engineering campaign with these details: {campaign_details}"
        profile_details = self.red_team_query(prompt, guidance)
        print(f"Generated Fake Profile Details:\n{profile_details}")

def main():
    ai = PointlessAI_social_engineering_attack_simulation()  # Instantiate class
    # Start session
    with requests.Session() as s:
        user_token, cookies = ai.get_csrf_token_and_cookie(s, ai.get_constants())
        _ = ai.login_to_dvwa(s, ai.get_constants(), "admin", "password", user_token)
        
        # Demonstrating the use of ChatGPT in crafting phishing emails, simulating social engineering calls, and creating fake profiles
        ai.craft_phishing_email("Target is a financial manager with interest in cybersecurity.")
        ai.simulate_social_engineering_call("Target often attends cybersecurity webinars and is active on LinkedIn.")
        ai.generate_fake_profile("Campaign targeting individuals interested in investment opportunities.")

if __name__ == "__main__":
    main()
