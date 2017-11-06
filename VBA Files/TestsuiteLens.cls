VERSION 1.0 CLASS
BEGIN
  MultiUse = -1  'True
END
Attribute VB_Name = "TestsuiteLens"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = False
Attribute VB_Exposed = False
' This module includes test for the ResutlLens class.



Private lensWithFullInfo1Lensname As String
Private lensWithFullInfo1FocalStart As Double
Private lensWithFullInfo1FocalEnd As Double
Private lensWithFullInfo1ApertureStart As Double
Private lensWithFullInfo1ApertureEnd As Double
Private lensWithFullInfo1Filter As Double
Private lensWithFullInfo1Magnification As Double
Private lensWithFullInfo1Mount As String
Private lensWithFullInfo1Sensor As String
Private lensWithFullInfo1Weight As Double
Private lensWithFullInfo1Diameter As Double
Private lensWithFullInfo1Length As Double
Private lensWithFullInfo1AllAttributes As Collection

Private lensWithFullInfo1 As lens
Private lensWithAllExceptFilterInfo1 As lens
Private lensWithAllExceptfilterMagnificationInfo1 As lens
Private lensWithallExceptMagnificationSensorInfo1 As lens


Private Sub Class_Initialize()
End Sub

Function testAllCases()
    Call testPosGetAllAttributes
End Function

Private Function printAndAssert(functionName As String, result As Boolean)
    If (result) Then
        Debug.Print (functionName + " Done.")
    Else
        Debug.Print (functionName + " FAIL!")
    End If
End Function


Private Function setUp()
    lensWithFullInfo1Lensname = getLensWithFullInfo1Lensname()
    lensWithFullInfo1FocalStart = getLensWithFullInfo1FocalStart()
    lensWithFullInfo1FocalEnd = getLensWithFullInfo1FocalEnd()
    lensWithFullInfo1ApertureStart = getLensWithFullInfo1ApertureStart()
    lensWithFullInfo1ApertureEnd = getLensWithFullInfo1ApertureEnd()
    lensWithFullInfo1Filter = getLensWithFullInfo1Filter()
    lensWithFullInfo1Magnification = getLensWithFullInfo1Magnification()
    lensWithFullInfo1Mount = getLensWithFullInfo1Mount()
    lensWithFullInfo1Sensor = getLensWithFullInfo1Sensor()
    lensWithFullInfo1Weight = getLensWithFullInfo1Weight()
    lensWithFullInfo1Diameter = getLensWithFullInfo1Diameter()
    lensWithFullInfo1Length = getLensWithFullInfo1Length()
    Set lensWithFullInfo1AllAttributes = New Collection
    lensWithFullInfo1AllAttributes.Add (lensWithFullInfo1Lensname)
    lensWithFullInfo1AllAttributes.Add (lensWithFullInfo1FocalStart)
    lensWithFullInfo1AllAttributes.Add (lensWithFullInfo1FocalEnd)
    lensWithFullInfo1AllAttributes.Add (lensWithFullInfo1ApertureStart)
    lensWithFullInfo1AllAttributes.Add (lensWithFullInfo1ApertureEnd)
    lensWithFullInfo1AllAttributes.Add (lensWithFullInfo1Filter)
    lensWithFullInfo1AllAttributes.Add (lensWithFullInfo1Magnification)
    lensWithFullInfo1AllAttributes.Add (lensWithFullInfo1Mount)
    lensWithFullInfo1AllAttributes.Add (lensWithFullInfo1Sensor)
    lensWithFullInfo1AllAttributes.Add (lensWithFullInfo1Weight)
    lensWithFullInfo1AllAttributes.Add (lensWithFullInfo1Diameter)
    lensWithFullInfo1AllAttributes.Add (lensWithFullInfo1Length)

    Set lensWithFullInfo1 = getLensWithFullInfo1()
    Set lensWithAllExceptFilterInfo1 = getLensWithAllExceptFilterInfo1()
    Set lensWithAllExceptfilterMagnificationInfo1 = getLensWithAllExceptFilterMagnificationInfo1()
    Set lensWithallExceptMagnificationSensorInfo1 = getLensWithAllExceptMagnificationSensorInfo1()
    
End Function

Private Function tearDown()

End Function

Private Function testPosGetAllAttributes()
    Call setUp
    
    Dim result As Boolean
    Dim returnValues As Collection
    Dim currentIndex As Integer
    Dim currentReturnValue As Variant
    Dim currentAttributeValue As Variant
    
    currentIndex = 1
    result = True
    Set returnValues = New Collection
    returnValues.Add (lensWithFullInfo1.getLensName)
    returnValues.Add (lensWithFullInfo1.getFocalLengthStart)
    returnValues.Add (lensWithFullInfo1.getFocalLengthEnd)
    returnValues.Add (lensWithFullInfo1.getApertureStart)
    returnValues.Add (lensWithFullInfo1.getApertureEnd)
    returnValues.Add (lensWithFullInfo1.getFilterSize)
    returnValues.Add (lensWithFullInfo1.getMagnification)
    returnValues.Add (lensWithFullInfo1.getMount)
    returnValues.Add (lensWithFullInfo1.getSensorCompatibility)
    returnValues.Add (lensWithFullInfo1.getWeight)
    returnValues.Add (lensWithFullInfo1.getDiameter)
    returnValues.Add (lensWithFullInfo1.getLength)
    
    While (currentIndex <= returnValues.Count)
        currentReturnValue = returnValues.Item(currentIndex)
        currentAttributeValue = lensWithFullInfo1AllAttributes.Item(currentIndex)
        
        If (TypeName(currentAttributeValue) = "str") Then
            Call printAndAssert("testPosGetAllAttributes" + Str(currentIndex), StrComp(currentAttributeValue, currentReturnValue) = 0)
        Else
            Call printAndAssert("testPosGetAllAttributes" + Str(currentIndex), currentAttributeValue = currentReturnValue)
        End If
        currentIndex = currentIndex + 1
    Wend

    Call tearDown
End Function
