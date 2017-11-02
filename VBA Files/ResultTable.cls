VERSION 1.0 CLASS
BEGIN
  MultiUse = -1  'True
END
Attribute VB_Name = "ResultTable"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = False
Attribute VB_Exposed = False
' Class to hold all Lenses and update the table due to filters

Private tableRange As range
Private resultLenses As Collection
Private rawDataLenses As Collection
Private rawDataTable As rawDataTable
Private filterTable As FiltersTable

Private Sub Class_Initialize()
End Sub

Public Function Init(newTableRange As range, newRawDataTable As rawDataTable, _
                        newFiltersTable As FiltersTable)
    Set tableRange = newTableRange
    Set rawDataTable = newRawDataTable
    Set filterTable = newFiltersTable
    
    Set resultLenses = New Collection
    Call updateResultTable
End Function

Public Function updateResultTable()
    
    Dim activeMinMaxFilters As Collection
    Dim activeMultipleFilters As Collection
    
    Set activeMinMaxFilters = filterTable.getAllMinMaxNumberFilters
    Set activeMultipleFilters = filterTable.getAllMultipleStringFilters

    Call filterRawDataLanesesAndSetResultLenses(activeMinMaxFilters, activeMultipleFilters)
    Call writeLenses
End Function

Private Function filterRawDataLanesesAndSetResultLenses(minMaxFilters As Collection, multipleFilters As Collection)
    Const NO_FILTERING As Boolean = False
    
    Dim currentResultLens As ResultLens
    Dim currentRawLens As RawDataLens
    Dim currentRawDataLens As RawDataLens

    'Get all RawDatalenses from RawDataTable, just do if no Data is there.
    If (rawDataLenses Is Nothing) Then
        Set rawDataLenses = rawDataTable.getAllRawDataLenses
    End If
    
    If (NO_FILTERING) Then
        For Each currentRawLens In rawDataLenses
            Set currentResultLens = CreateResultLensFromRawDataLens(currentRawLens)
            resultLenses.Add currentResultLens
        Next
    Else
        For Each currentRawLens In rawDataLenses
            Set currentResultLens = CreateResultLensFromRawDataLens(currentRawLens)
            If (resultLensMatchesAllMinMaxFilters(minMaxFilters, currentResultLens) And _
                resultLensMatchesAllMultipleFilters(multipleFilters, currentResultLens)) Then
                    resultLenses.Add currentResultLens
            End If
        Next
    End If
End Function

Private Function writeLenses()
    Dim currentInteration As Integer
    Dim currentRow As range
    Dim currentRawLens As ResultLens
    
    For currentInteration = 1 To resultLenses.Count
        Set currentRow = tableRange.Rows(currentInteration)
        Set currentRawLens = resultLenses.Item(currentInteration)

        With currentRow
            .Columns(1).value2 = currentRawLens.getLensName
            .Columns(2).value2 = currentRawLens.getFocalLengthStart
            .Columns(3).value2 = currentRawLens.getFocalLengthEnd
            .Columns(4).value2 = currentRawLens.getApertureStart
            .Columns(5).value2 = currentRawLens.getApertureEnd
            .Columns(6).value2 = currentRawLens.getFilterSize
            .Columns(7).value2 = currentRawLens.getMagnification
            .Columns(8).value2 = currentRawLens.getMount
            .Columns(9).value2 = currentRawLens.getSensorCompatibility
            .Columns(10).value2 = currentRawLens.getWeight
            .Columns(11).value2 = currentRawLens.getDiameter
            .Columns(12).value2 = currentRawLens.getLength
        End With
    Next
    
    Call clearRestOfRange
End Function

Private Function resultLensMatchesAllMinMaxFilters(minMaxFilters As Collection, lens As ResultLens) As Boolean
    Dim currentMinMaxFilter As MinMaxNumberFilter

    For Each currentMinMaxFilter In minMaxFilters
        If (currentMinMaxFilter.isSet And resultLensMatchTheMinMaxFilter(lens, currentMinMaxFilter)) Then
            resultLensMatchesAllMinMaxFilters = True
        ElseIf (Not currentMinMaxFilter.isSet) Then
            resultLensMatchesAllMinMaxFilters = True
        Else
            resultLensMatchesAllMinMaxFilters = False
            Exit Function
        End If
    Next
End Function

Private Function resultLensMatchesAllMultipleFilters(multipleFilters As Collection, lens As ResultLens) As Boolean
    Dim currentMultipleFilter As MultipleStringFilter

    For Each currentMultipleFilter In multipleFilters
        If (currentMultipleFilter.isSet And resultLensMatchTheMultipleFilter(lens, currentMultipleFilter)) Then
            resultLensMatchesAllMultipleFilters = True
        ElseIf (Not currentMultipleFilter.isSet) Then
            resultLensMatchesAllMultipleFilters = True
        Else
            resultLensMatchesAllMultipleFilters = False
            Exit Function
        End If
    Next
End Function

Private Function clearRestOfRange()
    Dim firstCellWithoutData As range
    Dim lastCellWithoutData As range
    Dim rangeWithoutData As range
    
    Set firstCellWithoutData = tableRange.Rows(1).Columns(1).Offset(resultLenses.Count, 0)
    Set lastCellWithoutData = tableRange.Rows(tableRange.Rows.Count).Columns(tableRange.Columns.Count).Offset(resultLenses.Count, 0)
    Set rangeWithoutData = firstCellWithoutData.Parent.range(firstCellWithoutData, lastCellWithoutData)
    
    rangeWithoutData.value2 = ""
End Function



