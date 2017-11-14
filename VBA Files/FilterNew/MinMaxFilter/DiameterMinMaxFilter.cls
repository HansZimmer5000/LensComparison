VERSION 1.0 CLASS
BEGIN
  MultiUse = -1  'True
END
Attribute VB_Name = "DiameterMinMaxFilter"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = False
Attribute VB_Exposed = False

Implements MinMaxFilter

Private superClass As MinMaxFilter

Public Property Get MinMaxFilter_getMinValue() As Double
    MinMaxFilter_getMinValue = superClass.getMinValue()
End Property

Public Property Get MinMaxFilter_getMaxValue() As Double
    MinMaxFilter_getMaxValue = superClass.getMaxValue()
End Property

Private Sub Class_Initialize()
    Set superClass = New MinMaxFilter
End Sub

Function MinMaxFilter_Init(range1 As range, range2 As range)
    Call superClass.Init(range1, range2)
End Function

Public Function MinMaxFilter_isSet() As Boolean
    MinMaxFilter_isSet = superClass.isSet()
End Function

Function MinMaxFilter_lensMatchTheMinMaxFilter(lens As lens) As Boolean
    'TODO
    MinMaxFilter_lensMatchTheMinMaxFilter = False
End Function