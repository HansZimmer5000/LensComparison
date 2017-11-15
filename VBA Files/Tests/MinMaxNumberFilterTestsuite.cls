VERSION 1.0 CLASS
BEGIN
  MultiUse = -1  'True
END
Attribute VB_Name = "MinMaxNumberfilterTestsuite"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = False
Attribute VB_Exposed = False
' Class contains all Tests for the FiltersTable

Private minMaxNumberFilter1 as MinMaxNumberFilter
Private minMaxNumberFilter1NameRange as Range
Private minMaxNumberFilter1MinValueRange as Range
Private minMaxnumberFilter1MaxValueRange as Range

Private minMaxNumberFilterMinDefaultValue as Double
Private minMaxNumberfilterMaxDefaultValue as Double

Private lens1 as Lens
Private lens2 as Lens

Private Sub Class_Initialize()
End Sub

Function testAllCases()
    Debug.Print(Str(Now) + " Starting MinMaxNumberfilterTestsuite")

    Call testPosGetMinMaxNumberFilter1Name
    Call testPosGetMinMaxNumberFilter1MinValue
    Call testPosGetMinMaxNumberFilter1MaxValue
    Call testPosGetMinMaxNumberFilter1IsSet
    Call testNegGetMinMaxnumberFilter1IsSet
    Call testPosGetMinMaxNumberFilter1LensMatchTheMinMaxFilter
    Call testNegGetMinMaxNumberFilter1LensMatchTheMinMaxFilter
End Function

Private Function setUp()
    Set minMaxNumberFilter1 = getMinMaxNumberFilter1
    Set minMaxNumberFilter1NameRange = getMinMaxNumberFilter1NameRange
    Set minMaxNumberFilter1MinValueRange = getMinMaxNumberFilter1MinValueRange
    Set minMaxnumberFilter1MaxValueRange = getMinMaxNumberFilter1MaxValueRange

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

Private Function testPosGetMinMaxNumberFilter1LensMatchTheMinMaxFilter()
    Call setUp
    Dim result As Boolean

    result = minMaxNumberFilter1.lensMatchTheMinMaxFilter(lens1)
    Call printAndAssert("testPosGetMinMaxNumberFilter1LensMatchTheMinMaxFilter", result)   
End Function

Private Function testNegGetMinMaxNumberFilter1LensMatchTheMinMaxFilter()
    Call setUp
    Dim result As Boolean

    result = minMaxNumberFilter1.lensMatchTheMinMaxFilter(lens2)
    Call printAndAssert("testNegGetMinMaxNumberFilter1LensMatchTheMinMaxFilter", result)   
End Function