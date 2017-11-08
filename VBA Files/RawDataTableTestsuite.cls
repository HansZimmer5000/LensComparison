VERSION 1.0 CLASS
BEGIN
  MultiUse = -1  'True
END
Attribute VB_Name = "RawDataTableTestsuite"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = False
Attribute VB_Exposed = False
' Class contains all Tests for the RawDataTable

Private lensWithFullInfo1 As lens
Private lensWithAllExceptFilterInfo1 As lens
Private lensWithAllExceptfilterMagnificationInfo1 As lens
Private lensWithallExceptMagnificationSensorInfo1 As lens

Private rawDataTable1 as RawDataTable

Private rawDataTable1Range as Range

Private Sub Class_Initialize()
End Sub

Function testAllCases()
    Debug.Print(Str(Now) + " Starting RawDataTableTestsuite")
    Call testPosGetTable1Range
End Function

Private Function setUp()
    Set lensWithFullInfo1 = getLensWithFullInfo1()
    Set lensWithAllExceptFilterInfo1 = getLensWithAllExceptFilterInfo1()
    Set lensWithAsllExceptfilterMagnificationInfo1 = getLensWithAllExceptFilterMagnificationInfo1()
    Set lensWithallExceptMagnificationSensorInfo1 = getLensWithAllExceptMagnificationSensorInfo1()

    Set rawDataTable1 = getRawDataTable1()

    Set rawDataTable1Range = getRawDataTable1Range()
End Function

Private Function tearDown()

End Function

Private Function testPosGetTable1Range()
    Call setUp
    Dim result As Boolean

    result = StrComp(rawDataTable1Range.Address,rawDataTable1.getTableRange().Address) = 0
    Call printAndAssert("testPosGetTable1Range", result)
    
    Call tearDown
End Function