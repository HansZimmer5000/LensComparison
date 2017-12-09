# Start the LensSpider and let it crawl.
# start_urls and name is set in LensSpider class.

from LensSpider import LensSpider
from scrapy.crawler import CrawlerProcess

def start_spider_within_python():
    custom_settings = {
        'CONCURRENT_REQUESTS_PER_DOMAIN': 1,
        'CONCURRENT_REQUESTS_PER_IP': 0, #If this >0 then CONCURRENT_REQUESTS_PER_DOMAIN would be ignored 
        
        'DOWNLOAD_DELAY': 7,
		'RANDOMIZE_DOWNLOAD_DELAY': False, #from 0.5*DELAY till 1.5*DELAY
		'COOKIES_ENABLED': False,

        'DEFAULT_TIME_CLASS': "Lens",

        'ITEM_PIPELINES': {
            'ghitempipeline.GhItemPipeline': 300
        }
    }
    
    process = CrawlerProcess(custom_settings)
    process.crawl(LensSpider)
    #process.crawls(OtherSpiderClass)
    #process.crawl(SomeSpider, start_urls=["http://www.example.com"]) Needed for upcoming changed in code
    process.start() 

if __name__ == "__main__":
	start_spider_within_python()

