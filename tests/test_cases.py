import subprocess

def run_test_case(url, vulnerability_type, expected_result):
    process = subprocess.Popen(['python', 'scanner.py', url], stdout=subprocess.PIPE)
    output, _ = process.communicate()
    return expected_result in output.decode()

def main():
    test_url = "http://testphp.vulnweb.com"
    
    test_cases = [
        {'vulnerability_type': 'xss', 'expected_result': 'Vulnerable to XSS'},
        {'vulnerability_type': 'sqli', 'expected_result': 'Vulnerable to SQL Injection'},
        {'vulnerability_type': 'csrf', 'expected_result': 'Vulnerable to CSRF'},
        {'vulnerability_type': 'open_redirect', 'expected_result': 'Vulnerable to Open Redirect'},
        {'vulnerability_type': 'rfi', 'expected_result': 'Vulnerable to RFI'},
        {'vulnerability_type': 'lfi', 'expected_result': 'Vulnerable to LFI'},
        {'vulnerability_type': 'command_injection', 'expected_result': 'Vulnerable to Command Injection'},
        {'vulnerability_type': 'unauthorized_access', 'expected_result': 'Vulnerable to Unauthorized Access'}
    ]

    with open('tests/test_results.txt', 'w') as results_file:
        for case in test_cases:
            result = run_test_case(test_url, case['vulnerability_type'], case['expected_result'])
            results_file.write(f"Test {case['vulnerability_type']}: {'Passed' if result else 'Failed'}\n")

if __name__ == "__main__":
    main()
