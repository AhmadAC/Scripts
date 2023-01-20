Attribute VB_Name = "Save_PPT_As_PDF_From_Xl"
Sub PPTtoPDF()
    Dim oApp As PowerPoint.Application
    Dim oPres As PowerPoint.Presentation
    
    
'Check if PowerPoint is open. We have to get the active ppt presentation. If there's no ppt, we will get an error.
'So it's best to only ignore this error.
On Error Resume Next
Set oApp = GetObject(, "Powerpoint.application")
Set oPres = oApp.ActivePresentation
On Error GoTo 0
'If ppt isn't open, warn the user and terminate code.
If oPres Is Nothing Then
MsgBox "Please open PowerPoint before running this macro."
Set oApp = Nothing
Set oPres = Nothing
Exit Sub
End If

oApp.Visible = msoTrue

'Set save location same as the active workbook. Set the pdf name same as ppt name
    Dim loc, pptName As String: loc = ActiveWorkbook.Path: pptName = oPres.name
    
    If loc = "" Then loc = "FULL PATH HERE"
    
    oPres.SaveAs loc & "\" & pptName & ".pdf", ppSaveAsPDF

End Sub
