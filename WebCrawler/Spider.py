import scrapy
import time

TEST_GH_PRODDESC'<div id="gh_proddesc">\nTyp: Tele-Objektiv \x95  \
	Brennweite: 800mm \x95  \
	Lichtstärke: 1:5.6 \x95 \
	Optischer Aufbau (Linsen/\u200bGruppen): 20/\u200b13 \x95 \
	Blendenlamellen: 9 (abgerundet) \x95 \
	Bildstabilisator: VR \x95 \
	Fokussiermotor: SWM \x95 \
	Naheinstellgrenze: 5.90m \x95 \
	Kleinste Blende: 32 \x95 \
	Abbildungsmaßstab: 1:6.7 \x95 Objektivbajonett: Nikon F \x95 \
	Sensorkompatibilität: APS-C/\u200bKleinbild \x95 \
	Filterdurchmesser: 52mm \x95 \
	Abmessungen (ØxL): 160x461mm \x95 \
	Gewicht:4.59kg\
	<p>EAN-Codes: 18208022052</p>\n\
	<p>Gelistet seit: 30.01.2013, 12:58</p>\n\
	<p>\n6 von 7 Besuchern empfehlen dieses Produkt (<b>86%</b>).<br>\n\
	<span itemprop=\'"aggregateRating"\' itemscope itemtype=\'"http://schema.org/AggregateRating\'>\n\
	<meta itemprop="ratingValue" content="4.46428571428571.2f">\n\
	<meta itemprop="ratingCount" content="7">\n\
	Bewertung:\n<a onclick="registerConversionTag([\'productpage_rating_stars\',\'2\', window.ghPageTypeCM, \'0\']);" href="./?sr=897954,-1">\n<span class="gh_stars" title="4.46 von 5"><span class="gh_stars1" style="width:89%"></span></span></a>\n\
	(<span>87%</span>)\n\
	(<a onclick="registerConversionTag([\'productpage_rating_read\',\'2\', window.ghPageTypeCM, \'0\']);" href="./?sr=897954,-1" rel="nofollow"><span>1\n</span>\nBewertung lesen</a> |\n\
	<a onclick="registerConversionTag([\'productpage_rating_rate\',\'2\', window.ghPageTypeCM, \'0\']);" href="./bew_897954.html" rel="nofollow">Produkt bewerten</a>)\n</span>\n</p>\n</div>'

KEYS = [
		"Brennweite",
		"Lichtstärke",
		"Abbildungsmaßstab",
		"Sensorkompatibilität",
		"Filterdurchmesser",
		"Abmessungen (ØxL)",
		"Gewicht"
		]

def getStringValue(key, string):
	keyLength = len(key)
	valueStartPos = string.find(key) + 2 + keyLength
	rawValue = string[valueStartPos:]
	valueEndPos = rawValue.find(" ")
	value = rawValue[:valueEndPos]
	return value

def collectNecessaryGHLensData(gh_proddesc):
	result = {}
	for key in KEYS:
		result.update(key,getStringValue(key,gh_proddesc))
	return result

def checkAndCollectGHLensData(gh_proddesc):
	#gh_proddesc is result of "response.xpath('//div[@id = "gh_proddesc"]').extract()[0]
	if gh_proddesc is not None:
		return collectNecessaryGHLensData(gh_proddesc)

class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    start_urls = ['https://geizhals.de/?cat=acamobjo&xf=8219_Nikon+F']

    def parseLensPage(self, response):
        gh_proddesc = response.xpath('//div[@id="gh_proddesc"]').extract_first()
        allData = checkAndCollectGHLensData(gh_proddesc)
        #Es fehlen dann noch folgende Infos:
        	#Vollständiger Lensname
        	#Mount
        writeToTempRawFile(allData)

    def parse(self, response):
        for lens_page in response.xpath('//a[@class = "productlist__link"]'):
        	time.sleep(1) # 1 sekunde schlafen
        	yield response.follow(lens_page, self.parseLensPage)

        time.sleep(10) #10 Sekunden schlafen

        next_page = response.xpath('//a[@class = "gh_pag_i only--desktop gh_pag_i_last gh_pag_next_active"'):
        	yield response.follow(overview_page, self.parse)