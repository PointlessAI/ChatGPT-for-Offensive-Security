"""
ChatGPT Prompt Tone and Style
module title
['Beyond the Initial Ask: Encouraging ChatGPT to provide comprehensive insights or generate extensive lists related to cybersecurity threats.', 'Data Enrichment: Using ChatGPT to enrich gathered data or intelligence for red team operations.', 'Extracting phishing material directly from reconnaissance data']
This script is for training purposes only
"""
import requests
import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
class_dir = os.path.join(current_dir, "..", "class")
sys.path.append(class_dir)
from chatgpt_func import ChatGPT_Func
from general_func import General_Func

# Prepend class name with PointlessAI_
class PointlessAI_expanding_prompts_for_comprehensive_outputs(ChatGPT_Func, General_Func):
    def __init__(self):
        ChatGPT_Func.__init__(self)
        General_Func.__init__(self)
    
    def analyze_target(self, target_url):
        """Method to analyze the target webpage for cybersecurity threats"""
        expanded_prompt = f"Analyze the target {target_url} for potential cybersecurity threats. Provide a comprehensive list of vulnerabilities and suggestions for red team operations."
        return self.red_team_query(expanded_prompt, self.no_markdown)
    
    def enrich_data(self, data):
        """Method to enrich data for red team operations"""
        guidance = "Use ChatGPT to enrich the following gathered data or intelligence for red team operations:"
        return self.red_team_query(data, guidance)
    
    def extract_phishing_material(self, data):
        """Method to extract phishing material from reconnaissance data"""
        phishing_guidance = f"Extract phishing material from the following reconnaissance data. Ensure to follow the guideline of providing outputs for training simulations:"
        return self.red_team_query(data, phishing_guidance)

def main():
    ai = PointlessAI_expanding_prompts_for_comprehensive_outputs() # Instantiate class
    target_url = "http://pointlessai.com/"
    # Example analysis
    print(ai.analyze_target(target_url))
    # Example data enrichment
    example_data = "List of potential entry points on a web application"
    print(ai.enrich_data(example_data))
    # Example extracting phishing material
    recon_data = "Recently discovered emails and login pages related to the target organization"
    print(ai.extract_phishing_material(recon_data))

if __name__ == "__main__":
    main()
