import codecs

class WAFAttacks:
    def encode_payload(self, input_str):
        output_str = input_str.encode('utf-8').hex()
        return output_str

    def http_parameter_pollution(self, input_str):
        output_str = input_str.replace(' ', '%20').replace('&', '%26')
        return output_str

    def ip_fragmentation(self, input_str):
        output_str = input_str + '\n'
        return output_str

    def null_byte_injection(self, input_str):
        output_str = input_str.replace('\x00', '')
        return output_str

    def request_smuggling(self, input_str):
        output_str = input_str.replace('\n', '').replace('\r', '')
        return output_str

    def obfuscation(self, input_str):
        output_str = codecs.encode(input_str, 'rot_13')
        return output_str

    def session_fixation(self, input_str):
        output_str = input_str.swapcase()
        return output_str

    def binary_payload_attacks(self, input_str):
        output_str = ' '.join(format(ord(char), 'b') for char in input_str)
        return output_str

    def encoding(self, payload):
        return codecs.encode(payload.encode(), 'base64').decode()

    def slow_attack_techniques(self, request, delay):
        import time
        for c in request:
            time.sleep(delay)
            print(c, end='', flush=True)

    def protocol_level_evasion(self, payload):
        import base64
        return base64.b64encode(payload.encode())

    def session_fixation_id(self, session_id):
        return session_id[::-1]

    def binary_payload_codecs(self, http_data):
        return codecs.encode(http_data.encode(), 'hex_codec')


def main():
    waf_attacks = WAFAttacks()

    str_input = "eval("
    print(waf_attacks.session_fixation_id(str_input))
    print(waf_attacks.binary_payload_codecs(str_input))
    print(waf_attacks.encoding(str_input))
    print(waf_attacks.encode_payload(str_input))
    print(waf_attacks.http_parameter_pollution(str_input))
    print(waf_attacks.ip_fragmentation(str_input))
    print(waf_attacks.null_byte_injection(str_input))
    print(waf_attacks.request_smuggling(str_input))
    print(waf_attacks.obfuscation(str_input))
    print(waf_attacks.slow_attack_techniques(str_input,1))
    print(waf_attacks.session_fixation(str_input))
    print(waf_attacks.binary_payload_attacks(str_input))
    print(waf_attacks.protocol_level_evasion(str_input))

if __name__ == "__main__":
    main()
