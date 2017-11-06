Attribute VB_Name = "Tests"


Sub loadNewLensesAccordingToFilters()
    Dim myFiltersTable As FiltersTable
    Dim myRawDataTable As rawDataTable
    Dim myResultTable As ResultTable
    Dim rawSheet As Worksheet
    
    Set rawSheet = ActiveWorkbook.Sheets("RawData")
    Set myFiltersTable = CreateFiltersTable(range("B3", "D11"), range("F3", "O7"))
    Set myRawDataTable = CreateRawDataTable(rawSheet.range("A2", "Q2"))
    Set myResultTable = CreateResultTable(range("B16", "M999"), myRawDataTable, myFiltersTable)
End Sub

Sub testAll()
    Dim myTestSuiteLens As testSuiteLens: Set myTestSuiteLens = New testSuiteLens
    
    Call myTestSuiteLens.testAllCases
End Sub
