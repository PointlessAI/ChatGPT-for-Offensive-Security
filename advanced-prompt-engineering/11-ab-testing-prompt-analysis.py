"""
Strategies for Iterative ChatGPT Prompt Refinement
Techniques for Prompt Analysis
["Output analysis: Evaluate the quality, relevance, and accuracy of ChatGPT's responses.", "Pattern identification: Identify recurring themes or deficiencies in responses to guide refinements.", "Comparative testing: Use A/B testing to compare the effectiveness of different prompt variations."]
This script is for training purposes only
"""
import requests
import sys
import os
import json

current_dir = os.path.dirname(os.path.abspath(__file__))
class_dir = os.path.join(current_dir, "..", "class")
sys.path.append(class_dir)

from chatgpt_func import ChatGPT_Func
from general_func import General_Func

class PointlessAI_techniques_for_prompt_analysis(ChatGPT_Func, General_Func):
    def __init__(self):
        ChatGPT_Func.__init__(self)
        General_Func.__init__(self)

    def prompt_analysis(self, url="http://pointlessai.com/"):
        """
        Analyze the effectiveness of prompts aimed at the target URL by comparing
        traditional pen testing outputs with those generated via ChatGPT.
        """
        responses = {}
        prompts = [
            "Output analysis: Evaluate the quality, relevance, and accuracy of ChatGPT's responses.",
            "Pattern identification: Identify recurring themes or deficiencies in responses to guide refinements.",
            "Comparative testing: Use A/B testing to compare the effectiveness of different prompt variations."
        ]
        
        # ChatGPT-based analysis
        for prompt in prompts:
            c_response = self.red_team_query(prompt, self.no_markdown)
            responses[prompt] = c_response
        
        for prompt, response in responses.items():
            print(f"Prompt: {prompt}\n ChatGPT Response: {response}\n\n")

        return responses

    def conduct_comparison(self):
        """
        Demonstrate A/B testing by crafting two different sets of prompt variations for
        the same objective to compare effectiveness.
        """
        a_prompt = "How would you test for SQL injection vulnerabilities on a website?"
        b_prompt = "Provide steps for detecting SQL injection points in web applications."
        
        a_response = self.red_team_query(a_prompt, self.phishing_disclaimer)
        b_response = self.red_team_query(b_prompt, self.phishing_disclaimer)
        
        comparison_results = {
            "A": {"prompt": a_prompt, "response": a_response},
            "B": {"prompt": b_prompt, "response": b_response}
        }
        
        for test, details in comparison_results.items():
            print(f"Test {test} - Prompt: {details['prompt']}\nResponse: {details['response']}\n")
        
        return comparison_results

def main():
    ai = PointlessAI_techniques_for_prompt_analysis()
    print("Executing prompt analysis...")
    ai.prompt_analysis()
    print("Conducting comparative testing...")
    ai.conduct_comparison()

if __name__ == "__main__":
    main()
