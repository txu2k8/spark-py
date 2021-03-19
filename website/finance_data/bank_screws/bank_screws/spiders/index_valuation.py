import scrapy


class IndexValuationSpider(scrapy.Spider):
    name = 'index_valuation'
    allowed_domains = ['https://www.wxnmh.com/user-12490-2.htm']
    start_urls = ['http://https://www.wxnmh.com/user-12490-2.htm/']

    def parse(self, response):
        pass
