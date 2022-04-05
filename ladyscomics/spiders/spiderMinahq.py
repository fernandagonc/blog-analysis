import scrapy


class MinahqSpider(scrapy.Spider):
    name = 'MinaHQ'
    start_urls = ['http://minadehq.com/']

    def parse(self, response):
        pass
