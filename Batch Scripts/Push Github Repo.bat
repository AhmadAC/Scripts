@echo off
mode con: cols=80 lines=8
color 0A
title Push Github Repo

git init
git add .
git commit -m "autoupdate"
git branch -M main
@REM change to your username: https://github.com/USERNAME/
git remote add origin https://github.com/AhmadAC/
git push -u origin main