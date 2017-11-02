Attribute VB_Name = "Factory"
' A Factory static module that creates and inits new instances
' of our classes.

Public Function CreateMinMaxNumberFilter(nameCell As range, minValueCell As range, maxValueCell As range) As MinMaxNumberFilter
    Set CreateMinMaxNumberFilter = New MinMaxNumberFilter
    Call CreateMinMaxNumberFilter.Init(nameCell, minValueCell, maxValueCell)
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

Public Function CreateRawDataLens(newLensName As String, _
                                    newFocalLength As String, _
                                    newFocalLengthStart As Double, _
                                    newFocalLengthEnd As Double, _
                                    newAperture As String, _
                                    newApertureStart As Double, _
                                    newApertureEnd As Double, _
                                    newFilterSize1 As String, _
                                    newFilterSize2 As Double, _
                                    newMagnification1 As String, _
                                    newMagnification2 As Double, _
                                    newMount As String, _
                                    newSensorCompatibiliy As String, _
                                    newWeight1 As String, _
                                    newWeight2 As Double, _
                                    newSize As String, _
                                    newDiameter As Double, _
                                    newLength As Double)
    Set CreateRawDataLens = New RawDataLens
    Call CreateRawDataLens.Init(newLensName, _
                                    newFocalLength, _
                                    newFocalLengthStart, _
                                    newFocalLengthEnd, _
                                    newAperture, _
                                    newApertureStart, _
                                    newApertureEnd, _
                                    newFilterSize1, _
                                    newFilterSize2, _
                                    newMagnification1, _
                                    newMagnification2, _
                                    newMount, _
                                    newSensorCompatibiliy, _
                                    newWeight1, _
                                    newWeight2, _
                                    newSize, _
                                    newDiameter, _
                                    newLength)
End Function


Public Function CreateResultTable(newTableRange As range, newRawDataTable As rawDataTable, _
                                    newFiltersTable As FiltersTable)
    Set CreateResultTable = New ResultTable
    Call CreateResultTable.Init(newTableRange, newRawDataTable, newFiltersTable)
End Function

Public Function CreateResultLens(newLensName As String, _
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
    Set CreateResultLens = New ResultLens
    Call CreateResultLens.Init(newLensName, _
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

Public Function CreateResultLensFromRawDataLens(RawDataLens As RawDataLens)
    Set CreateResultLensFromRawDataLens = New ResultLens
    Call CreateResultLensFromRawDataLens.Init(RawDataLens.getLensName, _
                                                RawDataLens.getFocalLengthStart, _
                                                RawDataLens.getFocalLengthEnd, _
                                                RawDataLens.getApertureStart, _
                                                RawDataLens.getApertureEnd, _
                                                RawDataLens.getFilterSize2, _
                                                RawDataLens.getMagnification2, _
                                                RawDataLens.getMount, _
                                                RawDataLens.getSensorCompatibility, _
                                                RawDataLens.getWeight2, _
                                                RawDataLens.getDiameter, _
                                                RawDataLens.getLength)
End Function
