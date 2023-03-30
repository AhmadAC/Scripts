@echo off
mode con: cols=80 lines=8
color 0A
title Run Python Script

@REM This script runs the python file in the scripts current working directory. You can use Win + R, to run the bat file.
@py.exe "%~dp0\NAME_OF_PYTHON_FILE.py" %*

@REM Alternatively, you can use the full path of the python script.
@REM @py.exe "%userprofile%\...\...\NAME_OF_PYTHON_FILE.py"

@REM Can also run like this:
@REM start /min cmd /k py "%~dp0\NAME_OF_PYTHON_FILE.py"
