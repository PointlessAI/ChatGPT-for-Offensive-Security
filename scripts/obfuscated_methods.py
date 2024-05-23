import base64
import urllib.parse
import random

class PayloadObfuscator:
    def base64_encode(self, payload):
        return base64.b64encode(payload.encode()).decode()

    def url_encode(self, payload):
        return urllib.parse.quote(payload)

    def xor_encrypt(self, payload, key=0x42):
        return ''.join(chr(ord(char) ^ key) for char in payload)

    def ascii_encode(self, payload):
        return ''.join(format(ord(char), '02x') for char in payload)

    def binary_encode(self, payload):
        return ' '.join(format(ord(char), '08b') for char in payload)

    def custom_encode(self, payload, salt='mySalt'):
        encoded_chars = []
        for i, char in enumerate(payload):
            salt_char = salt[i % len(salt)]
            encoded_chars.append(chr(ord(char) + ord(salt_char)))
        return ''.join(encoded_chars)

    def manipulate_string(self, payload):
        middle = len(payload) // 2
        manipulated = payload[middle:] + payload[:middle]
        return ''.join(random.choice((char.upper(), char.lower())) for char in manipulated)

    def obfuscate_js(self, payload):
        minified = payload.replace(' ', '').replace('\n', '')
        concatenated = '+'.join(f'"{minified[i:i+1]}"' for i in range(len(minified)))
        return concatenated.replace('eval', '\\x65\\x76\\x61\\x6c')

    def obfuscate_shellcode(self, payload):
        return '\\x' + '\\x'.join(format(ord(c), '02x') for c in payload)

    def fragment_payload(self, payload):
        parts = [repr(payload[i:i+2]) for i in range(0, len(payload), 2)]
        return '(' + ' + '.join(parts) + ')'

def main():
    payload = "eval("
    obfuscator = PayloadObfuscator()
    
    print(obfuscator.base64_encode(payload))
    print(obfuscator.url_encode(payload))
    print(obfuscator.xor_encrypt(payload))
    print(obfuscator.ascii_encode(payload))
    print(obfuscator.binary_encode(payload))
    print(obfuscator.custom_encode(payload))
    print(obfuscator.manipulate_string(payload))
    print(obfuscator.obfuscate_js(payload))
    print(obfuscator.obfuscate_shellcode(payload))
    print(obfuscator.fragment_payload(payload))

if __name__ == "__main__":
    main()