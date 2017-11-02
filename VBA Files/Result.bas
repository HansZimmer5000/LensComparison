Attribute VB_Name = "Result"
Public Function resultLensMatchTheMinMaxFilter(lens As ResultLens, filter As MinMaxNumberFilter) As Boolean
    
    Dim filterName As String
    Dim filterMinValue As Double
    Dim filterMaxValue As Double
    
    filterName = filter.getName
    filterMinValue = filter.getMinValue
    filterMaxValue = filter.getMaxValue
    
    If (StrComp("Focus Length", filterName) = 0 And _
        valueRangeIsBetweenMinMax(lens.getFocalLengthStart, lens.getFocalLengthEnd, filterMinValue, filterMaxValue)) Then
            resultLensMatchTheMinMaxFilter = True
            
    ElseIf (StrComp("Aperture", filterName) = 0 And _
        valueRangeIsBetweenMinMax(lens.getApertureStart, lens.getApertureEnd, filterMinValue, filterMaxValue)) Then
            resultLensMatchTheMinMaxFilter = True
    
    ElseIf (StrComp("Filter", filterName) = 0 And _
        singleValueIsBetweenMinMax(lens.getFilterSize, filterMinValue, filterMaxValue)) Then
            resultLensMatchTheMinMaxFilter = True
    
    ElseIf (StrComp("Magnification (0,1)", filterName) = 0 And _
        singleValueIsBetweenMinMax(lens.getMagnification, filterMinValue, filterMaxValue)) Then
            resultLensMatchTheMinMaxFilter = True
    
    ElseIf (StrComp("Weight", filterName) = 0 And _
        singleValueIsBetweenMinMax(lens.getWeight, filterMinValue, filterMaxValue)) Then
            resultLensMatchTheMinMaxFilter = True
    
    ElseIf (StrComp("Diameter", filterName) = 0 And _
        singleValueIsBetweenMinMax(lens.getDiameter, filterMinValue, filterMaxValue)) Then
            resultLensMatchTheMinMaxFilter = True
    
    ElseIf (StrComp("Length", filterName) = 0 And _
        singleValueIsBetweenMinMax(lens.getLength, filterMinValue, filterMaxValue)) Then
            resultLensMatchTheMinMaxFilter = True
    
    Else
        resultLensMatchTheMinMaxFilter = False
    End If
    
End Function

Public Function resultLensMatchTheMultipleFilter(lens As ResultLens, filter As MultipleStringFilter) As Boolean
    
    Dim filterName As String
    Dim activeFilterValues As Collection
    
    filterName = filter.getName
    Set activeFilterValues = filter.getActiveValues()
    
    If (StrComp("Mount", filterName) = 0 And _
        stringMatchesAtLeastOneValue(lens.getMount(), activeFilterValues)) Then
            resultLensMatchTheMultipleFilter = True
            
    ElseIf (StrComp("Sensor", filterName) = 0 And _
        stringMatchesAtLeastOneValue(lens.getSensorCompatibility, activeFilterValues)) Then
            resultLensMatchTheMultipleFilter = True

    'ElseIf ("Brand" = filterName And _
    '    stringMatchesAtLeastOneValue(lens.getLensName, activeFilterValues)) Then
    '        resultLensMatchTheMultipleFilter = True
            
    'ElseIf ("AF" = filterName And _
    '    stringMatchesAtLeastOneValue(lens.getAF??, activeFilterValues)) Then
    '        resultLensMatchTheMultipleFilter = True
            
    'ElseIf ("VR" = filterName And _
    '    stringMatchesAtLeastOneValue(lens.getVR??, activeFilterValues)) Then
    '        resultLensMatchTheMultipleFilter = True
            
    Else
        resultLensMatchTheMultipleFilter = False
    End If
    
End Function

Private Function singleValueIsBetweenMinMax(value As Double, min As Double, max As Double) As Boolean
    If (value >= min And value <= max) Then
        singleValueIsBetweenMinMax = True
    Else
        singleValueIsBetweenMinMax = False
    End If
End Function

Private Function valueRangeIsBetweenMinMax(valueRangeStart As Double, valueRangeEnd As Double, min As Double, max As Double) As Boolean
    If (singleValueIsBetweenMinMax(valueRangeStart, min, max) And _
        singleValueIsBetweenMinMax(valueRangeEnd, min, max)) Then
        valueRangeIsBetweenMinMax = True
    Else
        valueRangeIsBetweenMinMax = False
    End If
End Function

Private Function stringMatchesAtLeastOneValue(value As String, activeFilterValues As Collection) As Boolean
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

