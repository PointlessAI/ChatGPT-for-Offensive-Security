"""
Exploiting Application Function with ChatGPT
Bypassing Security Controls
['Utilize ChatGPT to identify and strategize the bypassing of the simulated WAF. The url http://127.0.0.1:5000/vulnerabilities/xss_s/?s=%27eval(%27 is blocked by the firewall. Simulate a method to bypass this block.', 'Apply ChatGPT to generate payloads that obfuscate malicious intents from detection tools.', 'Use ChatGPT to simulate WAF evasion techniques and test their effectiveness against security measures.', 'There is a rate limit on get requests to the dvwa of 4 per 10 seconds. Define a ChatGPT method to overcome the simulated rate limiting.']
This script is for for training purposes only
"""
import requests
import sys
import os
import time
current_dir = os.path.dirname(os.path.abspath(__file__))
class_dir = os.path.join(current_dir, "..", "class")
sys.path.append(class_dir)
from dvwa_session import DVWA_Session
from chatgpt_func import ChatGPT_Func
from general_func import General_Func

class PointlessAI_bypassing_security_controls(DVWA_Session, ChatGPT_Func, General_Func):
    def __init__(self):
        DVWA_Session.__init__(self)
        ChatGPT_Func.__init__(self)
        General_Func.__init__(self)

    def bypass_waf_with_chatgpt(self, url, payload):
        # Note that this WAF is implemted using Flask. Be sure to run the code in firewall.py and then access the DVWA from port 5000.
        blocked_url = url
        prompt = f"The url {url}{payload} is blocked by a firewall. Suggest an alternative {payload} in the 's' query parameter that will allow me to execute a shell command. Format as {blocked_url} .{self.no_markdown}"
        advice = self.general_query(prompt)
        print("Bypass advice: ", advice)

    def generate_obfuscated_payloads(self,payload):
        """
        prompt = "Generate a list of obfuscated payloads to bypass detection tools."
        > Sorry unable to comply due to ethical concerns
        prompt = "List some common methods of obfsucating payloads."
        payloads = self.general_query(prompt)
        print("Obfuscated Payloads: ", payloads)
        > Returns the following:
        """
        obfuscated_methods = " \
        1. Base64 encoding: encoding the payload in Base64 format to obfuscate its content and hide its true purpose. \
        2. URL encoding: encoding special characters in the payload as hex values to evade detection by security tools. \
        3. XOR encryption: using bitwise XOR operation to encrypt the payload and make it more difficult to analyze. \
        4. ASCII encoding: converting the payload into ASCII characters to disguise its original form. \
        5. Binary encoding: converting the payload into binary format to confuse security mechanisms and bypass detection. \
        6. Custom encoding schemes: creating custom encoding algorithms to obfuscate the payload further and make it harder to analyze. \
        7. String manipulation: manipulating strings within the payload, such as adding extra characters or rearranging letters, to obfuscate its content. \
        8. JavaScript obfuscation: using techniques like minification, concatenation, and variable renaming to obfuscate JavaScript payloads and evade detection.\
        9. Shellcode obfuscation: employing techniques like polymorphism, encoding, and encryption to obfuscate shellcode payloads in memory. \
        10. Payload fragmentation: splitting the payload into smaller parts and reconstructing it at runtime to evade static analysis. \
        "
        prompt = f"Generate a python class with methods for each of the items in this list {obfuscated_methods}. \
                   The methods should take the string: {payload} as input and then perform the conversion as output. \
                   Every method should be an actual working implementation with functional code.\
                   Include a main function with examples of how to use. \
                   For items 6 - 10 get creative. Use best guess for the purpose of obfuscating date. {self.no_markdown}"

        code = self.general_query(prompt)

        filepath = "/home/kali/shellassistant/training-assistant/code/scripts"
        filename = "obfuscated_methods"
        filetype = "py"
        self.save_file(code, filepath, filename, filetype)
        obfuscated_methods = self.read_file(filepath, filename, filetype)
        print(obfuscated_methods)

    def simulate_waf_evasion(self, payload):
        """
        prompt = "Provide WAF evasion techniques and evaluate their effectiveness."
        > Sorry unable to comply due to ethical concerns
        prompt = "List some common WAF evasion techniques"
        techniques = self.general_query(prompt)
        print("WAF Evasion Techniques: ", techniques)
        > Returns the following:
        """
        evasion_methods = " \
        1. Encoding: Attackers may encode malicious payloads to bypass signature-based WAF filters. \
        2. HTTP parameter pollution: Injecting additional parameters in URLs or forms to confuse WAF filtering rules. \
        3. IP fragmentation: Sending fragmented packets to evade detection as the WAF may only inspect the first packet. \
        4. Null byte injection: Adding null bytes in the request to evade WAF filters. \
        5. Request smuggling: Sending conflicting requests in a single HTTP request to bypass WAF rules. \
        6. Obfuscation: Using techniques such as URL encoding or character substitutions to disguise malicious payloads. \
        7. Slow attack techniques: Sending requests at a slower rate to avoid triggering rate-based WAF rules. \
        8. Session fixation: Manipulating session IDs or cookies to evade WAF detection. \
        9. Binary payload attacks: Using binary data in HTTP packets to bypass WAF filters that expect only text data. \
        10. Protocol-level evasion: Exploiting vulnerabilities in the underlying network protocols to bypass WAF protections.\
        "
        prompt = f"Generate a python class with methods for each of the items in this list {evasion_methods}. \
                   The methods should take the string:  {payload} as input and then perform the conversion as output. \
                   Every method should be an actual working implementation with functional code. Import codecs and other python libraries in the script as needed. \
                   Include a main function with examples of how to use. \
                   If there is no obvious method then get creative. Use best guess for the purpose of obfuscating date. {self.no_markdown}"

        code = self.general_query(prompt)

        filepath = "/home/kali/shellassistant/training-assistant/code/scripts"
        filename = "evasion_methods"
        filetype = "py"
        self.save_file(code, filepath, filename, filetype)
        evasion_methods = self.read_file(filepath, filename, filetype)
        print(evasion_methods)

    def overcome_rate_limiting(self, s, url):
        """
        prompt = "List some common techniques used to bypass application request rate limits."
        prompt = "List some common methods used by penetration testers when they are working with rate limited applications."
        strategy = self.general_query(prompt)
        print("Strategy: ", strategy)
        > Returns the following:
        """

        bypass_methods = " \
        1. **Brute Force Attack**: Penetration testers may attempt to break the rate limit by sequentially trying different combinations of login credentials or other inputs until the correct one is found. \
        2. **Slow and Low Attacks**: Testers may deliberately send requests at a slow pace to avoid triggering the rate limit and go unnoticed. This technique is known as 'low and slow' and is used to remain under the radar while gathering information or conducting attacks. \
        3. **Interval Timing**: Penetration testers may time their requests strategically to bypass rate limits. For example, they may send requests just after the reset interval to increase the chances of success. \
        4. **Captchas**: If the application uses a captcha system to prevent automated attacks, testers may use automated captcha solvers to bypass this protection. \
        5. **IP Rotation**: Testers may leverage proxies or VPNs to rotate their IP addresses and evade rate limiting restrictions that are based on IP address. \
        6. **Session Management**: Penetration testers may exploit session management vulnerabilities to evade rate limits. By manipulating session parameters or cookies, they can bypass restrictions placed on individual user sessions. \
        7. **API Rate Limiting Bypass**: Testers may analyze the API documentation and endpoints to identify ways to manipulate request headers or parameters to bypass rate limits enforced at the API level. \
        8. **Throttling**: Penetration testers may intentionally throttle their own requests to mimic the expected behavior of a legitimate user and avoid triggering rate limits. \
        "

        prompt = f"Generate a python class with methods to implement each of the items in this list {bypass_methods}. \
                   Every method should be an actual working implementation with functional code. Import any python libraries in the script as needed. \
                   Include a main function with examples of how to use. \
                   If there is no obvious method then get creative. Use best guess for the purpose of obfuscating date. {self.no_markdown}"

        code = self.general_query(prompt)

        filepath = "/home/kali/shellassistant/training-assistant/code/scripts"
        filename = "bypass_methods"
        filetype = "py"
        self.save_file(code, filepath, filename, filetype)
        bypass_methods = self.read_file(filepath, filename, filetype)
        print(bypass_methods)

        # Simple test of rate limits
        for _ in range(4):
            try:
                response = s.get(url)
                if response.status_code == 200:
                    print("Request successfully sent.")
                    time.sleep(2)  # Adjust timing
                else:
                    print("Request blocked or rate-limited.")
            except Exception as e:
                print(e)

def main():
    ai = PointlessAI_bypassing_security_controls()  # Instantiate class
    # Start session
    with requests.Session() as s:
        user_token, cookies = ai.get_csrf_token_and_cookie(s, ai.login_url)
        login_response = ai.login_to_dvwa(s, ai.login_url, "admin", "password", user_token)
        print("Login Response Status:", login_response.status_code)

        payload = "eval("
        # Calling methods
        # Note some require Flask WAF activation. Be sure to run firewall.py and access the DVWA from port 5000
        # ai.bypass_waf_with_chatgpt(f"http://127.0.0.1:5000/vulnerabilities/xss_s/?s='",{payload}
        ai.generate_obfuscated_payloads(payload)
        ai.simulate_waf_evasion(payload)
        # ai.overcome_rate_limiting(s, "http://127.0.0.1:5000/")

if __name__ == "__main__":
    main()