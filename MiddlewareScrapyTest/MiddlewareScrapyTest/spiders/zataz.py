# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request


class ZatazSpider(scrapy.Spider):
    name = "zataz"

    def start_requests(self):
        for i in list(range(1, 118)):
            url = 'https://eromang.zataz.com/page/' + str(i) + '/'
            url = str(url)
            request = Request(url)
            request.meta['name'] = 'zataz'
            yield request

    def parse(self, response):
        articles = response.xpath('//article').extract()
        print(len(articles))
