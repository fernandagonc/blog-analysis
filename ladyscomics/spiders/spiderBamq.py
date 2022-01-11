import scrapy
from ladyscomics.items import BamqItem

class LadysComicsSpider(scrapy.Spider):
    name = "LadysBamq"
    start_urls = [
            'http://ladyscomics.com.br/bamq',
                ]
 
    def parse(self, response):  
        for href in response.xpath('//div[has-class("pagination")]//a/@href').getall():
            print(href)
            url = response.urljoin(href)
            yield scrapy.Request(url, callback=self.parse_dir_contents, dont_filter=True)

        yield scrapy.Request('http://ladyscomics.com.br/bamq', callback=self.parse_dir_contents, dont_filter=True)
      
            
#  https://www.simplified.guide/scrapy/scrape-table  
    def parse_dir_contents(self, response):
        for row in response.xpath('//table//tbody//tr'):
            item = BamqItem()
            item['author'] = row.xpath('td[1]//a/text()').extract_first()
            item['signature'] = row.xpath('td[2]//text()').extract_first()
            item['city'] = row.xpath('td[3]//text()').extract_first()
            item['state'] = row.xpath('td[4]//text()').extract_first()
            item['role'] = row.xpath('td[5]//text()').extract_first()
            print(item)
            yield item