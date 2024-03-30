"""
Get subdomains
Python script demo to obtain a list of subdomains from a target.
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

import requests
import re

def get_subdomains_from_crt(domain):
    # Fetch subdomains from crt.sh
    url = f"https://crt.sh/?q=%.{domain}&output=json"
    try:
        resp = requests.get(url)
        if resp.status_code != 200:
            print(f"Error fetching data from crt.sh: HTTP {resp.status_code}")
            return []

        # Parse JSON response
        data = resp.json()
        if not data:
            print("No data found for domain.")
            return []

        # Extract subdomains
        subdomains = set()
        for entry in data:
            name_value = entry.get("name_value")
            if name_value:
                # Split by newlines and remove wildcard entries
                found_subdomains = [name.strip() for name in name_value.split('\n') if '*' not in name]
                subdomains.update(found_subdomains)

        return list(subdomains)

    except requests.RequestException as e:
        print(f"Request failed: {e}")
    except ValueError as e:
        print(f"Error processing response: {e}")
    return []

def save_subdomains(domain,subdomains):
    # Save subdomains to file.
    filename=f"{domain}-subdomains.txt"
    with open(filename, 'w') as file:
        for subdomain in subdomains:
            file.write(f"{subdomain}\n")
    print(f"Saved {len(subdomains)} subdomains to {filename}")

if __name__ == "__main__":
    target_domain = "pointlessai.com"  # input("Enter target domain: ")
    subdomains = get_subdomains_from_crt(target_domain)
    if subdomains:
        print(f"Found {len(subdomains)} subdomains for {target_domain}")
        save_subdomains(target_domain,subdomains)
    else:
        print("No subdomains found.")