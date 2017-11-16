#  Is this too much or is it relevant for this small project? - too much, but I am too lazy to do something that might has not a big impact at all. So I just do some of these tests.
# 1) No data: Run your TESTDATA cases on blank or default data. See if proper error messages are generated.
# 2) Valid data set: Create it to check if the application is functioning as per requirements and valid input data is properly saved in database or files.
# 3) Invalid data set: Prepare invalid data set to check application behavior for negative values, alphanumeric string inputs.
# 5) Illegal data format: Make one data set of illegal data format. The system should not accept data in invalid or illegal format. Also, check proper error messages are generated.
# 5) Boundary Condition dataset: Dataset containing out of range data. Identify application boundary cases and prepare data set that will cover lower as well as upper boundary conditions.
# 6) The dataset for performance, load and stress TESTDATAing: This data set should be large in volume.

#\\\\\\\\\\\\\\\\\\\\\\\\\
#	TESTDATA_DICT_FULLs
#/////////////////////////

TESTDATA_DICT_WITHOUT_VALUES = {
	'title=""': '', \
	'Brennweite: ': '', \
	'Lichtstärke: ': '', \
	'Filterdurchmesser: ': "", \
	'Abbildungsmaßstab: ': "", \
	'Naheinstellgrenze: ': "", \
 	'Objektivbajonett: ': '', \
	'Sensorkompatibilität: ': '', \
 	'Gewicht: ': '',\
	'Abmessungen (ØxL): ': ''	
}

TESTDATA_DICT_WITH_EVERYTHING1 = {
	'title=""': 'Nikon 1 NIKKOR VR 10-30mm 3.5-5.6 PD-Zoom schwarz (JVA707DA)', \
	'Brennweite: ': '10-30mm', \
	'Lichtstärke: ': '1:3.5-1:5.6', \
	'Filterdurchmesser: ': "", \
	'Abbildungsmaßstab: ': "", \
	'Naheinstellgrenze: ': "0.20m", \
 	'Objektivbajonett: ': 'Nikon 1', \
	'Sensorkompatibilität: ': 'Nikon CX', \
 	'Gewicht: ': '85g',\
	'Abmessungen (ØxL): ': '58x28mm'}

TESTDATA_DICT_WITH_EVERYTHING2 = {
	'title=""': 'Nikon AF-S VR 200-500mm 5.6E ED schwarz (JAA822DA)', \
	'Brennweite: ': '200-500mm', \
	'Lichtstärke: ': '1:5.6', \
	'Filterdurchmesser: ': '95mm', \
	'Abbildungsmaßstab: ': '1:4.50', \
	'Naheinstellgrenze: ': "2.20m", \
 	'Objektivbajonett: ': 'Nikon F', \
	'Sensorkompatibilität: ': 'APS-C/ Kleinbild', \
 	'Gewicht: ': '2300g', \
	'Abmessungen (ØxL): ': '108x267.5mm'
}

TESTDATA_DICT_WITH_EVERYTHING3 = {
	'title=""': 'Samyang 35mm 1.4 AS UMC für Sony E schwarz', \
	'Brennweite: ': '35mm', \
	'Lichtstärke: ': '1:1.4', \
	'Filterdurchmesser: ': '77mm', \
	'Abbildungsmaßstab: ': '', \
	'Naheinstellgrenze: ': "0.30m", \
 	'Objektivbajonett: ': 'Sony E', \
	'Sensorkompatibilität: ': 'APS-C', \
 	'Gewicht: ': '660g', \
	'Abmessungen (ØxL): ': '83x111mm'
}

TESTDATA_DICT_WITH_MISSING_INFO1 = {
	'title=""': 'Canon Objektiv CN-E 35mm T1.5 L F schwarz (9139B001)', \
	'Brennweite: ': '35mm', \
	'Lichtstärke: ': '1:1.5', \
	'Filterdurchmesser: ': "", \
	'Abbildungsmaßstab: ': "", \
	'Naheinstellgrenze: ': "", \
 	'Objektivbajonett: ': 'Canon EF', \
	'Sensorkompatibilität: ': 'APS-C/ Kleinbild', \
 	'Gewicht: ': '',\
	'Abmessungen (ØxL): ': ''		
}

