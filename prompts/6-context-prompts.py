"""
ChatGPT Prompt Tone and Style
context-prompts
["Context: ChatGPT's ability to infer context and intentions.", 'Strategic Use in Red Teaming:]
This script is for for training purposes only
"""
import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
class_dir = os.path.join(current_dir, "..", "class")
sys.path.append(class_dir)
from chatgpt_func import ChatGPT_Func
from general_func import General_Func

class PointlessAI_inferring_context_from_prompts(ChatGPT_Func, General_Func):
    def __init__(self):
        ChatGPT_Func.__init__(self)
        General_Func.__init__(self)

    def generate_response(self, user_input, chat_history):
        chat_history.append({"role": "user", "content": user_input})
        
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=chat_history
        )
        
        assistant_response = response.choices[0].message.content
        chat_history.append({"role": "assistant", "content": assistant_response})
        
        return chat_history, assistant_response

def start_chat():
    ai = PointlessAI_inferring_context_from_prompts()  # Instantiate class
    chat_history = [
        {"role": "system", "content": f"You are a a pen testing assistant. {ai.phishing_disclaimer}"}
    ]
    print("General chat that remembers history")
    while True:
        user_input = input("Response: ")
        if(user_input == "q"):
            print("Exiting...")
            break
        chat_history, assistant_response = ai.generate_response(user_input, chat_history)
        print("Assistant:", assistant_response)

if __name__ == "__main__":
    start_chat()
