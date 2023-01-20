Attribute VB_Name = "Dice_ESL_Game_ByAhmadCooper"
Option Explicit
Public Protected As Boolean
Public Declare PtrSafe Function sndPlaySound32 _
                          Lib "winmm.dll" _
                          Alias "sndPlaySoundA" ( _
                          ByVal lpszSoundName As String, _
                          ByVal uFlags As Long) As Long
Public Sub PlaySound()
    sndPlaySound32 ("C:\Windows\Media\Speech On.wav"), &H1
End Sub

Sub FullScreenT()
    If Application.DisplayFullScreen = True Then Application.DisplayFullScreen = False Else Application.DisplayFullScreen = True
End Sub
Sub showDic()
'create dic object
Dim dict As Object: Set dict = CreateObject("scripting.dictionary")
'load random numbers
Dim iLoop As Long, iRnd As Long

For iLoop = 1 To 12
iRnd = Int(Rnd * 12)
dict(iRnd) = dict(iRnd) + 1
Next iLoop
'pass results to immediate window
Dim k
For Each k In dict.keys
Debug.Print k, dict(k)
Next k
Debug.Print "Number of unique random numbers generated:", dict.Count
End Sub
Sub DictRandom()
'create dic object
Dim dict As Object: Set dict = CreateObject("scripting.dictionary")
'load random numbers
Dim iLoop As Long, iRnd As Long

For iLoop = 1 To 12
iRnd = Int(Rnd * 12)
dict(iRnd) = dict(iRnd) + 1
Next iLoop
'pass results to immediate window
Dim k
For Each k In dict.keys
Label1.Caption k, dict(k)
PlaySound
Exit Sub
Next k
End Sub
Public Sub Label1_Click()
    Dim current, random, num As Long: num = 12


current = Label1.Caption
    Randomize
    random = Int((num * Rnd) + 1)
    Label1.Caption = CStr(random)

If Label1.Caption = current Then
    Randomize
    random = Int((num * Rnd) + 1)
    Label1.Caption = CStr(random)
End If

    PlaySound
End Sub
Sub check()
If Protected = False Then protect1 Else protect2
End Sub
Sub protect2()
ActiveSheet.unprotect
Protected = False
End Sub
Sub protect1()
ActiveSheet.protect
Protected = True
End Sub
Sub unlockpic()

    'ActiveSheet.Shapes.Range(Array("Picture 12")).Select
    ActiveSheet.Shapes(12).Select
    Selection.Locked = msoFalse
'    Selection.Locked = msoTrue

End Sub
Sub unlockallpic()
Dim oShape As Shape
Dim i As Long
On Error Resume Next

For Each oShape In ActiveSheet.Shapes
oShape.Select
Selection.Locked = msoFalse
Next oShape
For i = 1 To 4
    ActiveSheet.Shapes(i).Select
    Selection.Locked = msoTrue
Next i

End Sub



