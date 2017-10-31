# This module is about my webcrawler with the use of scrapy.
# Its a generell web crawler, but the import and use of GhAdapter makes it usefull for geizhals.de sites.

# TODO: Make it fully general / adaptable, so its not limited to one site.
# TODO: Split every thing up, functions, the class and other executable code.

import scrapy
from scrapy.crawler import CrawlerProcess
import time
import GhAdapter
import RawData
import os

class BlogSpider(scrapy.Spider):
	__SAVE_FULL_LENS_PAGE_ONLY = False
	__SAVE_RAW_WITHOUT_TRANSFORMING = False
	__DELAY_SECONDS_BETWEEN_DOWNLOADS = '10'

	name = 'lensSpider' 
	start_urls = [GhAdapter.START_URL]
	custom_settings = {
        'DOWNLOAD_DELAY': __DELAY_SECONDS_BETWEEN_DOWNLOADS
    }

	def parse_lens_page(self, response):
		if(self.__SAVE_FULL_LENS_PAGE_ONLY):
			RawData.append_raw_lens_page_to_rawdata(response.body_as_unicode())
		else:
			gh_proddesc = response.xpath('//div[@id="gh_proddesc"]').extract_first()
			raw_lensname = response.xpath('//title').extract_first() 

			if(self.__SAVE_RAW_WITHOUT_TRANSFORMING):
				RawData.append_raw_desc_raw_lensname_to_rawdata(gh_proddesc,raw_lensname)
			else:
				clean_gh_proddesc = RawData.clear_string(gh_proddesc)
				clean_lensname = RawData.clear_string(raw_lensname)
				RawData.append_clean_lensdata_dict_to_rawdata(GhAdapter.get_all_attributes(clean_gh_proddesc,clean_lensname))

	def parse_overview_page(self,response):
		for lens_page in response.xpath('//a[@class = "productlist__link"]'):
			yield response.follow(lens_page, self.parse_lens_page)

		next_page_raw_url = response.xpath('//a[@class = "gh_pag_i only--desktop gh_pag_i_last gh_pag_next_active"]').extract_first()[3:80]
		next_page_url = GhAdapter.create_next_gh_overview_page(next_page_raw_url)
		if next_page_url is not None:
			yield scrapy.Request(next_page_url, callback=self.parse_overview_page)

	def parse(self, response):
		print("Started Parsing!")
		return self.parse_overview_page(response)

def start_spider_within_python():
	process = CrawlerProcess({})
	process.crawl(BlogSpider)
	process.start() 

if __name__ == "__main__":
	RawData.clean_rawdata_file_and_write_titles()
	start_spider_within_python()