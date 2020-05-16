import scrapy
import json
import calendar
import time
from ..items import UVaItem

class UVaSpider(scrapy.Spider):
    name = 'uva'
    start_urls = [
        'https://uhunt.onlinejudge.org/api/ranklist/754856/0/0'
    ]

    def parse(self, response):
        items = UVaItem()
        res = json.loads(response.text)
        items['global_rank'] = res[0]['rank']
        items['last_updated'] = calendar.timegm(time.gmtime())
        items['last_activity'] = 0
        items['total_solved'] = res[0]['ac']
        items['past2d_solved'] = res[0]['activity'][0]
        items['past7d_solved'] = res[0]['activity'][1]
        items['past31d_solved'] = res[0]['activity'][2]
        items['past3m_solved'] = res[0]['activity'][3]
        items['past1y_solved'] = res[0]['activity'][4]
        yield items
