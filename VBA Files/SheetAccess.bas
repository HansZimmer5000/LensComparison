Attribute VB_Name = "SheetAccess"

Function getPreparedDataSheet() as Worksheet
    Set getPreparedDataSheet = Sheets("PreparedData")
End Function

Function getOverviewSheet() as Worksheet
    Set getOverviewSheet = Sheets("Overview")
End Function