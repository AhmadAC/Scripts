@echo off
mode con: cols=80 lines=8
color 0A
title Write MP4 filenames

::Written by Ahmad Cooper
::Software comes "as is", no warranty.
::Writes the current directory and the mp4 file names to a text file.

set "variable=%cd%/"
set "variable=%variable:\=/%"
echo "%variable%"
echo %variable%>MP4_FileNames.txt

dir *.mp4 /b >>MP4_FileNames.txt
for /f "delims=" %%a in ('dir /s /b *.mp4') do set "name=%%a"


::uncomment to pause CMD.
::cmd /k