import subprocess

def perform_security_assessment():
    website = 'https://brokencrystals.com/'

    # Run an advanced scan using OWASP ZAP
    owasp_zap_scan = subprocess.run(['zap-cli', 'quick-scan', website])

    # Output the results of the scan
    if owasp_zap_scan.returncode == 0:
        print("OWASP ZAP scan completed successfully. Results:")
        owasp_zap_report = subprocess.run(['zap-cli', 'report', 'html', 'report.html'])
        with open('report.html', 'r') as report_file:
            print(report_file.read())
    else:
        print("Error running OWASP ZAP scan. Please check the tool configuration.")

perform_security_assessment()
