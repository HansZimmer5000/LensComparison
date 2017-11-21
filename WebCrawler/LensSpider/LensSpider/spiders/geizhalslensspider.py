import scrapy
from .. import items
from ..itemloader import GeizhalsItemloader

#Start with: "scrapy crawl " + Spidername (name Attribute)
def get_attribute_value(key,string,valueTillKey):
    key_length = len(key)
    key_start_pos = string.find(key)

    if(key_start_pos >= 0):
        value_start_pos = key_start_pos + key_length
        raw_value = string[value_start_pos:]
        value_end_pos = raw_value.find(valueTillKey)
        value = raw_value[:value_end_pos]
        result = value
    else:
        result = ""

    return result


class GeizhalsLensSpider(scrapy.Spider):
    
    name = 'GeizhalsLensSpider' 
    start_urls = ['https://geizhals.de/?cat=acamobjo&amp;pg=1']
    crawled_lenses = {}

    custom_settings = {
        'DOWNLOAD_DELAY': 7
    }

    def parse_lens_page(self, response):
        loader = GeizhalsItemloader()
        proddesc = response.xpath('//div[@id="gh_proddesc"]').extract_first()
        title = response.xpath('//title').extract_first()
        loader.populate_from_proddesc_and_title(proddesc, title)
        yield loader.get_item()

    def create_lens_page_requests(self, response):        
        for lens_page in response.xpath('//a[@class = "productlist__link"]'):
            yield response.follow(lens_page, self.parse_lens_page)

    def create_overview_page_request(self, response):
        next_page_raw_url = response.xpath('//a[@class = "gh_pag_i only--desktop gh_pag_i_last gh_pag_next_active"]').extract_first()[3:80]
        tmpResult = get_attribute_value('href="',next_page_raw_url,'"')
        next_page_url = tmpResult.replace(".","https://geizhals.de",1)

        if next_page_url is not None:
            yield scrapy.Request(next_page_url, callback=self.parse_overview_page)

    def parse_overview_page(self, response):
        for lens_page_request in self.create_lens_page_requests(response):
            yield lens_page_request

        for overview_page_request in self.create_overview_page_request(response):
            yield overview_page_request

    def parse(self, response):
        return self.parse_overview_page(response)


