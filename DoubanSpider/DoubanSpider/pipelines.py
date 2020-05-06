# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
import pymysql

'''
豆瓣top250
'''


class RankPipeline(object):
    quotes_name = 'quotes'
    author_name = 'author'

    def __init__(self, settings):
        self.settings = settings

    def process_item(self, item, spider):
        print(item)
        if spider.name == "douban_rank":
            sql = "insert into doubanrank(movie_name,rank,score,score_num) values(%s,%s,%s,%s)"
            # 执行sql语句
            self.cursor.execute(sql, (item['movie_name'], item['ranking'], item['score'], item['score_num']))
        elif spider.name == "author":
            pass
            # sqltext = self.authorInsert.format(
            #     name=pymysql.escape_string(item['name']),
            #     birthdate=pymysql.escape_string(item['birthdate']),
            #     bio=pymysql.escape_string(item['bio']))
            # self.cursor.execute(sqltext)
        else:
            spider.log('Undefined name: %s' % spider.name)

        return item

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings)

    def open_spider(self, spider):
        # 连接数据库
        self.connect = pymysql.connect(
            host=self.settings.get('MYSQL_HOST'),
            port=self.settings.get('MYSQL_PORT'),
            db=self.settings.get('MYSQL_DBNAME'),
            user=self.settings.get('MYSQL_USER'),
            passwd=self.settings.get('MYSQL_PASSWD'),
            charset='utf8',
            use_unicode=True)

        # 通过cursor执行增删查改
        self.cursor = self.connect.cursor()
        self.connect.autocommit(True)

    def close_spider(self, spider):
        self.cursor.close()
        self.connect.close()


# '''
# 豆瓣Top250 的爬虫Item Pipeline  mongodb
# '''
#
#
# class Douban250Pipeline(object):
#     def __init__(self):
#         client = pymongo.MongoClient(host='127.0.0.1', port=27017)
#         db = client["mydb"]
#         self.douban250_col = db['crawl_test']
#
#     def process_item(self, item, spider):
#         self.douban250_col.insert(dict(item))
#         return item
#
#     def close_spider(self, spider):
#         pass

import json
import codecs
class StackJsonPipeline:

    # 初始化时指定要操作的文件
    def __init__(self):
        self.file = codecs.open('questions.json', 'w', encoding='utf-8')
        self.read = codecs.open("hello.txt", "r")
        print(self.read)


    # 存储数据，将 Item 实例作为 json 数据写入到文件中
    def process_item(self, item, spider):
        lines = json.dumps(dict(item), ensure_ascii=False) + '\n'
        self.file.write(lines)
        return item
    # 处理结束后关闭 文件 IO 流
    def close_spider(self, spider):
        self.file.close()