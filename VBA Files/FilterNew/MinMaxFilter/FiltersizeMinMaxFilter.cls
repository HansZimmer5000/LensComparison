VERSION 1.0 CLASS
BEGIN
  MultiUse = -1  'True
END
Attribute VB_Name = "FiltersizeMinMaxFilter"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = False
Attribute VB_Exposed = False
'This is a Interface.

Public Property Get getMinValue() as Double
End Property

Public Property Get getMaxValue() As Double
End Property

Public Function Init(newNameCell As range, newMinValueCell As range, newMaxValueCell As range)
End Function

Public Function isSet() As Boolean
End Function

Public Function lensMatchTheMinMaxFilter(lens As Lens) As Boolean
End Function