VERSION 1.0 CLASS
BEGIN
  MultiUse = -1  'True
END
Attribute VB_Name = "MinMaxNumberFilterTestsuite"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = False
Attribute VB_Exposed = False
' Class contains all Tests for the MinMaxNumberFilter class

Private minMaxNumberFilter1 as MinMaxNumberFilter
Private minMaxNumberFilter1NameRange as Range
Private minMaxNumberFilter1MinValueRange as Range
Private minMaxnumberFilter1MaxValueRange as Range

Private minMaxNumberFilter2 as MinMaxNumberFilter
Private minMaxNumberFilter2NameRange as Range
Private minMaxNumberFilter2MinValueRange as Range
Private minMaxnumberFilter2MaxValueRange as Range

Private minMaxNumberFilterMinDefaultValue as Double
Private minMaxNumberfilterMaxDefaultValue as Double

Private lens1 as Lens
Private lens2 as Lens

Private Sub Class_Initialize()
End Sub

Function testAllCases()
    Debug.Print(Str(Now) + " Starting MinMaxNumberFilterTestsuite")

    Call testPosGetMinMaxNumberFilter1Name
    Call testPosGetMinMaxNumberFilter1MinValue
    Call testPosGetMinMaxNumberFilter1MaxValue
    Call testPosGetMinMaxNumberFilter1IsSet
    Call testNegGetMinMaxnumberFilter1IsSet
    Call testPosGetMinMaxNumberFilter1LensMatchTheMinMaxFilterLens1
    Call testNegGetMinMaxNumberFilter1LensMatchTheMinMaxFilterLens2

    Call testPosGetMinMaxNumberFilter2Name
    Call testPosGetMinMaxNumberFilter2MinValue
    Call testPosGetMinMaxNumberFilter2MaxValue
    Call testPosGetMinMaxNumberFilter2IsSet
    Call testNegGetMinMaxnumberFilter2IsSet
    Call testPosGetMinMaxNumberFilter2LensMatchTheMinMaxFilterLens1
    Call testPosGetMinMaxNumberFilter2LensMatchTheMinMaxFilterLens2
End Function

Private Function setUp()
    Set minMaxNumberFilter1 = getMinMaxNumberFilter1
    Set minMaxNumberFilter1NameRange = getMinMaxNumberFilter1NameRange
    Set minMaxNumberFilter1MinValueRange = getMinMaxNumberFilter1MinValueRange
    Set minMaxnumberFilter1MaxValueRange = getMinMaxNumberFilter1MaxValueRange

    Set minMaxNumberFilter2 = getMinMaxNumberFilter2
    Set minMaxNumberFilter2NameRange = getMinMaxNumberFilter2NameRange
    Set minMaxNumberFilter2MinValueRange = getMinMaxNumberFilter2MinValueRange
    Set minMaxnumberFilter2MaxValueRange = getMinMaxNumberFilter2MaxValueRange

    minMaxNumberFilterMinDefaultValue = getMinMaxNumberFilterMinDefaultValue
    minmaxNumberFilterMaxDefaultValue = getMinMaxNumberFilterMaxDefaultValue

    Set lens1 = getLensWithFullInfo1
    Set lens2 = getLensWithAllExceptFilterInfo1
End Function

Private Function testPosGetMinMaxNumberFilter1Name()
    Call setUp
    Dim result As Boolean

    result = StrComp(minMaxNumberFilter1NameRange.Text, minMaxNumberFilter1.getName) = 0
    Call printAndAssert("testPosGetMinMaxNumberFilter1Name", result)
End Function

Private Function testPosGetMinMaxNumberFilter1MinValue()
    Call setUp
    Dim result As Boolean

    result = minMaxNumberFilter1MinValueRange.Value2 = minMaxNumberFilter1.getMinValue
    Call printAndAssert("testPosGetMinMaxNumberFilter1MinValue", result)
End Function

