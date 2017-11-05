Attribute VB_Name = "TestsuiteResultLens"
' This module includes test for the ResutlLens class.
 

Function testAllCases()
    Call testPosGetAllAttributes
End Function

Private Function testPosGetAllAttributes()
    Call setUp

    
    Debug.Assert(result = True)

    Call tearDown
End Function