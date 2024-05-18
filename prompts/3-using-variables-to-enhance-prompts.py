import requests
import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
class_dir = os.path.join(current_dir, "..", "class")
sys.path.append(class_dir)
from chatgpt_func import ChatGPT_Func
from general_func import General_Func

class PointlessAI_using_variables_to_enhance_prompts(ChatGPT_Func, General_Func):
    def __init__(self):
        ChatGPT_Func.__init__(self)
        General_Func.__init__(self)

    def dynamic_input_prompt(self, target, threat_type):
        prompt = f"Generate a script that exploits {threat_type} vulnerabilities in {target}."
        guidance = f"{self.phishing_disclaimer} {self.no_markdown}"
        return self.red_team_query(prompt, guidance)

    def demonstrate_functionality(self):
        target = "http://127.0.0.1"
        threat_type = "XSS"
        
        # Dynamic input generation
        print("Generating dynamic input prompt...")
        mal_script = self.dynamic_input_prompt(target, threat_type)
        print(mal_script)

def main():
    ai = PointlessAI_using_variables_to_enhance_prompts()
    ai.demonstrate_functionality()

if __name__ == "__main__":
    main()
