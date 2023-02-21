Sub PrintColorIndexTable()
    Dim i, r, g, b As Long
    
    For i = 1 To 1000
        With Cells(Int((i - 1) / 8) + 1, (i - 1) Mod 8 + 1)
            .Interior.Color = RGB(r, g, b)
          ;  .Value = "Color " & i & ": " & Hex(.Interior.Color)
        End With
        
        ' Update RGB values for next color
        b = b + 3
        If b > 255 Then
            b = 0
            g = g + 3
        End If
        If g > 255 Then
            g = 0
            r = r + 3
        End If
        If r > 255 Then
            Exit For
        End If
    Next i
End Sub
