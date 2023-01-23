#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

;Press Ctrl+2 to change the default printer to: Microsoft Print to PDF

^2::
Send, #r
Sleep, 100
Send, RUNDLL32 PRINTUI.DLL,PrintUIEntry /y /n "Microsoft Print to PDF"
Send, {Enter}
MsgBox, , , Print to PDF, 0.40
return

;Press Ctrl+3 to change the default printer to: HP Smart Tank 510 series

^3::
Send, #r
Sleep, 100
Send, RUNDLL32 PRINTUI.DLL,PrintUIEntry /y /n "HP Smart Tank 510 series"
Send, {Enter}
MsgBox, , , Print to HP Smart Tank 510 series, 0.40
return