@echo off
set /p name="Email: "
set /p subject="Subject: "
python outlook.py "%name%" "%subject%"
exit