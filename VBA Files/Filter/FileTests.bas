Attribute VB_Name = "FileTests"

Sub asdf()
    Dim testMinMax As MinMaxFilter
    
    Set testMinMax = New ApertureMinMaxFilter
    Call testMinMax.Init(range("C4"), range("D4"))
    
    Debug.Print testMinMax.isSet()
    
End Sub