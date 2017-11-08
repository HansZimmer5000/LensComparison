Attribute VB_Name = "Tests"

Sub testAll()
    Dim myLensTestsuite As LensTestsuite: Set myLensTestsuite = New LensTestsuite
    Dim myLensRawDataTableTestsuite As RawDataTableTestsuite: Set myRawDataTableTestsuite = new RawDataTableTestsuite
    
    For i = 1 To 10
        Debug.Print vbNewLine
    Next
    Debug.Print (Str(Now) + " " + "Run testAll Start")
    
    Call myLensTestsuite.testAllCases
    Call myRawDataTableTestsuite.testAllCases

    Debug.Print (Str(Now) + " " + "Run testAll Done")
End Sub

Function printAndAssert(functionName As String, result As Boolean)
    if(InStr(functionName,"NEG")>0) Then
        result = not(result)
    End If
    
    If (result) Then
        Debug.Print (Str(Now) + " " + ".")
    Else
        Debug.Print (Str(Now) + " " + functionName + " FAIL!")
    End If
End Function