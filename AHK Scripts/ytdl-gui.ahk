;YouTube Downloader GUI
;Written by Ahmad Cooper
;For education purposes only, use at your own risk, no warranty, comes 'as is'

;Note: ignore this error; [generic] '%(title)s' is not a valid URL. Set --default-search "ytsearch" (or run  yt-dlp "ytsearch:%(title)s" ) to search YouTube


;Put in the script folder for the program to work:
; ffmpeg.exe
; ffplay.exe
; ffprobe.exe
; youtube-dl.exe

; Get the URL from the clipboard
vurl = %Clipboard%

Gui, Font, s10, Comic Sans MS  ; Preferred font
Gui, Add, Text,, Download Videos - Press Esc to close program.
Gui, Add, Text,, Press Ctrl+Q to restart program.
Gui, Add, Text,, URL:
Gui, Add, Edit, vurl, %vurl%
Gui, Add, Button, Default gButtonGo, Download
Gui, Show,,
return

ButtonGo:
    Gui, Submit
    ; Build the youtube-dl command, adjust it if you need to
    youtubeDLCommand = youtube-dl --write-sub --sub-lang en -f "best[height<=?1080]+bestaudio[ext=m4a]/best[ext=mp4]/best" "`%(title)s" "%url%"
    ; Run the youtube-dl command
    Run %youtubeDLCommand%
    Sleep, 200

IfNotExist, %a_scriptdir%\Videos\
{
FileCreateDir, %a_scriptdir%\Videos\
}
FileMove, %a_scriptdir%\*.mp4, %a_scriptdir%\Videos\*.mp4, 1
FileMove, %a_scriptdir%\*.vtt, %a_scriptdir%\Videos\*.vtt, 1
GUIClose:
Gui, destroy
return
^q::
;Send, {F5}
Reload
Sleep 1000 ; If successful, the reload will close this instance during the Sleep, so the line below will never be reached.
MsgBox, 4,, The script could not be reloaded. Would you like to open it for editing?
IfMsgBox, Yes, Edit
return
Esc::
ExitApp
return
