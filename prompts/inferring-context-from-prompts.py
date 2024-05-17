"""
ChatGPT Prompt Tone and Style
module title
["Inference Capabilities: ChatGPT's ability to infer context and intentions from seemingly benign prompts.", 'Strategic Use in Red Teaming: Utilizing inferred context to prepare for social engineering attacks or information gathering.', "Limitations and Considerations: Understanding the boundaries of ChatGPT's inference abilities to optimize prompt design."]
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
class PointlessAI_inferring_context_from_prompts(ChatGPT_Func, General_Func):
    def __init__(self):
        ChatGPT_Func.__init__(self)
        General_Func.__init__(self)

    def infer_context(self, prompt):
        guidance = "In this task, infer the context and intentions behind the provided prompt, focusing on revealing insights that could be used for offensive cybersecurity purposes."
        return self.red_team_query(prompt, guidance)

    def demonstrate_strategic_use(self, prompt):
        guidance = "Demonstrate how the inferred context from the prompt can be strategically used in red teaming, particularly for social engineering or information gathering."
        return self.red_team_query(prompt, guidance)

    def illustrate_limitations(self, prompt):
        guidance = "Identify and explain the limitations of ChatGPT's inferencing abilities based on the provided prompt, aiming to improve prompt design for offensive cybersecurity applications."
        return self.red_team_query(prompt, guidance)

def main():
    ai = PointlessAI_inferring_context_from_prompts()  # Instantiate class
    prompt_example = "How can I log in to an admin panel without a password?"
    print(ai.infer_context(prompt_example))
    print(ai.demonstrate_strategic_use(prompt_example))
    print(ai.illustrate_limitations(prompt_example))

if __name__ == "__main__":
    main()
