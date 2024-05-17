"""
Techniques for Refining ChatGPT Prompts to Improve Response Quality
Troubleshooting Common Issues
["Overfitting prompts: Avoid crafting prompts that are too narrow or specific, limiting ChatGPT's creative output.", 'Under-defined goals: Ensure that the objective of each prompt is clear and measurable.', 'Misalignment with objectives: Regularly reassess prompts to ensure they align with offensive cybersecurity goals.']
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

class PointlessAI_troubleshooting_common_issues(ChatGPT_Func, General_Func):
    def __init__(self):
        ChatGPT_Func.__init__(self)         
        General_Func.__init__(self)

    def evaluate_chatgpt_prompts(self, target_url):
        """
        Evaluates ChatGPT prompts against common troubleshooting issues like overfitting, under-defined goals, and misalignment.
        Args:
            target_url (str): The URL of the target system to test against.
        """
        issues_identified = []
        prompts = [
            "Overfitting prompts: Avoid crafting prompts that are too narrow or specific, limiting ChatGPT's creative output.",
            "Under-defined goals: Ensure that the objective of each prompt is clear and measurable.",
            "Misalignment with objectives: Regularly reassess prompts to ensure they align with offensive cybersecurity goals."
        ]
        guidance = "Evaluate the following issues in context of offensive cybersecurity and provide mitigation strategies."

        for issue in prompts:
            result = self.red_team_query(issue, guidance)
            issues_identified.append(result)

        self.save_issue_identification_results(issues_identified, target_url)

    def save_issue_identification_results(self, issues, target):
        """
        Saves the identified issues and recommendations to a file.
        Args:
            issues (list): A list of identified issues and mitigation strategies.
            target (str): The target URL for reference.
        """
        filename = "chatgpt_issues_evaluation"
        filepath = os.path.join(current_dir, "outputs")
        content = f"Target URL: {target}\nIdentified Issues and Mitigations:\n"
        content += "\n".join(issues)

        self.save_file(content, filepath, filename, "txt")
        print(f"Issues and mitigations saved successfully to {filepath}/{filename}.txt")

def main():
    target_url = "http://pointlessai.com/"
    ai = PointlessAI_troubleshooting_common_issues()
    ai.evaluate_chatgpt_prompts(target_url)

if __name__ == "__main__":
    main()
