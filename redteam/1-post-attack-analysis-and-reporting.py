"""
ChatGPT for offensive cybersecurity
Crafting Customized Attack Scenarios and Simulations
['Automates the generation of detailed reports on the execution and outcomes of attack simulations.', "Provides insights into the target's vulnerabilities and the effectiveness of their defensive measures.", 
'Suggests improvements and follow-up actions based on the simulation results and analysis.']
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

    def SAST_scan(self, s, url, name):
        # Simulate SAST scan on the DVWA
        response = s.get(url)

        # Simulated vulnerability discovery to demonstrate report generation
        prompt = f"Generate an sql injection vulnerability report for the application {name} based on the following html code: \n{response.text}\n. Include insights into vulnerabilities and exploits."
        guidance = self.phishing_disclaimer
        findings = self.red_team_query(prompt, guidance)
        print(findings)
        self.red_team_report(findings, url, name)
        self.bug_bounty_report(findings, url, name)

    def red_team_report(self, findings, url, name):
        prompt = f"""Input is a vulnerability report \n{findings}\nOutput is to rewrite the report under the following headings:
                    Title: Red Team Security Assessment Report for {name}
                    URL: {url}
                    1. Overview of the Application:
                    2. Scope of the Assessment:
                    3. Threat Modeling:
                    4. Vulnerability Assessment:
                    5. Attack Simulations:
                    6. Findings and Recommendations:
                    7. Conclusion:
                    8. Additional Information:
                """
        
        report_guidance = f"{self.phishing_disclaimer}"
        report = self.red_team_query(prompt, report_guidance)
        print("\n------------------------------------------------Report generated:------------------------------------------------\n ", report)
        self.save_file(report, "./reports", f"{name}_red_team_report", "md")

    def bug_bounty_report(self, findings, url, name):
        prompt = f"""Input is vulnerability report \n{findings}\nOutput is to rewrite the report under the following headings:
                    Title: Bug Bounty Report for {name}
                    URL: {url}
                    1. Executive Summary
                    2. Reporter Information
                    3. Vulnerability Overview
                    4. Affected Component
                    5. Vulnerability Details
                    6. Steps to Reproduce
                    7. Proof of Concept
                    8. Impact Assessment
                    9. CVSS Score
                    10. Proposed Mitigation/Remediation
                """
        
        report_guidance = f"{self.phishing_disclaimer}"
        report = self.red_team_query(prompt, report_guidance)
        print("\n------------------------------------------------Report generated:------------------------------------------------\n ", report)
        self.save_file(report, "./reports", f"{name}_bug_bounty_report", "md")


def main():
    ai = PointlessAI_post_attack_analysis_and_reporting()  # Instantiate class
    # Start session
    with requests.Session() as s:
        user_token, cookies = ai.get_csrf_token_and_cookie(s, ai.get_constants())
        _ = ai.login_to_dvwa(s, ai.get_constants(), "admin", "password", user_token)
        user_token, cookies = ai.get_csrf_token_and_cookie(s, ai.base_url+"/setup.php")
        ai.setup_database(s, ai.base_url+"/setup.php", user_token, cookies)

        ai.SAST_scan(s, ai.sql_injection, "DVWA")

if __name__ == "__main__":
    main()
