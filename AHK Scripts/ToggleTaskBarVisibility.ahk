#SingleInstance, Force
SendMode Input
SetWorkingDir, %A_ScriptDir%
^2::
if (check = 1)
{
MsgBox, , , Show Taskbar, 0.40
Run, powershell -command "&{$p='HKCU:SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\StuckRects3';$v=(Get-ItemProperty -Path $p).Settings;$v[8]=2;&Set-ItemProperty -Path $p -Name Settings -Value $v;&Stop-Process -f -ProcessName explorer}"
check := 2
}
else
{
MsgBox, , , Hide Taskbar, 0.40
Run, powershell -command "&{$p='HKCU:SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\StuckRects3';$v=(Get-ItemProperty -Path $p).Settings;$v[8]=3;&Set-ItemProperty -Path $p -Name Settings -Value $v;&Stop-Process -f -ProcessName explorer}"
check := 1
}
return
