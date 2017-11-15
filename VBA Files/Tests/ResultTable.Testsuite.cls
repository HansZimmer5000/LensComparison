VERSION 1.0 CLASS
BEGIN
  MultiUse = -1  'True
END
Attribute VB_Name = "ResultTableTestsuite"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = False
Attribute VB_Exposed = False
' Class contains all Tests for the ResultTable


Private lensWithFullInfo1 As lens
Private lensWithAllExceptFilterInfo1 As lens
Private lensWithAllExceptfilterMagnificationInfo1 As lens
Private lensWithallExceptMagnificationSensorInfo1 As lens

Private resultTable1 as ResultTable

Private resultTable1Range as Range

Private Sub Class_Initialize()
End Sub

Function testAllCases()
    Debug.Print(Str(Now) + " Starting RawDataTableTestsuite")
    Call testPosGetTable1Range
    Call testPosGetTable1AllLenses
    Call testPosGetTable1FilteredLenses
End Function

Private Function setUp()
    Set lensWithFullInfo1 = getLensWithFullInfo1()
    Set lensWithAllExceptFilterInfo1 = getLensWithAllExceptFilterInfo1()
    Set lensWithAllExceptfilterMagnificationInfo1 = getLensWithAllExceptFilterMagnificationInfo1()
    Set lensWithAllExceptMagnificationSensorInfo1 = getLensWithAllExceptMagnificationSensorInfo1()

    Set resultTable1 = getResultTable1()

    Set resultTable1Range = getResultTable1Range()
End Function

Private Function tearDown()

End Function