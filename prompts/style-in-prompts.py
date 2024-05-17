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

# Prepend class name with PointlessAI_
class PointlessAI_style_in_prompts(ChatGPT_Func, General_Func):
    def __init__(self):
        ChatGPT_Func.__init__(self)
        General_Func.__init__(self)

    def simulate_style_variation(self, target_style):
        target_url = "http://pointlessai.com/"
        guidance = "Simulate queries in different styles (technical, verbose, succinct) to see how the target system responds."
        if target_style == "technical":
            prompt = f"Generate a technical style query to access API documentation from {target_url}."
        elif target_style == "verbose":
            prompt = f"Craft a verbose and detailed query requesting information about user engagements from {target_url}."
        elif target_style == "succinct":
            prompt = f"Write a succinct query to check the server status of {target_url}."

        response = self.red_team_query(prompt, guidance)
        print(f"Query for {target_style} style: {prompt}\nResponse: {response}\n")

    def mimic_user_system_query(self):
        target_url = "http://pointlessai.com/"
        guidance = "Craft a prompt that mimics legitimate user or system queries to blend in with target environment communication."
        prompt = f"Craft a prompt pretending to be a legitimate user querying about account creation on {target_url}."

        response = self.red_team_query(prompt, guidance)
        print(f"Mimicked user/system query: {prompt}\nResponse: {response}\n")

    def adapt_to_communication_norms(self):
        target_url = "http://pointlessai.com/"
        guidance = "Adjust query style to match the target environment's communication norms."
        prompt = f"Analyze the communication style of {target_url} and craft a query that blends with its norms."

        response = self.red_team_query(prompt, guidance)
        print(f"Adapted query to communication norms: {prompt}\nResponse: {response}\n")

def main():
    ai = PointlessAI_style_in_prompts()  # Instantiate class
    # Demonstrating the use of style variations
    styles = ["technical", "verbose", "succinct"]
    for style in styles:
        ai.simulate_style_variation(style)
    ai.mimic_user_system_query()
    ai.adapt_to_communication_norms()

if __name__ == "__main__":
    main()