TESTDATA_DICT_RAW_WITHOUT_PRODIMG1 = {
	'title=""': '', \
	'Brennweite: ': '25mm', \
	'Lichtstärke: ': '1:0.95', \
	'Filterdurchmesser: ': "52mm", \
	'Abbildungsmaßstab: ': "", \
	'Naheinstellgrenze: ': "0.17m", \
 	'Objektivbajonett: ': 'Micro-Four-Thirds', \
	'Sensorkompatibilität: ': 'Four-Thirds', \
 	'Gewicht: ': '410g',\
	'Abmessungen (ØxL): ': '58.4x70mm'}

	
TESTDATA_DICT_VALUE_STRING_WITHOUT_VALUES = ";;;;;;;;;"
TESTDATA_DICT_VALUE_STRING_WITH_EVERYTHING1 = \
'Nikon 1 NIKKOR VR 10-30mm 3.5-5.6 PD-Zoom schwarz (JVA707DA);10-30mm;1:3.5-1:5.6;;;0.20m;Nikon 1;Nikon CX;85g;58x28mm'

TESTDATA_DICT_RAWRESPONSE_TWELVE_SIXTY_ENTRY_1   = TESTDATA_DICT_WITH_EVERYTHING1
TESTDATA_DICT_RAWRESPONSE_TWELVE_SIXTY_ENTRY_269 = TESTDATA_DICT_RAW_WITHOUT_PRODIMG1
TESTDATA_DICT_RAWRESPONSE_TWELVE_SIXTY_ENTRY_761 = TESTDATA_DICT_WITH_MISSING_INFO1
TESTDATA_DICT_VALUE_STRING_RAWRESPONSE_TWELVE_SIXTY_ENTRY_1 = TESTDATA_DICT_VALUE_STRING_WITH_EVERYTHING1

#\\\\\\\\\\\\\\\\\\\\\\\\\
#	TESTDATA_PRODDESC_WITH_PRODIMG_RAWs
#	Displayed how Python would read it (with "open" fucntion)
#/////////////////////////

TESTDATA_PRODDESC_WITH_PRODIMG_RAW_WITH_EVERYTHING1 = '"<div id=""gh_proddesc""> Typ: Universal-Zoom-Objektiv   Brennweite: 10-30mm  ' + \
'Lichtstärke: 1:3.5-1:5.6   Optischer Aufbau (Linsen/ Gruppen): 9/ 7   Blendenlam' + \
'ellen: 7 (abgerundet)   Bildstabilisator: VR   Fokussiermotor: SWM   Naheinstell' + \
'grenze: 0.20m   Kleinste Blende: 16   Objektivbajonett: Nikon 1   Sensorkompatib' + \
'ilität: Nikon CX   Abmessungen (ØxL): 58x28mm   Gewicht: 85g   Besonderheiten: P' + \
'ancake<p>EAN-Codes: 18208033676, 4960759028549, 5269692856219</p> <p>Gelistet se' + \
'it: 13.03.2014, 10:40</p> <p> Siehe auch: <a onclick=""registerConversionTag([\'' + \
'relatedproducts_click\', \'2\', window.ghPageTypeCM, \'0\'])";" href=nikon-1-nik' + \
'kor-vr-10-30mm-3-5-5-6-pd-zoom-silber-a1084341.html""> Nikon 1 NIKKOR VR 10-30mm' + \
' 3.5-5.6 PD-Zoom silber</a>, <a onclick=""registerConversionTag([\'relatedproduc' + \
'ts_click\', \'2\', window.ghPageTypeCM, \'0\'])";" href=nikon-1-nikkor-vr-10-30m' + \
'm-3-5-5-6-pd-zoom-weiss-jva707db-a1084342.html""> Nikon 1 NIKKOR VR 10-30mm 3.5-' + \
'5.6 PD-Zoom weiß (JVA707DB)</a>, <a onclick=""registerConversionTag([\'relatedpr' + \
'oducts_click\', \'2\', window.ghPageTypeCM, \'0\'])";" href=nikon-1-nikkor-vr-10' + \
'-30mm-3-5-5-6-pd-zoom-rot-a1084346.html""> Nikon 1 NIKKOR VR 10-30mm 3.5-5.6 PD-' + \
'Zoom rot</a>, <a onclick=""registerConversionTag([\'relatedproducts_click\', \'2' + \
'\', window.ghPageTypeCM, \'0\'])";" href=nikon-1-nikkor-vr-10-30mm-3-5-5-6-pd-zo' + \
'om-orange-a1084351.html""> Nikon 1 NIKKOR VR 10-30mm 3.5-5.6 PD-Zoom orange</a>,' + \
' <a onclick=""registerConversionTag([\'relatedproducts_click\', \'2\', window.gh' + \
'PageTypeCM, \'0\'])";" href=nikon-1-nikkor-vr-10-30mm-3-5-5-6-pd-zoom-gelb-a1084' + \
'352.html""> Nikon 1 NIKKOR VR 10-30mm 3.5-5.6 PD-Zoom gelb</a> </p> <p>Es liegen' + \
' noch keine Bewertungen für dieses Produkt vor (<a onclick=""registerConversionT' + \
'ag([\'productpage_rating_rate\',\'2\', window.ghPageTypeCM, \'0\'])";" rel=nofol' + \
'low"" href=""bew_1084320.html"">Produkt bewerten</a>).</p> </div>";"<img class="' + \
'"gh_prodImg"" id=""gh_prodImg"" src=""//gzhls.at/i/43/20/1084320-n0.jpg"" alt=""' + \
'Nikon 1 NIKKOR VR 10-30mm 3.5-5.6 PD-Zoom schwarz (JVA707DA)"" title=""Nikon 1 N' + \
'IKKOR VR 10-30mm 3.5-5.6 PD-Zoom schwarz (JVA707DA)"">"'

