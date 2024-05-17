"""
ChatGPT for offensive cybersecurity
Crafting Customized Attack Scenarios and Simulations
['Automates the generation of detailed reports on the execution and outcomes of attack simulations.', "Provides insights into the target's vulnerabilities and the effectiveness of their defensive measures.", 'Suggests improvements and follow-up actions based on the simulation results and analysis.']
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

class PointlessAI_post_attack_analysis_and_reporting(DVWA_Session, ChatGPT_Func, General_Func):
    def __init__(self):
        DVWA_Session.__init__(self)
        ChatGPT_Func.__init__(self)
        General_Func.__init__(self)

    def simulate_attack_and_generate_report(self, session, url):
        # Simulate an attack on the DVWA
        response = session.get(url)
        if response.status_code == 200:
            print("Attack simulation successful.")
        else:
            print("Attack simulation failed.")

        # Generate a report using ChatGPT
        prompt = "Generate a detailed report on an offensive cybersecurity attack simulation targeting a vulnerable web application. Include insights into vulnerabilities and defensive measures effectiveness."
        report_guidance = "Please provide insights on improvements and follow-up actions based on the simulation results."
        report = self.red_team_query(prompt, report_guidance)
        print("Report generated: ", report)

        # Suggest improvements based on the simulation results
        improvements_prompt = "Based on the following attack simulation results, suggest improvements and follow-up actions."
        improvements_guidance = "Ensure the suggestions are practical and can significantly enhance the target's security posture."
        improvements = self.red_team_query(improvements_prompt, improvements_guidance)
        print("Recommended improvements: ", improvements)

    def setup_database(self, s, url, user_token, cookies):
        # Setup the DVWA database to ensure it's in a known state
        data = {
            "create_db": "Create / Reset Database",
            "user_token": user_token
        }
        response = s.post(url, data=data, cookies=cookies)
        if response.status_code == 200:
            print("Database setup successful.")
        else:
            print("Database setup failed.")

def main():
    ai = PointlessAI_post_attack_analysis_and_reporting()  # Instantiate class
    # Start session
    with requests.Session() as s:
        user_token, cookies = ai.get_csrf_token_and_cookie(s, ai.get_constants())
        _ = ai.login_to_dvwa(s, ai.get_constants(), "admin", "password", user_token)
        user_token, cookies = ai.get_csrf_token_and_cookie(s, ai.base_url+"/setup.php")
        ai.setup_database(s, ai.base_url+"/setup.php", user_token, cookies)

        ai.simulate_attack_and_generate_report(s, ai.sql_injection)

if __name__ == "__main__":
    main()
