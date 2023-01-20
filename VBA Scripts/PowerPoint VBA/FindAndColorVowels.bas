Attribute VB_Name = "FindAndColorVowels"
Sub FindAndColorVowels()
'Written by Ahmad Cooper
'NOTE Does not look in Tables, Smart art etc
Dim oPres As Presentation
Dim oSl As Slide
Dim oSh As Shape
Dim oTR, oTR_Temp As TextRange
Dim i As Long
Dim ColorS, words As String

Dim WordArr, ColorArr
'The colours and words should have the same length
'Use long color codes: orange, red, pink, green, blue
ColorS = "39423,255,16711935,65280,16763904"
words = "a,e,i,o,u"

WordArr = Split(words, ",")
ColorArr = Split(ColorS, ",")
For i = 0 To UBound(WordArr)
For Each oPres In Application.Presentations
     For Each oSl In oPres.Slides
        For Each oSh In oSl.Shapes
            If oSh.HasTextFrame Then
        If oSh.TextFrame.HasText Then
            Set oTR = oSh.TextFrame.TextRange
            Set oTR_Temp = oTR.Find(FindWhat:=WordArr(i), MatchCase:=False, WholeWords:=False)
            If Not oTR_Temp Is Nothing Then oTR_Temp.Font.Color.RGB = ColorArr(i)
           Do While Not oTR_Temp Is Nothing
           Set oTR_Temp = oTR.Find(FindWhat:=WordArr(i), _
           After:=oTR_Temp.start + oTR_Temp.Length, MatchCase:=False, WholeWords:=False)
           If Not oTR_Temp Is Nothing Then oTR_Temp.Font.Color.RGB = ColorArr(i)
           Loop
       End If
    End If
        Next oSh
    Next oSl
Next oPres
Next i
End Sub

