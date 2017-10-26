# This Module is about getting the Data from the rawResponse files which are just 1:1 downloads of each product site, into the RawData csv.

# Flow
# 1. Get Fullpath + Name of rawResponse Files
# 2. Open RawData File
# 3. Take rawResponse file and extract for each lens the import data (if existent)
#   A. Get Row as one string, columns differ with ";"
#   B. Get (if existent, else just "") data from columns:
#       1. Column = prodDesc ------   Always there, but may not complete
#       2. till n-1. Column = Links   Sometimes there
#       n. Column = prodImg -------   Sometimes there
#           Data            Looks like                  get from
#       - Full Lensname (Text with numbers)         prodImg // Links (href != "href=./")
#       - Focal Length  (000mm - 000mm // 000mm)    prodDesc
#       - Aperture      (F/0.0 - 0.0)               prodDesc
#       - Filterthread  (00mm)                      prodDesc
#       - Magnification (0.26X // 1,00 // 1:3)      prodDesc
#       - Mount         (Nikon F // Canon EF// ...) prodDesc
#       - Sensor Compatibility (Full-Frame // APS-C) prodDesc
#       - Weight        (000g)                      prodDesc
#       - Size          (Diameter x Length"mm")     prodDesc
#   D. Return to Step 4 with this extracted data.
# 4. Write this data to RawData file, because some files are big its may better to write directly every n rows, till last row is reached.
# 5. Close current rawResponse file, continue at 3 with the next rawResponse file.
# 6. If every rawResponse file is done, close RawData file.

from glob import glob
from tqdm import tqdm
import GhAdapter
import Spider

# Module Variables
totalProcessesRows = 0
totalWrittenRows = 0

# Module Constants
EMPTY_DICT = GhAdapter.createEmtpyDict()

def getAllrawResponseFullPaths(directory):
    rawResponseName = "rawResponse*.csv"
    return glob(directory + rawResponseName)

def extractrawResponseFileAndWriteToRawData(rawResponseFile):
    MAX_DICT_LIST_SIZE = 1000 #As it gets bigger it gets faster.
    global totalProcessesRows
    #TODO: Problem if this constant is bigger then one. Problem pretty sure how I use the index in the while loop.

    #Open file and go through every row, then give rowtext (rows differs by '\n') to extractDataFromrawResponseRow
    rowTexts = rawResponseFile.read().split("\n")
    rowTextCount = len(rowTexts)
    currentDictList = []
    currentRowIndex = 0

    while(currentRowIndex < rowTextCount):
        #Save each return dict in a list, if list is bigger than *n* save into rawData file.

        currentRowText = rowTexts[currentRowIndex]
        if(GhAdapter.checkIfRawProdSiteIsValid(currentRowText)):
            currentDict = extractDataFromrawResponseRow(currentRowText)
            currentDictList.append(currentDict)
            if((len(currentDictList) == MAX_DICT_LIST_SIZE) or (currentRowIndex == rowTextCount - 1)):
                writeExtractedDictsToRawData(currentDictList)
                currentDictList = []

        currentRowIndex += 1
        totalProcessesRows += 1
    

def extractDataFromrawResponseRow(row):
    #find prodDesc, search for name in prodImg / links
    #return all found data in a dict.
    PROD_DESC_INDEX = 0

    prodDesc = getProdDescFromRawSite(row)
    prodImg = getProdImgFromRawSite(row)

    resultDict = GhAdapter.getAllAttributes(prodDesc, prodImg)
    # If there is no prodImg, the lens will have a empty lensname -> let them just aside?
    return resultDict

def writeExtractedDictsToRawData(dictList):
    global totalWrittenRows

    rawDataFullPath = "C:/Users/Michael/IdeaProjects/NikonLensComparison/WebCrawler/rawData.csv"
    rawDataFile = open(rawDataFullPath,"a")
    
    for currentDict in dictList:
        if(currentDict != EMPTY_DICT):
            currentDictText = GhAdapter.convertDictToCSVValueString(currentDict)
            rawDataFile.write(currentDictText + "\n")
            totalWrittenRows += 1

    rawDataFile.close()

def getProdImgFromRawSite(rawsite):
    indexOfProdImgTag = rawsite.find("gh_prodImg")
    if(indexOfProdImgTag < 0):
        return ""
    else:
        prodImg = rawsite[indexOfProdImgTag+1:]
        return prodImg

def getProdDescFromRawSite(rawsite):
    indexOfProdImgTag = rawsite.find("gh_prodImg")
    if(indexOfProdImgTag < 0):
        return rawsite
    else:
        prodDesc = rawsite[:indexOfProdImgTag]
        return prodDesc

if __name__ == "__main__":
    #If this module is not imported, do this code

    RAW_RESPONSE_DIR = "C:/Users/Michael/IdeaProjects/NikonLensComparison/WebCrawler/"

    print("Type 'clean' to clean the rawDataFile or 'import' to import new Data.")
    userInput = input()

    if(userInput == "import"):
        allrawResponseFullPaths = getAllrawResponseFullPaths(RAW_RESPONSE_DIR)

        for currentrawResponseFullPath in allrawResponseFullPaths:
            print(currentrawResponseFullPath)
            rawResponseFile = open(currentrawResponseFullPath,"r")
            extractrawResponseFileAndWriteToRawData(rawResponseFile)
            rawResponseFile.close()

        print("Total Count of Processed Rows: " + str(totalProcessesRows))
        print("Total Count of Written Rows: " + str(totalWrittenRows))

    elif(userInput == "clean"):
        Spider.cleanFileAndWriteTitles()