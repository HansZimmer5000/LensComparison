# Start the LensSpider and let it crawl.
# start_urls and name is set in LensSpider class.

#from webcrawler.spiders.lensspider import LensSpider
from webcrawler.spiders.ghlensspider import GhLensSpider
from webcrawler.spiders.pllensspider import PlLensSpider
from webcrawler.spiders import spiderghadapter
from scrapy.crawler import CrawlerProcess

def start_spider_within_python():
    custom_settings = {
        'CONCURRENT_REQUESTS_PER_DOMAIN': 1,
        'CONCURRENT_REQUESTS_PER_IP': 0, #If this >0 then CONCURRENT_REQUESTS_PER_DOMAIN would be ignored 
        
        'DOWNLOAD_DELAY': 7,
		'RANDOMIZE_DOWNLOAD_DELAY': False, #from 0.5*DELAY till 1.5*DELAY
		'COOKIES_ENABLED': False
    }
    
    process = CrawlerProcess(custom_settings)
    process.crawl(GhLensSpider)
    #process.crawl(PlLensSpider)
    process.start() 

if __name__ == "__main__":
	start_spider_within_python()

