Attribute VB_Name = "Result"

Sub loadNewLensesAccordingToFilters()
    Dim myFiltersTable As FiltersTable
    Dim myRawDataTable As rawDataTable
    Dim myResultTable As ResultTable
    Dim preparedDataSheet As Worksheet
    Dim overviewSheet as Worksheet
    
    Set preparedDataSheet = getPreparedDataSheet()
    Set overviewSheet = getOverviewSheet()
    Set myFiltersTable = CreateFiltersTable(overviewSheet.range("B3", "D10"), overviewSheet.range("F3", "O7"))
    Set myRawDataTable = CreateRawDataTable(preparedDataSheet.range("A2", "M2"))
    Set myResultTable = CreateResultTable(overviewSheet.range("B17", "N999"), myRawDataTable, myFiltersTable)

    Call myResultTable.updateResultTable()
End Sub