TESTDATA_PRODDESC_WITH_PRODIMG_RAW_WITH_EVERYTHING2 = '"<div id=""gh_proddesc""> Typ: Tele-Zoom-Objektiv   ' +\
'Brennweite: 200-500mm   Lichtstärke: 1:5.6   Optischer Aufbau (Linsen/ Gruppen): 19/ 12   ' +\
'Blendenlamellen: 9 (abgerundet)Bildstabilisator: VR   Fokussiermotor: SWM   Naheinstellgrenze: 2.20m   ' +\
'Kleinste Blende: 32   Abbildungsmaßstab: 1:4.50   Objektivbajonett: Nikon F   Sensorkompatibilität: APS-C' +\
'/ Kleinbild   Filterdurchmesser: 95mm   Abmessungen (ØxL): 108x267.5mm   Gewicht: 2.30kg<p>EAN-Codes: 0231844354459, ' +\
'18208200580, 4960759145765</p> <p>Gelistet seit: 04.08.2015, 13:02</p> <p> 4 von 4 Besuchern empfehlen dieses ' +\
'Produkt (<b>100%</b>).<br> <span itemprop=\'""aggregateRating""\' itemscope itemtype=\'""http://schema.org/AggregateRating\'> ' +\
'<meta itemprop=""ratingValue"" content=""5.2f""> <meta itemprop=""ratingCount"" content=""6""> Bewertung: ' +\
'<a onclick=""registerConversionTag([\'productpage_rating_stars\',\'2\',' +\
'window.ghPageTypeCM, \'0\'])";" href=./?sr=1306077,-1""> <span class=""gh_stars"" title=""5.00 von 5"">' +\
'<span class=""gh_stars1"" style=""width:100%""></span></span></a> (<span>1' +\
'00%</span>) (<a onclick=""registerConversionTag([\'productpage_rating_read\',\'2\', window.ghPageTypeCM, \'0\'])";"' +\
"'"+' href=./?sr=1306077,-1"" rel=""nofollow""><span>2 </span> Bewertungen lesen</a> | ' +\
' <a onclick=""registerConversionTag([\'productpage_rating_rate\',\'2\', window.ghPageTypeCM, \'0\'])";"' +\
"'"+' href=./bew_1306077.html"" rel=""nofollow"">Produkt bewerten</a>) </span> </p> </div>";"' +\
'<img class=""gh_prodImg"" id=""gh_prodImg"" src=""//gzhls.at/i/60/77/1306077-n0.jpg"" ' +\
'alt=""Nikon AF-S VR 200-500mm 5.6E ED schwarz (JAA822DA)""' +\
' title=""Nikon AF-S VR 200-500mm 5.6E ED schwarz (JAA822DA)"">";'

