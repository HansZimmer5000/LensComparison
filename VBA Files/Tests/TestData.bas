Attribute VB_Name = "TestData"


'Module to organize TestData in Sheet "TestData"

'\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
' Single Lens Rows:
'/////////////////////////////////////
Function getLensWithFullInfo1RowRange() as Range
    Set getLensWithFullInfo1RowRange = Sheets("TestData").Range("A2:L2")
End Function

'\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
' Single Lens Attributes:
'/////////////////////////////////////
Function getLensWithFullInfo1Lensname() As String
    getLensWithFullInfo1Lensname = Sheets("TestData").Range("A2").Text 'makes problems because of the 'sharp s' in the end: "Canon EF 100-400mm 4.5-5.6 L IS II USM weiß"
End Function

Function getLensWithFullInfo1FocalStart() As Double
    getLensWithFullInfo1FocalStart = 100#
End Function

Function getLensWithFullInfo1FocalEnd() As Double
    getLensWithFullInfo1FocalEnd = 400#
End Function

Function getLensWithFullInfo1ApertureStart() As Double
    getLensWithFullInfo1ApertureStart = 4.5
End Function

Function getLensWithFullInfo1ApertureEnd() As Double
    getLensWithFullInfo1ApertureEnd = 5.6
End Function

Function getLensWithFullInfo1Filter() As Double
    getLensWithFullInfo1Filter = 77#
End Function

Function getLensWithFullInfo1Magnification() As Double
    getLensWithFullInfo1Magnification = 3.23
End Function

Function getLensWithFullInfo1Mount() As String
    getLensWithFullInfo1Mount = "Canon EF"
End Function

Function getLensWithFullInfo1Sensor() As String
    getLensWithFullInfo1Sensor = "APS-C/ Kleinbild"
End Function

Function getLensWithFullInfo1Weight() As Double
    getLensWithFullInfo1Weight = 1570#
End Function

Function getLensWithFullInfo1Diameter() As Double
    getLensWithFullInfo1Diameter = 94#
End Function

Function getLensWithFullInfo1Length() As Double
    getLensWithFullInfo1Length = 193#
End Function

Function getLensWithFullInfo1Brand() as String
    getLensWithFullInfo1Brand = "Canon"
End Function

Function getLensWithFullInfo1AFCode() as Double
    getLensWithFullInfo1AFCode = 2
End Function

Function getLensWithFullInfo1HasVR() as Boolean
    getLensWithFullInfo1HasVR = True
End Function





Function getLensWithAllExceptMagnificationSensorInfo1Magnification() as Double
    getLensWithAllExceptMagnificationSensorInfo1Magnification = 0
End Function

Function getLensWithAllExceptMagnificationSensorInfo1Sensor() as String
    getLensWithAllExceptMagnificationSensorInfo1Sensor = "Unknown"
End Function

'\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
' Created Lenses from Raw Lensdata from the Sheet:
'/////////////////////////////////////
Function getLensWithFullInfo1() As lens
    Set getLensWithFullInfo1 = CreateLensFromRow(Sheets("TestData").range("A2:L2"))
End Function

Function getLensWithAllExceptFilterInfo1() As lens
    Set getLensWithAllExceptFilterInfo1 = CreateLensFromRow(Sheets("TestData").range("A3:L3"))
End Function

Function getLensWithAllExceptFilterMagnificationInfo1() As lens
    Set getLensWithAllExceptFilterMagnificationInfo1 = CreateLensFromRow(Sheets("TestData").range("A4:L4"))
End Function

Function getLensWithAllExceptMagnificationSensorInfo1() As lens
    Set getLensWithAllExceptMagnificationSensorInfo1 = CreateLensFromRow(Sheets("TestData").range("A5:L5"))
End Function

'\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
' Single RawDataTable Attributes from  the Sheet:
'/////////////////////////////////////
Function getRawDataTable1Range() as Range
    Set getRawDataTable1Range = Sheets("TestData").range("A2:L5")
End Function

'\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
' Created RawDataTable from the Sheet:
'/////////////////////////////////////

Function getRawDataTable1() as RawDataTable
    Set getRawDataTable1 = CreateRawDataTable(Sheets("TestData").range("A2:L2"))
End Function

'\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
' Single ResultTable Attributes from  the Sheet:
'/////////////////////////////////////
Function getResultTable1Range() as Range
    Set getResultTable1Range = Sheets("TestData").range("A2:L5")
End Function

'\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
' Created ResultTable from the Sheet:
'/////////////////////////////////////

Function getResultTable1() as RawDataTable
    Set getResultTable1 = CreateResultTable(Sheets("TestData").range("A2:L2"),getRawDataTable1, getFiltersTable1)
End Function

'\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
' Single FiltersTable Attributes from  the Sheet:
'/////////////////////////////////////
Function getMinMaxNumberFilter1Range() as Range
    Set getMinMaxNumberFilter1Range = Sheets("TestData").range("A20:C22")
End Function

Function getFiltersTable1Range() as Range
    Set getFiltersTable1Range = Sheets("TestData").range("A2:L5")
End Function

Function getMultipleStringFilter1Range() as Range
    Set getMultipleStringFilter1Range = Sheets("TestData").range("E20:N23")
End Function

'\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
' Created FiltersTable from the Sheet:
'/////////////////////////////////////

Function getFiltersTable1() as RawDataTable
    Set getFiltersTable1 = CreateFiltersTable(getMinMaxNumberFilter1Range, getMultipleStringFilter1Range)
End Function

'\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
' Single Filter Attributes from  the Sheet:
'/////////////////////////////////////

Function getMinMaxNumberFilterMinDefaultValue() as Double
    getMinMaxNumberFilterMinDefaultValue = 0
End Function

Function getMinMaxNumberFilterMaxDefaultValue() as Double
    getMinMaxNumberFilterMaxDefaultValue = 9999
End Function

Function getMinMaxNumberFilter1NameRange() as Range
    Set getMinMaxNumberFilter1NameRange = Sheets("TestData").range("A20")
End Function

Function getMinMaxNumberFilter1MinValueRange() as Range
    Set getMinMaxNumberFilter1MinValueRange = Sheets("TestData").range("B20")
End Function

Function getMinMaxNumberFilter1MaxValueRange() as Range
    Set getMinMaxNumberFilter1MaxValueRange = Sheets("TestData").range("C20")
End Function

Function getMultipleStringFilter1NameRange() as Range
    Set getMultipleStringFilter1NameRange = Sheets("TestData").range("E20")
End Function

Function getMultipleStringFilter1ValuesRow() as Range
    Set getMultipleStringFilter1ValuesRow = Sheets("TestData").range("F20:N20")
End Function

'\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
' Created Filters from the Sheet:
'/////////////////////////////////////

Function getMinMaxNumberFilter1() as MinMaxNumberFilter
    Set getMinMaxNumberFilter1 = CreateMinMaxNumberFilter(getMinMaxNumberFilter1NameRange, _
                                                            getMinMaxNumberFilter1MinValueRange, _
                                                            getMinMaxNumberFilter1MaxValueRange)
End Function

Function getMultipleStringFilter1() as MultipleStringFilter
    Set getMultipleStringFilter1 = CreateMultipleStringFilter(getMultipleStringFilter1NameRange, _
                                                                getMultipleStringFilter1ValuesRow)
End Function