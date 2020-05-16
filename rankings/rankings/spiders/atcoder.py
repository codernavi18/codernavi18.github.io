import scrapy
import calendar
import time
import unidecode
from ..items import AtcoderItem

class AtcoderSpider(scrapy.Spider):
    name = 'atcoder'
    start_urls = [
        'https://atcoder.jp/users/codernavi18'
    ]

    def parse(self, response):
        items = AtcoderItem()
        items['rank'] = response.xpath('//th[text()="Rank"]/following-sibling::td/text()').get()
        if items['rank'] is None:
            items['rating'] = "0"
            items['best_rating'] = "0"
            items['contests_participated'] = "0"
            items['last_activity'] = "0"
        else:
            items['rating'] = response.xpath('//th[text()="Rating"]/following-sibling::td/span[1]/text()').get()
            items['best_rating'] = response.xpath('//th[text()="Highest Rating"]/following-sibling::td/span[1]/text()').get()
            items['contests_participated'] = response.xpath('//th[contains(.,"Rated Matches")]/following-sibling::td/text()').get()
            items['last_activity'] = response.xpath('//th[contains(.,"Last Competed")]/following-sibling::td/text()').get()
        items['last_updated'] = calendar.timegm(time.gmtime())
        yield items
