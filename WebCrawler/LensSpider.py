# This module is about my webcrawler with the use of scrapy.
# Its a generell web crawler, but the import and use of GhAdapter makes it usefull for geizhals.de sites.

import scrapy
import GhAdapter
import datetime
import os
from CrawledLenses import CrawledLenses

class LensSpider(scrapy.Spider):

	name = 'lensSpider' 
	start_urls = [GhAdapter.START_URL]

	crawled_lenses = CrawledLenses("lens_db","geizhals_lens_coll")

	def parse_lens_page(self, response):
		raw_lens_info = response.xpath(GhAdapter.LENS_INFO_TAG).extract_first()
		raw_lens_name = response.xpath(GhAdapter.LENS_NAME_TAG).extract_first() 

		clean_lens_info = GhAdapter.clear_string(raw_lens_info)
		clean_lens_name = GhAdapter.clear_string(raw_lens_name)

		new_gh_lens_dict = GhAdapter.get_all_attributes(clean_lens_info,clean_lens_name)
		new_lens_dict = GhAdapter.transform_gh_dict_to_general_dict(new_gh_lens_dict)
		
		self.crawled_lenses.new_lens_dict(new_lens_dict)

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
