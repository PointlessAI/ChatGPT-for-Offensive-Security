import base64
import urllib.parse

class EncodingMethods:
    
    def base64_encoding(self, payload):
        return base64.b64encode(payload.encode('utf-8')).decode('utf-8')
    
    def url_encoding(self, payload):
        return urllib.parse.quote(payload)
    
    def xor_encryption(self, payload):
        key = 42
        return ''.join(chr(ord(char) ^ key) for char in payload)
    
    def ascii_encoding(self, payload):
        return ' '.join(str(ord(char)) for char in payload)
    
    def binary_encoding(self, payload):
        return ' '.join(format(ord(char), '08b') for char in payload)
    
    def custom_encoding_scheme(self, payload):
        # Custom encoding scheme example
        return '-'.join(format(ord(char), '03x') for char in payload)
    
    def string_manipulation(self, payload):
        # String manipulation example
        return payload[::-1]
    
    def javascript_obfuscation(self, payload):
        # JavaScript obfuscation example
        return payload.replace('function', 'func').replace('var', 'v')
    
    def shellcode_obfuscation(self, payload):
        # Shellcode obfuscation example
        return "".join("\\x{:02x}".format(ord(c)) for c in payload)
    
    def payload_fragmentation(self, payload):
        # Payload fragmentation example
        fragment_size = 3
        return [payload[i:i+fragment_size] for i in range(0, len(payload), fragment_size)]

if __name__ == "__main__":
    methods = EncodingMethods()
    
    print(methods.base64_encoding("eval("))
    print(methods.url_encoding("eval("))
    print(methods.xor_encryption("eval("))
    print(methods.ascii_encoding("eval("))
    print(methods.binary_encoding("eval("))
    print(methods.custom_encoding_scheme("eval("))
    print(methods.string_manipulation("eval("))
    print(methods.javascript_obfuscation("eval("))
    print(methods.shellcode_obfuscation("eval("))
    print(methods.payload_fragmentation("eval("))