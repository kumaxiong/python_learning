# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html
import time
from scrapy import signals
from scrapy.http import HtmlResponse
from selenium import webdriver


class MiddlewarescrapytestSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class AjaxDownloadMiddleware(object):

    def __init__(self):
        super(AjaxDownloadMiddleware, self).__init__()
        self.driver = webdriver.Firefox()

    def __del__(self):
        super(AjaxDownloadMiddleware, self).__del__()
        self.driver.quit()

    def process_request(self, request, spider):
        # 如果请求被我们的爬虫标志了ajax，则使用phantomjs渲染页面
        if request.meta['js']:
            self.driver.get(request.url)
            times = 1
            while times <= 13:
                self.driver.find_element_by_id("js-home-load-more").click()
                times = times + 1
                time.sleep(3)
            # 等待页面渲染，直至分页组件显示出来
            # webdriver.support.ui.WebDriverWait(self.driver, 1).until(
            #     lambda x: x.find_element_by_id("list_paginator"))  # 设置最多1秒等待，等至页面显示 `#list_paginator` 分页组件
            content = self.driver.page_source.encode('utf-8', 'ignore')
            return HtmlResponse(request.url, status=200, body=content)  # 返回ajax渲染结果页面
        else:
            return None  # 返回None将request交由scrapy继续处理


class ZatazDownloadMiddleware(object):

    def __init__(self):
        super(ZatazDownloadMiddleware, self).__init__()
        # 设置火狐浏览器无头模式
        options = webdriver.FirefoxOptions()
        options.add_argument('-headless')
        self.driver = webdriver.Firefox(options=options)
        self.first = False

    def __del__(self):
        super(ZatazDownloadMiddleware, self).__del__()
        self.driver.quit()

    def process_request(self, request, spider):
        first_url = request.url
        # 如果请求被我们的爬虫标志了ajax，则使用phantomjs渲染页面
        if request.meta['name'] == 'zataz':
            if not self.first:
                self.first = True
                self.driver.get(request.url)
                times = 1
                while True:
                    time.sleep(5)
                    times = times + 1
                    if first_url != self.driver.current_url:
                        first_url = self.driver.current_url
                        break
                    if times == 10:
                        break

            self.driver.get(first_url)
            # 等待页面渲染，直至分页组件显示出来
            # webdriver.support.ui.WebDriverWait(self.driver, 1).until(
            #     lambda x: x.find_element_by_id("list_paginator"))  # 设置最多1秒等待，等至页面显示 `#list_paginator` 分页组件
            content = self.driver.page_source.encode('utf-8', 'ignore')

            return HtmlResponse(request.url, status=200, body=content)  # 返回ajax渲染结果页面
        else:
            return None  # 返回None将request交由scrapy继续处理