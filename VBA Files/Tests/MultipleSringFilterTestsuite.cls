VERSION 1.0 CLASS
BEGIN
  MultiUse = -1  'True
END
Attribute VB_Name = "MultipleStringFilterTestsuite"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = False
Attribute VB_Exposed = False
' Class contains all Tests for the MultipleStringFilter Class

Private multipleStringFilter1 as MultipleStringFilter
Private multipleStringFiter1NameRange as Range
Private multipleStringFilter1ValuesRow as Range 
Private multipleStringFilter1ActiveValues as Collection

Private lens1 as Lens
Private lens4 as Lens

Private Sub Class_Initialize()
End Sub

Function testAllCases()
    Debug.Print(Str(Now) + " Starting MultipleStringFilterTestsuite")

    Call testPosGetMultipleStringFilter1Name
    Call testPosGetMultipleStringFilter1ActiveValues
    Call testPosGetMultipleStringFilter1IsSet
    Call testPosGetMultipleStringFilter1LensMatchTheMultipleFilterLens1
    Call testNegGetMultipleStringFilter1LensMatchTheMultipleFilterLens4
End Function

Private Function setUp()
    Set multipleStringFilter1 = getMultipleStringFilter1
    Set multipleStringFiter1NameRange = getMultipleStringFilter1NameRange() 
    Set multipleStringFilter1ValuesRow = getMultipleStringFilter1ValuesRow() 
    Set multipleStringFilter1ActiveValues = getMultipleStringFilter1ActiveValues()

    Set lens1 = getLensWithFullInfo1
    Set lens4 = getLensWithAllExceptMagnificationSensorInfo1
End Function


Private Function testPosGetMultipleStringFilter1Name()
    Call setUp
    Dim result As Boolean

    result = StrComp(multipleStringFiter1NameRange.Text, multipleStringFilter1.getName) = 0
    Call printAndAssert("testPosGetMultipleStringFilter1Name", result)
End Function

Private Function testPosGetMultipleStringFilter1ActiveValues()
    Call setUp
    Dim result As Boolean
  
    result = collectionsAreEqual(multipleStringFilter1ActiveValues, multipleStringFilter1.getActiveValues())
    Call printAndAssert("testPosGetMultipleStringFilter1ActiveValues", result)
End Function

Private Function testPosGetMultipleStringFilter1IsSet()
    Call setUp
    Dim result As Boolean

    result = multipleStringFilter1.isSet()
    Call printAndAssert("testPosGetMultipleStringFilter1IsSet", result)
End Function

Private Function testPosGetMultipleStringFilter1LensMatchTheMultipleFilterLens1()
    Call setUp
    Dim result As Boolean

    result = multipleStringFilter1.lensMatchTheMultipleFilter(lens1)
    Call printAndAssert("testPosGetMultipleStringFilter1LensMatchTheMultipleFilterLens1", result)
End Function

Private Function testNegGetMultipleStringFilter1LensMatchTheMultipleFilterLens4()
    Call setUp
    Dim result As Boolean

    result = multipleStringFilter1.lensMatchTheMultipleFilter(lens4)
    Call printAndAssert("testNegGetMultipleStringFilter1LensMatchTheMultipleFilterLens4", result)
End Function