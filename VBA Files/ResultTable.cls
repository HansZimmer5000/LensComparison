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
Private filteredLenses As Collection
Private allLenses As Collection
Private rawDataTable As rawDataTable
Private filterTable As FiltersTable

Private Sub Class_Initialize()
End Sub

Public Function Init(newTableRange As range, newRawDataTable As rawDataTable, _
                        newFiltersTable As FiltersTable)
    Set tableRange = newTableRange
    Set rawDataTable = newRawDataTable
    Set filterTable = newFiltersTable
    
    Set filteredLenses = New Collection
    Call updateResultTable
End Function

Public Function updateResultTable()
    
    Dim activeMinMaxFilters As Collection
    Dim activeMultipleFilters As Collection
    
    Set activeMinMaxFilters = filterTable.getAllMinMaxNumberFilters
    Set activeMultipleFilters = filterTable.getAllMultipleStringFilters

    Call setAndFilterLenses(activeMinMaxFilters, activeMultipleFilters)
    Call writeLenses
End Function

Private Function setAndFilterLenses(minMaxFilters As Collection, multipleFilters As Collection)
    Const USE_FILERS As Boolean = True
    
    Dim currentLens As Lens

    'Get all Lenses from RawDataTable, just do if no Data is there.
    If (allLenses Is Nothing) Then
        Set allLenses = rawDataTable.getAllLenses
    End If
    
    If (USE_FILERS) Then
        For Each currentLens In allLenses
            If (lensMatchesAllMinMaxFilters(minMaxFilters, currentLens) And _
                lensMatchesAllMultipleFilters(multipleFilters, currentLens)) Then
                    filteredLenses.Add currentLens
            End If
        Next
    Else
        Set filteredLenses = allLenses
    End If
End Function

Private Function writeLenses()
    Dim currentInteration As Integer
    Dim currentRow As range
    Dim currentLens As Lens
    
    For currentInteration = 1 To filteredLenses.Count
        Set currentRow = tableRange.Rows(currentInteration)
        Set currentLens = filteredLenses.Item(currentInteration)

        With currentRow
            .Columns(1).value2 = currentLens.getLensName
            .Columns(2).value2 = currentLens.getFocalLengthStart
            .Columns(3).value2 = currentLens.getFocalLengthEnd
            .Columns(4).value2 = currentLens.getApertureStart
            .Columns(5).value2 = currentLens.getApertureEnd
            .Columns(6).value2 = currentLens.getFilterSize
            .Columns(7).value2 = currentLens.getMagnification
            .Columns(8).value2 = currentLens.getMount
            .Columns(9).value2 = currentLens.getSensorCompatibility
            .Columns(10).value2 = currentLens.getWeight
            .Columns(11).value2 = currentLens.getDiameter
            .Columns(12).value2 = currentLens.getLength
        End With
    Next
    
    Call clearRestOfRange
End Function

Private Function lensMatchesAllMinMaxFilters(minMaxFilters As Collection, lens As Lens) As Boolean
    Dim currentMinMaxFilter As MinMaxNumberFilter

    For Each currentMinMaxFilter In minMaxFilters
        If (currentMinMaxFilter.isSet And lensMatchTheMinMaxFilter(lens, currentMinMaxFilter)) Then
            lensMatchesAllMinMaxFilters = True
        ElseIf (Not currentMinMaxFilter.isSet) Then
            lensMatchesAllMinMaxFilters = True
        Else
            lensMatchesAllMinMaxFilters = False
            Exit Function
        End If
    Next
End Function

Private Function lensMatchesAllMultipleFilters(multipleFilters As Collection, lens As Lens) As Boolean
    Dim currentMultipleFilter As MultipleStringFilter

    For Each currentMultipleFilter In multipleFilters
        If (currentMultipleFilter.isSet And Not(lensMatchTheMultipleFilter(lens, currentMultipleFilter))) Then
            lensMatchesAllMultipleFilters = False
            Exit Function
        End If
    Next
    lensMatchesAllMultipleFilters = True
End Function

Private Function clearRestOfRange()
    Dim firstCellWithoutData As range
    Dim lastCellWithoutData As range
    Dim rangeWithoutData As range
    
    Set firstCellWithoutData = tableRange.Rows(1).Columns(1).Offset(filteredLenses.Count, 0)
    Set lastCellWithoutData = tableRange.Rows(tableRange.Rows.Count).Columns(tableRange.Columns.Count).Offset(allLenses.Count, 0)
    Set rangeWithoutData = firstCellWithoutData.Parent.range(firstCellWithoutData, lastCellWithoutData)
    
    rangeWithoutData.value2 = ""
End Function



