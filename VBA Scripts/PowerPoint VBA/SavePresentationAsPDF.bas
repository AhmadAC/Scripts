Attribute VB_Name = "SavePresentationAsPDF"
Sub SavePresentationAsPDF()
    Dim loc, pptName As String
    On Error GoTo 1:
    pptName = Left(ActivePresentation.Name, (InStrRev(ActivePresentation.Name, ".", -1, vbTextCompare) - 1))
    loc = ActivePresentation.Path & "\" & pptName & ".pdf"
    ActivePresentation.SaveAs loc, ppSaveAsPDF
    Exit Sub
    
1:
MsgBox "Save presentation before exporting to PDF."
End Sub
