VERSION 1.0 CLASS
BEGIN
  MultiUse = -1  'True
END
Attribute VB_Name = "RawDataTable"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = False
Attribute VB_Exposed = False
' Class for the RawDataTable within are all RawDataLenses.
' Each Entry (Line / Row) is a RawDataLens.
' It just holds the data about these lenses.

Private tableRange As range
Private rawDataLenses As Collection

Public Property Get getTableRange() As range
    Set getTableRange = tableRange
End Property

Public Property Get getAllRawDataLenses() As Collection
    Set getAllRawDataLenses = rawDataLenses
End Property

Private Sub Class_Initialize()
End Sub

Public Function Init(newFirstTableRow As range)
    Set tableRange = calcTableRangeFromFirstRow(newFirstTableRow)
    Set rawDataLenses = collectAllRawDataLenses()
End Function

Private Function calcTableRangeFromFirstRow(newFirstTableRow As range) As range
    Dim firstCell As range
    Dim rowOffsetFirstToLastRow As Integer
    Dim lastCell As range
    
    Set firstCell = newFirstTableRow.Columns(1)
    rowOffsetFirstToLastRow = firstCell.End(xlDown).row - firstCell.row
    Set lastCell = newFirstTableRow.Columns(newFirstTableRow.Columns.Count).Offset(rowOffsetFirstToLastRow, 0)
    
    Set calcTableRangeFromFirstRow = newFirstTableRow.Parent.range(firstCell, lastCell)
End Function

Private Function collectAllRawDataLenses()
    Dim currentRow As range
    Dim currentRawDataLens As RawDataLens

    Set collectAllRawDataLenses = New Collection

    For Each currentRow In tableRange.Rows
        Set currentRawDataLens = CreateRawDataLens(currentRow.Columns(1).text, _
                                                currentRow.Columns(2).text, _
                                                currentRow.Columns(3).value2, _
                                                currentRow.Columns(4).value2, _
                                                currentRow.Columns(5).text, _
                                                currentRow.Columns(6).value2, _
                                                currentRow.Columns(7).value2, _
                                                currentRow.Columns(8).text, _
                                                currentRow.Columns(9).value2, _
                                                currentRow.Columns(10).text, _
                                                currentRow.Columns(11).value2, _
                                                currentRow.Columns(12).text, _
                                                currentRow.Columns(13).text, _
                                                currentRow.Columns(14).text, _
                                                currentRow.Columns(15).value2, _
                                                currentRow.Columns(16).text, _
                                                currentRow.Columns(17).value2, _
                                                currentRow.Columns(18).value2)
        collectAllRawDataLenses.Add currentRawDataLens
    Next currentRow
End Function

