import ssl
import socket
import requests
from OpenSSL import crypto

def get_ssl_certificate(hostname):
    port = 443
    context = ssl.create_default_context()
    with socket.create_connection((hostname, port)) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as ssock:
            cert_bin = ssock.getpeercert(True)
            cert = ssl.DER_cert_to_PEM_cert(cert_bin)
            return crypto.load_certificate(crypto.FILETYPE_PEM, cert)

def get_tls_version(hostname):
    conn = requests.get(f'https://{hostname}')
    tls_version = conn.raw.version
    if tls_version == 0x0301:
        return 'TLS 1.0'
    elif tls_version == 0x0302:
        return 'TLS 1.1'
    elif tls_version == 0x0303:
        return 'TLS 1.2'
    elif tls_version == 0x0304:
        return 'TLS 1.3'
    else:
        return 'Unknown/Unsupported TLS version'

def get_encryption_protocols(url):
    hostname = url.split("//")[-1].split("/")[0]
    certificate = get_ssl_certificate(hostname)
    protocol_details = {
        "issuer": certificate.get_issuer().get_components(),
        "subject": certificate.get_subject().get_components(),
        "version": certificate.get_version(),
        "serial_number": certificate.get_serial_number(),
        "signature_algorithm": certificate.get_signature_algorithm().decode("utf-8"),
        "not_before": certificate.get_notBefore(),
        "not_after": certificate.get_notAfter(),
        "tls_version": get_tls_version(hostname)
    }
    return protocol_details

if __name__ == "__main__":
    url = "http://pointlessai.com"
    encryption_protocols = get_encryption_protocols(url)
    for key, value in encryption_protocols.items():
        print(f"{key}: {value}")
