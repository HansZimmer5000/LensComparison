Attribute VB_Name = "WebCrawler"

' This class connect the excel file to the WebCrawler to get new data.
' Class is the mentioned WebCrawler Module in the UML Component Diagramm.

Sub runAllPythonTests()
	Dim command as String
	Dim excelFilePath as String

	excelFilePath = ActiveWorkbook.Path
	command = "python " + excelFilePath + "\WebCrawler\testall.py"
	Call executeShellCommand(command, True, True)
End Sub


Private Function runSpider()
	Dim command as String
	Dim excelFilePath as String

	excelFilePath = ActiveWorkbook.Path
	command = "python" + " " + excelFilePath + "\WebCrawler\StartCrawling.py"
	Call executeShellCommand(command, True, True)
End Function

Private Function getAllRawData()
	'Todo:
	'Open File
	'Get all Lensinfos
	'Copy everything to RawData shet in Alllenses.xlsm
	'Set every row in PreparedData Sheet with right function with link to the rawdata Sheet
	'Close Files
End Function


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
