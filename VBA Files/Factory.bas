Attribute VB_Name = "Factory"
' A Factory static module that creates and inits new instances
' of our classes.

Public Function CreateApertureMinMaxFilter(minValueCell As range, maxValueCell As range) As MinMaxFilter
    Set CreateMinMaxFilter = New ApertureMinMaxFilter
    Call CreateApertureMinMaxNumberFilter.Init(minValueCell, maxValueCell)
End Function

Public Function CreateDiameterMinMaxFilter(minValueCell As range, maxValueCell As range) As MinMaxFilter
    Set CreateMinMaxFilter = New DiameterMinMaxFilter
    Call CreateDiameterMinMaxNumberFilter.Init(minValueCell, maxValueCell)
End Function

Public Function CreateFiltersizeMinMaxFilter(minValueCell As range, maxValueCell As range) As MinMaxFilter
    Set CreateMinMaxFilter = New FiltersizeMinMaxFilter
    Call CreateFiltersizeMinMaxNumberFilter.Init(minValueCell, maxValueCell)
End Function

Public Function CreateFocalLengthMinMaxFilter(minValueCell As range, maxValueCell As range) As MinMaxFilter
    Set CreateMinMaxFilter = New FocalLengthMinMaxFilter
    Call CreateFocalLengthMinMaxNumberFilter.Init(minValueCell, maxValueCell)
End Function

Public Function CreateLengthMinMaxFilter(minValueCell As range, maxValueCell As range) As MinMaxFilter
    Set CreateMinMaxFilter = New LengthMinMaxFilter
    Call CreateLengthMinMaxNumberFilter.Init(minValueCell, maxValueCell)
End Function

Public Function CreateMagnificationMinMaxFilter(minValueCell As range, maxValueCell As range) As MinMaxFilter
    Set CreateMinMaxFilter = New MagnificationMinMaxFilter
    Call CreateMagnificationMinMaxNumberFilter.Init(minValueCell, maxValueCell)
End Function

Public Function CreateWeightMinMaxFilter(minValueCell As range, maxValueCell As range) As MinMaxFilter
    Set CreateMinMaxFilter = New WeightMinMaxFilter
    Call CreateWeightMinMaxNumberFilter.Init(minValueCell, maxValueCell)
End Function






Public Function CreateMultipleStringFilter(newNameCell As range, newValuesRow As range) As MultipleStringFilter
    Set CreateMultipleStringFilter = New MultipleStringFilter
    Call CreateMultipleStringFilter.Init(newNameCell, newValuesRow)
End Function

Public Function CreateFiltersTable(newMinMaxNumberFilterRange As range, newMultipleStringFilterRange As range) As FiltersTable
    Set CreateFiltersTable = New FiltersTable
    Call CreateFiltersTable.Init(newMinMaxNumberFilterRange, newMultipleStringFilterRange)
End Function

Public Function CreateRawDataTable(newFirstTableRow As range)
    Set CreateRawDataTable = New rawDataTable
    Call CreateRawDataTable.Init(newFirstTableRow)
End Function



Public Function CreateResultTable(newTableRange As range, newRawDataTable As rawDataTable, _
                                    newFiltersTable As FiltersTable)
    Set CreateResultTable = New ResultTable
    Call CreateResultTable.Init(newTableRange, newRawDataTable, newFiltersTable)
End Function

Public Function CreateLens(newLensName As String, _
                                    newFocalLengthStart As Double, _
                                    newFocalLengthEnd As Double, _
                                    newApertureStart As Double, _
                                    newApertureEnd As Double, _
                                    newFilterSize As Double, _
                                    newMagnification As Double, _
                                    newMount As String, _
                                    newSensorCompatibiliy As String, _
                                    newWeight As Double, _
                                    newDiameter As Double, _
                                    newLength As Double)
    Set CreateLens = New Lens
    Call CreateLens.Init(newLensName, _
                                    newFocalLengthStart, _
                                    newFocalLengthEnd, _
                                    newApertureStart, _
                                    newApertureEnd, _
                                    newFilterSize, _
                                    newMagnification, _
                                    newMount, _
                                    newSensorCompatibiliy, _
                                    newWeight, _
                                    newDiameter, _
                                    newLength)
End Function

Function CreateLensFromRow(row as Range) as Lens
    Set CreateLensFromRow = CreateLens(row.Columns(1).text, _
                                        row.Columns(2).value2, _
                                        row.Columns(3).value2, _
                                        row.Columns(4).value2, _
                                        row.Columns(5).value2, _
                                        row.Columns(6).value2, _
                                        row.Columns(7).value2, _
                                        row.Columns(8).text, _
                                        row.Columns(9).text, _
                                        row.Columns(10).value2, _
                                        row.Columns(11).value2, _
                                        row.Columns(12).value2)
End Function
