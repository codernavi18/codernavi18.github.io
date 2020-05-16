# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CodechefItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    rating = scrapy.Field()
    best_rating = scrapy.Field()
    global_rank = scrapy.Field()
    country_rank = scrapy.Field()
    last_updated = scrapy.Field()
    last_activity = scrapy.Field()
    pass

class CodeforcesItem(scrapy.Item):
    rating = scrapy.Field()
    best_rating = scrapy.Field()
    global_rank = scrapy.Field()
    country_rank = scrapy.Field()
    last_activity = scrapy.Field()
    last_updated = scrapy.Field()
    rank = scrapy.Field()
    max_rank = scrapy.Field()
    pass

class UVaItem(scrapy.Item):
    global_rank = scrapy.Field()
    last_updated = scrapy.Field()
    last_activity = scrapy.Field()
    total_solved = scrapy.Field()
    past2d_solved = scrapy.Field()
    past7d_solved = scrapy.Field()
    past31d_solved = scrapy.Field()
    past3m_solved = scrapy.Field()
    past1y_solved = scrapy.Field()

class LeetcodeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    rating = scrapy.Field()
    contests_participated = scrapy.Field()
    global_rank = scrapy.Field()
    last_activity = scrapy.Field()
    last_updated = scrapy.Field()
    total_solved = scrapy.Field()
    pass

class AtcoderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    rating = scrapy.Field()
    best_rating = scrapy.Field()
    rank = scrapy.Field()
    contests_participated = scrapy.Field()
    last_activity = scrapy.Field()
    last_updated = scrapy.Field()
    pass
