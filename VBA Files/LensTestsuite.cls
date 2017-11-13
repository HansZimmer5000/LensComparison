VERSION 1.0 CLASS
BEGIN
  MultiUse = -1  'True
END
Attribute VB_Name = "LensTestsuite"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = False
Attribute VB_Exposed = False
' This module has test for the Lens class.

Private lensWithFullInfo1RowRange as Range

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
Private lensWithFullInfo1Brand as String
Private lensWithFullInfo1AFCode as String
Private lensWithFullInfo1HasVR as Boolean

Private lensWithAllExceptMagnificationSensorInfo1Magnification as Double
Private lenswithAllExceptMagnificationSensorInfo1Sensor as String

Private lensWithFullInfo1 As lens
Private lensWithAllExceptFilterInfo1 As lens
Private lensWithAllExceptfilterMagnificationInfo1 As lens
Private lensWithallExceptMagnificationSensorInfo1 As lens


Private Sub Class_Initialize()
End Sub

Function testAllCases()
    Debug.Print(Str(Now) + " Starting LensTestsuite")

    Call testPosGetFullInfo1Lensname
    Call testPosGetFullInfo1FocalStart
    Call testPosGetFullInfo1FocalEnd
    Call testPosGetFullInfo1ApertureStart
    Call testPosGetFullInfo1ApertureEnd
    Call testPosGetFullInfo1Filter
    Call testPosGetFullInfo1Magnification
    Call testPosGetFullInfo1Mount
    Call testPosGetFullInfo1Sensor
    Call testPosGetFullInfo1Weight
    Call testPosGetFullInfo1Diameter
    Call testPosGetFullInfo1Length
    Call testPosGetFullInfo1Brand
    Call testPosGetFullInfo1AFCode
    Call testPosGetFullInfo1HasVR

    Call testPosGetWithAllExceptMagnificationSensorInfo1Magnification()
    Call testPosGetWithAllExceptMagnificationSensorInfo1Sensor()

    Call testPosEqualsFullInfo1()
    Call testNegEqualsNothing()
    Call testNegEqualsString()
End Function

Private Function setUp()
    Set lensWithFullInfo1RowRange = getLensWithFullInfo1RowRange()

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
    lensWithFullInfo1Brand = getLensWithFullInfo1Brand()
    lensWithFullInfo1AFCode = getLensWithFullInfo1AFCode()
    lensWithFullInfo1HasVR = getLensWithFullInfo1HasVR()
    

    lensWithAllExceptMagnificationSensorInfo1Magnification = getLensWithAllExceptMagnificationSensorInfo1Magnification()
    lenswithAllExceptMagnificationSensorInfo1Sensor = getLensWithAllExceptMagnificationSensorInfo1Sensor()

    Set lensWithFullInfo1 = getLensWithFullInfo1()
    Set lensWithAllExceptFilterInfo1 = getLensWithAllExceptFilterInfo1()
    Set lensWithAllExceptfilterMagnificationInfo1 = getLensWithAllExceptFilterMagnificationInfo1()
    Set lensWithallExceptMagnificationSensorInfo1 = getLensWithAllExceptMagnificationSensorInfo1()
End Function

Private Function tearDown()

End Function

Private Function testPosGetFullInfo1Lensname()
    Call setUp
    Dim result As Boolean

    result = StrComp(lensWithFullInfo1Lensname, lensWithFullInfo1.getLensName) = 0
    Call printAndAssert("testPosGetFullInfo1Lensname", result)
    
    Call tearDown
End Function

Private Function testPosGetFullInfo1FocalStart()
    Call setUp
    Dim result As Boolean

    result = lensWithFullInfo1FocalStart = lensWithFullInfo1.getFocalLengthStart
    Call printAndAssert("testPosGetFullInfo1FocalStart", result)
    
    Call tearDown
End Function

Private Function testPosGetFullInfo1FocalEnd()
    Call setUp
    Dim result As Boolean

    result = lensWithFullInfo1FocalEnd = lensWithFullInfo1.getFocalLengthEnd
    Call printAndAssert("testPosGetFullInfo1FocalEnd", result)
    
    Call tearDown
End Function

Private Function testPosGetFullInfo1ApertureStart()
    Call setUp
    Dim result As Boolean

    result = lensWithFullInfo1ApertureStart = lensWithFullInfo1.getApertureStart
    Call printAndAssert("testPosGetFullInfo1ApertureStart", result)
    
    Call tearDown
End Function

Private Function testPosGetFullInfo1ApertureEnd()
    Call setUp
    Dim result As Boolean

    result = lensWithFullInfo1ApertureEnd = lensWithFullInfo1.getApertureEnd
    Call printAndAssert("testPosGetFullInfo1ApertureEnd", result)
    
    Call tearDown
End Function

Private Function testPosGetFullInfo1Filter()
    Call setUp
    Dim result As Boolean

    result = lensWithFullInfo1Filter = lensWithFullInfo1.getFilterSize
    Call printAndAssert("testPosGetFullInfo1Filter", result)
    
    Call tearDown
