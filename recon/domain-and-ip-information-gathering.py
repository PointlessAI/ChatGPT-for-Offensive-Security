"""
Reconnaissance Techniques Using ChatGPT
Domain and IP Information Gathering
['Use ChatGPT to automate queries to WHOIS databases, retrieving vital domain and IP information.', 
'Analyze DNS information using ChatGPT to uncover subdomains and related IPs.', 
'Utilize ChatGPT to interpret scan results and prioritize targets based on gathered domain information.']
This script is for training purposes only
"""

"""
Running this script will produce a new file called network_recon.py - this file is available in current directory.
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
        # Traditional whois lookup demo
        print(f"Performing traditional WHOIS lookup for domain: {domain}")
        try:
            domain_info = whois.whois(domain)
            return domain_info
        except Exception as e:
            print(f"An error occurred during the WHOIS lookup: {e}")
            return None
        
    def chatgpt_whois_lookup(self,domain):
        # ChatGPT generated domain recon script
        # First generate a list of domain tools
        prompt = f"List 10 common python packages that can be used to gather domain information without an API key. \
                key is domain_tools and this should contain an array of tools."
        # Function called from chatgpt_func class. Calls ChatGPT and returns JSON
        domain_tools = self.json_query(prompt)
        print(domain_tools)
        # Generate a script that uses the provided domain tools to perform multifaceted domain recon
        prompt = f"Your role is to gather as much information as possible on the target domain. \
                Generate a python class with methods for each of the tools in the JSON array {domain_tools}. \
                The methods should take a domain as input and then perfom domain analysis on the domain. \
                Every method should be an actual working implementation with functional code.\
                Include a main function with examples of how to use. Output from examples should include a description of the result and then appended to to filename: domain_analysis_results.txt in filepath: {self.recon_dir}/output/.  \
                If you are unsure how to implement the tool then get creative. Use best guess in implelementing the tool to gather domain information. {self.no_markdown}"
        domain_info = self.general_query(prompt)
        filepath = f"{self.home_dir}/output"
        filename = f"{domain}_network_recon"
        filetype = "py"
        # Function called from general_func class to save file
        self.save_file(domain_info, filepath, filename, filetype)
        domain_info_aggregate = self.read_file(filepath, filename, filetype)
        print(domain_info_aggregate)
        # Now run generated script

    def chatgpt_dns_analysis(self, domain):
        # First run script you created in chatgpt_whois_lookup method.
        # Function called from general_func class to read file
        aggregated_domain_info = self.read_file(f"{self.recon_dir}/output", "domain_analysis_results", "txt")
        domain_summary = self.general_query(f"Provide a summary of the company based on {aggregated_domain_info}")
        self.save_file(domain_summary, f"{self.recon_dir}/output", "domain_analysis_summary", "md")

def main():
    ai = PointlessAI_domain_and_ip_information_gathering()

    domain = "www.ampol.com.au"

    # Create analysis files if not exist
    if not os.path.exists(f"{ai.recon_dir}/output/domain_analysis_results.txt"): 
        with open(f"{ai.recon_dir}/output/domain_analysis_results.txt", 'w') as file: 
            file.write("") 
    if not os.path.exists(f"{ai.recon_dir}/output/domain_analysis_summary.txt"): 
        with open(f"{ai.recon_dir}/output/domain_analysis_summary.txt", 'w') as file: 
            file.write("") 

    """
    How to use:
    set domain variable
    Run chatgpt_whois_lookup
    This will create a script within scripts dir
    Run generated script (not set to auto run as often has import errors)
    Then run chatgpt_dns_analysis method to aggregate data
    """

    # Conduct domain and IP information gathering
    # domain_details = ai.whois_lookup(domain); print(domain_details) # whois_lookup function is to demo traditional methods for training example only
    #cgpt_domain_details = ai.chatgpt_whois_lookup(domain); print(cgpt_domain_details)
    
    # After running scripts then execute:
    ai.chatgpt_dns_analysis(domain)

if __name__ == "__main__":
    main()
