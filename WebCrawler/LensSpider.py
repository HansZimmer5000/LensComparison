# This module is about my webcrawler with the use of scrapy.
# Its a generell web crawler, but the import and use of GhAdapter makes it usefull for geizhals.de sites.

import scrapy
import GhAdapter
import DataKeys
import RawDataAccess
import datetime
import os
from CrawledLenses import CrawledLenses

class LensSpider(scrapy.Spider):
	__RUN_WITHOUT_SAVING = False
	__SAVE_FULL_LENS_PAGE_ONLY = False
	__SAVE_RAW_WITHOUT_TRANSFORMING = False
	__SAVE_TRANSFORMED_AND_UNIQUE_LENSES_TO_MONGODB = True

	name = 'lensSpider' 
	start_urls = [GhAdapter.START_URL]

	crawled_lenses = CrawledLenses("geizhals_lens_coll")

	def parse_lens_page(self, response):
		if(self.__RUN_WITHOUT_SAVING):
			pass
		else:
			if(self.__SAVE_FULL_LENS_PAGE_ONLY):
				RawDataAccess.append_raw_lens_page_to_rawdata(response.body_as_unicode())
			else:
				raw_lens_info = response.xpath(GhAdapter.LENS_INFO_TAG).extract_first()
				raw_lens_name = response.xpath(GhAdapter.LENS_NAME_TAG).extract_first() 

				if(self.__SAVE_RAW_WITHOUT_TRANSFORMING):
					RawDataAccess.append_raw_desc_raw_lens_name_to_rawdata(raw_lens_info,raw_lens_name)
				else:
					clean_lens_info = RawDataAccess.clear_string(raw_lens_info)
					clean_lens_name = RawDataAccess.clear_string(raw_lens_name)
					new_gh_lens_dict = GhAdapter.get_all_attributes(clean_lens_info,clean_lens_name)
					new_lens_dict = self.__create_lens_dict_from_gh_lens_dict(new_gh_lens_dict)
					if(self.__SAVE_TRANSFORMED_AND_UNIQUE_LENSES_TO_MONGODB):
						self.crawled_lenses.new_lens_dict(new_lens_dict)
					else:
						RawDataAccess.append_clean_lensdata_dict_to_rawdata(new_lens_dict)

	def create_lens_page_requests(self,response):
		response_url = response.urljoin("")
		link_tag = "" 

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
		return self.parse_overview_page(response)

	def __create_lens_dict_from_gh_lens_dict(self, gh_lens_dict):
		new_lens_dict = {}
		for key_as_title in DataKeys.gh_keys_dict:
			key_as_gh = DataKeys.gh_keys_dict[key_as_title]
			gh_value = gh_lens_dict[key_as_gh]
			new_lens_dict.update({key_as_title: gh_value})
		return new_lens_dict
