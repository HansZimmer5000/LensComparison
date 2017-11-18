import requests
import datetime


from lxml import html
import urllib3

time = datetime.datetime.now()
content = urllib3.poolmanager.parse_url('https://geizhals.de/nikon-af-p-vr-dx-10-20mm-4-5-5-6g-schwarz-jaa832da-a1631964.html?hloc=at&hloc=de&hloc=pl&hloc=uk&hloc=eu')
#<title>Nik....Deutschland</title>
print("urlib3 GetPage: " + str(datetime.datetime.now() - time))


time = datetime.datetime.now()
response = requests.get("https://geizhals.de/nikon-af-p-vr-dx-10-20mm-4-5-5-6g-schwarz-jaa832da-a1631964.html?hloc=at&hloc=de&hloc=pl&hloc=uk&hloc=eu")
#<title>Nik....Deutschland</title>
#<div id="gh_proddesc">.... </div>

content = str(response.content)
print("Basic GetPage: " + str(datetime.datetime.now() - time))

index_title = content.find("<title>")
index_title_end = content.find("</title>")
title = content[index_title:index_title_end]

time = datetime.datetime.now()
index_proddesc = content.find('<div id="gh_proddesc">')
content_from_proddesc_on = content[index_proddesc:]
index_title_end = content_from_proddesc_on.find("</div>")
proddesc = content_from_proddesc_on[:index_title_end]
print("Basic scraping: " + str(datetime.datetime.now() - time))

from scrapy.selector import Selector
from scrapy.http import HtmlResponse

time = datetime.datetime.now()
title = Selector(text=content).xpath('//title').extract_first()
proddesc = Selector(text=content).xpath('//div[@id="gh_proddesc"]').extract_first()
print("Scrapy scraping: " + str(datetime.datetime.now() - time))


time = datetime.datetime.now()
tree = html.fromstring(content)
title = tree.xpath('//title')
proddesc = tree.xpath('//div[@id="gh_proddesc"]')
print("lxml GetPage: " + str(datetime.datetime.now() - time))

from lxml import etree as ET

#print(ET.tostring(tree,pretty_print=True))
print(title)
print(proddesc)