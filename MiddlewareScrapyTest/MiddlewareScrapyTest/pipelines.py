# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


import pymongo


class MongoPipeline(object):
    def __init__(self):
        client = pymongo.MongoClient(host='127.0.0.1', port=27017)
        db = client["mydb"]
        self.douban250_col = db['redis_test']

    def process_item(self, item, spider):
        hasdata = self.douban250_col.find_one({'url': item['url']})
        if hasdata is None:
            self.douban250_col.insert(dict(item))
        return item

    def close_spider(self, spider):
        pass