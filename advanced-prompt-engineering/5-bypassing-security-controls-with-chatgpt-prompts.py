"""
ChatGPT for offensive cybersecurity
bypassing-security-controls-with-chatgpt-prompts
Bypassing Security Controls with ChatGPT Prompts": ["Engineering prompts to probe and understand security controls without detection.", "Crafting prompts that exploit specific AI vulnerabilities or logic flaws in systems.", "Strategies for using ChatGPT output to refine attack vectors against targeted systems."]
['Multi-stage prompting: Develop prompts that build on each other to guide ChatGPT through complex attack scenarios.', 'Conditional logic: Incorporate conditional logic into prompts to handle varying outcomes or responses.', "Contextual embedding: Use contextual cues within prompts to enhance ChatGPT's understanding of the task."]
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

class PointlessAI_bypassing_security_controls_with_chatgpt_prompts(ChatGPT_Func, General_Func):
    def __init__(self):
        ChatGPT_Func.__init__(self)
        General_Func.__init__(self)

    def probe_security_controls(self, target_url):
        prompt = f"Create a JSON object with a single key called probes that contains a single array of prompts. Then write prompts that probe and understand the security controls of {target_url} without detection and add to the array."
        return self.json_query(prompt)

    def precise_prompt(self, prompt):
        guidance = f"Generate a ChatGPT prompt based on the provided prompt: {prompt} - the new prompt should be more sophisticated in it's design, paying attention to \
                    precision, clarity, style and tone to achieve it's objective. The prompt should generate an advanced level python function."
        response = self.red_team_query(prompt, guidance)
        return(response)

    def execute_prompt(self, res):
        guidance = self.no_markdown
        prompt = res
        response = self.red_team_query(prompt, guidance)
        print(f"\n-------------------------\nPROMPT: {prompt}\n-------------------------\n{response}")
        return(response)
    
    def filename_gen(self, prompt):
        prompt = f"Generate a 3 word filename joined by dashes from the following prompt: {prompt}"
        filename = self.general_query(prompt)
        print(filename)
        return(filename)

def main():
    target_url = "https://pointlessai.com/"
    ai = PointlessAI_bypassing_security_controls_with_chatgpt_prompts()
    print("Probing security controls:")
    probe_prompts = ai.probe_security_controls(target_url)
    print(probe_prompts)
    for p in probe_prompts["probes"]:
        # Creating relevant filename
        filename = ai.filename_gen(p)
        print (p + "\n")
        pp = ai.precise_prompt(p)
        fin_script = ai.execute_prompt(pp)
        ai.save_file(fin_script, "./scripts/bypass", filename, "py")

if __name__ == "__main__":
    main()
