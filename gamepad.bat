@echo off

set VENV_PATH=%CD%\.env\Scripts\activate
call %VENV_PATH%

python gamepad.py

pause