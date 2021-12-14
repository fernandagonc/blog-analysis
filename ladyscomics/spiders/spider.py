import scrapy
from ladyscomics.items import LadyscomicsItem

class LadysComicsSpider(scrapy.Spider):
    name = "LadysComics"
    start_urls = [
            'http://ladyscomics.com.br/',
                ]
 
    def parse(self, response):
        print(response)
        for href in response.xpath('//div[has-class("nav-previous")]//a/@href').getall():
            print(href)
            url = response.urljoin(href)
            yield scrapy.Request(url, callback=self.parse, dont_filter=True)
            
        for href in response.xpath('//a[has-class("button-primary")]/@href').getall():
            print(href)
            url = response.urljoin(href)
            yield scrapy.Request(url, callback=self.parse_dir_contents, dont_filter=True)

   
    def parse_dir_contents(self, response):
        item = LadyscomicsItem()
        item['title'] = response.xpath('//h1[has-class("entry-title")]/text()').extract()
        item['author'] = response.xpath('//a[has-class("author")]/text()').extract()
        item['date'] = response.xpath('//a[has-class("entry-date")]/text()').extract_first()
        item['body'] = [ ' '.join(
            line.strip() 
            for line in p.xpath('.//text()').extract() 
            if line.strip())    
            for p in response.xpath('//div[has-class("entry-content")]//p')
            ]
        item['comments'] = [ ' '.join(
            line.strip() 
            for line in p.xpath('.//text()').extract() 
            if line.strip())    
            for p in response.xpath('//div[has-class("comments-area")]//ol//p')
            ]
        

        if(response.xpath('//img').getall() != ''):
            item['hasImage'] = True
        else:
             item['hasImage'] = False
        yield item