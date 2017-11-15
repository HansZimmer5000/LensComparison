Attribute VB_Name = "Tests"

Sub testAll()
    Application.VBE.MainWindow.Visible = True 

    Dim myLensTestsuite As LensTestsuite: Set myLensTestsuite = New LensTestsuite
    Dim myLensRawDataTableTestsuite As RawDataTableTestsuite: Set myRawDataTableTestsuite = new RawDataTableTestsuite
    Dim myMinMaxNumberFilterTestsuite as MinMaxNumberFilterTestsuite: Set myMinMaxNumberFilterTestsuite = new MinMaxNumberFilterTestsuite
    Dim myMultipleStringFilterTestsuite as MultipleStringFilterTestsuite: Set myMultipleStringFilterTestsuite = new MultipleStringFilterTestsuite
    Dim myFiltersTableTestsuite as FiltersTableTestsuite: Set myFiltersTableTestsuite = new FiltersTableTestsuite

    For i = 1 To 10
        Debug.Print vbNewLine
    Next
    Debug.Print (Str(Now) + " " + "Run testAll Start")
    
    Call myLensTestsuite.testAllCases 
    Call myRawDataTableTestsuite.testAllCases
    Call myMinMaxNumberFilterTestsuite.testAllCases
    Call myMultipleStringFilterTestsuite.testAllCases
    Call myFiltersTableTestsuite.testAllCases

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

Function collectionsAreEqual(coll1 as Collection, coll2 as Collection) as Boolean

    If(coll1.Count = coll2.Count) Then
        For each elem1 in coll1
            On Error Resume Next
            Call coll2.Item(elem1)
            If(Err.Number = 9) Then
                collectionsAreEqual = False
                Exit Function
            End If
        Next
        collectionsAreEqual = True
    Else
        collectionsAreEqual = False
    End If
End Function