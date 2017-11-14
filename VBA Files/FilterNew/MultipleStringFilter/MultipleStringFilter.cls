VERSION 1.0 CLASS
BEGIN
  MultiUse = -1  'True
END
Attribute VB_Name = "MultipleStringFilter"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = False
Attribute VB_Exposed = False
'This is a Interface.

Public Property Get getActiveValues() As Collection
End Property

Public Function Init(newNameCell As range, newValuesRow As range)
End Function

Public Function isSet() As Boolean
End Function

Public Function lensMatchTheMultipleFilter(lens As Lens) As Boolean
End Function