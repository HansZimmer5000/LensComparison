Attribute VB_Name = "Filters"

Public Function rangeIsEmpty(range As range) As Boolean
    'returns if a range has no text / numbers in it.
    If (WorksheetFunction.CountA(range) = 0) Then
        rangeIsEmpty = True
    Else
        rangeIsEmpty = False
    End If
End Function