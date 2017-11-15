VERSION 1.0 CLASS
BEGIN
  MultiUse = -1  'True
END
Attribute VB_Name = "FiltersTableTestsuite"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = False
Attribute VB_Exposed = False
' Class contains all Tests for the FiltersTable

Private filtersTable1 as FiltersTable

Private allMinMaxNumberFilters as Collection
Private allMultipleStringFilters as Collection

Private Sub Class_Initialize()
End Sub

Function testAllCases()
    Debug.Print(Str(Now) + " Starting FiltersTableTestsuite")

    Call testPosGetFiltersTable1AllMinMaxNumberFilters
    Call testPosGetFiltersTable1AllMultipleStringFilters
End Function

Private Function setUp()
    Set filtersTable1 = getFiltersTable1

    Set allMinMaxNumberFilters = getAllMinMaxNumberFilters
    Set allMultipleStringFilters = getAllMultipleStringFilters
End Function

Private Function testPosGetFiltersTable1AllMinMaxNumberFilters()
    Call setUp
    Dim result as Boolean

    result = collectionsAreEqual(allMinMaxNumberFilters, filtersTable1.getAllMinMaxNumberFilters())
    Call printAndAssert("testPosGetFiltersTable1AllMinMaxNumberFilters", result)
End Function

Private Function testPosGetFiltersTable1AllMultipleStringFilters()
    Call setUp
    Dim result as Boolean

    result =  collectionsAreEqual(allMultipleStringFilters, filtersTable1.getAllMultipleStringFilters())
    Call printAndAssert("testPosGetFiltersTable1AllMultipleStringFilters", result)
End Function 