TESTDATA_PRODDESC_WITH_PRODIMG_RAW_WITH_EVERYTHING3 = '"<div id=""gh_proddesc""> Typ: Weitwinkel-Objektiv   Brennweite: 35mm   Lichtst' + \
'ärke: 1:1.4   Optischer Aufbau (Linsen/ Gruppen): 12/ 10   Blendenlamellen: 8 (a' + \
'bgerundet)   Bildstabilisator: nein   Fokussiermotor: nein   Naheinstellgrenze: ' + \
'0.30m   Kleinste Blende: 22   Objektivbajonett: Sony E   Sensorkompatibilität: A' + \
'PS-C   Filterdurchmesser: 77mm   Abmessungen (ØxL): 83x111mm   Gewicht: 660g<p>E' + \
'AN-Codes: 4056572644339, 8809298884703</p> <p>Gelistet seit: 19.12.2013, 14:25</' + \
'p> <p>Es liegen noch keine Bewertungen für dieses Produkt vor (<a onclick=""regi' + \
'sterConversionTag([\'productpage_rating_rate\',\'2\', window.ghPageTypeCM, \'0\'' + \
'])";" rel=nofollow"" href=""bew_1048533.html"">Produkt bewerten</a>).</p> </div>' + \
'";"<img class=""gh_prodImg"" id=""gh_prodImg"" src=""//gzhls.at/i/85/33/1048533-' + \
'n0.jpg"" alt=""Samyang 35mm 1.4 AS UMC für Sony E schwarz"" title=""Samyang 35mm' + \
' 1.4 AS UMC für Sony E schwarz"">";;;;;'

TESTDATA_PRODDESC_WITH_PRODIMG_RAW_WITH_MISSING_INFO1 = \
'<div id=""gh_proddesc""> Typ: Weitwinkel-Objektiv   Brennweite: 35mm   Lichtstärke: 1:1.5   Blendenlamellen: 11   ' + \
'Bildstabilisator: nein   Fokussiermotor: nein   Objektivbajonett: Can' + \
'on EF   Sensorkompatibilität: APS-C/ Kleinbild<p>EAN-Codes: 4549292002669, 4549292002676</p> <p>Gelistet seit: 12.08.2014, ' + \
'14:24</p> <p>Es liegen noch keine Bewertungen für dieses Prod' + \
'ukt vor (<a onclick=""registerConversionTag(['+"'productpage_rating_rate','2', window.ghPageTypeCM, '0'])"+'";" rel=nofollow"" ' + \
'href=""bew_1152662.html"">Produkt bewerten</a>).</p> </div>";"<' + \
'img class=""gh_prodImg"" id=""gh_prodImg"" src=""//gzhls.at/i/26/62/1152662-n0.jpg"" ' + \
'alt=""Canon Objektiv CN-E 35mm T1.5 L F schwarz (9139B001)"" title=""Canon Objektiv CN-E 35mm T1.5 ' + \
'L F schwarz (9139B001)"">";;;;;'

TESTDATA_PRODDESC_WITH_PRODIMG_RAW_WITHOUT_PRODIMG1 = '"<div id=""gh_proddesc""> Typ: Standard-Objektiv   Brennweite: 25mm   Lichtstär' + \
'ke: 1:0.95   Optischer Aufbau (Linsen/ Gruppen): 11/ 8   Blendenlamellen: 10   B' + \
'ildstabilisator: nein   Fokussiermotor: nein   Naheinstellgrenze: 0.17m   Kleins' + \
'te Blende: 16   Objektivbajonett: Micro-Four-Thirds   Sensorkompatibilität: Four' + \
'-Thirds   Filterdurchmesser: 52mm   Abmessungen (ØxL): 58.4x70mm   Gewicht: 410g' + \
'<p>EAN-Codes: 4002451195508, 4002451195539</p> <p>Gelistet seit: 22.02.2011, 10:' + \
'17</p> <p> 1 von 2 Besuchern empfehlen dieses Produkt (<b>50%</b>).<br> <span it' + \
'emprop=\'""aggregateRating""\' itemscope itemtype=\'""http://schema.org/Aggregat' + \
'eRating\'> <meta itemprop=""ratingValue"" content=""4.2f""> <meta itemprop=""rat' + \
'ingCount"" content=""2""> Bewertung: <a onclick=""registerConversionTag([\'produ' + \
'ctpage_rating_stars\',\'2\', window.ghPageTypeCM, \'0\'])";" href=./?sr=616904,-' + \
'1""> <span class=""gh_stars"" title=""4.00 von 5""><span class=""gh_stars1"" sty' + \
'le=""width:80%""></span></span></a> (<span>75%</span>) (<a onclick=""registerCon' + \
'versionTag([\'productpage_rating_read\',\'2\', window.ghPageTypeCM, \'0\'])";" h' + \
'ref=./?sr=616904,-1"" rel=""nofollow""><span>1 </span> Bewertung lesen</a> | <a ' + \
'onclick=""registerConversionTag([\'productpage_rating_rate\',\'2\', window.ghPag' + \
'eTypeCM, \'0\'])";" href=./bew_616904.html"" rel=""nofollow"">Produkt bewerten</' + \
'a>) </span> </p> </div>";;;;'

