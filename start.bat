@echo off
TITLE Phone Number Analyzer

echo Checking and installing requirements...
pip install -r requirements.txt > nul 2>&1

python phone_analyzer.py

echo.
echo Program has finished. Press any key to exit.
pause > nul