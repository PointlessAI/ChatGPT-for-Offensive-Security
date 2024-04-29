"""
Reconnaissance Techniques Using ChatGPT
Domain and IP Information Gathering
['Use ChatGPT to automate queries to WHOIS databases, retrieving vital domain and IP information.', 'Develop ChatGPT-driven scripts to correlate IP ranges with potential target systems.', 'Analyze DNS information using ChatGPT to uncover subdomains and related IPs.', 'Utilize ChatGPT to interpret scan results and prioritize targets based on gathered domain information.']
This script is for training purposes only
"""
import requests
import whois
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
class_dir = os.path.join(current_dir, "..", "class")
sys.path.append(class_dir)

from chatgpt_func import ChatGPT_Func
from general_func import General_Func

class PointlessAI_domain_and_ip_information_gathering(ChatGPT_Func, General_Func):
    def __init__(self):
        ChatGPT_Func.__init__(self)
        General_Func.__init__(self)

    def whois_lookup(self, domain):
        print(f"Performing traditional WHOIS lookup for domain: {domain}")
        try:
            domain_info = whois.whois(domain)
            return domain_info
        except Exception as e:
            print(f"An error occurred during the WHOIS lookup: {e}")
            return None
        
    def chatgpt_whois_lookup(self,domain):
        prompt = f"List 10 common python packages that can be used to gather domain information without an API key. key is domain_tools and this should contain an array of tools."
        domain_tools = self.json_query(prompt)
        print(domain_tools)

        prompt = f"Your role is to gather as much information as possible on the target domain. \
                Generate a python class with methods for each of the tools in the JSON array {domain_tools}. \
                The methods should take a domain as input and then perfom domain analysis on the domain. \
                Every method should be an actual working implementation with functional code.\
                Include a main function with examples of how to use. Output from examples should include a description of the result and then appended to to file.  \
                If you are unsure how to implement the tool then get creative. Use best guess in implelementing the tool to gather domain information. {self.no_markdown}"
        domain_info = self.general_query(prompt)
        filepath = "/home/kali/shellassistant/training-assistant/code/scripts"
        filename = f"{domain}-domain-info"
        filetype = "py"
        self.save_file(domain_info, filepath, filename, filetype)
        domain_info_aggregate = self.read_file(filepath, filename, filetype)
        print(domain_info_aggregate)

    def chatgpt_dns_analysis(self, domain):
        # First run script you created in chatgpt_whois_lookup method.
        aggregated_domain_info = self.read_file("/home/kali/shellassistant/training-assistant/code/recon", "domain_analysis_results", "txt")
        print(aggregated_domain_info)
        print(self.general_query(f"Provide a summary of the company based on {aggregated_domain_info}"))

def main():
    ai = PointlessAI_domain_and_ip_information_gathering()  # Instantiate class
    # Use case examples (Replace <your_domain> and <your_ip_range> with actual values)
    domain = "pointlessai.com"
    ip_range = "10.0.2.0/24"
    scan_results = "Sample scan results"

    # Conduct domain and IP information gathering
    # domain_details = ai.whois_lookup(domain); print(domain_details)
    # cgpt_domain_details = ai.chatgpt_whois_lookup(domain); print(cgpt_domain_details)
    #ai.traditional_ip_correlation(ip_range)
    #ai.chatgpt_ip_correlation(ip_range)
    #ai.traditional_dns_analysis(domain)
    ai.chatgpt_dns_analysis(domain)
    #ai.traditional_scan_interpretation(scan_results)
    #ai.chatgpt_scan_interpretation(scan_results)
    #ai.demonstrate_dvwa_interaction()

if __name__ == "__main__":
    main()
