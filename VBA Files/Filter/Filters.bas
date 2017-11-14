Attribute VB_Name = "Filters"
Public Function rangeIsEmpty(range As range) As Boolean
    'returns if a range has no text / numbers in it.
    If (WorksheetFunction.CountA(range) = 0) Then
        rangeIsEmpty = True
    Else
        rangeIsEmpty = False
    End If
End Function

Function isInRange(Range1 As range, Range2 As range) As Boolean
    'returns if range1 is within range2.
    isInRange = Not (Application.Intersect(Range1, Range2) Is Nothing)
End Function
