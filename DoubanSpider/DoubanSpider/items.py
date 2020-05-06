# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class DoubanRankItem(scrapy.Item):
    ranking = scrapy.Field()
    movie_name = scrapy.Field()
    score = scrapy.Field()
    score_num = scrapy.Field()


class DoubanContentItem(scrapy.Item):
    movie_name = scrapy.Field()
    movie_tags = scrapy.Field()


class BudejieItem(scrapy.Item):
    href = scrapy.Field()
    text = scrapy.Field()
