Attribute VB_Name = "ModuleManager"
' To run this Code its needed to do following Steps:
'1. Get to the the Trust Center tab, and then click Trust Center Settings.
'2. Click the Macro Settings tab, click to select the Trust access to the VBA project object model check box, and then click OK.
'3. Click OK

Sub updateAllModules()
    Call deleteAllModulesExceptThisOne
    Call addAllModules
End Sub

Private Sub addAllModules()
    Dim mainDirectoryPath As String
    
    mainDirectoryPath = ThisWorkbook.Path + "\VBA Files\"

    For Each moduleFullPath In getAllModuleFullPaths(mainDirectoryPath)
        ThisWorkbook.VBProject.VBComponents.Import (moduleFullPath)
    Next
End Sub

Private Sub deleteAllModulesExceptThisOne()
    For Each currentModul In ThisWorkbook.VBProject.VBComponents
        If (Not (currentModul.name = "ModuleManager" Or _
                currentModul.name = "DieseArbeitsmappe" Or _
                InStr(currentModul.name, "Tabelle") > 0)) Then
            
            ThisWorkbook.VBProject.VBComponents.Remove (currentModul)
        End If
    Next
End Sub

Private Function getAllModuleFullPaths(rootDirFullPath As String) As Collection
    'https://msdn.microsoft.com/de-de/library/1c87day3(v=vs.84).aspx
    
    Dim objFSO As Object
    Dim objFolder As Object
    Dim tempSubFolderFiles As Collection
    Dim rootFolderFullPath As String
    
    Set objFSO = CreateObject("Scripting.FileSystemObject")
    Set objFolder = objFSO.GetFolder(rootDirFullPath)
    Set getAllModuleFullPaths = New Collection
    
    For Each file In objFolder.Files
        If (InStr(file.Path, "ModuleManager") <= 0) Then
            getAllModuleFullPaths.Add file.Path
        End If
    Next
    
    For Each subFolder In objFolder.SubFolders
        Debug.Print ("SubFolder: " + subFolder.Path)
        Set tempSubFolderFiles = getAllModuleFullPaths(subFolder.Path + "\")
        Call addSecondToFirstCollection(getAllModuleFullPaths, tempSubFolderFiles)
    Next
End Function

Private Function addSecondToFirstCollection(ByRef mainColl As Collection, ByVal newColl As Collection)
    For Each elem In newColl
        mainColl.Add elem
    Next
End Function

