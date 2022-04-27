import scrapy
from crawlers.items import MinaHQItem

class LadysComicsSpider(scrapy.Spider):
    name = "MinaHQ"
    start_urls = ['https://minadehq.com.br/category/quadrinistas-mulheres-e-nao-binarias/',]

    def parse(self, response):
        print(response)
        for href in response.xpath('').getall():
            print(href)
            url = response.urljoin(href)
            yield scrapy.Request(url, callback=self.parse, dont_filter=True)

        for href in response.xpath('').getall():
            print(href)
            url = response.urljoin(href)
            yield scrapy.Request(url, callback=self.parse_dir_contents, dont_filter=True)

    def parse_dir_contents(self, response):
        item = MinaHQItem()