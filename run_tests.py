import os
import subprocess

def run_tests():
    print("Running tests...")

    test_url = "http://testphp.vulnweb.com"
    process = subprocess.Popen(["python", "scanner.py", test_url], stdout=subprocess.PIPE)
    output, _ = process.communicate()

    with open("tests/test_results.txt", "w") as results_file:
        results_file.write(output.decode())

    print("Tests completed successfully")

if __name__ == "__main__":
    run_tests()
