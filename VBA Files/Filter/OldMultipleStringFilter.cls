VERSION 1.0 CLASS
BEGIN
  MultiUse = -1  'True
END
Attribute VB_Name = "OldMultipleStringFilter"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = False
Attribute VB_Exposed = False
' Class for one Filter with multiple Values (filter).
' All the values can be set, or none at all.

Private name As String
Private valueCells As Collection
Private nameCell As range

Public Property Get getName() As String
    getName = name
End Property

Public Property Get getActiveValues() As Collection
    Dim currentValueCell As range
    
    Set getActiveValues = New Collection

    For Each currentValueCell In valueCells
        'Orange
        If (interiorColorIsOrange(currentValueCell.Interior)) Then
            getActiveValues.Add currentValueCell.text
        End If
    Next currentValueCell
End Property

Private Sub Class_Initialize()
    Set valueCells = New Collection
End Sub

Public Function Init(newNameCell As range, newValuesRow As range)
    Set nameCell = newNameCell
    name = newNameCell.text
    Set valueCells = gatherAllValueCells(newValuesRow)
End Function

Public Function isSet() As Boolean
    'returns if at least one value / filter is active (orange interior color)
    Dim currentValueCell As range

    For Each currentValueCell In valueCells
        If (interiorColorIsOrange(currentValueCell.Interior)) Then
            isSet = True
            Exit Function
        End If
    Next currentValueCell
    
    isSet = False
End Function


Public Function lensMatchTheMultipleFilter(lens As Lens) As Boolean
    'TODO: Make Classes that depend on this main class -> Open/Closed Principle
    Dim filterName As String
    Dim activeFilterValues As Collection
    Dim afValue as String
    Dim vrValue as String
    
    filterName = name
    Set activeFilterValues = Me.getActiveValues()
    
    If (StrComp("Mount", filterName) = 0 And _
        stringMatchesAtLeastOneValue(lens.getMount(), activeFilterValues)) Then
            lensMatchTheMultipleFilter = True
            
    ElseIf (StrComp("Sensor", filterName) = 0 And _
        stringMatchesAtLeastOneValue(lens.getSensorCompatibility, activeFilterValues)) Then
            lensMatchTheMultipleFilter = True

    ElseIf ("Brand" = filterName And _
        stringMatchesAtLeastOneValue(lens.getBrand(), activeFilterValues)) Then
            lensMatchTheMultipleFilter = True
            
    ElseIf ("AF" = filterName) Then
        if(lens.getAFCode() = 0) Then
            afValue = "Nein"
        ElseIf(lens.getAFCode() = 1) Then
            afValue = "Stange"
        ElseIf(lens.getAFCode() = 2) Then
            afValue = "Motor"
        end If
        if("Nikon" = lens.getBrand()) Then Debug.Print(lens.getLensName() + " " + afValue + " " + Cstr(lens.getAFCode()))
        If(stringMatchesAtLeastOneValue(afValue, activeFilterValues)) Then
            lensMatchTheMultipleFilter = True
        End If
            
    ElseIf ("VR" = filterName) Then
        If(lens.hasVR()) Then
            vrValue = "Ja"
        Else
            vrValue = "Nein"
        End If
        
        If stringMatchesAtLeastOneValue(vrValue, activeFilterValues) Then
            lensMatchTheMultipleFilter = True
        End If
            
    Else
        lensMatchTheMultipleFilter = False
    End If
    
End Function

Private Function gatherAllValueCells(valuesRow As range) As Collection
    Dim currentCell As range

    Set gatherAllValueCells = New Collection

    For Each currentCell In valuesRow
        If (Not rangeIsEmpty(currentCell)) Then
            Call addHyperlinkToItself(currentCell)
            gatherAllValueCells.Add currentCell
        End If
    Next currentCell
End Function

Private Function addHyperlinkToItself(unLinkedRange As range)
    'needed with a sheet macro to "activate" (set interior color orange) a value / filter'
    Dim sheet As Worksheet
    Set sheet = unLinkedRange.Parent
    
    Call sheet.Hyperlinks.Add(unLinkedRange, "", sheet.name & "!" & unLinkedRange.Address, TextToDisplay:=unLinkedRange.text)
    unLinkedRange.Font.ColorIndex = 1
End Function






