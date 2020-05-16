import scrapy
import calendar
import time
from ..items import CodechefItem

class CodechefSpider(scrapy.Spider):
    name = 'codechef'
    start_urls = [
        'https://www.codechef.com/users/codernavi18'
    ]

    def parse(self, response):
        items = CodechefItem()

        items['rating'] = response.xpath('//div[@class="rating-number"]/text()').get()
        items['best_rating'] = response.xpath('//div[@class="rating-header text-center"]//small[1]/text()').get().strip('()').split()[-1]
        items['global_rank'] = response.xpath('(//ul[@class="inline-list"]//strong)[1]/text()').get()
        items['country_rank'] = response.xpath('(//ul[@class="inline-list"]//strong)[2]/text()').get()
        items['last_updated'] = calendar.timegm(time.gmtime())
        items['last_activity'] = 0
        yield items
