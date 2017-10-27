# This module is about my webcrawler with the use of scrapy.
# Its a generell web crawler, but the import and use of GhAdapter makes it usefull for geizhals.de sites.

# TODO: Make it fully general / adaptable, so its not limited to one site.
# TODO: Split every thing up, functions, the class and other executable code.

import scrapy
import time
import GhAdapter
import RawData

class BlogSpider(scrapy.Spider):
	__SPIDER_NAME = 'lensSpider' #run with "scrapy runspider Spider.py"
	__SAVE_RAW_WITHOUT_TRANSFORMING = True

	start_urls = ['https://geizhals.de/?cat=acamobjo&amp;pg=1']

	RawData.clean_rawdata_file_and_write_titles()

	def parseLensPage(self, response):
		gh_proddesc = response.xpath('//div[@id="gh_proddesc"]').extract_first()
		gh_prodImg = response.xpath('//img[@class="gh_prodImg"]').extract_first()
		title = response.xpath('//title').extract_first() #-> <title>Sony E PZ 18-105mm 4.0 G OSS schwarz Preisvergleich | Geizhals Deutschland</title>
		
		if(self.__SAVE_RAW_WITHOUT_TRANSFORMING):
			#RawData.appendRawDescImgData(gh_proddesc,gh_prodImg)
			RawData.append_raw_desc_title_to_rawdata(gh_proddesc,title)
		else:
			RawData.append_lensdata_dict_to_rawdata(GhAdapter.getAllAttributes(gh_proddesc,gh_prodImg))
	def parse(self, response):
		print("parsing!")
		for lens_page in response.xpath('//a[@class = "productlist__link"]'):
			time.sleep(10) # sekunden schlafen
			yield response.follow(lens_page, self.parseLensPage)

		time.sleep(10) # Sekunden schlafen

		next_page_raw_url = response.xpath('//a[@class = "gh_pag_i only--desktop gh_pag_i_last gh_pag_next_active"]').extract_first()[3:80]
		next_page_url = GhAdapter.create_next_gh_overview_page(next_page_raw_url)
		if next_page_url is not None:
			yield scrapy.Request(next_page_url, callback=self.parse)

	
