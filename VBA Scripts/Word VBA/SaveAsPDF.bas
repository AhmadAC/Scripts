Attribute VB_Name = "SaveAsPDF"
Sub WordMacroSaveAsPDF()
'macro saves pdf either in the same folder where active doc is or in documents folder if file is not yet saved

    Dim loc, Name As String: loc = ActiveDocument.Path & Application.PathSeparator: Name = Left(ActiveDocument.name, (InStrRev(ActiveDocument.name, ".", -1, vbTextCompare) - 1))

    If loc = "" Then    'doc is not saved yet
        loc = Options.DefaultFilePath(wdDocumentsPath) & Application.PathSeparator
    End If
    
    ActiveDocument.ExportAsFixedFormat OutputFileName:= _
                                       loc & Name & ".pdf", _
                                       ExportFormat:=wdExportFormatPDF, _
                                       OpenAfterExport:=False, _
                                       OptimizeFor:=wdExportOptimizeForPrint, _
                                       Range:=wdExportAllDocument, _
                                       IncludeDocProps:=True, _
                                       CreateBookmarks:=wdExportCreateWordBookmarks, _
                                       BitmapMissingFonts:=True
End Sub


