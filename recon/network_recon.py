# IP, subdomain, network recon

import whois as whois_lib
import whois
import dns.resolver
import ipwhois
import json
import os
import sublist3r
import DNS
import dnsdumpster.DNSDumpsterAPI
from dnsdumpster.DNSDumpsterAPI import DNSDumpsterAPI
import dnslib
import tld

class DomainAnalyzer:
    def whois(self, domain):
        domain_info = whois_lib.whois(domain)
        return domain_info
         
    def python_whois(self, domain):
        w = whois.whois(domain)
        result = json.dumps(w, indent=4, default=str)
        return result

    def dnspython(self, domain):
        resolver = dns.resolver.Resolver()
        result = resolver.resolve(domain, 'A')
        return [str(ip) for ip in result]
    
    def ipwhois(self, ip):
        ip_info = ipwhois.IPWhois(ip).lookup_rdap()
        return ip_info
    
    def sublist3r(self, domain):
        if ("www" in domain):
            print("You have provided a subdomain www. Sublistr works best with top level domains.")
        subdomains = sublist3r.main(domain, 40, savefile=None, ports=None, silent=True, verbose=False, enable_bruteforce=False, engines=None)
        #return json.dumps(subdomains, indent=4)
        return subdomains
    
    def py3dns(self, domain, record_type):
        answers = dns.resolver.resolve(domain, record_type)
        return [rdata.to_text() for rdata in answers]

    def dnsdumpster(self, domain):
        result = DNSDumpsterAPI().search(domain)
        return result
    
    def tld(self, url):
        return tld.get_tld(url, fix_protocol=True)

def log_result(result, description):
    output_file = '/home/pai/code/ChatGPT/ChatGPT-for-Offensive-Security/recon/output/domain_analysis_results.txt'
    with open(output_file, 'a') as file:
        file.write(description + '\n' + str(result) + '\n\n')

def main():
    domain = 'pointlessai.com'
    analyzer = DomainAnalyzer()

    whois_result = analyzer.whois(domain)
    log_result(whois_result, 'WHOIS Information:')

    python_whois_result = analyzer.python_whois(domain)
    log_result(python_whois_result, 'Python WHOIS Information:')

    dnspython_result = analyzer.dnspython(domain)
    log_result(dnspython_result, 'DNSPython Information (A Records):')

    ip = dnspython_result[0]
    ipwhois_result = analyzer.ipwhois(ip)
    log_result(ipwhois_result, 'IPWHOIS Information:')

    sublist3r_result = analyzer.sublist3r(domain)
    log_result(sublist3r_result, 'Sublist3r Information:')

    py3dns_result = analyzer.py3dns(domain, 'A')
    log_result(py3dns_result, 'Py3DNS Information (MX Records):')

    dnsdumpster_result = analyzer.dnsdumpster(domain)
    log_result(dnsdumpster_result, 'DNSDumpster Information:')

    url = f"http://{domain}"
    tld_result = analyzer.tld(url)
    log_result(tld_result, 'TLD Extract where URL:')
  
if __name__ == "__main__":
    main()
