# This module is about my webcrawler with the use of scrapy.
# Its a generell web crawler, but the import and use of GhAdapter makes it usefull for geizhals.de sites.

from LensSpider import LensSpider
from scrapy.crawler import CrawlerProcess
import RawData

def start_spider_within_python():
    custom_settings = {
        'DOWNLOAD_DELAY': 7,
		'RANDOMIZE_DOWNLOAD_DELAY': False, #from 0.5*DELAY till 1.5*DELAY
		'COOKIES_ENABLED': False
    }
    process = CrawlerProcess(custom_settings)
    process.crawl(LensSpider)
    process.start() 

if __name__ == "__main__":
	RawData.clean_rawdata_file_and_write_titles()
	start_spider_within_python()