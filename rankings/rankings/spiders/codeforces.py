import scrapy
import json
import calendar
import time
from ..items import CodeforcesItem

class CodeforcesSpider(scrapy.Spider):
    name = 'codeforces'
    start_urls = [
        'https://codeforces.com/api/user.info?handles=codernavi18'
    ]

    def parse(self, response):
        items = CodeforcesItem()
        res = json.loads(response.text)
        items['rating'] = res['result'][0]['rating']
        items['best_rating'] = res['result'][0]['maxRating']
        items['global_rank'] = 0
        items['country_rank'] = 0
        items['last_activity'] = res['result'][0]['lastOnlineTimeSeconds']
        items['last_updated'] = calendar.timegm(time.gmtime())
        items['rank'] = res['result'][0]['rank']
        items['max_rank'] = res['result'][0]['maxRank']
        yield items
