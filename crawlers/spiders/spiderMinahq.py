import scrapy
from crawlers.items import TextItem

class LadysComicsSpider(scrapy.Spider):
    name = "MinaHQ"
    start_urls = [
    'https://minadehq.com.br/category/quadrinistas-mulheres-e-nao-binarias/',
    'https://minadehq.com.br/category/newsletter/',
    'https://minadehq.com.br/category/quadrinhos-exclusivos/',
    'https://minadehq.com.br/category/dicas-e-resenhas-de-quadrinhos/',
    'https://minadehq.com.br/category/noticias/',
    ]

    def parse(self, response):
        print(response)
        for href in response.xpath('//div[has-class("paginator")]//a[has-class("nav-next")]/@href').getall():
            print(href)
            url = response.urljoin(href)
            yield scrapy.Request(url, callback=self.parse, dont_filter=True)

        for href in response.xpath('//h3[has-class("entry-title")]//a/@href').getall():
            print(href)
            url = response.urljoin(href)
            yield scrapy.Request(url, callback=self.parse_dir_contents, dont_filter=True)

    def parse_dir_contents(self, response):
        print(response)
        item = TextItem()
        item['title'] = response.xpath('//div[has-class("titulo-olho")]/h2/text()').extract()
        item['author'] = response.xpath('//a[has-class("author vcard")]/span/text()').extract()
        item['date'] = response.xpath('//a/time[has-class("entry-date")]/text()').extract()
        item['body'] = [ ' '.join(
            line.strip() 
            for line in p.xpath('.//text()').extract() 
            if line.strip())    
            for p in response.xpath('//div[has-class("wpb_wrapper")]//p')
            ]
        if(response.xpath('//img').getall() != ''):
            item['hasImage'] = True
        else:
             item['hasImage'] = False

        item['category'] = response.xpath('//span[has-class("category-link")]/a/text()').extract()
        yield item
