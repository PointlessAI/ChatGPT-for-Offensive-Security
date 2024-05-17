"""
Techniques for Refining ChatGPT Prompts to Improve Response Quality
Introduction to Prompt Refinement
['Understanding baseline responses: Analyze initial outputs from ChatGPT to identify areas of improvement.', 'Goal definition: Clearly define what improvement means for the specific offensive cybersecurity context.', "Feedback loop importance: Utilize ChatGPT's responses as feedback to refine further prompts."]
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
class PointlessAI_introduction_to_prompt_refinement(ChatGPT_Func, General_Func):
    def __init__(self):
        ChatGPT_Func.__init__(self)
        General_Func.__init__(self)

    def analyze_baseline_responses(self, target_url):
        initial_prompt = "Given the output from ChatGPT: Analyze the initial response quality for offensive cybersecurity testing on {}.".format(target_url)
        guidance = self.phishing_disclaimer
        baseline_analysis = self.red_team_query(initial_prompt, guidance)
        print("Baseline ChatGPT Response Analysis:\n", baseline_analysis)

    def define_improvement_goals(self, target_url):
        goal_prompt = "Define improvement goals for ChatGPT responses in the context of penetrating testing for {}.".format(target_url)
        guidance = self.phishing_disclaimer
        improvement_goals = self.red_team_query(goal_prompt, guidance)
        print("Improvement Goals Definition:\n", improvement_goals)

    def refine_prompts_via_feedback_loop(self, target_url):
        feedback_prompt = "Describe how to use ChatGPT's responses as feedback to refine further prompts for targeted offensive cybersecurity actions against {}.".format(target_url)
        guidance = self.phishing_disclaimer
        feedback_loop_strategy = self.red_team_query(feedback_prompt, guidance)
        print("Feedback Loop Strategy for Prompt Refinement:\n", feedback_loop_strategy)

def main():
    target_url = "http://pointlessai.com/"
    ai = PointlessAI_introduction_to_prompt_refinement()  # Instantiate class
    ai.analyze_baseline_responses(target_url)
    ai.define_improvement_goals(target_url)
    ai.refine_prompts_via_feedback_loop(target_url)

if __name__ == "__main__":
    main()
