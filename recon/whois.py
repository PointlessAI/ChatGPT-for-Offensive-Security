"""
Domain and IP Information Gathering
Demo Python script that illustrates how to automate the process of querying WHOIS databases for domain and IP information
correlating IP ranges with potential target systems, 
analyzing DNS information to uncover subdomains and related IPs
using ChatGPT to interpret scan results to prioritize targets.
This script is for for training purposes only
"""

"""
Prerequisites:
# Create virtual Python environment
python -m venv exp-venv
python source exp-venv/bin/activate
# Install dependencies
python -m pip install --upgrade -r requirements.txt
"""

"""
SUBDOMAIN resources
# Enumeration tools
python -m pip install anubis-netsec
    anubis -t pointlessai.com
git clone https://github.com/aboul3la/Sublist3r.git
    python sublist3r.py -d pointlessai.com
nmap --script dns-brute [domain]
# Wordlists
wget -r --no-parent -R "index.html*" -e robots=off https://wordlists-cdn.assetnote.io/data/ -nH
https://gist.github.com/jhaddix/86a06c5dc309d08580a018c66354a056
https://github.com/danielmiessler/SecLists
https://github.com/danielmiessler/SecLists/blob/master/Discovery/DNS/subdomains-top1million-110000.txt
"""


import dns.resolver
from openai import OpenAI
import whois
import os

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

client = OpenAI(
   api_key=os.environ.get("OPENAI_API_KEY"),
 )

def query_whois(domain):
    try:
        domain_info = whois.whois(domain)
        return domain_info
    except Exception as e:
        return f"Error retrieving WHOIS data: {str(e)}"

# DNS and Subdomain Analysis
def find_subdomains(domain, subdomain_list):
    found_subdomains = []
    for subdomain in subdomain_list:
        try:
            addresses = dns.resolver.resolve(f"{subdomain}.{domain}", "A")
            for ip in addresses:
                found_subdomains.append(f"{subdomain}.{domain} resolves to {ip}")
        except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
            continue
    return found_subdomains

# IP Range Correlation (Pseudocode)
def correlate_ip_ranges(ip_ranges, known_data):
    # This function would compare known IP ranges with any gathered or known information
    # about potential targets. This might involve querying additional databases,
    # cross-referencing with known vulnerabilities, etc.
    pass

# Interpreting Scan Results with ChatGPT
def analyze_scan_results_with_chatgpt(scan_results):
    message = f"Given these scan results, how should we prioritize our targets?\n\n{scan_results}"
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": message},
        ],
        temperature=0.5,
        max_tokens=1024,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    target_domain = "pointlessai.com" #input("Enter a target domain E.G. pointlessai.com: ")
    target_domain = "https://"+target_domain
    print(f"Gathering domain information for: {target_domain}")
    
    domain_info = query_whois(target_domain)
    print(domain_info)

    #subdomain_list=["mail","www","smtp","test"]
    #subdomain_info = find_subdomains(target_domain, subdomain_list)
    #print(subdomain_info)