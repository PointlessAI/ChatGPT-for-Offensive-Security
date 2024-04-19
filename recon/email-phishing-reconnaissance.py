"""
Reconnaissance Techniques Using ChatGPT
Email Phishing Reconnaissance
This script is for training purposes only

Objectives:
1. Craft phishing campaigns with ChatGPT by generating personalized email content that increases engagement rates.
2. Utilize ChatGPT to create context-aware phishing emails based on the target's public interests and activities.
3. Implement ChatGPT to analyze the effectiveness of different phishing approaches and refine strategies.
4. Apply ChatGPT's feedback to adapt phishing campaigns in real-time, improving success rates.
"""

import os
from openai import OpenAI
from dotenv import load_dotenv, find_dotenv

# Loading API key from .env file
load_dotenv(find_dotenv())
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

class EmailPhishing:
    def __init__(self, target):
        self.target = target
        self.templates = {
            'interests': "Dear {name},\n\nAs someone who is passionate about {interest}, we thought you might enjoy...",
            'activity': "Hello {name},\n\nWe saw your recent participation in {activity} and wanted to reach out..."
        }

    def generate_email_content(self, template_type, context):
        """
        Use ChatGPT to generate personalized email content based on a chosen template and provided context.
        """
        template = self.templates.get(template_type, "")
        filled_template = template.format(**context)
        
        prompt = f"Improve this phishing email to make it more engaging and personalized: {filled_template}"
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": prompt},
            ],
            temperature=0.7,
            max_tokens=150,
            top_p=1
        )
        return response.choices[0].message.content

    def analyze_and_refine(self, email_content):
        """
        Analyze the effectiveness of a phishing email and suggest improvements.
        """
        prompt = f"How can this phishing email be improved for higher engagement and effectiveness? {email_content}"
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": prompt},
            ],
            temperature=0.7,
            max_tokens=200,
            top_p=1
        )
        return response.choices[0].message.content

def main():
    target_info = {'name': 'Jane Smith', 'interest': 'cybersecurity', 'activity': 'recent cybersecurity conference'}
    phishing = EmailPhishing(target="PointlessAI")
    
    # Generate context-aware email content
    interest_email = phishing.generate_email_content('interests', target_info)
    activity_email = phishing.generate_email_content('activity', target_info)
    
    print("Generated Email (Interest-based):", interest_email)
    print("Generated Email (Activity-based):", activity_email)
    
    # Analyze and refine email content
    refined_interest_email = phishing.analyze_and_refine(interest_email)
    refined_activity_email = phishing.analyze_and_refine(activity_email)
    
    print("Refined Email (Interest-based):", refined_interest_email)
    print("Refined Email (Activity-based):", refined_activity_email)

if __name__ == "__main__":
    main()