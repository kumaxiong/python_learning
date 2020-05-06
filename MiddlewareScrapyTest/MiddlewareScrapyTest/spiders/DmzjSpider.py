#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from scrapy.spiders import Rule, Request
from scrapy.linkextractors import LinkExtractor
from MiddlewareScrapyTest.items import ManhuaItem
from scrapy_redis.spiders import RedisCrawlSpider


class DmzjSpider(RedisCrawlSpider):
    name = 'dmzj'
    allowed_domains = ['manhua.dmzj.com']
    redis_key = 'test_urls'
    # start_urls = ['https://manhua.dmzj.com/chuzhongxuelilaodongzhekaishidegaozhongshenghuo/']

    rules = [
        Rule(LinkExtractor(allow=(r'\D+/'), deny=(r'.*.shtml', r'.*.xml')), callback='parse_item', follow=True)
    ]

    def parse_link(self, response):
        print(response.url)

    def parse_item(self, response):
        name = response.xpath('//span[@class="anim_title_text"]/a/h1/text()').extract()[0]
        texts = response.xpath('//div[@class="line_height_content"]/text()').extract()
        dec = ''
        for i in texts:
            dec += i
        item = ManhuaItem()
        item['name'] = name
        item['dec'] = dec.strip()
        item['url'] = response.url
        yield item
