import os
import json
import whois
import dns.resolver
import pycares
import tldextract
import dns.resolver
import whois
import sublist3r
import nmap
import scapy.all as scapy

class DomainAnalysis:
    
    def whois_info(self, domain):
        w = whois.whois(domain)
        result = json.dumps(w, indent=4, default=str)
        return result
    
    def dns_resolver_info(self, domain):
        resolver = dns.resolver.Resolver()
        result = resolver.resolve(domain)
        records = []
        for rdata in result:
            records.append(str(rdata))
        return json.dumps(records, indent=4)
    
    def tldextract_info(self, domain):
        extracted = tldextract.extract(domain)
        result = {
            'subdomain': extracted.subdomain,
            'domain': extracted.domain,
            'suffix': extracted.suffix
        }
        return json.dumps(result, indent=4)
    
    def dnspython_info(self, domain):
        dns_records = dns.resolver.resolve(domain, 'A')
        records = [r.to_text() for r in dns_records]
        return json.dumps(records, indent=4)
    
    def python_whois_info(self, domain):
        w = whois.whois(domain)
        result = json.dumps(w, indent=4, default=str)
        return result
    
    def sublist3r_info(self, domain):
        subdomains = sublist3r.main(domain, 40, savefile=None, ports=None, silent=True, verbose=False, enable_bruteforce=False, engines=None)

        return json.dumps(subdomains, indent=4)
    
    def python_nmap_info(self, domain):
        nm = nmap.PortScanner()
        nm.scan(domain)
        result = {host: nm[host] for host in nm.all_hosts()}
        return json.dumps(result, indent=4, default=str)
    
    def scapy_info(self, domain):
        ans, unans = scapy.arping(domain)
        result = []
        for send, rcv in ans:
            json_obj = {'send': send.show(dump=True), 'receive': rcv.show(dump=True)}
            result.append(json_obj)
        return json.dumps(result, indent=4)
    
def main():
    domain = 'pointlessai.com'
    analysis = DomainAnalysis()
    
    results = {}
    results['whois'] = analysis.whois_info(domain)
    results['dns_resolver'] = analysis.dns_resolver_info(domain)
    results['tldextract'] = analysis.tldextract_info(domain)
    results['dnspython'] = analysis.dnspython_info(domain)
    results['python_whois'] = analysis.python_whois_info(domain)
    results['sublist3r'] = analysis.sublist3r_info(domain)
    #results['python_nmap'] = analysis.python_nmap_info(domain)
    #results['scapy'] = analysis.scapy_info(domain)
    
    with open('/home/kali/shellassistant/training-assistant/offensive-security-chatgpt/recon/output/domain_analysis_results.txt', 'w') as outfile:
        descriptions = {
            'whois': 'WHOIS lookup information',
            'dns_resolver': 'DNS resolver information',
            'pycares': 'pycares resolver information',
            'tldextract': 'TLD extract information',
            'dnspython': 'dnspython resolvers',
            'python_whois': 'python-whois information',
            'sublist3r': 'Subdomain enumeration',
            'python_nmap': 'Port scan results',
            'requests_html': 'Website HTML content',
            'scapy': 'Scapy ARP response'
        }

        for key, value in results.items():
            outfile.write(f'{descriptions[key]}:\n')
            outfile.write(value + '\n\n')
            
if __name__ == "__main__":
    main()
