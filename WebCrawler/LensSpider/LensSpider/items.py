# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class QuoteItem(scrapy.Item):
    text = scrapy.Field()
    author = scrapy.Field()
    tags = scrapy.Field()


class LensItem(scrapy.Item):
    lensname = scrapy.Field()
    focal_length = scrapy.Field()
    aperture = scrapy.Field()
    filter = scrapy.Field()
    magnification = scrapy.Field()
    minimalfocus = scrapy.Field()
    mount = scrapy.Field()
    sensor_compatibility = scrapy.Field()
    weight = scrapy.Field()
    size = scrapy.Field()
