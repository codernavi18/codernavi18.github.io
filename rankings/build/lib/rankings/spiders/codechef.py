import scrapy
from ..items import CodechefItem

class CodechefSpider(scrapy.Spider):
    name = 'codechef'
    start_urls = [
        'https://www.codechef.com/users/errichto'
    ]

    def parse(self, response):
        items = CodechefItem()

        rating = response.css('.rating::text').extract()
        items['rating'] = rating
        yield items
