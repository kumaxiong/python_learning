#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from scrapy.spiders import Spider
from scrapy import Request
from DoubanSpider.items import DoubanContentItem


class DoubanMovieTop250Spider(Spider):
    name = 'douban_tag'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
    }

    def start_requests(self):
        url = "https://movie.douban.com/top250"
        yield Request(url, headers=self.headers)

    def parse(self, response):
        movies = response.xpath('//ol[@class="grid_view"]/li')

        for movie in movies:
            link = movie.xpath('.//a/@href').extract()[0]
            yield Request(link,headers=self.headers, callback=self.parse_content)

        next_url = response.xpath('//span[@class="next"]/a/@href').extract()

        if next_url:
            next_url = 'https://movie.douban.com/top250' + next_url[0]
            yield Request(next_url, headers=self.headers)

    def parse_content(self, response):
        movie_name = response.xpath('//h1/span/text()').extract()[0]
        movie_tags = response.xpath('//div[@class="tags-body"]/a/text()').extract()
        item = DoubanContentItem()
        item['movie_name'] = movie_name
        item['movie_tags'] = movie_tags
        yield item
