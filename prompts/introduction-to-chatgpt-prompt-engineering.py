"""
ChatGPT for offensive cybersecurity
Introduction to ChatGPT Prompt Engineering
['Understanding the role of prompt engineering in manipulating AI models.', 'The significance of tone, style, and specificity in crafting effective prompts.', 'How prompt engineering can be tailored for cybersecurity testing and red teaming operations.']
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

class PointlessAI_introduction_to_chatgpt_prompt_engineering(ChatGPT_Func, General_Func):
    def __init__(self):
        ChatGPT_Func.__init__(self)
        General_Func.__init__(self)

    def demonstrate_prompt_engineering(self, target_url):
        # Understanding the role of prompt engineering in manipulating AI models
        role_of_prompt_engineering = """
        Traditionally, the manipulation of AI models for cybersecurity testing would require direct code-based interaction or predefined scripts to test model behaviors. 
        With prompt engineering, we can indirectly guide the AI (like ChatGPT) towards specific behaviors or to execute certain tasks just by the way we frame our prompts. 
        This opens up novel approaches in offensive cybersecurity to probe for vulnerabilities, simulate social engineering attacks, or even generate phishing content that adapts to the target's profile.
        """
        print(role_of_prompt_engineering)

        # The significance of tone, style, and specificity in crafting effective prompts
        tone_style_specificity_significance = """
        In the context of offensive cybersecurity, crafting prompts with a specific tone, style, and level of specificity can crucially impact the success rate of information gathering or attack simulation. 
        For instance, a prompt tailored to emulate a genuine customer service inquiry could be more effective at eliciting sensitive information from a target system. 
        Similarly, a prompt designed with a high level of specificity can help in generating highly tailored attack vectors that are likely to evade generic security measures.
        """
        print(tone_style_specificity_significance)

        # How prompt engineering can be tailored for cybersecurity testing and red teaming operations
        prompt_engineering_for_cybersecurity = """
        Let's utilize ChatGPT to generate a simulated phishing email tailored to the target, '{}'. We'll craft a prompt that incorporates an understanding of the target's digital footprint and customize the email's tone and style to match.
        """.format(target_url)
        phishing_email_example = self.red_team_query(prompt_engineering_for_cybersecurity, self.phishing_disclaimer)
        print(phishing_email_example)

        # Simulating a target system exploitation attempt
        exploit_simulation = """
        Simulating a target system exploitation attempt using prompt engineering involves creating scenarios where the AI is tasked to outline steps or generate payloads 
        that could exploit known vulnerabilities within a targeted framework or system, '{}'. By refining our prompts with specific details about the target system's configuration or known weaknesses, 
        we can guide the AI to propose unique and possibly unthought-of attack vectors.
        """.format(target_url)
        exploit_attempt = self.red_team_query(exploit_simulation, self.phishing_disclaimer)
        print(exploit_attempt)

def main():
    target_url = "http://pointlessai.com/"
    ai = PointlessAI_introduction_to_chatgpt_prompt_engineering()
    ai.demonstrate_prompt_engineering(target_url)

if __name__ == "__main__":
    main()
