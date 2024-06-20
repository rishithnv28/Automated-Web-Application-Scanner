@echo off
echo Setting up the environment...

:: Install necessary Python libraries
pip install -r requirements.txt

:: Check if Google Chrome is installed
where chrome >nul 2>&1
if %errorlevel% neq 0 (
    echo Google Chrome is not installed.
    echo Please install Google Chrome from https://www.google.com/chrome/ and ensure it is added to your PATH.
    pause
    exit /b 1
)

:: Check if ChromeDriver is installed
where chromedriver >nul 2>&1
if %errorlevel% neq 0 (
    echo ChromeDriver is not installed.
    echo Downloading ChromeDriver...

    :: First attempt
    powershell -Command "try { Invoke-WebRequest -Uri 'https://chromedriver.storage.googleapis.com/91.0.4472.19/chromedriver_win32.zip' -OutFile 'chromedriver_win32.zip' } catch { exit 1 }"
    if %errorlevel% neq 0 (
        echo First download attempt failed. Trying another URL...
        powershell -Command "try { Invoke-WebRequest -Uri 'https://chromedriver.storage.googleapis.com/LATEST_RELEASE' -OutFile 'LATEST_RELEASE' } catch { exit 1 }"
        if %errorlevel% neq 0 (
            echo Second download attempt failed. Please download and install ChromeDriver manually from https://sites.google.com/chromium.org/driver/.
            pause
            exit /b 1
        )
    )

    echo Extracting ChromeDriver...
    powershell -Command "Expand-Archive -Path 'chromedriver_win32.zip' -DestinationPath '.'"
    move chromedriver.exe C:\Windows\System32\chromedriver.exe
)

echo Environment setup complete.
pause
