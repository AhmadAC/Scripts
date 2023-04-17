@REM Written by Ahmad Cooper
@REM Change source 1 and 2 file names. Copies and replaces the same files in subfolders located in the script folder.

@echo off
setlocal enabledelayedexpansion
set "source1=example1.fileextension"
set "source2=example2.fileextension"

for /r "%~dp0." %%f in (*.svg) do (
    if not "%%~nxf"=="%~nx0" (
        set "dest=%%~dpf%%~nf.svg"
        copy /y "!source1!" "!dest!"
        copy /y "!source2!" "!dest!"
        echo Copied files to: "%%~dpf"
    )
)
