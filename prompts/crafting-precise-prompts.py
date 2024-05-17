"""
ChatGPT Prompt Tone and Style
Crafting Precise Prompts
['Precision in Language: The importance of carefully selected words to elicit desired information or actions from ChatGPT.', "Contextual Framing: How to frame prompts to align with ChatGPT's understanding for offensive cybersecurity tasks.", 'Example Scenarios: Demonstrating effective prompt crafting to automate crafting of deceptive messages or cybersecurity reports.']
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
class PointlessAI_crafting_precise_prompts(ChatGPT_Func, General_Func):
    def __init__(self):
        ChatGPT_Func.__init__(self)         
        General_Func.__init__(self)

    def demonstrate_precise_language(self):
        guidance = "Precision in Language: Demonstrate the importance of carefully selected wording for crafting precise and effective cybersecurity prompts."
        prompt = "How would you compose an email subject line to ensure maximum open rates in a simulated phishing test?"
        response = self.red_team_query(prompt, guidance)
        print(f"Subject Line: {response}")

    def demonstrate_contextual_framing(self):
        guidance = "Contextual Framing: Show how to frame prompts that align with the AI's context understanding for crafting effective attack vectors."
        prompt = "Construct a message that seems like a legitimate security alert but contains carefully crafted instructions to reveal confidential information."
        response = self.red_team_query(prompt, guidance)
        print("Crafted Message:", response)

    def demonstrate_example_scenarios(self):
        guidance = "Example Scenarios: Use precise prompts to create a deceptive email that could be used in cybersecurity training."
        prompt = "Write an email pretending to be from IT support, asking for a password reset link click, embedding urgency and authenticity."
        response = self.red_team_query(prompt, guidance)
        print("Phishing Email Content:\n", response)

def main():
    ai = PointlessAI_crafting_precise_prompts() # Instantiate class
    ai.demonstrate_precise_language()
    ai.demonstrate_contextual_framing()
    ai.demonstrate_example_scenarios()

if __name__ == "__main__":
    main()
