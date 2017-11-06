'VERSION 1.0 CLASS
'BEGIN
''  MultiUse = -1  'True
'END
Attribute VB_Name = "WebCrawler"
'Attribute VB_GlobalNameSpace = False
'Attribute VB_Creatable = False
'Attribute VB_PredeclaredId = False
'Attribute VB_Exposed = False

' This class connect the excel file to the WebCrawler to get new data.
' Class is the mentioned WebCrawler Module in the UML Component Diagramm.

Sub runAllPythonTests()
	dim command as String

	command = "python C:\Users\Michael\IdeaProjects\NikonLensComparison\WebCrawler\testall.py"
	Call executeShellCommand(command, True, True)
End Sub

Private Function executeShellCommand(command, waitForReturn as Boolean, keepShellOpen as Boolean)
	'From https://stackoverflow.com/a/17956816/8136274
	'/S Modifies the treatment of string after /C or /K (see below) 
	'/C Carries out the command specified by string and then terminates  
	'/K Carries out the command specified by string but remains  '
    Const WINDOW_STYLE As Integer = 1

    Dim wsShell As Object
    Dim secondShellParameter as String

    Set wsShell = VBA.CreateObject("WScript.Shell")

    if(keepShellOpen) then
 		secondShellParameter = "/K"
 	Else
 		secondShellParameter = "/C"
 	End if

    wsShell.Run "cmd.exe /S "+secondShellParameter+" " + command, WINDOW_STYLE, waitForReturn
End Function