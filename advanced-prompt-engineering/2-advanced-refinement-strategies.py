"""
ChatGPT for offensive cybersecurity
Advanced refinement strategies
['Multi-stage prompting: Develop prompts that build on each other to guide ChatGPT through complex attack scenarios.', 'Conditional logic: Incorporate conditional logic into prompts to handle varying outcomes or responses.', "Contextual embedding: Use contextual cues within prompts to enhance ChatGPT's understanding of the task."]
This script is for for training purposes only
"""
import subprocess
import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
class_dir = os.path.join(current_dir, "..", "class")
sys.path.append(class_dir)
from chatgpt_func import ChatGPT_Func
from general_func import General_Func

class PointlessAI_advanced_refinement_strategies(ChatGPT_Func, General_Func):
    def __init__(self):
        ChatGPT_Func.__init__(self)
        General_Func.__init__(self)

    def nmap_assistant(self, prompt):
        # Formulate the prompt to generate the nmap scan command
        nmap_command = self.red_team_query(prompt, self.no_markdown)  # Assume this function returns a valid command

        print(f"Stage 1 nmap_scan command: {nmap_command}")

        try:
            # Execute the nmap command using subprocess
            sudo_command = f"sudo {nmap_command}"
            result = subprocess.run(sudo_command, shell=True, text=True, capture_output=True)
            # Check if the command was executed successfully
            if result.returncode == 0:
                # Print and return the standard output of the command
                print(f"Scan results: {result.stdout}")
                return result.stdout
            else:
                # Print and return the standard error if the command failed
                print(f"Error in scanning: {result.stderr}")
                return result.stderr
        except Exception as e:
            # Print and return the error if an exception occurred during command execution
            print(f"Execution error: {str(e)}")
            return str(e)
        
    def conditional_logic(self, nmap_res):
        # Conditional logic to proceed based on stage 1 outcomes

        prompt = f""" \
        Given the following rules, respond to the output result below:

        Rules:
        Return only the text in backticks E.G. return only  ```text```
        1. If port 22 is open then return ```Attacking port 22```
        2. If port 21 is open then return ```Attacking port 21```
        3. If no ports are open then return ```No attack here```

        Output result from nmap: 
        {nmap_res}
        
        """
        prompt = prompt + "\nRespond base on the rules."
        guidance = self.red_team_query(prompt, self.phishing_disclaimer)
        print(f"Conditional logic outcome: {guidance}")
        return guidance

    def phish_me(self, logic):
        # Contextual embedding for deeper understanding
        context = f"Using the identified vulnerabilities in {logic}, craft a spear-phishing attack targeting the system administrators."
        prompt = f"Given the context: {context}, create a phishing email scenario."
        guidance = self.red_team_query(prompt, self.phishing_disclaimer)
        print(f"Stage 3 Guidance: {guidance}")
        # ...Logic to simulate sending the email or next steps in the scenario

    def demonstrate_advanced_strategies(self, target_url):
        print(f"Targeting: {target_url}")
        nmap_prompt = "nmap scan showing open ports - fast but stealthy" # Describe your dream nmap scan here
        prompt = f"Output a terminal command for an {nmap_prompt} on the target url: {target_url}"
        nmap_res = self.nmap_assistant(prompt)
        logic = self.conditional_logic(nmap_res)
        self.phish_me(logic)

def main():
    ai = PointlessAI_advanced_refinement_strategies() # Instantiate class
    target_url = "http://pointlessai.com/"
    ai.demonstrate_advanced_strategies(target_url)

if __name__ == "__main__":
    main()
