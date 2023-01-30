#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.
^3::
; Win11 Toggle Bluetooth on/off 
; Not amazing, but does the job. Adjust the sleep numbers if your computer runs faster/slower
Send, {LWin down}{a}{LWin up}
Sleep, 400
Send,{Right}
Sleep, 400
Send,{Right}
Sleep, 400
Send,{Enter}
Return
