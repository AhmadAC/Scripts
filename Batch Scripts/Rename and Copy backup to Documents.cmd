@echo off

if not exist "C:\Users\%username%\Documents\Game\" (
    mkdir "C:\Users\%username%\Documents\Game\"
)

REM Renames and copies the "b" file as b.pptm to the Game directory.
copy /y "%~dp0\b" "C:\Users\%username%\Documents\Game\b.pptm" > nul
