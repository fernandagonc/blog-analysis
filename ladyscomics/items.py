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