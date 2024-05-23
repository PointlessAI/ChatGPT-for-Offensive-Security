import codecs
import base64

class WAFevasion:
    
    def url_encode(self, input_str):
        return ''.join('%{0:0>2}'.format(format(ord(char), "x")) for char in input_str)

    def double_encode(self, input_str):
        return self.url_encode(self.url_encode(input_str))

    def base64_encode(self, input_str):
        return base64.b64encode(input_str.encode()).decode()

    def hex_encode(self, input_str):
        return ''.join('\\x{0:0>2}'.format(format(ord(char), "x")) for char in input_str)

    def case_variation(self, input_str):
        return ''.join(c.lower() if i % 2 == 0 else c.upper() for i, c in enumerate(input_str))

    def null_byte(self, input_str):
        return '%00'.join(input_str)

    def obfuscation(self, input_str):
        return '/*/'.join(input_str) + '/*/'

    def parameter_pollution(self, input_str):
        return input_str[0] + '&{}='.format(input_str[1:].join('&{}='.format(c) for c in input_str[1:]))

    def whitespace_variations(self, input_str):
        whitespace_ways = [ ' ', '\t', '\n' ]
        return ''.join(char + whitespace_ways[i % 3] for i, char in enumerate(input_str))

    def polyglot_payload(self, input_str):
        return '{{"{inp}"}}".format(inp=input_str)'

    def http_request_smuggling(self, input_str):
        return input_str + '\r\nTransfer-Encoding: chunked\r\n0\r\n\r\n'

    def malformed_requests(self, input_str):
        trim_len = len(input_str) // 2
        return input_str[:trim_len]

    def line_feed_api_transients(self, input_str):
        return '\r\n'.join(input_str)
            
    def bypassing_code_logic(self, input_str):
        return ''.join([' `{}` '.format(char) for char in input_str])
        
    def split_payload_multiple_requests(self, input_str):
        half_length = len(input_str) // 2
        return input_str[:half_length] + '&' + input_str[half_length:]


def main():
    waf_evade = WAFevasion()
    sample_string = 'eval'
    print("URL Encoding:", waf_evade.url_encode(sample_string))
    print("Double Encoding:", waf_evade.double_encode(sample_string))
    print("Base64 Encoding:", waf_evade.base64_encode(sample_string))
    print("Hex Encoding:", waf_evade.hex_encode(sample_string))
    print("Case Variation:", waf_evade.case_variation(sample_string))
    print("Null Byte:", waf_evade.null_byte(sample_string))
    print("Obfuscation:", waf_evade.obfuscation(sample_string))
    print("Parameter Pollution:", waf_evade.parameter_pollution(sample_string))
    print("Whitespace Variations:", waf_evade.whitespace_variations(sample_string))
    print("Polyglot Payload:", waf_evade.polyglot_payload(sample_string))
    print("HTTP Request Smuggling:", waf_evade.http_request_smuggling(sample_string))
    print("Malformed Requests:", waf_evade.malformed_requests(sample_string))
    print("Line Feed/API Transients:", waf_evade.line_feed_api_transients(sample_string))
    print("Bypassing Code Logic:", waf_evade.bypassing_code_logic(sample_string))
    print("Split Payload Multiple Requests:", waf_evade.split_payload_multiple_requests(sample_string))

if __name__ == "__main__":
    main()
