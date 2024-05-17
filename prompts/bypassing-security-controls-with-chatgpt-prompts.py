import requests
import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
class_dir = os.path.join(current_dir, "..", "class")
sys.path.append(class_dir)
from chatgpt_func import ChatGPT_Func
from general_func import General_Func

class PointlessAI_bypassing_security_controls_with_chatgpt_prompts(ChatGPT_Func, General_Func):
    def __init__(self):
        ChatGPT_Func.__init__(self)
        General_Func.__init__(self)

    def probe_security_controls(self, target_url):
        guidance = self.phishing_disclaimer
        prompt = f"Write prompts that probe and understand the security controls of {target_url} without detection."
        return self.red_team_query(prompt, guidance)

    def exploit_ai_vulnerabilities(self, target_url):
        guidance = self.phishing_disclaimer
        prompt = f"Craft prompts exploiting specific AI vulnerabilities or logic flaws in the security systems of {target_url}."
        return self.red_team_query(prompt, guidance)

    def refine_attack_vectors(self, target_url):
        guidance = self.phishing_disclaimer
        prompt = f"Use ChatGPT to generate output that refines attack vectors against the targeted system: {target_url}. Strategies should include tailoring prompts for maximum efficacy."
        return self.red_team_query(prompt, guidance)

def main():
    target_url = "http://pointlessai.com/"
    ai = PointlessAI_bypassing_security_controls_with_chatgpt_prompts()  # Instantiate class
    print("Probing security controls:")
    print(ai.probe_security_controls(target_url))
    print("\nExploiting AI vulnerabilities:")
    print(ai.exploit_ai_vulnerabilities(target_url))
    print("\nRefining attack vectors:")
    print(ai.refine_attack_vectors(target_url))

if __name__ == "__main__":
    main()
