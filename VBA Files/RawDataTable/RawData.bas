Attribute VB_Name = "RawData"
Function convertNumberStringPointToNumberCommaAndCleanEmpySpaces(rawString As String) As Double
    ' This Function converts a "1.33" to 1,33
    Dim tmpResultStr As String

    tmpResultStr = Replace(rawString, ".", ",")
    tmpResultStr = Replace(tmpResultStr, " ", "")
    convertNumberStringPointToNumberCommaAndCleanEmpySpaces = CDbl(tmpResultStr)
End Function

Function getFocalLengthStart(focalLengthInfo As String) As Double
    getFocalLengthStart = getFocalLengthPart(focalLengthInfo, True)
End Function

Function getFocalLengthEnd(focalLengthInfo As String) As Double
    getFocalLengthEnd = getFocalLengthPart(focalLengthInfo, False)
End Function

Function getApertureStart(apertureInfo As String) As Double
    getApertureStart = getAperturePart(apertureInfo, True)
End Function

Function getApertureEnd(apertureInfo As String) As Double
    getApertureEnd = getAperturePart(apertureInfo, False)
End Function

Function getFiltersizeAsDouble(filtersize As String) As Double
    If (StrComp(filtersize, "") = 0 Or _
        InStr(filtersize, "x") > 0) Then
        getFiltersizeAsDouble = 0
    Else
        getFiltersizeAsDouble = convertNumberStringPointToNumberCommaAndCleanEmpySpaces(Replace(filtersize, "mm", ""))
    End If
End Function

Function getWeightAsDouble(weight As String) As Double
    if(StrComp(weight, "") = 0) Then
        getWeightAsDouble = 0
    Else
        getWeightAsDouble = convertNumberStringPointToNumberCommaAndCleanEmpySpaces(Replace(weight, "g", ""))
    End If
End Function

Function getSizeDiameter(sizeInfo As String) As Double
    Const X_ELEM As String = "x"

    Dim indexOfX As Integer
    Dim resultStr As String
    Dim resultDbl As Double

    If (StrComp(sizeInfo, "0") = 0 or _
        StrComp(sizeInfo, "") = 0) Then
        resultStr = "0"
    Else
        indexOfX = InStr(sizeInfo, X_ELEM)
        resultStr = Left(sizeInfo, indexOfX - 1) '-1 because we don't "x" in our resultStr
    End If
    
    resultDbl = convertNumberStringPointToNumberCommaAndCleanEmpySpaces(resultStr)
    getSizeDiameter = resultDbl
End Function

Function getSizeLength(sizeInfo As String) As Double
    Const X_ELEM As String = "x"

    Dim indexOfX As Integer
    Dim resultStr As String
    Dim resultDbl As Double

    if(StrComp(sizeInfo, "") = 0) Then
        resultStr = "0"
    Else
        indexOfX = InStr(sizeInfo, X_ELEM)

        resultStr = Mid(sizeInfo, indexOfX + 1) '-1 because we don't "x" in our resultStr
        resultStr = Replace(resultStr, "mm", "")
    End If

    resultDbl = convertNumberStringPointToNumberCommaAndCleanEmpySpaces(resultStr)
    getSizeLength = resultDbl
End Function

Function getMount(mountInfo as String) as String
    if(StrComp(MountInfo, "") = 0) Then
        getMount = "Unknown"
    Else
        getMount = MountInfo
    End If
End Function

Function getSensorCompatibility(sensorInfo as String) as String
    if(StrComp(sensorInfo, "") = 0) Then
        getSensorCompatibility = "Unknown"
    Else
        getSensorCompatibility = sensorInfo
    End If
End Function

