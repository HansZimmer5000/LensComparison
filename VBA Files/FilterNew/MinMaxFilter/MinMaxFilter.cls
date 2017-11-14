VERSION 1.0 CLASS
BEGIN
  MultiUse = -1  'True
END
Attribute VB_Name = "MinMaxFilter"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = False
Attribute VB_Exposed = False
'This is a Interface/Base class mix.

Private minValue As Double
Private maxValue As Double
Private minValueCell As range
Private maxValueCell As range

Const minDefaultValue As Double = 0
Const maxDefaultValue As Double = 9999

Public Property Get getMinValue() As Double
    If (Not rangeIsEmpty(minValueCell)) Then
        minValue = minValueCell.value
    Else
        minValue = minDefaultValue
    End If
    getMinValue = minValue
End Property

Public Property Get getMaxValue() As Double
    If (Not rangeIsEmpty(maxValueCell)) Then
        maxValue = maxValueCell.value
    Else
        maxValue = maxDefaultValue
    End If
    getMaxValue = maxValue
End Property

Private Sub Class_Initialize()
    minValue = minDefaultValue
    maxValue = maxDefaultValue
End Sub

Public Function Init(newMinValueCell As range, newMaxValueCell As range)
    Set minValueCell = newMinValueCell
    Set maxValueCell = newMaxValueCell
    If (Not rangeIsEmpty(newMinValueCell)) Then
        minValue = newMinValueCell.value
    End If
    If (Not rangeIsEmpty(newMaxValueCell)) Then
        maxValue = newMaxValueCell.value
    End If
End Function

Public Function isSet() As Boolean
    'returns if at least one value is set.
    If (rangeIsEmpty(minValueCell) And rangeIsEmpty(maxValueCell)) Then
        isSet = False
    Else
        isSet = True
    End If
End Function

Public Function lensMatchTheMinMaxFilter(lens As lens) As Boolean
End Function
