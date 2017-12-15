# This module is about my webcrawler with the use of scrapy.
# Its a generell web crawler, but the import and use of GhAdapter makes it usefull for geizhals.de sites.

import scrapy
from abc import ABC, abstractmethod

class BaseLensSpider(scrapy.Spider, ABC):

	@property
	@abstractmethod
	def adapter(self):
		raise NotImplementedError()

	

	@abstractmethod
	def parse_lens_page(self, response):
		raise NotImplementedError()

	@abstractmethod
	def create_lens_page_requests(self,response):
		raise NotImplementedError()

	@abstractmethod
	def create_overview_page_request(self, response):
		raise NotImplementedError()

	def parse_overview_page(self,response):
		for lens_page_request in self.create_lens_page_requests(response):
			yield lens_page_request

		for overview_page_request in self.create_overview_page_request(response):
			yield overview_page_request

	def parse(self, response):
		return self.parse_overview_page(response)
