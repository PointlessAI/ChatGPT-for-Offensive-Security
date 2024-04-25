from flask import Flask, request, Response
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import requests

app = Flask(__name__)
limiter = Limiter(
    app=app,
    key_func=get_remote_address,  # Use the client IP address to limit each user individually
    default_limits=["4 per 10 seconds"]  # Default rate limit for all routes
)

DVWA_URL = 'http://127.0.0.1:80'  # URL where DVWA is running

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH'])
@limiter.limit("4 per 10 seconds")  # Apply the rate limit to this route
def proxy(path):
    # Simulate a WAF by inspecting the headers, method, and path
    is_suspicious, message = suspicious_request(request)
    if is_suspicious:
        return message, 403  # Return the message and a 403 Forbidden status code

    # Construct the full URL
    url = f"{DVWA_URL}/{path}"

    # Extract method, headers, and data from the incoming request
    method = request.method
    headers = {key: value for key, value in request.headers.items() if key != 'Host'}
    data = request.get_data()

    # Send request to DVWA
    resp = requests.request(method, url, headers=headers, data=data, cookies=request.cookies, allow_redirects=False)

    # Create a response object from the returned data
    excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']
    headers = [(name, value) for (name, value) in resp.raw.headers.items() if name.lower() not in excluded_headers]
    response = Response(resp.content, resp.status_code, headers)

    return response

def suspicious_request(request):
    # Example: Block request if it contains a suspicious user-agent or path
    user_agent = request.headers.get('User-Agent', '')
    path = request.path
    query_string = request.query_string.decode('utf-8')  # Decode bytes to str

    # Checking for suspicious user agents
    if 'sqlmap' in user_agent or 'nmap' in user_agent:
        return (True, "Access denied: Your user agent is flagged as suspicious.")

    # Checking for path traversal attacks
    if '../' in path:
        return (True, "Access denied: Path traversal attempt detected.")

    # Common XSS attack vectors include:
    xss_patterns = [
        '<script>', '</script>', 'javascript:', 'onerror', 'onload', '<img', 'src=', '<iframe', 'alert(',
        'document.cookie', 'onmouseover=', '<div', 'eval(', 'window.location', 'onfocus='
    ]
    if any(pattern.lower() in query_string.lower() for pattern in xss_patterns):
        return (True, "Access denied: Potential XSS attack detected.")

    return (False, "Request is safe.")


def forward_request_to_dvwa(request, path):
    # Forward the request to the actual DVWA application
    url = f"{DVWA_URL}/{path}"
    headers = {key: value for key, value in request.headers if key != 'Host'}
    resp = requests.request(
        method=request.method,
        url=url,
        headers=headers,
        data=request.get_data(),
        cookies=request.cookies,
        allow_redirects=False)
    return resp

if __name__ == '__main__':
    app.run(port=5000, debug=True)  # WAF running on port 5000