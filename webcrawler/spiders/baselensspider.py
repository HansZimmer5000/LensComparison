# This module is about my webcrawler with the use of scrapy.
# Its a generell web crawler, but the import and use of GhAdapter makes it usefull for geizhals.de sites.

import scrapy
from abc import ABC, abstractmethod

class BaseLensSpider(scrapy.Spider, ABC):

	@property
	@abstractmethod
	def adapter(self):
		raise NotImplementedError()


	def parse_lens_page(self, response):
		raw_lens_info = response.xpath(self.adapter.LENS_INFO_TAG).extract_first()
		raw_lens_name = response.xpath(self.adapter.LENS_NAME_TAG).extract_first() 

		yield {
			"name": raw_lens_name,
			"info": raw_lens_info
		}

	def create_lens_page_requests(self,response):
		link_tag = self.adapter.LINK_TAG_TO_LENS_IN_OVERVIEW_PAGE
		for lens_page in response.xpath(link_tag):
			yield response.follow(lens_page, self.parse_lens_page)

	def create_overview_page_request(self, response):
		next_page_raw_url = response.xpath(self.adapter.LINK_TAG_TO_NEXT_OVERVIEW_PAGE_IN_OVERVIEW_PAGE).extract_first()[3:80]
		next_page_url = self.adapter.create_next_gh_overview_page(next_page_raw_url)
		yield scrapy.Request(next_page_url, callback=self.parse_overview_page)

	def parse_overview_page(self,response):
		for lens_page_request in self.create_lens_page_requests(response):
			yield lens_page_request

		for overview_page_request in self.create_overview_page_request(response):
			yield overview_page_request

	def parse(self, response):
		return self.parse_overview_page(response)
