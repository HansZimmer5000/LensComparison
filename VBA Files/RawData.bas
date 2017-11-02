Attribute VB_Name = "RawData"
Function convertNumberStringPointToNumberCommaAndCleanEmpySpaces(rawString As String) As Double
    ' This Function converts a "1.33" to 1,33
    Dim tmpResultStr As String

    tmpResultStr = Replace(rawString, ".", ",")
    tmpResultStr = Replace(tmpResultStr, " ", "")
    convertNumberStringPointToNumberCommaAndCleanEmpySpaces = CDbl(tmpResultStr)
End Function

Function getFocalLengthStart(fullFocalLength As String) As Double
    getFocalLengthStart = getFocalLengthPart(fullFocalLength, True)
End Function

Function getFocalLengthEnd(fullFocalLength As String) As Double
    getFocalLengthEnd = getFocalLengthPart(fullFocalLength, False)
End Function

Function getApertureStart(fullApertureInfo As String) As Double
    getApertureStart = getAperturePart(fullApertureInfo, True)
End Function

Function getApertureEnd(fullApertureInfo As String) As Double
    getApertureEnd = getAperturePart(fullApertureInfo, False)
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
    getWeightAsDouble = convertNumberStringPointToNumberCommaAndCleanEmpySpaces(Replace(weight, "g", ""))
End Function

Function getSizeDiameter(fullSizeInfo As String) As Double
    Const X_ELEM As String = "x"

    Dim indexOfX As Integer
    Dim resultStr As String
    Dim resultDbl As Double

    indexOfX = InStr(fullSizeInfo, X_ELEM)

    If (StrComp(fullSizeInfo, "0") = 0) Then
        resultStr = fullSizeInfo
    Else
        resultStr = Left(fullSizeInfo, indexOfX - 1) '-1 because we don't "x" in our resultStr
    End If
    
    resultDbl = convertNumberStringPointToNumberCommaAndCleanEmpySpaces(resultStr)
    getSizeDiameter = resultDbl
End Function

Function getSizeLength(fullSizeInfo As String) As Double
    Const X_ELEM As String = "x"

    Dim indexOfX As Integer
    Dim resultStr As String
    Dim resultDbl As Double

    indexOfX = InStr(fullSizeInfo, X_ELEM)

    resultStr = Mid(fullSizeInfo, indexOfX + 1) '-1 because we don't "x" in our resultStr
    resultStr = Replace(resultStr, "mm", "")
    resultDbl = convertNumberStringPointToNumberCommaAndCleanEmpySpaces(resultStr)

    getSizeLength = resultDbl
End Function

Function getMagnification(fullMagnificationInfo As String) As Double

    ' Can only understand Magnifications similar to:
    '   1:3.10 / 1:1
    '   0.28X / 1X
    
    Const UNIT As String = "1:"
    Const X_ELEM As String = "X"
    
    Dim inputIsAlreadyCorrect As Boolean
    Dim resultStr As String
    Dim resultDbl As Double
    Dim magnificationAsDouble As Double
    
    inputIsAlreadyCorrect = (InStr(fullMagnificationInfo, UNIT) = 1)
    
    If (StrComp(fullMagnificationInfo, "") = 0 Or _
        StrComp(fullMagnificationInfo, "0") = 0 _
        ) Then
        resultStr = "0"
    Else
        If (inputIsAlreadyCorrect) Then
            resultStr = Replace(fullMagnificationInfo, UNIT, "")
        Else
            If (InStr(fullMagnificationInfo, X_ELEM) > 0) Then
                magnificationAsDouble = convertNumberStringPointToNumberCommaAndCleanEmpySpaces(Replace(fullMagnificationInfo, X_ELEM, ""))
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

Private Function getFocalLengthPart(fullFocalLength As String, focalLengthStartIsNeeded As Boolean) As Double
    Const MINUS_ELEM As String = "-"

    Dim indexOfMinus As Integer
    Dim resultStr As String
    Dim resultDbl As Double
    Dim inputLength As Integer

    indexOfMinus = InStr(fullFocalLength, MINUS_ELEM)
    
    If (indexOfMinus > 0) Then
        If (focalLengthStartIsNeeded) Then
            resultStr = Left(fullFocalLength, indexOfMinus - 1) '-1 because otherwise Minus would be returned too.
        Else
            resultStr = Mid(fullFocalLength, indexOfMinus + 1)
            resultStr = Replace(resultStr, "mm", "")
        End If
    Else
        resultStr = Replace(fullFocalLength, "mm", "")
    End If

    resultDbl = convertNumberStringPointToNumberCommaAndCleanEmpySpaces(resultStr)
    getFocalLengthPart = resultDbl
End Function

Private Function getAperturePart(fullApertureInfo As String, apertureStartIsNeeded As Boolean) As Double
    Const MINUS_ELEM As String = "-"

    Dim indexOfMinus As Integer
    Dim resultStr As String
    Dim resultDbl As Double
    Dim inputLength As Integer

    indexOfMinus = InStr(fullApertureInfo, MINUS_ELEM)

    If (indexOfMinus > 0) Then
        If (apertureStartIsNeeded) Then
            resultStr = Left(fullApertureInfo, indexOfMinus - 1) '1:3.5
            resultStr = Replace(resultStr, "1:", "")
        Else
            resultStr = Mid(fullApertureInfo, indexOfMinus + 1)
            resultStr = Replace(resultStr, "1:", "")
        End If
    Else
        resultStr = Replace(fullApertureInfo, "1:", "")
    End If
    
    resultDbl = convertNumberStringPointToNumberCommaAndCleanEmpySpaces(resultStr)
    getAperturePart = resultDbl

End Function




