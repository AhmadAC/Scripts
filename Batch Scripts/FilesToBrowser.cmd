@REM Written by Ahmad Cooper
@REM Software comes "as is", no warranty.
@REM Copy script to a folder with pdf and mp4 files you want to open with a browser

@echo off
for /f "delims=" %%a in ('dir /s /b *.mp4 *.pdf') do (
@REM for /f "delims=" %%a in ('dir /s /b ADD FILE NAMES THAT CAN OPEN IN A BROWSER HERE') do (
	 set "a=%%a"
	 setLocal EnableDelayedExpansion
	 set "a=!a: =%%20!"
@REM change msedge.exe to any browser you want to open the mp4/pdf files.
@REM	 start chrome.exe "%%a"
	 start msedge.exe "%%a"
	endlocal
)

exit /b

