# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class Wxcj01Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class SinafiItem(scrapy.Item):
    title = scrapy.Field()
    date = scrapy.Field()
    source = scrapy.Field()
    content = scrapy.Field()
    keywords = scrapy.Field()
    des = scrapy.Field()