Private Function testPosGetMinMaxNumberFilter1MaxValue()
    Call setUp
    Dim result As Boolean

    result = minMaxNumberFilter1MaxValueRange.Value2 = minMaxNumberFilter1.getMaxValue
    Call printAndAssert("testPosGetMinMaxNumberFilter1MaxValue", result)
End Function

Private Function testPosGetMinMaxNumberFilter1IsSet()
    Call setUp
    Dim result As Boolean

    result = minMaxNumberFilter1.isSet()
    Call printAndAssert("testPosGetMinMaxNumberFilter1IsSet", result)   
End Function

Private Function testNegGetMinMaxNumberFilter1IsSet()
    Call setUp
    Dim result As Boolean

    result = Not(minMaxNumberFilter1.isSet())
    Call printAndAssert("testNegGetMinMaxNumberFilter1IsSet", result)   
End Function

Private Function testPosGetMinMaxNumberFilter1LensMatchTheMinMaxFilterLens1()
    Call setUp
    Dim result As Boolean

    result = minMaxNumberFilter1.lensMatchTheMinMaxFilter(lens1)
    Call printAndAssert("testPosGetMinMaxNumberFilter1LensMatchTheMinMaxFilterLens1", result)   
End Function

Private Function testNegGetMinMaxNumberFilter1LensMatchTheMinMaxFilterLens2()
    Call setUp
    Dim result As Boolean

    result = minMaxNumberFilter1.lensMatchTheMinMaxFilter(lens2)
    Call printAndAssert("testNegGetMinMaxNumberFilter1LensMatchTheMinMaxFilterLens2", result)   
End Function




Private Function testPosGetMinMaxNumberFilter2Name()
    Call setUp
    Dim result As Boolean

    result = StrComp(minMaxNumberFilter2NameRange.Text, minMaxNumberFilter2.getName) = 0
    Call printAndAssert("testPosGetMinMaxNumberFilter2Name", result)
End Function

Private Function testPosGetMinMaxNumberFilter2MinValue()
    Call setUp
    Dim result As Boolean

    result = getMinMaxNumberFilterMinDefaultValue = minMaxNumberFilter2.getMinValue
    Call printAndAssert("testPosGetMinMaxNumberFilter2MinValue", result)
End Function

Private Function testPosGetMinMaxNumberFilter2MaxValue()
    Call setUp
    Dim result As Boolean

    result = getMinMaxNumberFilterMaxDefaultValue = minMaxNumberFilter2.getMaxValue
    Call printAndAssert("testPosGetMinMaxNumberFilter2MaxValue", result)
End Function

Private Function testPosGetMinMaxNumberFilter2IsSet()
    Call setUp
    Dim result As Boolean

    result = Not(minMaxNumberFilter1.isSet())
    Call printAndAssert("testPosGetMinMaxNumberFilter2IsSet", result)   
End Function

Private Function testNegGetMinMaxNumberFilter2IsSet()
    Call setUp
    Dim result As Boolean

    result = minMaxNumberFilter2.isSet()
    Call printAndAssert("testNegGetMinMaxNumberFilter2IsSet", result)   
End Function

Private Function testPosGetMinMaxNumberFilter2LensMatchTheMinMaxFilterLens1()
    Call setUp
    Dim result As Boolean

    result = minMaxNumberFilter2.lensMatchTheMinMaxFilter(lens1)
    Call printAndAssert("testPosGetMinMaxNumberFilter2LensMatchTheMinMaxFilterLens1", result)   
End Function

Private Function testPosGetMinMaxNumberFilter2LensMatchTheMinMaxFilterLens2()
    Call setUp
    Dim result As Boolean

    result = minMaxNumberFilter2.lensMatchTheMinMaxFilter(lens2)
    Call printAndAssert("testPosGetMinMaxNumberFilter2LensMatchTheMinMaxFilterLens2", result)   
End Function