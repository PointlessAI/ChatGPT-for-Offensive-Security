"""
ChatGPT for offensive cybersecurity
Advanced Prompt Structures
['Chain of thought prompting: Guide ChatGPT through a logical progression of steps.', 'Hypothetical scenarios: Use fictional situations to explore creative attack vectors.', 'Conditional responses: Request ChatGPT to provide outputs based on specific conditions or outcomes.']
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
class PointlessAI_advanced_prompt_structures(ChatGPT_Func, General_Func):
    def __init__(self):
        ChatGPT_Func.__init__(self)
        General_Func.__init__(self)

    def execute_chain_of_thought(self, target):
        prompt = f"Provide detailed logical steps to analyze potential vulnerabilities in {target} using advanced prompt structures"
        guidance = "Provide a series of logical steps, considering different aspects of the system, such as entry points, data flow, and potential weaknesses."
        analysis_steps = self.red_team_query(prompt, guidance)
        print("Analysis Steps:")
        print(analysis_steps)

    def execute_hypothetical_scenarios(self, target):
        prompt = f"Create hypothetical scenarios where {target} could be compromised through unique attack vectors."
        guidance = "Think outside the box and propose creative yet plausible attack vectors that could be exploited."
        scenarios = self.red_team_query(prompt, guidance)
        print("Hypothetical Scenarios:")
        print(scenarios)

    def execute_conditional_responses(self, target):
        prompt = f"If {target} has an outdated web server, what specific vulnerabilities can be exploited, and how? Additionally, outline how to mitigate these risks."
        guidance = "Consider the condition provided and elaborate on potential exploitation methods along with suggested countermeasures."
        conditional_responses = self.red_team_query(prompt, guidance)
        print("Conditional Responses:")
        print(conditional_responses)

    def demonstrate_functionality(self):
        target = "http://pointlessai.com/"
        print("Executing Chain of Thought Prompting...")
        self.execute_chain_of_thought(target)
        print("\nExecuting Hypothetical Scenarios...")
        self.execute_hypothetical_scenarios(target)
        print("\nExecuting Conditional Responses...")
        self.execute_conditional_responses(target)

def main():
    ai = PointlessAI_advanced_prompt_structures() # Instantiate class
    ai.demonstrate_functionality()

if __name__ == "__main__":
    main()
