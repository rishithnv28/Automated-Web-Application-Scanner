from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from vulnerabilities import (
    scan_xss, scan_sqli, scan_csrf, scan_open_redirect,
    scan_rfi, scan_lfi, scan_command_injection, scan_unauth_access
)

def scan_website(url):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)

    try:
        driver.get(url)
        time.sleep(3)

        results = {
            'xss': scan_xss(driver, url),
            'sqli': scan_sqli(driver, url),
            'csrf': scan_csrf(driver, url),
            'open_redirect': scan_open_redirect(driver, url),
            'rfi': scan_rfi(driver, url),
            'lfi': scan_lfi(driver, url),
            'command_injection': scan_command_injection(driver, url),
            'unauthorized_access': scan_unauth_access(driver, url)
        }

        driver.quit()
        return results

    except Exception as e:
        driver.quit()
        print(f"Error scanning website: {e}")
        return None

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Automated Web Application Security Scanner")
    parser.add_argument('url', type=str, help="URL of the web application to scan")

    args = parser.parse_args()
    results = scan_website(args.url)

    if results:
        print("Scan Results:")
        for vulnerability, result in results.items():
            print(f"{vulnerability}: {result}")
    else:
        print("Scanning failed.")
