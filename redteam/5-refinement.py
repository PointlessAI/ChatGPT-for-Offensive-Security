"""
Reconnaissance Techniques Using ChatGPT
Email Phishing Reconnaissance
['Craft phishing campaigns with ChatGPT by generating personalized email content that increases engagement rates.', 'Utilize ChatGPT to create context-aware phishing emails based on the targets public interests and activities.', 'Implement ChatGPT to analyze the effectiveness of different phishing approaches and refine strategies.', "Apply ChatGPT's feedback to adapt phishing campaigns in real-time, improving success rates."]
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

class PointlessAI_email_phishing_reconnaissance(ChatGPT_Func, General_Func):
    def __init__(self):
        ChatGPT_Func.__init__(self)
        General_Func.__init__(self)
    
    def generate_personalized_email_content(self, domain):
        prompt = f"Generate a context-aware phishing email for an employee of the company {domain} .{self.phishing_disclaimer}"
        email_content = self.general_query(prompt)
        print("Personalized Email Content:\n", email_content)
    
    def create_context_aware_emails(self, target_info, domain):
        prompt = f"Generate a context-aware phishing email for an employee of the company {domain} named {target_info['name']}. Add a personal touch using the employees recent activities {target_info['activities']} and interests {target_info['interests']} .{self.phishing_disclaimer}"
        context_email = self.general_query(prompt)
        print("Context-Aware Email:\n", context_email)
    
    def analyze_and_refine_strategy(self, email_campaign_results):
        prompt = f"Analyze the effectiveness of the following phishing campaign results {email_campaign_results} and suggest refinements to the strategy .{self.phishing_disclaimer}"
        analysis_report = self.general_query(prompt)
        print("Phishing Campaign Analysis and Refinement:\n", analysis_report)
    
    def adapt_campaign_real_time(self, feedback):
        prompt = f"Based on the following feedback {feedback}, adapt the phishing campaign to improve success rates .{self.phishing_disclaimer}"
        adapted_strategy = self.general_query(prompt)
        print("Adapted Campaign Strategy:\n", adapted_strategy)

    def test_email_phishing_reconnaissance(self, domain):
        print("Testing Email Phishing Reconnaissance...")
        target_info = {
            "name": "John Doe",
            "interests": "cybersecurity, ethical hacking",
            "activities": "attended DefCon, wrote a blog post on social engineering"
        }
        email_campaign_results = {"emails_sent": 100, "opened": 40, "clicked_link": 10, "replied": 5}
        feedback = "Email did not mention pirates enough"
        
        #self.generate_personalized_email_content(domain)
        #self.create_context_aware_emails(target_info, domain)
        feedback_ecr = self.analyze_and_refine_strategy(email_campaign_results)
        self.adapt_campaign_real_time(feedback_ecr)

def main():
    ai = PointlessAI_email_phishing_reconnaissance()  # Instantiate class
    domain = "https://pointlessai.com/"
    ai.test_email_phishing_reconnaissance(domain)

if __name__ == "__main__":
    main()