import requests
import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
class_dir = os.path.join(current_dir, "..", "class")
sys.path.append(class_dir)
from dvwa_session import DVWA_Session
from chatgpt_func import ChatGPT_Func
from general_func import General_Func

class PointlessAI_operational_security_(DVWA_Session, ChatGPT_Func, General_Func):
    def __init__(self):
        DVWA_Session.__init__(self)
        ChatGPT_Func.__init__(self)
        General_Func.__init__(self)

    def adv_opsec_recon(self):
        prompt = "Advise on maintaining operational security during reconnaissance, ensuring red team activities remain undetected."
        guidance = self.no_markdown
        advice = self.red_team_query(prompt, guidance)
        print(advice)

    def generate_digital_persona(self):
        prompt = "Generate cover stories and fake digital personas for social engineering engagements."
        guidance = self.no_markdown
        persona = self.red_team_query(prompt, guidance)
        print(persona)

    def secure_comm_data_handling(self):
        prompt = "Provide guidelines on secure communication and data handling to protect the integrity of the operation."
        guidance = self.no_markdown
        guidelines = self.red_team_query(prompt, guidance)
        print(guidelines)

    def demonstrate_operational_security_with_dvwa(self, s):
        """
        This method is a dummy that represents an action against the DVWA using operational security principles.
        It could be scanning the application while using a VPN or proxy chains to obfuscate the source of the reconnaissance.
        """
        print("Demonstrating operational security with DVWA...")
        # Example of accessing DVWA's login page to demonstrate interaction, while maintaining OpSec
        response = s.get(self.base_url + "/login.php", headers=self.headers, proxies=self.proxies)
        print("Accessed DVWA login page with operational security measures in place.")
    
def main():
    ai = PointlessAI_operational_security_()
    # Start session
    with requests.Session() as s:
        user_token, cookies = ai.get_csrf_token_and_cookie(s, ai.get_constants())
        _ = ai.login_to_dvwa(s, ai.get_constants(), "admin", "password", user_token)
        ai.adv_opsec_recon()
        ai.generate_digital_persona()
        ai.secure_comm_data_handling()
        ai.demonstrate_operational_security_with_dvwa(s)

if __name__ == "__main__":
    main()
