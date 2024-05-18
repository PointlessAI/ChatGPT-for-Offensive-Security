"""
ChatGPT Prompt Tone and Style
module title
['Style variations: technical, verbose, succinct, and their effects on responses.', 'Crafting prompts in a style that mimics legitimate user or system queries.', 'The role of style in blending with target environment communication norms.']
This script is for for training purposes only
"""
import requests
import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
class_dir = os.path.join(current_dir, "..", "class")
sys.path.append(class_dir)
from chatgpt_func import ChatGPT_Func
from general_func import General_Func

class PointlessAI_style_in_prompts(ChatGPT_Func, General_Func):
    def __init__(self):
        ChatGPT_Func.__init__(self)
        General_Func.__init__(self)

    def simulate_style_variation(self, target_style):
        target_url = "http://pointlessai.com/"
        guidance = f"Simulate queries in different styles to see how the target system responds. {self.phishing_disclaimer}"
        prompt = f"Explain SSRF server side request forgery in a {target_style} style."

        response = self.red_team_query(prompt, guidance)
        print(f"\n---------------------{target_style}---------------------\n{response}\n")

def main():
    ai = PointlessAI_style_in_prompts()  # Instantiate class
    # Demonstrating the use of style variations
    styles = ["technical", "verbose", "succinct", "funny", "intelligent", "genius", "red team", "hacker"]
    for style in styles:
        ai.simulate_style_variation(style)

if __name__ == "__main__":
    main()
