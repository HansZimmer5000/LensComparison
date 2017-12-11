
from webcrawler.spiders.baselensspider import BaseLensSpider
from webcrawler.spiders import spiderghadapter

class GhLensSpider(BaseLensSpider):

    name = "GhLensSpider"
    start_urls = [spiderghadapter.START_URL]
    custom_settings = {
        'ITEM_PIPELINES' : {
            'webcrawler.itempipelines.ghitempipeline.GhItemPipeline': 300
        }
    }

    @property
    def adapter(self):
        return spiderghadapter