# TESTDATA_PRODDESC_WITH_PRODIMG_RAW_WITHOUT_PRODIMG2 includes slightly different format in 3rd last row because of the placement of the \'0.
# Has no effect on how it is displayed.
TESTDATA_PRODDESC_WITH_PRODIMG_RAW_WITHOUT_PRODIMG2 = '"<div id=""gh_proddesc""> Typ: Weitwinkel-Objektiv   Brennweite: 28mm   Lichtst' + \
'ärke: 1:2.8   Optischer Aufbau (Linsen/ Gruppen): 8/ 6   Bildstabilisator: nein ' + \
'  Fokussiermotor: nein   Naheinstellgrenze: 0.70m   Kleinste Blende: 22   Abbild' + \
'ungsmaßstab: 1:22.00   Objektivbajonett: Leica M   Sensorkompatibilität: APS-C/ ' + \
'Kleinbild   Filterdurchmesser: 39mm   Abmessungen (ØxL): 52x46mm   Gewicht: 180g' + \
'<p>EAN-Codes: 4022243116061, 4022243116771</p> <p>Gelistet seit: 10.04.2003, 09:' + \
'39</p> <p>Es liegen noch keine Bewertungen für dieses Produkt vor (<a onclick=""' + \
'registerConversionTag([\'productpage_rating_rate\',\'2\', window.ghPageTypeCM, ' + \
'\'0\'])";" rel=nofollow"" href=""bew_51352.html"">Produkt bewerten</a>).</p> </di' + \
'v>";;;;;;'

TESTDATA_PRODDESC_WITH_PRODIMG_RAW_RESPONSE_TWELVE_SIXTY_ENTRY_1 = TESTDATA_PRODDESC_WITH_PRODIMG_RAW_WITH_EVERYTHING1
TESTDATA_RPODSITE_RAW_RESPONSE_TWELVE_SICTY_ENTRY_269 = TESTDATA_PRODDESC_WITH_PRODIMG_RAW_WITHOUT_PRODIMG1
TESTDATA_PRODDESC_WITH_PRODIMG_RAW_RESPONSE_TWELVE_SIXTY_ENTRY_761 = TESTDATA_PRODDESC_WITH_PRODIMG_RAW_WITH_MISSING_INFO1 


#\\\\\\\\\\\\\\\\\\\\\\\\\
#	TESTDATA_TITLE_RAWS
#/////////////////////////

TESTDATA_TITLE_RAW1 = "<title>Nikon AF-S 28mm 1.4E ED schwarz Preisvergleich | Geizhals Deutschland</title>"

#\\\\\\\\\\\\\\\\\\\\\\\\\
#	TESTDATA_TITLE_CLEAR
#/////////////////////////

TESTDATA_TITLE_CLEAR1 = "Nikon AF-S 28mm 1.4E ED schwarz"


def printRowFromFile(file,rowNumber):
	file = str(file)
	if(file == "1"):
		file = 'C:\\Users\\Michael\\IdeaProjects\\NikonLensComparison\\WebCrawler\\rawResponseData 1 - 4.csv'
	elif (file == "2"):
		file = 'C:\\Users\\Michael\\IdeaProjects\\NikonLensComparison\\WebCrawler\\rawResponseData 5 - 7.csv'
	elif(file == "3"):
		file = 'C:\\Users\\Michael\\IdeaProjects\\NikonLensComparison\\WebCrawler\\rawResponseData 8 - 11.csv'
	elif(file == "4"):
		file = 'C:\\Users\\Michael\\IdeaProjects\\NikonLensComparison\\WebCrawler\\rawResponseData 12 - 60.csv'

	openFile = open(file,'r')
	rows = openFile.readlines()
	rowDiff = len(rows) - rowNumber
	if(rowDiff < 0):
		print("Rownumber is " + rowDiff + " too high.")
	else:
		print(rows[rowNumber-1])




if __name__ == "__main__":
	print("Print a certain Row from a certain file with 'printRowFromFile'.")
	print("rowNumber = number")
	print("File = fullpath (incl. filename) or:")
	print("4 = rawResponseData12-60")
	print("You can import the fuction or type here 'file' (as string) and space and rownumber (as numer) or exit here with 'exit'")
	
	userInput = input()
	if(userInput != "exit"):
		file = userInput.split(" ")[0]
		rowNumber = int(userInput.split(" ")[1])
		printRowFromFile(file,rowNumber)
	