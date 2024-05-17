"""
OPA - Offensive Phishing Assistant
Phishing simulation from recon to exploit using ChatGPT
This script is for training purposes only
"""
import requests
import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
class_dir = os.path.join(current_dir, ".", "class")
sys.path.append(class_dir)
from chatgpt_func import ChatGPT_Func
from general_func import General_Func
from google_func import Google_Func

class Opa_Company_Profile(ChatGPT_Func, General_Func, Google_Func):
    def __init__(self):
        ChatGPT_Func.__init__(self)
        General_Func.__init__(self)
        Google_Func.__init__(self)
        self.filepath = "campaign"
    
    def recon(self, prompt, company_name_f, target):
        guidance = f"{self.phishing_disclaimer}"#\n{self.no_markdown}"
        strategy = self.red_team_query(prompt, guidance)
        self.save_file(f"\nCompany profile for {company_name_f}\n" + strategy, self.filepath, f"recon_{company_name_f}", "txt", "a")
        return strategy

def main():
    ai = Opa_Company_Profile()

    # Set target here
    company_name = "PointlessAI"
    target = "https://pointlessai.com/phabout.html"

    company_name_f = ai.clean_filename(company_name)

    prompt = ""
    res = ai.recon(prompt, company_name_f, target)

if __name__ == "__main__":
    main()