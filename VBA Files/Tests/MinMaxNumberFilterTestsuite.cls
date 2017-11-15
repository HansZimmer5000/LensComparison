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

Private minMaxNumberFilter3 as MinMaxNumberFilter
Private minMaxNumberFilter3NameRange as Range
Private minMaxNumberFilter3MinValueRange as Range
Private minMaxnumberFilter3MaxValueRange as Range

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

    Call testPosGetMinMaxNumberFilter3Name
    Call testPosGetMinMaxNumberFilter3MinValue
    Call testPosGetMinMaxNumberFilter3MaxValue
    Call testNegGetMinMaxnumberFilter3IsSet
    Call testPosGetMinMaxNumberFilter3LensMatchTheMinMaxFilterLens1
    Call testPosGetMinMaxNumberFilter3LensMatchTheMinMaxFilterLens2
End Function

Private Function setUp()
    Set minMaxNumberFilter1 = getMinMaxNumberFilter1
    Set minMaxNumberFilter1NameRange = getMinMaxNumberFilter1NameRange
    Set minMaxNumberFilter1MinValueRange = getMinMaxNumberFilter1MinValueRange
    Set minMaxnumberFilter1MaxValueRange = getMinMaxNumberFilter1MaxValueRange

    Set minMaxNumberFilter3 = getMinMaxNumberFilter3
    Set minMaxNumberFilter3NameRange = getMinMaxNumberFilter3NameRange
    Set minMaxNumberFilter3MinValueRange = getMinMaxNumberFilter3MinValueRange
    Set minMaxnumberFilter3MaxValueRange = getMinMaxNumberFilter3MaxValueRange

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




Private Function testPosGetMinMaxNumberFilter3Name()
    Call setUp
    Dim result As Boolean

    result = StrComp(minMaxNumberFilter3NameRange.Text, minMaxNumberFilter3.getName) = 0
    Call printAndAssert("testPosGetMinMaxNumberFilter3Name", result)
End Function

Private Function testPosGetMinMaxNumberFilter3MinValue()
    Call setUp
    Dim result As Boolean

    result = getMinMaxNumberFilterMinDefaultValue = minMaxNumberFilter3.getMinValue
    Call printAndAssert("testPosGetMinMaxNumberFilter3MinValue", result)
End Function

Private Function testPosGetMinMaxNumberFilter3MaxValue()
    Call setUp
    Dim result As Boolean

    result = getMinMaxNumberFilterMaxDefaultValue = minMaxNumberFilter3.getMaxValue
    Call printAndAssert("testPosGetMinMaxNumberFilter3MaxValue", result)
End Function

Private Function testNegGetMinMaxNumberFilter3IsSet()
    Call setUp
    Dim result As Boolean

    result = minMaxNumberFilter3.isSet()
    Call printAndAssert("testNegGetMinMaxNumberFilter3IsSet", result)   
End Function

Private Function testPosGetMinMaxNumberFilter3LensMatchTheMinMaxFilterLens1()
    Call setUp
    Dim result As Boolean

    result = minMaxNumberFilter3.lensMatchTheMinMaxFilter(lens1)
    Call printAndAssert("testPosGetMinMaxNumberFilter3LensMatchTheMinMaxFilterLens1", result)   
End Function

Private Function testPosGetMinMaxNumberFilter3LensMatchTheMinMaxFilterLens2()
    Call setUp
    Dim result As Boolean

    result = minMaxNumberFilter3.lensMatchTheMinMaxFilter(lens2)
    Call printAndAssert("testPosGetMinMaxNumberFilter3LensMatchTheMinMaxFilterLens2", result)   
End Function