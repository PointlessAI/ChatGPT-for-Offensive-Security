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
import requests
import whois
import os
import socket
import json

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

client = OpenAI(
   api_key=os.environ.get("OPENAI_API_KEY"),
 )

def get_ip_address(domain, timeout=5):
    try:
        resolver = dns.resolver.Resolver()
        resolver.timeout = timeout
        resolver.lifetime = timeout
        answers = resolver.resolve(domain, 'A')
        return answers[0].address
    except dns.resolver.NoAnswer:
        print("No IP address found for the domain.")
        return None
    except dns.exception.Timeout:
        print("DNS resolution timed out.")
        return None

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
                found_subdomains.append(f"{ip}")
        except (dns.resolver.LifetimeTimeout, dns.resolver.NXDOMAIN, dns.resolver.Timeout, dns.resolver.NoAnswer):
            dns_fail += 1
            print(f"DNS resolution error. Attempt {dns_fail}/3")
            if dns_fail > 0:
                return 3
            continue
        except Exception as e:
            print("An unexpected error occurred:", e)
            continue

    return found_subdomains

def find_subdomains_fallback(domain):
    url = f"https://jldc.me/anubis/subdomains/{domain}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            # The API returns a list of subdomains
            subdomains = response.json()
            return subdomains
        else:
            print(f"Failed to fetch subdomains. Status code: {response.status_code}")
            return []
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return []

# IP Range Correlation (Not yet implemented)
def correlate_ip_ranges(ip_ranges, known_data):
    # Compare known IP ranges with any gathered or known information
    pass

# Interpreting Scan Results with ChatGPT
def analyze_scan_results_with_chatgpt(scan_results):
    message = f"Given these scan results, return a json object with key named: unip that contains an array of unique IPs\n\n{scan_results}"
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        response_format={ "type": "json_object" },
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
    target_domain = "boxchilli.com" #input("Enter a target domain E.G. pointlessai.com: ")
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

    print(f"Querying Anubis-DB for subdomains of: {target_domain}")
    subdomain_info = find_subdomains_fallback(target_domain)
    fallback_sublist = []
    if (subdomain_info == 3):
        print("DNS failed. No subdomains found.")
    else:
        print(f"Found {len(subdomain_info)} subdomains:")
        for subdomain in subdomain_info:
            timeout_seconds = 3
            ip_address = get_ip_address(subdomain, timeout_seconds)
            if ip_address:
                fallback_sublist.add(ip_address)
            else:
                print(f"Unable to resolve the IP address of {subdomain}")

    subdomain_info = find_subdomains(target_domain, subdomain_list)
    if (subdomain_info == 3):
        print("DNS failed. No subdomains found.")
    else: 
        sublist.append(subdomain_info)

    sublist.append(subdomain_info)
    #analysis = analyze_scan_results_with_chatgpt(subdomain_info)
    #analysis = json.loads(analysis)
    #print(analysis["unip"])
    print(type(sublist))
    print(sublist)
    print(type(subdomain_info))
    print(subdomain_info)
    print("\n")
    unique_list = list(dict.fromkeys(subdomain_info))
    print(unique_list)