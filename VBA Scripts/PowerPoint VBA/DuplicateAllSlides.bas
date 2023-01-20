Attribute VB_Name = "DuplicateAllSlides"
Sub DuplicateAllSlides()
'Written By Ahmad Cooper
'Code comes 'as is', no warranty

Dim i, j As Long: j = 1
For i = 1 To ActivePresentation.Slides.count
On Error Resume Next
Set newSlide = ActivePresentation.Slides(j).Duplicate
j = j + 2
Set newSlide = ActivePresentation.Slides(j)
Next i
End Sub
