Attribute VB_Name = "Save_PPT_From_Xl"
Sub SavePowerpointFromXL()
Dim oApp As PowerPoint.Application
Dim oPres As PowerPoint.Presentation
Dim ppt, name As String
'Saves the Active PowerPoint with a new name. If there isn't a ppt open, it'll open a new one.

' Show an input box to get the name of the PowerPoint file
name = InputBox("Enter the name of the PowerPoint file to save: ", "Save As", name, vbCancel)

' Check if the user clicked the Cancel button or closed the input box
If name = "" Then
        ' If so, exit the subroutine
        Exit Sub
End If

' Set the location of the PowerPoint file to be created, change pptm to ppt if not using a ppt with macros
ppt = ActiveWorkbook.Path & "\" & name & ".pptm"


' Check if PowerPoint is already open
On Error Resume Next
Set oApp = GetObject(, "PowerPoint.Application")

If oApp Is Nothing Then
    ' If not, create a new instance of PowerPoint
    Set oApp = CreateObject("PowerPoint.Application")
    oApp.Visible = True
        
    ' Open a new presentation
    Set oPres = oApp.Presentations.add
End If
On Error GoTo 0
Set oPres = oApp.ActivePresentation

' Save the presentation to the specified location
oPres.SaveAs ppt

' Clean up
Set oPres = Nothing
Set oApp = Nothing
End Sub
