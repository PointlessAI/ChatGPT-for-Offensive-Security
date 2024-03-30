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
python -m pip install --upgrade -r /setup/requirements.txt
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
    dns_fail = 0
    for subdomain in subdomain_list:
        try:
            addresses = dns.resolver.resolve(f"{subdomain}.{domain}", "A")
            for ip in addresses:
                found_subdomains.append(f"{subdomain}.{domain} resolves to {ip}")
        except (dns.resolver.LifetimeTimeout, dns.resolver.NXDOMAIN, dns.resolver.Timeout, dns.resolver.NoAnswer):
            print(f"DNS resolution error {dns_fail+1}/3")
            dns_fail += 1
            if dns_fail > 2:
                return 3
            continue
        except Exception as e:
            print("An unexpected error occurred:", e)
            continue

    return found_subdomains

# IP Range Correlation (Not yet implemented)
def correlate_ip_ranges(ip_ranges, known_data):
    # Compare known IP ranges with any gathered or known information
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
    target_domain = "opnx.com" #input("Enter a target domain E.G. pointlessai.com: ")
    #target_domain = "https://"+target_domain
    print(f"Gathering domain information for: {target_domain}")
    
    #domain_info = query_whois(target_domain)
    #print(domain_info)

    # Open the wordlist file
    with open('../wordlists/subdomains.txt', 'r') as file:
        wordlist_array = file.readlines()
    subdomain_list = [word.strip() for word in wordlist_array]

    subdomain_list = [
        "www", "mail", "remote", "blog", "webmail", "server",
        "ns1", "ns2", "smtp", "secure", "vpn", "m", "shop",
        "ftp", "mail2", "test", "portal", "ns", "ww1", "host",
        "support", "dev", "web", "bbs", "ww42", "mx", "email",
        "cloud", "1", "mail1", "2", "forum", "owa", "www2", "gw",
        "admin", "store", "mx1", "cdn", "api", "exchange", "app",
        "gov", "2tty", "vps", "govyty", "hgfgdf", "news"
    ]

    subdomain_info = find_subdomains(target_domain, subdomain_list)
    if (subdomain_info == 3):
        print("DNS failed. Trying alternative...")
    else: 
        print(subdomain_info)