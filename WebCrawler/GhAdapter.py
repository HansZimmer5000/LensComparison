KEY_LENSNAME = 'title=""'
KEY_FOCAL_LENGTH = "Brennweite: "
KEY_APERTURE = "Lichtstärke: " 
KEY_FILTER = "Filterdurchmesser: "
KEY_MAGNIFICATION = "Abbildungsmaßstab: " 
KEY_MOUNT = "Objektivbajonett: "
KEY_SENSORKOMPATIBILITÄT = "Sensorkompatibilität: " 
KEY_WEIGHT = "Gewicht: "
KEY_SIZE = "Abmessungen (ØxL): "

ALL_KEYS = [
	KEY_LENSNAME,
	KEY_FOCAL_LENGTH, 
	KEY_APERTURE,
	KEY_FILTER, 
	KEY_MAGNIFICATION,
	KEY_MOUNT,
	KEY_SENSORKOMPATIBILITÄT,
	KEY_WEIGHT,
	KEY_SIZE]

SORT_OUT_STRINGS_FOR_TITLE=[
	"verschiedene Modelle",
	"Pro Set"
]

def getAllAttributes(prodDesc,prodImg):
	
	resultDict = {
		KEY_LENSNAME: getLensName(prodImg)
	}
	resultDict.update(
		getAllProdDescAttributes(prodDesc)
	)

	return resultDict

def checkIfRawProdSiteIsValid(rawProdSite):
	for currentSortOutString in SORT_OUT_STRINGS_FOR_TITLE:
		if(currentSortOutString in rawProdSite):
			return False

	return True	

def checkIfDataIsValid(prodImg):
	title = getLensNameFromProdImg(prodImg)
	if(title == ""):
		return True

	for currentSortOutString in SORT_OUT_STRINGS_FOR_TITLE:
		if(currentSortOutString in title):
			return False

	return True


def getAllProdDescAttributes(prodDesc):
	return {
		KEY_FOCAL_LENGTH: getFocalLength(prodDesc), 
		KEY_APERTURE: getAperture(prodDesc),
		KEY_FILTER: getFilter(prodDesc), 
		KEY_MAGNIFICATION: getMagnification(prodDesc),
		KEY_MOUNT: getMount(prodDesc),
		KEY_SENSORKOMPATIBILITÄT: getSensor(prodDesc),
		KEY_WEIGHT: getWeight(prodDesc),
		KEY_SIZE: getSize(prodDesc)
	}

def getLensName(prodImg):
	#TODO: Maybe later: get LensnameFromSiteTitle here in a ifcase
	return getLensNameFromProdImg(prodImg)

def getLensNameFromProdImg(prodImg):
	return getAttributeValue(KEY_LENSNAME,prodImg,'"">')

def getFocalLength(prodDesc):
	return getAttributeValue(KEY_FOCAL_LENGTH,prodDesc," ")

def getAperture(prodDesc):
	return getAttributeValue(KEY_APERTURE,prodDesc," ")

def getFilter(prodDesc):
	return getAttributeValue(KEY_FILTER,prodDesc," ")

def getMagnification(prodDesc):
	return getAttributeValue(KEY_MAGNIFICATION,prodDesc," ")

def getMount(prodDesc):
	return getAttributeValue(KEY_MOUNT,prodDesc,"  ")
	
def getSensor(prodDesc):
	return getAttributeValue(KEY_SENSORKOMPATIBILITÄT,prodDesc,"  ")

def getWeight(prodDesc):
	weightWithoutLetterG = getAttributeValue(KEY_WEIGHT,prodDesc,"g")
	if(weightWithoutLetterG == ""):
		return ""
	else:
		return weightWithoutLetterG + "g"

def getSize(prodDesc):
	return getAttributeValue(KEY_SIZE,prodDesc," ")

def getAttributeValue(key,string,valueTillKey):
	keyLength = len(key)
	keyStartPos = string.find(key)
	if(keyStartPos >= 0):
		valueStartPos = keyStartPos + keyLength
		rawValue = string[valueStartPos:]
		valueEndPos = rawValue.find(valueTillKey)
		value = rawValue[:valueEndPos]
		result = value
	else:
		result = ""

	if("<p>" in result):
		result = result.split("<p>")[0]
	
	return result

def convertDictToCSVValueString(dict):
	currentValue = ""
	currentKey = ""
	currentIndex = 0
	result = ""

	while(currentIndex < len(ALL_KEYS)):
		currentKey = ALL_KEYS[currentIndex]
		try:
			currentValue = dict[currentKey]

			result += currentValue
			if(currentIndex != len(ALL_KEYS)-1):
				result += ";"
			currentIndex += 1
		except KeyError:
			result = convertDictToCSVValueString(createEmtpyDict)
			currentIndex = len(ALL_KEYS)


	return result

def createEmtpyDict():
	emptyDict = {}
	for currentKey in ALL_KEYS:
		emptyDict.update({currentKey: ""})
	return emptyDict