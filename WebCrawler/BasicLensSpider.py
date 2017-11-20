import requests
import datetime


from lxml import html
from lxml import etree
import requests

site = "https://geizhals.de/nikon-af-p-vr-dx-18-55mm-3-5-5-6g-schwarz-jaa826da-a1375455.html?hloc=at&hloc=de&hloc=pl&hloc=uk&hloc=eu"
content = requests.get(site).content


tree = html.fromstring(content)
title = tree.xpath('//title')
proddesc = tree.xpath('//div[@id="gh_proddesc"]')


import http.client

body = http.client.HTTPSResponse(site).request("GET", "/").getresponse().read()
print(body)

#scrapy crawl MySpider -s CONCURRENT_REQUESTS_PER_DOMAIN=1000 -s CONCURRENT_REQUESTS=30