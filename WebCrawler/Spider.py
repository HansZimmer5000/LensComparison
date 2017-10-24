# This module is about my webcrawler with the use of scrapy.
# Its a generell web crawler, but the import and use of GhAdapter makes it usefull for geizhals.de sites.

# TODO: Make it fully general / adaptable, so its not limited to one site.
# TODO: Split every thing up, functions, the class and other executable code.

import scrapy
import time
import GhAdapter
import GhExamples

def writeToTempRawFile(lensDataDict):
	rawfile = open("rawData.csv","a")
	for key in lensDataDict.keys():
		rawfile.write(lensDataDict[key]+";")
	rawfile.write("\n")
	rawfile.close()

def cleanRawDataFile():
	rawfile = open("rawResponseData.csv", 'w').close()

def cleanFileAndWriteTitles():
	#Didn't decide to use cleanRawDataFile Function because than I head to open / close it twice
	rawfile = open("rawData.csv", 'w') 
	for key in GhAdapter.ALL_KEYS:
		rawfile.write(key+";")
	rawfile.write("\n")
	rawfile.close()

def clearOfNewLines(string):
	return string.replace("\n", " ")

def writeRawData(gh_proddesc,gh_prodImg):
	rawfile = open("rawResponseData.csv", 'a')
	clearedGhProddesc = clearOfNewLines(gh_proddesc.replace("\x95"," ").replace("\u200b"," "))
	if gh_prodImg is None:
		clearedGhProdimg = ""
	else:
		clearedGhProdimg = clearOfNewLines(gh_prodImg.replace("\x95"," ").replace("\u200b"," "))
	
	rawfile.write(clearedGhProddesc + ";" + clearedGhProdimg + "\n")
	rawfile.close()

def createNextOverviewPage(a):
	tmpResult = GhAdapter.getAttributeValue('href="',a,'"')
	result = tmpResult.replace(".","https://geizhals.de",1)
	return result

class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    start_urls = ['https://geizhals.de/?cat=acamobjo&amp;pg=12']

	cleanRawDataFile()

    def parseLensPage(self, response):
        gh_proddesc = response.xpath('//div[@id="gh_proddesc"]').extract_first()
        gh_prodImg = response.xpath('//img[@class="gh_prodImg"]').extract_first()
        writeRawData(gh_proddesc,gh_prodImg)
        #writeToTempRawFile(GhAdapter.getAllAttributes(gh_proddesc,gh_prodImg))

    def parse(self, response):
    	print("parsing!")
    	for lens_page in response.xpath('//a[@class = "productlist__link"]'):
    		time.sleep(10) # sekunden schlafen
    		yield response.follow(lens_page, self.parseLensPage)

    	time.sleep(10) # Sekunden schlafen

    	nextPageRawUrl = response.xpath('//a[@class = "gh_pag_i only--desktop gh_pag_i_last gh_pag_next_active"]').extract_first()[3:80]
    	nextPageUrl = createNextOverviewPage(nextPageRawUrl)
    	if nextPageUrl is not None:
    		yield scrapy.Request(nextPageUrl, callback=self.parse)

