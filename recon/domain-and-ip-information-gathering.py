"""
Reconnaissance Techniques Using ChatGPT
Domain and IP Information Gathering
Learning objectives: Use ChatGPT to automate queries to WHOIS databases, retrieving vital domain and IP information,
develop ChatGPT-driven scripts to correlate IP ranges with potential target systems, analyze DNS information using ChatGPT
to uncover subdomains and related IPs, and utilize ChatGPT to interpret scan results and prioritize targets based on gathered
domain information.
This script is for training purposes only.
"""

import socket
import whois
from openai import OpenAI
import os
from dotenv import load_dotenv, find_dotenv

# Load the environment variable from .env file
_ = load_dotenv(find_dotenv())

# Initialize OpenAI client with API key
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

class DomainInfoGatherer:
    def __init__(self, domain):
        self.domain = domain

    def get_whois_info(self):
        try:
            domain_info = whois.whois(self.domain)
            return domain_info.text
        except Exception as e:
            return str(e)

    def get_dns_records(self):
        try:
            records = socket.gethostbyname_ex(self.domain)
            return records
        except Exception as e:
            return str(e)

    def analyze_information(self, info):
        prompt = f"Analyze the following information and provide insights and possible implications for cybersecurity: {info}"
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": prompt},
            ],
            temperature=1,
            max_tokens=350,
            top_p=1
        )
        return response.choices[0].message.content

# Example usage:
domain = "pointlessai.com"
gatherer = DomainInfoGatherer(domain)
whois_info = gatherer.get_whois_info()
dns_info = gatherer.get_dns_records()
analyzed_whois = gatherer.analyze_information(whois_info)
analyzed_dns = gatherer.analyze_information(str(dns_info))

print("WHOIS Information Analysis: ", analyzed_whois)
print("DNS Information Analysis: ", analyzed_dns)
