import scrapy
import calendar
import time
import unidecode
from ..items import LeetcodeItem

class LeetcodeSpider(scrapy.Spider):
    name = 'leetcode'
    start_urls = [
        'https://leetcode.com/codernavi18/'
    ]

    def parse(self, response):
        items = LeetcodeItem()
        items['contests_participated'] = response.xpath('(//h3[contains(., "Contest")])[1]/../../ul/li[1]/span/text()').get().strip('\n ')
        if items['contests_participated'] != "0":
            items['rating'] =  response.xpath('(//h3[contains(., "Contest")])[1]/../../ul/li[2]/span/text()').get().strip('\n ')
            items['global_rank'] = response.xpath('(//h3[contains(., "Contest")])[1]/../../ul/li[3]/span/text()').get().strip("\n ")
        else:
            items['rating'] = 0
            items['global_rank'] = 0
        last_activity=response.xpath('(//h3[contains(., "Most recent submissions")]/../../ul/a)[1]/span[3]/text()').get()
        items['last_activity'] = unidecode.unidecode(last_activity).strip('\n ')
        items['last_updated'] = calendar.timegm(time.gmtime())
        items['total_solved'] = response.xpath('(//h3[contains(., "Progress")])[1]/../../ul/li[1]/span/text()').get().strip('\n ')
        yield items
