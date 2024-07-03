# ChatGPT For Offensive Cybersecurity Training Materials

This project utilizes Python and the OpenAI API to as part of the ChatGPT For Offensive Cybersecurity Training Course through the INFOSEC INSTITUTE. The purpose is to uncover the capabilities of ChatGPT to generate, analyze, and refine content, code, scripts and logs, tailored for cybersecurity professionals.

## License for Training Materials

The training materials in this repository are licensed under the Creative Commons Attribution 4.0 International (CC BY 4.0). To view a copy of this license, visit [http://creativecommons.org/licenses/by/4.0/](http://creativecommons.org/licenses/by/4.0/) or see the [LICENSE-CC-BY](LICENSE-CC-BY) file for details.

## Features
- ChatGPT For Offensive Cybersecurity Training Materials
- Generate offensive cybersecurity scenarios and materials using ChatGPT.
- Customize and enhance content through Python scripts.
- Run the project in a Python virtual environment for isolation and dependency management.

## Prerequisites
- Python 3.7 or higher
- An OpenAI API key

## Installation
* First virtual environment:
- python -m venv yourname-venv
- source yourname-venv/bin/activate
* Then get repo:
- Clone the Repository
- Set API keys either by passing api_key to the client or by setting the OPENAI_API_KEY environment variable
```python
        # /class/chatgpt_func.py
        self.githubapi_key = os.environ.get("GITHUB_API_KEY")
        self.google_api_key = os.environ.get("google_api_key")
        self.google_cse_id = os.environ.get("google_cse_id")
```
- pip install -r requirements.txt

