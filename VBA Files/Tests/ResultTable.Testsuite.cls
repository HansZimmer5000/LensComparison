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
    Debug.Print(Str(Now) + " Starting ResultTableTestsuite")
    Call testPosUpdateResultTable1()
End Function

Private Function setUp()
    Set lensWithFullInfo1 = getLensWithFullInfo1()
    Set lensWithAllExceptFilterInfo1 = getLensWithAllExceptFilterInfo1()
    Set lensWithAllExceptfilterMagnificationInfo1 = getLensWithAllExceptFilterMagnificationInfo1()
    Set lensWithAllExceptMagnificationSensorInfo1 = getLensWithAllExceptMagnificationSensorInfo1()

    Set resultTable1 = getResultTable1()

    Set resultTable1Range = getResultTable1Range()
End Function

Private Function testPosUpdateResultTable1()
    Call setUp
    Dim result as Boolean
    Dim currentFilteredLenses as Collection
    Dim currentRowRange as Range

    Set currentFilteredLenses = New Collection
    Call resultTable1.updateResultTable()

    For each currentRowRange in resultTable1Range.rows
        if(currentRowRange.columns(1).Text <> "") Then
            currentFilteredLenses.Add CreateLensFromRow(currentRowRange)
        End If
    Next

    result = collectionsAreEqual(getResultTable1FilteredLenses(), currentFilteredLenses)

    Call printAndAssert("testPosUpdateResultTable1", result)
End Function
