Sub ChangeNumToWords()

Dim I As Long, numbers As String

numbers = "zero,one,two,three,four,five,six,seven,eight,nine,ten"

Dim arr
arr = Split(numbers, ",")
    
Options.DefaultHighlightColorIndex = wdYellow
With Selection.Find

    For I = 11 To 1 Step -1
    .Text = I - 1
    .Replacement.Text = arr(I - 1)
    '.Replacement.Highlight = True 'UnComment to Highlight Keywords
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
    Next I
    
End With

End Sub
