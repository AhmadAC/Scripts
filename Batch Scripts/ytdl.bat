@REM Written by Ahmad Cooper
@REM YouTube DL GUI with Command Prompt. Need to have yt-dlp and the dependencies.
@echo off
mode con: cols=80 lines=8
color 0A
title YouTube Downloader

@REM Get clipboard contents using PowerShell
for /f "delims=" %%a in ('powershell -command "Get-Clipboard"') do set "clipboard=%%a"

@REM Extract URL from clipboard using a regular expression
set "regex=^(https?://)?(www\.)?[a-zA-Z0-9-]+(\.[a-zA-Z]+)+(/[^\s]*)*$"
for /f "delims=" %%b in ('powershell -Command "$env:clipboard -replace '%regex%', '$&' "') do set "url=%%b"


@REM Download video using youtube-dl
"C:\Users\ahmad\Documents\YoutubeDLer\YTDL\youtube-dl.exe" --write-sub --sub-lang en -f "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best" %url%


