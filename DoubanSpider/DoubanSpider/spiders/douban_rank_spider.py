#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from scrapy import Request
from scrapy.spiders import Spider
from DoubanSpider.items import DoubanRankItem


class DoubanRankSpider(Spider):
    name = 'douban_rank'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
    }

    def start_requests(self):
        url = "https://movie.douban.com/top250"
        yield Request(url, headers=self.headers)

    def parse(self, response):

        movies = response.xpath('//ol[@class="grid_view"]/li')
        item = DoubanRankItem()
        for movie in movies:
            item['ranking'] = movie.xpath(
                './/div[@class="pic"]/em/text()'
            ).extract()[0]
            item['movie_name'] = movie.xpath(
                './/span[@class="title"]/text()'
            ).extract()[0]
            item['score'] = movie.xpath(
                './/span[@class="rating_num"]/text()'
            ).extract()[0]
            item['score_num'] = movie.xpath(
                './/div[@class="star"]/span/text()'
            ).re('(\d+)人评价')
            yield item

        next_url = response.xpath('//span[@class="next"]/a/@href').extract()

        if next_url:
            next_url = 'https://movie.douban.com/top250' + next_url[0]
            yield Request(next_url, headers=self.headers)