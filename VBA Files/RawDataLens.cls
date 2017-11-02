VERSION 1.0 CLASS
BEGIN
  MultiUse = -1  'True
END
Attribute VB_Name = "RawDataLens"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = False
Attribute VB_Exposed = False
' Class for a Entry in the RawDataTable.
' It holds the data but does nothing.

Private lensName As String
Private focalLength As String
Private focalLengthStart As Double
Private focalLengthEnd As Double
Private aperture As String
Private apertureStart As Double
Private apertureEnd As Double
Private filterSize1 As String
Private filterSize2 As Double
Private magnification1 As String
Private magnification2 As Double
Private mount As String
Private sensorCompatibiliy As String
Private weight1 As String
Private weight2 As Double
Private size As String
Private diameter As Double
Private length As Double


Public Property Get getLensName() As String
    getLensName = lensName
End Property
Public Property Get getFocalLength() As String
    getFocalLength = focalLength
End Property
Public Property Get getFocalLengthStart() As Double
    getFocalLengthStart = focalLengthStart
End Property
Public Property Get getFocalLengthEnd() As Double
    getFocalLengthEnd = focalLengthEnd
End Property
Public Property Get getAperture() As String
    getAperture = aperture
End Property
Public Property Get getApertureStart() As Double
    getApertureStart = apertureStart
End Property
Public Property Get getApertureEnd() As Double
    getApertureEnd = apertureEnd
End Property
Public Property Get getFilterSize1() As String
    getFilterSize1 = filterSize1
End Property
Public Property Get getFilterSize2() As Double
    getFilterSize2 = filterSize2
End Property
Public Property Get getMagnification1() As String
    getMagnification1 = magnification1
End Property
Public Property Get getMagnification2() As Double
    getMagnification2 = magnification2
End Property
Public Property Get getMount() As String
    getMount = mount
End Property
Public Property Get getSensorCompatibility() As String
    getSensorCompatibility = sensorCompatibiliy
End Property
Public Property Get getWeight1() As String
    getWeight1 = weight1
End Property
Public Property Get getWeight2() As Double
    getWeight2 = weight2
End Property
Public Property Get getSize() As String
    getSize = size
End Property
Public Property Get getDiameter() As Double
    getDiameter = diameter
End Property
Public Property Get getLength() As Double
    getLength = length
End Property

Private Sub Class_Initialize()
End Sub

Public Function Init(newLensName As String, _
                        newFocalLength As String, _
                        newFocalLengthStart As Double, _
                        newFocalLengthEnd As Double, _
                        newAperture As String, _
                        newApertureStart As Double, _
                        newApertureEnd As Double, _
                        newFilterSize1 As String, _
                        newFilterSize2 As Double, _
                        newMagnification1 As String, _
                        newMagnification2 As Double, _
                        newMount As String, _
                        newSensorCompatibiliy As String, _
                        newWeight1 As String, _
                        newWeight2 As Double, _
                        newSize As String, _
                        newDiameter As Double, _
                        newLength As Double)
    lensName = newLensName
    focalLength = newFocalLength
    focalLengthStart = newFocalLengthStart
    focalLengthEnd = newFocalLengthEnd
    aperture = newAperture
    apertureStart = newApertureStart
    apertureEnd = newApertureEnd
    filterSize1 = newFilterSize1
    filterSize2 = newFilterSize2
    magnification1 = newMagnification1
    magnification2 = newMagnification2
    mount = newMount
    sensorCompatibiliy = newSensorCompatibiliy
    weight1 = newWeight1
    weight2 = newWeight2
    size = newSize
    diameter = newDiameter
    length = newLength

End Function






