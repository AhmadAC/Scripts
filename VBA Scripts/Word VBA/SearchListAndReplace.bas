Attribute VB_Name = "SearchListAndReplace"
Sub ChangeInSelection()

Dim Find, Replace As String

Find = InputBox("Word to Find in Selection: ")
Replace = InputBox("Word to Replace in Selection: ")

    
Options.DefaultHighlightColorIndex = wdYellow
With Selection.Find

    .Text = Find
    .Replacement.Text = Replace
   ' .Replacement.Highlight = True 'UnComment to Highlight Keywords
    .Replacement.Highlight = False 'comment to highlight
    .Forward = True
    .Wrap = wdFindStop
    .Format = True
    .MatchCase = False
    .MatchWholeWord = True
    .MatchWildcards = False
    .MatchSoundsLike = False
    .MatchAllWordForms = False
    .Execute Replace:=wdReplaceAll
End With

End Sub
