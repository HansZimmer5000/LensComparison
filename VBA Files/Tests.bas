Attribute VB_Name = "Tests"

Sub testAll()
    Dim myLensTestsuite As LensTestsuite: Set myLensTestsuite = New LensTestsuite
    Dim myLensRawDataTableTestsuite As RawDataTableTestsuite: Set myRawDataTableTestsuite = new RawDataTableTestsuite
    
    For i = 1 To 10
        Debug.Print vbNewLine
    Next
    Debug.Print (Str(Now) + " " + "Run testAll Start")
    
    Debug.Print (Str(Now) + " " + "Run Pyhton tests.")
    Call runAllPythonTests()
    Call myLensTestsuite.testAllCases 
    Call myRawDataTableTestsuite.testAllCases

    Debug.Print (Str(Now) + " " + "Run testAll Done")
End Sub

Function printAndAssert(functionName As String, result As Boolean)
    if(InStr(functionName,"Neg") > 0) Then
        result = not(result)
    End If
    
    If (result) Then
        Debug.Print (Str(Now) + " " + ".")
    Else
        Debug.Print (Str(Now) + " " + functionName + " FAIL!")
    End If
End Function

Function elemIsInCollection(elem as Variant, coll as Collection) as Boolean
    elemIsInCollection = False
    for each currentElem in coll
        if(StrComp(TypeName(currentElem),"Lens") = 0) Then
            if(elem.equals(currentElem)) Then
                elemIsInCollection = True
            End If
        End If
    next
End Function