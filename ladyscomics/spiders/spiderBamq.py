import scrapy
from ladyscomics.items import BamqItem

class LadysComicsSpider(scrapy.Spider):
    name = "LadysBamq"
    start_urls = [
            'http://ladyscomics.com.br/bamq',
                ]
 
    def parse(self, response):
        print(response)
        for href in response.xpath('//div[has-class("pagination")]//a[has-class("nextpage")]/@href').getall():
            print(href)
            url = response.urljoin(href)
            yield scrapy.Request(url, callback=self.parse_dir_contents, dont_filter=True)
            
        self.parse_dir_contents(response)


   
    def parse_dir_contents(self, response):
        table = response.xpath('//table//tbody').extract()
        rows = table.xpath('//tr')
        for row in rows:
            item = BamqItem()
            item['author'] = row.xpath('td[0]//text()').extract_first()
            item['signature'] = row.xpath('td[1]//text()').extract_first()
            item['city'] = row.xpath('td[2]//text()').extract_first()
            item['state'] = row.xpath('td[3]//text()').extract_first()
            item['role'] = row.xpath('td[4]//text()').extract_first()
            print(item)
            yield item