# This module is about my webcrawler with the use of scrapy.
# Its a generell web crawler, but the import and use of GhAdapter makes it usefull for geizhals.de sites.

# TODO: Make it fully general / adaptable, so its not limited to one site.
# TODO: Split every thing up, functions, the class and other executable code.

import scrapy
import time
import GhAdapter
import RawData

if __name__ == "__main__":
	print("Works only in combination with scrapy\nUsage: 'scrapy runspider Spider.py'")

class BlogSpider(scrapy.Spider):
	__SAVE_FULL_LENS_PAGE_ONLY = True
	__SAVE_RAW_WITHOUT_TRANSFORMING = False

	__SLEEP_SECONDS_BETWEEN_LENSE_PAGES = 10
	__SLEEP_SECONDS_BETWEEN_OVERVIEW_PAGES = 10

	name = 'lensSpider' 
	start_urls = ['https://geizhals.de/?cat=acamobjo&amp;pg=1']

	# TODO: Following line will be executed even whenits just importat
	RawData.clean_rawdata_file_and_write_titles()

	def parseLensPage(self, response):
		if(self.__SAVE_FULL_LENS_PAGE_ONLY):
			#print(response.body_as_unicode())
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

	def parse(self, response):
		print("parsing!")
		for lens_page in response.xpath('//a[@class = "productlist__link"]'):
			time.sleep(self.__SLEEP_SECONDS_BETWEEN_LENSE_PAGES) 
			yield response.follow(lens_page, self.parseLensPage)

		time.sleep(self.__SLEEP_SECONDS_BETWEEN_OVERVIEW_PAGES) 

		next_page_raw_url = response.xpath('//a[@class = "gh_pag_i only--desktop gh_pag_i_last gh_pag_next_active"]').extract_first()[3:80]
		print("next_page_raw_url: " + next_page_raw_url)
		next_page_url = GhAdapter.create_next_gh_overview_page(next_page_raw_url)
		print("next_page_url: " + next_page_url)
		if next_page_url is not None:
			yield scrapy.Request(next_page_url, callback=self.parse)

	
