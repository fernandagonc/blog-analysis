# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class LadyscomicsItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    author = scrapy.Field()
    date = scrapy.Field()
    body = scrapy.Field()
    hasImage = scrapy.Field()
    comments =  scrapy.Field()
    category = scrapy.Field()

class BamqItem(scrapy.Item):
    # define the fields for your item here like:
    author = scrapy.Field()
    signature = scrapy.Field()
    city = scrapy.Field()
    state = scrapy.Field()
    role =  scrapy.Field()

class MinaHQItem(scrapy.Item):
    test = scrapy.Field()