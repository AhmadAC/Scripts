@echo off

if not exist "%~dp0\Game\" mkdir "%~dp0\Game\"
REM Renames and copies the "b" file as b.pptm to the Game directory.
copy /y "%~dp0\b" "%~dp0\Game\b.pptm" > nul
