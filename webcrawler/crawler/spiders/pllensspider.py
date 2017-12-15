
from webcrawler.crawler.spiders.baselensspider import BaseLensSpider
from webcrawler.crawler.adapter import pladapter

class PlLensSpider(BaseLensSpider):

    name = "PlLensSpider"
    start_urls = [pladapter.START_URL]
    custom_settings = {
        'ITEM_PIPELINES' : {
            'webcrawler.crawler.itempipelines.plitempipeline.PlItemPipeline': 300
        }
    }

    @property
    def adapter(self):
        return pladapter

    def parse_lens_page(self, response):
        raw_name = response.xpath("//h3").extract_first()
        raw_data = response.xpath("//table").extract_first()
        yield {
            "name": raw_name,
            "data": raw_data
        }


    def create_lens_page_requests(self, response):
        for lens_page in self.adapter.get_list_of_lenses_from_ov_page(response):
            yield response.follow(lens_page, self.parse_lens_page)

    def create_overview_page_request(self, response):
        next_overview_page = self.adapter.get_next_overview_page(response)
        yield response.follow(next_overview_page, self.parse_overview_page)

