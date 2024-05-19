"""
ChatGPT Prompt Tone and Style
Crafting Precise Prompts
['Precision in Language: The importance of carefully selected words to elicit desired information or actions from ChatGPT.', "Contextual Framing: How to frame prompts to align with ChatGPT's understanding for offensive cybersecurity tasks.", 'Example Scenarios: Demonstrating effective prompt crafting to automate crafting of deceptive messages or cybersecurity reports.']
This script is for for training purposes only
"""
import requests
import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
class_dir = os.path.join(current_dir, "..", "class")
sys.path.append(class_dir)
from chatgpt_func import ChatGPT_Func
from general_func import General_Func

class PointlessAI_crafting_precise_prompts(ChatGPT_Func, General_Func):
    def __init__(self):
        ChatGPT_Func.__init__(self)         
        General_Func.__init__(self)

    def demonstrate_precise_language(self, csp):
        guidance = self.phishing_disclaimer
        prompt = f"Precision in Language: Generate a ChatGPT prompt that demonstrates the importance of carefully selected wording and precision. \
                   Your objective is to analyse the following content security policy for vulnerabilities: {csp}."
        response = self.red_team_query(prompt, guidance)
        return(response)
    
    def precise_prompt(self, prompt):
        guidance = f"Generate a ChatGPT prompt based on the provided prompt: {prompt} - the new prompt should be more sophisticated in it's design, paying attention to \
                    precision, clarity, style and tone to achieve it's objective. The prompt should generate an advanced level python script."
        response = self.red_team_query(prompt, guidance)
        return(response)
    
    def execute_prompt(self, res):
        guidance = self.no_markdown
        prompt = res
        response = self.red_team_query(prompt, guidance)
        print(f"\n-------------------------\nPROMPT: {prompt}\n-------------------------\n{response}")
        return(response)

def main():
    ai = PointlessAI_crafting_precise_prompts()

    csp = "Content-Security-Policy: default-src 'self'; img-src 'self' cdn.example.com;"
    res = ai.demonstrate_precise_language(csp)
    # Inprecise Prompt
    ai.execute_prompt(f"Your objective is to analyse the following content security policy for vulnerabilities: {csp}.")
    """
    Your objective is to analyse the following content security policy for vulnerabilities: Content-Security-Policy: default-src 'self'; img-src 'self' cdn.example.com;
    """
    # OUTPUT
    """
    Here is the analysis of the Content Security Policy provided:
    1. default-src 'self': This directive sets the default policy for loading content on the website to only be allowed from the same origin ('self'). This helps to prevent data from being loaded from external sources unless explicitly allowed.
    2. img-src 'self' cdn.example.com: This directive specifies that images can be loaded from the same origin ('self') as well as from the cdn.example.com domain. This allows images to be loaded from the specified domain in addition to the originating website.

    Potential vulnerability:
    - One potential vulnerability in this CSP is that only the 'cdn.example.com' domain is whitelisted for image sources. If an attacker manages to compromise the CDN domain, they could potentially serve malicious images to users.

    Recommendation:
    - To enhance security, it is recommended to include additional specific domains that are trusted to serve images. This would reduce the risk of a single domain compromise leading to a successful attack.
    - It is also a good practice to implement various other directives such as script-src, style-src, and connect-src to further restrict the loading of resources. 

    Overall, the provided CSP is a good baseline but can be strengthened by adding more specific directives and domain whitelisting to enhance security.
    """
    # Precise prompt generated by ChatGPT
    ai.execute_prompt(res)
    """
    Your objective is to analyse the following content security policy for vulnerabilities: Content-Security-Policy: default-src 'self'; img-src 'self' cdn.example.com;
    In discussions concerning security, precision is pivotal. Analyzing the provided Content Security Policy, 
    certain elements necessitate a closer examination. The designated 'default-src' specifies content sources considered trusted ('self' is restricted to the same origin). 
    However, we must scrutinize the declaration of 'img-src' to cdn.example.com.
    """
    # OUTPUT:
    """
    Penetration Testing Scenario:
    As part of your security assessment, you have identified a potential security vulnerability in the Content Security Policy (CSP) of a web application. During your analysis of the CSP header, you noticed the following directive:

    Content-Security-Policy: default-src 'self'; img-src 'self' cdn.example.com;

    Upon reviewing this CSP configuration, you have observed that the img-src directive allows resources to be loaded from the 'self' origin and cdn.example.com. While this might seem sufficient at first glance, there is a critical oversight in the way the CDN domain is specified.

    The lack of an explicit protocol (http:// or https://) before the cdn.example.com domain in the img-src directive leaves the application vulnerable to potential security risks. This implies that any subresource loaded from cdn.example.com, regardless of the protocol used, would be allowed by the CSP. An attacker could potentially exploit this situation by serving malicious content over HTTP or employing other protocol manipulation techniques.

    To enhance the security posture of the application and mitigate such risks, it is imperative to include the appropriate protocol in the CSP directive. By explicitly defining the protocol in the img-src directive for cdn.example.com, such as 'img-src https://cdn.example.com', you can enforce a more granular level of control and prevent mixed-content vulnerabilities effectively.

    In conclusion, the precision and clarity of language in defining security policies, such as CSP directives, play a pivotal role in strengthening the security defenses of web applications. By paying attention to details like specifying protocols and origins accurately, we can fortify our defenses against common attack vectors and ensure a robust security posture.
    To test the security vulnerability arising from the lack of an explicit protocol in the CSP directive for cdn.example.com, you could follow these steps:

    1. Craft a malicious content or payload that can be delivered over HTTP to cdn.example.com or via any other protocol.
    2. Inject this payload into the web application and trigger a request for the resource from cdn.example.com.
    3. While the request is made and the resource is loaded, monitor if the content is allowed by the CSP due to the oversight in specifying the protocol for cdn.example.com in the img-src directive.
    4. Evaluate whether the application processes and displays the resource loaded from cdn.example.com despite the absence of a secure protocol (https://) in the CSP directive.
    5. Document any successful loading of the malicious content and assess the impact it could have on the security of the web application, such as the introduction of mixed-content vulnerabilities.

    By simulating this attack scenario and demonstrating how the lack of an explicit protocol in the CSP directive can lead to security risks, you can provide valuable insights to the red team about the importance of accurately defining and enforcing content security policies.

    """


if __name__ == "__main__":
    main()