# Automatic web application security scanner

## Observation
This application uses Selenium and Python to scan web applications for security vulnerabilities. It contains detection methods for XSS, SQL Injection, CSRF, Open Redirect, RFI, LFI, Command Injection, and Unauthorized Access.

Check out the Python installation:

Verify that Python is added to the PATH by enabling python --version in the Command Prompt.

Run the setup script:

Run setup.bat to install dependencies and set up the environment.

Run the test:

In order to create the test scenarios and run_tests.py to make sure everything works as expected.

## features
- **Comprehensive Scanning**: Detects multiple vulnerabilities in web applications.
- **Comprehensive Test Cases**: Includes multiple test cases to ensure ease of identification.
- **Automatic testing**: Automates the scanning process with predefined test cases.
- **Detailed Report**: Provides a detailed report of known vulnerabilities.

## lay
1. Cloning a repository:
    ```Sh
    git clone https://github.com/yourusername/active_security_scanner.git
    cd automatic_security_scanner
    ```

2. Run `setup.bat` with the necessary installation:
    ```Sh
    system.bat
    ```

## Survey
### Website scanning
Use the following command to browse the web to see if it is vulnerable.
```Sh
Python Scanner.py <url>

url: The URL of the web application to search for.

For example
Python Scanner.py http://testphp.vulnweb.com

Examine

Run run_tests.py to create the custom test scenarios:

Python run_test.py

This will run multiple test cases and save the results to tests/test_results.txt.


Details of fragility

XSS (Cross-Site Scripting): Checks for malicious scripts embedded in web pages.
SQL Injection: Test for vulnerability where there may be negative SQL statements