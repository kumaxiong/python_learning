# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request

class MicroSpider(scrapy.Spider):
    name = "micro"

    def start_requests(self):
        url = 'https://cloudblogs.microsoft.com/microsoftsecure/?product=windows,windows-defender-advanced-threat-protection'
        request = Request(url)
        request.meta['js'] = True
        yield request

    def parse(self, response):
        titles = response.xpath('//h2[@class="entry-title"]/a/text()').extract()
        print(len(titles))
        print(titles)

