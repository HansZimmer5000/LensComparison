VERSION 1.0 CLASS
BEGIN
  MultiUse = -1  'True
END
Attribute VB_Name = "FiltersTable"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = False
Attribute VB_Exposed = False
' Class for the filters table which contains all the filters.

Private minMaxNumberFilterRange As range
Private multipleStringFilterRange As range
Private allMinMaxNumberFilters As Collection
Private allMultipleStringFilters As Collection

Public Property Get getAllMinMaxNumberFilters() As Collection
    Set getAllMinMaxNumberFilters = allMinMaxNumberFilters
End Property

Public Property Get getAllMultipleStringFilters() As Collection
    Set getAllMultipleStringFilters = allMultipleStringFilters
End Property

Private Sub Class_Initialize()
End Sub

Public Function Init(newMinMaxNumberFilterRange As range, newMultipleStringFilterRange As range)
    Set minMaxNumberFilterRange = newMinMaxNumberFilterRange
    Set multipleStringFilterRange = newMultipleStringFilterRange

    Set allMinMaxNumberFilters = collectAllMinMaxNumberFilters(minMaxNumberFilterRange)
    Set allMultipleStringFilters = collectAllMultipleStringFilters(multipleStringFilterRange)
End Function

Private Function collectAllMinMaxNumberFilters(range As range) As Collection
    ' Collects all the MinMaxNumberFilters from the sheet defined as the parent of range
    
    Const NAME_COLUMN_INDEX As Integer = 1
    Const MIN_VALUE_COLUMN_INDEX As Integer = 2
    Const MAX_VALUE_COLUMN_INDEX As Integer = 3

    Dim rowCount As Integer
    Dim currentRow As range
    Dim currentMinMaxNumberFilter As MinMaxNumberFilter

    rowCount = range.Rows.Count
    Set collectAllMinMaxNumberFilters = New Collection

    firstDataRow = range.row
    lastDataRow = range.Rows(range.Rows.Count).row

    For currentIteration = 1 To rowCount
        Set currentRow = range.Rows(currentIteration)
        Set currentMinMaxNumberFilter = CreateMinMaxNumberFilter( _
                                            currentRow.Columns(NAME_COLUMN_INDEX), _
                                            currentRow.Columns(MIN_VALUE_COLUMN_INDEX), _
                                            currentRow.Columns(MAX_VALUE_COLUMN_INDEX))
        collectAllMinMaxNumberFilters.Add currentMinMaxNumberFilter
    Next currentIteration
End Function

Private Function collectAllMultipleStringFilters(range As range) As Collection
    ' Collects all the MultipleStringFilters from the sheet defined as the parent of range

    Const NAME_COLUMN_INDEX As Integer = 1
    
    Dim currentRow As range
    Dim currentMultipleStringFilter As MultipleStringFilter
    Dim dataColumnCount As Integer
    Dim rowCount As Integer
    Dim sheet As Worksheet

    dataColumnCount = range.Columns.Count - 1
    rowCount = range.Rows.Count
    Set collectAllMultipleStringFilters = New Collection
    Set sheet = range.Parent

    For currentIteration = 1 To rowCount
        Set currentRow = range.Rows(currentIteration)
        Set currentMultipleStringFilter = CreateMultipleStringFilter( _
                                            currentRow.Columns(NAME_COLUMN_INDEX), _
                                            sheet.range(currentRow.Columns(NAME_COLUMN_INDEX).Offset(0, 1), _
                                                        currentRow.Columns(NAME_COLUMN_INDEX).Offset(0, dataColumnCount)))
        collectAllMultipleStringFilters.Add currentMultipleStringFilter
    Next currentIteration
End Function


