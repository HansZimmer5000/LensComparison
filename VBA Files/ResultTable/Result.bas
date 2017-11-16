Attribute VB_Name = "Result"

Sub loadNewLensesAccordingToFilters()
    Dim myFiltersTable As FiltersTable
    Dim myRawDataTable As rawDataTable
    Dim myResultTable As ResultTable
    Dim rawSheet As Worksheet
    Dim overviewSheet as Worksheet
    
    Set rawSheet = getRawDataSheet()
    Set overviewSheet = getOverviewSheet()
    Set myFiltersTable = CreateFiltersTable(overviewSheet.range("B3", "D11"), overviewSheet.range("F3", "O7"))
    Set myRawDataTable = CreateRawDataTable(rawSheet.range("A2", "Q2"))
    Set myResultTable = CreateResultTable(overviewSheet.range("B16", "M999"), myRawDataTable, myFiltersTable)

    myResultTable.updateResultTable()
End Sub


