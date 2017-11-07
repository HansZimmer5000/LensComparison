Attribute VB_Name = "Tests"

Sub testAll()
    Dim myLensTestsuite As LensTestsuite: Set myLensTestsuite = New LensTestsuite
    
    For i = 1 To 10
        Debug.Print vbNewLine
    Next
    Debug.Print (Str(Now) + " Run testAll Start")
    
    Call myLensTestsuite.testAllCases

    Debug.Print (Str(Now) + " Run testAll Done")
End Sub

Function printAndAssert(functionName As String, result As Boolean)
    if(InStr(functionName,"NEG")>0) Then
        result = not(result)
    End If
    
    If (result) Then
        Debug.Print (Str(Now) + " .")
    Else
        Debug.Print (Str(Now) + " " + functionName + " FAIL!")
    End If
End Function