End Function

Private Function testPosGetFullInfo1Magnification()
    Call setUp
    Dim result As Boolean

    result = lensWithFullInfo1Magnification = lensWithFullInfo1.getMagnification
    Call printAndAssert("testPosGetFullInfo1Magnification", result)
    
    Call tearDown
End Function

Private Function testPosGetFullInfo1Mount()
    Call setUp
    Dim result As Boolean

    result = StrComp(lensWithFullInfo1Mount, lensWithFullInfo1.getMount) = 0
    Call printAndAssert("testPosGetFullInfo1Mount", result)
    
    Call tearDown
End Function

Private Function testPosGetFullInfo1Sensor()
    Call setUp
    Dim result As Boolean

    result = StrComp(lensWithFullInfo1Sensor, lensWithFullInfo1.getSensorCompatibility) = 0
    Call printAndAssert("testPosGetFullInfo1Sensor", result)
    
    Call tearDown
End Function

Private Function testPosGetFullInfo1Weight()
    Call setUp
    Dim result As Boolean

    result = lensWithFullInfo1Weight = lensWithFullInfo1.getWeight
    Call printAndAssert("testPosGetFullInfo1Weight", result)
    
    Call tearDown
End Function

Private Function testPosGetFullInfo1Diameter()
    Call setUp
    Dim result As Boolean

    result = lensWithFullInfo1Diameter = lensWithFullInfo1.getDiameter
    Call printAndAssert("testPosGetFullInfo1Diameter", result)
    
    Call tearDown
End Function

Private Function testPosGetFullInfo1Length()
    Call setUp
    Dim result As Boolean

    result = lensWithFullInfo1Length = lensWithFullInfo1.getLength
    Call printAndAssert("testPosGetFullInfo1Length", result)
    
    Call tearDown
End Function

Private Function testPosGetFullInfo1Brand()
    Call setUp
    Dim result as Boolean

    result = StrComp(lensWithFullInfo1Brand, lensWithFullInfo1.getBrand()) = 0
    Call printAndAssert("testPosGetFullInfo1Brand",result)

    Call tearDown
End Function

Private Function testPosGetFullInfo1AFCode()
    Call setUp
    Dim result as Boolean

    result = lensWithFullInfo1AFCode = lensWithFullInfo1.getAFCode()
    Call printAndAssert("testPosGetFullInfo1AFCode",result)

    Call tearDown
End Function

Private Function testPosGetFullInfo1HasVR()
    Call setUp
    Dim result as Boolean

    result = lensWithFullInfo1HasVR And lensWithFullInfo1.hasVR()
    Call printAndAssert("testPosGetFullInfo1HasVR",result)

    Call tearDown
End Function






Private Function testPosGetWithAllExceptMagnificationSensorInfo1Magnification()
    Call setUp
    Dim result As Boolean

    result = lensWithAllExceptMagnificationSensorInfo1Magnification = lensWithallExceptMagnificationSensorInfo1.getMagnification
    Call printAndAssert("testPosGetWithAllExceptMagnificationSensorInfo1Magnification", result)
    
    Call tearDown
End Function

Private Function testPosGetWithAllExceptMagnificationSensorInfo1Sensor()
    Call setUp
    Dim result As Boolean

    result = StrComp(lenswithAllExceptMagnificationSensorInfo1Sensor,lensWithallExceptMagnificationSensorInfo1.getSensorCompatibility()) = 0
    Call printAndAssert("testPosGetWithAllExceptMagnificationSensorInfo1Sensor", result)
    
    Call tearDown
End Function

Private Function testPosEqualsFullInfo1()
    Call setUp
    Dim result As Boolean

    result = lensWithFullInfo1.equals(lensWithFullInfo1)
    Call printAndAssert("testPosEqualsFullInfo1", result)
    
    Call tearDown
End Function

Private Function testPosEqualslensWithAllExceptFilterInfo1()
    Call setUp
    Dim result As Boolean

    result = lensWithAllExceptFilterInfo1.equals(lensWithAllExceptFilterInfo1)
    Call printAndAssert("testPosEqualslensWithAllExceptFilterInfo1", result)
    
    Call tearDown
End Function

Private Function testPosEqualslensWithAllExceptMagnificationSensorInfo1()
    Call setUp
    Dim result As Boolean

    result = lensWithAllExceptMagnificationSensorInfo1.equals(lensWithAllExceptMagnificationSensorInfo1)
    Call printAndAssert("testPosEqualslensWithAllExceptMagnificationSensorInfo1", result)
    
    Call tearDown
End Function

Private Function testNegEqualsNothing()
    Call setUp
    Dim result As Boolean

    result = lensWithFullInfo1.equals(Nothing)
    Call printAndAssert("testNegEqualsNothing", result)
    
    Call tearDown
End Function

Private Function testNegEqualsString()
    Call setUp
    Dim result As Boolean

    result = lensWithFullInfo1.equals("2")
    Call printAndAssert("testNegEqualsString", result)
    
    Call tearDown
End Function