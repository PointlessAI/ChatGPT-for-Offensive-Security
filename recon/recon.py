"""
Reconnaissance with ChatGPT
Python script demo focusing on automating the collection of public domain information about a target. 
Objective is to demonstrate how ChatGPT can aid in the reconnaissance phase of offensive cybersecurity.
    Interact with various APIs to gather public domain information.
    Use ChatGPT to summarize findings.
    Demonstrate how to prepare data for potential ethical social engineering simulations.
This script is for for training purposes only
"""

"""
Prerequisites:
# Create virtual Python environment
python -m venv exp-venv
python source exp-venv/bin/activate
# Install dependencies
python -m pip install --upgrade -r /setup/requirements.txt
"""

from urllib.parse import urlparse
from bs4 import BeautifulSoup
from openai import OpenAI
import requests
import whois
import json
import os

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

client = OpenAI(
   api_key=os.environ.get("OPENAI_API_KEY"),
 )

def get_site_meta(url):
    # Fetches website metadata based on the given URL.
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
          
            # Fetch site title
            title = soup.find('title').text if soup.find('title') else 'No title found'
            
            # Fetch meta description
            description = soup.find('meta', attrs={'name': 'description'})
            description = description['content'] if description else 'No description found'
            
            # Fetch other meta tags as needed
            # For example, keywords
            keywords = soup.find('meta', attrs={'name': 'keywords'})
            keywords = keywords['content'] if keywords else 'No keywords found'
            
            return {
                'title': title,
                'description': description,
                'keywords': keywords,
            }
    except Exception as e:
        print(f"Error fetching site metadata: {e}")
        return {}

def summarize_text(text):
    # Utilize ChatGPT to summarize the collected data.
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Summarize this text:\n\n" + str(text)},
        ],
        temperature=0.7,
        max_tokens=250,
        top_p=1.0
    )
    return response.choices[0].message.content

def get_site_info(domain):
    # Crawl the site with beautiful soup and return title, des and key words
    metadata = get_site_meta(domain)
    print("Site Metadata:")
    dict_str = json.dumps(metadata)
    return metadata

def craft_social_engineering_attack(summary):
    # Craft social engineering attack
    message = f"Based on this information, suggest a social engineering attack vector:\n\n{summary}"
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": message},
        ],
        temperature=0.7,
        max_tokens=100,
        top_p=1.0,
        frequency_penalty=0.5,
        presence_penalty=0.0
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    # Script entry point
    target_domain = input("Enter a target domain E.G. pointlessai.com: ")
    target_domain = "https://"+target_domain
    print(f"Gathering company information for: {target_domain}")
    company_info = get_site_info(target_domain)

    print("Title: " + company_info["title"])
    print("Description: " + company_info["description"])
    print("Keywords: " + company_info["keywords"])
    
    summary = summarize_text(company_info)
    print(f"\nCompany Overview:\n{summary}")
    
    social_engineering_idea = craft_social_engineering_attack(summary)
    print(f"\nReccomended Social Engineering Attack:\n{social_engineering_idea}")

                                                                                                                                                      
""" 
SAMPLE OUTPUT >

Gathering company information for: https://pointlessai.com
Title: PointlessAI
Description: PointlessAI is a cybersecurity research company focused on the application of AI within ethical hacking research.
Keywords: AI, Ethical hacking, cybersecurity, security research, bug bounty, vdp

Company Overview:
PointlessAI is a cybersecurity research company specializing in using AI for ethical hacking research. They focus on security research, bug bounty programs, and vulnerability disclosure programs.

Reccomended Social Engineering Attack:
One potential social engineering attack vector could involve sending phishing emails to PointlessAI employees pretending to be from a well-known bug bounty program or security research organization. 
The email could contain a malicious attachment or link that, when clicked, could compromise the company's network or steal sensitive information. 
Since PointlessAI is involved in bug bounty and vulnerability disclosure programs, employees may be more likely to engage with such emails thinking it is related to their area of expertise.

"""