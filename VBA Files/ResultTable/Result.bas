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


Public Function valueRangeIsBetweenMinMax(valueRangeStart As Double, valueRangeEnd As Double, min As Double, max As Double) As Boolean
    If (singleValueIsBetweenMinMax(valueRangeStart, min, max) And _
        singleValueIsBetweenMinMax(valueRangeEnd, min, max)) Then
        valueRangeIsBetweenMinMax = True
    Else
        valueRangeIsBetweenMinMax = False
    End If
End Function

Public Function singleValueIsBetweenMinMax(value As Double, min As Double, max As Double) As Boolean
    If (value >= min And value <= max) Then
        singleValueIsBetweenMinMax = True
    Else
        singleValueIsBetweenMinMax = False
    End If
End Function

Public Function stringMatchesAtLeastOneValue(value As String, activeFilterValues As Collection) As Boolean
    Dim currentFilterString As String
    Dim currentIteration As Integer
    
    For currentIteration = 1 To activeFilterValues.Count
        currentFilterString = activeFilterValues.Item(currentIteration)

        If (InStr(value, currentFilterString) > 0) Then
            stringMatchesAtLeastOneValue = True
            Exit Function
        End If
    Next
    stringMatchesAtLeastOneValue = False
End Function