Function getMagnification(magnificationInfo As String) As Double

    ' Can only understand Magnifications similar to:
    '   1:3.10 / 1:1
    '   0.28X / 1X
    
    Const UNIT As String = "1:"
    Const X_ELEM As String = "X"
    
    Dim inputIsAlreadyCorrect As Boolean
    Dim resultStr As String
    Dim resultDbl As Double
    Dim magnificationAsDouble As Double
    
    inputIsAlreadyCorrect = (InStr(magnificationInfo, UNIT) = 1)
    
    If (StrComp(magnificationInfo, "") = 0 Or _
        StrComp(magnificationInfo, "0") = 0 _
        ) Then
        resultStr = "0"
    Else
        If (inputIsAlreadyCorrect) Then
            resultStr = Replace(magnificationInfo, UNIT, "")
        Else
            If (InStr(magnificationInfo, X_ELEM) > 0) Then
                magnificationAsDouble = convertNumberStringPointToNumberCommaAndCleanEmpySpaces(Replace(magnificationInfo, X_ELEM, ""))
                magnificationAsDouble = 1 / magnificationAsDouble
                resultStr = CStr(magnificationAsDouble)
            Else
                resultStr = "This Inputformat is not known!"
            End If
        End If
    End If
    
    resultDbl = convertNumberStringPointToNumberCommaAndCleanEmpySpaces(resultStr)
    getMagnification = resultDbl
End Function

Function getMinimalFocus(minimalFocusInfo as String) as Double
    Dim resultDbl as Double
    Dim resultStr as String

    If (StrComp(minimalFocusInfo, "0") = 0 or _
        StrComp(minimalFocusInfo, "") = 0) Then
        resultStr = "0"
    Else
        resultStr = Replace(minimalFocusInfo,"m","")
    End If

    resultDbl = convertNumberStringPointToNumberCommaAndCleanEmpySpaces(resultStr)
    getMinimalFocus = resultDbl
End Function

Private Function getFocalLengthPart(focalLengthInfo As String, focalLengthStartIsNeeded As Boolean) As Double
    Const MINUS_ELEM As String = "-"

    Dim indexOfMinus As Integer
    Dim resultStr As String
    Dim resultDbl As Double
    Dim inputLength As Integer

    indexOfMinus = InStr(focalLengthInfo, MINUS_ELEM)
    
    If(StrComp(focalLengthInfo, "") = 0) Then
        resultStr = "0"
    Else
        If (indexOfMinus > 0) Then
            If (focalLengthStartIsNeeded) Then
                resultStr = Left(focalLengthInfo, indexOfMinus - 1) '-1 because otherwise Minus would be returned too.
            Else
                resultStr = Mid(focalLengthInfo, indexOfMinus + 1)
                resultStr = Replace(resultStr, "mm", "")
            End If
        Else
            resultStr = Replace(focalLengthInfo, "mm", "")
        End If
    end If

    resultDbl = convertNumberStringPointToNumberCommaAndCleanEmpySpaces(resultStr)
    getFocalLengthPart = resultDbl
End Function

Private Function getAperturePart(apertureInfo As String, apertureStartIsNeeded As Boolean) As Double
    Const MINUS_ELEM As String = "-"

    Dim indexOfMinus As Integer
    Dim resultStr As String
    Dim resultDbl As Double
    Dim inputLength As Integer

    indexOfMinus = InStr(apertureInfo, MINUS_ELEM)

    If(StrComp(apertureInfo, "") = 0) Then
        resultStr = "0"
    Else
        If (indexOfMinus > 0) Then
            If (apertureStartIsNeeded) Then
                resultStr = Left(apertureInfo, indexOfMinus - 1) '1:3.5
                resultStr = Replace(resultStr, "1:", "")
            Else
                resultStr = Mid(apertureInfo, indexOfMinus + 1)
                resultStr = Replace(resultStr, "1:", "")
            End If
        Else
            resultStr = Replace(apertureInfo, "1:", "")
        End If
    End If
    
    resultDbl = convertNumberStringPointToNumberCommaAndCleanEmpySpaces(resultStr)
    getAperturePart = resultDbl

End Function




