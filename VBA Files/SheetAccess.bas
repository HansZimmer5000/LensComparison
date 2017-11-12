Attribute VB_Name = "SheetAccess"

Function getRawDataSheet() as Worksheet
    Set getRawDataSheet = Sheets("RawData")
End Function

Function getOverviewSheet() as Worksheet
    Set getOverviewSheet = Sheets("Overview")
End Function