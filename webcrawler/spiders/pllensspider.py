
from webcrawler.spiders.baselensspider import BaseLensSpider
from webcrawler.spiders import spiderpladapter

class PlLensSpider(BaseLensSpider):

    name = "PlLensSpider"
    start_urls = [spiderpladapter.START_URL]
    custom_settings = {
        'ITEM_PIPELINES' : {
            'webcrawler.itempipelines.plitempipeline.PlItemPipeline': 300
        }
    }

    @property
    def adapter(self):
        return spiderpladapter

    def create_lens_page_requests(self, response):
        pass

    def create_overview_page_request(self, response):
        pass

