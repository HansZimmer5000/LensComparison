Attribute VB_Name = "MultipleStringFilterColors"
'A Module to collect all the functions to set colors for a range.
'Or to check if a range has some certain color

Const THEME_COLOR_GREY_WHITE As Long = xlThemeColorDark1
Const THEME_COLOR_ORANGE As Long = xlThemeColorAccent2
Const TINT_SHADE_GREY As Double = -0.149998474074526
Const ZERO As Double = 0

Public Function setFontColorBlack(rangeFont)
    rangeFont.ColorIndex = 1
End Function

Public Function setInteriorColorGrey(rangeInterior)
    rangeInterior.ThemeColor = THEME_COLOR_GREY_WHITE
    rangeInterior.TintAndShade = TINT_SHADE_GREY
    rangeInterior.PatternTintAndShade = ZERO
End Function

Public Function setInteriorColorWhite(rangeInterior)
    rangeInterior.ThemeColor = THEME_COLOR_GREY_WHITE
    rangeInterior.TintAndShade = ZERO
    rangeInterior.PatternTintAndShade = ZERO
End Function

Public Function setInteriorColorOrange(rangeInterior)
    rangeInterior.ThemeColor = THEME_COLOR_ORANGE
    rangeInterior.TintAndShade = ZERO
    rangeInterior.PatternTintAndShade = ZERO
End Function

Public Function interiorColorIsOrange(rangeInterior) As Boolean
    If (rangeInterior.ThemeColor = THEME_COLOR_ORANGE And _
        rangeInterior.TintAndShade = ZERO And _
        rangeInterior.PatternTintAndShade = ZERO) Then
        interiorColorIsOrange = True
    Else
        interiorColorIsOrange = False
    End If
End Function

Function filterValueIsActive(range As range) As Boolean
    filterValueIsActive = (xlThemeColorAccent2 = range.Interior.ThemeColor)
End Function

Function deactivateFilterValue(range As range)
    Call setInteriorColorOrange(range.Interior)
End Function

Function activateFilterValue(range As range)
    If (range.row Mod 2 = 0) Then
        Call setInteriorColorGrey(range.Interior)
    Else
        Call setInteriorColorWhite(range.Interior)
    End If
End Function