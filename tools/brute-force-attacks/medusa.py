
```
import requests

# Brute-Force Attacks using Medusa
# Medusa is a popular password cracking tool for network authentication services.
# Description: This Python class demonstrates session hijacking using Medusa tool.

class SessionHijacking:
    def brute_force_attack(self):
        response = s.get('http://127.0.0.1:81/vulnerabilities/xss_d/')
        print(response.text)

    def medusa_attack(self):
        response = s.get('http://127.0.0.1:81/vulnerabilities/xss_d/')
        print(response.text)

def main():
    with requests.Session() as s:
        attacker = SessionHijacking()
        attacker.brute_force_attack()
	    attacker.medusa_attack()

if __name__ == "__main__":
    main()
```
