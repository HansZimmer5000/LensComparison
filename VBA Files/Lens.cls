VERSION 1.0 CLASS
BEGIN
  MultiUse = -1  'True
END
Attribute VB_Name = "Lens"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = False
Attribute VB_Exposed = False
' Class to hold all the necessary info for the ResultTable
'
Private lensName As String
Private focalLengthStart As Double
Private focalLengthEnd As Double
Private apertureStart As Double
Private apertureEnd As Double
Private filtersize As Double
Private magnification As Double
Private mount As String
Private sensorCompatibiliy As String
Private weight As Double
Private diameter As Double
Private length As Double


Public Property Get getLensName() As String
    getLensName = lensName
End Property
Public Property Get getFocalLengthStart() As Double
    getFocalLengthStart = focalLengthStart
End Property
Public Property Get getFocalLengthEnd() As Double
    getFocalLengthEnd = focalLengthEnd
End Property
Public Property Get getApertureStart() As Double
    getApertureStart = apertureStart
End Property
Public Property Get getApertureEnd() As Double
    getApertureEnd = apertureEnd
End Property
Public Property Get getFilterSize() As Double
    getFilterSize = filtersize
End Property
Public Property Get getMagnification() As Double
    getMagnification = magnification
End Property
Public Property Get getMount() As String
    getMount = mount
End Property
Public Property Get getSensorCompatibility() As String
    getSensorCompatibility = sensorCompatibiliy
End Property
Public Property Get getWeight() As Double
    getWeight = weight
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
                        newFocalLengthStart As Double, _
                        newFocalLengthEnd As Double, _
                        newApertureStart As Double, _
                        newApertureEnd As Double, _
                        newFilterSize As Double, _
                        newMagnification As Double, _
                        newMount As String, _
                        newSensorCompatibiliy As String, _
                        newWeight As Double, _
                        newDiameter As Double, _
                        newLength As Double)
    lensName = newLensName
    focalLengthStart = newFocalLengthStart
    focalLengthEnd = newFocalLengthEnd
    apertureStart = newApertureStart
    apertureEnd = newApertureEnd
    filtersize = newFilterSize
    magnification = newMagnification
    mount = newMount
    sensorCompatibiliy = newSensorCompatibiliy
    weight = newWeight
    diameter = newDiameter
    length = newLength

End Function

Function equals(obj as Variant) as Boolean
    equals = False

    if(StrComp(TypeName(obj), "Lens") = 0) Then
        if(StrComp(Me.getLensName(),obj.getLensName()) = 0 and _
            Me.getFocalLengthStart() = obj.getFocalLengthStart() and _ 
            Me.getFocalLengthEnd() = obj.getFocalLengthEnd() and _
            Me.getApertureStart() = obj.getApertureStart() and _
            Me.getApertureEnd() = obj.getApertureEnd() and _
            Me.getFilterSize() = obj.getFilterSize() and _
            Me.getMagnification() = obj.getMagnification() and _
            StrComp(Me.getMount(),obj.getMount()) = 0 and _
            StrComp(Me.getSensorCompatibility(), obj.getSensorCompatibility()) = 0 and _
            Me.getWeight() = obj.getWeight() and _
            Me.getDiameter() = obj.getDiameter() and _
            Me.getLength() = obj.getLength()) Then
            equals = True
        end If
    End If
End Function