# This module is about my webcrawler with the use of scrapy.
# Its a generell web crawler, but the import and use of GhAdapter makes it usefull for geizhals.de sites.

import scrapy
import GhAdapter
import RawData
import os

class LensSpider(scrapy.Spider):
	__RUN_WITHOUT_SAVING = False
	__SAVE_FULL_LENS_PAGE_ONLY = False
	__SAVE_RAW_WITHOUT_TRANSFORMING = False

	name = 'lensSpider' 
	start_urls = [GhAdapter.START_URL]

	def parse_lens_page(self, response):
		#TODO: Create functionalitiy to prove if some lens already is recorded, then add Mount / fill up missing data / ignore it.
		if(self.__RUN_WITHOUT_SAVING):
			pass
		else:
			if(self.__SAVE_FULL_LENS_PAGE_ONLY):
				RawData.append_raw_lens_page_to_rawdata(response.body_as_unicode())
			else:
				raw_lens_info = response.xpath(GhAdapter.LENS_INFO_TAG).extract_first()
				raw_lens_name = response.xpath(GhAdapter.LENS_NAME_TAG).extract_first() 

				if(self.__SAVE_RAW_WITHOUT_TRANSFORMING):
					RawData.append_raw_desc_raw_lens_name_to_rawdata(raw_lens_info,raw_lens_name)
				else:
					clean_lens_info = RawData.clear_string(raw_lens_info)
					clean_lens_name = RawData.clear_string(raw_lens_name)
					RawData.append_clean_lensdata_dict_to_rawdata(GhAdapter.get_all_attributes(clean_lens_info,clean_lens_name))

	def create_lens_page_requests(self,response):
		response_url = response.urljoin("")
		link_tag = "" 
		#TODO: Make extra Function for that + own UrlNotKnownError Exception?

		if("geizhals" in response_url):
			link_tag = GhAdapter.LINK_TAG_TO_LENS_IN_OVERVIEW_PAGE
		else:
			print("create_lens_page_requests: response URL not familiar to any known site!")

		if(link_tag != ""):
			for lens_page in response.xpath(link_tag):
				yield response.follow(lens_page, self.parse_lens_page)

	def create_overview_page_request(self, response):
		response_url = response.urljoin("")
		next_page_url = None 
		#TODO: Make extra Function for that + own UrlNotKnownError Exception?

		if("geizhals" in response_url):
			next_page_raw_url = response.xpath(GhAdapter.LINK_TAG_TO_NEXT_OVERVIEW_PAGE_IN_OVERVIEW_PAGE).extract_first()[3:80]
			next_page_url = GhAdapter.create_next_gh_overview_page(next_page_raw_url)
		else:
			print("create_lens_page_requests: response URL not familiar to any known site!")

		if next_page_url is not None:
			yield scrapy.Request(next_page_url, callback=self.parse_overview_page)

	def parse_overview_page(self,response):
		for lens_page_request in self.create_lens_page_requests(response):
			yield lens_page_request

		for overview_page_request in self.create_overview_page_request(response):
			yield overview_page_request

	def parse(self, response):
		print("Started Parsing!")
		return self.parse_overview_page(response)