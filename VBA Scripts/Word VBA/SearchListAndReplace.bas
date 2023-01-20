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
Sub ChangeMFwords()

Dim Gender, I, MWords, FWords As String
Gender = InputBox("Boy(1)/Girl(2): ")

'currently 6 words, words in the masculine list need to match the replacements in the feminine list
'i.e. MWords = "boy,his", FWords ="girl,her" NOT MWords = "his,boy", FWords ="girl,her"
MWords = "boy,his,he,by him,of him,by himself"
FWords = "girl,her,she,by her,of her,by herself"

'Make two arrays
Dim M, F
M = Split(MWords, ",")
F = Split(FWords, ",")

Options.DefaultHighlightColorIndex = wdYellow
With Selection.Find

'loop through all words in the array, since they have the same list length, only need to choose one.
    For I = 1 To UBound(M)
        If Gender = 1 Then 'If boy then change feminine words to masculine words
            .Text = F(I - 1)
            .Replacement.Text = M(I - 1)
        Else 'If girl then change masculine words to feminine words
            .Text = M(I - 1)
            .Replacement.Text = F(I - 1)
        End If
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
